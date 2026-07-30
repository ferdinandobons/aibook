"""SNIP-ATT-001. Scaled dot-product attention per una singola query."""

from __future__ import annotations

import math

import torch


def single_query_attention() -> tuple[torch.Tensor, torch.Tensor, torch.Tensor]:
    """Restituisce score scalati, pesi e output per un esempio deterministico."""
    q = torch.tensor([1.0, 0.0], dtype=torch.float64)
    k = torch.tensor([[1.0, 0.0], [0.0, 1.0], [1.0, 1.0]], dtype=torch.float64)
    v = torch.tensor([[1.0, 0.0], [0.0, 1.0], [1.0, 1.0]], dtype=torch.float64)

    scores = (q @ k.transpose(0, 1)) / math.sqrt(q.numel())
    weights = torch.softmax(scores, dim=-1)
    output = weights @ v

    assert scores.shape == (3,)
    assert weights.shape == (3,)
    assert output.shape == (2,)
    torch.testing.assert_close(weights.sum(), torch.tensor(1.0, dtype=weights.dtype))
    return scores, weights, output


if __name__ == "__main__":
    torch.set_printoptions(precision=4, sci_mode=False)
    s, a, o = single_query_attention()
    print("scores:", s)
    print("weights:", a)
    print("output:", o)
