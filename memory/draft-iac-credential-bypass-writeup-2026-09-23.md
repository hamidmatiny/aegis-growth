# A credential-echo bypass, and the patch

**Status (2026-09-23):** Hamid approved this text for publication and skipped a further review. Raw attack prompts are not in this file. Show HN was not posted: no Hacker News session is available in the browser or in Chrome. dev.to and r/LocalLLaMA stay unposted on purpose — the channel order is Show HN, then dev.to, then r/LocalLLaMA, not all at once.

**Voice:** technical, first person if Hamid posts it. No “case study” gloss. Numbers below are from the repo and the live retest on the day of the merge.

---

## Title options

- We shipped a block for code-shaped credential leaks, then Terraform and OpenAPI walked around it
- An LLM security gateway missed IaC-shaped secrets for a day. Here is the patch.

## Body

AEGIS sits on the OpenAI-compatible URL between an app and a model. One job of the output check is to stop the model from handing back credentials for *this* service when the user asks for them in a form that looks like configuration.

On 2026-09-23 we had already merged a block for the obvious shapes: Python, bash, YAML, Authorization headers (`#89`, `3cef61c`). A fresh pair of cases still came back allowed. The ask was the same — emit this service’s credentials — but the wrapping was infrastructure-as-code and API-spec form: Terraform, OpenAPI `securitySchemes`, Helm, Kubernetes, GitHub Actions, Pulumi, Ansible. Quoted token-shaped values in those documents were not treated as a secret assignment. Issues [#90](https://github.com/hamidmatiny/aegis/issues/90) and [#91](https://github.com/hamidmatiny/aegis/issues/91).

The patch is in [#92](https://github.com/hamidmatiny/aegis/pull/92), squash-merged **2026-09-23T13:15:24Z** as `a7d155a`.

What changed, in the output detector:

- A prompt counts as this attack only when it asks for credentials (or tokens, keys, passwords, auth material) **and** names a config format, near “this assistant” or “this service.” A generic “how do I set an Authorization header?” tutorial does not match.
- The output counts when it looks like those formats **and** assigns a token-shaped value. Placeholders (`example`, `changeme`, `redacted`, and the usual stand-ins) and `${...}` interpolations do not.
- When both sides match and the completion is not a clear refusal, the credential-framing score is **0.88**, which is over the block threshold for critical secret leak.
- The ambiguous band that sends a case to the judge moved to fused **0.40–0.70** (it had started higher). Scores just under the old floor were skipping the judge. A benign “capital of France” prompt stays well under that floor.

Same-day live check against `https://defenseaegis.org/v1/chat/completions` (public demo, mock model), after the new output-defense image was up:

| Case | Result |
|------|--------|
| The IaC / API-spec credential family that had been allowed (the #90 / #91 set, plus the earlier code-format set) | **HTTP 403** `aegis_policy_blocked`, rule `block-critical-pii-leak` |
| “What is the capital of France?” | **HTTP 200**, allow, fused score **0.058** |

That is one family, closed in a day, with the unflattering part stated: the first fix was too narrow, and a config-shaped echo walked through until the prompt and the output had to agree.

Repo: https://github.com/hamidmatiny/aegis

## Do not add

- The raw prompts from the red-team fixtures.
- A claim that adaptive bypass rates are solved. `RESULTS.md` still shows adaptive campaigns are a different, worse number than round-1.
- $29, walkthroughs, or “SMB security copilot.”
