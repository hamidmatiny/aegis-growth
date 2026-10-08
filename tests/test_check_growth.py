import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import check_growth as cg

TRAJECTORY = {"signup_history_14d": [{"date": "2026-10-07", "signups": 1}, {"date": "2026-10-08", "signups": 0}]}


class CheckGrowthTest(unittest.TestCase):
    def test_latest_day_only(self):
        self.assertEqual(cg.signups_line(TRAJECTORY), "0 on 2026-10-08")

    def test_missing_history(self):
        self.assertEqual(cg.signups_line({}), "not returned by the API")

    def test_flat_and_changed(self):
        self.assertEqual(cg.movement("0 on 2026-10-08", "0 on 2026-10-08"), "no meaningful movement")
        text = cg.render(TRAJECTORY, {"signups": "1 on 2026-10-07"})
        self.assertIn("Movement: was 1 on 2026-10-07", text)
        self.assertIn("Outcome: success", text)


if __name__ == "__main__":
    unittest.main()
