from __future__ import annotations

import json
import math

CHAPTER = 40
TITLE = 'Attention hardware-aware'


def contract(case: str = "default"):
    if case != "default":
        raise ValueError("only the documented default case is supported")
    scores = [[1.0, 2.0], [0.0, 3.0]]
    row_maxima = [max(row) for row in scores]
    exp_sums = [sum(math.exp(value - maximum) for value in row) for row, maximum in zip(scores, row_maxima)]
    return {"row_maxima": row_maxima, "exp_sums": [round(value, 6) for value in exp_sums], "invariant": "softmax normalization is stable within each row"}


def main() -> None:
    print(json.dumps(contract(), ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    main()
