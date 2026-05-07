# Submission/Reproducibility LLM Expert Pre-Audit

Snapshot date: 2026-05-07.

This is a read-only LLM expert audit of submission/release provenance. It is not a release sign-off and not a human audit.

## Recommended Artifact Split

| Artifact area | Contents | Provenance rule |
| --- | --- | --- |
| `analysis/llm_expert_audit/` | LLM expert prompts/results, scope, and limitations | Internal pre-audit only |
| `Human-Expert-Audit` package | Blinded worksheets, rubric, coder declaration, recode CSVs, κ output, sign-off memo | Create only after a real independent human pass |
| Reproducibility package | Release tag, DOI, `dataset.meta.json`, `sources/source_manifest.*`, paper tables, exact commands, strict-gate output | Only after clean release tree |
| Claims package | `docs/paper_claims.md`, trigger registry, coverage matrix, limitations, generated tables | Cite with denominator-aware language |

Human IRR independence rule: do not include this LLM report in the blinded human coder packet if the goal is independent-human reliability.

## Allowed Wording Before Human-Expert-Audit

Use:

> κ is reported as a self-consistency check from a single-coder LLM-assisted blinded recode, not as independent-human inter-rater reliability.

Do not use before a real human pass:

- "human-audited"
- "independent human reliability"
- "inter-rater reliability" without the LLM-assisted caveat
- "expert human validation"
- "almost perfect inter-rater agreement" without provenance qualification

## Current Strict-Gate Result

Command:

```sh
python3 scripts/check_paper_readiness.py --strict-audit --strict-repro --strict-reliability
```

Current hard blockers:

| Blocker | Meaning | Resolution |
| --- | --- | --- |
| `CITATION.cff date-released=2026-04-23` predates cutoff `2026-05-06` | Release metadata describes an older snapshot | Update on release/submission cut |
| Dirty source-input tree | Working snapshot was generated before a clean committed release surface | Commit intended surface and regenerate |
| `coder_provenance.mode='llm_assisted_blinded'` | Current κ is self-consistency, not independent-human reliability | Run real blinded human recode and recompute κ |

Current warning for null cases:

- 13 null denominator cases lack `last_human_audit`; aggregate/null tables are acceptable with warnings, but named narrative spotlight use is blocked.

## Paper Citation Guidance

Safe to cite with current provenance:

- Generated paper tables as descriptive artifacts.
- Trigger registry and sampling frame.
- Coverage matrix and denominator-reason fields.
- Source manifest and local artifact hashes.
- κ only as LLM-assisted self-consistency.

Not safe to cite before Human-Expert-Audit:

- Current κ as independent-human IRR.
- Unaudited null cases as named narrative examples.
- Off-ramp CEX null cases as proof that no private exchange action occurred.
- `asset_onchain` as a rate.
- L0/L3 zero denominators as zero reactions.
- C2/C5-style central claims that require independent-human `observation_kind` reliability.

