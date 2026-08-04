from __future__ import annotations

from dataclasses import dataclass
import math

import torch


X = 2.0
TARGET = 0.4
INITIAL = (1.5, -0.5, -0.7, 0.2)


@dataclass(frozen=True)
class ForwardValues:
    z: float
    h: float
    y_hat: float
    loss: float


@dataclass(frozen=True)
class Gradients:
    w1: float
    b1: float
    w2: float
    b2: float


def manual_forward_backward(
    w1: float,
    b1: float,
    w2: float,
    b2: float,
) -> tuple[ForwardValues, Gradients]:
    z = w1 * X + b1
    h = math.tanh(z)
    y_hat = w2 * h + b2
    error = y_hat - TARGET
    loss = 0.5 * error**2

    dloss_dy = error
    dloss_dw2 = dloss_dy * h
    dloss_db2 = dloss_dy
    dloss_dh = dloss_dy * w2
    dh_dz = 1.0 - h**2
    dloss_dz = dloss_dh * dh_dz
    dloss_dw1 = dloss_dz * X
    dloss_db1 = dloss_dz

    return (
        ForwardValues(z=z, h=h, y_hat=y_hat, loss=loss),
        Gradients(w1=dloss_dw1, b1=dloss_db1, w2=dloss_dw2, b2=dloss_db2),
    )


def torch_loss(
    w1: torch.Tensor,
    b1: torch.Tensor,
    w2: torch.Tensor,
    b2: torch.Tensor,
) -> torch.Tensor:
    x = torch.tensor(X, dtype=torch.float64)
    target = torch.tensor(TARGET, dtype=torch.float64)
    z = w1 * x + b1
    h = torch.tanh(z)
    y_hat = w2 * h + b2
    return 0.5 * (y_hat - target) ** 2


def autograd_gradients() -> tuple[float, Gradients]:
    parameters = [
        torch.tensor(value, dtype=torch.float64, requires_grad=True)
        for value in INITIAL
    ]
    loss = torch_loss(*parameters)
    loss.backward()
    gradients = Gradients(*(parameter.grad.item() for parameter in parameters))
    return loss.item(), gradients


def finite_difference_gradients(epsilon: float = 1e-6) -> Gradients:
    values = list(INITIAL)
    approximations: list[float] = []
    for index in range(len(values)):
        plus = values.copy()
        minus = values.copy()
        plus[index] += epsilon
        minus[index] -= epsilon
        loss_plus = manual_forward_backward(*plus)[0].loss
        loss_minus = manual_forward_backward(*minus)[0].loss
        approximations.append((loss_plus - loss_minus) / (2.0 * epsilon))
    return Gradients(*approximations)


def gradcheck_passes() -> bool:
    parameters = tuple(
        torch.tensor(value, dtype=torch.float64, requires_grad=True)
        for value in INITIAL
    )
    return bool(
        torch.autograd.gradcheck(torch_loss, parameters, eps=1e-6, atol=1e-5, rtol=1e-3)
    )


def accumulated_gradient() -> tuple[float, float]:
    value = torch.tensor(2.0, dtype=torch.float64, requires_grad=True)
    (value**2).backward()
    first = value.grad.item()
    (value**2).backward()
    second = value.grad.item()
    return first, second


def main() -> None:
    forward, manual_gradients = manual_forward_backward(*INITIAL)
    autograd_loss, autograd_values = autograd_gradients()
    finite_difference_values = finite_difference_gradients()
    first_accumulated, second_accumulated = accumulated_gradient()

    print(f"z: {forward.z:.6f}")
    print(f"h: {forward.h:.6f}")
    print(f"y_hat: {forward.y_hat:.6f}")
    print(f"loss: {forward.loss:.6f}")
    print(f"autograd_loss: {autograd_loss:.6f}")
    print(f"manual_gradients: {manual_gradients}")
    print(f"autograd_gradients: {autograd_values}")
    print(f"finite_difference_gradients: {finite_difference_values}")
    print(f"gradcheck_passes: {gradcheck_passes()}")
    print(f"accumulated_gradient_after_first_backward: {first_accumulated:.1f}")
    print(f"accumulated_gradient_after_second_backward: {second_accumulated:.1f}")


if __name__ == "__main__":
    main()
