# Methodology — Cross-Layer Censorship Event Study Database

This document specifies **exactly how** an event enters the dataset: what we treat as a trigger, how we reconstruct the cascade per layer, how we verify, how we archive, and how lightweight watcher jobs support both historical backfill and new-event capture. This is the reproducibility contract for the dataset and the methodology appendix for the eventual paper.

> **Want to see the whole pipeline end-to-end with real URLs and commands?** See [example-tornado-cash-2022.md](example-tornado-cash-2022.md) for a worked walkthrough on the canonical pilot event.

## 1. Protocol summary

An event moves through five stages:

```text
TRIGGER DISCOVERED
    ↓
OBSERVATION WINDOW OPENS  (trigger − 24h .. trigger + 8 weeks)
    ↓
LAYER OBSERVATIONS COLLECTED  (per-layer procedures, §4)
    ↓
TWO-SOURCE VERIFICATION  (§5)
    ↓
ADMISSION REVIEW  → event published in release vN
```

Historical events run through the same pipeline with the window already closed. Watchers are allowed to capture new triggers and preserve sources early, but publication still happens only after stabilization and review.

### 1.1 Sampling frame and trigger registry

Case expansion is not ad hoc. The pre-declared frame lives in
[`sampling/frame.yaml`](../sampling/frame.yaml), and the generated
registry lives in
[`analysis/trigger_registry/trigger_registry.md`](../analysis/trigger_registry/trigger_registry.md).
Collection is now open-ended from 2008 onward: 2008-2012 is discovery-only,
2013-2016 is historical baseline, and 2017-present is the comparable main
corpus. The 120 admitted-quality number is a progress milestone under
[`final-collection-protocol.md`](final-collection-protocol.md), not a freeze
target or cap. New discoveries remain candidates until they satisfy the same
admission and human-review gates as the original corpus.

The registry is a pre-admission surface:

1. Every `events/*.yaml` record appears in the registry with its current
   lifecycle status (`admitted`, `draft`, `rejected`, etc.).
2. Watcher or backfill jobs add new candidates under
   `candidate_triggers/*.yaml` before promotion to `events/`.
3. Rejected or out-of-scope triggers remain under
   `candidate_triggers/rejected/*.yaml` so selection decisions are
   auditable.
4. `make trigger-registry` recomputes current counts and the v0.2
   milestone gaps declared in the sampling frame.
5. `make temporal-ledger` records every source-frame/month from 2008-01
   through the dataset cutoff so `pending` months are distinct from searched
   months with no candidate.

The first committed historical backfill is the OFAC recent-actions sweep:
`scripts/materialize_ofac_recent_action_candidates.py` converts the cached
triage artifact at
`sources/ofac_sdn_diffs/opensanctions/ofac-recent-actions-triage.json`
into candidate, promoted, and screened stubs. Rows already represented by
event YAMLs are marked `promoted_to_event`; rows without a concrete crypto
target are retained as `screened_no_extractor_target` and excluded from
distinct in-frame trigger gaps.

The registry does not feed paper counts directly. Paper-facing tables
remain admitted-only. The registry answers a different question: which
triggers were considered, deferred, rejected, or still missing evidence.

### 1.2 Six-artifact reproducibility contract

The project addresses the research gap through six live artifacts:

| artifact | path | contract |
| --- | --- | --- |
| Trigger registry | `analysis/trigger_registry/` | selection transparency and v0.2 expansion gaps |
| Event corpus | `events/*.yaml` | source-of-truth trigger, coverage, observation, and source records |
| Coverage matrix | `derived/coverage_matrix.*`, `derived/l0_coverage_summary.*` | one event-layer row per tracked layer, plus L0 OONI query denominators |
| Evidence chains | `analysis/evidence-chains/` | claim -> observation -> source -> archive/hash -> limitation |
| Paper tables | `analysis/paper_tables/` | admitted-only paper numbers from a fail-closed generator |
| Audit/sensitivity | `analysis/audit_worksheets/`, `derived/admission_sensitivity.*`, `analysis/inter_rater/`, `analysis/staleness.*` | human audit, rubric sensitivity, recoding consistency, and freshness gates |

External benchmark checks live in
`analysis/external_crosschecks/benchmark_crosswalk.yaml`. They are deliberately
outside the six-artifact contract: OONI, Censored Planet, Tornado Cash
event-study work, MEV Watch, and compliance/transparency sources are used to
crosscheck denominator scope, baseline ambiguity, entity normalization, and
claim wording. They do not create an event denominator or satisfy admission
without replayable local evidence.

Any new claim must name which artifact supports it. If the supporting
artifact is absent or stale, `make check` should fail before the paper
surface changes.

The public validation contract is **JSON Schema + `scripts/validate.py`**.
The JSON Schema defines portable structure and enums; `scripts/validate.py`
enforces admission semantics that JSON Schema cannot express cleanly, including
source-threshold logic, replayable null anchors, cross-event action-dedupe
references, and coverage-denominator anchors. Passing JSON Schema alone is not
an admission-grade validation.

## 2. Controlled vocabulary

Used in every YAML field. Centralized in `schema/controlled_vocab.yaml`.

### 2.1 Trigger types

| Code | Meaning |
| --- | --- |
| `ofac_sdn_designation` | OFAC adds an address/entity to the SDN list |
| `ofac_sdn_removal` | OFAC removes (delisting) |
| `doj_indictment` | DOJ criminal indictment touching crypto actors |
| `doj_seizure_order` | Court-authorized seizure of on-chain funds |
| `cftc_action` | CFTC enforcement action |
| `sec_action` | SEC enforcement action |
| `non_us_sanctions` | EU / UK / UN / other state sanctions |
| `court_civil_order` | Civil court freeze / injunction |
| `corporate_policy_change` | Issuer / exchange / frontend policy change |
| `nation_state_block` | Country-level infrastructure block (e.g. CN 2021 ban) |

### 2.2 Layers (matches README §3.2)

`l0_network` · `l1_consensus` · `l3_rpc` · `l4_frontend` · `asset_onchain` · `offramp_cex`

### 2.3 Source types

| Code | Authority | Example |
| --- | --- | --- |
| `primary_legal` | Original legal document | OFAC SDN XML, PACER docket PDF, SEC EDGAR filing |
| `primary_onchain` | Finalized chain data | Tx hash + block number for a freeze event |
| `primary_corporate` | Issuer's own statement | Circle blog / SEC 8-K, archived |
| `semi_primary_measurement` | Independent measurement data | Censored Planet BQ result, OONI probe, Wahrstätter dataset |
| `semi_primary_wayback` | Pinned Wayback snapshot of the primary | Frontend screenshot at T+Δ |
| `supporting_journalism` | Contemporaneous reporting | Reuters / Bloomberg / CoinDesk article |
| `supporting_community` | Forum thread, GitHub issue with evidence | Ethereum-magicians post with tx hash |

**Admission requires at least one `primary_*` source OR two independent `semi_primary_*` sources per layer observation. `supporting_*` sources may corroborate but never satisfy admission on their own. `asset_onchain` is the sole exception: one `primary_onchain` source is sufficient.**

### 2.4 Coverage statuses

Every layer receives one coverage status, even when no positive reaction is observed:

| Code | Meaning |
| --- | --- |
| `measured` | Sufficient source coverage existed to assess the layer in the relevant scope |
| `partially_measured` | Some jurisdictions / providers / chains were covered, but coverage was incomplete |
| `not_measured` | We did not have enough source coverage to make a claim |
| `not_applicable` | The layer does not meaningfully apply to this trigger / target |

### 2.5 Observation semantics

Every layer record distinguishes the factual observation from the causal claim:

| Field | Meaning |
| --- | --- |
| `observation_kind` | `observed_change`, `observed_no_change`, or `coverage_gap` |
| `attribution` | `direct`, `plausible`, `unknown`, or `none` |

`observed_change` means a state transition was seen. `attribution` answers whether that transition can be tied to the trigger, rather than merely occurring in the same window.

`unknown` is reserved for an observed transition whose linkage to the named
trigger is unresolved. It may document a state transition in evidence chains
or cross-event anchors, but it must not enter strong-attribution numerators or
causal prose. Use `none` for `observed_no_change` and `coverage_gap` rows.

## 3. Event lifecycle in detail

### 3.1 Admissibility criteria for the trigger

A candidate trigger must satisfy all of:

1. Identifiable actor with legal or policy authority (no anonymous Twitter rumors).
2. Machine-checkable primary source at a stable URL (archived to Wayback or captured locally at discovery time).
3. Concrete target: address set, protocol contract, domain, asset, or entity.
4. Datable with an explicit precision level. Hour-level or better is required for intraday cascade timing claims; day-level legal or corporate sources may be admitted only when the event records `timestamp_precision: day` and downstream analysis treats the uncertainty explicitly.

### 3.2 Classification fields (schema 0.2.0)

Prior to 2026-04-22 the dataset used a single `event_class` field conflating
three orthogonal things (trigger family / infrastructure theme / empirical
shape). Per 2026-Q2 reviewer feedback, that field was split into three:

- **`research_stratum`** — which stratum the event belongs to in the
  sampling frame:
  - `S1_ofac_sdn` — OFAC SDN designations (2018–2025)
  - `S2_ofac_removal` — OFAC SDN delistings
  - `S3_doj_sec_cftc_fiod` — US federal enforcement (DOJ / SEC / CFTC / FinCEN)
    plus non-US MLAT companion actions (e.g., NL FIOD)
  - `S4_nation_state` — single-country central-bank / emergency-order actions
    (IN RBI, NG CBN, TR CBRT, CN PBOC, CA Emergencies Act, KR FSC Travel Rule)
  - `S5_corporate` — issuer / exchange / frontend unilateral policy (Circle,
    Tether, Uniswap Labs, Coinbase)
  - `S6_supranational` — EU / UN / G7-level actions, including both regulatory
    frameworks (`supranational_regulation` trigger: MiCA) and sanctions
    packages (`non_us_sanctions` trigger: EU Russia sanctions)

  Derived from `trigger.type`; validator enforces the mapping AND
  checks actor/type coherence (e.g., `actor=US_SEC` must carry
  `trigger.type=sec_action`).

- **`empirical_shape`** — the cross-layer reaction shape actually observed:
  - `cascade` — ≥ 3 distinct layers with `observed_change` entries. Main
    analysis unit for cross-layer timing statistics.
  - `comparison` — 1 or 2 distinct layers with `observed_change`.
    Retained for baseline and heterogeneity analysis.
  - `null_event` — 0 observed_change layers. Admitted on the basis of
    `observed_no_change` with admission-grade sources (foreign-operator
    mixer domain survives an OFAC action, individual-level BTC
    designation produces no measurable public cascade). Anchored
    denominator controls, not cascade-analysis anchors.

- **`admission_tier`** — paper-use quality stratification:
  - `anchor_case` — ≥ 2 observed_change layers with attribution ∈
    {direct, plausible}. Suitable for detailed paper exposition.
  - `empirical_case` — ≥ 1 strong-attribution observed_change layer.
    Valid datapoint for aggregate statistics.
  - `null_case` — 0 strong-attribution observed_change layers.
    Anchored denominator control; do not cite as a cascade exemplar.

The paper's main cascade timing statistics are computed on
`empirical_shape == cascade` events; anchor_case events carry most of the
narrative exposition weight.

### 3.3 Observation window

Default: `[trigger − 24h, trigger + 8 weeks]`.

- 24h pre-window captures reactions that preceded public announcement (leaks, prepositioning).
- 8 weeks is empirical — Tornado Cash, Bitzlato, and Garantex cascades all stabilized within 6 weeks; we add buffer.
- Extended window (up to 12 months) applied if any layer still shows active state transitions at week 8.

### 3.4 Stabilization criteria

A layer is "stable" when: no new relevant state transition in that layer for 14 consecutive days. Event moves out of active observation when **all touched layers** are stable **or** the 12-month hard cap is reached.

### 3.5 Admission review

Two-reviewer sign-off required. Reviewers check:

- All observations satisfy the source rule (§5).
- All admission-grade web observation sources have a replayable archive
  anchor (`wayback` or `body_hash` + `body_path`). Supplemental trigger
  citations may include live URL pointers only when at least one trigger
  citation is archived; set `trigger.citation[].evidence_use:
  contextual_unarchived` or `non_admission` for citations that are context
  rather than admission anchors.
- Timestamps are internally consistent (no claim of a reaction before trigger unless the pre-window explicitly flags it).
- Coverage statuses are explicit for every tracked layer.
- Any `coverage[]` row in `measured` or `partially_measured` status has a
  structured denominator artifact on the row itself (`denominator_artifact`)
  or at least one same-layer observation source with a replayable anchor
  (`body_hash` + `body_path`, `query_hash`, `measurement_ids`, `wayback`, or
  primary on-chain id). A `scope_descriptor` explains scope but does not count
  as evidence by itself.
- No observation conflates a measured change with a causal attribution claim.
- The schema validator passes.

## 4. Per-layer observation procedures

Every procedure below is a recipe: input = trigger + target + time window, output = zero or more `observations[]` entries plus one `coverage[]` entry per layer.

### 4.1 L0 — network blocking

**Primary instruments**: Censored Planet BigQuery (weekly snapshots since 2018), OONI public API (volunteer probes).

**v0.1 execution note**: the committed denominator audit is OONI-only.
`derived/l0_coverage_summary.*` summarizes archived OONI query cells and
currently finds no measurement rows for the queried event/domain windows.
Censored Planet ingestion remains a v0.2 expansion task; until it lands, the
paper may report only an OONI denominator gap, not a completed CP + OONI
cross-check.

Procedure:

1. Resolve target to a set of **crypto-relevant domains**: official site, RPC endpoints, block explorer, mixer UI, wallet app backend, CDN endpoints listed in frontend `<script>` tags.
2. Query Censored Planet for each domain × jurisdiction × (window start .. window end). Extract reachability state transitions. At v0.1 this step is specified but not yet ingested into committed derived artifacts.
3. Cross-check with OONI `web_connectivity` measurements from the same jurisdiction. At v0.1 the OONI query artifact is the only committed L0 denominator audit.
4. First decide whether there is an **observed reachability change**. That requires either:
   - both CP and OONI showing a transition within ±24h, or
   - one primary-legal source (e.g. ISP notice, government directive) documenting the block.
5. Then decide attribution:
   - `direct` if a legal / operator source names the target or order explicitly,
   - `plausible` if the transition starts inside the observation window, matches the target domain set, and no broader outage signal appears in IODA / Cloudflare Radar,
   - `unknown` otherwise.

**Known failure mode**: CP snapshots are 2×/week and OONI is volunteer-driven. Events smaller than 3 days may not be sampled, and anomalous OONI measurements can include false positives. Mark sparse cases as `coverage: partially_measured` and use `observation_kind: coverage_gap` when no defensible claim can be made.

`scripts/build_l0_coverage_summary.py` is the local denominator guard for
archived OONI queries. It emits `derived/l0_coverage_summary.*` and labels
zero-result query windows as `no_ooni_measurements`, never as
`observed_no_change`.

`scripts/ooni_batch_query.py` normalizes OONI intake to query cells:
`{event_id, domain, input_url, probe_cc, since, until}`. The legacy
domain mapping is still accepted, but new measurement campaigns should use
the list-of-records form with explicit HTTP/HTTPS variants and probe
countries. Output filenames include a query hash so repeated domain/event
windows cannot overwrite each other.

### 4.2 L1 — consensus-layer filtering

**Primary instruments**: Wahrstätter historical datasets (`mevwatch.info`, `censorship.pics`), `relayscan.io` archives, direct queries against relay data APIs (`ProposerPayloadsDelivered`).

Procedure:

1. Identify target transactions (by `from`, `to`, or address interaction with `target.addresses`).
2. For the observation window, pull **every produced block** and check each against the known relay registry.
3. Compute inclusion-delay distribution for target txs vs control (random txs of similar priority fee). A relay is considered to show filtering evidence iff the target-vs-control delay difference is statistically significant (≥ 2σ over ≥100 target txs) AND the relay's public filtering policy or operator statement confirms it.
4. Annotate `started_filtering_at` = earliest block where the relay first rejects a target tx that another relay accepts.

**Known failure mode**: low-frequency targets (few txs per day) can't hit the 100-tx threshold. In that case, downgrade coverage to `partially_measured`; published relay policy alone can support `attribution: plausible` but not a high-confidence timing claim.

### 4.3 L3 — RPC endpoint rejection

**Primary instruments**: Infura / Alchemy / QuickNode Terms of Service changelogs (via GitHub or Wayback diff), provider status pages, user reports with reproducible tx hashes.

Procedure:

1. Monitor the provider's docs / ToS / status-page git (or Wayback-diff at weekly cadence during observation window) for language changes referencing the target.
2. Collect user-reported rejections: require the report to include a **tx hash or RPC call hash** that we can independently replay. Replay against the provider; if rejection is reproduced, report is admissible.
3. Admission: one primary provider-controlled source (ToS change, docs diff, status page, or replayed rejection) plus either a second primary provider-controlled source or an independent semi-primary measurement artifact. A news article or forum post may corroborate but does not satisfy the threshold.

**Known failure mode**: private API paths (enterprise RPC, WalletConnect internals) are invisible. The dataset explicitly flags these as `l3_rpc_coverage: public_only`. A provider landing page, general filter-list documentation, or public-RPC substrate snapshot establishes that an L3 measurement substrate exists, but it does **not** by itself count as event-specific `partially_measured` coverage or support `observed_no_change`; the event still needs a bracketing provider artifact, replayable rejection, or target-specific filter-list diff.

### 4.4 L4 — frontend delisting / geofence

**Primary instruments**: Wayback Machine, frontend repo git history (open-source repos), frontend JS bundle diff (proprietary frontends).

Procedure:

1. Enumerate candidate frontends: known dApp UIs associated with the target protocol (e.g. `app.uniswap.org` for Uniswap token delistings, `app.tornado.cash` historically).
2. For each frontend, pull all Wayback snapshots in the observation window. Diff for:
    - Disappearance of the target (token symbol, address, asset name).
    - Appearance of geofencing logic (`if country === "US"`).
    - Terms of Service updates.
3. For open-source frontends, match against the repo's commit history for a code-level timestamp. This is the highest-precision layer (commit timestamps are minute-accurate).
4. Distinguish "removed from UI" vs "geofenced by origin" using §4.1 L0 data from the operator's origin country.

**Known failure mode**: JS bundle minification masks semantic changes. Use the git history preferentially; fall back to keyword search in the bundle.

### 4.5 Asset layer — on-chain freeze / blacklist

**Primary instruments**: Etherscan (and chain-specific equivalent) event logs, chain archive nodes.

Procedure:

1. For each stablecoin / frozen-token of interest (USDC, USDT, DAI, BUSD-historical, BNB-B, etc.), identify its admin / blacklist method selectors: `blacklist(address)`, `addBlackList(address)`, `freeze(address)`, `pause()`.
2. Query for all admin-method invocations in the window that affected `target.addresses` — this is fully deterministic from chain data.
3. Record tx hash, block number, block timestamp (to the second), caller address.
4. Cross-verify with the issuer's public statement, if any (Circle / Tether blogs are usually 10 minutes to 2 hours behind the chain action).

This is the **highest-integrity layer** in the dataset — chain data is authoritative, so one `primary_onchain` source suffices for admission at this layer alone.

### 4.6 Off-ramp — CEX delisting / withdrawal freeze

**Primary instruments**: Exchange official announcement pages, API snapshots (`/api/v3/exchangeInfo` and similar), Wayback Machine.

Procedure:

1. Announcement scraping: maintain a registry of official announcement URLs for top 20 exchanges. Poll weekly during the window (or use their RSS where available).
2. API diff: compare the exchange's trading-pair list between snapshots separated by 24h; record pair disappearances for the target asset.
3. Withdrawal freeze: detect via withdrawal status endpoints (`GET /wallet/status?coin=XXX`) where available; otherwise rely on announcement + user report triangulation.
4. Admission: one primary_corporate announcement + one independently observable API / platform change = admissible.

## 5. Verification, attribution, and admission rule

The rule from the README, formalized:

- **Per layer-level observation**: one primary source OR two independent semi-primary sources, EXCEPT `asset_onchain` which accepts one `primary_onchain` source.
- **Independent** means: sources must not derive from each other. A Reuters article that cites "according to [blog]" and the blog itself count as one.
- **Supporting sources**: journalism and community reports can corroborate or guide collection, but never satisfy admission by themselves.
- **Disagreement handling**: if sources disagree on timestamp by > 6h, observation is admitted with a `timestamp_range: [earliest, latest]` instead of a single value, and flagged `precision: hour_range`.
- **Conflict escalation**: if sources disagree on whether the layer reacted at all, observation goes to `unverified/` and is excluded from the release. A conflict note is logged for audit.
- **Observation vs attribution**: an observation may be admitted as `observed_change` with `attribution: unknown` if a state transition is real but the link to the trigger is not defensible.
- **No-reaction claims**: `observed_no_change` is only allowed when `coverage` is `measured` or `partially_measured` and the covered scope is explicit.

## 6. Archival protocol

Every admission-grade web observation source gets archived at the moment of admission. The event YAML stores a Wayback URL or a local `body_hash` + `body_path` replay artifact. Trigger citations follow the same rule for at least one primary trigger source; additional trigger URLs may remain as live pointers when an archived trigger anchor is already present.

```text
for each source.url where source.type in {primary_corporate, primary_legal,
                                           semi_primary_wayback, supporting_journalism,
                                           supporting_community}:
    1. POST to https://web.archive.org/save/<url>
    2. On success, record Wayback timestamp + content hash
    3. On failure (Wayback blocklist, robots.txt, 403):
       - download page locally
       - store WARC under sources/archived_htmls/<event_id>/
       - compute sha256 and record in YAML
```

On-chain sources record a validated 64-hex transaction hash and, when available, a positive block number. A redundant JSON-RPC receipt under `sources/onchain_receipts/<event_id>/<tx_hash>.json` is preferred for release artifacts, but older v0.1 rows may rely on the tx hash plus issuer/tracker body hashes until receipt backfill is complete.

OFAC SDN diffs are archived separately: use Treasury's Sanctions List Service archive for 2022+ and store local snapshots under `sources/ofac_sdn_diffs/YYYY-MM-DD.xml.gz`. This gives us our own working corpus rather than relying on future URL stability.

## 7. Historical backfill — how to collect events from 2008 onward

This is the initial dataset build. Estimated 3 months of work.

### 7.1 Trigger enumeration phase

Work **backward from trigger**, not forward from effects. For the 2008+
tiered frame:

1. **OFAC SDN history**: use Treasury's Sanctions List Service archive for 2022+ and a combination of OpenSanctions + Wayback for older periods. Diff consecutive snapshots to enumerate every designation and removal event. Filter for designations mentioning crypto keywords (`virtual currency`, `digital asset`, known address patterns like `0x[0-9a-f]{40}`). Planning range: 40–80 crypto-relevant SDN candidates in the 8-year window.
2. **DOJ press release archive**: scrape `justice.gov/news` with keyword filters (`cryptocurrency`, `virtual currency`, `mixer`, `blockchain`). Manual review to drop cases where DOJ action did not actually touch on-chain state. Planning range: 20–40 candidates.
3. **Court docket search**: query CourtListener / RECAP for federal filings involving the known target entities surfaced by steps 1–2. Also search for standalone civil freeze orders. This step is additive — most triggers originate from OFAC or DOJ, courts are secondary.
4. **Non-US regulator events**: EU Official Journal (sanctions regulations), UK OFSI consolidated list, selected Chinese / Russian regulatory announcements via established translation sources.
5. **Corporate policy changes**: Uniswap / OpenSea / Circle / Tether / Binance announcement archives, working back in time via Wayback. Only admit corporate events with a traceable external legal trigger or an explicit policy statement.

**Output of this phase**: a triage spreadsheet of ~150 candidate triggers. The screened-out share is recorded explicitly rather than inferred from a target percentage.

### 7.2 Cascade reconstruction phase

For each admitted trigger, run the §4 per-layer procedures with the time window centered on the trigger date. Because data is historical:

- Censored Planet BQ and OONI both have broad historical data back to 2018 and 2012 respectively, but both require explicit coverage accounting before a null claim is made.
- Wahrstätter's MEV data starts late 2022 (post-PBS). Triggers before this have **no L1 observations possible** — record as `l1_consensus: { coverage: not_available_pre_2022 }`.
- Wayback snapshot coverage varies; some frontends have dense coverage (Uniswap), some sparse (Tornado Cash UI went through multiple domains). Use repo history where available.
- Positive on-chain receipts are high-integrity once a transaction is known,
  but no-change denominators are not automatically complete. A rate-eligible
  asset-layer denominator requires a predeclared issuer × chain × target-window
  scan that can count both freezes and non-freezes; v0.1 has not completed
  that independent denominator, so asset-layer rates remain retracted.

### 7.3 Prioritization order

Do not backfill chronologically. Prioritize by **anticipated measurement surface**:

1. Pilot-five (README §5) — proves the pipeline.
2. Events where prior evidence suggests ≥ 3 layers may have measurable artifacts (Tornado Cash family, China 2021, major mixer designations).
3. Events where prior evidence suggests ≥ 2 layers may have measurable artifacts.
4. Single-layer events (mostly asset-only freezes) — useful as comparison cases, but analyzed separately from cascade timing claims.

This ordering lets us stop at any point with a publishable dataset, rather than stopping mid-coverage.

## 8. Watcher-assisted intake for new events

> **Implementation status**: watcher script skeletons (`scripts/watchers/ofac_sdn_watch.py`), the agent drafter (`scripts/agent_draft_event.py`), and the staleness report (`scripts/staleness_report.py`) are committed. Schema support (`origin`, `last_human_audit`, `candidate_triggers/` directory) is in place. Production cron scheduling of the watchers is a separate deployment step; until it runs, intake remains manual.

Two modes run concurrently: **trigger watcher** (always on, lightweight) and **observation engine** (activated per event). These exist to preserve evidence and reduce source loss, not to turn the project into a live dashboard.

### 8.1 Trigger watchers

Cron-scheduled jobs that detect new triggers. Each produces a `candidate_triggers/<date>-<slug>.yaml` stub when it fires.

| Source | Cadence | Detection method |
| --- | --- | --- |
| OFAC SDN XML | Every 6h | diff against previous snapshot; filter crypto keywords / address patterns |
| DOJ press releases | Every 12h | RSS / scrape with keyword filter |
| SEC EDGAR | Daily | filter for 8-K / press releases mentioning crypto enforcement |
| CourtListener RECAP | Daily | search alerts on known entity names + keywords |
| EU OJ / UK OFSI | Daily | sanctions-list diff |
| Stablecoin admin events | Real-time (block subscription) | `eth_subscribe` on `logs` filtered to known admin method topics for USDC / USDT / DAI |
| Issuer blogs | Daily | Wayback integration: RSS where available, diff otherwise |
| Exchange announcements | Every 12h | registry of announcement URLs, keyword filter for target class |

Each watcher is one script under `scripts/watchers/`. Output is append-only to `candidate_triggers/`.

### 8.2 Trigger triage

A human reviewer (initially: the dataset maintainer) scans `candidate_triggers/` at least 2×/week. Decides:

- **Accept** → create `events/<slug>.yaml` stub with `status: observation_active`, activate observation engine.
- **Reject** → file in `candidate_triggers/rejected/` with reason.
- **Defer** → held for additional context.

### 8.3 Observation engine

For each event with `status: observation_active`:

- Re-run all §4 layer procedures **daily** against the newest data.
- Append new observations to the event YAML with timestamps.
- Check stabilization criterion (§3.3). When met, change status to `observation_closed`.
- Move event into the admission review queue.

### 8.4 Admission review queue

Closed events are reviewed (§3.4), then included in the next dataset release. Release cadence: **monthly minor releases** (new events, no schema changes), **quarterly major releases** (schema or methodology updates).

### 8.5 Correction protocol

Post-admission errors happen. Two kinds of update:

- **Errata**: a source link rot, a timestamp correction within ±1h. Applied in place; logged in `CHANGELOG.md`.
- **Retraction**: an observation invalidated by new evidence. Observation is removed from the published event; a `retractions/` record preserves the old state and reason. Paper authors citing a retracted observation are notified via GitHub release notes.

## 9. Reproducibility commitments

For the paper and for external users:

1. Every script in `scripts/` takes deterministic inputs and is idempotent on re-run against the same archived sources.
2. Archived sources are content-hashed; re-running the pipeline against the archive reproduces every observation bit-exactly.
3. The validator (`scripts/validate.py`) re-verifies all citations on every CI run; rot is flagged within 24h.
4. Release tarballs bundle the YAML events, the archived sources, and a manifest of content hashes so downstream users can self-verify.

## 10. Known-uncovered regions (honest scope)

The methodology is silent about (and the dataset will explicitly flag gaps for):

- **Private order flow** (Flashbots Protect, private mempools): no public measurement gives ground truth on filtering inside these; recorded as `l1_consensus.private_orderflow: unmeasured`.
- **KYC-at-onboarding censorship** (wallet creation refusals, IP-gated signup): observable only through user reports; never admitted as primary.
- **Non-English legal triggers**: procedure §7.1 step 4 depends on translated regulatory corpora; coverage is uneven.
- **Pre-PBS L1 filtering** (before mid-2022): no dataset exists; events from this period have `l1_consensus: not_available_pre_2022`.
- **Code-hosting / domain / app-distribution enforcement**: some removals happen at GitHub, registrar, CDN, DNS host, or app-store layers; these are partially covered and remain sparse outside major incidents.
- **Layer-2 sequencer filtering**: handled by the separate L2 tracker project (P2 in the portfolio), not here.

These are **features, not bugs**: explicit scope boundaries make the paper's claims falsifiable and the dataset honest.
