from __future__ import annotations

import hashlib
import json
import math
import statistics
from collections import Counter

CHAPTER = 76
TITLE = 'Decoding e generazione vincolata'


def normalize(values):
    if not values:
        raise ValueError('values must not be empty')
    maximum = max(values)
    exponentials = [math.exp(value - maximum) for value in values]
    total = sum(exponentials)
    return [value / total for value in exponentials]


def contract():
    logits = [2.0, 1.0, 0.5]
    greedy = max(range(len(logits)), key=logits.__getitem__)
    sampled_support = [index for index, probability in enumerate(normalize(logits)) if probability >= 0.2]
    return {"greedy": greedy, "support": sampled_support, "invariant": "decoding chooses a trajectory from logits without changing model parameters"}


def main() -> None:
    print(json.dumps(contract(), ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    main()
