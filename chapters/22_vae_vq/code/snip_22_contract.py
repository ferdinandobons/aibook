from __future__ import annotations

import json

CHAPTER = 22
TITLE = 'Variational Autoencoder e latent discreti'


def contract(case: str = "default"):
    if case != "default":
        raise ValueError("only the documented default case is supported")
    reconstruction = 0.40
    kl = 0.10
    beta = 0.5
    objective = reconstruction + beta * kl
    return {"reconstruction": reconstruction, "kl": kl, "objective": round(objective, 6), "invariant": "reconstruction and regularization stay separately observable"}


def main() -> None:
    print(json.dumps(contract(), ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    main()
