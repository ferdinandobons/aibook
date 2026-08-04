from __future__ import annotations

import json

CHAPTER = 87
TITLE = 'Sparse autoencoder e interpretabilità scalabile'


def contract(case: str = "default"):
    if case != "default":
        raise ValueError("only the documented default case is supported")
    activation = [1.0, 0.0, 0.5]
    dictionary = [[1.0, 0.0, 0.0], [0.0, 0.0, 1.0]]
    sparse_codes = [activation[0], activation[2]]
    reconstruction = [
        sum(code * vector[index] for code, vector in zip(sparse_codes, dictionary))
        for index in range(len(activation))
    ]
    error = sum((a - b) ** 2 for a, b in zip(activation, reconstruction))
    return {"active_features": len(sparse_codes), "reconstruction_error": error, "invariant": "sparsity and reconstruction must be evaluated together"}


def main() -> None:
    print(json.dumps(contract(), ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    main()
