from __future__ import annotations

import json

CHAPTER = 50
TITLE = 'Process supervision, outcome supervision e verifier'


def contract(case: str = "default"):
    if case != "default":
        raise ValueError("only the documented default case is supported")
    answers = ["4", "5", "4"]
    def verifier(answer):
        return answer == "4"
    accepted = [answer for answer in answers if verifier(answer)]
    return {"accepted": accepted, "acceptance_rate": len(accepted) / len(answers), "invariant": "a verifier is an explicit signal with its own error surface"}


def main() -> None:
    print(json.dumps(contract(), ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    main()
