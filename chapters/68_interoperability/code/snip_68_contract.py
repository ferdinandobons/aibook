from __future__ import annotations

import hashlib
import json
import math
import statistics
from collections import Counter

CHAPTER = 68
TITLE = 'Protocolli e interoperabilità'


def contract():
    producer = {"version": 1, "capability": "lookup_order"}
    consumer = {"accepted_versions": {1, 2}, "required": "lookup_order"}
    compatible = producer["version"] in consumer["accepted_versions"] and producer["capability"] == consumer["required"]
    return {"compatible": compatible, "invariant": "interoperability is a versioned contract, not a shared label"}


def main() -> None:
    print(json.dumps(contract(), ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    main()
