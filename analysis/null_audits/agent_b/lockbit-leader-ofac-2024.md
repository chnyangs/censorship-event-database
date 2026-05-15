# Null-case audit · lockbit-leader-ofac-2024 · agent B

## Summary verdict
- **agent_verdict**: `pass_with_concerns`
- **confidence**: medium
- **one-sentence justification**: Trigger is clean and the Khoroshev address enumeration is complete (1 BTC), but the YAML is the leanest of the individual-BTC null events — no per-coverage note on `offramp_cex` explaining the measurement basis, while still claiming `measured` status.

## Trigger
- type / actor / timestamp / precision: `ofac_sdn_designation` / `US_OFAC` / `2024-05-07T00:00:00Z` / day
- citation admissibility (primary / semi-primary count): 2 primary_legal (OFAC RA capture with body_hash+body_path+wayback; Treasury JY2328 press release, no body_hash)
- verdict: pass

## Scoped claim
- which layers were scoped: `offramp_cex` only (Bitcoin-only individual, all other layers `not_applicable`)
- is the null-case claim properly bounded? Yes — scoped_claim is bounded to "datapoint in the LockBit cluster (paired with 2024-02-20 affiliates)".

## Observation anchors
- layer=`offramp_cex` / kind=`observed_no_change` / attribution=`none` / anchors: 1 primary_legal source with body_hash + body_path (OFAC RA capture) + structured `scope_descriptor`
- verdict per row: pass — meets validator anchor requirements; standard "no public CEX statement in 14-day window" framing.

## Coverage status honesty
- `l0_network` = not_applicable — defensible
- `l1_consensus` = not_applicable (Bitcoin) — correct
- `l3_rpc` = not_applicable (Bitcoin) — correct
- `l4_frontend` = not_applicable — defensible (individual, no canonical_domain)
- `asset_onchain` = not_applicable (Bitcoin) — correct
- `offramp_cex` = **measured** with **no note** — concern: this is the only event in the 13 where the `offramp_cex` coverage entry has neither a substrate note nor a denominator_artifact. The observation note carries the framing, but coverage-level honesty would benefit from at least the substrate-anchors-pinned-but-not-per-event-sliced paragraph used by sinbad-ofac-2023 and iran-ransomware-ofac-2018.

## Issues / concerns
- `coverage.offramp_cex` has no `note` field; for parity with the other null events that mark `measured` based on the same substrate convention, a short note clarifying what was scoped would help.
- `related_events: [lockbit-affiliates-ofac-2024]` references a sibling — sanity-check that the sibling is `empirical_case` or `anchor_case` so this pair is intelligible in Table 1.

## Recommendation for human reviewer
Add a substrate note to `coverage.offramp_cex` consistent with the other 6 individual-BTC null events. Decide the corpus convention question on `measured` for these OFAC-RA-only nulls.
