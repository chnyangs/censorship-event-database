# LLM-Expert-Audit

Snapshot date: 2026-05-07.

This directory records a multi-expert LLM pre-audit. It is intentionally
separate from `Human-Expert-Audit`: the findings below can narrow and prepare
the human review, but they do not create `last_human_audit`, do not satisfy
`independent_human` IRR provenance, and must not be cited as human validation.

## Expert Roles

| Expert | Scope | Output |
| --- | --- | --- |
| LLM Expert 1 | Denominator/methods audit of the 13 null cases | [`null_case_pre_audit.md`](null_case_pre_audit.md) |
| LLM Expert 2 | Evidence-anchor/provenance audit of the same 13 cases | [`null_case_pre_audit.md`](null_case_pre_audit.md) |
| LLM Expert 3 | Submission/reproducibility and provenance-boundary audit | [`submission_repro_pre_audit.md`](submission_repro_pre_audit.md) |

## Combined Workflow

The two audit classes should be combined as a two-stage protocol:

| Stage | Who/what | Purpose | May stamp human provenance? |
| --- | --- | --- | --- |
| LLM-Expert-Audit | Multiple LLM expert roles | Find methodological, evidence, and submission risks before human review. | No |
| Human-Expert-Audit | Independent human reviewer/coder | Confirm semantic evidence sufficiency, denominator scope, and blinded IRR labels. | Yes, if truly independent |

Operational boundary:

- LLM outputs can be cited as internal pre-audit artifacts.
- LLM outputs can identify cases that should be downgraded, re-scoped, or sent to human attention.
- LLM outputs must not be used to set `last_human_audit`.
- LLM outputs must not be used to change `coder_provenance.mode` to `independent_human`.
- Human reviewers should receive the rubric and blinded worksheets, not this LLM report, when the goal is independent IRR.

## Headline Findings

- All 13 null-case YAML files pass local validator/archive-hash checks.
- All 13 relevant no-change observations have at least one local `body_hash` + `body_path` replay anchor.
- Most off-ramp CEX null cases are semantically weak as exchange-action denominators: the replayable anchor proves the legal trigger and defines a public-disclosure search scope, but does not replay a systematic absence search across exchange statements.
- `sec-v-uniswap-wells-notice-2024` is the highest-risk null case: the current anchors support disclosure/absence-of-SEC-complaint context, but not a replayed `app.uniswap.org` operational-uptime measurement across the full 2024-04-10 to 2025-02-25 window.
- Strict release/submission mode still fails on release metadata, dirty source tree, and missing independent-human reliability provenance.

Recommended paper posture before Human-Expert-Audit:

- Null cases can support aggregate descriptive tables only with explicit "public-evidence null" language.
- Do not use unaudited null cases as narrative spotlight examples.
- Do not claim that off-ramp CEX null cases prove no private exchange action.
- Do not cite current κ as independent-human IRR.

