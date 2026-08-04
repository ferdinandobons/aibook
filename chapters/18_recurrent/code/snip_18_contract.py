from __future__ import annotations

import hashlib
import json
import math

CHAPTER = 18
TITLE = 'Reti ricorrenti e modelli sequenziali'
PROFILE = 'rnn'


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
    state = 0.0
    for value in (1.0, 2.0, -1.0):
        state = math.tanh(0.5 * value + 0.8 * state)
    return {"state": round(state, 6), "invariant": "the previous state is consumed before the next step"}

def main() -> None:
    print(json.dumps(contract(), sort_keys=True))


if __name__ == "__main__":
    main()
