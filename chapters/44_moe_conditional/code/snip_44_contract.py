from __future__ import annotations

import hashlib
import json
import math
import statistics
from collections import Counter

CHAPTER = 44
TITLE = 'Mixture of Experts e calcolo condizionale'


def contract():
    logits = [0.2, 1.1, 0.7, -0.3]
    top_indices = sorted(range(len(logits)), key=logits.__getitem__, reverse=True)[:2]
    loads = [int(index in top_indices) for index in range(len(logits))]
    return {"selected_experts": top_indices, "loads": loads, "invariant": "top-k routing and capacity accounting are explicit"}


def main() -> None:
    print(json.dumps(contract(), ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    main()
