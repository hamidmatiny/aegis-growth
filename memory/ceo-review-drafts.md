# Drafts awaiting CEO / Hamid review (do not publish)

Standing constraints: zero budget, zero cold outreach, no personal posting by Hamid without explicit approval. These are **drafts only** — route via `aegis-ceo` before any public post.

**Product positioning (Hamid, 2026-09-17 — standing):** Sell the **enforcer/gateway** only. Autonomous-agent / SMB-copilot narrative is **shelved** from all public material until the agent R&D competence bar is met (see `memory/agent-rd-competence-bar.md`).

---

## Draft A — Show HN (Hacker News) — REVISED 2026-09-17

**Target:** https://news.ycombinator.com/submit (Show HN)  
**Status:** Draft for CEO review — revised after enforcer/gateway repositioning  
**Who posts:** Hamid (his account / voice) after approval  

**Removed overclaim:** prior draft sold “SMB security copilot” + $29 walkthroughs as a co-equal product. That path is internal R&D, not the public pitch.

**Title (≤80 chars):**
```
Show HN: AEGIS – open-source LLM security gateway (policy + audit + human gate)
```

**Body:**
```
I built AEGIS as a governance layer that sits between your own internal app and whatever LLM provider you use — not as another chat product.

What it does today:
- Policy-as-code (CEL) over prompts / tool calls
- Four-tier risk governance: LOW / MEDIUM / HIGH / IRREVERSIBLE
- Human-approval gating for high-risk tool use
- Tamper-evident Ed25519 audit trail

Category neighbors: LLM Guard / Rebuff / Vigil-style defenses, plus stronger tool-call governance.

Repo: https://github.com/hamidmatiny/aegis

Honest status: still early ($0 MRR). Looking for feedback from teams wiring their own internal LLM apps who need an enforcer they can actually audit — not a black-box “AI security” SaaS.
```

---

## Draft B — Reddit — REVISED 2026-09-17 (gateway-adjacent; not SMB-copilot pitch)

**Status:** Draft for CEO review — revised; prior CVE/SMB-owner draft shelved as wrong ICP for the active sale  
**Constraint:** Value-first; not a launch spam post. Prefer r/LocalLLaMA, r/selfhosted, or r/netsec over SMB-owner subs until copilot is real. Adapt subreddit rules before posting.

**Title:**
```
What do you put between your internal app and the LLM provider for tool-call risk?
```

**Body (skeleton — CEO should edit for Hamid’s voice):**
```
If you run an internal chatbot / tool that can call functions or touch systems, how do you stop a bad completion from doing something irreversible?

Patterns I’ve seen:
1) Prompt filters only (injection scanners) — necessary, not sufficient once tools exist
2) Hard-coded allowlists in app code — drifts, no audit story
3) A real policy + approval + audit layer in front of the provider

I’ve been building an open-source gateway for (3): CEL policy-as-code, LOW/MEDIUM/HIGH/IRREVERSIBLE tiers, human gate for high-risk tool calls, Ed25519-signed audit trail.

Repo: https://github.com/hamidmatiny/aegis

Curious what others run in production for the same seat — especially if you’ve tried LLM Guard / similar and hit a gap on tool-call governance.
```

---

## Shelved (do not publish under current positioning)

- Prior Show HN “gateway + SMB security copilot” + $29 walkthrough ask
- Prior Reddit “CVE relevant to me?” SMB-owner draft (fine as future R&D marketing *after* competence bar; wrong primary sale now)

---

## Preferred first post (2026-09-23) — review this before Show HN

The product-launch Show HN above is the wrong first artifact. The post to review is the bypass-to-fix write-up:

`memory/draft-iac-credential-bypass-writeup-2026-09-23.md`

Do not publish it until Hamid says so. Channel order and the pricing shape are in `memory/gtm-icp-channels-pricing-2026-09-23.md`.

## Not drafted here (needs different channel)

- Product Hunt launch materials — scout listed; needs dedicated launch day + assets; not started; when started → **gateway-only** copy
- SaaSHub / G2 / Capterra / BetaList — see `directory-submissions.md` (packets rewritten for gateway; SaaSHub live listing still needs human edit)
