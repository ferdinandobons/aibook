from __future__ import annotations

import hashlib
import json
import math
import statistics
from collections import Counter

CHAPTER = 95
TITLE = 'Costruire un piccolo language model'


def contract():
    tokens = [[1, 2, 3], [2, 3, 4]]
    inputs = [row[:-1] for row in tokens]
    targets = [row[1:] for row in tokens]
    return {"input_shape": [len(inputs), len(inputs[0])], "target_shape": [len(targets), len(targets[0])], "invariant": "causal training shifts target one token after the input"}


def main() -> None:
    print(json.dumps(contract(), ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    main()
