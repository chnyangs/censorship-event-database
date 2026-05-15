# Null-case audit · lazarus-laundering-ofac-2020 · agent B

## Summary verdict
- **agent_verdict**: `pass_with_concerns`
- **confidence**: medium
- **one-sentence justification**: Trigger and address enumeration are clean (20 BTC addresses, complete), but the `offramp_cex` coverage status `measured` is anchored only by the OFAC RA capture — same generous-status pattern as the other individual-BTC null events.

## Trigger
- type / actor / timestamp / precision: `ofac_sdn_designation` / `US_OFAC` / `2020-03-02T00:00:00Z` / day
- citation admissibility (primary / semi-primary count): 2 primary_legal (OFAC RA capture with body_hash+body_path+wayback; Treasury SM924 press release, no body_hash)
- verdict: pass

## Scoped claim
- which layers were scoped: `offramp_cex` only (Bitcoin-only individuals, all other layers `not_applicable`)
- is the null-case claim properly bounded? Yes — the scoped_claim is explicitly limited to "datapoint for the individual-BTC-sanction class". The longer prose note in `coverage.offramp_cex.note` is unusually candid about distinguishing public disclosure vs. private chain-analytics workflows.

## Observation anchors
- layer=`offramp_cex` / kind=`observed_no_change` / attribution=`none` / anchors: 1 primary_legal source with body_hash + body_path (OFAC RA capture) + structured `scope_descriptor`
- verdict per row: pass — body_hash+body_path satisfies the validator's replayable-anchor rule; observation note explicitly carves out private chain-analytics workflows as out-of-scope, which is good attribution discipline.

## Coverage status honesty
- `l0_network` = not_applicable — defensible
- `l1_consensus` = not_applicable (Bitcoin, pre-Merge by 929 days) — correct
- `l3_rpc` = not_applicable (Bitcoin) — correct
- `l4_frontend` = not_applicable — correct
- `asset_onchain` = not_applicable (Bitcoin) — correct
- `offramp_cex` = **measured** — concern: same as IRGC and Lazarus-entity, the supporting note is honest but the substrate is the OFAC RA page alone. The note language is the most candid in the corpus ("the offramp-CEX cascade, if any occurred, happened through private chain-analytics-driven KYC flags rather than public corporate statements").

## Issues / concerns
- `analysis_notes` contains a self-contradictory sentence: "Admitting as null_event rather than null_event — the target is individuals without services". One of the two `null_event`s should be a different empirical_shape value (likely `null_event_individual` was intended, or one side of the comparison was edited out). Minor textual bug.
- Same `offramp_cex` = `measured` framing concern.

## Recommendation for human reviewer
Fix the `analysis_notes` typo ("null_event rather than null_event"). Otherwise this event is the cleanest example of the "individual-BTC null" pattern — if the convention is going to stay, this YAML can serve as the template.
