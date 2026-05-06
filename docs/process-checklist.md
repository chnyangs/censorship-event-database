# Process Checklist

Actionable checklist form of the [methodology](methodology.md). The rationale and definitions live there; this file is the short operational companion you read when actually running the pipeline.

## 1. Lifecycle state transitions

See [methodology §3](methodology.md) for full criteria. Quick reference:

| State | Enter when | Exit when |
| --- | --- | --- |
| `draft` | any trigger source placeholder, missing admission-grade evidence, or incomplete coverage | evidence upgraded, or case re-scoped to `rejected` |
| `observation_active` | trigger is primary and archived; target is concrete; reviewer accepted | stabilization reached, or 12-month hard cap |
| `observation_closed` | window closed and all touched layers stable (or hard cap hit) | promoted to `admitted`, sent back to `draft`, or marked `rejected` |
| `admitted` | release-grade: no placeholders, no `coverage_gap` observations, source rule satisfied, coverage explicit for all layers, ≥ 1 `observed_change`, validator passes | normally terminal; retracted only under the correction protocol ([methodology §8.5](methodology.md)) |
| `rejected` | trigger real but target ambiguous, attribution undefensible, or evidence too weak | terminal |

## 2. Event construction — step-by-step

1. Create stub from `templates/event.yaml` or `python3 scripts/new_event.py <slug>`.
2. Fill `trigger`, `target`, `jurisdiction`.
3. Fill `coverage[]` for **all six layers** before adding any interpretive claim. Speculative work stays in coverage notes, not in observations.
4. Add only `observations[]` entries that are already evidence-backed per [methodology §5](methodology.md).
5. For any current-state web evidence, capture a local bundle: `python3 scripts/capture_http_artifact.py --output-dir sources/http_captures/<slug>/... <url...>`.
6. QA loop (§3 below).

## 3. QA command sequence

Run in this order. Each is idempotent.

```sh
make validate EVENTS=events/<slug>.yaml
make verify-citations EVENTS=events/<slug>.yaml  # when network is available
make draft-gaps
make status
make review
```

Interpret `review_report.py` output conservatively:

- `release_ready_complete` — publishable and broadly complete at intended scope.
- `release_ready_scoped` — publishable but only with an explicitly narrow claim.
- `admitted_scope_blocked` — admitted to the corpus, but not release-publishable until listed blockers are resolved.
- `candidate_for_admission` — no low scores, no gap markers, but still `draft`.
- `working_draft` — empirical shape visible, core artifacts or attributions missing.
- `needs_re_scoping` — current file cannot represent a stable case shape.

Automation does not replace reviewer judgment. Treat the scoring as a forcing function, not a verdict.

## 4. Promotion gate for `admitted`

Every item must be true at the moment of promotion:

1. All URLs and artifact references are concrete.
2. No note contains `placeholder`, `replace`, `need`, `still needs`, or similar TODO language.
3. Every `observed_change` has admission-grade sources ([methodology §5](methodology.md)).
4. Any layer without enough evidence is expressed as `coverage` only, not as a weak observation.
5. `analysis_notes` describes the event actually present in the file, not the intended future version.
6. `review_report.py` does not rate `observation_reliability` or `attribution_reliability` as `low`.
7. If `release_ready_scoped`, `analysis_notes` states the narrow empirical claim in plain language.
8. Any current-state web claim relied on for admission has a local capture bundle or equivalent archival artifact.
9. If `review_report.py` returns `admitted_scope_blocked`, do not publish the case as release-ready; use it only in repair queues or explicitly marked appendices until blockers clear.

## 5. Release posture

- In-repo: mix of `admitted` and `draft` is fine.
- Release artifacts: `admitted` only by default, excluding `admitted_scope_blocked` unless the release explicitly marks them as blocked/non-claim rows.
- Paper inclusion: state the inclusion rule explicitly (e.g. "cascade_event only, primary-onchain corroboration required").

## 6. Adversarial quarterly audit

Once the agent-assisted infrastructure is active (scripts/watchers/ + agent_draft_event.py + staleness_report.py are committed; cron scheduling is a separate deployment step), every quarter:

1. Pick 5 admitted events from the most recent quarter, biased toward `admitted_scope_blocked` and `release_ready_scoped`.
2. Try to find reasons to roll back, re-classify, or downgrade attribution.
3. Record the outcome in `CHANGELOG.md` as `YYYY-QN audit: N reviewed, N rolled back, N re-scoped, N escalated`.

The audit is not a review in disguise — it is deliberately adversarial. Without this slot, agent-assisted admissions drift quietly.
