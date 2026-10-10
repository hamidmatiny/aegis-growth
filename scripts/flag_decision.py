#!/usr/bin/env python3
"""Decide whether a growth change is worth escalating to aegis-ceo.

No network. Reads memory/growth-baseline.json written by check_growth.py and
prints either "Escalate: no — <reason>" or "Escalate: yes" plus the message to send.
The model only acts on this output.
"""

from __future__ import annotations

import json
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from check_growth import count_of  # noqa: E402


def decide(baseline: dict | None) -> tuple[bool, str]:
    baseline = baseline or {}
    current, previous = baseline.get("signups"), baseline.get("previous")
    now, before = count_of(current), count_of(previous)
    if now is None or before is None:
        return False, f"no comparable signup counts (now: {current or 'none'}, before: {previous or 'none'})"
    if now == before:
        return False, f"signups unchanged at {now}"
    kind = "jump" if now > before else "drop"
    message = (
        "Growth escalation from aegis-growth (source=aegis-growth). "
        f"Signups {kind}: {previous} -> {current}. "
        "Field: /api/corp/v1/bev/trajectory signup_history_14d (latest day). "
        "Advisory only; no causation claimed."
    )
    return True, message


def main() -> int:
    if Path("/home/developer").is_dir():
        os.chdir("/home/developer")
    path = Path("memory/growth-baseline.json")
    baseline = json.loads(path.read_text()) if path.is_file() else None
    escalate, text = decide(baseline)
    if escalate:
        print("Escalate: yes")
        print(text)
    else:
        print(f"Escalate: no — {text}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
