# Null-case audit · pertsev-nl-arrest-2022 · agent B

## Summary verdict
- **agent_verdict**: `pass`
- **confidence**: high
- **one-sentence justification**: Cross-border-arrest null is clean and well-bounded — the FIOD press release is a single primary_legal anchor with body_hash+body_path, and the scoped claim properly acknowledges that the Tornado Cash 2022-08-08 cascade absorbed CEX-response bandwidth two days earlier.

## Trigger
- type / actor / timestamp / precision: `doj_indictment` / `NL_FIOD` / `2022-08-10T00:00:00Z` / day
- citation admissibility (primary / semi-primary count): 1 primary_legal (FIOD press release with body_hash+body_path; no wayback URL listed)
- verdict: pass — single primary citation is acceptable for a null-case trigger admissibility check; the FIOD press release is the canonical operator artifact.

## Scoped claim
- which layers were scoped: `offramp_cex` only (the YAML correctly notes Tornado L4 was already offline from 2022-08-08 cascade)
- is the null-case claim properly bounded? Yes — scoped_claim is limited to "first cross-border arrest of a crypto privacy-tool developer", explicitly framed as a non-US-jurisdiction extension downstream of the Tornado Cash OFAC cascade.

## Observation anchors
- layer=`offramp_cex` / kind=`observed_no_change` / attribution=`none` / anchors: 1 primary_legal source with body_hash + body_path (FIOD press release) + structured `scope_descriptor`
- verdict per row: pass — meets validator anchor requirements; the observation note honestly flags the confounder (Tornado Cash 2022-08-08 cascade absorbed CEX-response bandwidth).

## Coverage status honesty
- `l0_network` = not_applicable — defensible
- `l1_consensus` = not_applicable — defensible (developer arrest, not protocol designation)
- `l3_rpc` = not_applicable — defensible
- `l4_frontend` = not_applicable with explicit note ("Tornado Cash frontend already offline from 2022-08-08 OFAC cascade; no fresh L4 action for Pertsev arrest") — honest
- `asset_onchain` = not_applicable — defensible
- `offramp_cex` = **measured** — same OFAC-RA-only-substrate concern as the other null events, but here the FIOD release is the analogous artifact. Acceptable.

## Issues / concerns
- Trigger citation [0] lacks a `wayback` URL — minor archival-hygiene gap (also flagged on lazarus-entity-ofac-2019).
- `target.kind: entity` for an individual-developer arrest is slightly awkward — `actor_type: individual_developer` makes this clear, but a human should confirm.

## Recommendation for human reviewer
Add a wayback URL for the FIOD press release for archival hygiene. The event is otherwise the textbook example of a non-US-jurisdiction null event with a clear confounder (the 2022-08-08 cascade) handled correctly.
