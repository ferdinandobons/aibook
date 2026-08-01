from __future__ import annotations

import math
from typing import Any

import torch


DTYPES = (
    torch.float16,
    torch.bfloat16,
    torch.float32,
    torch.float64,
)


def dtype_summary(dtype: torch.dtype) -> dict[str, Any]:
    info = torch.finfo(dtype)
    return {
        "dtype": str(dtype).removeprefix("torch."),
        "bits": info.bits,
        "eps": float(info.eps),
        "tiny": float(info.tiny),
        "max": float(info.max),
    }


def representable_step(dtype: torch.dtype) -> tuple[float, float]:
    info = torch.finfo(dtype)
    one = torch.tensor(1.0, dtype=dtype)
    half_step = one + torch.tensor(info.eps / 2, dtype=dtype)
    full_step = one + torch.tensor(info.eps, dtype=dtype)
    return float(half_step), float(full_step)


def non_associativity_example() -> tuple[float, float]:
    a = torch.tensor(1e20, dtype=torch.float32)
    b = torch.tensor(-1e20, dtype=torch.float32)
    c = torch.tensor(3.14, dtype=torch.float32)
    return float((a + b) + c), float(a + (b + c))


def logsumexp_example() -> tuple[float, float]:
    values = torch.tensor([1000.0, 999.0, 998.0], dtype=torch.float32)
    naive = torch.log(torch.exp(values).sum())
    stable = torch.logsumexp(values, dim=0)
    return float(naive), float(stable)


def range_example() -> tuple[float, float]:
    fp16_value = torch.tensor(70000.0, dtype=torch.float16)
    bf16_value = torch.tensor(70000.0, dtype=torch.bfloat16)
    return float(fp16_value), float(bf16_value)


def autocast_example() -> dict[str, float | str]:
    torch.manual_seed(0)
    left = torch.randn(16, 16, dtype=torch.float32)
    right = torch.randn(16, 16, dtype=torch.float32)
    reference = left @ right

    with torch.autocast(device_type="cpu", dtype=torch.bfloat16):
        reduced = left @ right

    absolute_error = (reduced.float() - reference).abs()
    relative_error = absolute_error / (reference.abs() + 1e-8)
    return {
        "output_dtype": str(reduced.dtype),
        "max_abs_error": float(absolute_error.max()),
        "median_rel_error": float(relative_error.median()),
    }


def tensor_bytes(shape: tuple[int, ...], dtype: torch.dtype) -> int:
    element_size = torch.empty((), dtype=dtype).element_size()
    return math.prod(shape) * element_size


def main() -> None:
    print(f"torch_version: {torch.__version__}")
    print("device: cpu")
    print()

    print("dtype_properties")
    for dtype in DTYPES:
        row = dtype_summary(dtype)
        print(
            f"{row['dtype']}: bits={row['bits']} "
            f"eps={row['eps']:.17g} "
            f"tiny={row['tiny']:.17g} "
            f"max={row['max']:.17g}"
        )
    print()

    print("representable_step_near_one")
    for dtype in DTYPES:
        half_step, full_step = representable_step(dtype)
        name = str(dtype).removeprefix("torch.")
        print(f"{name}: 1+eps/2={half_step:.17g} 1+eps={full_step:.17g}")
    print()

    left_grouping, right_grouping = non_associativity_example()
    print("non_associativity_float32")
    print(f"(a+b)+c: {left_grouping:.17g}")
    print(f"a+(b+c): {right_grouping:.17g}")
    print()

    naive, stable = logsumexp_example()
    print("logsumexp")
    print(f"naive: {naive}")
    print(f"stable: {stable:.17g}")
    print()

    fp16_value, bf16_value = range_example()
    print("range_example_70000")
    print(f"float16: {fp16_value}")
    print(f"bfloat16: {bf16_value:.17g}")
    print()

    autocast = autocast_example()
    print("cpu_autocast_bfloat16_matmul")
    print(f"output_dtype: {autocast['output_dtype']}")
    print(f"max_abs_error: {autocast['max_abs_error']:.17g}")
    print(f"median_rel_error: {autocast['median_rel_error']:.17g}")
    print()

    shape = (1024, 1024)
    print("tensor_storage_1024x1024")
    print(f"float32_bytes: {tensor_bytes(shape, torch.float32)}")
    print(f"float16_bytes: {tensor_bytes(shape, torch.float16)}")


if __name__ == "__main__":
    main()
