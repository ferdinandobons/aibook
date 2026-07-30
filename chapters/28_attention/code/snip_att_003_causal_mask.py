"""SNIP-ATT-003. Causal mask booleana con scaled_dot_product_attention."""

from __future__ import annotations

import math

import torch
import torch.nn.functional as F


def causal_attention() -> tuple[torch.Tensor, torch.Tensor, torch.Tensor]:
    """Verifica che le posizioni future ricevano peso nullo."""
    q = torch.tensor([[[[1.0, 0.0], [0.0, 1.0], [1.0, 1.0]]]], dtype=torch.float64)
    k = q.clone()
    v = q.clone()
    allowed = torch.ones(3, 3, dtype=torch.bool).tril()

    scores = q @ k.transpose(-2, -1) / math.sqrt(q.size(-1))
    masked_scores = scores.masked_fill(~allowed, float("-inf"))
    weights = torch.softmax(masked_scores, dim=-1)
    output = weights @ v

    api_output = F.scaled_dot_product_attention(q, k, v, attn_mask=allowed, dropout_p=0.0)
    torch.testing.assert_close(output, api_output, rtol=1e-12, atol=1e-12)
    assert torch.count_nonzero(weights[..., ~allowed]).item() == 0
    return allowed, weights, output


if __name__ == "__main__":
    torch.set_printoptions(precision=4, sci_mode=False)
    m, a, o = causal_attention()
    print("allowed mask (True = ammesso):\n", m)
    print("weights:\n", a)
    print("output:\n", o)
