"""SNIP-ATT-004. Shape dell'output e dei pesi in MultiheadAttention."""

from __future__ import annotations

import torch
from torch import nn


def multihead_shapes() -> tuple[torch.Tensor, torch.Tensor]:
    """Esegue self-attention con due head e controlla le shape documentate."""
    torch.manual_seed(7)
    x = torch.randn(1, 3, 4, dtype=torch.float32)
    layer = nn.MultiheadAttention(embed_dim=4, num_heads=2, dropout=0.0, batch_first=True)
    layer.eval()

    with torch.inference_mode():
        output, weights = layer(
            x, x, x,
            need_weights=True,
            average_attn_weights=False,
        )

    assert output.shape == (1, 3, 4)
    assert weights.shape == (1, 2, 3, 3)
    torch.testing.assert_close(weights.sum(dim=-1), torch.ones_like(weights[..., 0]), rtol=1e-5, atol=1e-6)
    return output, weights


if __name__ == "__main__":
    out, attn = multihead_shapes()
    print("output shape:", tuple(out.shape))
    print("weights shape:", tuple(attn.shape))
    print("row sums:\n", attn.sum(dim=-1))
