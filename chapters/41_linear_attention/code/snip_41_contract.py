from __future__ import annotations

import hashlib
import json
import math
import statistics
from collections import Counter

CHAPTER = 41
TITLE = 'Linear attention, fast weights e delta rule'


def contract():
    state = 0.0
    inputs = [1.0, -0.5, 2.0]
    for value in inputs:
        state = 0.7 * state + 0.3 * value
    return {"state": round(state, 6), "steps": len(inputs), "invariant": "the recurrence reuses one state in input order"}


def main() -> None:
    print(json.dumps(contract(), ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    main()
