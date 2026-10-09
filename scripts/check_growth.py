#!/usr/bin/env python3
"""Read signup movement. The model only posts this script's stdout.

GET only. CORP_READONLY_TOKEN only.
"""

from __future__ import annotations

import json
import os
import sys
import urllib.error
import urllib.request
from pathlib import Path

SUMMARY_URL = "https://defenseaegis.org/api/corp/v1/bev/summary"
TRAJECTORY_URL = "https://defenseaegis.org/api/corp/v1/bev/trajectory"
UA = "Mozilla/5.0 (compatible; aegis-growth/1.0; +https://defenseaegis.org)"


def load_dotenv(path: Path) -> None:
    if not path.is_file():
        return
    for line in path.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        if key and key not in os.environ:
            os.environ[key] = value


def _get(url: str, token: str) -> tuple[int, dict]:
    req = urllib.request.Request(
        url,
        headers={"Authorization": f"Bearer {token}", "User-Agent": UA},
        method="GET",
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            body = resp.read().decode()
            return resp.status, json.loads(body) if body else {}
    except urllib.error.HTTPError as exc:
        raw = exc.read().decode(errors="replace")
        try:
            payload = json.loads(raw) if raw else {}
        except json.JSONDecodeError:
            payload = {"error": raw[:200]}
        return exc.code, payload


def latest_day(trajectory: dict) -> dict | None:
    hist = trajectory.get("signup_history_14d") if isinstance(trajectory, dict) else None
    if not isinstance(hist, list) or not hist or not isinstance(hist[-1], dict):
        return None
    return hist[-1]


def signups_line(trajectory: dict) -> str:
    hist = trajectory.get("signup_history_14d") if isinstance(trajectory, dict) else None
    if isinstance(hist, list) and not hist:
        return "empty (no days returned)"
    last = latest_day(trajectory)
    if not last or "signups" not in last:
        return "not returned by the API"
    day = last.get("date") or last.get("day") or ""
    return f"{last['signups']}" + (f" on {day}" if day else "")


def movement(current: str, previous: str | None) -> str:
    if not previous:
        return "no prior baseline"
    if current == previous:
        return "no meaningful movement"
    return f"was {previous}"


def render(trajectory: dict, baseline: dict | None) -> str:
    signups = signups_line(trajectory)
    previous = (baseline or {}).get("signups")
    return "\n".join(
        [
            "Task: /check-growth",
            "What I did: GET /api/corp/v1/bev/trajectory (signup_history_14d)",
            f"Signups: {signups}",
            f"Movement: {movement(signups, previous)}",
            "Outcome: success",
        ]
    )


def main() -> int:
    if Path("/home/developer").is_dir():
        os.chdir("/home/developer")
    for candidate in (Path("/home/developer/.env"), Path(".env")):
        load_dotenv(candidate)
    token = os.environ.get("CORP_READONLY_TOKEN", "")
    if not token:
        print("Task: /check-growth")
        print("Outcome: failure")
        print("CORP_READONLY_TOKEN is missing. No other credential was used.")
        return 1
    summary_status, _summary = _get(SUMMARY_URL, token)
    traj_status, trajectory = _get(TRAJECTORY_URL, token)
    if summary_status == 403 or traj_status == 403:
        print("Task: /check-growth")
        print("Outcome: failure")
        print("HTTP 403 from defenseaegis.org. This is the Cloudflare check, not a rotated token.")
        return 1
    if summary_status == 401 or traj_status == 401:
        print("Task: /check-growth")
        print("Outcome: failure")
        print("HTTP 401. CORP_READONLY_TOKEN was rejected.")
        return 1
    if traj_status != 200:
        print("Task: /check-growth")
        print("Outcome: failure")
        print(f"HTTP trajectory={traj_status}")
        return 1
    baseline_path = Path("memory/growth-baseline.json")
    baseline = None
    if baseline_path.is_file():
        baseline = json.loads(baseline_path.read_text())
    print(render(trajectory, baseline))
    baseline_path.parent.mkdir(parents=True, exist_ok=True)
    baseline_path.write_text(json.dumps({"signups": signups_line(trajectory)}, indent=2) + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
