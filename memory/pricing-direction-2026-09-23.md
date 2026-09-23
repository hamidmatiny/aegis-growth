# Pricing direction (Hamid, 2026-09-23)

**Status:** Approved as the direction to build toward. **Stripe is unchanged.** No price, product, or Checkout session was created or edited.

This is the reference point for when a hosted gateway exists. Do not re-open the shape from scratch. The dollar figure is a category prior, not evidence that anyone will pay it. Last written BEV in this repo is still **$0.00 CAD MRR**, **0** paying subscribers.

| Tier | What it is | Price | When |
|---|---|---|---|
| Community | Self-host the gateway (CEL, risk tiers, human gate, Ed25519 audit) | $0 | Live now. This is the offer on the site. |
| Team | Hosted gateway plus metered log retention | About **$49 per 100k logs**, a starting point taken from the public hosted-gateway category (Portkey Production, checked 2026-09-23) | Only after a hosted gateway actually exists. Do not charge before then. |
| Org | SSO, longer retention | Custom | Later. Undesigned. Do not invent the package. |

**Not in this decision:** a flat consumer subscription, the legacy $29 CAD walkthrough, or any change to the Stripe price id `price_1UDYTKKDOQtI1TQzKVuXg6Wd`.

Source note: `memory/gtm-icp-channels-pricing-2026-09-23.md`. Fleet graph node: `decision:pricing-shape-2026-09-23`.
