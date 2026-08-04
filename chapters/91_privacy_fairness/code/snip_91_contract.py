from __future__ import annotations

import hashlib
import json
import math
import statistics
from collections import Counter

CHAPTER = 91
TITLE = 'Privacy, fairness e unlearning'


def contract():
    groups = {"A": {"correct": 3, "total": 4}, "B": {"correct": 2, "total": 4}}
    accuracy = {group: value["correct"] / value["total"] for group, value in groups.items()}
    gap = abs(accuracy["A"] - accuracy["B"])
    return {"accuracy_by_group": accuracy, "gap": gap, "invariant": "aggregate utility does not hide group-specific outcomes"}


def main() -> None:
    print(json.dumps(contract(), ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    main()
