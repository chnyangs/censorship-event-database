# Null-case audit · iran-ransomware-ofac-2018 · agent B

## Summary verdict
- **agent_verdict**: `pass`
- **confidence**: high
- **one-sentence justification**: Historically-anchored OFAC SDN with primary citations and a single L4 observation backed by a pre/post Wayback bracket; scoped claim is properly bounded to what is structurally measurable for a Bitcoin-only individual designation.

## Trigger
- type / actor / timestamp / precision: `ofac_sdn_designation` / `US_OFAC` / `2018-11-28T00:00:00Z` / day
- citation admissibility (primary / semi-primary count): 2 primary_legal (OFAC RA page with body_hash+body_path+wayback; Treasury SM556 press release without body_hash but linked as confirmatory)
- verdict: pass

## Scoped claim
- which layers were scoped: L4 frontend (enexchanger.com via Wayback bracket); offramp_cex marked `not_measured` with substrate anchors pinned; L1/L3/asset_onchain all `not_applicable` for Bitcoin pre-Merge
- is the null-case claim properly bounded (not a corpus-wide claim)? Yes — scoped_claim explicitly limits to the enexchanger.com 20-day window and acknowledges L1/L3 Ethereum infrastructure did not yet exist.

## Observation anchors
- layer=`l4_frontend` / kind=`observed_no_change` / attribution=`none` / anchors: 2 semi_primary_wayback sources, each with body_hash + body_path + wayback URL; `evidence_group_id: enexchanger-wayback-bracket` ties them
- verdict per row: pass — pre-event (2018-11-23) and post-event (2018-12-12) Wayback snapshots form a falsifiable bracket consistent with the validator's null-anchor rule.

## Coverage status honesty
- `l0_network` = not_measured (scope: enexchanger.com) — honest; no L0 substrate cited
- `l1_consensus` = not_applicable (Bitcoin + pre-Merge by 1387 days) — correct
- `l3_rpc` = not_applicable (Bitcoin) — correct
- `l4_frontend` = partially_measured — honest qualifier given 303 redirect responses give minimal application-state evidence
- `asset_onchain` = not_applicable (Bitcoin) — correct
- `offramp_cex` = not_measured — honest; the YAML even explicitly distinguishes substrate-anchors-pinned from per-event-slicing-pinned

## Issues / concerns
- The post-event Wayback snapshot is on `www.enexchanger.com` while the pre-event one is `enexchanger.com` — the YAML transparently notes this Host-header difference, but a human reviewer should confirm this does not undermine the "same redirect shell" framing.
- Body_path for the wayback HTML files should ideally be cross-checked on disk for hash integrity, but that is a runtime concern, not an admission concern.

## Recommendation for human reviewer
Confirm the Wayback CDX digests cited in the notes (`4WO4P3H4OIGHSLGBJG2L3SGKLOED3WNU` pre / `JQ4LSL5LOS2KX6REN2UWAGNQBX5GEK4C` post) actually resolve and that the `www.` vs apex difference is acceptable for the "redirect-shell unchanged" claim. Otherwise this is clean.
