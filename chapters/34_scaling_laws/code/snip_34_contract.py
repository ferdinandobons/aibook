from __future__ import annotations

import hashlib
import json
import math
import statistics
from collections import Counter

CHAPTER = 34
TITLE = 'Scaling law e progettazione del modello'


def contract():
    tokens = [1000.0, 2000.0, 4000.0, 8000.0]
    losses = [3.10, 2.74, 2.47, 2.29]
    slope = (losses[-1] - losses[0]) / (tokens[-1] - tokens[0])
    return {"points": len(tokens), "slope": round(slope, 8), "interval": [tokens[0], tokens[-1]], "invariant": "the fit is interpreted only on the observed interval"}


def main() -> None:
    print(json.dumps(contract(), ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    main()
