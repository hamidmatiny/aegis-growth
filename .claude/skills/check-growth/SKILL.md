---
name: check-growth
description: Query corp-orchestrator's read-only API for real signup figures and report the delta
allowed-tools: Bash, mcp__trinity__list_channel_groups, mcp__trinity__send_group_message
user-invocable: true
metadata:
  version: "1.1"
  created: 2026-09-15
  author: aegis-growth
---

# Check Growth

The numbers come from a script. You post them. You do not fetch or parse.

## Do this

1. Run `python3 /home/developer/scripts/check_growth.py`.
2. Call `mcp__trinity__send_group_message` to `#aegis-growth` with that stdout as the message. Do this even when the script exits non-zero.
3. Stop.

Do not read other files. Do not call other agents. Do not invent a signup count the script did not print.

GET-only and `CORP_READONLY_TOKEN` are enforced inside the script. HTTP 403 is Cloudflare, not a dead token. HTTP 401 means the token was rejected.
