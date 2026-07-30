"""SNIP-ATT-002. Formula matriciale e confronto con l'API PyTorch."""

from __future__ import annotations

import math

import torch
import torch.nn.functional as F


def matrix_attention() -> tuple[torch.Tensor, torch.Tensor, torch.Tensor]:
    """Calcola attention da zero e verifica l'equivalenza con l'API ufficiale."""
    q = torch.tensor([[[[1.0, 0.0], [0.0, 1.0], [1.0, 1.0]]]], dtype=torch.float64)
    k = q.clone()
    v = q.clone()

    scores = q @ k.transpose(-2, -1) / math.sqrt(q.size(-1))
    weights = torch.softmax(scores, dim=-1)
    output = weights @ v

    api_output = F.scaled_dot_product_attention(q, k, v, dropout_p=0.0)
    torch.testing.assert_close(output, api_output, rtol=1e-12, atol=1e-12)
    torch.testing.assert_close(weights.sum(dim=-1), torch.ones_like(weights[..., 0]))
    return scores, weights, output


if __name__ == "__main__":
    torch.set_printoptions(precision=4, sci_mode=False)
    s, a, o = matrix_attention()
    print("scores:\n", s)
    print("weights:\n", a)
    print("output:\n", o)
