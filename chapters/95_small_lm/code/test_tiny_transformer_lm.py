from __future__ import annotations

import unittest

import torch

from tiny_transformer_lm import CORPUS, CharTokenizer, TinyCausalLM, build_training_batch, train_and_generate


class TinyTransformerLMTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.result = train_and_generate()

    def test_training_reduces_loss_and_preserves_shift(self):
        self.assertLess(self.result["final_loss"], self.result["initial_loss"])
        self.assertTrue(self.result["target_shift_verified"])

    def test_generation_starts_from_declared_prompt(self):
        self.assertTrue(self.result["generated"].startswith("il modello"))
        self.assertGreater(len(self.result["generated"]), len("il modello"))

    def test_causal_model_rejects_oversized_context(self):
        tokenizer = CharTokenizer(CORPUS)
        model = TinyCausalLM(len(tokenizer.tokens), context=4)
        with self.assertRaises(ValueError):
            model(torch.zeros((1, 5), dtype=torch.long))

    def test_batch_has_explicit_next_token_targets(self):
        tokenizer = CharTokenizer(CORPUS)
        inputs, targets = build_training_batch(tokenizer.encode(CORPUS), 8)
        self.assertTrue(torch.equal(inputs[:, 1:], targets[:, :-1]))


if __name__ == "__main__":
    unittest.main(verbosity=2)
