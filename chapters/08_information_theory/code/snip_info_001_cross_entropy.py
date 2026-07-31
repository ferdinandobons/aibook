from __future__ import annotations

import torch
import torch.nn.functional as F


def entropy(probabilities: torch.Tensor) -> torch.Tensor:
    if probabilities.ndim != 1:
        raise ValueError("probabilities must be one-dimensional")
    if torch.any(probabilities < 0):
        raise ValueError("probabilities cannot be negative")
    if not torch.isclose(
        probabilities.sum(),
        torch.tensor(1.0, dtype=probabilities.dtype),
    ):
        raise ValueError("probabilities must sum to one")
    positive = probabilities > 0
    return -(probabilities[positive] * probabilities[positive].log()).sum()


def cross_entropy(target: torch.Tensor, prediction: torch.Tensor) -> torch.Tensor:
    if target.shape != prediction.shape:
        raise ValueError("target and prediction must have the same shape")
    if torch.any(target < 0) or torch.any(prediction <= 0):
        raise ValueError("invalid probability vector")
    if not torch.isclose(target.sum(), torch.tensor(1.0, dtype=target.dtype)):
        raise ValueError("target must sum to one")
    if not torch.isclose(
        prediction.sum(),
        torch.tensor(1.0, dtype=prediction.dtype),
    ):
        raise ValueError("prediction must sum to one")
    return -(target * prediction.log()).sum()


def kl_divergence(target: torch.Tensor, prediction: torch.Tensor) -> torch.Tensor:
    positive = target > 0
    return (
        target[positive]
        * (target[positive].log() - prediction[positive].log())
    ).sum()


def main() -> None:
    logits = torch.tensor(
        [2.0, 0.5, -1.0],
        dtype=torch.float64,
        requires_grad=True,
    )
    target_index = torch.tensor(0)
    probabilities = torch.softmax(logits, dim=0)
    log_probabilities = torch.log_softmax(logits, dim=0)
    manual_nll = -log_probabilities[target_index]
    api_cross_entropy = F.cross_entropy(
        logits.unsqueeze(0),
        target_index.unsqueeze(0),
    )
    api_cross_entropy.backward()

    print(f"probabilities: {probabilities.detach()}")
    print(f"probability_target_class: {probabilities[0].item():.6f}")
    print(f"manual_nll: {manual_nll.item():.6f}")
    print(f"api_cross_entropy: {api_cross_entropy.item():.6f}")
    print(f"gradient_logits: {logits.grad}")
    print(
        f"prediction_entropy_nats: "
        f"{entropy(probabilities.detach()).item():.6f}"
    )

    soft_target = torch.tensor([0.90, 0.05, 0.05], dtype=torch.float64)
    soft_ce = cross_entropy(soft_target, probabilities.detach())
    soft_entropy = entropy(soft_target)
    soft_kl = kl_divergence(soft_target, probabilities.detach())
    print(f"soft_target_entropy: {soft_entropy.item():.6f}")
    print(f"soft_target_cross_entropy: {soft_ce.item():.6f}")
    print(f"soft_target_kl: {soft_kl.item():.6f}")
    print(f"entropy_plus_kl: {(soft_entropy + soft_kl).item():.6f}")

    wrong_logits = torch.tensor([-1.0, 0.5, 2.0], dtype=torch.float64)
    wrong_loss = F.cross_entropy(
        wrong_logits.unsqueeze(0),
        target_index.unsqueeze(0),
    )
    print(f"confident_wrong_loss: {wrong_loss.item():.6f}")

    large_logits = torch.tensor([1000.0, 999.0, 998.0], dtype=torch.float64)
    naive_probabilities = torch.exp(large_logits) / torch.exp(large_logits).sum()
    stable_log_probabilities = torch.log_softmax(large_logits, dim=0)
    print(f"naive_large_logits_probabilities: {naive_probabilities}")
    print(
        f"stable_large_logits_log_probabilities: "
        f"{stable_log_probabilities}"
    )


if __name__ == "__main__":
    main()
