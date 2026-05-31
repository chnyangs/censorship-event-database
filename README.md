# P1 — Cross-Layer Censorship Event Study Database

> Main line 1 of the chain-censorship-measurement research program. See [../docs/3-TODOs.md](../docs/3-TODOs.md) for the overall portfolio rationale.

> **Status as of 2026-05-15**: dryrun release-candidate snapshot, not strict release/submission artifact. `validate`, tests, and working-snapshot paper checks are intended to pass, but the full release gate remains blocked until independent-human IRR, null-case human audit, and human release metadata sign-off are complete on a clean tree. Do not cite this snapshot as strict-release-ready.

## 1. Thesis

**Cross-layer crypto-censorship measurement needs explicit denominators, not implicit zeros. This repository provides a six-artifact measurement protocol, a 52-admitted-event corpus, a fail-closed paper-table generator, and a forkable admission protocol that connect legal / policy triggers to observable stack-layer reactions only where a replayable public evidence substrate exists. Public operator source-control history is one worked mechanism channel: real, structurally narrow, and minute-precise where it exists.**

Two parallel surfaces, designed to be cited together:

- **The substrate census** (8-repo v0.1 public-source-control scan, [`analysis/operator_census/`](analysis/operator_census/)) reports both an *existence proof* (5 substrate edits across 3.5 years on `flashbots/rpc-endpoint::ofacblacklist.go`, including the canonical 2022-08-08 PR #90 *update* and the 2025-04-01 PR #173 *deletion* — bidirectional, primary-corporate, minute-precise) and a *bounded negative result* scoped to the scanned public repos/patterns (6 of the other 7 surveyed repos ship no operative compliance file in public git, or are schema-only).
- **The 53-record YAML snapshot** (`events/*.yaml`, cutoff 2026-05-15) currently contains 52 admitted events, 1 rejected registry row, and no working drafts. Paper-facing tables use admitted events only and answer "for events admitted under a public-evidence rubric, where do reactions land?" under three admission rubrics (strict / current / permissive — see [`derived/admission_sensitivity.md`](derived/admission_sensitivity.md)).

The measurement protocol is implemented as six reproducible artifacts:

| Artifact | Path | Why it exists |
| --- | --- | --- |
| Trigger registry | [`analysis/trigger_registry/trigger_registry.md`](analysis/trigger_registry/trigger_registry.md) | pre-admission selection surface; exposes v0.2 candidate/admitted gaps instead of hiding them |
| Event corpus | [`events/`](events/) | trigger, coverage, observation, source, and status records |
| Coverage matrix | [`derived/coverage_matrix.md`](derived/coverage_matrix.md) | explicit event-by-layer denominator eligibility |
| Evidence chains | [`analysis/evidence-chains/`](analysis/evidence-chains/) | claim -> observation -> source -> archive/hash -> limitation |
| Paper-table generator | [`scripts/build_paper_tables.py`](scripts/build_paper_tables.py) | admitted-only fail-closed paper numbers |
| Audit/sensitivity package | [`analysis/audit_worksheets/`](analysis/audit_worksheets/), [`derived/admission_sensitivity.md`](derived/admission_sensitivity.md), [`analysis/inter_rater/kappa_report.md`](analysis/inter_rater/kappa_report.md), [`analysis/staleness.md`](analysis/staleness.md) | audit, rubric sensitivity, recoding consistency, and freshness gates |

Draft manuscript wrapper: [`docs/paper.md`](docs/paper.md). The manuscript
is generated from the claim lock and paper tables; if it conflicts with
[`docs/paper_claims.md`](docs/paper_claims.md), the claim lock controls.

External validity is tracked separately in
[`analysis/external_crosschecks/`](analysis/external_crosschecks/). That
crosswalk maps OONI, Censored Planet, Tornado Cash event-study work, MEV Watch,
and compliance/transparency sources to the project layers, with explicit
"what it validates / what it cannot validate / how the denominator differs"
rules plus an execution-status ledger. It is a crosscheck layer, not a seventh
admission artifact.

Among the seven explicit choices that distinguish this project:

1. **Coverage-denominator discipline.** Every conditional rate ("within measured rows, what share of layer X changed?") is reported *conditional on that layer having an admission-grade denominator in the dataset* — the numerator is filtered to the same coverage subset as the denominator. Absent measurement is flagged as `—`, not encoded as `0`. This is the methodological backbone: [analysis/paper_tables/table2_layer_observability.md](analysis/paper_tables/table2_layer_observability.md) is the reader-facing instantiation, with strict / current / permissive recomputation for sensitive layers.
2. **The substrate census as a first-class measurement** (existence proof + bounded negative result). [`analysis/operator_census/README.md`](analysis/operator_census/README.md) tiers the 8-repo v0.1 public-source-control scan into `confirmed_filter_file` (n=2) / `glob_swept_matched` (n=2) / `schema_or_index_only` (n=1) / `glob_swept_zero` (n=3), and reports two parallel headline numbers: **5 known-channel substrate edits** across the 1 `known_channel: true` candidate, and **1 OFAC-keyword-subject commit** under the narrow keyword classifier. The two ledgers answer different questions on purpose. PR #90 (2022-08-08, +Tornado pool addresses, 2h 50m post-SDN) and PR #173 (2025-04-01, deletion of the 132-address map, 11d post-delisting) are the bookend events; both live in the substrate-edit ledger, only PR #90 lives in the OFAC-keyword ledger. This is an **existence proof** for the channel and a **bounded negative result** within the scanned public repos/patterns — **not** a population claim about operator behavior. See [`analysis/anchor_gap_fill_log.md §4`](analysis/anchor_gap_fill_log.md) for the per-anchor reproducibility trail.
3. **Precision-aware claims.** Hour-granularity latency claims are computed only from triggers whose `timestamp_precision` is hour-or-better; day-precision triggers are reported in separate panels and never mixed.
4. **Attribution discipline.** `direct` vs `plausible` vs `none` are reported separately in every paper table; collapsing them is a phrasing violation, not a cosmetic choice.
5. **Null cases with evidence anchors, not prose.** An `observed_no_change` row requires at least one of `body_hash`+`body_path`, `query_hash`, or `measurement_ids`; a structured `scope_descriptor` can define the covered scope but is not itself a replayable evidence anchor.
6. **Fail-closed paper-table generator + admission-sensitivity ablation.** `make paper-tables` aborts if a null case is anchorless, if a precision bucket is ambiguous, or if a rate would be emitted without a matched denominator. `make admission-sensitivity` recomputes per-layer rates under three rubrics; `l4_frontend` (Δ=0.13) and `l1_consensus` (Δ=0.29) are flagged sensitive and the paper reports all three rubrics. `l3_rpc` has named Flashbots partial observations but no emitted conditional rate. `asset_onchain` is structurally circular at v0.1 (the admission rubric requires the change as the admission anchor) and **its rate is retracted** in favor of a descriptive observation — see [`docs/paper_claims.md §C1`](docs/paper_claims.md) "Not said".
7. **Schema + admission protocol as a durable artifact.** Other researchers can fork the schema, run the validator, and measure events we did not cover. Layer 2 below.

Delta over prior art:

- **Methodology ancestors transplanted (not invented here)**: OONI (Filastò & Appelbaum, FOCI 2012) + Censored Planet (Sundara Raman et al., CCS 2020) → L0 substrate and coverage-denominator accounting; Pearce et al. "Global DNS Manipulation" (USENIX Sec 2017) → the coverage-matched conditional-rate convention; Gebru et al. "Datasheets for Datasets" (CACM 2021) → the `docs/datasheet.md` template.
- **Wahrstätter et al. "Blockchain Censorship" (ACM WebConf 2024)** — the closest concurrent work, formalizing L1 relay/builder filtering. Delta: we go above their unit of observation (block → event), span 6 layers rather than 1, add explicit trigger models with timestamp precision, and report a multi-repo git-history census of operator compliance that their block-level frame does not address. L1 numbers in this corpus come from them as a semi-primary input; we do not compete at the L1-prevalence question.
- **Chainalysis / Elliptic / TRM** — asset-layer freezes under proprietary feeds, not event-keyed with open provenance. Delta: openness + admission protocol + body-hash anchoring.
- **Nadler & Schär / OFAC event-study papers in finance** — economic / flow-level analyses. Delta: we target stack reactions, not price/volume, and do not attempt event-study finance methodology.

The deliverable has two layers:

- **Layer 1** — a 52-admitted-event corpus (cutoff 2026-05-15; 53 YAML records total, including 1 rejected registry row) under a coverage-denominator discipline, with the Flashbots bidirectional case as a worked mechanism study.
- **Layer 2** — sampling frame (`sampling/frame.yaml`), trigger registry (`analysis/trigger_registry/`), public validation contract (JSON Schema in `schema/event.schema.json` plus admission checks in `scripts/validate.py`), coverage matrix (`derived/coverage_matrix.*`), L0 OONI denominator summary (`derived/l0_coverage_summary.*`), and paper-table generator (`scripts/build_paper_tables.py`) that make the methodology forkable.

Layer 2 is the more durable contribution: the framework stays citable when the specific events age.

## 2. Non-goals (read before citing)

What this repository is *not*, even though a casual reader might expect it to be:

- **Not a cascade rate estimator.** The admitted corpus contains 4 `multi_layer` events under the deterministic archetype classifier; that is not a prevalence estimate for cross-layer cascades in the population. See the FORBID list in [docs/paper_claims.md §5](docs/paper_claims.md) and the survivorship discussion in §3.
- **Not a six-layer coverage claim.** Of the six layers, `l0_network` has zero `measured` denominators and `l3_rpc` has zero `measured` denominators at v0.1.0; their conditional rates are `—`, with L3 retained only as named Flashbots partial observations. Upper-layer (frontend / asset / off-ramp) evidence is where the corpus actually has mass. [Table 2](analysis/paper_tables/table2_layer_observability.md) is the honest picture.
- **Not a predictive model.** No rate from this corpus supports a claim about future enforcement. [docs/limitations-and-use.md §2.1](docs/limitations-and-use.md).
- **Not a compliance service or risk-scoring tool.** [docs/limitations-and-use.md §2.3](docs/limitations-and-use.md).
- **Not a general censorship prevalence statement.** The sampling frame is events with an admissible evidence surface, not a population sample. [docs/paper_claims.md §0 Sampling frame](docs/paper_claims.md).

## 2.5 Why this is the right project to build now

- **Operator-layer behavior can be publicly git-observable in narrow cases.** The Flashbots bidirectional finding is an existence proof that one public operator repository carries filter-list decisions as artifacts with commit-level precision. The v0.1 census finds the substrate is structurally narrow, so this is not a population-wide operator-channel claim.
- **Coverage-denominator discipline is underused in adjacent dataset literature.** Freedom House press-freedom indices, ESG scores, and similar composite-rate datasets frequently mix denominators that are not measurement-matched; doing the honest version is cheap but rare.
- **Low access risk relative to proprietary datasets.** The evidence layer uses public primary sources (SDN lists, court filings, on-chain transactions, operator code repositories, ISP advisories), but public evidence does not make legal, privacy, sanctions, or redistribution risk literally zero.
- **Long half-life.** The admission protocol and paper-table generator are forkable infrastructure; the corpus grows incrementally.

## 3. Scope definition

### 3.1 What counts as an "event"

A trigger action by an identifiable actor that has the *legal or policy* authority to cause downstream censorship. Required fields:

| Field | Example |
| --- | --- |
| Trigger type | SDN listing / court order / corporate policy / sanctions regulator action |
| Trigger actor | OFAC, DOJ, ESMA, Circle Inc., a specific exchange |
| Trigger timestamp | 2022-08-08 14:30 UTC (OFAC Tornado Cash designation) |
| Target | address set / protocol / domain / asset |
| Jurisdiction | US, EU, UK, RU, CN, etc. |

**Not an event**: random Tornado Cash user deciding to stop, a random relay changing its policy for unknown reasons, anecdotal Twitter reports without primary source.

### 3.2 Layers tracked per event

| Layer | Observable | Primary source |
| --- | --- | --- |
| **L0** network | DNS / TCP / TLS blocking of key domains from specific countries | Censored Planet, OONI, contemporaneous ISP notices |
| **L1** consensus | Relay / builder filtering of target txs | mevwatch.info historical, relayscan.io, Wahrstätter datasets |
| **L3** RPC | Public RPC endpoints rejecting calls touching the target | Infura / Alchemy / QuickNode ToS changelogs, user reports with tx-hash evidence |
| **L4** frontend | dApp UIs delisting / geofencing the target | Wayback Machine snapshots, GitHub commit history of frontend repos |
| **Asset** | On-chain freeze / blacklist calls | Etherscan event logs (USDC, USDT, DAI blacklist events) |
| **Off-ramp** | CEX delisting / withdrawal freeze | Exchange press releases, API-level evidence |

Not every event touches every layer. **An event with cross-layer reactions in ≥3 layers is the cascade unit.** The current v0.1 paper surface is broader and more conservative: it measures public observability across all admitted events, while single-layer or two-layer events remain aggregate contributors and comparison cases.

### 3.3 Timestamp precision requirement

**Precision-aware UTC timestamps.** The dataset stores the strongest precision supported by the evidence: second/minute precision for on-chain or commit-level artifacts, hour precision where publication metadata supports it, and day precision where legal or corporate sources publish only dates. Cascade timing analysis must carry this precision explicitly; observations coarser than hour-level are tagged with `precision: day` or `precision: week` and excluded from intraday latency claims.

### 3.4 Multi-source verification rule

**Admission requires at least one primary source OR two independent semi-primary sources per layer-level observation.** `supporting_*` sources may corroborate but do not satisfy the threshold on their own. `asset_onchain` is the sole exception: one `primary_onchain` source is sufficient because finalized chain data is authoritative. Sources must be primary or semi-primary:

- **Primary**: on-chain logs, court PACER filings, OFAC SDN XML diffs, corporate SEC filings, ISP admin notices.
- **Semi-primary**: contemporaneous Wayback snapshot, Wahrstätter / mevwatch archived data, peer-reviewed measurement papers citing the event.
- **Not acceptable alone**: news articles (okay as a second source, never sole), Twitter threads, blog posts, Chainalysis summaries (paywalled, uncheckable).

## 4. Data schema

One event = one YAML file under `events/<slug>.yaml`.

```yaml
id: tornado-cash-ofac-2022
trigger:
  type: ofac_sdn_designation
  actor: US_OFAC
  timestamp: 2022-08-08T14:30:00Z
  citation:
    - https://ofac.treasury.gov/recent-actions/20220808
    - sdn_xml_diff_hash: <sha256>
target:
  kind: address_set
  addresses: [0x8589...d2c5, ...]
  protocol: tornado_cash
  chains: [ethereum]
jurisdiction: [US]

coverage:
  - layer: l0_network
    status: not_measured
    scope: [OONI public web-connectivity query windows]
    note: archived OONI queries returned no measurement denominator
  - layer: l1_consensus
    status: measured
    chain: ethereum

observations:
  - layer: asset_onchain
    actor: circle_usdc
    event: blacklist_addresses
    observation_kind: observed_change
    attribution: direct
    timestamp: 2022-08-08T19:25:00Z
    delta_hours: 4.9
    sources:
      - type: primary_onchain
        tx: 0x...
        block: 15306080
      - type: primary_corporate
        url: https://www.circle.com/blog/...
        archived: https://web.archive.org/web/...
  - layer: l3_rpc
    actor: infura
    event: endpoint_rejection
    observation_kind: observed_change
    attribution: plausible
    timestamp: 2022-08-08T18:10:00Z  # approximate, see notes
    delta_hours: 3.7
    precision: hour
    sources:
      - type: primary_corporate
        url: ...
      - type: semi_primary_measurement
        url: ...
  # ... more observations

recovery:
  - layer: asset
    resolved: false  # USDC freezes not reverted as of 2026-04
  - layer: l3_rpc
    resolved_timestamp: 2025-03-21T00:00:00Z  # post-delisting
    citation: [ofac-delisting-2025]

analysis_notes: |
  Primary cascade completed within 5 hours across 3 layers.
  L0 remains an observability gap in this snapshot; archived OONI
  query windows returned no denominator and cannot support a
  no-blocking claim.
  Significant because...

tags: [sanctions, privacy_tool, stablecoin_freeze]
```

## 5. Current Snapshot Status

The pilot phase is complete. The repo now carries a 53-admitted-event working snapshot with no draft event YAMLs, generated paper tables, and an explicit human-audit queue.

Release/submission readiness is intentionally stricter than working-snapshot validity:

- Working snapshot: `make check` and `make paper-check` are intended to validate the current artifact surface without mutating paper outputs.
- Release/submission snapshot: `python3 scripts/check_paper_readiness.py --strict-audit --strict-null-audit --strict-repro --strict-reliability` must pass from a clean intended source tree.
- Human gates cannot be substituted by agents: independent-human IRR, codebook-4.0 `evidence_tier` IRR, H2 null-case audit, and H3 release sign-off are tracked in [`human-audit.md`](human-audit.md) and [`analysis/NEXT_STEPS.md`](analysis/NEXT_STEPS.md).

## 6. v0.2 expansion frame (more cases without losing denominator discipline)

Expansion is governed by [`sampling/frame.yaml`](sampling/frame.yaml), not
by ad hoc additions. The current frame is open-ended from 2008 onward:
`2008-2012` is a discovery-only monthly ledger, `2013-2016` is a historical
baseline, and `2017-present` is the comparable main corpus. **150-250 distinct
in-frame triggers** and **120 admitted-quality events** are milestones, not
stop rules or caps. The source-frame exhaustion rule and tier semantics are
documented in
[`docs/final-collection-protocol.md`](docs/final-collection-protocol.md).
Current gaps are generated by `make trigger-registry` under
[`analysis/trigger_registry/trigger_registry.md`](analysis/trigger_registry/trigger_registry.md).
The monthly source-frame ledger is generated by `make temporal-ledger` under
[`analysis/temporal_ledger/`](analysis/temporal_ledger/), including a
year-level control surface at
[`analysis/temporal_ledger/yearly_collection_plan.md`](analysis/temporal_ledger/yearly_collection_plan.md)
for working from 2008 through the current cutoff.
Draft/rejected/screened/deferred trigger stubs remain in the registry so
selection decisions are visible, but target gaps exclude promoted
duplicates and extractor-screened rows.

The first systematic backfill is the OFAC recent-actions sweep:
`make ofac-recent-action-candidates` materializes the cached triage file
under `sources/ofac_sdn_diffs/opensanctions/` into 73 registry stubs
(`candidate`, `promoted_to_event`, or `screened_no_extractor_target`).
This expands the audit surface without changing the admitted-event count
or satisfying the S1 in-frame quota by itself.

Grouped by trigger type, the expansion backlog should prioritize:

### OFAC SDN actions

- Tornado Cash 2022 + 2025 delisting
- Blender.io 2022
- Garantex 2022
- Hydra Market 2022
- Chatex 2021
- SUEX 2021
- Secondary designations involving mixers and ransomware wallets

### DOJ / criminal actions

- Bitzlato 2023
- Silk Road BTC seizures (historical, tests pre-2020 tooling)
- Hydra takedown 2022
- BTC-e seizure 2017

### Court orders

- Various freeze orders on specific addresses
- CFTC actions against DeFi frontends

### Corporate policy / compliance

- Uniswap frontend token delistings (2023 batch)
- OpenSea NFT delistings
- Circle / Tether freezing specific addresses outside sanctions contexts

### Non-US regulator actions

- ESMA-triggered EU exchange actions
- UK FCA policy changes affecting stablecoins
- Russia's VPN blocks as they touched crypto infrastructure
- China's 2021 crypto ban (L0-heavy cascade, tests non-sanctions trigger)

## 7. Methodology paper outline

Target venue: **IMC 2026 (Cycle 2, Aug decision)** as primary — its explicit
artifact / replicability track is the best fit for a dataset + methodology paper
spanning network + consensus + RPC + frontend + asset + off-ramp observations.
**AFT 2026** remains a secondary target for the empirical-finance framing of the
same dataset (event-study of regulatory cascades on crypto infrastructure).

Proposed structure:

1. **Motivation** — prior measurement work sees individual stack layers well but does not connect identified enforcement triggers to observable operator behavior across the stack with open, auditable provenance. The substrate of interest — public source-control history of crypto operators — has been informally noted but not treated as a bounded, reproducible measurement channel. We treat it as one under explicit coverage limits.
2. **Methodology contribution (the framework)** — pre-declared sampling frame; trigger registry; six-layer admission protocol; event-by-layer coverage matrix; L0 OONI denominator summary that separates no measurements from no blocking; coverage-matched conditional rates (transplanted from Pearce et al. 2017 / OONI / Censored Planet, credited as such); three-rubric admission-sensitivity ablation (`derived/admission_sensitivity.md`); precision-aware latency filtering; attribution discipline; fail-closed paper-table generation that aborts on anchorless nulls or denominator mismatch; substrate census methodology with `repo_tier` + `known_channel` + subject-only keyword classification.
3. **Substrate census (a measurable channel + a bounded negative result)** — [`analysis/operator_census/`](analysis/operator_census/). The 8-repo v0.1 public-source-control scan is tiered into `confirmed_filter_file` (n=2) / `glob_swept_matched` (n=2) / `schema_or_index_only` (n=1) / `glob_swept_zero` (n=3). Two parallel headline numbers: **5 known-channel substrate edits** across the 1 `known_channel: true` candidate (the wide ledger; bookend events PR #90 and PR #173 both visible), and **1 OFAC-keyword commit** across the scanned repos (the narrow ledger). The two ledgers are reported separately on purpose. The Flashbots PR #90 (2022-08-08, `+Tornado pool addresses` 2h 50m post-SDN, direct attribution) and PR #173 (2025-04-01, deletion of the 132-address map 11d post-OFAC-delisting, plausible attribution — frames as operational cleanup) anchor the existence proof; the 6 surveyed repos with no compliance file (or schema-only) are the bounded negative result that says *"this substrate is real but rare in the scanned public source-control frame"*.
4. **52 admitted events + coverage-discipline (the paper corpus)** — 53 YAML records across 6 strata, with 52 admitted under the v0.1 protocol and 1 rejected row retained for registry transparency; coverage-matched layer observability ([Table 2](analysis/paper_tables/table2_layer_observability.md)) under three rubrics for sensitive layers; single-layer dominance in the changed-event subset (36 / 40 changed events) is descriptive rather than population-inferential; the Tornado reversal (PR #173) appears only inside §3's substrate-edit ledger, not as a standalone recovery-rate claim.
5. **Negative / observability result** — `l0_network` and `l3_rpc` have zero `measured` denominators in the admitted corpus; `l3_rpc` keeps two named Flashbots git-history observations without emitting a conditional rate; `asset_onchain`'s 17/17 = 1.00 is structurally circular and **its rate is retracted** at v0.1 (kept as a descriptive observation; reinstatement requires a coverage rubric that does not require the change as the admission anchor). Under the same admission protocol anyone can fork, **public-record-visible evidence of base-layer crypto censorship is genuinely thin**, and the usual denominator-implicit reporting of "L0 shows no censorship" is unsafe. This is what the dataset + substrate census jointly make *measurable*.
6. **Limitations and scope boundary** — sampling frame is admissibility-bounded, English-indexable, and US/EU-trigger-dominant; survivorship bias in the evidence substrate is structural; hour-precision latency is supportable only on named events, not as a distribution; the substrate census is bounded to the candidates list and excludes private repos / server-side compliance. κ for `coverage_status`, `observation_kind`, and `attribution` is currently a *self-consistency check* (LLM-assisted blinded recode under same-family provenance), not an `independent_human` reliability estimate; an independent-human pass is v0.2 open work.
7. **Open dataset + schema + replication package** — Zenodo-minted DOI, fail-closed regeneration pipeline gated by `make paper-check`, byte-stable artifacts under `SOURCE_DATE_EPOCH`, per-event audit worksheets, CC-BY-4.0 data + MIT code, CI exercises the full reproduction path.

**Primary contribution (framework-level)**: a forkable admission protocol + paper-table generator + substrate census methodology that make cross-layer enforcement observability measurable with coverage-matched conditional rates, attribution discipline, body-hash-anchored evidence, three-rubric sensitivity reporting, and a tiered substrate census with parallel wide / narrow ledgers. Layer 2 in the Thesis.

**Substantive findings** (paper §3–§5):

- (existence proof) the Flashbots `rpc-endpoint::ofacblacklist.go` bidirectional case — 5 known-channel substrate edits across 3.5 years, including PR #90 and PR #173, body-hash-verifiable;
- (bounded negative result) 6 of 7 other surveyed repos in the 8-repo v0.1 public-source-control scan ship no operative compliance file in public git, or are schema-only — the substrate is real but rare in the scanned public source-control frame;
- (upper-stack admissible-evidence concentration under coverage-matched conditioning, with three-rubric reporting for sensitive layers) C1 — this is a statement about public measurement substrates, not layer reaction propensity; the asset_onchain rate is retracted at v0.1 (structural circularity); L4 frontend and L1 consensus are reported strict / current / permissive; L3 RPC carries two named Flashbots partial observations from the Tornado bookend events but no conditional rate; L0 has no measured denominator;
- (observability gap on base layers as a measured feature, not an artifact of curation).

**What this paper explicitly does not claim**: that operator-layer filter-list maintenance is the dominant crypto-censorship mechanism in the wild; that the six-layer split captures the population; that the rate figures estimate a population prevalence; that the Tornado bookend events alone establish a generalizable operator channel; that the κ figures establish inter-rater reliability under independent-human provenance. See [docs/paper_claims.md §0 "What this paper is NOT"](docs/paper_claims.md).

## 7.5 Browsing the dataset

Three surfaces for reading the catalog:

- **Live site (recommended for review)** — run `make render-site` to generate `site/index.html` locally; open in a browser. The site shows all events with filters by class/year/chain and one page per event. Auto-deployed on push via `.github/workflows/site.yml` if GitHub Pages is enabled for the repo.
- **Raw YAMLs** — `events/*.yaml` with full primary-source citations, body_hashes, and analysis notes. Validate-clean via `make validate`.
- **Markdown indices** — `EVENTS-CHECKLIST.md` for admission status per stratum, `CHANGELOG.md` for chronological provenance, `analysis/review-report.md` for readiness scoring.
- **Datasheet** — [docs/datasheet.md](docs/datasheet.md) follows Gebru et al.'s "Datasheets for Datasets" template and is the single-page intake point for external consumers (motivation, composition, admission protocol, biases, distribution).
- **Citation** — [`CITATION.cff`](CITATION.cff) is the canonical machine-readable record (GitHub renders a "Cite this repository" button from it; Zenodo reads it on each tagged release to mint a DOI). [docs/citing.md](docs/citing.md) holds BibTeX / APA / Chicago templates and the release cadence. [docs/releasing.md](docs/releasing.md) documents the Zenodo ↔ GitHub integration (one-time setup, then tag-to-DOI on every release).
- **Stable metadata** — [`dataset.meta.json`](dataset.meta.json) is emitted on every `make dataset` run and pins version, cutoff date, schema, commit, and per-facet counts. `dataset.json` / `dataset.csv` are the all-event YAML registry surface; `paper_corpus_included=true` and `paper_corpus_event_count` identify the admitted-only paper corpus. This is the file downstream pipelines / site / evidence-chain / comparable-case reports read to stamp their output with a consistent snapshot identity.
- **Trigger registry** — [`analysis/trigger_registry/trigger_registry.md`](analysis/trigger_registry/trigger_registry.md) shows every YAML event plus candidate/rejected trigger stubs and v0.2 expansion gaps.
- **Coverage matrix** — [`derived/coverage_matrix.md`](derived/coverage_matrix.md) is the event-by-layer denominator eligibility surface behind Table 2.
- **License** — two licenses, one per artifact class. The dataset + docs are **CC-BY-4.0** ([`LICENSE`](LICENSE)); the code is **MIT** ([`LICENSE-CODE`](LICENSE-CODE)). Full split + rationale in [`NOTICE`](NOTICE) and [`docs/limitations-and-use.md §6`](docs/limitations-and-use.md).

Three framework tools are built on the dataset (see [docs/limitations-and-use.md](docs/limitations-and-use.md) before using any output):

- **A. Evidence Chain** — `make render-evidence SLUG=<slug>` emits a structured "claim → observations → sources (body_hash) → honest gaps" argument per event. `make render-evidence-all` regenerates admitted-event chains under `analysis/evidence-chains/`.
- **B. Comparable-Case Finder** — `make compare LIKE=<slug> TOP=5` returns top-N historical precedents structurally similar to the reference event, with transparent feature-weight breakdown and divergence factors. Also accepts `--trigger-type` / `--actor` / `--stratum` / ... for proposed actions.
- **C. Decision Rubric** — [docs/decision-rubric.md](docs/decision-rubric.md) — hand-followed structural checklist mapping features to historical pattern classes. Comparative, not predictive.

All common operations are wired into the `Makefile` — run `make help` for the full list.

## 8. Repo structure

```text
p1-event-db/
  README.md                    # this file
	  schema/
	    event.schema.json          # JSON Schema half of the validation contract
	    controlled_vocab.yaml      # enum of trigger types, layers, source types
	  sampling/
	    frame.yaml                 # pre-declared sampling frame + v0.2 quotas
	  candidate_triggers/
	    README.md                  # pre-admission trigger-stub workflow
	  events/
	    tornado-cash-ofac-2022.yaml
	    ...
  templates/
    event.yaml                # starter event template
  sources/
    archived_htmls/            # pinned Wayback snapshots
    http_captures/             # local current-state web capture bundles
    onchain_receipts/          # tx / block JSON snapshots
    ofac_sdn_diffs/            # daily SDN XML diffs
  scripts/
    validate.py                # admission-rule validation + citation check
    verify_citations.py        # URL reachability and archive freshness checks
    build_dataset.py           # emit unified JSON / CSV release
    freshness_check.py         # alert if a source link 404s
	    capture_http_artifact.py   # save local bundles for current-state web evidence
	    build_trigger_registry.py  # pre-admission selection surface
	    build_coverage_matrix.py   # event×layer denominator eligibility
	    draft_gap_report.py        # summarize unresolved evidence gaps in draft events
    status_report.py           # emit machine-readable pilot status summary
    review_report.py           # score process robustness and case readiness
    render_site.py             # render events/*.yaml → static HTML site under site/
    ooni_batch_query.py        # systematic OONI Explorer API query for L0 substrate
    build_l0_coverage_summary.py # denominator-aware L0 query summary
    batch_usdtbanlist_check.py # asset-layer batch scan via usdtbanlist.com
  Makefile                    # unified QA / dataset build entrypoints
	  analysis/
	    trigger_registry/          # generated registry CSV/JSON/MD
	    paper/                     # TeX + figure notebooks
    pilot-status.md            # human-readable pilot readiness notes
    review-report.md           # human-readable robustness / case review output
    descriptives.ipynb
  docs/
    methodology.md             # detailed provenance rules
    process-checklist.md       # lifecycle entry / exit criteria
    case-review-rubric.md      # reliability / completeness rubric for cases
    contributor-guide.md       # how to propose a new event
  CHANGELOG.md
```

## 9. Milestones & gates

| Month | Milestone | Decision gate |
| --- | --- | --- |
| 1 | v0.1 protocol frozen: schema, validator, trigger registry, coverage matrix, paper-table generator. | If `make check` or `make trigger-registry` fails, do not add cases. |
| 2 | Expand registry to 150-250 trigger rows under `sampling/frame.yaml` by adding systematic backfills beyond OFAC. | If candidate gaps remain concentrated in one stratum, keep paper framing US-trigger-dominant and descriptive. |
| 3 | Promote admitted-quality events with archived evidence chains; 120 is the current progress milestone, not a cap. | If L0/L3 denominators remain absent, report observability gaps, not zero rates. |
| 4 | Rebuild asset independent denominator and L0/RPC targeted measurement slices. | Only reinstate asset/L3 rates after denominator source exists outside positive-change admission. |
| 5 | Independent-human IRR pass and paper submission package. | If independent-human κ fails, keep attribution-sensitive claims parked. |

## 10. Quality standards (non-negotiable)

1. **Admission rule** — a layer-level observation needs one primary source or two independent semi-primary sources; `supporting_*` sources never satisfy admission by themselves.
2. **Precision-aware timing** — every timestamp carries a `precision` value; observations coarser than hour-level are excluded from intraday cascade timing analysis.
3. **Archival requirement** — every admission-grade web observation source must have a Wayback snapshot or a local `body_hash` + `body_path` replay artifact recorded at admission time; trigger citations must include at least one replayable archived anchor, with extra live URL pointers allowed only as supplements.
4. **Reversibility** — every event is reviewable; the `validate.py` script must re-verify all citations against archived copies and flag rot.
5. **Coverage accounting** — every layer must record `measured`, `partially_measured`, `not_measured`, or `not_applicable`; "no reaction observed" is only allowed when coverage is explicit.
6. **Contributor vetting** — external contributions go through two-reviewer approval, modeled on CVE numbering authority practice.

## 10.5 Maintainer

| | |
| --- | --- |
| Editor-in-chief | Xiangwen Yang (<xwy411@gmail.com>) |
| Capacity commitment | 5-10 h/month for the 12 months following the first admitted release |
| Inbound response SLA | 48 hours |
| Release attribution | Monthly CHANGELOG entries carry the editor-in-chief's name on each release line |
| Escape hatch | If two consecutive months fall below 2 h of actual investment, the repo switches to `maintenance_paused` in the top-level README rather than silently going stale (see [docs/3-TODOs.md Observatory section](../docs/3-TODOs.md)) |

Agent-assisted ingestion (drafts, captures, Wayback submissions) is permitted; admission, adversarial audits, and stakeholder communication remain human responsibilities. The v0.3 ingestion monitor is documented in [docs/ingestion-v03.md](docs/ingestion-v03.md); it writes local candidates and review-queue entries, not verified paper rows. See [docs/audit-protocol.md](docs/audit-protocol.md) for the quarterly adversarial audit commitment.

## 11. Explicit non-goals

- **Not a real-time dashboard product**. The static site is a navigational
  research dashboard for the frozen artifact surface; it is not a live
  observatory or monitoring UI.
- **Not a real-time observatory product**. Lightweight trigger watchers are allowed for archival coverage, but published events are admitted only after the cascade stabilizes under an explicit observation window.
- **Not a sanctions compliance tool, and not a prescriptive playbook**. The dataset is a **descriptive historical record with open provenance** — what happened, when, and with what evidence. It is **not** a normative statement about how future events should be handled, not a compliance determination, not legal advice, and not an expert opinion on covered-party status. Lawyers, regulators, compliance teams, and journalists may cite specific cascade timelines as factual evidence in their own work; the project takes no position on the legal or policy conclusions they draw. The distinction matters because it keeps the project in the role of archivist / witness rather than expert witness, and prevents adversarial use of the dataset's edge cases against the methodology itself.
- **Not a Chainalysis replacement**. The edge is rigorous cross-layer timelines with open provenance, not asset-flow analytics.
- **Scope does not expand to active probing infrastructure.** This repo may run passive watchers, archival jobs, and replayable verification scripts, but not a bespoke internet-scale measurement platform. Those belong to main line 2 if at all.

## 12. Dependencies & risks

### External data dependencies

- OFAC Sanctions List Service XML archive for 2022+ plus older SDN history sources (public, stable).
- Wahrstätter / mevwatch historical data (public, maintained by one person — some continuity risk).
- Censored Planet BigQuery (stable, funded).
- Wayback Machine (stable, but non-guaranteed; budget for occasional missing snapshots).

### Key risks

- **Verification bottleneck** — if human audit and multi-source discipline take longer than expected, strict release/submission slips. Mitigation: publish only working-snapshot language until H1/H2/H3 clear.
- **Null regularity** — the admitted events may not yield a striking pattern. Mitigation: paper angle stays denominator-aware observability rather than prevalence.
- **New cascading event during project** — a 2026 cascade could be captured in real-time as a case study, enriching the paper.

## 13. Immediate Hardening Backlog

1. Complete H1 independent-human IRR using `make irr-packet` and `make irr-kappa`; keep current LLM-assisted κ phrased as self-consistency only.
2. Complete H2 null-case audits before using null cases as named narrative evidence or stronger denominator claims.
3. Complete H3 release sign-off: update `CITATION.cff`, regenerate from a clean intended tree, and run the full strict gate.
4. Keep operator-census language fixed to the 8-repo v0.1 public-source-control scan; do not promote it to an operator-population census.
5. Expand v0.2 only after denominator artifacts and claim locks are stable: S2 reversals, S4 non-US state, S3 federal enforcement, then S6/S5.
