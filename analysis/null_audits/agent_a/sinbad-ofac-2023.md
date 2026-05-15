# Null-case audit · sinbad-ofac-2023 · agent A

## Summary verdict
- **agent_verdict**: `pass`
- **confidence**: high
- **one-sentence justification**: This is one of the two strongest null cases in the set — the L4 frontend `observed_no_change` claim is anchored by two Wayback captures of sinbad.io (event-day +23 hours and +10 days), with explicit OONI-API negative-query documentation for L0 and honest `not_measured` codings elsewhere; the claim is properly scoped and not over-attributed.

## Trigger
- type / actor / timestamp / precision: `ofac_sdn_designation` / `US_OFAC` / 2023-11-29T00:00:00Z / day
- citation admissibility (primary / semi-primary count): 2 primary_legal citations (OFAC RA 20231129 with wayback + body_hash + body_path; Treasury press release jy1933 note only). Solid trigger anchor.
- verdict: pass

## Scoped claim
- which layers were scoped: l4_frontend (`measured`, sinbad.io); l0_network (`not_measured` with attested OONI 0-result query); offramp_cex (`not_measured`); l1/l3/asset_onchain `not_applicable` (Bitcoin native).
- is the null-case claim properly bounded? Yes — the `scoped_claim` is specifically about sinbad.io reachability + content-identity at +23h and +10d post-event, and contrasts with Tornado Cash 2022 L4 specifically. Honest scope, no overreach. attribution=none is correctly applied.

## Observation anchors
- layer `l4_frontend` / `observed_no_change` / attribution `none` / anchors present: 2 × `body_hash + body_path` Wayback captures (sinbad.io 2023-11-29 23:25:41 UTC, sinbad.io 2023-12-09 12:43 UTC). Direct frontend artifacts that *replay* the observation.
  - verdict: pass — this is what a strong frontend null looks like: two independent Wayback captures bracketing the window with archival digests in the note.

## Coverage status honesty
- `l4_frontend`: `measured` — defensible; two pinned Wayback captures with body_hash anchors.
- `l0_network`: `not_measured` with an attested negative-query artifact (OONI API 0 results, body_hash for the JSON) — exemplary honest coding.
- `l1_consensus`, `l3_rpc`, `asset_onchain`: `not_applicable` — defensible (Bitcoin native chain with no PBS / no issuer freeze).
- `offramp_cex`: `not_measured` with chain-analytics-substrate-anchored note — appropriately conservative.

## Issues / concerns
- The two Wayback captures have different digests (IS6YYGAQ... vs FI6T7CEP...). The note says "a variant of the earlier page but with matching core structure" — a human should manually open both HTML files and confirm the variation is benign (e.g. dynamic banner) rather than a substantive change.
- Treasury press release citation has no body_hash + body_path.
- Bitcoin precision claim: the L4 observation has `precision: minute` and `delta_hours: 23.4` — the trigger is day-precision, so any downstream hour-granularity reasoning needs to respect the day-precision discipline. The observation timestamp itself is minute-precision because the Wayback capture has that precision, which is correct, but a human should confirm the `delta_hours` value is not propagated into hour-precision latency tables for the trigger.

## Recommendation for human reviewer
Open both Wayback HTML files (`web.archive.org__web-20231129232541-http-sinbad.io__a971040b77.html` and `web.archive.org__web-20231209124309-https-sinbad.io__65c801905c.html`) and confirm the digest difference is benign (e.g. timestamp, ad banner) rather than substantive content change. If clean, this case is a strong candidate for sign-off. The case is paper-worthy as the structural-contrast to Tornado Cash 2022 (Sinbad's self-hosted infrastructure persisted; Tornado's compliance-mediated infrastructure did not).
