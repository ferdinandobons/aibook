"""SNIP-AI-001. Separare training e inference con un modello lineare."""

from __future__ import annotations

from dataclasses import dataclass

import torch
from torch import nn


@dataclass(frozen=True)
class DemoResult:
    initial_loss: float
    final_loss: float
    training_parameters_changed: bool
    inference_parameters_changed: bool
    inference_logits: torch.Tensor
    predicted_class: int


def parameters_changed(before: list[torch.Tensor], model: nn.Module) -> bool:
    """Restituisce True quando almeno un parametro differisce dalla copia iniziale."""
    return any(
        not torch.equal(old, new.detach())
        for old, new in zip(before, model.parameters())
    )


def run_demo() -> DemoResult:
    """Addestra un classificatore toy e verifica che l'inference non aggiorni i pesi."""
    torch.manual_seed(7)

    features = torch.tensor(
        [[2.0, 0.0], [1.5, 0.2], [0.0, 2.0], [0.2, 1.5]],
        dtype=torch.float32,
    )
    labels = torch.tensor([0, 0, 1, 1], dtype=torch.long)

    model = nn.Linear(2, 2)
    loss_fn = nn.CrossEntropyLoss()
    optimizer = torch.optim.SGD(model.parameters(), lr=0.1)

    with torch.no_grad():
        initial_loss = loss_fn(model(features), labels).item()

    parameters_before_training = [
        parameter.detach().clone() for parameter in model.parameters()
    ]

    model.train()
    for _ in range(100):
        optimizer.zero_grad()
        logits = model(features)
        loss = loss_fn(logits, labels)
        loss.backward()
        optimizer.step()

    with torch.no_grad():
        final_loss = loss_fn(model(features), labels).item()

    training_parameters_changed = parameters_changed(parameters_before_training, model)

    model.eval()
    parameters_before_inference = [
        parameter.detach().clone() for parameter in model.parameters()
    ]

    new_input = torch.tensor([[1.8, 0.1]], dtype=torch.float32)
    with torch.inference_mode():
        inference_logits = model(new_input)
        predicted_class = int(inference_logits.argmax(dim=-1).item())

    inference_parameters_changed = parameters_changed(
        parameters_before_inference, model
    )

    return DemoResult(
        initial_loss=initial_loss,
        final_loss=final_loss,
        training_parameters_changed=training_parameters_changed,
        inference_parameters_changed=inference_parameters_changed,
        inference_logits=inference_logits,
        predicted_class=predicted_class,
    )


if __name__ == "__main__":
    torch.set_printoptions(precision=4, sci_mode=False)
    result = run_demo()
    print(f"initial_loss: {result.initial_loss:.6f}")
    print(f"final_loss: {result.final_loss:.6f}")
    print(f"training_parameters_changed: {result.training_parameters_changed}")
    print(f"inference_parameters_changed: {result.inference_parameters_changed}")
    print("inference_logits:", result.inference_logits)
    print(f"predicted_class: {result.predicted_class}")
