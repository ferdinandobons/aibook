from __future__ import annotations

import hashlib
import json
import math
import statistics
from collections import Counter

CHAPTER = 88
TITLE = 'Robustezza, jailbreak e attacchi adversarial'


def contract():
    prompts = [("base", False), ("perturbed", True)]
    failures = [name for name, attack_succeeded in prompts if attack_succeeded]
    return {"attack_success_rate": len(failures) / len(prompts), "failures": failures, "invariant": "robustness is defined relative to an explicit threat model"}


def main() -> None:
    print(json.dumps(contract(), ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    main()
