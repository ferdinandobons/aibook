from __future__ import annotations
import math


def fit(xs, losses, asymptote):
    ys = [y - asymptote for y in losses]
    if any(y <= 0 for y in ys):
        raise ValueError
    lx = [math.log(x) for x in xs]
    ly = [math.log(y) for y in ys]
    mx = sum(lx) / len(lx)
    my = sum(ly) / len(ly)
    slope = sum((x - mx) * (y - my) for x, y in zip(lx, ly)) / sum(
        (x - mx) ** 2 for x in lx
    )
    return math.exp(my - slope * mx), -slope


def predict(x, L, A, alpha):
    return L + A * x ** (-alpha)


def demo():
    A, a = fit([1, 4, 16], [3, 2, 1.5], 1)
    return {"A": A, "alpha": a, "prediction": predict(64, 1, A, a)}


def checks():
    d = demo()
    return {
        "exponent": abs(d["alpha"] - 0.5) < 1e-10,
        "decreases": d["prediction"] < 1.5,
        "positive": d["A"] > 0,
    }
