# Null-case audit · matveev-ofac-2023 · agent B

## Summary verdict
- **agent_verdict**: `pass_with_concerns`
- **confidence**: medium
- **one-sentence justification**: Trigger is clean and target is correctly framed as an individual designation, but `asset_onchain` = `not_measured` with a "SDN XML cross-reference pending" note indicates the event is admitted before address enumeration is closed — a forgivable null-event posture, but worth a human eye.

## Trigger
- type / actor / timestamp / precision: `ofac_sdn_designation` / `US_OFAC` / `2023-05-16T00:00:00Z` / day
- citation admissibility (primary / semi-primary count): 2 primary_legal (OFAC RA capture with body_hash+body_path+wayback; Treasury JY1455 press release, no body_hash)
- verdict: pass

## Scoped claim
- which layers were scoped: `offramp_cex` is the only layer with an observation; `asset_onchain` is `not_measured` with explicit pending-XML-cross-reference language
- is the null-case claim properly bounded? Yes — scoped_claim explicitly says "Per-address cross-reference to SDN XML pending; cross-layer observations limited by individual-level targeting", which is honest.

## Observation anchors
- layer=`offramp_cex` / kind=`observed_no_change` / attribution=`none` / anchors: 1 primary_legal source with body_hash + body_path (OFAC RA capture) + structured `scope_descriptor`
- verdict per row: pass — meets validator anchor requirements; identical pattern to the other individual-BTC nulls.

## Coverage status honesty
- `l0_network` = not_applicable — defensible
- `l1_consensus` = not_applicable — correct (target is individual, no chain-specific consensus claim)
- `l3_rpc` = not_applicable — correct
- `l4_frontend` = not_applicable — correct
- `asset_onchain` = **not_measured** with "SDN XML cross-reference pending" — honest, but this means the event is admitted while the address enumeration is open. For a null-case admission, the rubric tolerates this (the event is not used as a denominator for asset-layer change rates), but a human should confirm.
- `offramp_cex` = **measured** — same concern as other individual-BTC nulls.

## Issues / concerns
- Admission with an open address enumeration (asset_onchain status=not_measured, pending SDN XML cross-reference) means the event is structurally incomplete; the rubric admits this for null cases but the cross-reference should be tracked.
- Same `offramp_cex` = `measured` framing concern as the other individual-BTC nulls.

## Recommendation for human reviewer
Confirm the SDN XML cross-reference is on a tracked TODO and decide whether to wait for it to close before stamping `last_human_audit`. Otherwise the event is functionally clean as a null-case datapoint.
