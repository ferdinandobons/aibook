from __future__ import annotations

import hashlib
import json
import math
import statistics
from collections import Counter

CHAPTER = 47
TITLE = 'Fine-tuning efficiente'


def contract():
    base = [1.0, 2.0]
    direction_a = [0.5, 0.0]
    direction_b = [0.0, -0.25]
    scale = 0.4
    delta = [scale * (a + b) for a, b in zip(direction_a, direction_b)]
    adapted = [value + change for value, change in zip(base, delta)]
    return {"delta": delta, "adapted": adapted, "invariant": "the low-rank update is separated from frozen base weights"}


def main() -> None:
    print(json.dumps(contract(), ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    main()
