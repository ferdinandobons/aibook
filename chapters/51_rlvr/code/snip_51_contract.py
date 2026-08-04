from __future__ import annotations

import json

CHAPTER = 51
TITLE = 'Reinforcement learning con reward verificabili'


def contract(case: str = "default"):
    if case != "default":
        raise ValueError("only the documented default case is supported")
    rewards = [1.0, 0.0, 1.0]
    mean = sum(rewards) / len(rewards)
    advantages = [round(value - mean, 6) for value in rewards]
    return {"mean_reward": mean, "advantages": advantages, "invariant": "the policy update depends on declared reward and baseline"}


def main() -> None:
    print(json.dumps(contract(), ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    main()
