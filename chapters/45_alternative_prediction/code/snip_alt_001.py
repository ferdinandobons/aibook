from __future__ import annotations
import random

MASK = 256


def encode(text):
    return list(text.encode("utf-8"))


def decode(values):
    return bytes(values).decode("utf-8")


def targets(tokens, h):
    return [
        [tokens[i + k] if i + k < len(tokens) else None for i in range(len(tokens))]
        for k in range(1, h + 1)
    ]


def corrupt(tokens, p, seed):
    rng = random.Random(seed)
    return [MASK if rng.random() < p else x for x in tokens]


def reveal(masked, original, fraction):
    out = list(masked)
    indices = [i for i, x in enumerate(out) if x == MASK]
    count = max(1, round(len(indices) * fraction)) if indices else 0
    for i in indices[:count]:
        out[i] = original[i]
    return out


def demo():
    text = "pacco 📦"
    b = encode(text)
    c = corrupt(b, 0.4, 7)
    r = reveal(c, b, 0.5)
    return {
        "roundtrip": decode(b),
        "targets": targets(b[:4], 2),
        "masked_before": c.count(MASK),
        "masked_after": r.count(MASK),
    }


def checks():
    d = demo()
    return {
        "roundtrip": d["roundtrip"] == "pacco 📦",
        "horizons": d["targets"][0] == [97, 99, 99, None],
        "denoise": d["masked_after"] < d["masked_before"],
    }
