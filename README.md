# AEGIS Growth

**Role:** Growth/Marketing Analyst — real signup/conversion numbers, no spin.

Seventh hire in Hamid's personal Trinity agent company. Reports to `aegis-ceo`. Reads corp-orchestrator's read-only BEV API only; never writes; never campaigns.

## Capabilities

- **Check growth** — live signup/conversion deltas (`/check-growth`)
- **Flag growth change** — escalate real jump/drop/flatline to `aegis-ceo` (`/flag-growth-change`)
- **Trial report** — one real validation before scheduling (`/trial-report`)

## Getting Started

```
cd ~/aegis-growth && claude
/onboarding
```

See **[ARCHITECTURE.md](ARCHITECTURE.md)** and **[TARGET-ARCHITECTURE.md](TARGET-ARCHITECTURE.md)**.

## Skills

| Skill | Purpose |
|-------|---------|
| `/check-growth` | Query live signup/conversion data and report deltas |
| `/flag-growth-change` | Escalate a concrete growth signal to aegis-ceo |
| `/trial-report` | One-time initial validation before recurring cadence |
| `/reconcile-docs` | Keep docs, skills, and architecture consistent |
