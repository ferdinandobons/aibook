"""Esempio JAX: funzione pura, grad, vmap e jit sullo stesso contratto."""

from __future__ import annotations

import json

import jax
import jax.numpy as jnp


def predict(params: dict[str, jax.Array], x: jax.Array) -> jax.Array:
    return jnp.tanh(x @ params["weight"] + params["bias"])


def mse(params: dict[str, jax.Array], x: jax.Array, target: jax.Array) -> jax.Array:
    prediction = jax.vmap(predict, in_axes=(None, 0))(params, x)
    return jnp.mean((prediction - target) ** 2)


def run_example() -> dict[str, object]:
    params = {
        "weight": jnp.array([[0.4, -0.2], [0.1, 0.3]], dtype=jnp.float32),
        "bias": jnp.array([0.05, -0.10], dtype=jnp.float32),
    }
    x = jnp.array([[1.0, -1.0], [0.5, 2.0]], dtype=jnp.float32)
    target = jnp.zeros((2, 2), dtype=jnp.float32)

    batched_predict = jax.jit(jax.vmap(predict, in_axes=(None, 0)))
    predictions = batched_predict(params, x)
    loss, gradients = jax.value_and_grad(mse)(params, x, target)

    return {
        "shape": list(predictions.shape),
        "predictions": jnp.round(predictions, 6).tolist(),
        "loss": round(float(loss), 6),
        "gradient_shapes": {
            "weight": list(gradients["weight"].shape),
            "bias": list(gradients["bias"].shape),
        },
    }


if __name__ == "__main__":
    print(json.dumps(run_example(), ensure_ascii=False, sort_keys=True))
