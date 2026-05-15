# Null-case audit · lazarus-entity-ofac-2019 · agent B

## Summary verdict
- **agent_verdict**: `pass_with_concerns`
- **confidence**: medium
- **one-sentence justification**: Historically important entity-level designation with clean primary triggers, but the `offramp_cex` coverage status `measured` rests on the OFAC RA page alone and the trigger primary citation lacks a wayback URL, which is a minor archival-hygiene gap.

## Trigger
- type / actor / timestamp / precision: `ofac_sdn_designation` / `US_OFAC` / `2019-09-13T00:00:00Z` / day
- citation admissibility (primary / semi-primary count): 2 primary_legal (OFAC RA capture with body_hash+body_path but **no wayback URL**; Treasury SM774 press release, no body_hash)
- verdict: pass — body_hash+body_path is itself a sufficient replayable anchor under the validator rule.

## Scoped claim
- which layers were scoped: `offramp_cex` only (entity-level designation with no on-chain addresses → all other layers correctly `not_applicable`)
- is the null-case claim properly bounded? Yes — scoped_claim limits the claim to a historical-anchor entity-level designation, explicitly notes addresses surfaced later in downstream events.

## Observation anchors
- layer=`offramp_cex` / kind=`observed_no_change` / attribution=`none` / anchors: 1 primary_legal source with body_hash + body_path (OFAC RA capture) + structured `scope_descriptor`
- verdict per row: pass — body_hash+body_path satisfies the validator's replayable-anchor rule. As with irgc-ransomware-ofac-2022, the substantive null claim about Binance/Coinbase/Kraken absence is asserted in the note but not anchored to a query log.

## Coverage status honesty
- `l0_network` = not_applicable — defensible (no domain scoped, entity-level)
- `l1_consensus` = not_applicable (pre-Merge by 1097 days) — correct
- `l3_rpc` = not_applicable — correct
- `l4_frontend` = not_applicable (no canonical web presence) — correct
- `asset_onchain` = not_applicable (no on-chain addresses on RA page) — correct
- `offramp_cex` = **measured** — concern: like the IRGC case, the only attached substrate is the OFAC RA page. Status `measured` is generous; `partially_measured` would be more honest.

## Issues / concerns
- Trigger citation [0] is missing a `wayback` URL (the other 12 null events with OFAC triggers all carry wayback URLs in the trigger.citation). Minor archival-hygiene gap.
- Same `offramp_cex` = `measured` framing concern as irgc-ransomware-ofac-2022.
- `related_events` lists `tether-dprk-precommit-freeze-2025` which I should sanity-check exists in the corpus.

## Recommendation for human reviewer
Add a wayback URL to the trigger citation for archival hygiene parity with the rest of the OFAC corpus. Otherwise decide the `offramp_cex.status: measured` convention question once (this event, IRGC, Sichuan-Silence, Matveev, LockBit-leader, Zservers, Russian-cybercrime-infra all use the same pattern).
