from __future__ import annotations

import hashlib
import json
import math
import statistics
from collections import Counter

CHAPTER = 26
TITLE = 'Il testo come dato'


def contract():
    text = "pacco"
    code_points = list(text)
    token_ids = [ord(char) for char in code_points]
    return {"code_points": code_points, "token_ids": token_ids, "invariant": "tokenization preserves an explicit mapping from text to ids"}


def main() -> None:
    print(json.dumps(contract(), ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    main()
