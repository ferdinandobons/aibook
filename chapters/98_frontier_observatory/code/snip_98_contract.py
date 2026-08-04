from __future__ import annotations

import hashlib
import json
import math

CHAPTER = 98
TITLE = 'Osservatorio della frontiera'
PROFILE = 'labs'


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
    record = {"claim": "new method", "source_date": "2026-08-03", "evidence": "paper", "maturity": "FRONTIER"}
    required = {"claim", "source_date", "evidence", "maturity"}
    return {"record_complete": required <= set(record), "maturity": record["maturity"], "invariant": "novelty, evidence and readiness remain separate fields"}
def main() -> None:
    print(json.dumps(contract(), sort_keys=True))


if __name__ == "__main__":
    main()
