# Go-to-market: buyer, channels, pricing shape (2026-09-23)

**Status:** Proposal for Hamid. No Track A code, policy, or Stripe change in this document. Landing copy that follows from the audit is [PR #93](https://github.com/hamidmatiny/aegis/pull/93) and is not merged.

**What was checked this pass:** live SaaSHub page, GitHub repo description, `emerging.md` on beyefendi/awesome-llm-security, open awesome-list PRs, landing source on `main` (PR #68 merged 2026-09-20), README lede, unpublished drafts in `memory/ceo-review-drafts.md`, and Portkey’s public pricing page. BEV was **not** re-queried today. The last written BEV snapshot in this repo is still the 2026-09-17 review: **$0.00 CAD MRR**, **0** paying subscribers, one signup on **2026-09-08**. Hamid’s brief for this task states that picture is unchanged ($0 MRR, 0 paying, a single free signup for 8+ days).

---

## 1. Ideal customer

**Buyer:** the engineer or technical founder who owns an application that calls an LLM API and needs a control point in that path.

They already have the product. They need, in the request path:

- policy they can read and change (CEL, not a prompt)
- a risk decision with a human stop on the irreversible tier
- an audit receipt they can show later (Ed25519)
- a base URL they can drop in without rewriting the app (OpenAI-compatible)

**Not the buyer:** a security generalist or small-business owner looking for someone to answer “are we exposed?” or to walk them through a patch. That was the SMB Q&A copilot. It is a side surface on defenseaegis.org. It is not what the repo enforces.

**What the product actually is today**

| Capability | Where it lives |
|------------|----------------|
| CEL policy-as-code, tenant overrides | policy engine |
| Risk tiers LOW / MEDIUM / HIGH / IRREVERSIBLE, human approval before high-risk tool calls | agent-gate |
| Ed25519-signed allow / deny / escalate receipts | audit |
| Drop-in OpenAI-compatible base URL between the app and the provider | gateway |
| Input and output checks, including the credential-framing fixes in #89 and #92 | input-defense / output-defense |

**The job to be done:** “I am shipping an app that calls a model and can take actions. I want a gate I run, with a policy file and an audit log, not a chatbot that advises me.”

**Why the old offer missed them.** The paid SKU is still Standard at **$29 CAD/mo** for guided walkthroughs (`price_1UDYTKKDOQtI1TQzKVuXg6Wd` in the 2026-09-17 review). An engineer integrating a gateway does not buy a walkthrough. Zero pay attempts on that SKU is what that mismatch looks like. It is not evidence that $29 is the wrong *number* for a consumer plan. It is evidence the plan is the wrong *object*.

---

## 2. Public-asset audit

| Asset | What it says now | Verdict |
|--------|------------------|---------|
| Landing hero (`smb-portal/src/pages/Landing.tsx`, live since PR #68) | “Enforce policy between your app and any LLM.” Drop-in base URL. Primary CTA is GitHub. | Matches the buyer. |
| Landing pricing block (same file, before #93) | Featured card was **Standard $29 CAD/mo**, button “Sign up, then upgrade.” | Still the old offer, visually. **PR #93** makes self-host $0 the featured card and labels $29 as the Q&A example only. Not merged. |
| README lede | Led with the SMB CVE checklist next to the live site. | **PR #93** removes that from the lede and marks the guide as legacy SEO in the table. |
| README service table | Modules are still named SMB Copilot / SMB Portal. | Internal names of the example app. Not a sales claim. Leave them. |
| GitHub About (`gh repo view`) | “Open-source AI security gateway **+ AEGIS-for-SMB copilot** … Live at defenseaegis.org.” | Still the old co-sale. Not changed here (repo metadata, not a pull request). Proposed replacement below. |
| https://www.saashub.com/defense-aegis (fetched 2026-09-23) | “AI-native defense-in-depth gateway for LLM apps and agents — blocks prompt injection, data exfiltration, and tool abuse with policy-as-code, tamper-evident audit trails, and human approval for high-risk actions.” Pricing taxonomy: Open source / Freemium / Free trial. Status: Pending approval. | The 2026-09-17 tracker said the tagline was still infrastructure Q&A. **That is stale.** Live tagline matches the buyer. “Agents” is slightly broad; it is not the Q&A persona. No edit required for the old overclaim. |
| BetaList submission 188668 | Unpublished, paywalled ($39+). Packet in `directory-submissions.md` is already the gateway text. | Do not pay to launch. If resumed, paste the gateway packet, not the old Q&A pitch. |
| Show HN / Reddit drafts (`ceo-review-drafts.md`) | Revised 2026-09-17 to the gateway. Old SMB drafts are marked do-not-publish. | Drafts are aimed at the right buyer. Do not publish them as a product launch. The post to review first is the bypass write-up. |
| beyefendi `emerging.md` (live) | “LLM gateway with agent-gate tool permissioning and Ed25519 audit trails.” PR #51 closed 2026-09-18; the line is on the default branch. | Matches the buyer. |
| corca-ai/awesome-llm-security#348 | Open. Title and body are gateway-only and explicitly refuse an SMB-copilot pitch. | Leave open. No copy fix. |
| Danush-Aries/awesome-ai-agent-security#6 | Open. Body has no SMB / Q&A / walkthrough pitch. | Leave open. |
| christiancscott/awesome-LLM-security#15 | Open. Same. | Leave open. |
| https://defenseaegis.org/guides/smb-cve-exposure-checklist | Written to a small-business owner checking server CVEs. Published 2026-09-16. | Wrong persona for acquisition. Left up. Do not use it as a distribution post or a peer of the GitHub CTA. A rewrite of that article is a separate Track A change if Hamid wants the URL retired. |
| Logged-in Q&A, billing, walkthrough paywall, privacy, terms | Still describe the advisory example. | Correct for that surface. They are not the landing pitch. Out of this pass. |

**Proposed GitHub About** (Hamid applies in the repo settings; not done here):

> Open-source LLM security gateway. CEL policy-as-code, four-tier risk, human approval for high-risk tool calls, Ed25519 audit. Drop-in OpenAI-compatible base URL between your app and any model provider.

---

## 3. Channel order

The buyer looks where people wire models into their own apps. Cybersecurity-owner channels are the wrong room.

| Order | Channel | Why | What to do |
|-------|---------|-----|------------|
| 1 | A technical post, then Show HN | Engineers trust a bypass that was found, measured, and patched. A product announcement with $0 MRR does not. | Draft is `draft-iac-credential-bypass-writeup-2026-09-23.md`. Hamid reviews before any publish. |
| 2 | dev.to, same post | Same reader, longer shelf life than a thread. | Same draft. Do not publish in parallel with Show HN on the same day if Hamid wants one conversation. |
| 3 | r/LocalLLaMA | People running models and building apps, not buying security software. | Same post, subreddit rules, no launch tone. The existing Reddit skeleton in `ceo-review-drafts.md` is a question; the write-up is the stronger artifact. |
| 4 | Awesome-lists already in motion | `emerging.md` is live. Three PRs are open and already gateway-worded. | Do not open more lists until one of those lands or is rejected. |
| 5 | SaaSHub | Listing exists and the tagline is already the gateway. | Maintain. Do not spend another cycle on directory copy. |
| 6 | AI-engineering newsletters | Right reader, but they want a piece, not a tagline. | Send only after the write-up is approved. No cold blast. |

**Do not prioritize:** SMB-owner subreddits, “are we exposed?” SEO as the front door, G2/Capterra (buyers of this middleware do not shortlist there at this stage), BetaList’s paid launch, Product Hunt, or a cybersecurity Q&A community.

---

## 4. Pricing shape (decision for Hamid — do not implement)

Infrastructure in this category is not a flat consumer subscription. The public pattern, checked against [Portkey’s pricing page](https://portkey.ai/pricing) on 2026-09-23:

| Portkey tier | Public price | Meter |
|--------------|--------------|--------|
| Open source, host it yourself | $0 software | Your infra |
| Developer | $0 | 10k recorded logs/mo, 3-day log retention |
| Production | **$49/mo** | 100k logs, then **$9 per extra 100k** |
| Enterprise | Custom | SSO, private cloud / VPC, SOC2 / HIPAA, custom retention |

LiteLLM’s public shape is the same idea: free self-host, paid enterprise for the control plane. Helicone and Cloudflare meter requests or logs. None of them sell a $29 walkthrough.

**Proposed shape for AEGIS. Not a Stripe change.**

| Tier | What they pay for | When it can exist |
|------|-------------------|-------------------|
| **Community** | Self-host the gateway. CEL, tiers, human gate, audit. $0. | **Now.** This is the product. |
| **Team** | A hosted gateway plus retained audit (on the order of 30 days) and a request/log allowance. | Only after a hosted control plane exists. Do not charge for it before then. |
| **Org** | SSO, longer retention, audit export for compliance, higher limits. | Later. Custom. Not designed in this pass. |

**Band to decide, not to turn on:** if Team is built, start from Portkey’s public Production shape — about **$49/mo for a log allowance, overage per additional 100k** — because that is how neighboring gateways price the hosted path. That number is a category prior. It is not evidence anyone will pay AEGIS that. We have **no** gateway pay attempts.

**What not to do**

- Do not retune $29. The object is wrong.
- Do not create a new Stripe price in this pass.
- PR #93 only changes what the landing *features*. The $29 Q&A SKU can keep existing until Hamid retires that example. Killing the price in Stripe is a separate yes.

**Ask:** approve the shape (free self-host is the offer; paid is hosted + retention + SSO later, metered, not a seat), and say whether $49/100k-class is the band to design toward or whether Team stays “contact” until the hosted path is real.
