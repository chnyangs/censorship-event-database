# Null-case audit · sichuan-silence-ofac-2024 · agent A

## Summary verdict
- **agent_verdict**: `pass_with_concerns`
- **confidence**: medium
- **one-sentence justification**: Trigger is well-anchored, but this is an entity-level designation with no on-chain addresses on the RA page; the off-ramp CEX `measured` row relies on trigger page + scope_descriptor, and the address cohort label is the entity name — same structural weakness as `lazarus-entity-ofac-2019`.

## Trigger
- type / actor / timestamp / precision: `ofac_sdn_designation` / `US_OFAC` / 2024-12-10T00:00:00Z / day
- citation admissibility (primary / semi-primary count): 2 primary_legal citations (OFAC RA 20241210 with wayback + body_hash + body_path; Treasury press release jy2731 note only). Solid trigger anchor.
- verdict: pass

## Scoped claim
- which layers were scoped: offramp_cex (`measured`, 14-day window 2024-12-10 → 2024-12-24); asset_onchain (`not_measured`, pending SDN XML cross-reference); all others `not_applicable`.
- is the null-case claim properly bounded? Yes — the `scoped_claim` is restrained ("datapoint for the China-cyber-actor class"). Observation note acknowledges no on-chain addresses and bounds claim to "no public CEX policy statement".

## Observation anchors
- layer `offramp_cex` / `observed_no_change` / attribution `none` / anchors present: 1 × `body_hash + body_path` (OFAC RA) + `scope_descriptor` (providers, time_window, addresses_cohort=`sichuan_silence_entity` — an entity label, not an address set).
  - verdict: concerns — same as `lazarus-entity-ofac-2019`: trigger + scope_descriptor with cohort-as-name.

## Coverage status honesty
- `offramp_cex`: `measured` — concerning. No enumerated addresses; cohort is the entity name. Honest framing would be entity-name-mention null or downgrade to `partially_measured`.
- `asset_onchain`: `not_measured` — defensible.
- All other layers `not_applicable` — defensible (cybersecurity firm + employee, no canonical crypto presence).

## Issues / concerns
- Entity-level designation with no addresses on the RA page; this is structurally identical to `lazarus-entity-ofac-2019` and `matveev-ofac-2023` in lacking a concrete address denominator.
- Treasury press release citation has no body_hash + body_path.
- The China-nexus framing (alongside Yinyin/Jiadong 2020 and Funnull CDN 2025) is appropriately cautious in `analysis_notes`.
- No aggregator query artifact for the absence search.

## Recommendation for human reviewer
Apply the same decision as for `lazarus-entity-ofac-2019` and `matveev-ofac-2023`: either complete the SDN XML cross-reference for addresses and upgrade observation anchors, or downgrade `offramp_cex` to `partially_measured` reflecting the entity-name-only nature of the absence search. Otherwise treat as aggregate-only.
