# Null-case audit · lazarus-laundering-ofac-2020 · agent A

## Summary verdict
- **agent_verdict**: `pass_with_concerns`
- **confidence**: medium
- **one-sentence justification**: Strong trigger anchor and a concrete 20-BTC-address cohort make this null more falsifiable than the entity-only Lazarus case, but the off-ramp CEX `measured` coding still rests on the OFAC trigger page + scope_descriptor only — no exchange-statement search artifact is pinned.

## Trigger
- type / actor / timestamp / precision: `ofac_sdn_designation` / `US_OFAC` / 2020-03-02T00:00:00Z / day
- citation admissibility (primary / semi-primary count): 2 primary_legal citations (OFAC RA 20200302 with wayback + body_hash + body_path; Treasury press release sm924 note only). Strong trigger anchor.
- verdict: pass

## Scoped claim
- which layers were scoped: offramp_cex (`measured`, 14-day window 2020-03-02 → 2020-03-16) against 20 unique BTC addresses; all other layers `not_applicable`.
- is the null-case claim properly bounded? Yes — the observation note explicitly says "private chain-analytics-driven KYC flags rather than public corporate statements" and attribution is `none`. The `scoped_claim` is honestly modest. The `analysis_notes` text actually contains a self-flagging "Admitting as null_event rather than null_event" sentence that looks like a stale typo from a comparison-vs-null refactor — worth flagging for cleanup.

## Observation anchors
- layer `offramp_cex` / `observed_no_change` / attribution `none` / anchors present: 1 × `body_hash + body_path` (OFAC RA) + `scope_descriptor` (providers, time_window, addresses_cohort=`lazarus_laundering_20_btc`).
  - verdict: concerns — the OFAC RA proves the listing and the 20 BTC addresses are enumerated in the target block, which is a useful concrete denominator, but no exchange-search artifact replays the absence.

## Coverage status honesty
- `offramp_cex`: `measured` — borderline. The 20-address cohort is more concrete than the entity-only cases, but the absence search is still implicit. The coverage note even spells this out ("14-day post-event public-CEX-announcement scan: no public statement... was published") which is the right wording — though the scan itself is not artifact-pinned.
- All other layers `not_applicable` — defensible (Bitcoin native, individual-level, pre-Merge by 929 days).

## Issues / concerns
- Off-ramp CEX `measured` without a pinned aggregator query artifact — same systemic concern as the other OFAC RA-only nulls.
- `analysis_notes` contains the text "Admitting as null_event rather than null_event" which appears to be a stale phrase from a prior shape vocabulary; this should be cleaned up but does not affect audit substance.
- Treasury press-release citation has no body_hash + body_path.

## Recommendation for human reviewer
This case is on the stronger end of the off-ramp CEX nulls because the 20-address cohort is concretely enumerated. The human should (a) decide whether `measured` requires an explicit exchange-search artifact or whether the trigger + scope_descriptor convention is sufficient for the public-disclosure-null reading; and (b) clean up the stale "null_event rather than null_event" line in `analysis_notes`. Either way, this case should remain aggregate-only until the human stamps it.
