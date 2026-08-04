from __future__ import annotations

import hashlib
import json
import math
import statistics
from collections import Counter

CHAPTER = 75
TITLE = 'Modelli low-bit nativi e co-design numerico'


def contract():
    codes = [-1, 0, 1]
    scale = 0.5
    restored = [code * scale for code in codes]
    accumulated = sum(restored)
    return {"restored": restored, "accumulated": accumulated, "invariant": "nominal bit width is distinct from accumulation precision"}


def main() -> None:
    print(json.dumps(contract(), ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    main()
