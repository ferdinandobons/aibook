from __future__ import annotations

import hashlib
import json
import math
import statistics
from collections import Counter

CHAPTER = 77
TITLE = 'Speculative e parallel decoding'


def contract():
    draft = ["a", "b", "c"]
    target_accepts = [True, True, False]
    accepted = [token for token, ok in zip(draft, target_accepts) if ok]
    fallback = "target_next" if not target_accepts[-1] else None
    return {"accepted": accepted, "fallback": fallback, "invariant": "speculative decoding verifies draft tokens before committing them"}


def main() -> None:
    print(json.dumps(contract(), ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    main()
