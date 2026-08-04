from __future__ import annotations

import hashlib
import json
import math

CHAPTER = 29
TITLE = 'Il Transformer da zero'
PROFILE = 'sequence'


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
    q = [[1.0, 0.0], [0.0, 1.0]]
    k = [[1.0, 0.0], [0.0, 1.0]]
    v = [[2.0, 0.0], [0.0, 3.0]]
    scores = [[sum(q[i][d] * k[j][d] for d in range(2)) for j in range(2)] for i in range(2)]
    weights = [normalize(row) for row in scores]
    output = [[sum(weights[i][j] * v[j][d] for j in range(2)) for d in range(2)] for i in range(2)]
    return {"scores": scores, "output": [[round(value, 6) for value in row] for row in output], "invariant": "queries read keys and values through the declared attention matrix"}
def main() -> None:
    print(json.dumps(contract(), sort_keys=True))


if __name__ == "__main__":
    main()
