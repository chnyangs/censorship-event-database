# A-Class Submission Gap Report

Status as of 2026-05-07 after running the working-snapshot paper gate.

This report is the current execution view for the A-class submission track in
[`docs/a-class-submission-readiness.md`](../docs/a-class-submission-readiness.md).
It distinguishes machine-complete work from items that require human judgment
or corpus expansion.

## Machine Gate Baseline

Latest working-snapshot command:

```sh
make paper-check
```

Result: passed with warnings.

Remaining warnings:

| warning | submission impact | owner |
| --- | --- | --- |
| `CITATION.cff date-released=2026-04-23` predates cutoff `2026-05-06` | strict release/submission gate fails until a human release version/date is chosen | release sign-off |
| `dataset.meta.json` generated from a dirty source-input tree | expected during local edits; strict repro passes only after commit / clean checkout regeneration | release sign-off |
| 13 null denominator cases lack `last_human_audit` | null cases may stay in aggregate tables, but cannot be narrative spotlight or stronger denominator proof | Human-Expert-Audit |
| IRR provenance is `llm_assisted_blinded` | kappa can be cited only as self-consistency, not independent reliability | independent human coder |

## A-Class Readiness Matrix

| area | current status | A-class target | next action |
| --- | --- | --- | --- |
| Claim framing | strong; `paper_claims.md` now uses A-class submission-lock status | every claim tied to table, denominator, role, and audit gate | keep paper prose synchronized with `paper_claims.md` |
| L0/L3 denominators | sufficient for "observability gap" claim | appendix cited next to primary result | cite `docs/l0-l3-denominator-appendix.md` in the paper's Results section |
| Human IRR | not complete; LLM-assisted only | independent-human provenance for cited reliability claims | run blinded human recode and `make irr-kappa` |
| Null denominator audit | not complete; 13 cases listed | audited or excluded from stronger claims | complete `human-audit.md` H2 |
| Anchor cases | 2 anchors, 7 release-ready scoped cases | at least 6 audited anchors; 20+ release-ready scoped | promote queue in `docs/a-class-submission-readiness.md` Phase A3 |
| Sampling frame | transparent but under target | 70-90 admitted minimum; 150-250 frame units preferred | add S2/S3/S4/S6 backlog before expanding claims |
| Artifact package | working-snapshot gates pass | strict gate from clean committed tree | after human work, run strict gate and tag release |
| Dashboard | refactored static artifact map | dashboard exposes paper/audit/readiness surfaces | regenerate site after each release-bound change |

## Do-Now Queue

1. Complete independent-human IRR.
2. Human-audit the 13 null denominator cases, with priority on
   `sec-v-uniswap-wells-notice-2024`.
3. Promote at least four more anchors from the Phase A3 queue.
4. Add non-OFAC sampling backlog in S2/S3/S4/S6 before making any stronger
   external-validity claim.
5. After human work lands, choose release version/date, commit the intended
   source tree, then run:

```sh
make regenerate
make check
make render-site
python3 scripts/check_paper_readiness.py --strict-audit --strict-repro --strict-reliability
```

## Current Submission Judgment

The current working snapshot is suitable for internal paper drafting and
artifact review. It is not yet a strict A-class submission package because
human reliability, null-case human audit, and release sign-off are still open.

If the human items pass and the paper keeps the current denominator-aware
framing, the project is a plausible A-class measurement/data-paper submission.
If the paper overclaims population prevalence, L0/L3 rates, or independent IRR,
the same artifact surface becomes high-risk.

