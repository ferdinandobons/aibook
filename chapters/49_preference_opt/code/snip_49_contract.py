from __future__ import annotations

import hashlib
import json
import math
import statistics
from collections import Counter

CHAPTER = 49
TITLE = 'Ottimizzazione diretta delle preferenze'


def contract():
    policy_margin = 0.8
    reference_margin = 0.2
    beta = 0.5
    preference_logit = beta * (policy_margin - reference_margin)
    loss = math.log1p(math.exp(-preference_logit))
    return {"preference_logit": round(preference_logit, 6), "loss": round(loss, 6), "invariant": "DPO uses a policy-versus-reference margin"}


def main() -> None:
    print(json.dumps(contract(), ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    main()
