from __future__ import annotations
import math
import torch
from torch import nn


def lr(step, total, warmup, peak):
    if step < warmup:
        return peak * (step + 1) / warmup
    p = (step - warmup) / max(total - warmup - 1, 1)
    return peak * (0.1 + 0.9 * 0.5 * (1 + math.cos(math.pi * min(max(p, 0), 1))))


def demo():
    torch.manual_seed(7)
    model = nn.Linear(2, 2)
    opt = torch.optim.AdamW(model.parameters(), lr=0.05)
    x = torch.tensor([[1.0, 0.0], [0.0, 1.0]])
    y = torch.tensor([0, 1])
    losses = []
    for step in range(30):
        opt.param_groups[0]["lr"] = lr(step, 30, 4, 0.05)
        opt.zero_grad()
        loss = nn.functional.cross_entropy(model(x), y)
        loss.backward()
        nn.utils.clip_grad_norm_(model.parameters(), 1.0)
        opt.step()
        losses.append(float(loss))
    state = {
        "model": model.state_dict(),
        "optimizer": opt.state_dict(),
        "step": 30,
        "rng": torch.get_rng_state(),
    }
    return {"first": losses[0], "last": losses[-1], "keys": sorted(state)}


def checks():
    d = demo()
    return {
        "loss_down": d["last"] < d["first"],
        "checkpoint": d["keys"] == ["model", "optimizer", "rng", "step"],
        "warmup": lr(0, 30, 4, 0.05) < lr(3, 30, 4, 0.05),
    }
