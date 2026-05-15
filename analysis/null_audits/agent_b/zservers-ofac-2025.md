# Null-case audit · zservers-ofac-2025 · agent B

## Summary verdict
- **agent_verdict**: `pass_with_concerns`
- **confidence**: medium
- **one-sentence justification**: Joint US/UK/AU action with clean primary triggers and complete address enumeration (4 XBT), but `l0_network` = `not_measured` is unusually thin — there is no scope, no note, and no negative-query artifact attached, unlike sinbad-ofac-2023 which sets the bar for L0 honesty.

## Trigger
- type / actor / timestamp / precision: `ofac_sdn_designation` / `US_OFAC` / `2025-02-11T00:00:00Z` / day
- citation admissibility (primary / semi-primary count): 2 primary_legal (OFAC RA capture with body_hash+body_path+wayback; Treasury SB0012 press release, no body_hash)
- verdict: pass

## Scoped claim
- which layers were scoped: `offramp_cex` only (despite `actor_type: hosting_provider`)
- is the null-case claim properly bounded? Yes — scoped_claim limits to "infrastructure-provider target with limited cross-layer measurable surface".

## Observation anchors
- layer=`offramp_cex` / kind=`observed_no_change` / attribution=`none` / anchors: 1 primary_legal source with body_hash + body_path (OFAC RA capture) + structured `scope_descriptor`
- verdict per row: pass — standard OFAC-RA-anchor pattern.

## Coverage status honesty
- `l0_network` = **not_measured** with **no scope, no note, no denominator_artifact** — concern: a hosting provider is a textbook L0 target. The decision to mark `not_measured` rather than `not_applicable` is correct, but the lack of any substrate (compare with sinbad-ofac-2023's attested OONI negative query) is a meaningful gap.
- `l1_consensus` = not_applicable (Bitcoin) — correct
- `l3_rpc` = not_applicable (Bitcoin) — correct
- `l4_frontend` = not_applicable with note "No canonical domain listed in SDN entries; infrastructure provider" — defensible but slightly inconsistent with `l0_network = not_measured` (a hosting provider's customers' domains are arguably scopable at L0 even if no operator-owned canonical_domain is listed)
- `asset_onchain` = not_applicable (Bitcoin) — correct
- `offramp_cex` = **measured** — same OFAC-RA-only-substrate concern as other null events.

## Issues / concerns
- L0 substrate gap: `l0_network = not_measured` with no scope and no artifact is a weaker version of the sinbad-ofac-2023 treatment. If the rubric tolerates this, fine; but for a bulletproof-hosting target, the L0 substrate question is most acute.
- Inconsistency with related events: `aeza-group-ofac-2025` (related event) and `russian-cybercrime-infra-ofac-2025` (related event) should be treated consistently at L0/L4.
- The 4-BTC address enumeration is complete, which is good — most individual-BTC nulls only have 1 address.

## Recommendation for human reviewer
Either (a) attest an OONI negative-query artifact for L0 (following sinbad-ofac-2023's template), or (b) document why L0 is `not_measured` rather than `not_applicable` for a bulletproof-hosting target with no enumerated L0 scope. Cross-check consistency with `aeza-group-ofac-2025` and `russian-cybercrime-infra-ofac-2025`.
