# Null-case audit · irgc-ransomware-ofac-2022 · agent B

## Summary verdict
- **agent_verdict**: `pass_with_concerns`
- **confidence**: medium
- **one-sentence justification**: Trigger and scoped claim are tight, but the `offramp_cex` coverage is flagged `measured` while the only "evidence" is the OFAC RA page itself plus a structured `scope_descriptor` — the substantive observation rests on an unstated literature scan rather than a pinned negative artifact, which is exactly the framing the audit rubric calls out as borderline.

## Trigger
- type / actor / timestamp / precision: `ofac_sdn_designation` / `US_OFAC` / `2022-09-14T00:00:00Z` / day
- citation admissibility (primary / semi-primary count): 2 primary_legal (OFAC RA page with full body_hash+body_path+wayback; Treasury JY0948 press release as secondary primary, no body_hash)
- verdict: pass

## Scoped claim
- which layers were scoped: only `offramp_cex` carries an observation; the YAML correctly notes that the event lies 1 day before The Merge and Bitcoin-only individual targeting renders L0/L1/L3/L4/asset_onchain `not_applicable`
- is the null-case claim properly bounded? Yes — scoped_claim is limited to "datapoint for Iran-related individual-BTC-sanction class" and does not over-claim a corpus-wide null.

## Observation anchors
- layer=`offramp_cex` / kind=`observed_no_change` / attribution=`none` / anchors: 1 primary_legal source with body_hash + body_path (OFAC RA capture) plus a structured `scope_descriptor` (providers, time_window, addresses_cohort)
- verdict per row: pass — the OFAC RA capture satisfies the validator's replayable-anchor rule (body_hash+body_path). The substantive "no Binance/Kraken/Coinbase/Bybit policy statement was published" claim is asserted in the note but not anchored to a query log or measurement_ids; this is a weak but admissible null per the validator.

## Coverage status honesty
- `l0_network` = not_applicable — defensible (Bitcoin individual cohort, no L0 substrate scoped)
- `l1_consensus` = not_applicable (Bitcoin) — correct
- `l3_rpc` = not_applicable (Bitcoin) — correct
- `l4_frontend` = not_applicable — defensible (individuals, no canonical_domain)
- `asset_onchain` = not_applicable (Bitcoin) — correct
- `offramp_cex` = **measured** — concern: the only observation source is the OFAC RA capture (not a CEX-side artifact, not a query log of CEX disclosures, not a chain-analytics report slice). The status `measured` is generous for "we eyeballed exchange newsrooms and found nothing"; `partially_measured` would be more honest given the lack of a per-event chain-analytics slice or exchange-statement query log.

## Issues / concerns
- `offramp_cex` status=`measured` is potentially over-claimed given that the only attached substrate is the OFAC RA page itself. Compare to `lazarus-laundering-ofac-2020` which uses the same pattern and is at minimum consistent.
- The observation note correctly carves out private chain-analytics KYT workflows as out-of-scope, which is good attribution discipline.

## Recommendation for human reviewer
Decide whether the OFAC RA capture alone is sufficient substrate to merit `coverage.offramp_cex.status: measured` on an event where no CEX-side artifact and no query log of exchange newsrooms is pinned. Either (a) downgrade to `partially_measured`, or (b) attach a query_hash for a literature scan, or (c) accept the current pattern as the corpus convention for individual-BTC null events.
