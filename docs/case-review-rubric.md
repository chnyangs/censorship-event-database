# Case Review Rubric

This rubric answers a narrower question than the methodology:

Is this *specific case design* reliable and complete enough for the current
release goal?

## 1. Reliability

Score each case on these dimensions:

### Trigger reliability

- `High`: primary legal or primary corporate trigger with precise target
- `Medium`: trigger is primary but timing or target scope is still coarse
- `Low`: trigger is real but the relevant target set is still under-specified

### Observation reliability

- `High`: retained observations are evidence-backed and non-speculative
- `Medium`: one or more layers still depend on semi-primary inference or current-state captures without a stronger archival anchor
- `Low`: observations are carrying more interpretation than evidence

### Attribution reliability

- `High`: the retained changed layers can be tied directly to the trigger
- `Medium`: plausible timing match but incomplete operator-side confirmation
- `Low`: correlation dominates and attribution remains weak

## 2. Completeness

Evaluate separately from reliability.

### Coverage completeness

- `High`: every relevant layer is either measured or explicitly ruled out
- `Medium`: some layers are only partially measured
- `Low`: multiple layers are effectively unknown

### Case-shape completeness

- `High`: the current file already captures the case's main empirical shape
- `Medium`: the main shape is visible but one important layer is still open
- `Low`: the file captures only the trigger and one obvious downstream effect

## 3. Operationalization in this repo

`scripts/review_report.py` turns this rubric into a heuristic QA artifact.

Interpret it as an aid, not a substitute for reading the case:

- `trigger_reliability` follows whether the trigger is primary and the target is concrete.
- `observation_reliability` drops when retained observations still carry gap markers or weak evidence scaffolding.
- `attribution_reliability` drops when retained changed layers are mostly plausible rather than direct; for `null_event` / `null_case` rows, scoped `observed_no_change` evidence is evaluated without requiring changed-layer attribution.
- `coverage_completeness` is driven by how many layers remain `not_measured`.
- `case_shape_completeness` asks whether the file already contains a stable empirical shape.
- `overall_readiness` should be read with scope in mind: a case can be ready for a narrow release claim without being complete across all six layers.

## 4. Admission guidance

### Safe to admit now

When:

- the core empirical claim survives even if no more sources are added
- remaining gaps are peripheral, not central

### Keep as draft

When:

- the event's main claim depends on unresolved evidence
- or the event class could change after more collection

## 5. Current practical rule

For this repo, a case is a good admission candidate if:

- it has zero gap markers in `scripts/draft_gap_report.py`
- its strongest claim can be stated in one sentence without caveats like
  "likely", "possible", or "still needs"
- removing all weak layers would still leave a useful event
- `scripts/review_report.py` does not flag `observation_reliability` or
  `attribution_reliability` as `low`
- if it is admitted with only partial coverage, the event file itself states the scoped release claim in plain language
- if a case relies on live-web current-state evidence, that evidence should be backed by a local capture bundle under `sources/http_captures/`
