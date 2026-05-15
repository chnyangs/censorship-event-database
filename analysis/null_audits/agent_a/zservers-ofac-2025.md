# Null-case audit · zservers-ofac-2025 · agent A

## Summary verdict
- **agent_verdict**: `pass_with_concerns`
- **confidence**: medium
- **one-sentence justification**: Trigger is well-anchored; the 4-BTC-address cohort is concretely enumerated, but the off-ramp CEX `measured` row rests on trigger page + scope_descriptor only — same systemic null-case pattern as the other OFAC RA-only nulls.

## Trigger
- type / actor / timestamp / precision: `ofac_sdn_designation` / `US_OFAC` / 2025-02-11T00:00:00Z / day
- citation admissibility (primary / semi-primary count): 2 primary_legal citations (OFAC RA 20250211 with wayback + body_hash + body_path; Treasury press release sb0012 note only). Solid trigger anchor.
- verdict: pass

## Scoped claim
- which layers were scoped: offramp_cex (`measured`, 14-day window 2025-02-11 → 2025-02-25) against 4 BTC addresses; all others `not_applicable`. No canonical domain published (infrastructure provider with no public-facing brand site).
- is the null-case claim properly bounded? Yes — `scoped_claim` is short and limits itself to "infrastructure-provider target with limited cross-layer measurable surface" without overreach. Observation note explicitly says "absence of public disclosure".

## Observation anchors
- layer `offramp_cex` / `observed_no_change` / attribution `none` / anchors present: 1 × `body_hash + body_path` (OFAC RA) + `scope_descriptor` (providers, time_window, addresses_cohort=`zservers_russian_4_btc`).
  - verdict: concerns — same pattern: trigger + scope_descriptor, no exchange-search artifact.

## Coverage status honesty
- `offramp_cex`: `measured` — borderline. 4 concrete BTC addresses (3 legacy P2SH + 1 Bech32) are falsifiable cohort, but the absence search is not artifact-pinned.
- `l0_network`: `not_measured` — appropriately conservative (no probe data, no canonical domain to probe).
- `l4_frontend`: `not_applicable` — defensible (no canonical domain listed in SDN entries).
- All other layers `not_applicable` — defensible (Bitcoin-only addresses, hosting-provider entity).

## Issues / concerns
- Treasury press release citation has no body_hash + body_path.
- Joint US/UK/AU jurisdiction but scope_descriptor providers list is again the standard US-focused major-CEX list — the absence search could plausibly extend to UK/AU exchanges given the joint sanction.
- No aggregator query artifact for the absence search.
- Hosting-provider class — pairs with Aeza 2025-07 and Russian-cybercrime-infra 2025-11 as a 2025 hosting cluster; the three events together would benefit from shared aggregator-query artifacts for the off-ramp absence search.

## Recommendation for human reviewer
Same decision shape as the other OFAC RA-only off-ramp nulls. This is the most concrete of the 2025 hosting-provider trio (4 BTC addresses, vs 1 for Russian-cybercrime-infra). Human should apply a consistent corpus-wide convention on whether `measured` requires a pinned aggregator artifact. Aggregate-only until stamped.
