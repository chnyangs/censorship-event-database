# Top-Venue Upgrade Plan

This is the execution plan for moving the current v0.1 artifact from a
strong dataset / methodology package toward an A/A+ full-paper submission.
The plan is deliberately artifact-gated: a task is not complete until a
file, table, audit worksheet, or validation command proves it.

## Current Baseline

- Corpus: 53 YAML records, 52 admitted, 1 rejected registry row, 0 working drafts.
- Case roles: 2 `anchor_case`, 38 `empirical_case`, 13 `null_case`.
- Review posture: 7 `release_ready_scoped`, 46 `admitted_scope_blocked`.
- Registry posture: 126 trigger-registry rows; 54 distinct in-frame
  triggers against the 150-250 v0.2 target.
- Measurement gaps: `l0_network` and `l3_rpc` have zero measured
  denominators; `asset_onchain` rates remain retracted as structurally
  circular.

## Phase 1 - Thesis And Claim Boundaries

Goal: make the paper read as a denominator-aware measurement protocol and
reproducible corpus, not as a global censorship-prevalence study.

Deliverables:

- `docs/paper_claims.md` states the primary estimand and every claim's
  table source, case-role scope, and forbidden phrasing.
- `README.md`, `docs/limitations-and-use.md`, and `docs/datasheet.md`
  use the current 53-admitted-event snapshot and no longer mention draft
  repair candidates as the current state.
- SEC v. Binance and SEC v. Coinbase are described only as scoped
  CEX/platform-service comparison rows.

Acceptance gate:

- `rg` finds no stale pre-repair corpus-count or SEC draft-repair language in
  paper-facing docs.
- `make paper-check` passes.

## Phase 2 - Sampling Expansion

Goal: expand from a good v0.1 corpus to a predeclared v0.2 sampling frame.

Targets:

- 150-250 distinct in-frame trigger-registry rows.
- 120 admitted-quality events as a progress milestone; the stop rule is
  source-frame exhaustion, not a case cap.
- Stratum gaps are reported explicitly; missing cases are backlog, not
  hidden exclusions.

Priority strata:

- S2 removals / reversals: OFAC delistings, court reversals, corporate
  policy reversals.
- S3 federal enforcement: DOJ / SEC / CFTC / FinCEN actions with
  platform-side artifacts.
- S4 non-US state actions: central-bank, emergency-order, or travel-rule
  events outside the US/EU block.
- S6 supranational: EU / UN / G7 sanctions or regulatory actions with
  concrete crypto targets.

Acceptance gate:

- `make trigger-registry` reports unique target-level frame units, not only
  raw rows, and every candidate has a `source_frame_id` / source-frame
  provenance or is explicitly marked legacy-v0.1.
- The registry contains real non-promoted backlog across S2/S3/S4/S5/S6;
  promoted duplicates and screened OFAC rows do not satisfy the v0.2
  candidate minima by themselves.
- Every promoted event has an archival trigger source and at least one
  admissible observation or anchored null denominator.
- New cases may expand corpus breadth, but they do not support layer-rate
  claims unless their row has `measured_rate_denominator`; L0/L3 remain
  non-rate layers until Phase 4 supplies measurement-grade denominators.

## Phase 3 - Anchor And Release-Ready Promotion

Goal: increase narrative-grade evidence without weakening admission rules.

Targets:

- `anchor_case` count >= 6.
- `release_ready_scoped` count >= 25.
- `admitted_scope_blocked` count <= 25.

Candidate promotion queue:

- `tornado-cash-ofac-delisting-2025` for reversal / recovery exemplar.
- `chatex-ofac-2021` for multi-layer OFAC exchange response.
- `binance-4framework-2023` for large-scale CEX compliance remediation.
- `semenov-ofac-2023` and `circle-usdc-tornado-2022` for asset-layer
  mechanisms with distinct attribution shapes.
- One non-US state action and one supranational action after Phase 2 adds
  enough evidence.

Acceptance gate:

- Each anchor has `last_human_audit`, `scoped_knowledge`, and an evidence
  chain with replayable `body_hash` / `body_path` or primary on-chain IDs.
- Narrative claims cite only anchors; aggregate claims cite only generated
  tables.

## Phase 4 - L0/L3 Denominator Appendix

Goal: turn base-layer non-measurement into a defensible measurement result.

Deliverables:

- `docs/l0-l3-denominator-appendix.md` explaining the denominator model.
- `derived/l0_coverage_summary.*` documents every OONI/Censored-Planet
  query window as measured, zero-result, or no-denominator.
- An L3/RPC provider census distinguishes public endpoints, provider
  documentation, GitHub-visible policy substrates, and private-only
  compliance channels.

Acceptance gate:

- Table 2's `—` rates for L0/L3 can be traced to query/provider evidence,
  not undocumented absence.
- Any L3 named observation remains marked `named_partial_only_no_conditional_rate`
  until a measured provider denominator exists.

## Phase 5 - Artifact Release

Goal: produce a clean artifact-evaluation package.

Deliverables:

- Tagged release with `CITATION.cff`, DOI-ready metadata, and release notes.
- Frozen `dataset.json`, `dataset.csv`, `dataset.meta.json`, derived tables,
  evidence chains, and static site output.
- Docker / Makefile reproduction path: `make check` and `make regenerate`
  from a clean checkout.
- Source manifest for all local HTTP captures and archive hashes.

Acceptance gate:

- `make check`, `make regenerate`, and `python3 scripts/validate.py
  --check-archives events/*.yaml` pass.
- Release notes list known limitations: US-trigger dominance, L0/L3
  denominator gaps, retracted asset-onchain rate, non-independent-human IRR
  unless Phase 3/4 resolves it.
