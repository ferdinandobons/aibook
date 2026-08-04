from __future__ import annotations

import hashlib
import json
import math

CHAPTER = 84
TITLE = 'Fattualità, incertezza e affidabilità'
PROFILE = 'evaluation'


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
    claims = [(True, 0.9), (True, 0.8), (False, 0.95), (True, 0.7)]
    confident_errors = sum((not correct) and score >= 0.9 for correct, score in claims)
    return {"accuracy": sum(correct for correct, _score in claims) / len(claims), "confident_errors": confident_errors, "invariant": "confidence is evaluated against factual correctness, not substituted for it"}
def main() -> None:
    print(json.dumps(contract(), sort_keys=True))


if __name__ == "__main__":
    main()
