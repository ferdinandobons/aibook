from __future__ import annotations

import hashlib
import json
import math
import statistics
from collections import Counter

CHAPTER = 61
TITLE = '3D, spazio e rappresentazione delle scene'


def contract():
    points = [(0.0, 0.0, 0.0), (1.0, 0.0, 0.0), (0.0, 1.0, 0.0)]
    centroid = [sum(point[index] for point in points) / len(points) for index in range(3)]
    return {"count": len(points), "centroid": centroid, "invariant": "a 3D representation preserves coordinate dimension"}


def main() -> None:
    print(json.dumps(contract(), ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    main()
