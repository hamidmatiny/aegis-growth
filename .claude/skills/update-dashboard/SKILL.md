---
name: update-dashboard
description: Refresh dashboard.yaml with current growth metrics from baselines and findings
allowed-tools: Read, Write, Edit, Bash, Glob, Grep, mcp__trinity__report
user-invocable: true
metadata:
  version: "1.0"
  created: 2026-09-15
  author: aegis-growth
---

# Update Dashboard

Refresh `dashboard.yaml` from `memory/growth-baselines.md` and recent findings.

## Process

### Step 1: Gather Metrics

Read baselines and findings. Note last check timestamp and latest signup figures.

### Step 2: Update Dashboard

Update widget values and `updated` timestamp.

### Step 3: KPI snapshot report (Trinity)

If `mcp__trinity__report` available: `report_type: aegis_growth.kpi_snapshot`, `display_hint: kpi`. Skip silently otherwise.

### Step 4: Confirm

Report what changed.

## Outputs

- Updated `dashboard.yaml`
