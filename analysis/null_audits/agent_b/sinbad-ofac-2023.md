# Null-case audit · sinbad-ofac-2023 · agent B

## Summary verdict
- **agent_verdict**: `pass`
- **confidence**: high
- **one-sentence justification**: This is the textbook well-anchored null event — a real L4 observation backed by two Wayback snapshots bracketing the OFAC designation, an explicit L0 negative-query artifact, and a properly-bounded paper-worthy contrast to Tornado Cash 2022.

## Trigger
- type / actor / timestamp / precision: `ofac_sdn_designation` / `US_OFAC` / `2023-11-29T00:00:00Z` / day
- citation admissibility (primary / semi-primary count): 2 primary_legal (OFAC RA capture with body_hash+body_path+wayback; Treasury JY1933 press release, no body_hash)
- verdict: pass

## Scoped claim
- which layers were scoped: `l4_frontend` (measured), `l0_network` (not_measured with attested negative OONI query), `offramp_cex` (not_measured with substrate-anchors-pinned-but-not-per-event-sliced note); `l1_consensus`/`l3_rpc`/`asset_onchain` correctly `not_applicable` for Bitcoin
- is the null-case claim properly bounded? Yes — scoped_claim is explicitly a structural contrast to Tornado Cash 2022 (Bitcoin native chain, no PBS, no issuer freeze, operator-owned domain). The framing "did not cause a short-term takedown" is appropriately scoped to the 10-day window, not a corpus-wide claim.

## Observation anchors
- layer=`l4_frontend` / kind=`observed_no_change` / attribution=`none` / anchors: 2 semi_primary_wayback sources, each with body_hash + body_path; `evidence_group_id: sinbad-io-wayback-same-day` ties them; timestamp precision = `minute` with `delta_hours: 23.4` from event day
- verdict per row: pass — exemplary anchor: event-day snapshot at 23:25:41 UTC (≈23 hours post-event) plus 10-day-post snapshot, both with content-identity reasoning via Wayback CDX digests in the notes.

## Coverage status honesty
- `l0_network` = **not_measured** with attested OONI negative query (body_hash sha256:49ee17fd…) and explicit "0/1 domains returned any OONI volunteer measurements in the relevant windows" note — exemplary honesty about measurement-gap.
- `l1_consensus` = not_applicable (Bitcoin) — correct; the note explicitly says "marked not_applicable rather than not_measured because the measurement construct itself is undefined for this chain"
- `l3_rpc` = not_applicable (Bitcoin) — correct; same reasoning
- `l4_frontend` = **measured** with scope `[sinbad.io]` and substantive note tying status to the Wayback bracket — honest
- `asset_onchain` = not_applicable (Bitcoin) — correct
- `offramp_cex` = **not_measured** with explicit substrate-anchors-pinned-but-not-per-event-sliced paragraph — exemplary honesty.

## Issues / concerns
- None of substance. This is the model null event.
- `last_verified: 2026-04-21` is the earliest of the 13 events; ensure freshness gate is satisfied.

## Recommendation for human reviewer
This event is ready to stamp `last_human_audit` once the Wayback CDX digests in the notes are spot-checked. The L0 OONI negative-query artifact and the L4 Wayback bracket together exemplify the rubric's intent.
