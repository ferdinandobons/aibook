from __future__ import annotations

import hashlib
import json
import math

CHAPTER = 31
TITLE = 'Dalla rappresentazione linguistica agli LLM'
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
    logits = [2.0, 1.0, 0.0]
    probabilities = normalize(logits)
    demonstrations = 2
    chosen = max(range(len(probabilities)), key=probabilities.__getitem__)
    return {"demonstrations": demonstrations, "probabilities": [round(value, 6) for value in probabilities], "chosen": chosen, "invariant": "decoding selects from a distribution and does not certify truth"}
def main() -> None:
    print(json.dumps(contract(), sort_keys=True))


if __name__ == "__main__":
    main()
