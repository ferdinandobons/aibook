from __future__ import annotations

import json
import math

CHAPTER = 29
TITLE = 'Il Transformer da zero'


def normalize(values):
    if not values:
        raise ValueError('values must not be empty')
    maximum = max(values)
    exponentials = [math.exp(value - maximum) for value in values]
    total = sum(exponentials)
    return [value / total for value in exponentials]


def contract(case: str = "default"):
    if case != "default":
        raise ValueError("only the documented default case is supported")
    q = [[1.0, 0.0], [0.0, 1.0]]
    k = [[1.0, 0.0], [0.0, 1.0]]
    v = [[2.0, 0.0], [0.0, 3.0]]
    scores = [[sum(q[i][d] * k[j][d] for d in range(2)) for j in range(2)] for i in range(2)]
    weights = [normalize(row) for row in scores]
    output = [[sum(weights[i][j] * v[j][d] for j in range(2)) for d in range(2)] for i in range(2)]
    return {"scores": scores, "output": [[round(value, 6) for value in row] for row in output], "invariant": "queries read keys and values through the declared attention matrix"}


def main() -> None:
    print(json.dumps(contract(), ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    main()
