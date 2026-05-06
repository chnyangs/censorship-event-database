# tests/ — regression guards and their scope

65 test functions yielding **74 pytest-collected cases** (the
expansion is from parametrized latency-band and safety-class suites),
locking the invariants fixed during the 2026-04-23, 2026-04-24, and
2026-05-06
reviews. Runnable via `make test`; wired into CI
(`.github/workflows/validate.yml`) so a silent regression cannot
re-enter main.

## What's covered

| File | Functions | Cases | What it locks |
| --- | --- | --- | --- |
| `test_archetype_classifier.py` | 14 | 23 | 6 archetype rules + priority ordering; latency-regime band inclusivity (parametrized across 8 boundary values); `trigger_is_action` coincidence rule (requires `corporate_policy_change` AND `\|Δt\| ≤ 1h`) |
| `test_layer_observability.py` | 8 | 8 | Coverage-matched numerator: `changed_under_measured / measured`; L3 partial-only rows and structurally circular asset rows are named/descriptive observations, not conditional rates |
| `test_event_metrics_recovery.py` | 3 | 3 | Recovery rows on layers NOT in `changed_layers` are ignored (the 2026-04-23 P2 fix — prevents tally inflation) |
| `test_paper_tables_fail_closed.py` | 9 | 9 | Precision helper prefers canonical `trigger.timestamp_precision`; day-precision triggers never enter Panel A; anchorless null cases cause `SystemExit`; L3/asset rate suppression reaches paper/sensitivity tables |
| `test_render_evidence_chain.py` | 2 | 2 | Related draft events render as status text, not dead links; evidence-chain cleanup refuses existing unmarked output directories |
| `test_render_site_safety.py` | 8 | 8 | Static-site rendering refuses destructive output directories, `.git`, symlinked outputs, and existing unmarked directories; raw YAML export publishes admitted records only |
| `test_repro_source_date_epoch.py` | 1 | 1 | Non-git Docker/source-archive reproduction can derive a deterministic fallback epoch from committed metadata |
| `test_schema_fail_closed.py` | 10 | 10 | JSON Schema rejects validator-critical bypass shapes for schema-only consumers |
| `test_staleness_report.py` | 1 | 1 | Staleness report honors `SOURCE_DATE_EPOCH` so regenerate remains byte-stable |
| `test_validate_source_rules.py` | 9 | 9 | On-chain tx hashes / block anchors, trigger/source Wayback URL validation, nonblank measurement IDs, note-only semi-primary source loopholes, `observed_change`/`attribution:none`, and unknown provider scopes fail closed |

When citing the count in prose, **prefer "74 pytest cases (65 test
functions)"**. `grep -c '^def test_' tests/*.py` gives the function
count; `pytest --collect-only -q` gives the collected-case count.

Every prior review finding has a test that fails-closed on
re-introduction. The suite runs in about 1s and is gatekept by CI.

## What's NOT covered — and what "fail-closed" does not mean

The test suite verifies **numerical and structural invariants of the
derivation pipeline**. It does not verify the **semantic content** of
the YAML corpus. Specifically, none of the following are automated by
pytest:

- **Content-validity of evidence anchors.** `body_hash` / `query_hash` /
  `measurement_ids` / `scope_descriptor` existence is enforced by
  `scripts/validate.py`; what the anchor *actually shows* is not. A
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
