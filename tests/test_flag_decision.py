import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import check_growth as cg
import flag_decision as fd


class FlagDecisionTest(unittest.TestCase):
    def test_new_date_same_count_is_not_movement(self):
        self.assertEqual(cg.movement("0 on 2026-10-09", "0 on 2026-10-08"), "no meaningful movement")

    def test_same_count_does_not_escalate(self):
        escalate, reason = fd.decide({"signups": "0 on 2026-10-09", "previous": "0 on 2026-10-08"})
        self.assertFalse(escalate)
        self.assertIn("unchanged at 0", reason)

    def test_no_counts_does_not_escalate(self):
        self.assertFalse(fd.decide({"signups": "empty (no days returned)", "previous": None})[0])
        self.assertFalse(fd.decide(None)[0])

    def test_real_jump_escalates(self):
        escalate, message = fd.decide({"signups": "3 on 2026-10-09", "previous": "0 on 2026-10-08"})
        self.assertTrue(escalate)
        self.assertIn("jump", message)
        self.assertIn("source=aegis-growth", message)


if __name__ == "__main__":
    unittest.main()
