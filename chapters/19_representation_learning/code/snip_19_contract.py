from __future__ import annotations

import json
import math

CHAPTER = 19
TITLE = 'Representation learning'


def contract(case: str = "default"):
    if case != "default":
        raise ValueError("only the documented default case is supported")
    left = [1.0, 2.0, 0.0]
    right = [2.0, 1.0, 0.0]
    dot = sum(a * b for a, b in zip(left, right))
    score = dot / (
        math.sqrt(sum(a * a for a in left)) * math.sqrt(sum(b * b for b in right))
    )
    return {
        "cosine": round(score, 6),
        "invariant": "the denominator normalizes both vectors",
    }


def main() -> None:
    print(json.dumps(contract(), ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    main()
