from __future__ import annotations
import torch
from torch import nn


def grad(model, x, y):
    model.zero_grad(set_to_none=True)
    nn.functional.mse_loss(model(x), y).backward()
    return [p.grad.clone() for p in model.parameters()]


def demo():
    torch.manual_seed(7)
    model = nn.Linear(2, 1, bias=False, dtype=torch.float64)
    x = torch.tensor(
        [[1.0, 0.0], [0.0, 1.0], [1.0, 1.0], [2.0, 1.0]], dtype=torch.float64
    )
    y = torch.tensor([[1.0], [2.0], [3.0], [4.0]], dtype=torch.float64)
    a = grad(model, x[:2], y[:2])
    b = grad(model, x[2:], y[2:])
    avg = [(u + v) / 2 for u, v in zip(a, b)]
    full = grad(model, x, y)
    return {
        "max_diff": max(float((u - v).abs().max()) for u, v in zip(avg, full)),
        "shards": [4, 3, 3],
    }


def checks():
    d = demo()
    return {
        "gradient_equivalence": d["max_diff"] < 1e-12,
        "shards_cover": sum(d["shards"]) == 10,
        "balanced": max(d["shards"]) - min(d["shards"]) <= 1,
    }
