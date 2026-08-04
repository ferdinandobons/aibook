from __future__ import annotations

import hashlib
import json
import math

CHAPTER = 34
TITLE = 'Scaling law e progettazione del modello'
PROFILE = 'scaling'


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
    tokens = [1000.0, 2000.0, 4000.0, 8000.0]
    losses = [3.10, 2.74, 2.47, 2.29]
    slope = (losses[-1] - losses[0]) / (tokens[-1] - tokens[0])
    return {"points": len(tokens), "slope": round(slope, 8), "interval": [tokens[0], tokens[-1]], "invariant": "the fit is interpreted only on the observed interval"}
def main() -> None:
    print(json.dumps(contract(), sort_keys=True))


if __name__ == "__main__":
    main()
