from __future__ import annotations

import hashlib
import json
import math
import statistics
from collections import Counter

CHAPTER = 83
TITLE = 'Progettare una valutazione'


def contract():
    predictions = [1, 1, 0, 1]
    labels = [1, 0, 0, 1]
    correct = sum(prediction == label for prediction, label in zip(predictions, labels))
    failures = [index for index, pair in enumerate(zip(predictions, labels)) if pair[0] != pair[1]]
    return {"accuracy": correct / len(labels), "failures": failures, "invariant": "a metric is reported with its decision target and failure cases"}


def main() -> None:
    print(json.dumps(contract(), ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    main()
