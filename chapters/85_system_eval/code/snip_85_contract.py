from __future__ import annotations

import hashlib
import json
import math
import statistics
from collections import Counter

CHAPTER = 85
TITLE = 'Valutare contesto lungo, RAG, multimodalità e agenti'


def contract():
    trace = {"retrieval": True, "answer": True, "citation": False, "tool": True}
    system_success = all(trace.values())
    return {"component_failures": [key for key, ok in trace.items() if not ok], "system_success": system_success, "invariant": "end-to-end evaluation keeps component failures visible"}


def main() -> None:
    print(json.dumps(contract(), ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    main()
