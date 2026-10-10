---
name: flag-growth-change
description: Package a real signup/conversion jump, drop, or flatline and deliver it to aegis-ceo; claim escalated only after confirmed delivery
allowed-tools: Bash, Read, Write, mcp__trinity__chat_with_agent, mcp__trinity__report, mcp__trinity__list_reports, mcp__trinity__list_channel_groups, mcp__trinity__send_group_message
user-invocable: true
metadata:
  version: "1.1"
  created: 2026-09-15
  author: aegis-growth
---

# Flag Growth Change

Escalate a concrete growth signal to `aegis-ceo`. Advisory only — do not remediate, rewrite marketing, or claim causation you cannot verify.

A script decides whether there is anything to escalate. You do not compare numbers yourself.

## Do this

1. Run `python3 /home/developer/scripts/flag_decision.py`.
2. If the first line is `Escalate: no — ...`: do **not** call `aegis-ceo`. Post that line to `#aegis-growth` as the close-out and stop.
3. If the first line is `Escalate: yes`: call `mcp__trinity__chat_with_agent` **once** with `name: "aegis-ceo"` and the script's second line as the message. If the tool offers an async / fire-and-forget option, use it.
   - Never retry, never poll, never wait for aegis-ceo to finish its own work.
   - If the call errors or does not return, the result is **"flagged, delivery failed"** with the error text.
   - Claim **"escalated"** only when the call returned a delivery confirmation.
4. Append one line to `memory/findings.md`: date, the script's message, and `escalated` or `flagged, delivery failed`.
5. If `mcp__trinity__report` is available: `report_type: aegis_growth.change_flag`, `display_hint: markdown`. Skip silently if not.
6. Post the close-out to `#aegis-growth` (what was asked, who asked, the script result, delivery status). No commit trailers.

Do not read other files. Do not fetch the API — `/check-growth` already did.
