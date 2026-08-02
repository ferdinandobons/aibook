from __future__ import annotations

import math

CHAPTER = 24
TITLE = 'Normalizing flow e trasformazioni invertibili'

def normalize(values: list[float]) -> list[float]:
    if not values:
        raise ValueError("values must not be empty")
    maximum = max(values)
    exps = [math.exp(value - maximum) for value in values]
    total = sum(exps)
    return [value / total for value in exps]

def weighted_state(values: list[float], states: list[list[float]]) -> list[float]:
    weights = normalize(values)
    if len(weights) != len(states):
        raise ValueError("one state per score is required")
    dimension = len(states[0])
    if any(len(state) != dimension for state in states):
        raise ValueError("states must share a dimension")
    return [sum(weight * state[index] for weight, state in zip(weights, states)) for index in range(dimension)]

def main() -> None:
    output = weighted_state([1.0, 0.0, -1.0], [[1.0, 0.0], [0.0, 1.0], [1.0, 1.0]])
    print("chapter:", CHAPTER)
    print("title:", TITLE)
    print("output:", [round(value, 6) for value in output])

if __name__ == "__main__":
    main()
