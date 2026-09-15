# AEGIS Growth Architecture (Current State)

**What this is:** the agent as it actually runs today. For where it's headed, see **`TARGET-ARCHITECTURE.md`**.

**Last updated:** 2026-09-15

## Overview

Read-only Growth/Marketing Analyst. Pulls signup/conversion fields from corp-orchestrator BEV endpoints with `CORP_READONLY_TOKEN`, reports deltas, escalates real movement to `aegis-ceo`. Free-pool tier via OmniRoute (auth flip required post-deploy).

## Components

### Skills

- `/check-growth`, `/flag-growth-change`, `/trial-report`
- `/onboarding`, `/update-dashboard`, `/reconcile-docs`

### Subagents

None yet.

### Data & State

- `memory/growth-baselines.md`
- `memory/findings.md`
- `onboarding.json`, `dashboard.yaml`

### Schedules

Declared in `template.yaml` (`enabled: false` until trial approved): daily growth check, dashboard refresh, weekly reconcile-docs.

## Trinity Integration

`template.yaml` resources + credentials (`CORP_READONLY_TOKEN`). Deploy via `/trinity:onboard` from the GitHub repo when ready.
