# Null-case audit · matveev-ofac-2023 · agent A

## Summary verdict
- **agent_verdict**: `pass_with_concerns`
- **confidence**: medium
- **one-sentence justification**: Trigger is properly anchored, but the target enumeration is `subset` with no addresses on the RA page, asset_onchain is `not_measured` (SDN XML cross-reference pending), and the off-ramp CEX `measured` row again rests on trigger + scope_descriptor only.

## Trigger
- type / actor / timestamp / precision: `ofac_sdn_designation` / `US_OFAC` / 2023-05-16T00:00:00Z / day
- citation admissibility (primary / semi-primary count): 2 primary_legal citations (OFAC RA 20230516 with wayback + body_hash + body_path; Treasury press release jy1455 note only). Solid trigger anchor.
- verdict: pass

## Scoped claim
- which layers were scoped: offramp_cex (`measured`, 14-day window); asset_onchain (`not_measured`, pending SDN XML cross-reference); all others `not_applicable`.
- is the null-case claim properly bounded? Yes — `scoped_claim` is honest about the per-address cross-reference being pending and limits itself to a datapoint for the ransomware-individual class. No overreach.

## Observation anchors
- layer `offramp_cex` / `observed_no_change` / attribution `none` / anchors present: 1 × `body_hash + body_path` (OFAC RA) + `scope_descriptor` (providers, time_window, addresses_cohort=`matveev_wazawaka_individual` — again, this is a person label, not an address set).
  - verdict: concerns — same systemic pattern, plus the cohort label is an individual rather than addresses (analogous to the entity-only Lazarus 2019 case).

## Coverage status honesty
- `offramp_cex`: `measured` — concerning. Target enumeration is `subset` and asset layer is `not_measured`; there are no enumerated addresses to search for. Same issue as `lazarus-entity-ofac-2019`. Honest framing would be entity-name-mention null or downgrade to `partially_measured`.
- `asset_onchain`: `not_measured` — defensible; the note is honest about pending SDN XML cross-reference.
- Other layers `not_applicable` — defensible for an individual designation with no enumerated addresses or canonical domain.

## Issues / concerns
- No enumerated address cohort. Per the pre-audit, this is flagged: "Target enumeration is `subset` and asset layer is not measured; human must decide if the off-ramp null denominator remains defensible."
- Treasury press release citation has no body_hash + body_path.
- The off-ramp CEX cohort label `matveev_wazawaka_individual` is essentially a name; the absence search reduces to "no exchange mentioned WAZAWAKA in 14 days" — possibly true but conceptually thin.

## Recommendation for human reviewer
Human should decide one of: (a) complete the SDN XML cross-reference to enumerate Matveev's addresses, then upgrade `asset_onchain` and re-anchor the offramp_cex cohort; or (b) downgrade `offramp_cex` to `partially_measured` reflecting that the absence search has no concrete address denominator. This case is closely parallel to `lazarus-entity-ofac-2019` (entity/individual without enumerated addresses); the verdict should be aligned with whatever the human decides for that case.
