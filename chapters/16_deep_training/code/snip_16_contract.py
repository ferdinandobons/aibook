from __future__ import annotations

import hashlib
import json
import math
import statistics
from collections import Counter

CHAPTER = 16
TITLE = 'Addestrare reti profonde'


def contract():
    x = [1.0, -2.0]
    residual = [0.2, 0.3]
    output = [a + b for a, b in zip(x, residual)]
    return {"output": output, "shape": [2], "invariant": "residual operands share shape"}


def main() -> None:
    print(json.dumps(contract(), ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    main()
