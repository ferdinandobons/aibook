from __future__ import annotations

import unittest

from snip_calc_001_manual_autograd import (
    INITIAL,
    accumulated_gradient,
    autograd_gradients,
    finite_difference_gradients,
    gradcheck_passes,
    manual_forward_backward,
)


class CalculusBackpropTests(unittest.TestCase):
    def test_forward_values(self) -> None:
        forward, _ = manual_forward_backward(*INITIAL)
        self.assertAlmostEqual(forward.z, 2.5)
        self.assertAlmostEqual(forward.h, 0.9866142981514303)
        self.assertAlmostEqual(forward.y_hat, -0.4906300087060012)
        self.assertAlmostEqual(forward.loss, 0.39661090620382594)

    def test_manual_matches_autograd(self) -> None:
        forward, manual = manual_forward_backward(*INITIAL)
        autograd_loss, automatic = autograd_gradients()
        self.assertAlmostEqual(forward.loss, autograd_loss)
        for name in ("w1", "b1", "w2", "b2"):
            self.assertAlmostEqual(
                getattr(manual, name), getattr(automatic, name), places=12
            )

    def test_finite_differences_match_manual(self) -> None:
        _, manual = manual_forward_backward(*INITIAL)
        numerical = finite_difference_gradients()
        for name in ("w1", "b1", "w2", "b2"):
            self.assertAlmostEqual(
                getattr(manual, name), getattr(numerical, name), places=7
            )

    def test_gradcheck(self) -> None:
        self.assertTrue(gradcheck_passes())

    def test_backward_accumulates_gradients(self) -> None:
        first, second = accumulated_gradient()
        self.assertEqual(first, 4.0)
        self.assertEqual(second, 8.0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
