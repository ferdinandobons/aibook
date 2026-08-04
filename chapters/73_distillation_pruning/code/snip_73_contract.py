from __future__ import annotations

import hashlib
import json
import math
import statistics
from collections import Counter

CHAPTER = 73
TITLE = 'Distillazione e pruning'


def contract():
    teacher = [0.8, 0.2]
    student = [0.6, 0.4]
    distillation_error = sum((a - b) ** 2 for a, b in zip(teacher, student))
    mask = [True, False]
    return {"distillation_error": round(distillation_error, 6), "kept_weights": sum(mask), "invariant": "compression quality and structural pruning are measured separately"}


def main() -> None:
    print(json.dumps(contract(), ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    main()
