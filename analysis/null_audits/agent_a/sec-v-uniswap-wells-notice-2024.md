# Null-case audit · sec-v-uniswap-wells-notice-2024 · agent A

## Summary verdict
- **agent_verdict**: `needs_human_review`
- **confidence**: high
- **one-sentence justification**: The Wells-notice framing is a pre-enforcement procedural step, not a final enforcement action, and the L4 frontend `measured` coding rests on Uniswap's own blog post + an SEC press-releases index — *neither* of which actually replays `app.uniswap.org` operational uptime across the 10½-month coded window (2024-04-10 → 2025-02-25); the LLM pre-audit independently rated this `fail_pre_audit` and the user explicitly flagged it.

## Trigger
- type / actor / timestamp / precision: `sec_action` / `US_SEC` / 2024-04-10T00:00:00Z / day
- citation admissibility (primary / semi-primary count): 2 citations — citation[0] is `primary_corporate` (Uniswap Labs blog "Fighting for DeFi") with body_hash + body_path; citation[1] is `primary_legal` (SEC press-releases index page) with body_hash + body_path. **The primary_legal anchor for the SEC side is a press-releases index, not an SEC document about the Wells notice** — because SEC Wells notices are private correspondence and the SEC never filed nor disclosed. The trigger date (2024-04-10) is sourced *only* from the corporate disclosure (Uniswap's own blog).
- verdict: concerns — the trigger is properly day-precision-anchored to a corporate disclosure, which is acceptable for a primary-corporate-only event class (the SEC will not publish a Wells notice), but the legal-side anchor is effectively absence-of-press-release, not affirmative legal documentation. The trigger note correctly flags this as "the absence of an SEC press release is itself the paper-worthy signal" — a defensible framing, but human should weigh whether a single primary_corporate source is sufficient to admit a regulatory-trigger row.

## Scoped claim
- which layers were scoped: l4_frontend (`measured`, scope=`app.uniswap.org`, window 2024-04-10 → 2025-02-25); all others `not_applicable` (no addresses, no domains beyond app.uniswap.org, no chains listed).
- is the null-case claim properly bounded? **The `scoped_claim` overreads the evidence**. It asserts:
  - "Wells notice ... produced no L4 cascade" — at face value this requires evidence that `app.uniswap.org` remained operational across the full ~10.6-month window.
  - "Demonstrates that SEC pre-enforcement signals alone — without formal complaint filing — do NOT produce measurable censorship effects at the frontend or off-ramp layers" — this is a *causal* claim that goes beyond the `attribution: none` discipline applied to the observation row. Per `paper_claims.md §0 "Attribution discipline"`, `none` may not support any causal statement.
  - In addition, **Wells notice is a pre-action procedural step, not a final enforcement action**. The dataset's `null_case` admission for the broader off-ramp/sanctions framework presupposes a real enforcement trigger; a pre-enforcement signal is a weaker class of trigger than the other 12 events (all OFAC SDN / DOJ indictment / FIOD arrest).

## Observation anchors
- layer `l4_frontend` / `observed_no_change` / attribution `none` / anchors present: 2 × `body_hash + body_path` (same Uniswap blog and same SEC press-releases index from the trigger) + `scope_descriptor` (providers=`uniswap_labs_frontend`, time_window, addresses_cohort=`uniswap_labs_wells_notice`).
  - verdict: **fail**. Neither anchor demonstrates `app.uniswap.org` operational uptime during the 10½-month window. The Uniswap blog says "we will continue operating" (an intent statement, not a measurement); the SEC press-releases index is an absence-of-notice anchor. **There is no Wayback snapshot pair, no app.uniswap.org HTTP capture, no DNS log, no measurement_ids** anchoring actual frontend continuity. This is the structural deficiency the LLM pre-audit flagged as `fail_pre_audit`.

## Coverage status honesty
- `l4_frontend`: `measured` — **not defensible** as currently anchored. The claim requires direct observation of `app.uniswap.org` being reachable + content-stable across 10½ months, which is precisely what `sinbad-ofac-2023` and `iran-ransomware-ofac-2018` provide via Wayback pairs. This event has no analogous artifact. Should be downgraded to `not_measured` or the artifact set should be upgraded with `app.uniswap.org` Wayback captures bracketing the window.
- All other layers `not_applicable` — defensible (Uniswap Labs is a frontend operator, no addresses, no chains, no off-ramp surface).

## Issues / concerns
- **Wells-notice framing**: a Wells notice is a pre-enforcement staff letter indicating intent to recommend formal action. It is materially different in kind from the other 12 null cases (which are completed enforcement actions: OFAC SDN designations, DOJ indictments, FIOD arrest). Whether a pre-enforcement signal can serve as a paper-table null denominator alongside completed enforcement actions is a methodological question the human reviewer must adjudicate. The corpus's `null_case` admission tier was designed around enforcement triggers; this one is a pre-trigger signal.
- **No replayable frontend-uptime artifact**: the LLM pre-audit identified this exactly: "Current anchors do not replay `app.uniswap.org` operational uptime across 2024-04-10 to 2025-02-25." A clean fix would be to add Wayback captures of `app.uniswap.org` from (say) 2024-04-15, 2024-09-01, 2025-01-15, and 2025-02-20 with body_hash anchors; without this, the claim is intent-stated by Uniswap rather than measurement-verified.
- **Causal overreading in `scoped_claim`**: the phrase "do NOT produce measurable censorship effects" is a causal claim that exceeds `attribution: none`. This needs softening even if the artifact set is improved.
- **Single-source primary for trigger**: only Uniswap's own corporate disclosure dates the Wells notice. This is unavoidable (Wells notices are private), but the human should acknowledge that the trigger admissibility relies on corporate self-disclosure rather than legal documentation.
- The 2025-02-25 "SEC formally dropped the matter" claim in the trigger note is not separately anchored in the cited sources; if the paper text leans on this date (e.g. as an end-of-window), a second source for the drop announcement should be pinned.

## Recommendation for human reviewer
**This case requires human override before it can be used in any paper-facing capacity.** Concrete recommended actions in priority order:

1. Decide whether a Wells notice — a pre-enforcement procedural signal — is admissible as a `null_case` denominator alongside completed enforcement actions. If not, demote out of the null-case denominator and either drop the event or move it to a "candidate trigger / pre-enforcement signal" stratum.
2. If admitted: upgrade the L4 frontend evidence with at least 2–3 Wayback captures of `app.uniswap.org` bracketing the 10½-month window (event day, mid-window, near-drop) with body_hash anchors. Without this, downgrade `l4_frontend` to `not_measured`.
3. Rewrite `scoped_claim` to remove the causal phrasing "SEC pre-enforcement signals alone do NOT produce measurable censorship effects". A `none`-attribution observation supports only "within the scoped window and the limited sources, no change was observed", not a general causal claim about Wells notices.
4. Add a second corroborating source for the 2025-02-25 dismissal if the dismissal date is referenced as an end-of-window anchor.

This is the case in the 13 most likely to require remediation rather than a sign-off as-is.
