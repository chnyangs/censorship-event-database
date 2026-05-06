# Adversarial Audit Protocol

Quarterly discipline that keeps the dataset from quietly drifting. Without this slot, agent-assisted admissions and rubber-stamp reviews compound silently over 6-12 months until the dataset is no longer defensible.

## 1. Cadence

- One audit per calendar quarter. Frequency is fixed; quantity scales.
- Performed by the editor-in-chief. If the dataset ever has more than one maintainer, the audit rotates — the author of an event does not audit it.

## 2. Audit sample

Pick **five** admitted events from the most recent quarter. Selection bias:

1. Prefer events with `admitted_scope_blocked`, then `release_ready_scoped`, over `release_ready_complete`.
2. Prefer events where any score in [`review_report.py`](../scripts/review_report.py) is `medium`.
3. Prefer events whose `origin` is `agent_draft → human_reviewed` over `human_authored`.
4. Include at least one event where `attribution: direct` appears on any changed layer.

If fewer than 5 new events were admitted in the quarter, audit all of them.

## 3. Review stance

The audit is **adversarial**. Default assumption: the admission is wrong somehow. Specifically, try to find a reason to roll back, re-classify, or downgrade each case.

Concrete checks to run against each sampled event:

1. **Body-hash drift** — run `python3 scripts/validate.py events/<slug>.yaml --check-archives`. Any error is a failed audit for that case.
2. **Wayback rot** — same flag, covers `wayback` URLs. A Wayback failure is blocking only when Wayback is the source's sole archive anchor. If the source also has a valid local `body_hash` + `body_path`, the validator emits a warning because the replay path still exists.
3. **Attribution re-read** — for every `attribution: direct`, find the primary source backing it and read the exact passage. If the passage does not explicitly name the target or the order, downgrade to `plausible`.
4. **Evidence independence** — inspect semi-primary sources for hidden sharing. If two mirrors of the same repo or two archives of the same URL are counted as independent, assign an `evidence_group_id` to collapse them.
5. **Scope-vs-claim** — re-read `analysis_notes` and compare to `coverage[]`. If notes claim effects on layers that are `not_measured`, remove or rewrite.
6. **Target enumeration** — if `target.enumeration: complete`, verify the list matches the original primary source (e.g. SDN XML). If not, downgrade to `subset`.

## 4. Outcomes

For each event the audit produces one of:

| Outcome | Meaning | Action |
| --- | --- | --- |
| `clean` | All checks pass, no changes | Bump `last_human_audit` to today's date |
| `re_scoped` | A claim is narrowed (attribution downgraded, enumeration narrowed, observation dropped) | Apply the narrowing; `last_human_audit` bumps |
| `rolled_back` | Admission withdrawn; status reverts to `draft` or `rejected` | Record in CHANGELOG with specific reason |
| `escalated` | Issue affects multiple events or reveals a methodology gap | File in `../CHANGELOG.md` under an "audit escalation" entry; may block further admissions until resolved |

## 5. CHANGELOG entry template

After the audit concludes, add to [`../CHANGELOG.md`](../CHANGELOG.md):

```text
- YYYY-QN adversarial audit: N reviewed, N clean, N re_scoped, N rolled_back, N escalated.
  Sample: <slug>, <slug>, <slug>, <slug>, <slug>.
  Notable outcomes: <one-line per non-clean outcome with linking slug>.
```

## 6. Tooling checklist

The audit relies on these scripts and artifacts:

- `scripts/validate.py --check-archives` — body-hash recompute + wayback HEAD-check
- `scripts/review_report.py` — current readiness signal per case
- `scripts/draft_gap_report.py` — surfaces residual placeholder / gap text
- `analysis/review-report.md` + `analysis/pilot-status.md` — human-readable summaries

## 7. When this protocol is allowed to slip

Never in the first year after the paper is submitted. After that, if all of the following hold:

- The dataset has not received any new admission in a full quarter, AND
- `scripts/validate.py --check-archives` still passes against every admitted event, AND
- The maintainer explicitly records in the CHANGELOG that the audit slot is skipped for that quarter and why.

Even then: skip at most one consecutive quarter. Two skipped quarters without explanation is the trigger to flag the project as `maintenance_paused` (see `docs/3-TODOs.md` Observatory section).
