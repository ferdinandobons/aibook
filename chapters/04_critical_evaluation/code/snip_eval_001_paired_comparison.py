from __future__ import annotations

from dataclasses import dataclass
from random import Random
from typing import Sequence


@dataclass(frozen=True)
class Example:
    label: int
    model_a: int
    model_b: int
    group: str
    cost: float


EXAMPLES: tuple[Example, ...] = (
    Example(0, 0, 0, "standard", 1.0),
    Example(1, 1, 1, "standard", 1.0),
    Example(0, 0, 0, "standard", 1.0),
    Example(1, 1, 1, "standard", 1.0),
    Example(0, 1, 0, "standard", 1.0),
    Example(1, 1, 1, "standard", 1.0),
    Example(0, 0, 0, "standard", 1.0),
    Example(1, 0, 1, "standard", 1.0),
    Example(0, 0, 0, "standard", 1.0),
    Example(1, 1, 1, "standard", 1.0),
    Example(0, 1, 0, "standard", 1.0),
    Example(1, 1, 1, "standard", 1.0),
    Example(0, 0, 0, "standard", 1.0),
    Example(1, 0, 1, "standard", 1.0),
    Example(0, 0, 1, "standard", 1.0),
    Example(1, 1, 1, "standard", 1.0),
    Example(1, 1, 1, "urgent", 4.0),
    Example(1, 1, 0, "urgent", 4.0),
    Example(1, 1, 1, "urgent", 4.0),
    Example(1, 1, 0, "urgent", 4.0),
    Example(1, 1, 1, "urgent", 4.0),
    Example(1, 1, 0, "urgent", 4.0),
    Example(1, 0, 1, "urgent", 4.0),
    Example(1, 1, 1, "urgent", 4.0),
)


def value(row: Example, model: str) -> int:
    if model == "A":
        return row.model_a
    if model == "B":
        return row.model_b
    raise ValueError(model)


def accuracy(rows: Sequence[Example], model: str) -> float:
    return sum(value(row, model) == row.label for row in rows) / len(rows)


def accuracy_by_group(rows: Sequence[Example], model: str) -> dict[str, float]:
    groups = sorted({row.group for row in rows})
    return {
        group: accuracy(tuple(row for row in rows if row.group == group), model)
        for group in groups
    }


def weighted_error_cost(rows: Sequence[Example], model: str) -> float:
    return sum(row.cost for row in rows if value(row, model) != row.label)


def paired_bootstrap_difference(
    rows: Sequence[Example],
    samples: int = 10_000,
    seed: int = 7,
) -> tuple[float, float, float]:
    rng = Random(seed)
    n = len(rows)
    differences: list[float] = []
    for _ in range(samples):
        indices = [rng.randrange(n) for _ in range(n)]
        sample = tuple(rows[index] for index in indices)
        differences.append(accuracy(sample, "B") - accuracy(sample, "A"))
    differences.sort()
    observed = accuracy(rows, "B") - accuracy(rows, "A")
    lower = differences[int(0.025 * (samples - 1))]
    upper = differences[int(0.975 * (samples - 1))]
    return observed, lower, upper


def main() -> None:
    for model in ("A", "B"):
        print(f"model_{model}_accuracy: {accuracy(EXAMPLES, model):.3f}")
        print(f"model_{model}_group_accuracy: {accuracy_by_group(EXAMPLES, model)}")
        print(f"model_{model}_weighted_error_cost: {weighted_error_cost(EXAMPLES, model):.1f}")
    observed, lower, upper = paired_bootstrap_difference(EXAMPLES)
    print(f"accuracy_difference_B_minus_A: {observed:.3f}")
    print(f"paired_bootstrap_95pct_interval: [{lower:.3f}, {upper:.3f}]")
    print(f"interval_contains_zero: {lower <= 0.0 <= upper}")


if __name__ == "__main__":
    main()
