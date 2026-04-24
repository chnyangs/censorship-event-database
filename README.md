# P1 — Cross-Layer Censorship Event Study Database

> Main line 1 of the chain-censorship-measurement research program. See [../docs/3-TODOs.md](../docs/3-TODOs.md) for the overall portfolio rationale.

## 1. Thesis

**A coverage-denominator-disciplined catalog of publicly documented crypto censorship events, instrumented to ask what operators actually do — with a worked mechanism finding on operator filter-list maintenance as a git-observable censorship channel, and a reusable admission protocol for cross-layer enforcement observation.**

Prior measurement work sees individual layers well but does not connect identified enforcement triggers to observable operator behavior across the stack with open, auditable provenance. Among the seven explicit choices that distinguish this project:

1. **Coverage-denominator discipline.** Every conditional rate ("how often does layer X react to triggers like these?") is reported *conditional on that layer having an admission-grade denominator in the dataset* — the numerator is filtered to the same coverage subset as the denominator. Absent measurement is flagged as `—`, not encoded as `0`. This is the methodological backbone: [analysis/paper_tables/table2_layer_observability.md](analysis/paper_tables/table2_layer_observability.md) is the reader-facing instantiation.
2. **A worked mechanism finding — operator filter-list maintenance as a public, git-observable channel.** Flashbots' [rpc-endpoint::ofacblacklist.go](https://github.com/flashbots/rpc-endpoint) adds OFAC-listed Tornado pool addresses via commit `92ab6b1f` **2h 50m** after the 2022-08-08 SDN (PR #90 "update ofac black list"), and the entire 132-address map is deleted in commit `1e9c29c` eleven days after OFAC's 2025-03-21 delisting (PR #173). Same infrastructure, bidirectional, primary-corporate, minute-precise. See [analysis/anchor_gap_fill_log.md §4](analysis/anchor_gap_fill_log.md).
3. **Precision-aware claims.** Hour-granularity latency claims are computed only from triggers whose `timestamp_precision` is hour-or-better; day-precision triggers are reported in separate panels and never mixed.
4. **Attribution discipline.** `direct` vs `plausible` vs `none` are reported separately in every paper table; collapsing them is a phrasing violation, not a cosmetic choice.
5. **Null cases with evidence anchors, not prose.** An `observed_no_change` row requires at least one of `body_hash`+`body_path`, `query_hash`, `measurement_ids`, or a structured `scope_descriptor` — the null denominator is auditable at the artifact level.
6. **Fail-closed paper-table generator.** `make paper-tables` aborts if a null case is anchorless, if a precision bucket is ambiguous, or if a rate would be emitted without a matched denominator. The generator is the single source of truth for every number in the paper.
7. **Schema + admission protocol as a durable artifact.** Other researchers can fork the schema, run the validator, and measure events we did not cover. Layer 2 below.

Delta over prior art:

- **Wahrstätter et al. ("Blockchain Censorship", ACM WebConf 2024)** — formalize L1 relay/builder filtering on Ethereum; the present corpus uses their data as the L1 semi-primary substrate. Delta: event-keying plus the mechanism-channel finding on `rpc-endpoint` git-history (a different operator surface than PBS relays).
- **Censored Planet (CCS 2020+)** — global connection-tampering; not crypto-keyed. The present corpus queried OONI for anchor domains and records the null result as a measurement gap.
- **Chainalysis / Elliptic / TRM** — asset-layer freezes under proprietary feeds, not event-keyed with open provenance. Delta: openness + admission protocol.
- **Prior OFAC event-study papers in finance** — price/flow reactions; not stack reactions.

The deliverable has two layers:

- **Layer 1** — a 53-event corpus (cutoff 2026-04-22) under a coverage-denominator discipline, with the Flashbots bidirectional case as a worked mechanism study.
- **Layer 2** — schema (`schema/event.schema.json`), admission protocol (`scripts/validate.py`), and paper-table generator (`scripts/build_paper_tables.py`) that make the methodology forkable.

Layer 2 is the more durable contribution: the framework stays citable when the specific events age.

## 2. Non-goals (read before citing)

What this repository is *not*, even though a casual reader might expect it to be:

- **Not a cascade rate estimator.** The corpus contains 5 `multi_layer` events under the deterministic archetype classifier; that is not a prevalence estimate for cross-layer cascades in the population. See the FORBID list in [docs/paper_claims.md §5](docs/paper_claims.md) and the survivorship discussion in §3.
- **Not a six-layer coverage claim.** Of the six layers, `l0_network` has zero `measured` denominators and `l3_rpc` has zero `measured` denominators at v0.1.0; their conditional rates are either `—` or under partial coverage only. Upper-layer (frontend / asset / off-ramp) evidence is where the corpus actually has mass. [Table 2](analysis/paper_tables/table2_layer_observability.md) is the honest picture.
- **Not a predictive model.** No rate from this corpus supports a claim about future enforcement. [docs/limitations-and-use.md §2.1](docs/limitations-and-use.md).
- **Not a compliance service or risk-scoring tool.** [docs/limitations-and-use.md §2.3](docs/limitations-and-use.md).
- **Not a general censorship prevalence statement.** The sampling frame is events with an admissible evidence surface, not a population sample. [docs/paper_claims.md §0 Sampling frame](docs/paper_claims.md).

## 2.5 Why this is the right project to build now

- **Operator-layer behavior is publicly git-observable for the first time.** The Flashbots bidirectional finding is the existence proof that public operator repositories carry filter-list decisions as artifacts with commit-level precision. This channel did not exist before mid-2022 and was not archived by any measurement project until this corpus.
- **Coverage-denominator discipline is underused in adjacent dataset literature.** Freedom House press-freedom indices, ESG scores, and similar composite-rate datasets frequently mix denominators that are not measurement-matched; doing the honest version is cheap but rare.
- **Zero legal risk.** All evidence is public primary sources (SDN lists, court filings, on-chain transactions, operator code repositories, ISP advisories).
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

Not every event touches every layer. **An event with cross-layer reactions in ≥3 layers is the target unit of analysis.** Single-layer or two-layer events are still retained as comparison cases, but they are not the headline "cascade" unit for the paper.

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
    status: partially_measured
    scope: [IR, RU, DE, US]
    note: OONI coverage sparse outside listed jurisdictions
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
  No L0 layer reaction observed (crypto networks were not
  nationally blocked anywhere as direct response).
  Significant because...

tags: [sanctions, privacy_tool, stablecoin_freeze]
```

## 5. Pilot events (first 5)

These are chosen to exercise the schema and verify multi-source discipline works:

1. **Tornado Cash OFAC designation (2022-08-08)** — canonical cross-layer cascade, 4+ layers touched.
2. **Tornado Cash OFAC delisting (2025-03-21)** — the reverse cascade; tests whether recovery is measurable.
3. **Bitzlato DOJ action (2023-01-18)** — different actor type (DOJ not OFAC), different target type (exchange not protocol).
4. **Garantex sanctions (2022-04-05)** — RU-targeted, tests jurisdiction axis and whether EU/US cascades diverge.
5. **USDC Iran-address freeze (pick a specific documented case)** — single-layer comparison case to test non-cascade events and null coverage handling.

If the schema survives these 5 without modification, proceed to scale. If not, fix schema first.

## 6. Candidate events for full dataset (20-50 target)

Grouped by trigger type. Exact selection refined after pilots.

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

1. **Motivation** — prior measurement work sees layers individually; a coverage-denominator-disciplined catalog reveals *where public operator behavior is actually observable* and *where it is not*, and operator source code is an under-used substrate.
2. **Methodology contribution** — the six-layer admission protocol, coverage-matched conditional rates, precision-aware latency filtering, attribution discipline, and fail-closed paper-table generation as a reusable measurement framework.
3. **Mechanism finding — Flashbots rpc-endpoint** — primary case study: `ofacblacklist.go` grows by +Tornado-pool addresses in PR #90, **2h 50m** after the 2022-08-08 SDN (direct attribution via commit title "update ofac black list"), and the entire 132-entry map is deleted in PR #173, eleven days after OFAC's 2025-03-21 delisting (plausible attribution; PR title frames as operational cleanup, not policy). Bidirectional, minute-precise, primary-corporate, and visible **only** because the operator's code is public.
4. **Dataset** — 53 events across 6 strata; coverage-matched layer observability ([Table 2](analysis/paper_tables/table2_layer_observability.md)); single-layer dominance in the admitted corpus (35 / 53); bidirectional Tornado case as sole reversal event (n=1).
5. **Negative / observability result** — `l0_network` and `l3_rpc` have zero `measured` denominators in the admitted corpus. Under the same admission protocol anyone can fork, **public-record-visible evidence of base-layer crypto censorship is genuinely thin**, and the usual denominator-implicit reporting of "L0 shows no censorship" is unsafe. This is what the dataset makes *measurable*.
6. **Limitations** — sampling frame is admissibility-bounded, not population; survivorship bias in the evidence substrate is structural, not fixable by adding events; hour-precision latency is supportable only on named events, not as a distribution.
7. **Open dataset + schema + replication package** — Zenodo-minted DOI, fail-closed regeneration pipeline, per-event audit worksheets, CC-BY-4.0 data + MIT code.

**Primary finding (headline)**: operator filter-list maintenance is a public, git-observable censorship channel with minute-level precision and bidirectional response to OFAC state. Both directions of the Tornado Cash cascade on Flashbots' rpc-endpoint are archived with body_hash-verifiable commit state; this is the first dataset to pin that channel.

**Secondary (supporting) findings**: (a) upper-layer concentration under coverage-matched conditioning; (b) single-layer dominance (35 / 53) in the admitted corpus; (c) observability gap on L0 / L1 / L3 as a measured feature of the public evidentiary substrate, not an artifact of curation.

## 7.5 Browsing the dataset

Three surfaces for reading the catalog:

- **Live site (recommended for review)** — run `make render-site` to generate `site/index.html` locally; open in a browser. The site shows all events with filters by class/year/chain and one page per event. Auto-deployed on push via `.github/workflows/site.yml` if GitHub Pages is enabled for the repo.
- **Raw YAMLs** — `events/*.yaml` with full primary-source citations, body_hashes, and analysis notes. Validate-clean via `make validate`.
- **Markdown indices** — `EVENTS-CHECKLIST.md` for admission status per stratum, `CHANGELOG.md` for chronological provenance, `analysis/review-report.md` for readiness scoring.
- **Datasheet** — [docs/datasheet.md](docs/datasheet.md) follows Gebru et al.'s "Datasheets for Datasets" template and is the single-page intake point for external consumers (motivation, composition, admission protocol, biases, distribution).
- **Citation** — [`CITATION.cff`](CITATION.cff) is the canonical machine-readable record (GitHub renders a "Cite this repository" button from it; Zenodo reads it on each tagged release to mint a DOI). [docs/citing.md](docs/citing.md) holds BibTeX / APA / Chicago templates and the release cadence. [docs/releasing.md](docs/releasing.md) documents the Zenodo ↔ GitHub integration (one-time setup, then tag-to-DOI on every release).
- **Stable metadata** — [`dataset.meta.json`](dataset.meta.json) is emitted on every `make dataset` run and pins version, cutoff date, schema, commit, and per-facet counts. This is the file downstream pipelines / site / evidence-chain / comparable-case reports read to stamp their output with a consistent snapshot identity.
- **License** — two licenses, one per artifact class. The dataset + docs are **CC-BY-4.0** ([`LICENSE`](LICENSE)); the code is **MIT** ([`LICENSE-CODE`](LICENSE-CODE)). Full split + rationale in [`NOTICE`](NOTICE) and [`docs/limitations-and-use.md §6`](docs/limitations-and-use.md).

Three framework tools are built on the dataset (see [docs/limitations-and-use.md](docs/limitations-and-use.md) before using any output):

- **A. Evidence Chain** — `make render-evidence SLUG=<slug>` emits a structured "claim → observations → sources (body_hash) → honest gaps" argument per event. `make render-evidence-all` regenerates all 53 under `analysis/evidence-chains/`.
- **B. Comparable-Case Finder** — `make compare LIKE=<slug> TOP=5` returns top-N historical precedents structurally similar to the reference event, with transparent feature-weight breakdown and divergence factors. Also accepts `--trigger-type` / `--actor` / `--stratum` / ... for proposed actions.
- **C. Decision Rubric** — [docs/decision-rubric.md](docs/decision-rubric.md) — hand-followed structural checklist mapping features to historical pattern classes. Comparative, not predictive.

All common operations are wired into the `Makefile` — run `make help` for the full list.

## 8. Repo structure

```text
p1-event-db/
  README.md                    # this file
  schema/
    event.schema.json          # JSON Schema for validation
    controlled_vocab.yaml      # enum of trigger types, layers, source types
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
    validate.py                # schema validation + citation check
    verify_citations.py        # URL reachability and archive freshness checks
    build_dataset.py           # emit unified JSON / CSV release
    freshness_check.py         # alert if a source link 404s
    capture_http_artifact.py   # save local bundles for current-state web evidence
    draft_gap_report.py        # summarize unresolved evidence gaps in draft events
    status_report.py           # emit machine-readable pilot status summary
    review_report.py           # score process robustness and case readiness
    render_site.py             # render events/*.yaml → static HTML site under site/
    ooni_batch_query.py        # systematic OONI Explorer API query for L0 substrate
    batch_usdtbanlist_check.py # asset-layer batch scan via usdtbanlist.com
  Makefile                    # unified QA / dataset build entrypoints
  analysis/
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
| 1 | Schema frozen after 5 pilot events. JSON-Schema validator works. | If schema still under revision at month 1 end → shrink scope before proceeding. |
| 2 | 12 events complete with full multi-source verification. | If verification is taking >1 week per event → loosen to semi-primary or drop events that can't be verified. |
| 3 | 20 events done. First descriptive statistics. | If no non-trivial regularities visible at 20 events → reassess methodology paper angle. |
| 4 | Paper draft v1. Optional: extend to 30-50 events. | Submit to AFT if deadline fits; else target IMC. |
| 5 | Submit paper. Release v1 dataset publicly. | Observatory-integration question revisited. |

## 10. Quality standards (non-negotiable)

1. **Admission rule** — a layer-level observation needs one primary source or two independent semi-primary sources; `supporting_*` sources never satisfy admission by themselves.
2. **Precision-aware timing** — every timestamp carries a `precision` value; observations coarser than hour-level are excluded from intraday cascade timing analysis.
3. **Archival requirement** — every web-based source must have a Wayback snapshot or a local `body_hash` + `body_path` replay artifact recorded at admission time.
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

Agent-assisted ingestion (drafts, captures, Wayback submissions) is permitted; admission, adversarial audits, and stakeholder communication remain human responsibilities. See [docs/audit-protocol.md](docs/audit-protocol.md) for the quarterly adversarial audit commitment.

## 11. Explicit non-goals

- **Not a dashboard**. No live UI. Static site generation from dataset is optional and low priority.
- **Not a real-time observatory product**. Lightweight trigger watchers are allowed for archival completeness, but published events are admitted only after the cascade stabilizes (typically 2-8 weeks post-trigger).
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

- **Verification bottleneck** — if multi-source discipline takes longer than estimated, the 20-event target slips. Mitigation: month-2 gate explicitly asks this question.
- **Null regularity** — the 20-50 events may not yield a striking pattern. Mitigation: paper angle can pivot to "cascade heterogeneity" as a negative-result contribution.
- **New cascading event during project** — a 2026 cascade could be captured in real-time as a case study, enriching the paper.

## 13. Immediate next actions

1. Replace placeholder notes in the pilot drafts with concrete archived artifacts, receipts, and query hashes.
2. Promote the strongest 1-2 pilot events from `draft` to admission-ready status.
3. Decide citation-archival tooling (Wayback direct API vs a local WARC store).
4. Use `scripts/draft_gap_report.py` to drive evidence collection across pilots.
5. Use `scripts/status_report.py` to keep admitted-vs-draft pilot readiness visible as the dataset evolves.
6. Use `scripts/review_report.py` to keep process robustness and case-design quality explicit as the pilots evolve.
7. Treat `release_ready_scoped` cases as publishable only for the narrow empirical claim already supported by artifacts.
8. For live web evidence, create and retain a local bundle with `scripts/capture_http_artifact.py` before relying on the claim.
