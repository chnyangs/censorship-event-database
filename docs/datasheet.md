# Datasheet: Cross-Layer Censorship Event Database

Follows the template of Gebru et al., "Datasheets for Datasets" (CACM 2021).
Intended to be read alongside [../README.md](../README.md) and
[methodology.md](methodology.md). Length is deliberately short; each section
points at the authoritative source of truth in the repo rather than restating it.

## 1. Motivation

- **Purpose**: a curated catalog of crypto censorship events with cross-layer,
  hour-precision, multi-source-verified observations of how each event
  propagated through network (L0), consensus (L1), RPC (L3), frontend (L4),
  asset on-chain, and CEX off-ramp layers.
- **Intended tasks**: event-study analysis of regulatory cascades; empirical
  baseline for censorship-resistance claims; reference for journalism, policy,
  and systems research. Not for compliance, legal determination, or predictive
  sanction-screening (see [limitations-and-use.md](limitations-and-use.md)).
- **Funder / creator**: human-maintained by Xiangwen Yang; agent-assisted
  ingestion allowed at `origin=agent_draft` stage, admission is human-only.

## 2. Composition

- **Instances**: each row is a single censorship event defined by a trigger
  action (OFAC SDN, DOJ indictment, corporate policy, nation-state block, etc.)
  and one or more layer-level observations.
- **Count at release time**: see `dataset.csv` header count + `analysis/pilot-status.json`.
- **Per-instance fields**: governed by [../schema/event.schema.json](../schema/event.schema.json).
- **Labels**: `research_stratum` (S1–S6 trigger family), `empirical_shape`
  (cascade / comparison / null_event), `admission_tier` (anchor / empirical /
  null). Rules for each are in `validate.py::_check_field_consistency`.
- **Null cases**: `null_event` rows with `observed_no_change` observations are
  deliberately included to avoid survivorship bias.
- **Missingness**: every layer is explicitly accounted for — `measured` /
  `partially_measured` / `not_measured` / `not_applicable`. Missing fields are
  a validation error, not a silent gap (README §10.5).

## 3. Collection process

- **Acquisition**: primary sources pulled from OFAC Sanctions List Service,
  court PACER filings, exchange press releases, and on-chain receipts; semi-
  primary from published measurement datasets (Wahrstätter / relayscan CSVs,
  OONI Explorer, Censored Planet) and Wayback snapshots.
- **Admission protocol**: one `primary_*` source OR two independent
  `semi_primary_*` sources per layer-level observation. `supporting_*` never
  satisfies admission alone. `asset_onchain` accepts one `primary_onchain`.
  Rule enforced in `validate.py::_validate_sources`.
- **Attribution gates**: `attribution=direct` requires a primary source
  (enforced 2026-04-22). Two semi-primary measurements downgrade to
  `attribution=plausible`.
- **Archival**: every web source is required to have either a Wayback URL or a
  local `body_hash` + `body_path` pair (plus `query_hash` for measurement API
  pulls). The weekly `freshness.yml` workflow rechecks reachability.
- **Instrumentation**: ingestion scripts live under `scripts/`; the `Makefile`
  wires them into a single `make all` / `make validate` surface.

## 4. Preprocessing / Cleaning / Labeling

- YAML files are the ground truth. `build_dataset.py` emits the JSON and CSV
  release artifacts deterministically from those YAMLs.
- Timestamps stored in UTC ISO-8601; `precision` enum documents the claimed
  granularity (`second`–`week`); the validator ensures `delta_hours` matches
  the trigger-to-observation gap within the stated tolerance.
- No model-derived labels. Stratum / shape / tier are derived from explicit
  admissions-rule counts in validator, not inferred statistically.

## 5. Uses

- **Appropriate**: empirical measurement research on censorship cascades,
  event-study papers, pedagogical examples of cross-layer failure modes,
  contextual journalism that cites specific timelines with provenance.
- **Inappropriate**: sanctions compliance, covered-party determination, legal
  opinion, predictive sanction screening. See
  [limitations-and-use.md](limitations-and-use.md) for the full disclaimer.
- **Known biases**:
  - US-regulator events are over-represented because their provenance is
    easiest to verify (OFAC SDN XML diff + treasury.gov press releases).
  - L0 network observations are sparse where OONI coverage is thin.
  - Off-ramp CEX observations lean on press releases; private API-level
    evidence is rare.

## 6. Distribution

- Repository: this repo.
- License: see the `LICENSE` file at the repo root when published (the dataset
  is released openly so other researchers can extend it; the Layer-2 schema
  contribution depends on this).
- Citation: pending DOI. At time of release, cite by the git tag + URL; once a
  Zenodo deposit exists, cite the DOI.

## 7. Maintenance

- **Editor-in-chief**: Xiangwen Yang (<xwy411@gmail.com>).
- **Cadence**: 5–10 h/month for the first 12 months post-release (see README §10.5).
- **Update protocol**: schema changes bump `schema_version`; breaking changes
  bump the major version and are announced in `CHANGELOG.md`. The `staleness_report.py`
  flags events whose `last_human_audit` date has aged past the audit window
  (see [audit-protocol.md](audit-protocol.md)).
- **Contribution**: external PRs go through two-reviewer approval
  ([contributor-guide.md](contributor-guide.md)). Agent-drafted events are
  admitted only after `origin: human_reviewed`.
