"""Laboratorio completo: dati, baseline, training, eval e manifest."""

from __future__ import annotations

import hashlib
import json

import numpy as np


DATA = np.array(
    [
        [-2.0, -1.0, 0.0],
        [-1.0, -1.5, 0.0],
        [-1.5, 0.2, 0.0],
        [1.0, 1.2, 1.0],
        [1.5, 0.8, 1.0],
        [2.0, 1.5, 1.0],
    ],
    dtype=np.float64,
)


def dataset_digest(data: np.ndarray) -> str:
    if data.ndim != 2 or data.shape[1] != 3:
        raise ValueError("attese due feature e una label per riga")
    return hashlib.sha256(data.tobytes()).hexdigest()[:16]


def sigmoid(values: np.ndarray) -> np.ndarray:
    return 1.0 / (1.0 + np.exp(-np.clip(values, -30.0, 30.0)))


def binary_cross_entropy(probabilities: np.ndarray, labels: np.ndarray) -> float:
    probabilities = np.clip(probabilities, 1e-12, 1.0 - 1e-12)
    return float(-np.mean(labels * np.log(probabilities) + (1.0 - labels) * np.log(1.0 - probabilities)))


# BOOK-EXCERPT-START
def train_classifier(data: np.ndarray, steps: int = 120, learning_rate: float = 0.2) -> dict[str, object]:
    if steps <= 0 or learning_rate <= 0:
        raise ValueError("steps e learning_rate devono essere positivi")
    dataset_digest(data)  # valida shape e rende esplicito l'artefatto usato
    features, labels = data[:, :2], data[:, 2]
    weights = np.zeros(2, dtype=np.float64)
    bias = 0.0

    initial_loss = binary_cross_entropy(sigmoid(features @ weights + bias), labels)
    for _ in range(steps):
        probabilities = sigmoid(features @ weights + bias)
        residual = probabilities - labels
        weights -= learning_rate * (features.T @ residual) / len(features)
        bias -= learning_rate * float(np.mean(residual))

    probabilities = sigmoid(features @ weights + bias)
    predictions = (probabilities >= 0.5).astype(np.float64)
    return {
        "initial_loss": round(initial_loss, 6),
        "final_loss": round(binary_cross_entropy(probabilities, labels), 6),
        "accuracy": round(float(np.mean(predictions == labels)), 6),
        "weights": weights.round(6).tolist(),
        "bias": round(bias, 6),
        "dataset_sha256": dataset_digest(data),
        "rows": int(len(data)),
    }
# BOOK-EXCERPT-END


def run_lab() -> dict[str, object]:
    result = train_classifier(DATA)
    result["baseline_accuracy"] = 0.5
    result["acceptance"] = bool(result["accuracy"] >= 0.95 and result["final_loss"] < result["initial_loss"])
    return result


if __name__ == "__main__":
    print(json.dumps(run_lab(), ensure_ascii=False, sort_keys=True))
