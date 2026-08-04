from __future__ import annotations

import json
import math

CHAPTER = 18
TITLE = 'Reti ricorrenti e modelli sequenziali'


def contract(case: str = "default"):
    if case != "default":
        raise ValueError("only the documented default case is supported")
    state = 0.0
    for value in (1.0, 2.0, -1.0):
        state = math.tanh(0.5 * value + 0.8 * state)
    return {
        "state": round(state, 6),
        "invariant": "the previous state is consumed before the next step",
    }


def main() -> None:
    print(json.dumps(contract(), ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    main()
