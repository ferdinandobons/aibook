from __future__ import annotations

import hashlib
import json
import math

CHAPTER = 23
TITLE = 'Generative Adversarial Network'
PROFILE = 'generative'


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
    real = [0.9, 0.8]
    fake = [0.2, 0.3]
    discriminator_gap = sum(real) / len(real) - sum(fake) / len(fake)
    return {"discriminator_gap": round(discriminator_gap, 6), "invariant": "generator and discriminator signals are not the same loss"}
def main() -> None:
    print(json.dumps(contract(), sort_keys=True))


if __name__ == "__main__":
    main()
