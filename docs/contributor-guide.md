# Contributor Guide

External contributions are accepted only when they preserve the dataset's provenance discipline. If you are the maintainer, read [process-checklist.md](process-checklist.md) instead — this file only covers what is different for an outside contributor.

## Before you start

Familiarize yourself with:

1. [methodology.md](methodology.md) — what counts as an admissible event and why.
2. [process-checklist.md](process-checklist.md) — the operational checklist and QA loop.
3. [data-sources.md](data-sources.md) — where to get primary sources.
4. [example-tornado-cash-2022.md](example-tornado-cash-2022.md) — a worked walkthrough of a real event.

## Minimum submission package

One new event = one PR containing:

- `candidate_triggers/YYYY-MM-DD-<slug>.yaml` — first-stage trigger stub.
  New cases should enter the registry before becoming event YAML.
- `events/<slug>.yaml` — start from `templates/event.yaml` or run `python3 scripts/new_event.py <slug>`.
- Any archived artifacts your event depends on: Wayback snapshot references, on-chain receipt JSON under `sources/onchain_receipts/<slug>/`, local HTTP captures under `sources/http_captures/<slug>/` for live-web evidence, SDN XML diff under `sources/ofac_sdn_diffs/` if your trigger is a sanctions action.
- A one-line `CHANGELOG.md` entry describing the contribution.

The `<slug>` must be kebab-case (enforced by validator).

## What qualifies as a valid event

Admission rules are defined authoritatively in [methodology §5](methodology.md). In short:

- Non-`asset_onchain` observations require one primary source or two independent semi-primary sources.
- `supporting_*` sources corroborate but cannot satisfy admission on their own.
- `observed_no_change` is valid only when coverage is `measured` or `partially_measured`, with an explicit `scope_descriptor` or equivalent.
- Every layer must have an explicit `coverage[]` entry — including `not_applicable` and `not_measured`.
- `observation_kind` and `attribution` must both be set; they are not aliases (see [methodology §2.5](methodology.md)).

## Submission QA

Run the QA loop from [process-checklist.md §3](process-checklist.md) against your event before opening the PR. A submission with validator errors will not be reviewed.

Run `make trigger-registry` after adding the candidate stub or event. The
registry must show the case's current status and source file.

If you use current-state live-web evidence, capture a local bundle first (see process-checklist §2 step 5). PRs that rely on live URLs without a preserved bundle will be asked to add one.

## Review

Reviewers apply the [case-review-rubric](case-review-rubric.md) and the promotion gate in [process-checklist §4](process-checklist.md). Two reviewers must sign off before `status: admitted` is set.

Reviewers may:

- Ask you to strengthen a weak layer.
- Ask you to drop a weak layer from `observations[]` and express it in `coverage` only.
- Ask to re-scope the `event_class` (e.g. cascade → comparison) if the retained shape does not meet its class criteria.

## Style

- Kebab-case event ids.
- ISO-8601 UTC timestamps.
- Notes over silent assumptions; describe what was seen, not what is expected.
- Placeholder text is only allowed in `status: draft`; promote only after placeholders are resolved.
