from __future__ import annotations

import hashlib
import json
import math

CHAPTER = 47
TITLE = 'Fine-tuning efficiente'
PROFILE = 'posttraining'


def normalize(values):
    if not values:
        raise ValueError("values must not be empty")
    maximum = max(values)
    exp_values = [math.exp(value - maximum) for value in values]
    total = sum(exp_values)
    return [value / total for value in exp_values]


def weighted_state(scores, states):
    if len(scores) != len(states):
        raise ValueError("one state per score is required")
    if not states:
        raise ValueError("states must not be empty")
    dimension = len(states[0])
    if any(len(state) != dimension for state in states):
        raise ValueError("states must share a dimension")
    weights = normalize(scores)
    return [sum(weight * state[index] for weight, state in zip(weights, states)) for index in range(dimension)]


def stable_softmax(values):
    return normalize(values)


def weighted_combine(scores, states):
    return weighted_state(scores, states)

def contract():
    base = [1.0, 2.0]
    direction_a = [0.5, 0.0]
    direction_b = [0.0, -0.25]
    scale = 0.4
    delta = [scale * (a + b) for a, b in zip(direction_a, direction_b)]
    adapted = [value + change for value, change in zip(base, delta)]
    return {"delta": delta, "adapted": adapted, "invariant": "the low-rank update is separated from frozen base weights"}
def main() -> None:
    print(json.dumps(contract(), sort_keys=True))


if __name__ == "__main__":
    main()
