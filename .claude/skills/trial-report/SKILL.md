---
name: trial-report
description: One-time initial validation — confirm CORP_READONLY_TOKEN and BEV endpoints, then produce one real growth trial report before any schedule
allowed-tools: Bash, Read, Write, WebFetch, AskUserQuestion, mcp__trinity__report
user-invocable: true
metadata:
  version: "1.0"
  created: 2026-09-15
  author: aegis-growth
---

# Trial Report

## Purpose

Prove credential + API work, and hand Hamid one real (not placeholder) growth report before enabling recurring cadence.

## Process

### Step 1: Confirm credential

`CORP_READONLY_TOKEN` must be set. If missing, ask Hamid and stop.

### Step 2: Confirm reachability

`GET https://defenseaegis.org/api/corp/v1/bev/summary` with the bearer token. Report exact errors on failure — never fabricate figures.

### Step 3: One real check

Run the same query steps as `/check-growth` once end-to-end. Real numbers only.

### Step 4: Present to Hamid

Show signup/conversion figures returned, token OK, API reachable, and whether any change signal was found.

### Step 5: Ask before scheduling

Confirm with Hamid whether to enable the Daily growth check schedule in `template.yaml` (currently `enabled: false`).

### Step 6: Trinity report (when available)

- `report_type`: `aegis_growth.trial_report`
- `display_hint`: `markdown` or `kpi`
- Guard: skip silently if unavailable

## Outputs

- Credential/API confirmation
- One real trial growth report
- Scheduling decision from Hamid
