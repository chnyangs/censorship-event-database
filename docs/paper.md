# Paper Surface

This tracked file is the public manuscript wrapper for the current working
paper surface. It is intentionally not a submission-formatted paper draft.
The claim lock in [`paper_claims.md`](paper_claims.md), the generated tables in
[`../analysis/paper_tables/`](../analysis/paper_tables/), and the release gates
in [`a-class-submission-readiness.md`](a-class-submission-readiness.md) control
what the paper may say.

If a private LaTeX or Overleaf working copy exists outside the public artifact
set, it is downstream of this repository's claim lock. A disagreement between
private manuscript prose and `paper_claims.md` is resolved in favor of the
claim lock.

## Current Snapshot

Use [`../dataset.meta.json`](../dataset.meta.json) and
[`../analysis/paper_tables/table1_case_roles.md`](../analysis/paper_tables/table1_case_roles.md)
for live corpus counts. Do not hand-copy admitted-event, total-event, or
cutoff numbers into this wrapper.

## Required Claim Sources

- Sampling frame and limitations: [`paper_claims.md`](paper_claims.md),
  [`limitations-and-use.md`](limitations-and-use.md), and
  [`datasheet.md`](datasheet.md).
- Layer observability and denominator language:
  [`../analysis/paper_tables/table2_layer_observability.md`](../analysis/paper_tables/table2_layer_observability.md)
  plus [`../derived/admission_sensitivity.md`](../derived/admission_sensitivity.md).
- Latency and trigger precision:
  [`../analysis/paper_tables/table4_latency_by_precision.md`](../analysis/paper_tables/table4_latency_by_precision.md).
- Null-denominator interpretation:
  [`../analysis/paper_tables/table6_null_denominator.md`](../analysis/paper_tables/table6_null_denominator.md).

## Release Blockers

This remains a working snapshot until the release checklist clears the
independent-human reliability, evidence-tier IRR, null-case audit, and
submission sign-off gates. The wrapper exists so the public repository keeps a
stable paper-facing entry point while the formatted manuscript evolves.
