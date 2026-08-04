from __future__ import annotations

import unittest

from replication_protocol import Protocol, replicate, run_trial


class ReplicationProtocolTests(unittest.TestCase):
    def setUp(self):
        self.protocol = Protocol(probability=0.70, samples=1000, tolerance=0.05)

    def test_independent_replica_is_within_declared_tolerance(self):
        result = replicate(self.protocol)
        self.assertNotEqual(result["original"]["seed"], result["replica"]["seed"])
        self.assertTrue(result["within_declared_tolerance"])

    def test_protocol_and_output_are_deterministic(self):
        self.assertEqual(replicate(self.protocol), replicate(self.protocol))

    def test_seed_changes_the_sample_not_the_protocol(self):
        self.assertNotEqual(run_trial(self.protocol, 1)["successes"], run_trial(self.protocol, 2)["successes"])

    def test_invalid_sample_size_is_rejected(self):
        with self.assertRaises(ValueError):
            run_trial(Protocol(probability=0.70, samples=10, tolerance=0.05), 1)


if __name__ == "__main__":
    unittest.main(verbosity=2)
