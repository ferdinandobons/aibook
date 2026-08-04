from __future__ import annotations

import json
import math

CHAPTER = 25
TITLE = 'Diffusione, score matching e flow matching'


def contract(case: str = "default"):
    if case != "default":
        raise ValueError("only the documented default case is supported")
    alpha_bar = [0.9, 0.5, 0.1]
    signal = [math.sqrt(value) for value in alpha_bar]
    noise = [math.sqrt(1.0 - value) for value in alpha_bar]
    return {"signal": [round(value, 6) for value in signal], "noise": [round(value, 6) for value in noise], "invariant": "the sampler uses the same noise schedule as the forward process"}


def main() -> None:
    print(json.dumps(contract(), ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    main()
