# Null-case audit · sichuan-silence-ofac-2024 · agent B

## Summary verdict
- **agent_verdict**: `pass_with_concerns`
- **confidence**: medium
- **one-sentence justification**: Entity-level Chinese cybersecurity firm designation with clean primary triggers; `asset_onchain` = `not_measured` with "SDN XML cross-reference pending" indicates open address enumeration similar to Matveev, and `offramp_cex` = `measured` follows the same convention as other entity-level null events.

## Trigger
- type / actor / timestamp / precision: `ofac_sdn_designation` / `US_OFAC` / `2024-12-10T00:00:00Z` / day
- citation admissibility (primary / semi-primary count): 2 primary_legal (OFAC RA capture with body_hash+body_path+wayback; Treasury JY2731 press release, no body_hash)
- verdict: pass

## Scoped claim
- which layers were scoped: `offramp_cex` only (entity-level designation with no addresses on RA page)
- is the null-case claim properly bounded? Yes — scoped_claim limits to "datapoint for the China-cyber-actor class".

## Observation anchors
- layer=`offramp_cex` / kind=`observed_no_change` / attribution=`none` / anchors: 1 primary_legal source with body_hash + body_path (OFAC RA capture) + structured `scope_descriptor`
- verdict per row: pass — standard OFAC-RA-anchor pattern.

## Coverage status honesty
- `l0_network` = not_applicable — defensible (no domain scoped despite the firm operating online)
- `l1_consensus` = not_applicable — correct
- `l3_rpc` = not_applicable — correct
- `l4_frontend` = not_applicable — defensible (no canonical_domain listed; the firm may have had a corporate website but it is not scoped)
- `asset_onchain` = **not_measured** with "SDN XML cross-reference pending" — honest but open (same posture as Matveev)
- `offramp_cex` = **measured** — same OFAC-RA-only-substrate concern as the other entity nulls.

## Issues / concerns
- Sichuan Silence Info Tech is a Chinese cybersecurity firm — almost certainly had a corporate website that could have been L4-scoped. The decision to leave L4 = `not_applicable` rather than `not_measured` (with the firm's domain in scope) is a defensible choice for paper-rigor but may be too quick — a human should confirm whether a canonical Sichuan-Silence corporate domain exists.
- Open `asset_onchain` enumeration (same as Matveev).
- `null_event` tag in `tags:` list is informational but the YAML already carries `empirical_shape: null_event`.

## Recommendation for human reviewer
Confirm there is no canonical Sichuan-Silence corporate website that should be L4-scoped (e.g., a `sichuansilence.com` or similar). If there is, the event should likely have `l4_frontend.status: not_measured` rather than `not_applicable`. Otherwise standard null-event treatment.
