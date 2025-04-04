# Copyright 2024 The jax_triton Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Edited in EasyDeL For caching kernels which doesn't work in jax-triton version
"""Module for calling Triton kernels from JAX."""

from __future__ import annotations

import copy
import dataclasses
import functools
import hashlib
import inspect
import os
import pickle
import pprint
import tempfile
import types
import zlib
from collections.abc import Callable, Sequence
from pathlib import Path
from typing import TYPE_CHECKING, Any, List, Protocol, Union

import jax
import jax.dlpack
import jax.numpy as jnp
import numpy as np
from jax import tree_util
from jax._src import core, state, util
from jax._src.lib import gpu_triton as triton_kernel_call_lib
from jax._src.lib.mlir import ir
from jax.interpreters import mlir, xla

CAN_USE_TRITON = False
try:
	import triton
	import triton._C.libtriton as _triton
	import triton.backends.nvidia.compiler as cb
	import triton.language as tl
	from triton.compiler import code_generator as code_gen
	from triton.compiler import compiler as tc
	from triton.runtime import autotuner

	CAN_USE_TRITON = True
except ModuleNotFoundError:
	pass

try:
	import triton.backends.amd.compiler as hb
except ImportError:
	hb = None
	pass

if TYPE_CHECKING:
	from triton import JITFunction
else:
	JITFunction = Any


def get_cache_dir() -> Path:
	home_dir = Path.home()
	app_name = "triton-compiled-kernels"
	if os.name == "nt":  # Windows
		cache_dir = (
			Path(os.getenv("LOCALAPPDATA", home_dir / "AppData" / "Local")) / app_name
		)
	elif os.name == "posix":  # Linux and macOS
		if "darwin" in os.sys.platform:  # macOS
			cache_dir = home_dir / "Library" / "Caches" / app_name
		else:  # Linux
			cache_dir = home_dir / ".cache" / app_name
	else:
		cache_dir = home_dir / ".cache" / app_name
	cache_dir.mkdir(parents=True, exist_ok=True)
	return cache_dir


_JAX_TRITON_DUMP_DIR = Path(os.environ.get("JAX_TRITON_DUMP_DIR", get_cache_dir()))
_CACHE_TRITON_KERNELS = os.environ.get("CACHE_TRITON_KERNELS", "true") in [
	"1",
	"on",
	"true",
	"yes",
]
map, unsafe_map = util.safe_map, map
zip, unsafe_zip = util.safe_zip, zip


_JAX_TO_TRITON_TYPE_MAP = {
	jnp.dtype("bfloat16"): "bf16",
	jnp.dtype("float64"): "fp64",
	jnp.dtype("float32"): "fp32",
	jnp.dtype("float16"): "fp16",
	jnp.dtype("float8_e4m3fn"): "fp8e4nv",
	jnp.dtype("float8_e5m2"): "fp8e5",
	jnp.dtype("float8_e4m3fnuz"): "fp8e4b8",
	jnp.dtype("float8_e5m2fnuz"): "fp8e5b16",
	jnp.dtype("int64"): "i64",
	jnp.dtype("int32"): "i32",
	jnp.dtype("int16"): "i16",
	jnp.dtype("int8"): "i8",
	jnp.dtype("uint64"): "u64",
	jnp.dtype("uint32"): "u32",
	jnp.dtype("uint16"): "u16",
	jnp.dtype("uint8"): "u8",
	# Triton defines a 'B' type, which is an alias for both i1 and bool.
	jnp.dtype("bool"): "B",
}

Grid = Union[int, tuple[int], tuple[int, int], tuple[int, int, int]]
GridOrLambda = Union[Grid, Callable[[dict[str, Any]], Grid]]


def normalize_grid(grid: GridOrLambda, metaparams) -> tuple[int, int, int]:
	if callable(grid):
		grid = grid(metaparams)
	if isinstance(grid, int):
		grid = (grid,)
	elif len(grid) > 3:
		raise ValueError("`grid` should have three or fewer dimensions.")
	return tuple(grid) + (1,) * (3 - len(grid))


def avals_to_layouts(avals):
	return [list(reversed(range(aval.ndim))) for aval in avals]


def get_triton_type(obj: Any) -> str:
	if isinstance(obj, (jax.core.ShapedArray, state.AbstractRef)):
		return f"*{_JAX_TO_TRITON_TYPE_MAP[obj.dtype]}"
	if isinstance(obj, tl.constexpr):
		obj = obj.value
	if isinstance(obj, int):
		if -(2**31) <= obj < 2**31:
			return "i32"
		elif 2**31 <= obj < 2**32:
			return "u32"
		elif -(2**63) <= obj < 2**63:
			return "i64"
		elif 2**63 <= obj < 2**64:
			return "u64"
		else:
			raise ValueError(f"integer overflow representing {obj}")
	if isinstance(obj, float):
		return "fp32"
	if isinstance(obj, np.float32):
		return "fp32"
	if isinstance(obj, bool):
		return "B"
	if isinstance(obj, str):
		return "str"
	raise NotImplementedError(f"could not compute type name for {obj}: {type(obj)}")


triton_kernel_call_p = jax.core.Primitive("triton_kernel_call")
triton_kernel_call_p.multiple_results = True
triton_kernel_call_p.def_impl(
	functools.partial(xla.apply_primitive, triton_kernel_call_p)
)


@triton_kernel_call_p.def_abstract_eval
def triton_kernel_call_abstract_eval(*_, out_shapes, **__):
	return [
		core.ShapedArray(out_shape.shape, out_shape.dtype) for out_shape in out_shapes
	]


def aval_size_bytes(aval):
	return np.dtype(aval.dtype).itemsize * aval.size


def get_cuda_backend(device, compute_capability):
	target = cb.GPUTarget("cuda", compute_capability, 32)
	backend = cb.CUDABackend(target)
	return backend


def get_hip_backend(device, compute_capability):
	arch = triton_kernel_call_lib.get_arch_details(device)
	arch = arch.split(":")[0]
	target = hb.GPUTarget("hip", arch, 64)
	backend = hb.HIPBackend(target)
	return backend


@dataclasses.dataclass
class CompilationResult:
	binary: str
	name: str
	shared_mem_bytes: int
	cluster_dims: tuple
	ttgir: str | None
	llir: str | None


def compile_ttir_inplace(
	ttir,
	backend: List[Union[cb.CUDABackend, hb.HIPBackend]],  # type:ignore
	options: List[Union[cb.CUDAOptions, hb.HIPOptions]],  # type:ignore
	compute_capability,
	platform,
):
	if platform == "cuda":
		return compile_ttir_to_ptx_inplace(
			ttir,
			backend,
			options,
			compute_capability,
		)

	elif platform == "rocm":
		return compile_ttir_to_hsaco_inplace(
			ttir,
			backend,
			options,
			compute_capability,
		)
	else:
		raise ValueError("Unsupported device.")


def compile_ttir_to_ptx_inplace(
	ttir,
	cuda_backend: cb.CUDABackend,
	cuda_options: cb.CUDAOptions,
	compute_capability,
) -> CompilationResult:
	if cuda_options.debug:
		print(ttir)
	try:
		metadata = {}
		opt_ttir = cuda_backend.make_ttir(ttir, metadata, cuda_options)
		ttgir = cuda_backend.make_ttgir(
			opt_ttir,
			metadata,
			cuda_options,
			compute_capability,
		)
	except RuntimeError as e:
		ttir.dump()
		raise ValueError("TTIR->TTGIR pass failed!") from e
	if cuda_options.debug:
		print(ttgir)
	try:
		llir = cuda_backend.make_llir(
			ttgir,
			metadata,
			cuda_options,
			compute_capability,
		)
	except RuntimeError as e:
		ttgir.dump()
		raise ValueError("TTGIR->LLIR pass failed!") from e
	shared_mem_bytes = metadata["shared"]
	if cuda_options.debug:
		print(llir)
	ptx = cuda_backend.make_ptx(
		llir,
		metadata,
		cuda_options,
		compute_capability,
	)
	if cuda_options.debug:
		print(ptx)
	name = metadata["name"]
	cluster_dims = metadata["cluster_dims"]
	ttgir = str(ttgir)
	llir = str(llir)
	return CompilationResult(
		binary=ptx,
		name=name,
		shared_mem_bytes=shared_mem_bytes,
		cluster_dims=cluster_dims,
		ttgir=ttgir,
		llir=llir,
	)


def compile_ttir_to_hsaco_inplace(
	ttir,
	hip_backend: hb.HIPBackend,  # type:ignore
	hip_options: hb.HIPOptions,  # type:ignore
	compute_capability,
) -> CompilationResult:
	if hip_options.debug:
		print(ttir)
	try:
		metadata = {}
		opt_ttir = hip_backend.make_ttir(ttir, metadata, hip_options)
		ttgir = hip_backend.make_ttgir(opt_ttir, metadata, hip_options)
	except RuntimeError as e:
		ttir.dump()
		raise ValueError("TTIR->TTGIR pass failed!") from e
	if hip_options.debug:
		print(ttgir)
	try:
		llir = hip_backend.make_llir(ttgir, metadata, hip_options)
	except RuntimeError as e:
		ttgir.dump()
		raise ValueError("TTGIR->LLIR pass failed!") from e
	shared_mem_bytes = metadata["shared"]
	if hip_options.debug:
		print(llir)

	amdgcn = hip_backend.make_amdgcn(llir, metadata, hip_options)
	hsaco = hip_backend.make_hsaco(amdgcn, metadata, hip_options)

	name = metadata["name"]
	ttgir = str(ttgir)
	llir = str(llir)
	cluster_dims = (0, 0, 0)
	fd, hsaco_path = tempfile.mkstemp()
	with os.fdopen(fd, "wb") as f:
		f.write(hsaco)
	return CompilationResult(
		binary=hsaco_path,
		name=name,
		shared_mem_bytes=shared_mem_bytes,
		cluster_dims=cluster_dims,
		ttgir=ttgir,
		llir=llir,
	)


def cdiv(a: int | jax.Array, b: int | jax.Array) -> int | jax.Array:
	if isinstance(a, int) and isinstance(b, int):
		return (a + b - 1) // b
	return jax.lax.div(a + b - 1, b)


def strides_from_shape(shape: tuple[int, ...]) -> tuple[int, ...]:
	size = np.prod(shape)
	strides = []
	for s in shape:
		size = size // s
		strides.append(int(size))
	return tuple(strides)


def next_power_of_2(x: int) -> int:
	"""Returns the next power of two greater than or equal to `x`."""
	if x < 0:
		raise ValueError("`next_power_of_2` requires a non-negative integer.")
	return 1 if x == 0 else 2 ** (x - 1).bit_length()


_COMPILED_KERNEL_CACHE = {}


def get_or_create_triton_kernel(
	backend_init_func,
	platform,
	fn: JITFunction,
	arg_dtypes,
	scalar_args,
	device,
	*,
	num_warps,
	num_stages,
	num_ctas,
	compute_capability,
	enable_fp_fusion,
	metaparams,
	dump: bool,
) -> tuple[triton_kernel_call_lib.TritonKernel, Any]:  # type:ignore
	if num_warps is None:
		num_warps = 4
	if num_stages is None:
		num_stages = 3
	if compute_capability is None:
		compute_capability = triton_kernel_call_lib.get_compute_capability(device)
	if num_ctas > 1 and compute_capability < 90:
		raise ValueError("num_ctas > 1 unsupported before Hopper.")

	signature = {fn.arg_names[i]: v for i, v in enumerate(arg_dtypes)}
	mock_torch_tensor = types.SimpleNamespace(data_ptr=lambda: 16)
	args_for_specialization_attr = [mock_torch_tensor] * len(arg_dtypes)
	backend = backend_init_func(device, compute_capability)
	for i, _, v in scalar_args:
		args_for_specialization_attr[i] = v
 
	specialization_attr = backend.get_attrs_descriptor(
		fn.params[: len(args_for_specialization_attr)], args_for_specialization_attr
	)
	# pylint: disable=protected-access
	constants = dict(metaparams)
	constants.update({k: None for _, k, v in scalar_args if v is None})
	constants.update({fn.arg_names[i]: 1 for i in specialization_attr.equal_to_1})
	cache_key = (
		fn,
		tuple(signature.items()),
		tuple(specialization_attr.get_fn_attrs()),
		tuple(constants.items()),
		num_warps,
		num_stages,
		num_ctas,
		compute_capability,
		enable_fp_fusion,
	)

	kernel = _COMPILED_KERNEL_CACHE.get(cache_key)
	if kernel is not None:
		return kernel, specialization_attr
	kernel_hash = hashlib.sha256(str(cache_key).encode("utf-8")).hexdigest()

	if not Path(_JAX_TRITON_DUMP_DIR / kernel_hash).exists():
		if _CACHE_TRITON_KERNELS:
			os.makedirs(f"{_JAX_TRITON_DUMP_DIR}/{kernel_hash}")
			with open(f"{_JAX_TRITON_DUMP_DIR}/{kernel_hash}/config", "w") as f:
				pprint.pprint(cache_key, stream=f)
		opts = {
			"num_warps": num_warps,
			"num_stages": num_stages,
			"num_ctas": num_ctas,
			"optimize_epilogue": False,
			"debug": dump,
			"enable_fp_fusion": enable_fp_fusion,
		}
		options = backend.parse_options(opts)

		context = _triton.ir.context()
		_triton.ir.load_dialects(context)
		backend.load_dialects(context)
		codegen_fns = backend.get_codegen_implementation()

		module = (
			code_gen.ast_to_ttir(
				fn,
				specialization=tc.ASTSource(
					fn,
					constants=constants,
					signature=signature,
					attrs=specialization_attr,
				),
				options=options,
				codegen_fns=codegen_fns,
				context=context,
				module_map=backend.get_module_map(),
			)
			if "module_map" in inspect.getfullargspec(code_gen.ast_to_ttir).args
			else code_gen.ast_to_ttir(
				fn,
				specialization=tc.ASTSource(
					fn,
					constants=constants,
					signature=signature,
					attrs=specialization_attr,
				),
				options=options,
				codegen_fns=codegen_fns,
				context=context,
			)
		)
		ttir = str(module)

		compilation_result = compile_ttir_inplace(
			module,
			backend,
			options,
			compute_capability,
			platform,
		)
		kernel_name = compilation_result.name
		if _CACHE_TRITON_KERNELS:
			(_JAX_TRITON_DUMP_DIR / kernel_hash).mkdir(parents=True, exist_ok=True)
			with open(
				_JAX_TRITON_DUMP_DIR / kernel_hash / "compilation_result",
				"wb",
			) as buffer:
				pickle.dump((compilation_result, ttir, kernel_name), buffer)

		kernel = triton_kernel_call_lib.TritonKernel(
			kernel_name,
			num_warps,
			compilation_result.shared_mem_bytes,
			compilation_result.binary,
			ttir,
			compute_capability,
			*compilation_result.cluster_dims,
		)

		_COMPILED_KERNEL_CACHE[cache_key] = kernel
	elif Path(_JAX_TRITON_DUMP_DIR / kernel_hash).exists():
		compilation_result, ttir, kernel_name = pickle.load(
			open(
				_JAX_TRITON_DUMP_DIR / kernel_hash / "compilation_result",
				"rb",
			)
		)
		kernel = triton_kernel_call_lib.TritonKernel(
			kernel_name,
			num_warps,
			compilation_result.shared_mem_bytes,
			compilation_result.binary,
			ttir,
			compute_capability,
			*compilation_result.cluster_dims,
		)

	return kernel, specialization_attr


def triton_kernel_call_lowering(
	backend_init_func,
	ctx,
	*array_args,
	fn,
	scalar_args,
	name,
	custom_call_target_name,
	out_shapes,
	grid,
	num_warps,
	num_stages,
	num_ctas,
	compute_capability,
	enable_fp_fusion,
	input_output_aliases,
	zeroed_outputs,
	debug,
	serialized_metadata,
	device,
	**metaparams,
):
	kernel_call_name = name
	args = list(ctx.avals_in)
	arg_dtypes = list(map(get_triton_type, ctx.avals_in))
	for idx, dtype, v in scalar_args:
		args.insert(idx, v)
		arg_dtypes.insert(idx, dtype)
	args.extend(ctx.avals_out)
	arg_dtypes.extend(map(get_triton_type, ctx.avals_out))
	named_args = dict(unsafe_zip(fn.arg_names, args))

	if isinstance(fn, autotuner.Autotuner):
		prev_early_config_prune_fn = fn.early_config_prune

		def prune_configs(configs, named_args, **kwargs):
			pruned_configs = []
			for config in configs:
				if config.pre_hook is not None:
					raise NotImplementedError("`pre_hook` is not supported")

				if all(config.kwargs.get(k, v) == v for k, v in metaparams.items()):
					pruned_configs.append(config)
			if prev_early_config_prune_fn is not None:
				pruned_configs = prev_early_config_prune_fn(pruned_configs, named_args)
			return pruned_configs

		fn.early_config_prune = prune_configs
		fn.nargs = named_args
		configs = fn.prune_configs(metaparams)
		fn = fn.fn
	else:
		config = triton.Config(
			{},
			num_warps=num_warps,
			num_stages=num_stages,
			num_ctas=num_ctas,
		)
		configs = [config]

	if isinstance(fn, autotuner.Heuristics):
		updated_configs = []
		for config in configs:
			kwargs = config.kwargs.copy()
			for name, heuristic in fn.values.items():
				kwargs[name] = heuristic({**named_args, **metaparams, **kwargs})
			updated_config = copy.copy(config)
			updated_config.kwargs = kwargs
			updated_configs.append(updated_config)
		configs = updated_configs
		fn = fn.fn

	if not isinstance(fn, triton.JITFunction):
		raise ValueError(
			"`kernel` must be a Triton `JITFunction`, `Heuristics` or `Autotuner`."
		)

	outputs_offset = len(ctx.avals_in) + len(scalar_args)
	config_params = []
	for config in configs:
		config_metaparams = {**metaparams, **config.kwargs}
		config_grid = normalize_grid(grid, config_metaparams)

		config_zeroed_outputs = zeroed_outputs
		if callable(zeroed_outputs):
			config_zeroed_outputs = config_zeroed_outputs(config_metaparams)

		zeroed_params_with_sizes = {
			i + outputs_offset: aval_size_bytes(ctx.avals_out[i])
			for i in sorted(config_zeroed_outputs)
		}

		config_params.append(
			dict(
				metaparams=tuple(sorted(config_metaparams.items())),
				num_warps=config.num_warps,
				num_stages=config.num_stages,
				num_ctas=config.num_ctas,
				grid=config_grid,
				zeroed_params_with_sizes=tuple(zeroed_params_with_sizes.items()),
			)
		)

	kernel_calls = []
	for params in config_params:
		kernel, specialization_attr = get_or_create_triton_kernel(
			backend_init_func,
			ctx.module_context.platforms[0],
			fn,
			arg_dtypes,
			scalar_args,
			device,
			num_warps=params["num_warps"],
			num_stages=params["num_stages"],
			num_ctas=params["num_ctas"],
			compute_capability=compute_capability,
			enable_fp_fusion=enable_fp_fusion,
			metaparams=dict(params["metaparams"]),
			dump=debug,
		)

		kernel_params = []
		zeroed_params_with_sizes = dict(params["zeroed_params_with_sizes"])
		for i, (arg, dtype) in enumerate(zip(args, arg_dtypes)):
			if isinstance(arg, core.ShapedArray):
				kernel_params.append(
					triton_kernel_call_lib.create_array_parameter(
						zeroed_params_with_sizes.get(i, 0),
						16 if (i in specialization_attr.divisibility_16) else 0,
					)
				)
			elif i not in specialization_attr.equal_to_1:
				kernel_params.append(triton_kernel_call_lib.create_scalar_parameter(arg, dtype))

		kernel_calls.append(
			triton_kernel_call_lib.TritonKernelCall(
				kernel,
				params["grid"][0],
				params["grid"][1],
				params["grid"][2],
				kernel_params,
			)
		)

	if len(kernel_calls) > 1:
		named_scalar_args = {fn.arg_names[i]: v for i, _, v in scalar_args}
		input_output_aliases_with_sizes = tuple(
			(input_idx, output_idx, aval_size_bytes(ctx.avals_in[input_idx]))
			for input_idx, output_idx in input_output_aliases
		)
		kernel_call = triton_kernel_call_lib.TritonAutotunedKernelCall(
			f"{kernel_call_name} ({fn.fn.__name__}) {named_scalar_args}",
			[(call, str(config)) for call, config in zip(kernel_calls, configs)],
			input_output_aliases_with_sizes,
		)
	else:
		kernel_call = kernel_calls[0]

	out_types = [
		ir.RankedTensorType.get(shape.shape, mlir.dtype_to_ir_type(shape.dtype))
		for shape in out_shapes
	]
	call_proto = kernel_call.to_proto(kernel_call_name, serialized_metadata)
	return mlir.custom_call(
		call_target_name=custom_call_target_name,
		result_types=out_types,
		operands=array_args,
		backend_config=zlib.compress(call_proto),
		operand_layouts=avals_to_layouts(ctx.avals_in),
		result_layouts=avals_to_layouts(ctx.avals_out),
		operand_output_aliases=dict(input_output_aliases),
	).results


mlir.register_lowering(
	triton_kernel_call_p,
	functools.partial(triton_kernel_call_lowering, get_cuda_backend),
	platform="cuda",
)

mlir.register_lowering(
	triton_kernel_call_p,
	functools.partial(triton_kernel_call_lowering, get_hip_backend),
	platform="rocm",
)


class ShapeDtype(Protocol):
	@property
	def shape(self) -> tuple[int, ...]: ...

	@property
	def dtype(self) -> np.dtype: ...


def triton_call(
	*args: jax.Array | bool | int | float | np.float32,
	kernel: triton.JITFunction,
	out_shape: ShapeDtype | Sequence[ShapeDtype],
	grid: GridOrLambda,
	name: str = "",
	custom_call_target_name: str = "triton_kernel_call",
	num_warps: int | None = None,
	num_stages: int | None = None,
	num_ctas: int = 1,
	compute_capability: int | None = None,
	enable_fp_fusion: bool = True,
	input_output_aliases: dict[int, int] | None = None,
	zeroed_outputs: (Sequence[int] | Callable[[dict[str, Any]], Sequence[int]]) = (),
	debug: bool = False,
	serialized_metadata: bytes = b"",
	device: int = 0,
	**metaparams: Any,
) -> Any:
	"""Calls a Triton kernel with `jax.Array` arguments.
	Args:
	  *args: Inputs for the Triton kernel.
	  kernel: A Triton kernel (e.g. a function decorated with `triton.jit`). All
	    static values should be annotated with `triton.language.constexpr`.
	  out_shape: A `jax.ShapeDtypeStruct` (or something that has `.shape` and
	    `.dtype` attributes) or a sequence thereof that specify the output(s) of
	    the kernel. Pointers for each of the `jax.ShapeDtypeStruct`s in
	    `out_shape` will be passed into `kernel` following the input parameters.
	  grid: An integer, tuple of up to 3 integers, or a function that returns a
	    tuple of up to 3 integers. When `grid` is an integer, `kernel` is
	    invocated in `grid`-many parallel executions. When `grid` is a sequence of
	    integers, `kernel` is launched in a `prod(grid)`-many parallel execution.
	    When `grid` is a function, it is passed `**metaparams` and should return a
	    tuple of up to 3 integers.
	  input_output_aliases: A dictionary mapping input argument indices to output
	    indices. Providing a mapping will alias the corresponding buffers.
	  zeroed_outputs: A sequence of indices, or a function returning a sequence of
	    indices, for outputs that should be zeroed before the kernel is launched.
	  num_warps: The number of warps used to execute the Triton kernel.
	  num_stages: The number of stages emitted by the Triton compiler.
	  num_ctas: The size of thread blocks per cluster to be used on GPUs with
	    compute capabilities >= 9.0. It must be less or equal to 8.
	  debug: Prints out intermediate IRs if True for debugging purposes.
	  serialized_metadata: Arbitrary metadata that will be added into the
	    serialized kernel call.
	  device (int): device id in current process to compile triton kernel on
	  **metaparams: Additional keyword arguments that will be provided to a `grid`
	    (if it is a function) and to the Triton kernel as `constexpr` arguments.

	Returns:
	  Outputs from the Triton kernel.
	"""
	if not CAN_USE_TRITON:
		raise ValueError("`triton_call` is only available when `triton` is installed.")
	out_shape = tree_util.tree_map(
		lambda a: jax.ShapeDtypeStruct(a.shape, a.dtype), out_shape
	)
	flat_args, _ = tree_util.tree_flatten(args)
	flat_out_shapes, out_tree = tree_util.tree_flatten(out_shape)
	array_args = []
	scalar_args = []
	for i, arg in enumerate(flat_args):
		if isinstance(arg, (bool, int, float)):
			scalar_args.append((i, get_triton_type(arg), arg))
		elif isinstance(arg, np.float32):
			scalar_args.append((i, get_triton_type(arg), float(arg)))
		else:
			array_args.append(arg)
	if input_output_aliases is None:
		input_output_aliases = {}
	out_flat = triton_kernel_call_p.bind(
		*array_args,
		fn=kernel,
		scalar_args=tuple(scalar_args),
		name=name,
		custom_call_target_name=custom_call_target_name,
		out_shapes=tuple(flat_out_shapes),
		grid=grid,
		num_warps=num_warps,
		num_stages=num_stages,
		num_ctas=num_ctas,
		compute_capability=compute_capability,
		enable_fp_fusion=enable_fp_fusion,
		input_output_aliases=tuple(input_output_aliases.items()),
		zeroed_outputs=zeroed_outputs,
		debug=debug,
		serialized_metadata=serialized_metadata,
		device=device,
		**metaparams,
	)
	return tree_util.tree_unflatten(out_tree, out_flat)
