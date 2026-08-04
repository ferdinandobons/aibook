from __future__ import annotations

import json
import math

CHAPTER = 24
TITLE = 'Normalizing flow e trasformazioni invertibili'


def contract(case: str = "default"):
    if case != "default":
        raise ValueError("only the documented default case is supported")
    scale = [2.0, 0.5]
    log_det = sum(math.log(value) for value in scale)
    inverse = [1.0 / value for value in scale]
    return {"log_det": round(log_det, 6), "inverse_scale": inverse, "invariant": "the transform exposes both an inverse and a log determinant"}


def main() -> None:
    print(json.dumps(contract(), ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    main()
