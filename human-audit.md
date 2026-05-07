# Human Audit Queue

Status as of 2026-05-07. This file tracks work that should not be faked or
auto-stamped by scripts/agents. Machine-verifiable gates currently pass in
working-snapshot mode; the items below require independent human judgment,
sign-off, or release authority.

Related LLM pre-audit: [`analysis/llm_expert_audit/`](analysis/llm_expert_audit/).
The LLM-Expert-Audit is useful for triage and issue discovery, but it does not
complete any item in this file.

## Two-Stage Audit Model

| Audit class | Status | What it can do | What it cannot do |
| --- | --- | --- | --- |
| LLM-Expert-Audit | Completed for the current null-case/repro scope | Identify methodological risks, evidence-anchor gaps, and release-provenance blockers before human review. | Stamp `last_human_audit`, satisfy `independent_human` IRR, or authorize release. |
| Human-Expert-Audit | Pending | Confirm semantic evidence sufficiency, denominator scope, and independent blinded recodes. | Reuse LLM conclusions as a substitute for independent judgment. |

## Current Human Blockers

| ID | Blocker | Why human | Blocks |
| --- | --- | --- | --- |
| H1 | Independent-human IRR pass | Current `analysis/inter_rater/kappa_report.*` uses `llm_assisted_blinded`; it can support self-consistency only, not independent reliability. | `--strict-reliability`, A-class/A+ submission reliability claims |
| H2 | Null-case denominator audit for 13 events | A human must confirm that each null case's `observed_no_change` evidence anchor actually supports the coded scope and denominator statement. | Narrative spotlight use of these null cases; stronger denominator-validity claims |
| H3 | Formal release/submission sign-off | A human must decide the release version/date, confirm the working tree is clean after commit, and authorize tag/DOI publication. | `--strict-repro`, tagged release, archival DOI, camera-ready artifact package |

## H1: Independent-Human IRR Pass

Required action:

1. Select an independent coder who did not produce the gold labels or the
   agent-assisted recode.
2. Give the coder only the H1 packet generated at
   `site/h1_irr_packet/` (or an equivalent folder containing only blank
   worksheets, rubric, methodology, and sample metadata), not the full
   dashboard/site bundle, raw event YAML, rendered event pages, existing coded
   answers, kappa reports, LLM rationale, or null-case pre-audit notes.
3. Recode at least the variables that support paper-facing claims:
   `coverage_status`, `observation_kind`, and `attribution`.
4. Recompute κ with `make irr-kappa`.
5. Update `analysis/inter_rater/kappa_report.json` so
   `coder_provenance.mode` is `independent_human` only if the pass was truly
   independent and blinded.

Acceptance criteria:

- `coverage_status` κ is present and `>= 0.6`.
- `observation_kind` and `attribution` are either `>= 0.6` or the related
  paper claims remain explicitly parked/descriptive.
- `python3 scripts/check_paper_readiness.py --strict-reliability` no longer
  fails on coder provenance.

Do not do:

- Do not relabel the current LLM-assisted recode as `independent_human`.
- Do not use the same author/agent rationale as a second coder.

## H2: Null-Case Denominator Audit

Audit these 13 `null_case` events before using them as named narrative
examples or stronger denominator evidence:

| Event ID | Required human check |
| --- | --- |
| `iran-ransomware-ofac-2018` | Confirm the `observed_no_change` anchor supports the coded scope and no-change window. |
| `irgc-ransomware-ofac-2022` | Confirm the `observed_no_change` anchor supports the coded scope and no-change window. |
| `lazarus-entity-ofac-2019` | Confirm the `observed_no_change` anchor supports the coded scope and no-change window. |
| `lazarus-laundering-ofac-2020` | Confirm the `observed_no_change` anchor supports the coded scope and no-change window. |
| `lockbit-leader-ofac-2024` | Confirm the `observed_no_change` anchor supports the coded scope and no-change window. |
| `matveev-ofac-2023` | Confirm the `observed_no_change` anchor supports the coded scope and no-change window. |
| `pertsev-nl-arrest-2022` | Confirm the `observed_no_change` anchor supports the coded scope and no-change window. |
| `russian-cybercrime-infra-ofac-2025` | Confirm the `observed_no_change` anchor supports the coded scope and no-change window. |
| `sec-v-uniswap-wells-notice-2024` | High priority. LLM-Expert-Audit flagged this as methods `fail_pre_audit`: current anchors do not replay `app.uniswap.org` operational uptime across the full coded window. Upgrade direct frontend continuity evidence or re-scope before aggregate/null-rate use. |
| `sichuan-silence-ofac-2024` | Confirm the `observed_no_change` anchor supports the coded scope and no-change window. |
| `sinbad-ofac-2023` | Confirm the `observed_no_change` anchor supports the coded scope and no-change window. |
| `storm-semenov-doj-2023` | Confirm the `observed_no_change` anchor supports the coded scope and no-change window. |
| `zservers-ofac-2025` | Confirm the `observed_no_change` anchor supports the coded scope and no-change window. |

Per-event audit procedure:

1. Maintainer pre-flight: run
   `python3 scripts/validate.py --check-archives events/<event-id>.yaml`
   before distributing the static packet. Static H2 auditors are not expected
   to run repository commands unless they receive a full checkout/container.
2. Open the event YAML and its rendered evidence chain under
   `analysis/evidence-chains/<event-id>.md`.
3. Inspect the local artifact referenced by `body_hash` + `body_path`,
   `query_hash`, or `measurement_ids`.
4. Verify that the artifact supports the coded no-change claim, denominator
   scope, and time window. A `scope_descriptor` can define the scope but does
   not count as a replayable evidence anchor by itself.
5. If clean, set `last_human_audit: YYYY-MM-DD` in the event YAML.
6. If not clean, downgrade/re-scope the observation or move the case out of
   narrative use before stamping `last_human_audit`.

Acceptance criteria:

- Every listed event has a truthful `last_human_audit` date.
- `make validate` and `make paper-check` still pass.
- The warning about 13 null denominator cases lacking `last_human_audit`
  disappears or is reduced to only unaudited remaining cases.

## H3: Release/Submission Sign-Off

Required action:

1. Decide whether the next public artifact is a working paper snapshot,
   submission artifact, or tagged dataset release.
2. If releasing, update `CITATION.cff::version` and
   `CITATION.cff::date-released` so the release date is on or after
   `dataset.meta.json::cutoff_date` (`2026-05-06` for the current snapshot).
3. Run `make regenerate` from a clean, intended source tree.
4. Review `git status --short` and commit the intended release surface.
5. Run the strict gate:

```sh
python3 scripts/check_paper_readiness.py --strict-audit --strict-null-audit --strict-repro --strict-reliability
```

Acceptance criteria:

- No dirty-source-tree strict repro error.
- `CITATION.cff::date-released` no longer predates the dataset cutoff.
- Strict reliability passes, or the paper explicitly removes independent-IRR
  claims and the submission package is marked as a working snapshot rather
  than final release.

## Non-Blockers For Working Snapshot

The following warnings are acceptable for the current non-release working
snapshot, but not for a strict release/submission package:

- `dataset.meta.json` generated from a dirty source-input tree.
- `CITATION.cff date-released=2026-04-23` predating cutoff `2026-05-06`.
- `IRR coder_provenance.mode='llm_assisted_blinded'`.
- Null-case `last_human_audit` missing when the cases are used only in
  aggregate/null tables and not as narrative spotlight examples.
