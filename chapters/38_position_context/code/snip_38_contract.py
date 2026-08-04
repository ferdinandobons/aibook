from __future__ import annotations

import json
import math

CHAPTER = 38
TITLE = 'Posizione e contesto lungo'


def contract(case: str = "default"):
    if case != "default":
        raise ValueError("only the documented default case is supported")
    position = 2
    angle = position * 0.5
    query = [1.0, 0.0]
    rotated = [query[0] * math.cos(angle) - query[1] * math.sin(angle), query[0] * math.sin(angle) + query[1] * math.cos(angle)]
    return {"position": position, "rotated": [round(value, 6) for value in rotated], "invariant": "the positional transform is indexed by position"}


def main() -> None:
    print(json.dumps(contract(), ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    main()
