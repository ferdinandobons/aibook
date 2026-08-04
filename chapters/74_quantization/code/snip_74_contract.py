from __future__ import annotations

import json

CHAPTER = 74
TITLE = 'Quantizzazione'


def contract(case: str = "default"):
    if case != "default":
        raise ValueError("only the documented default case is supported")
    values = [-0.5, 0.0, 0.5]
    scale = 0.25
    quantized = [round(value / scale) for value in values]
    restored = [code * scale for code in quantized]
    error = max(abs(value - recovered) for value, recovered in zip(values, restored))
    return {"quantized": quantized, "restored": restored, "max_error": error, "invariant": "scale and calibration determine quantization error"}


def main() -> None:
    print(json.dumps(contract(), ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    main()
