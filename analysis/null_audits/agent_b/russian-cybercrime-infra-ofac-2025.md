# Null-case audit · russian-cybercrime-infra-ofac-2025 · agent B

## Summary verdict
- **agent_verdict**: `pass_with_concerns`
- **confidence**: medium
- **one-sentence justification**: Trigger is clean and the joint-US/UK/AU framing is properly acknowledged, but the 14-day observation window (2025-11-19 to 2025-12-03) ends 2025-12-03 — the YAML's `last_verified: 2026-04-22` is a long gap, and `offramp_cex` = `measured` reproduces the same OFAC-RA-only-substrate concern as the other 2025 hosting-cluster null events.

## Trigger
- type / actor / timestamp / precision: `ofac_sdn_designation` / `US_OFAC` / `2025-11-19T00:00:00Z` / day
- citation admissibility (primary / semi-primary count): 2 primary_legal (OFAC RA capture with body_hash+body_path+wayback; Treasury SB0314 press release, no body_hash)
- verdict: pass

## Scoped claim
- which layers were scoped: `offramp_cex` only (Bitcoin-only individuals with 1 XBT address)
- is the null-case claim properly bounded? Yes — scoped_claim limits to "sustained 2025 policy focus on hosting-layer targets"; does not over-claim.

## Observation anchors
- layer=`offramp_cex` / kind=`observed_no_change` / attribution=`none` / anchors: 1 primary_legal source with body_hash + body_path (OFAC RA capture) + structured `scope_descriptor`
- verdict per row: pass — standard OFAC-RA-anchor pattern.

## Coverage status honesty
- `l0_network` = not_applicable — defensible (no domain scoped despite "infrastructure provider" framing in actor_type)
- `l1_consensus` = not_applicable (Bitcoin) — correct
- `l3_rpc` = not_applicable (Bitcoin) — correct
- `l4_frontend` = not_applicable — defensible (no canonical_domain)
- `asset_onchain` = not_applicable (Bitcoin) — correct
- `offramp_cex` = **measured** — same concern as other individual-BTC nulls.

## Issues / concerns
- `actor_type: individuals` and `actor_name: Russian bulletproof hosting operators` — for a "hosting provider" cluster, the question of whether the operators ran a hosting domain that could be L0/L4-scoped is left open. The YAML notes the action also targeted Aeza-linked individuals; if Aeza had a canonical domain, one might argue L0/L4 should be `not_measured` rather than `not_applicable`. Compare with `aeza-group-ofac-2025` event (sibling).
- Multiple individuals designated (VOLOSOVIK, MAKAROV, PANKOVA, ZAKIROV), but only 1 BTC address listed — the YAML correctly notes only VOLOSOVIK carried an address.

## Recommendation for human reviewer
Cross-check with `aeza-group-ofac-2025.yaml` for consistency on whether bulletproof-hosting designations imply L0/L4 substrate. If Aeza was scoped at L0/L4, this event arguably should not be `not_applicable` for those layers given the MAKAROV-Aeza linkage. Otherwise standard null-event treatment.
