from __future__ import annotations

import math

CHAPTER = 88
TITLE = 'Robustezza, jailbreak e attacchi adversarial'

def stable_softmax(values: list[float]) -> list[float]:
    if not values:
        raise ValueError("values must not be empty")
    maximum = max(values)
    exps = [math.exp(value - maximum) for value in values]
    total = sum(exps)
    return [value / total for value in exps]

def weighted_combine(scores: list[float], states: list[list[float]]) -> list[float]:
    if len(scores) != len(states):
        raise ValueError("one state per score is required")
    if not states:
        raise ValueError("states must not be empty")
    dimension = len(states[0])
    if any(len(state) != dimension for state in states):
        raise ValueError("states must share a dimension")
    weights = stable_softmax(scores)
    return [sum(weight * state[index] for weight, state in zip(weights, states)) for index in range(dimension)]

def main() -> None:
    output = weighted_combine([1.0, 0.0, -1.0], [[1.0, 0.0], [0.0, 1.0], [1.0, 1.0]])
    print("chapter:", CHAPTER)
    print("title:", TITLE)
    print("output:", [round(value, 6) for value in output])

if __name__ == "__main__":
    main()
