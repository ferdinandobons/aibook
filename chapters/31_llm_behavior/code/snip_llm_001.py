from __future__ import annotations
import math

VOCAB = ("pacco", "ritardo", "ordine", "ticket")
BIGRAM = {
    "pacco": {"ritardo": 2.0, "ordine": 0.5, "ticket": -0.5, "pacco": -1.0},
    "ordine": {"ticket": 1.8, "pacco": 0.4, "ritardo": 0.2, "ordine": -1.0},
}


def probabilities(context, temperature=1.0):
    if temperature <= 0:
        raise ValueError("temperature must be positive")
    logits = BIGRAM.get(context, {t: 0.0 for t in VOCAB})
    vals = [logits[t] / temperature for t in VOCAB]
    m = max(vals)
    ex = [math.exp(v - m) for v in vals]
    s = sum(ex)
    return {t: v / s for t, v in zip(VOCAB, ex)}


def demo():
    return {"pacco": probabilities("pacco"), "ordine": probabilities("ordine")}


def checks():
    d = demo()
    return {
        "normalized": all(abs(sum(x.values()) - 1) < 1e-12 for x in d.values()),
        "context_changes": d["pacco"] != d["ordine"],
        "greedy": max(d["pacco"], key=d["pacco"].get) == "ritardo",
    }
