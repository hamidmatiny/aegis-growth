---
name: check-growth
description: Query corp-orchestrator's read-only API for real signup/conversion figures and report deltas plainly — no spin, no unverified causation
allowed-tools: Bash, Read, Write, WebFetch, mcp__trinity__list_reports, mcp__trinity__report, mcp__trinity__chat_with_agent
user-invocable: true
metadata:
  version: "1.0"
  created: 2026-09-15
  author: aegis-growth
---

# Check Growth

## Purpose

Read AEGIS's real signup/conversion numbers from corp-orchestrator's read-only API and report them exactly as returned, with deltas vs the last known baseline — including when the honest answer is "no meaningful movement."

## Process

### Step 1: Confirm the credential

`CORP_READONLY_TOKEN` lives in `/home/developer/.env` (Trinity credentials). It is **not** always exported into the process environment — scheduled/headless shells often see an empty `printenv`. Always load it before any API call:

```bash
set -a
[ -f /home/developer/.env ] && . /home/developer/.env
[ -f .env ] && . ./.env
set +a
```

Then verify: `test -n "$CORP_READONLY_TOKEN"` (expect non-empty). If still empty: ask Hamid; never substitute `AEGIS_INTERNAL_TOKEN`; stop. Do **not** treat a 401/`admin login required` as an expired token until you have confirmed the env was actually loaded — empty Bearer produces that exact error.

### Step 2: Query the endpoints (GET only)

Prefer **`curl`** (not bare `urllib` / default Python User-Agent). Cloudflare returns **403 / error code 1010** when the client UA looks like a bot — that is **not** a bad token. Always send a real UA:

```bash
curl -sS -H "Authorization: Bearer $CORP_READONLY_TOKEN" \
  -H "User-Agent: aegis-growth/1.0 (+https://defenseaegis.org)" \
  https://defenseaegis.org/api/corp/v1/bev/summary
curl -sS -H "Authorization: Bearer $CORP_READONLY_TOKEN" \
  -H "User-Agent: aegis-growth/1.0 (+https://defenseaegis.org)" \
  https://defenseaegis.org/api/corp/v1/bev/trajectory
```

If you must use Python, set the same `User-Agent` header on `urllib.request.Request`.

Extract only growth-relevant fields that actually exist, e.g.:

- `signup_history_14d` (and any per-day signup counts)
- Paying / conversion-adjacent fields **only if present** on the endpoint that owns them (do not invent conversion rate)
- `mrr_snapshot` figures only as context if useful for conversion framing — do not steal Finance's job; prefer signup movement

Missing field → say "not returned by the API."

### Step 3: Compare to baseline

Read `memory/growth-baselines.md` if present. If `mcp__trinity__list_reports` is available, also check the latest `aegis_growth.growth_snapshot`.

State unchanged / up / down / flatline with the actual numbers.

### Step 4: Report (no spin, no causation claims)

Output:

- Figures as returned
- Delta vs last check of **the same field**
- Optional correlation note only if a known event shares the window (e.g. landing redesign) — label it as correlation, not cause
- If nothing meaningful moved: say so plainly

### Step 5: Update baseline memory

Append/update `memory/growth-baselines.md` with today's figures and ISO timestamp.

### Step 6: Escalate if warranted

If there is a real jump, drop, or multi-period flatline that should reach `aegis-ceo`, hand off to `/flag-growth-change` with the exact figures and JSON paths.

### Step 7: Publish Trinity report (when available)

- `report_type`: `aegis_growth.growth_snapshot`
- `display_hint`: `kpi`
- `payload`: tiles + `checked_at` + source URLs
- Guard: skip silently if tool unavailable / agent-scoped key refused

## Outputs

- Plain growth report with real numbers and deltas
- Updated `memory/growth-baselines.md`
- Optional handoff to `/flag-growth-change`
