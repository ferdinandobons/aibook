from __future__ import annotations

import hashlib
import json
import math
import statistics
from collections import Counter

CHAPTER = 56
TITLE = 'Vision encoder e Vision-Language Model'


def contract():
    patches = [[0.8, 0.1], [0.2, 0.7]]
    question = [0.5, 0.5]
    scores = [sum(a * b for a, b in zip(patch, question)) for patch in patches]
    selected = max(range(len(scores)), key=scores.__getitem__)
    return {"scores": scores, "selected_patch": selected, "invariant": "visual grounding links a text query to explicit image features"}


def main() -> None:
    print(json.dumps(contract(), ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    main()
