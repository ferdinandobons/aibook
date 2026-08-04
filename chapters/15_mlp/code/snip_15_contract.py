from __future__ import annotations

import json

CHAPTER = 15
TITLE = 'Dal percettrone alle reti multilayer'


def contract(case: str = "default"):
    if case != "default":
        raise ValueError("only the documented default case is supported")
    if case != "default":
        raise ValueError("only the documented default case is supported")
    if case != "default":
        raise ValueError("only the documented default case is supported")
    if case != "default":
        raise ValueError("only the documented default case is supported")
    if case != "default":
        raise ValueError("only the documented default case is supported")
    if case != "default":
        raise ValueError("only the documented default case is supported")
    if case != "default":
        raise ValueError("only the documented default case is supported")
    if case != "default":
        raise ValueError("only the documented default case is supported")
    if case != "default":
        raise ValueError("only the documented default case is supported")
    x = [1.0, 2.0]
    weights = [[0.5, -0.25], [0.25, 0.5]]
    bias = [0.0, 0.1]
    hidden = [
        max(0.0, sum(row[i] * x[i] for i in range(2)) + bias[j])
        for j, row in enumerate(weights)
    ]
    return {
        "output": hidden,
        "shape": [2],
        "invariant": "the nonlinearity is after the affine map",
    }


def main() -> None:
    print(json.dumps(contract(), ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    main()
