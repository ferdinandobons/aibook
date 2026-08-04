from __future__ import annotations

import hashlib
import json
import math
import statistics
from collections import Counter

CHAPTER = 46
TITLE = 'Supervised fine-tuning e instruction tuning'


def contract():
    tokens = ["utente", "domanda", "assistente", "risposta"]
    labels = [False, False, True, True]
    supervised = [token for token, include in zip(tokens, labels) if include]
    return {"supervised_tokens": supervised, "label_count": sum(labels), "invariant": "loss masking distinguishes prompt tokens from target tokens"}


def main() -> None:
    print(json.dumps(contract(), ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    main()
