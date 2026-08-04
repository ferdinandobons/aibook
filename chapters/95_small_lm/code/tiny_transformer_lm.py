"""Un language model causale minuscolo, addestrato e campionato su CPU."""

from __future__ import annotations

import json
import random

import torch
from torch import nn


CORPUS = ("il modello legge token e predice il token seguente. " * 5).strip()


class CharTokenizer:
    def __init__(self, text: str):
        self.tokens = sorted(set(text))
        self.to_id = {token: index for index, token in enumerate(self.tokens)}
        self.to_token = {index: token for token, index in self.to_id.items()}

    def encode(self, text: str) -> list[int]:
        return [self.to_id[token] for token in text]

    def decode(self, ids: list[int]) -> str:
        return "".join(self.to_token[index] for index in ids)


class TinyCausalLM(nn.Module):
    def __init__(self, vocab_size: int, context: int = 16, width: int = 24):
        super().__init__()
        self.context = context
        self.token = nn.Embedding(vocab_size, width)
        self.position = nn.Embedding(context, width)
        layer = nn.TransformerEncoderLayer(
            d_model=width,
            nhead=4,
            dim_feedforward=48,
            dropout=0.0,
            activation="gelu",
            batch_first=True,
            norm_first=True,
        )
        self.blocks = nn.TransformerEncoder(
            layer, num_layers=1, enable_nested_tensor=False
        )
        self.norm = nn.LayerNorm(width)
        self.head = nn.Linear(width, vocab_size, bias=False)

    def forward(self, token_ids: torch.Tensor) -> torch.Tensor:
        if token_ids.ndim != 2 or token_ids.shape[1] > self.context:
            raise ValueError("atteso un batch [B, T] con T entro la context window")
        positions = torch.arange(token_ids.shape[1], device=token_ids.device)
        hidden = self.token(token_ids) + self.position(positions)
        mask = torch.triu(
            torch.ones(
                token_ids.shape[1],
                token_ids.shape[1],
                dtype=torch.bool,
                device=token_ids.device,
            ),
            diagonal=1,
        )
        hidden = self.blocks(hidden, mask=mask, is_causal=True)
        return self.head(self.norm(hidden))


def build_training_batch(
    ids: list[int], context: int
) -> tuple[torch.Tensor, torch.Tensor]:
    if len(ids) <= context:
        raise ValueError("il corpus deve contenere più token della context window")
    inputs = [ids[start : start + context] for start in range(len(ids) - context)]
    targets = [
        ids[start + 1 : start + context + 1] for start in range(len(ids) - context)
    ]
    return torch.tensor(inputs, dtype=torch.long), torch.tensor(
        targets, dtype=torch.long
    )


# BOOK-EXCERPT-START
def train_and_generate(steps: int = 24) -> dict[str, object]:
    if steps <= 0:
        raise ValueError("steps deve essere positivo")
    random.seed(7)
    torch.manual_seed(7)
    torch.use_deterministic_algorithms(True)

    tokenizer = CharTokenizer(CORPUS)
    model = TinyCausalLM(len(tokenizer.tokens))
    inputs, targets = build_training_batch(tokenizer.encode(CORPUS), model.context)
    optimizer = torch.optim.AdamW(model.parameters(), lr=0.01)

    losses: list[float] = []
    model.train()
    for _ in range(steps):
        optimizer.zero_grad(set_to_none=True)
        logits = model(inputs)
        loss = nn.functional.cross_entropy(
            logits.reshape(-1, logits.shape[-1]), targets.reshape(-1)
        )
        loss.backward()
        optimizer.step()
        losses.append(float(loss.detach()))

    model.eval()
    generated = tokenizer.encode("il modello")
    with torch.inference_mode():
        for _ in range(18):
            context = torch.tensor([generated[-model.context :]], dtype=torch.long)
            next_id = int(model(context)[0, -1].argmax())
            generated.append(next_id)

    return {
        "vocab_size": len(tokenizer.tokens),
        "context": model.context,
        "initial_loss": round(losses[0], 6),
        "final_loss": round(losses[-1], 6),
        "generated": tokenizer.decode(generated),
        "target_shift_verified": bool(torch.equal(inputs[:, 1:], targets[:, :-1])),
    }


# BOOK-EXCERPT-END


if __name__ == "__main__":
    print(json.dumps(train_and_generate(), ensure_ascii=False, sort_keys=True))
