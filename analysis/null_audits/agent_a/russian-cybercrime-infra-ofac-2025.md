# Null-case audit · russian-cybercrime-infra-ofac-2025 · agent A

## Summary verdict
- **agent_verdict**: `pass_with_concerns`
- **confidence**: medium
- **one-sentence justification**: Trigger is well-anchored joint US/UK/AU action; the single-BTC-address cohort (Yalishanda) is concrete, but the off-ramp CEX `measured` row rests on trigger page + scope_descriptor only — same systemic null-case pattern.

## Trigger
- type / actor / timestamp / precision: `ofac_sdn_designation` / `US_OFAC` / 2025-11-19T00:00:00Z / day
- citation admissibility (primary / semi-primary count): 2 primary_legal citations (OFAC RA 20251119 with wayback + body_hash + body_path; Treasury press release sb0314 note only). Solid trigger anchor.
- verdict: pass

## Scoped claim
- which layers were scoped: offramp_cex (`measured`, 14-day window 2025-11-19 → 2025-12-03) against 1 BTC address (Volosovik/Yalishanda); all others `not_applicable`.
- is the null-case claim properly bounded? Yes — `scoped_claim` is short and limits itself to "sustained 2025 policy focus on hosting-layer targets" without overreach. Observation note explicitly says "absence of public disclosure".

## Observation anchors
- layer `offramp_cex` / `observed_no_change` / attribution `none` / anchors present: 1 × `body_hash + body_path` (OFAC RA) + `scope_descriptor` (providers, time_window, addresses_cohort=`russian_cybercrime_infra_1_btc`).
  - verdict: concerns — trigger + scope_descriptor, no exchange-search artifact.

## Coverage status honesty
- `offramp_cex`: `measured` — borderline. 1 concrete address is falsifiable but absence is not artifact-pinned.
- All other layers `not_applicable` — defensible (Bitcoin only, multiple individuals, no canonical web).

## Issues / concerns
- Multiple designees (VOLOSOVIK, MAKAROV, PANKOVA, ZAKIROV) on the same RA page, but only one (VOLOSOVIK) carries a BTC address. The `scoped_claim` and observation focus correctly on the one address, but the four named individuals make the "absence of public CEX statement" search more multi-faceted than the single-name framing suggests.
- Joint US/UK/AU jurisdiction but the scope_descriptor providers list is again US-focused.
- 2025 is recent; the observation window closes 2025-12-03, which is before the dataset cutoff (2026-05-06) — adequate lead time for delayed exchange statements.
- Treasury press release citation has no body_hash + body_path.

## Recommendation for human reviewer
Same as the other OFAC RA-only off-ramp nulls: human should decide on the corpus-wide convention for `measured` without a pinned aggregator artifact, and apply that consistently. This case is on the easier side because the address cohort is concrete and the trigger is recent enough that any public CEX response could still surface. Aggregate-only until stamped.
