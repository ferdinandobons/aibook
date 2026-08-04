from __future__ import annotations

import hashlib
import json
import math
import statistics
from collections import Counter

CHAPTER = 81
TITLE = 'Compiler, kernel e runtime'


def contract():
    graph = ["matmul", "add", "relu"]
    fused = ["matmul_add", "relu"]
    return {"original_ops": len(graph), "fused_ops": len(fused), "invariant": "compiler optimization preserves the declared operator result"}


def main() -> None:
    print(json.dumps(contract(), ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    main()
