from __future__ import annotations

import hashlib
import json
import math

CHAPTER = 44
TITLE = 'Mixture of Experts e calcolo condizionale'
PROFILE = 'architecture'


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
    logits = [0.2, 1.1, 0.7, -0.3]
    top_indices = sorted(range(len(logits)), key=logits.__getitem__, reverse=True)[:2]
    loads = [int(index in top_indices) for index in range(len(logits))]
    return {"selected_experts": top_indices, "loads": loads, "invariant": "top-k routing and capacity accounting are explicit"}
def main() -> None:
    print(json.dumps(contract(), sort_keys=True))


if __name__ == "__main__":
    main()
