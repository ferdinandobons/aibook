from __future__ import annotations

import hashlib
import json
import math
import statistics
from collections import Counter

CHAPTER = 23
TITLE = 'Generative Adversarial Network'


def contract():
    real = [0.9, 0.8]
    fake = [0.2, 0.3]
    discriminator_gap = sum(real) / len(real) - sum(fake) / len(fake)
    return {"discriminator_gap": round(discriminator_gap, 6), "invariant": "generator and discriminator signals are not the same loss"}


def main() -> None:
    print(json.dumps(contract(), ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    main()
