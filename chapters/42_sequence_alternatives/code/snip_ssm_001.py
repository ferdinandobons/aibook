from __future__ import annotations
import math
import torch


def recurrence(x, a, b, c):
    h = torch.zeros_like(a)
    out = []
    for value in x:
        h = a * h + b * value
        out.append((c * h).sum())
    return torch.stack(out)


def kernel(n, a, b, c):
    p = torch.ones_like(a)
    values = []
    for _ in range(n):
        values.append((c * p * b).sum())
        p = p * a
    return torch.stack(values)


def convolution(x, k):
    return torch.stack(
        [(torch.flip(x[: t + 1], [0]) * k[: t + 1]).sum() for t in range(len(x))]
    )


def demo():
    x = torch.tensor([1.0, 2.0, -1.0, 0.5], dtype=torch.float64)
    a = torch.tensor([0.5, 0.8], dtype=torch.float64)
    b = torch.tensor([1.0, -0.2], dtype=torch.float64)
    c = torch.tensor([0.7, 0.3], dtype=torch.float64)
    r = recurrence(x, a, b, c)
    conv = convolution(x, kernel(len(x), a, b, c))
    return {"max_diff": float((r - conv).abs().max()), "shape": tuple(r.shape)}


def checks():
    d = demo()
    return {
        "duality": d["max_diff"] < 1e-12,
        "shape": d["shape"] == (4,),
        "finite": math.isfinite(d["max_diff"]),
    }
