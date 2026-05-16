# Candidate-trigger retirement policy

> Addresses Agent C (M4) from the 2026-05-16 temporal-ledger review:
> stubs in this directory were untracked until 2026-05-16, so stub
> age was invisible to git. This policy makes stub aging explicit and
> defines a retirement path so stubs do not accumulate indefinitely.

## Lifecycle

A candidate trigger moves through these states:

| state | location | how it gets here |
| --- | --- | --- |
| `candidate` | `candidate_triggers/<slug>.yaml` with `registry_status: candidate` | watcher / human / agent draft |
| `promoted_to_event` | same file, `registry_status: promoted_to_event`; corresponding `events/<slug>.yaml` exists | human promotes the stub via the §4 admission procedure |
| `screened_out` | `candidate_triggers/rejected/<slug>.yaml` | human (or agent + human-confirm) decides the case is out of frame |
| `retired_stale` | `candidate_triggers/rejected/<slug>.yaml` with `registry_status: retired_stale` | this policy fires (see below) |

`promoted_to_event` and `screened_out` are explicit human decisions
with their rationale recorded. `retired_stale` is the time-based
fallback for stubs that nobody ever decided.

## Age thresholds

Stub age is measured from the file's first git-tracked commit
(use `git log --diff-filter=A --follow -- <path>` for the
introduction date). The retirement clock starts there.

| stub age | required action |
| --- | --- |
| 0–60 days | normal pipeline; no action required |
| 61–180 days | quarterly maintainer review touches the stub: either advance state or add a `triage_notes:` paragraph explaining why it's still pending |
| 181–365 days | flag for retirement decision in the next maintainer review; if not advanced within 30 days of the flag, retire |
| > 365 days | **retire automatically** to `rejected/` with `registry_status: retired_stale` and a `retired_reason: aged_out` field; this is a soft tombstone, not a re-screening |

A retired stub can always be re-promoted by moving it back to
`candidate_triggers/` and resetting `registry_status: candidate` —
retirement is a triage default, not a permanent decision.

## What retirement does NOT mean

- It does not assert that the event is out of scope.
- It does not assert that the underlying censorship event didn't happen.
- It does not block a future admission of the same event under a refined codebook.

A retired stub is "nobody had the bandwidth to promote this within
a year" — the corpus signal is about maintainer capacity, not about
the event itself.

## Operational checks

- **Quarterly**: maintainer runs `git log --diff-filter=A
  --follow -- candidate_triggers/*.yaml` and reviews any stub
  > 60 days old.
- **Pre-release**: maintainer confirms no `candidate` stubs are
  > 365 days old; any that are get retired before the tag.
- **Release notes**: the `analysis/release_signoff/<version>.md`
  log records a count of `candidate` / `promoted_to_event` /
  `screened_out` / `retired_stale` for that release snapshot.

## Initial state (2026-05-16)

All 31 stubs currently under `candidate_triggers/` were committed
together at first git-tracked commit on 2026-05-16. Under this
policy:

- The retirement clock starts 2026-05-16 for all 31 stubs.
- First quarterly review due 2026-08-16.
- First retirement-eligibility check due 2027-05-16.

This start-date convention prevents an artificial "all stubs are
zero days old" reading after the initial commit; the maintainer
knows the underlying drafts predate 2026-05-16, but the git-tracked
clock is reset at this commit so future ages are honest.

## Cross-references

- Promotion procedure: [`docs/process-checklist.md §4`](../docs/process-checklist.md)
- Admission rules: [`docs/methodology.md §3`](../docs/methodology.md)
- Screened-out rationale convention: see `candidate_triggers/rejected/`
  for examples (each rejected file carries a `triage_notes:`
  block explaining the decision).
- Stub-aging review surface: this policy + Agent C's pipeline-state
  review at [`analysis/temporal_ledger/review_c_pipeline_state.md`](../analysis/temporal_ledger/review_c_pipeline_state.md).
