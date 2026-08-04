from __future__ import annotations

import hashlib
import json
import math
import statistics
from collections import Counter

CHAPTER = 21
TITLE = 'Modelli autoregressivi'


def contract():
    logits = [[2.0, 1.0, 0.0], [4.0, 3.0, 2.0]]
    causal = [[True, False, False], [True, True, False]]
    visible = [[row[j] for j in range(len(row)) if causal[i][j]] for i, row in enumerate(logits)]
    return {"visible_lengths": [len(row) for row in visible], "invariant": "a causal position cannot read a future token"}


def main() -> None:
    print(json.dumps(contract(), ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    main()
