from __future__ import annotations

import hashlib
import json
import math

CHAPTER = 76
TITLE = 'Decoding e generazione vincolata'
PROFILE = 'inference'


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
    logits = [2.0, 1.0, 0.5]
    greedy = max(range(len(logits)), key=logits.__getitem__)
    sampled_support = [index for index, probability in enumerate(normalize(logits)) if probability >= 0.2]
    return {"greedy": greedy, "support": sampled_support, "invariant": "decoding chooses a trajectory from logits without changing model parameters"}
def main() -> None:
    print(json.dumps(contract(), sort_keys=True))


if __name__ == "__main__":
    main()
