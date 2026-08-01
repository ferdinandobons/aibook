from __future__ import annotations

from dataclasses import dataclass
from typing import Dict

import torch
from torch import nn
import torch.nn.functional as F


@dataclass(frozen=True)
class DataSplit:
    features: torch.Tensor
    targets: torch.Tensor
    tracking_missing: torch.Tensor


@dataclass(frozen=True)
class BinaryMetrics:
    count: int
    tp: int
    tn: int
    fp: int
    fn: int
    accuracy: float
    precision: float
    recall: float
    f1: float
    weighted_cost: float
    predicted_positive_rate: float


@dataclass(frozen=True)
class TrainingResult:
    model: nn.Linear
    initial_objective: float
    final_objective: float


def make_split(n: int, seed: int, missing_rate: float) -> DataSplit:
    """Create an illustrative binary classification split.

    The latent label uses a delay signal, an urgency-language signal and noise.
    For the `tracking_missing` slice, the observed delay feature is attenuated,
    which makes the same classification task harder in a controlled way.
    """
    generator = torch.Generator().manual_seed(seed)
    latent_delay = torch.randn(n, generator=generator, dtype=torch.float64)
    urgency_language = torch.randn(n, generator=generator, dtype=torch.float64)
    tracking_missing = (
        torch.rand(n, generator=generator, dtype=torch.float64) < missing_rate
    )
    noise = 0.45 * torch.randn(n, generator=generator, dtype=torch.float64)

    latent_score = (
        1.2 * latent_delay
        + 1.6 * urgency_language
        + 0.7 * tracking_missing.to(torch.float64)
        + noise
        - 1.0
    )
    targets = (latent_score > 0.0).to(torch.float64)

    observed_delay = latent_delay.clone()
    observed_delay[tracking_missing] *= 0.45
    features = torch.stack((observed_delay, urgency_language), dim=1)
    return DataSplit(
        features=features,
        targets=targets,
        tracking_missing=tracking_missing.to(torch.int64),
    )


def objective(
    model: nn.Linear,
    split: DataSplit,
    l2_strength: float,
) -> torch.Tensor:
    logits = model(split.features).squeeze(-1)
    data_loss = F.binary_cross_entropy_with_logits(logits, split.targets)
    l2_penalty = l2_strength * model.weight.square().sum()
    return data_loss + l2_penalty


def train_model(
    split: DataSplit,
    *,
    seed: int = 7,
    steps: int = 500,
    learning_rate: float = 0.05,
    l2_strength: float = 0.01,
) -> TrainingResult:
    torch.manual_seed(seed)
    model = nn.Linear(2, 1, dtype=torch.float64)
    with torch.no_grad():
        model.weight.normal_(0.0, 0.1)
        model.bias.zero_()

    initial_objective = objective(model, split, l2_strength).detach().item()
    optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)

    for _ in range(steps):
        optimizer.zero_grad()
        loss = objective(model, split, l2_strength)
        loss.backward()
        optimizer.step()

    final_objective = objective(model, split, l2_strength).detach().item()
    return TrainingResult(model, initial_objective, final_objective)


def predict_probabilities(model: nn.Linear, split: DataSplit) -> torch.Tensor:
    with torch.inference_mode():
        return torch.sigmoid(model(split.features).squeeze(-1))


def binary_metrics(
    probabilities: torch.Tensor,
    targets: torch.Tensor,
    threshold: float,
    *,
    false_negative_cost: float = 5.0,
    false_positive_cost: float = 1.0,
) -> BinaryMetrics:
    predictions = (probabilities >= threshold).to(torch.int64)
    labels = targets.to(torch.int64)

    tp = int(((predictions == 1) & (labels == 1)).sum())
    tn = int(((predictions == 0) & (labels == 0)).sum())
    fp = int(((predictions == 1) & (labels == 0)).sum())
    fn = int(((predictions == 0) & (labels == 1)).sum())
    count = labels.numel()

    accuracy = (tp + tn) / count
    precision = tp / (tp + fp) if tp + fp else 0.0
    recall = tp / (tp + fn) if tp + fn else 0.0
    f1 = (
        2.0 * precision * recall / (precision + recall)
        if precision + recall
        else 0.0
    )
    weighted_cost = false_negative_cost * fn + false_positive_cost * fp

    return BinaryMetrics(
        count=count,
        tp=tp,
        tn=tn,
        fp=fp,
        fn=fn,
        accuracy=accuracy,
        precision=precision,
        recall=recall,
        f1=f1,
        weighted_cost=weighted_cost,
        predicted_positive_rate=float(predictions.to(torch.float64).mean()),
    )


def select_threshold(
    validation_probabilities: torch.Tensor,
    validation_targets: torch.Tensor,
) -> tuple[float, BinaryMetrics]:
    candidates = torch.linspace(0.10, 0.90, 17, dtype=torch.float64)
    evaluated = [
        (
            float(threshold),
            binary_metrics(
                validation_probabilities,
                validation_targets,
                float(threshold),
            ),
        )
        for threshold in candidates
    ]
    return min(
        evaluated,
        key=lambda item: (
            item[1].weighted_cost,
            -item[1].f1,
            item[0],
        ),
    )


def metrics_by_slice(
    probabilities: torch.Tensor,
    split: DataSplit,
    threshold: float,
) -> Dict[str, BinaryMetrics]:
    result: Dict[str, BinaryMetrics] = {}
    for value, name in ((0, "tracking_available"), (1, "tracking_missing")):
        mask = split.tracking_missing == value
        result[name] = binary_metrics(
            probabilities[mask],
            split.targets[mask],
            threshold,
        )
    return result


def format_metrics(name: str, metrics: BinaryMetrics) -> str:
    return (
        f"{name}: count={metrics.count}, accuracy={metrics.accuracy:.3f}, "
        f"precision={metrics.precision:.3f}, recall={metrics.recall:.3f}, "
        f"f1={metrics.f1:.3f}, cost={metrics.weighted_cost:.1f}, "
        f"tp={metrics.tp}, tn={metrics.tn}, fp={metrics.fp}, fn={metrics.fn}"
    )


def run_experiment() -> dict[str, object]:
    train = make_split(120, seed=11, missing_rate=0.35)
    validation = make_split(50, seed=12, missing_rate=0.40)
    test = make_split(50, seed=13, missing_rate=0.30)

    training = train_model(train)
    probabilities = {
        "train": predict_probabilities(training.model, train),
        "validation": predict_probabilities(training.model, validation),
        "test": predict_probabilities(training.model, test),
    }

    threshold, validation_metrics = select_threshold(
        probabilities["validation"],
        validation.targets,
    )
    test_selected = binary_metrics(
        probabilities["test"],
        test.targets,
        threshold,
    )
    test_default = binary_metrics(
        probabilities["test"],
        test.targets,
        0.50,
    )

    majority_label = int(train.targets.mean() >= 0.50)
    majority_probabilities = torch.full_like(test.targets, float(majority_label))
    majority_baseline = binary_metrics(
        majority_probabilities,
        test.targets,
        0.50,
    )

    return {
        "train": train,
        "validation": validation,
        "test": test,
        "training": training,
        "probabilities": probabilities,
        "threshold": threshold,
        "validation_metrics": validation_metrics,
        "test_selected": test_selected,
        "test_default": test_default,
        "majority_baseline": majority_baseline,
        "slice_metrics": metrics_by_slice(
            probabilities["test"],
            test,
            threshold,
        ),
    }


def main() -> None:
    result = run_experiment()
    training = result["training"]
    assert isinstance(training, TrainingResult)

    print(f"train_positive_rate: {result['train'].targets.mean().item():.3f}")
    print(f"validation_positive_rate: {result['validation'].targets.mean().item():.3f}")
    print(f"test_positive_rate: {result['test'].targets.mean().item():.3f}")
    print(f"initial_objective: {training.initial_objective:.6f}")
    print(f"final_objective: {training.final_objective:.6f}")
    print(f"model_weight: {training.model.weight.detach().flatten().tolist()}")
    print(f"model_bias: {training.model.bias.detach().flatten().tolist()}")
    print(f"selected_threshold_from_validation: {result['threshold']:.2f}")
    print(format_metrics("validation_selected", result["validation_metrics"]))
    print(format_metrics("test_selected", result["test_selected"]))
    print(format_metrics("test_default_0.50", result["test_default"]))
    print(format_metrics("test_majority_baseline", result["majority_baseline"]))
    for name, metrics in result["slice_metrics"].items():
        print(format_metrics(f"test_slice_{name}", metrics))


if __name__ == "__main__":
    main()
