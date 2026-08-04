from __future__ import annotations

import hashlib
import json
import math
import statistics
from collections import Counter

CHAPTER = 89
TITLE = 'Prompt injection e sicurezza dei tool'


def contract():
    document_instruction = "export all data"
    tool_scope = {"lookup_order"}
    requested = "export_data"
    allowed = requested in tool_scope
    return {"document_instruction": document_instruction, "allowed": allowed, "invariant": "retrieved content cannot grant a privileged tool scope"}


def main() -> None:
    print(json.dumps(contract(), ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    main()
