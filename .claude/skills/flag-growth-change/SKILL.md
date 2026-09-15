---
name: flag-growth-change
description: Package a real signup/conversion jump, drop, or flatline and deliver it to aegis-ceo; claim escalated only after confirmed delivery
allowed-tools: Bash, Read, Write, mcp__trinity__chat_with_agent, mcp__trinity__report, mcp__trinity__list_reports
user-invocable: true
metadata:
  version: "1.0"
  created: 2026-09-15
  author: aegis-growth
---

# Flag Growth Change

## Purpose

Escalate a concrete growth signal to `aegis-ceo`. Advisory only — do not remediate, rewrite marketing, or claim causation you cannot verify.

## Process

### Step 1: Package the signal

Include:

- Exact figures (before / after) and field paths
- Window (timestamps)
- Whether this is a jump, drop, or flatline
- Correlation context only if labeled as such

### Step 2: Deliver to aegis-ceo

Call `mcp__trinity__chat_with_agent` with `name: "aegis-ceo"` and a message that starts with `/handle-anomaly` or a clear growth-escalation framing, plus `source=aegis-growth`.

### Step 3: Confirm delivery

Claim **"escalated"** only after confirmed delivery. On failure: say **"flagged, delivery failed"** and append an operator-queue alert if headless.

### Step 4: Record

Append to `memory/findings.md` with delivery status.

### Step 5: Trinity report (when available)

- `report_type`: `aegis_growth.change_flag`
- `display_hint`: `markdown`
- Guard: skip silently if unavailable

## Outputs

- Confirmed (or failed) delivery to `aegis-ceo`
- `memory/findings.md` entry
