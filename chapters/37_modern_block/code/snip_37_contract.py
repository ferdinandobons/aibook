from __future__ import annotations

import json

CHAPTER = 37
TITLE = 'Anatomia del blocco moderno'


def contract(case: str = "default"):
    if case != "default":
        raise ValueError("only the documented default case is supported")
    state = [1.0, -2.0]
    update = [0.25, 0.5]
    output = [left + right for left, right in zip(state, update)]
    return {"output": output, "shape": [2], "invariant": "the residual stream keeps the declared dimension"}


def main() -> None:
    print(json.dumps(contract(), ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    main()
