from __future__ import annotations

import json

CHAPTER = 75
TITLE = 'Modelli low-bit nativi e co-design numerico'


def contract(case: str = "default"):
    if case != "default":
        raise ValueError("only the documented default case is supported")
    codes = [-1, 0, 1]
    scale = 0.5
    restored = [code * scale for code in codes]
    accumulated = sum(restored)
    return {"restored": restored, "accumulated": accumulated, "invariant": "nominal bit width is distinct from accumulation precision"}


def main() -> None:
    print(json.dumps(contract(), ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    main()
