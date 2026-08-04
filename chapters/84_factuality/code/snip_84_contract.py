from __future__ import annotations

import hashlib
import json
import math
import statistics
from collections import Counter

CHAPTER = 84
TITLE = 'Fattualità, incertezza e affidabilità'


def contract():
    claims = [(True, 0.9), (True, 0.8), (False, 0.95), (True, 0.7)]
    confident_errors = sum((not correct) and score >= 0.9 for correct, score in claims)
    return {"accuracy": sum(correct for correct, _score in claims) / len(claims), "confident_errors": confident_errors, "invariant": "confidence is evaluated against factual correctness, not substituted for it"}


def main() -> None:
    print(json.dumps(contract(), ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    main()
