from __future__ import annotations

from dataclasses import dataclass

import torch
from torch import nn


@dataclass(frozen=True)
class Split:
    train: torch.Tensor
    validation: torch.Tensor
    test: torch.Tensor


def build_dataset(seed: int = 11) -> tuple[torch.Tensor, torch.Tensor, Split]:
    generator = torch.Generator().manual_seed(seed)
    class_0 = torch.randn(60, 2, generator=generator) * 0.35 + torch.tensor([-1.0, -0.5])
    class_1 = torch.randn(60, 2, generator=generator) * 0.35 + torch.tensor([1.0, 0.5])
    features = torch.cat([class_0, class_1])
    labels = torch.cat([
        torch.zeros(60, dtype=torch.long),
        torch.ones(60, dtype=torch.long),
    ])
    permutation = torch.randperm(len(features), generator=generator)
    features = features[permutation]
    labels = labels[permutation]
    split = Split(
        train=torch.arange(0, 72),
        validation=torch.arange(72, 96),
        test=torch.arange(96, 120),
    )
    return features, labels, split


def accuracy(model: nn.Module, x: torch.Tensor, y: torch.Tensor) -> float:
    with torch.inference_mode():
        predictions = model(x).argmax(dim=-1)
    return float((predictions == y).float().mean())


def train_candidate(
    x: torch.Tensor,
    y: torch.Tensor,
    split: Split,
    learning_rate: float,
) -> tuple[dict[str, torch.Tensor], float]:
    torch.manual_seed(19)
    model = nn.Linear(2, 2)
    optimizer = torch.optim.SGD(model.parameters(), lr=learning_rate)
    loss_fn = nn.CrossEntropyLoss()
    model.train()
    for _ in range(60):
        optimizer.zero_grad()
        loss = loss_fn(model(x[split.train]), y[split.train])
        loss.backward()
        optimizer.step()
    model.eval()
    state = {name: value.detach().clone() for name, value in model.state_dict().items()}
    val_accuracy = accuracy(model, x[split.validation], y[split.validation])
    return state, val_accuracy


def load_model(state: dict[str, torch.Tensor]) -> nn.Module:
    model = nn.Linear(2, 2)
    model.load_state_dict(state)
    model.eval()
    return model


def main() -> None:
    x, y, split = build_dataset()
    candidates = {}
    for learning_rate in (0.0005, 0.1):
        state, val_accuracy = train_candidate(x, y, split, learning_rate)
        candidates[learning_rate] = (state, val_accuracy)

    chosen_lr = max(candidates, key=lambda lr: candidates[lr][1])
    chosen_state, chosen_val_accuracy = candidates[chosen_lr]
    model = load_model(chosen_state)
    test_accuracy = accuracy(model, x[split.test], y[split.test])

    train_mean = x[split.train].mean(dim=0)
    train_std = x[split.train].std(dim=0).clamp_min(1e-6)
    production_batch = x[split.test] + torch.tensor([0.8, 0.0])
    standardized_mean_shift = (
        (production_batch.mean(dim=0) - train_mean).abs()
        / train_std
    )

    print(f"chosen_learning_rate: {chosen_lr}")
    print(f"validation_accuracy: {chosen_val_accuracy:.3f}")
    print(f"test_accuracy: {test_accuracy:.3f}")
    print(f"standardized_mean_shift: {standardized_mean_shift.tolist()}")


if __name__ == "__main__":
    main()
