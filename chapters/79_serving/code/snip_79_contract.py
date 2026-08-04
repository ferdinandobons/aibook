from __future__ import annotations

import hashlib
import json
import math
import statistics
from collections import Counter

CHAPTER = 79
TITLE = 'Serving, batching e scheduling'


def contract():
    requests = [("short-1", 2), ("short-2", 2), ("long", 6)]
    batch = [request[0] for request in requests]
    total_tokens = sum(length for _request, length in requests)
    return {"batch": batch, "total_tokens": total_tokens, "invariant": "serving reports throughput and latency for the same admitted requests"}


def main() -> None:
    print(json.dumps(contract(), ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    main()
