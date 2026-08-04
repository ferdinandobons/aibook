from __future__ import annotations

import json

CHAPTER = 16
TITLE = 'Addestrare reti profonde'


def contract(case: str = "default"):
    if case != "default":
        raise ValueError("only the documented default case is supported")
    x = [1.0, -2.0]
    residual = [0.2, 0.3]
    output = [a + b for a, b in zip(x, residual)]
    return {
        "output": output,
        "shape": [2],
        "invariant": "residual operands share shape",
    }


def main() -> None:
    print(json.dumps(contract(), ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    main()
