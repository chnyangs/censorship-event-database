# Null-case audit · irgc-ransomware-ofac-2022 · agent A

## Summary verdict
- **agent_verdict**: `pass_with_concerns`
- **confidence**: medium
- **one-sentence justification**: Trigger is properly anchored and the claim is correctly scoped to a public-disclosure null on 6 BTC addresses, but the `offramp_cex` layer is coded `measured` while the only observation anchor is the OFAC trigger page plus a scope descriptor — per the `null_case_pre_audit.md` rubric, scope_descriptor alone does not replay an exchange-statement absence search.

## Trigger
- type / actor / timestamp / precision: `ofac_sdn_designation` / `US_OFAC` / 2022-09-14T00:00:00Z / day
- citation admissibility (primary / semi-primary count): 2 primary_legal citations (OFAC RA 20220914 + wayback + body_hash + body_path; Treasury press release jy0948 with note only). Solid anchor on OFAC RA.
- verdict: pass

## Scoped claim
- which layers were scoped: offramp_cex (`measured`, 14-day window); all others `not_applicable` (Bitcoin native; 1 day before The Merge so L1 Ethereum is structurally outside).
- is the null-case claim properly bounded (not a corpus-wide claim)? The observation note properly bounds the claim to "no public CEX policy statement" by Binance/Kraken/Coinbase/Bybit and acknowledges private KYT workflows are outside scope. The `scoped_claim` field is more cautious and just describes the designation; defensible.

## Observation anchors
- layer `offramp_cex` / `observed_no_change` / attribution `none` / anchors present: 1 × `body_hash + body_path` (OFAC RA page) + `scope_descriptor` (providers, time_window, addresses_cohort).
  - verdict: concerns — the anchor proves the trigger and the scope but does NOT replay the exchange-statement absence search. Per the LLM pre-audit, this is the correct read of the corpus rule: a legal trigger + scope_descriptor is not an independent evidence anchor for the absence claim.

## Coverage status honesty
- `offramp_cex`: `measured` — borderline. The validator and schema allow it because there is a `body_hash` anchor, but the anchor evidences the trigger, not the absence of CEX statements. A `partially_measured` coding might be more honest given that no aggregator/news scan artifact (a search-results capture, an event-window query log) is pinned. Acceptable under the pre-audit's "public-disclosure CEX null" interpretation.
- `l1_consensus` / `l3_rpc` / `asset_onchain` / `l0_network` / `l4_frontend`: all `not_applicable` — defensible for Bitcoin-only individual designation.

## Issues / concerns
- The `offramp_cex: measured` coding rests on the OFAC RA page being the source of truth for the *absence* claim, which is conceptually weak; the page proves the listing existed, not that no exchange disclosed. The `null_case_pre_audit.md` recommends treating this as a public-disclosure null only.
- The Treasury press release citation has no `body_hash + body_path`. Only the OFAC RA carries the hard anchor.
- The `addresses_cohort: irgc_iranian_6_btc` is a useful scope label, but six bech32/legacy addresses are listed in the target block — no aggregator query was logged demonstrating "we searched X exchanges for Y in this window."

## Recommendation for human reviewer
Human reviewer should decide whether `offramp_cex: measured` is defensible without a CEX-search artifact (the OFAC RA does not constitute a search of exchange statements). Reasonable options: (a) stamp `last_human_audit` with `measured` retained and accept the scope_descriptor + trigger as the corpus convention for public-disclosure nulls (consistent with the pre-audit's recommended limitation text); (b) downgrade to `partially_measured` and add an explicit aggregator/news-search artifact; (c) keep `measured` but tighten `analysis_notes` to explicitly say "public-disclosure null only".
