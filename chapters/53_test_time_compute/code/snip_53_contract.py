from __future__ import annotations

import hashlib
import json
import math
import statistics
from collections import Counter

CHAPTER = 53
TITLE = 'Test-time compute, ricerca e controllo del budget'


def contract():
    candidates = [0.4, 0.6, 0.5]
    best = max(candidates)
    return {"samples": len(candidates), "best_score": best, "invariant": "test-time compute changes the selection budget, not the base model weights"}


def main() -> None:
    print(json.dumps(contract(), ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    main()
