from __future__ import annotations

import hashlib
import json
import math

CHAPTER = 56
TITLE = 'Vision encoder e Vision-Language Model'
PROFILE = 'multimodal'


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
    patches = [[0.8, 0.1], [0.2, 0.7]]
    question = [0.5, 0.5]
    scores = [sum(a * b for a, b in zip(patch, question)) for patch in patches]
    selected = max(range(len(scores)), key=scores.__getitem__)
    return {"scores": scores, "selected_patch": selected, "invariant": "visual grounding links a text query to explicit image features"}
def main() -> None:
    print(json.dumps(contract(), sort_keys=True))


if __name__ == "__main__":
    main()
