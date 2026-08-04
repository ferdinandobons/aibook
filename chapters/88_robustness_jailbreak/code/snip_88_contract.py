from __future__ import annotations

import json

CHAPTER = 88
TITLE = 'Robustezza, jailbreak e attacchi adversarial'


def contract(case: str = "default"):
    if case != "default":
        raise ValueError("only the documented default case is supported")
    prompts = [("base", False), ("perturbed", True)]
    failures = [name for name, attack_succeeded in prompts if attack_succeeded]
    return {"attack_success_rate": len(failures) / len(prompts), "failures": failures, "invariant": "robustness is defined relative to an explicit threat model"}


def main() -> None:
    print(json.dumps(contract(), ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    main()
