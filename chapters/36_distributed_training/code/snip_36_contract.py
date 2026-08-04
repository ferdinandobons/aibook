from __future__ import annotations

import hashlib
import json
import math
import statistics
from collections import Counter

CHAPTER = 36
TITLE = 'Training distribuito e continued pretraining'


def contract():
    worker_gradients = [[1.0, 3.0], [3.0, 1.0]]
    workers = len(worker_gradients)
    reduced = [sum(row[index] for row in worker_gradients) / workers for index in range(2)]
    return {"workers": workers, "reduced_gradient": reduced, "invariant": "all workers contribute to the same declared reduction"}


def main() -> None:
    print(json.dumps(contract(), ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    main()
