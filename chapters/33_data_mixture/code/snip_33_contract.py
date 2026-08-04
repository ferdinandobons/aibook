from __future__ import annotations

import hashlib
import json
import math
import statistics
from collections import Counter

CHAPTER = 33
TITLE = 'Dataset mixture, curriculum e dati sintetici'


def contract():
    weights = [0.6, 0.3, 0.1]
    temperature = 0.5
    powered = [weight ** temperature for weight in weights]
    total = sum(powered)
    probabilities = [value / total for value in powered]
    return {"probabilities": [round(value, 6) for value in probabilities], "invariant": "the mixture is normalized after temperature sampling"}


def main() -> None:
    print(json.dumps(contract(), ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    main()
