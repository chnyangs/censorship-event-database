# Promotion review — kraken-sec-staking-2023

## Verdict
- **promotion_recommendation**: `admit_with_minor_fixes`
- **confidence**: high
- **one-sentence justification**: The trigger and the sole `offramp_cex` observation are both supported by two archived primary sources whose body hashes verify on disk and whose text contains the named-link evidence; the only blockers are an unenumerated `coverage` layer (`l2_l2` is omitted, but more importantly `offramp_cex` is `measured` without a `denominator_artifact`) and the absence of a `last_human_audit` stamp required when origin is promoted off `agent_draft`.

## Trigger gate
- citation count + tier: two `primary_*` citations on `trigger.citation` (lines 19–36): one `primary_legal` (SEC press release 2023-25, line 20) and one `primary_corporate` (Kraken blog settlement statement, line 28). Methodology §3.1 + §5 only require one primary; threshold easily met.
- archive anchors present: yes — both citations carry `body_hash` + `body_path` (lines 22–23, 30–31). I independently re-hashed both local files and got `dbcde40b…3bb2` and `5ee3db50…f41e`, which match the YAML exactly. Both files exist under `sources/http_captures/kraken-sec-staking-2023/primary/`.
- timestamp + precision honest: `2023-02-09T00:00:00Z`, `timestamp_precision: day` (lines 17–18). The SEC press release is dated 2023-02-09 and Kraken's statement is same-day; per methodology §3.1.4, day-level is admissible when the event records it explicitly, which it does. `timestamp_sources` (lines 37–39) cite both. No intraday claim is made anywhere, so the day-precision is honest.
- verdict: **pass**.

## Per-observation gates
- `offramp_cex` / `observed_change` / `direct` / anchor types present: `body_hash` + `body_path` on both `sources[]` entries (lines 93–94, 101–102), matching the schema `source` rule for `primary_legal` and `primary_corporate` types. Two primary sources for one observation row, both replayable. Verdict: **pass**.

(There is only one `observations[]` row; no `observed_no_change` or `coverage_gap` rows are declared.)

## Coverage status honesty
- `l0_network` (line 56): `not_applicable`. Honest — an SEC settlement targeting a staking *service* has no network-reachability surface to assess.
- `l1_consensus` (lines 58–62): `not_applicable` with a `note` explicitly disclaiming protocol-level effect. Honest and well-scoped — the YAML even calls out that "network protocols continued to support staking."
- `l3_rpc` (line 64): `not_applicable`. Honest — no RPC-provider surface implicated.
- `l4_frontend` (lines 65–69): `not_measured`, scope `[kraken.com]`, with note that "No admission-grade historical frontend diff is retained in this file." Honest in spirit, but slightly aggressive scoping: kraken.com clearly *was* changed (the staking page was disabled), and a frontend diff would be feasible from Wayback. Calling it `not_measured` is honest as long as nobody downstream interprets it as "frontend untouched." Acceptable for promotion.
- `asset_onchain` (line 71): `not_applicable`. Honest — no token freeze, no on-chain blacklist call.
- `offramp_cex` (lines 73–79): `measured`, scope `[kraken_us_staking]`. **This is the soft spot.** Methodology §3.5 / admission review checkpoint requires that any `measured` or `partially_measured` row carries either a `denominator_artifact` *on the coverage row* or at least one same-layer observation source with a replayable anchor. The observation row at lines 90–105 *does* carry replayable `body_hash` anchors on both sources, so the coverage row is technically satisfied. But the row itself has no `denominator_artifact`. That is consistent with current schema practice elsewhere in the corpus but worth a maintainer glance.

## Attribution discipline
- `offramp_cex` row (lines 82–105), `attribution: direct`: the SEC source body (verified above) contains the strings `Kraken`, `Payward`, `Staking`, `cease`, `Discontinu`, `30 million`, and the URL slug `press-releases/2023-25`. The Kraken source body contains `Staking`, `unstaked`, `U.S.`, `non-ETH`, `enrolled`, `rewards`, `SEC`, `settlement`. Both sources name the named Kraken entity, the named SEC action, and the discontinued service in plain text. Direct attribution is supported by the named-link standard.

## Scoped claim
The `scoped_claim` (lines 113–116) is unusually conservative and well-written: it says the event is coded *only* as a "U.S.-scoped centralized exchange service shutdown" and explicitly disclaims any "protocol-level staking censorship or token delisting" claim. This stays squarely inside what a `direct`-attribution `offramp_cex` observation can carry: a service-level shutdown by a specific exchange-operator, tied by a named SEC settlement on a stated date, in a stated jurisdiction. The claim does not assert anything about L1 validator behavior, on-chain freeze of tokens, frontend geofencing, or RPC rejection — all of which the YAML correctly marks as `not_applicable` or `not_measured`. The scope (`kraken_us_staking`, line 75) matches the claim wording. **No over-attribution.**

## Self-contradiction check
- `analysis_notes` (lines 107–111) and the `l1_consensus` coverage note (lines 58–62) agree: both say "the file intentionally does not code an L1 consensus change" and "network protocols continued to support staking." Consistent.
- `scoped_claim` (lines 113–116) and `coverage` (lines 55–79) agree on the layer scoping. Consistent.
- `empirical_shape: comparison` (line 7) is consistent with 1 `observed_change` row (lines 82–105) under the §3.2 definition (`comparison` = 1 or 2 observed_change layers).
- `admission_tier: empirical_case` (line 8) is consistent with ≥1 strong-attribution observed_change layer (1 direct row qualifies).
- `research_stratum: S3_doj_sec_cftc_fiod` (line 4) is consistent with `trigger.type: sec_action` + `trigger.actor: US_SEC` per the §3.2 actor-coherence rule.
- `analysis_use: comparable_analysis` (line 6) is consistent with `temporal_tier: comparable_main_2017_present` (line 5).
- No "null_event rather than null_event"–style typos. No coverage/observation/attribution self-contradictions found.

## Specific issues blocking admit_now
- `origin: agent_draft` (line 9). Per the schema `origin` description ("agent_draft = ingested / drafted by an agent and not yet reviewed; **only valid at status=draft**"), promoting `status` to `admitted` while keeping `origin: agent_draft` is *schema-invalid*. The origin field must be flipped to `human_reviewed` (or `human_authored` if a human rewrote it) at the same commit that flips `status` to `admitted`.
- `last_human_audit` is missing entirely. The staleness gate (§1.2, six-artifact contract) treats this field as the canonical timestamp; admitted-tier events should carry it.
- `coverage[].offramp_cex` (lines 73–79) has `status: measured` but no `denominator_artifact` on the row itself. The row currently relies on the observation-row's `body_hash` anchors to satisfy the §3.5 admission checkpoint. That is technically permitted by the worded rule, but a `denominator_artifact` mirroring the SEC body_hash (or pointing to a same-day Kraken status-page snapshot enumerating affected assets) would harden the row. Treat as a soft request, not a hard blocker.

## Recommended fixes (if admit_with_minor_fixes)
- Flip `origin: agent_draft` → `origin: human_reviewed` on line 9 (concurrent with the status flip).
- Add `last_human_audit: 2026-05-16` (today) immediately under `last_verified` (around line 12).
- Optional but recommended: add a `denominator_artifact` to the `offramp_cex` coverage row (around lines 73–79), pointing at the same SEC body_hash + body_path already used by the observation, with a `scope_descriptor` enumerating the affected chains `[ethereum, cardano, solana, polkadot]` so the `measured` claim is structurally anchored at the coverage row, not only indirectly via the observation.
- Optional: tighten the `l4_frontend` note (lines 65–69) by adding one sentence saying the frontend was *known to be* modified per the Kraken statement but no Wayback diff was retained; this keeps `status: not_measured` honest while preventing a future auditor from misreading it as "frontend untouched."
- No other edits required; the trigger gate, observation gate, attribution discipline, and scoped-claim discipline are all sound.
