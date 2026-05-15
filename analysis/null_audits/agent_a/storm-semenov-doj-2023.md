# Null-case audit · storm-semenov-doj-2023 · agent A

## Summary verdict
- **agent_verdict**: `needs_human_review`
- **confidence**: medium
- **one-sentence justification**: This event is structurally entangled with the same-day Semenov OFAC SDN (which triggered a 24-hour Circle USDC batch-freeze cascade), and the observation note acknowledges this — the "no fresh CEX cascade for the DOJ indictment specifically" claim is conceptually parallel to the Pertsev case and similarly hard to separate from the simultaneous OFAC cascade.

## Trigger
- type / actor / timestamp / precision: `doj_indictment` / `US_DOJ_SDNY` / 2023-08-23T00:00:00Z / day
- citation admissibility (primary / semi-primary count): 1 primary_legal citation (DOJ USAO-SDNY press release with body_hash + body_path; no wayback URL pinned). Single anchor.
- verdict: pass_with_concerns — single-source primary trigger from the prosecuting authority; acceptable for a DOJ press release event, but adding a wayback URL would strengthen.

## Scoped claim
- which layers were scoped: offramp_cex (`measured`, 14-day window 2023-08-23 → 2023-09-06); all others `not_applicable`. Tornado Cash frontend was already offline from 2022-08-08; asset-layer activity is attributed to the companion `semenov-ofac-2023` event.
- is the null-case claim properly bounded? The text is bounded ("no fresh CEX policy statement referencing the DOJ indictment distinct from the same-day OFAC Semenov SDN"), and it explicitly acknowledges the entanglement ("CEX cascade bandwidth on 2023-08-23 was absorbed by the OFAC side"). However, this is structurally parallel to `pertsev-nl-arrest-2022` — the null observation is essentially "no incremental cascade attributable to the DOJ trigger when the OFAC trigger fired the same day". This is honest but conceptually thin as a clean null.

## Observation anchors
- layer `offramp_cex` / `observed_no_change` / attribution `none` / anchors present: 1 × `body_hash + body_path` (DOJ press release) + `scope_descriptor` (providers, time_window, addresses_cohort=`storm_semenov_doj_indictment`).
  - verdict: concerns — anchor exists; underlying observation is structurally entangled with the same-day OFAC cascade.

## Coverage status honesty
- `offramp_cex`: `measured` — concerning. The 14-day window starts the same day as the OFAC Semenov SDN, which (per the observation note) triggered a 24-hour Circle USDC batch-freeze. Disentangling DOJ-attributable from OFAC-attributable CEX action in this window is structurally hard. Honest coding might prefer `partially_measured` or `coverage_gap`.
- All other layers `not_applicable` — defensible given the companion-event split.

## Issues / concerns
- **Same-day OFAC entanglement**: this is the systemic issue. The 14-day window is dominated by OFAC-side action; the null claim is essentially "DOJ side alone didn't add to the cascade", which is hard to falsify.
- Single primary citation, no wayback URL pinned.
- The 2024 Storm conviction (SDNY, conspiracy to operate unlicensed money-transmitting business) is mentioned in `analysis_notes` as a follow-on but not catalogued — fine for now.
- `addresses_cohort: storm_semenov_doj_indictment` is an indictment label, not an address set; the companion `semenov-ofac-2023` event carries the 8 ETH addresses.

## Recommendation for human reviewer
Same decision shape as `pertsev-nl-arrest-2022`: human should decide whether the temporal co-occurrence with the OFAC Semenov SDN disqualifies the DOJ-side row from being a clean independent null observation. Options: (a) downgrade to `coverage_gap` reflecting the inseparability; (b) re-scope to a later DOJ-specific milestone (e.g. 2024-07 trial start, 2024 conviction) that is decoupled from the same-day OFAC; (c) keep `observed_no_change` with explicit narrative acknowledgement that this is a "no incremental CEX action attributable to the DOJ side" claim. This case + `pertsev-nl-arrest-2022` are the two highest-confounding nulls aside from sec-v-uniswap.
