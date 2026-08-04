from __future__ import annotations

import hashlib
import json
import math
import statistics
from collections import Counter

CHAPTER = 31
TITLE = 'Dalla rappresentazione linguistica agli LLM'


def normalize(values):
    if not values:
        raise ValueError('values must not be empty')
    maximum = max(values)
    exponentials = [math.exp(value - maximum) for value in values]
    total = sum(exponentials)
    return [value / total for value in exponentials]


def contract():
    logits = [2.0, 1.0, 0.0]
    probabilities = normalize(logits)
    demonstrations = 2
    chosen = max(range(len(probabilities)), key=probabilities.__getitem__)
    return {"demonstrations": demonstrations, "probabilities": [round(value, 6) for value in probabilities], "chosen": chosen, "invariant": "decoding selects from a distribution and does not certify truth"}


def main() -> None:
    print(json.dumps(contract(), ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    main()
