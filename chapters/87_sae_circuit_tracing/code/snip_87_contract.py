from __future__ import annotations

import hashlib
import json
import math
import statistics
from collections import Counter

CHAPTER = 87
TITLE = 'Sparse autoencoder e interpretabilità scalabile'


def contract():
    activation = [1.0, 0.0, 0.5]
    dictionary = [[1.0, 0.0, 0.0], [0.0, 0.0, 1.0]]
    sparse_codes = [activation[0], activation[2]]
    reconstruction = [sparse_codes[0], 0.0, sparse_codes[1]]
    error = sum((a - b) ** 2 for a, b in zip(activation, reconstruction))
    return {"active_features": len(sparse_codes), "reconstruction_error": error, "invariant": "sparsity and reconstruction must be evaluated together"}


def main() -> None:
    print(json.dumps(contract(), ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    main()
