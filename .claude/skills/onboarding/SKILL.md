---
name: onboarding
description: Track your setup progress — shows what's done, what's next, and walks you through each step
allowed-tools: Read, Write, Edit, Bash, AskUserQuestion
user-invocable: true
metadata:
  version: "1.0"
  created: 2026-09-15
  author: aegis-growth
---

# Onboarding

Track and continue setup. Reads `onboarding.json`, shows status, walks the next incomplete step.

## Process

### Step 1: Load State

Read `onboarding.json`. If missing, say onboarding is complete or the file was removed.

### Step 2: Show Progress

Checklist by phase with the current phase marked. Report Progress N/M.

### Step 3: Guide Next Step

**env_configured:** `cp .env.example .env` and set `CORP_READONLY_TOKEN` (never `AEGIS_INTERNAL_TOKEN`).

**first_skill_run:** run `/trial-report` successfully.

**plugins_installed:**
```
/plugin install agent-dev@abilityai
/plugin install trinity@abilityai
```

**onboarded:** `/trinity:onboard` from this directory (prefer GitHub-repo deploy).

**free_pool_auth:** confirm with Hamid/`aegis-infra` that OmniRoute free-pool auth is applied (new agents often land on Claude Pro).

**first_remote_run:** `mcp__trinity__chat_with_agent` with `/trial-report` or `/check-growth`.

**schedules_configured / first_scheduled_run:** leave `enabled: false` until trial approved; then toggle via Trinity.

### Step 4: Update State

Mark steps done; advance phase when complete.

## Outputs

- Updated `onboarding.json`
- Guidance for the current step
