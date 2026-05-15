# Null-case audit · pertsev-nl-arrest-2022 · agent A

## Summary verdict
- **agent_verdict**: `needs_human_review`
- **confidence**: medium
- **one-sentence justification**: This event is structurally confounded — the FIOD arrest occurred 2 days after the 2022-08-08 OFAC Tornado Cash cascade, so any "no CEX cascade for Pertsev specifically" claim is contaminated by the already-running protocol-level cascade, and the observation note acknowledges this explicitly ("CEX-response bandwidth was absorbed by the OFAC side"), which makes the null claim conceptually problematic as a clean denominator row.

## Trigger
- type / actor / timestamp / precision: `doj_indictment` (FIOD action, non-US) / `NL_FIOD` / 2022-08-10T00:00:00Z / day
- citation admissibility (primary / semi-primary count): 1 primary_legal citation (FIOD press release with body_hash + body_path). Single anchor; not a true 2-source primary cross-check, but FIOD is a primary authoritative source. No wayback URL is supplied for the FIOD press release, which is a minor archival risk.
- verdict: pass_with_concerns — single-source primary trigger is acceptable for cross-border arrests where the announcing authority is the only on-record body, but adding a wayback would strengthen.

## Scoped claim
- which layers were scoped: offramp_cex (`measured`, 14-day window 2022-08-10 → 2022-08-24); all others `not_applicable`. The note on l4_frontend explicitly defers to the 2022-08-08 OFAC cascade.
- is the null-case claim properly bounded? The text is bounded ("no public CEX cascade for individual developer arrest"), but the bounding is essentially "the CEX cascade had already happened 2 days earlier" — which is honest but undermines the claim's value as an *independent* null observation. A scoped clean null requires the absence search to be over a window not already perturbed by another trigger.

## Observation anchors
- layer `offramp_cex` / `observed_no_change` / attribution `none` / anchors present: 1 × `body_hash + body_path` (FIOD press release) + `scope_descriptor` (providers, time_window, addresses_cohort=`pertsev_individual_developer`).
  - verdict: concerns — anchor exists, but the underlying observation is structurally confounded.

## Coverage status honesty
- `offramp_cex`: `measured` — concerning. The 2022-08-10 → 2022-08-24 window overlaps with the already-running Tornado Cash 2022-08-08 cascade. Claiming "no Pertsev-specific CEX cascade" is hard to falsify because Pertsev's name was already entangled with Tornado Cash in exchange-policy discussions.
- All other layers `not_applicable` — defensible (no on-chain addresses; l4 frontend already offline from OFAC event).

## Issues / concerns
- **Confounding**: the 14-day window starts 2 days after the OFAC Tornado Cash cascade. The "no Pertsev-individual CEX cascade" null is hard to separate from "the cascade already happened".
- The pre-audit explicitly flagged this: "Confounded by prior Tornado Cash OFAC cascade; human must confirm a Pertsev-individual no-change scope is defensible."
- Single primary citation, no wayback.
- The 2024-05-14 Dutch court conviction (5y4m sentence) is mentioned in `analysis_notes` as a follow-on event but is not catalogued separately; this is fine for now but reduces this case's clean-null integrity.

## Recommendation for human reviewer
Human should decide whether the temporal confounding with the OFAC Tornado Cash cascade disqualifies this row from clean-null use. Options: (a) downgrade observation to `coverage_gap` (the relevant signal is unmeasurable because of the already-running cascade); (b) re-scope to a longer window (e.g. 2024-05-14 Dutch conviction window) that is decoupled from the OFAC cascade; (c) keep `observed_no_change` with explicit acknowledgement that this is a "no incremental CEX action attributable to the FIOD arrest itself" claim and accept the structural caveat. This is the case in the 13 where the structural confounding is highest after sec-v-uniswap.
