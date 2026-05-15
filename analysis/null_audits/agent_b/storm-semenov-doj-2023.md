# Null-case audit · storm-semenov-doj-2023 · agent B

## Summary verdict
- **agent_verdict**: `pass`
- **confidence**: high
- **one-sentence justification**: Companion DOJ indictment to a same-day OFAC SDN designation; the YAML correctly carves out cross-layer cascade as absorbed by the OFAC side and limits the DOJ null observation to the offramp_cex layer with a clean primary_legal anchor.

## Trigger
- type / actor / timestamp / precision: `doj_indictment` / `US_DOJ_SDNY` / `2023-08-23T00:00:00Z` / day
- citation admissibility (primary / semi-primary count): 1 primary_legal (DOJ USAO-SDNY press release with body_hash+body_path; no wayback URL listed)
- verdict: pass — single primary citation is acceptable for a null-case trigger admissibility check; the DOJ release is the canonical operator artifact for the indictment.

## Scoped claim
- which layers were scoped: `offramp_cex` only — the YAML explicitly notes (a) L4 was already offline from 2022-08-08, (b) asset-layer activity captured in companion `semenov-ofac-2023`
- is the null-case claim properly bounded? Yes — scoped_claim is bounded to the DOJ-side companion of the same-day OFAC action; it does not over-claim a cross-layer cascade.

## Observation anchors
- layer=`offramp_cex` / kind=`observed_no_change` / attribution=`none` / anchors: 1 primary_legal source with body_hash + body_path (DOJ press release) + structured `scope_descriptor`
- verdict per row: pass — the observation note honestly flags the confounder (CEX-response bandwidth absorbed by the OFAC side), which is the cleanest treatment of co-occurring trigger interference in the 13-event set.

## Coverage status honesty
- `l0_network` = not_applicable — defensible
- `l1_consensus` = not_applicable — defensible
- `l3_rpc` = not_applicable — defensible
- `l4_frontend` = not_applicable with explicit note ("Tornado Cash frontend already offline from 2022-08-08; no fresh L4 action for 2023-08-23 indictment") — honest
- `asset_onchain` = not_applicable with explicit pointer to companion event — honest
- `offramp_cex` = **measured** — same DOJ-release-only-substrate concern as other null events, but the cross-event handoff to `semenov-ofac-2023` is the right design.

## Issues / concerns
- Trigger citation lacks `wayback` URL — minor archival-hygiene gap.
- The "no fresh CEX policy statement referencing the DOJ indictment" claim is sound but inherently hard to falsify; the structured `scope_descriptor` is the right substrate.

## Recommendation for human reviewer
Add a wayback URL for the DOJ press release for archival hygiene. Otherwise this is the cleanest DOJ-companion-to-OFAC null event in the 13.
