# tests/ — regression guards and their scope

165 test functions yielding **174 pytest-collected cases** (the
expansion is from parametrized latency-band and safety-class suites),
locking the invariants fixed during the 2026-04-23, 2026-04-24, and
2026-05-06 reviews plus the 2026-06-01 duplicate-YAML-key,
paper-anchor-readiness, and evidence-tier-readiness guards. Runnable via
`make test`; wired into CI (`.github/workflows/validate.yml`) so a
silent regression cannot re-enter main.

## What's covered

| File | Functions | Cases | What it locks |
| --- | --- | --- | --- |
| `test_action_registry.py` | 1 | 1 | Duplicate physical actions are grouped under a canonical `action_id` |
| `test_archetype_classifier.py` | 14 | 23 | 6 archetype rules + priority ordering; latency-regime band inclusivity (parametrized across 8 boundary values); `trigger_is_action` coincidence rule (requires `corporate_policy_change` AND `\|Δt\| ≤ 1h`) |
| `test_capture_http_artifact.py` | 3 | 3 | HTTP capture keeps body/metadata separate, supports user-agent override, and truncates long encoded filenames |
| `test_census_gap_registry_check.py` | 4 | 4 | Census-gap registry counts, exact-id reconciliation, doc-count freshness, and duplicate candidate/registry IDs fail closed |
| `test_coverage_matrix.py` | 3 | 3 | Event-by-layer denominator matrix emits exactly one row per tracked layer and keeps L3/asset rows out of conditional-rate denominators |
| `test_event_metrics_recovery.py` | 7 | 7 | Recovery rows on layers NOT in `changed_layers` are ignored; cascade breadth is coverage-matched; latency consumers see `trigger_is_action` |
| `test_evidence_tier_irr_kappa.py` | 4 | 4 | Evidence-tier IRR scoring rejects incomplete packets by default, supports incomplete summaries without completion claims, validates labels, and computes κ on completed rows |
| `test_ingestion_v03.py` | 17 | 17 | Ingestion DB, source registry, OFAC canary, triage, review packets, repair plans, and human-audit surfaces keep machine and human decisions separated |
| `test_l0_coverage_summary.py` | 5 | 5 | OONI zero-result windows stay observability gaps, non-empty OONI rows expose denominator fields, YAML denominator/source artifacts are read, and L0-applicable-but-unqueried events are surfaced |
| `test_l0_query_metadata_backfill.py` | 1 | 1 | Legacy OONI artifacts are backfilled with query-cell metadata, query hashes, pagination status, and updated body hashes |
| `test_l3_provider_census.py` | 1 | 1 | L3 provider/event census emits named partial and observability-gap rows without creating rate-eligible provider denominators |
| `test_layer_observability.py` | 9 | 9 | Coverage-matched numerator: `changed_under_measured / measured`; L3 partial-only rows, L0 applicable-rate suppression, and structurally circular asset rows are named/descriptive observations, not conditional rates |
| `test_ofac_recent_action_backfill.py` | 3 | 3 | OFAC recent-actions triage materializes promoted, candidate, and screened trigger stubs without changing admitted-event counts or creating cross-directory duplicates |
| `test_ooni_batch_query.py` | 2 | 2 | OONI ingestion normalizes domain/window/probe/url cells and emits query-hash-safe output names |
| `test_paper_readiness_contracts.py` | 4 | 4 | Paper-readiness contracts reject bad corpus-count / CSV-inclusion claims and handle archived-context citation evidence correctly |
| `test_paper_readiness_dryrun.py` | 5 | 5 | Dry-run human-audit and IRR provenance are warnings by default but blocked in strict modes |
| `test_paper_readiness_evidence_tier_irr.py` | 5 | 5 | Evidence-tier IRR report is a working-snapshot warning but a strict reliability blocker until independent human coding clears coverage and κ floors |
| `test_paper_tables_fail_closed.py` | 10 | 10 | Precision helper prefers canonical `trigger.timestamp_precision`; day-precision triggers never enter Panel A; day intervals mark boundary ambiguity; anchorless null cases cause `SystemExit`; L3/asset rate suppression reaches paper/sensitivity tables |
| `test_render_evidence_chain.py` | 3 | 3 | Related draft events render as status text, not dead links; evidence-chain cleanup refuses existing unmarked output directories |
| `test_render_site_safety.py` | 8 | 8 | Static-site rendering refuses destructive output directories, `.git`, symlinked outputs, and existing unmarked directories; raw YAML export publishes admitted records only |
| `test_repair_evidence_anchors.py` | 2 | 2 | Evidence-anchor repair finds missing URLs and recognizes replayable local body, Wayback, query, measurement, and tx anchors |
| `test_repro_source_date_epoch.py` | 6 | 6 | Non-git Docker/source-archive reproduction can derive a deterministic fallback epoch from committed metadata; generated metadata uses checkout-independent paths, source-input hashes, and a declared Python ABI rather than local patch versions |
| `test_review_report.py` | 6 | 6 | Review-report trigger scoring distinguishes missing primary trigger evidence from concrete target-enumeration state, respects claim-usable evidence anchors, does not require changed layers for null cases, and only promotes release-ready anchor cases to paper anchors |
| `test_schema_fail_closed.py` | 10 | 10 | JSON Schema rejects validator-critical bypass shapes for schema-only consumers |
| `test_source_manifest.py` | 3 | 3 | Release source manifest excludes recursive outputs/refetchable clones, hashes event source artifacts deterministically, and paper-readiness re-hashes manifest rows against current files |
| `test_staleness_report.py` | 1 | 1 | Staleness report honors `SOURCE_DATE_EPOCH` so regenerate remains byte-stable |
| `test_temporal_discovery_ledger.py` | 3 | 3 | Temporal ledger emits the complete source-frame month grid and ties candidate-found cells to manifest status |
| `test_trigger_registry.py` | 6 | 6 | Trigger registry includes event/candidate rows under the declared sampling frame, preserves and validates promoted-event links, and rejects unknown registry statuses / early comparable rows |
| `test_v03_yaml_surface.py` | 2 | 2 | Validator rejects internal re-extraction flags and agent-draft claims of primary-source verification in YAML |
| `test_validate_source_rules.py` | 17 | 17 | On-chain tx hashes / block anchors, trigger/source Wayback URL validation, duplicate YAML keys, body-hash verification, nonblank measurement IDs, note-only semi-primary loopholes, `observed_change`/`attribution:none`, denominator anchors, duplicate action IDs, and unknown provider scopes fail closed |

When citing the count in prose, **prefer "174 pytest cases (165 test
functions)"**. `grep -c '^def test_' tests/*.py` gives the function
count; `pytest --collect-only -q` gives the collected-case count.

Every prior review finding has a test that fails-closed on
re-introduction. The suite runs in about 20s locally and is gatekept by CI.

## What's NOT covered — and what "fail-closed" does not mean

The test suite verifies **numerical and structural invariants of the
derivation pipeline**. It does not verify the **semantic content** of
the YAML corpus. Specifically, none of the following are automated by
pytest:

- **Content-validity of evidence anchors.** `body_hash` / `query_hash` /
  `measurement_ids` existence is enforced by `scripts/validate.py`;
  what the anchor *actually shows* is not. A
  Wayback snapshot whose `body_hash` resolves can still be misread
  by the coder.
- **Inter-coder consistency of `coverage.status`.** `measured` vs
  `partially_measured` vs `not_measured` vs `not_applicable` is
  author-assigned; the tests do not cross-check the rubric. An
  inter-rater-reliability study (Cohen's κ) is the appropriate
  instrument here — see `analysis/inter_rater/kappa_report.md` and
  `scripts/compute_irr_kappa.py`.
- **Inter-coder consistency of `observation_kind` / `attribution`.**
  Same caveat. `direct` / `plausible` / `none` is author-assigned.
- **Admission-protocol sensitivity.** The tests do not ablate the
  admission rubric; they assume the current YAML corpus is frozen.
- **Scope of the sampling frame.** The tests do not check that the
  corpus covers any particular jurisdiction or trigger-actor; they
  do not catch over-claiming against a population the corpus does
  not represent.
- **Citation reachability / Wayback drift.** This is checked by
  `make verify-citations` / `make freshness`, not by pytest — those
  targets run in CI on a separate cadence.
- **Paper-table byte-stability under `SOURCE_DATE_EPOCH`.** Asserted by
  CI's `make regenerate` byte-stability round-trip, not by pytest.
- **Prose / README / paper-claims phrasing-lock enforcement.**
  `scripts/check_paper_readiness.py` covers the paper-facing table
  layer; README / paper-claims prose is not automatically checked.

The phrase "fail-closed" in this repo means: if any tested invariant is
violated, `make test` exits non-zero and CI blocks the merge. It does
**not** mean that every review finding is automated;
the review process itself (audit worksheets, quarterly adversarial
audits per `docs/audit-protocol.md`) is the layer that catches
content-validity issues.

## Adding a new test

1. Reproduce the bug with a minimal synthetic event fixture (see
   `test_event_metrics_recovery.py::_event_with_recovery` for the
   canonical pattern).
2. Assert the bug causes the failure mode.
3. Fix the code; the test should now pass.
4. Add the test file to this README's table and to `make test` if a
   new file.

## Running

```bash
# one-shot
make test

# with coverage
python3 -m pytest tests/ -v --cov=scripts

# single file
python3 -m pytest tests/test_paper_tables_fail_closed.py -v
```

CI runs the suite via pinned `requirements-dev.txt` (currently
`pytest==8.3.4`).
