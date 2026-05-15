# Null-case audit · lockbit-leader-ofac-2024 · agent A

## Summary verdict
- **agent_verdict**: `pass_with_concerns`
- **confidence**: medium
- **one-sentence justification**: Trigger anchor is strong (OFAC RA + Treasury press release) and the single-address cohort is concrete, but the off-ramp CEX `measured` coding rests entirely on the OFAC trigger page + scope_descriptor with no exchange-search artifact.

## Trigger
- type / actor / timestamp / precision: `ofac_sdn_designation` / `US_OFAC` / 2024-05-07T00:00:00Z / day
- citation admissibility (primary / semi-primary count): 2 primary_legal citations (OFAC RA 20240507 with wayback + body_hash + body_path; Treasury press release jy2328 note only). Solid trigger anchor.
- verdict: pass

## Scoped claim
- which layers were scoped: offramp_cex (`measured`, 14-day window 2024-05-07 → 2024-05-21) against 1 BTC address; all other layers `not_applicable` (Bitcoin native, individual-level).
- is the null-case claim properly bounded? Yes — the `scoped_claim` is short, factual, and limits itself to "datapoint in the LockBit cluster" without overreach. Observation note explicitly says "absence of public disclosure".

## Observation anchors
- layer `offramp_cex` / `observed_no_change` / attribution `none` / anchors present: 1 × `body_hash + body_path` (OFAC RA) + `scope_descriptor` (providers, time_window, addresses_cohort=`khoroshev_lockbit_leader_1_btc`).
  - verdict: concerns — same structural pattern: trigger + scope_descriptor only; no replayable exchange-statement search artifact.

## Coverage status honesty
- `offramp_cex`: `measured` — borderline. 1 concrete BTC address (Khoroshev's `bc1qvhnfknw852ephxyc5hm4q520zmvf9maphetc9z`) is a falsifiable cohort, but no aggregator query artifact replays the absence. Acceptable under the public-disclosure-null reading.
- All other layers `not_applicable` — defensible.

## Issues / concerns
- The Operation Cronos follow-on context is important: KHOROSHEV was unmasked via prior 2024-02-20 LockBit-affiliates action plus law-enforcement seizure. The "no public CEX cascade" claim should be interpreted against a backdrop where exchanges had already been alerted via the February action. This nuance is partially captured in the trigger note but is not surfaced in the observation note.
- Treasury press release citation has no body_hash + body_path.
- Jurisdiction is `[US, UK, AU]` (joint sanction) but the scope_descriptor providers list only major US-focused exchanges — fine for the disclosure-null framing but worth a human eye.

## Recommendation for human reviewer
This case is straightforward as a "public-disclosure CEX null for a single BTC address" but is conceptually entangled with the prior 2024-02-20 LockBit-affiliates event. Human should confirm that the post-Cronos-follow-on context is acceptable as a separate datapoint (i.e. exchanges had already moved on the LockBit cluster three months earlier). Otherwise, treat as aggregate-only.
