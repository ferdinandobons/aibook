"""Confronto minimo e riproducibile tra NumPy e PyTorch.

Il calcolo forward usa gli stessi valori nelle due librerie. PyTorch aggiunge
autograd, così il lettore può distinguere il risultato numerico dal grafo delle
derivate.
"""

from __future__ import annotations

import json

import numpy as np
import torch


def run_example() -> dict[str, object]:
    x_np = np.array([[1.0, -1.0], [0.5, 2.0]], dtype=np.float64)
    w_np = np.array([[0.4, -0.2], [0.1, 0.3]], dtype=np.float64)
    b_np = np.array([0.05, -0.10], dtype=np.float64)
    y_np = x_np @ w_np.T + b_np

    x = torch.tensor(x_np, dtype=torch.float64)
    w = torch.tensor(w_np, dtype=torch.float64, requires_grad=True)
    b = torch.tensor(b_np, dtype=torch.float64, requires_grad=True)
    y = x @ w.T + b
    loss = y.square().mean()
    loss.backward()

    if not np.allclose(y_np, y.detach().numpy(), atol=1e-12):
        raise AssertionError("NumPy e PyTorch non coincidono nel forward")

    return {
        "shape": list(y.shape),
        "forward": y.detach().numpy().round(6).tolist(),
        "loss": round(float(loss.detach()), 6),
        "weight_grad": w.grad.detach().numpy().round(6).tolist(),
        "bias_grad": b.grad.detach().numpy().round(6).tolist(),
    }


if __name__ == "__main__":
    print(json.dumps(run_example(), ensure_ascii=False, sort_keys=True))
