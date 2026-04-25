# P1 Documentation

Reference documentation for the Cross-Layer Censorship Event Study Database. Already-landed changes are recorded in [`../CHANGELOG.md`](../CHANGELOG.md). Portfolio-level planning (roadmap, priorities, decisions) lives in [`../../docs/3-TODOs.md`](../../docs/3-TODOs.md).

## Start here

| If you want to… | Read |
| --- | --- |
| Understand what this project is and why | [`../README.md`](../README.md) |
| See a real event end-to-end before reading rules | [`example-tornado-cash-2022.md`](example-tornado-cash-2022.md) |
| See the Gebru-style datasheet (motivation / composition / use) | [`datasheet.md`](datasheet.md) |

## Paper-facing surface

| Topic | Doc |
| --- | --- |
| Single source of truth for what the paper argues (claims C1–C6, phrasing locks, claim-to-table-source matrix, sampling frame, prior-art delta, IRR κ-floor language) | [`paper_claims.md`](paper_claims.md) |
| Inter-rater reliability protocol — runnable via `make irr-sample` / `make irr-kappa`; report at `analysis/inter_rater/kappa_report.md` | (script-only; see [`paper_claims.md §0`](paper_claims.md) "κ-floor language") |
| One-command Zenodo artifact-eval reproduction (Docker + `SOURCE_DATE_EPOCH`) | top-level [`Dockerfile`](../Dockerfile) + [`docs/releasing.md`](releasing.md) |
| What the dataset cannot say (predictive use, prevalence claims, compliance scoring) | [`limitations-and-use.md`](limitations-and-use.md) |
| Citation formats + Zenodo DOI integration | [`citing.md`](citing.md), [`releasing.md`](releasing.md) |

## Methodology reference

| Topic | Doc |
| --- | --- |
| What counts as an event, how it is reconstructed and verified | [`methodology.md`](methodology.md) |
| URLs and endpoints for every external data source | [`data-sources.md`](data-sources.md) |
| Coverage gaps on chains that don't appear in the corpus | [`chain-coverage-note.md`](chain-coverage-note.md) |
| 5-dimension readiness rubric used by `review_report.py` | [`case-review-rubric.md`](case-review-rubric.md) |
| Quarterly adversarial-audit commitment | [`audit-protocol.md`](audit-protocol.md) |

## Schema

| Topic | Doc |
| --- | --- |
| Stack-features schema (per-event structural feature vector) | [`stack-features-schema.md`](stack-features-schema.md) |
| Evaluation-profile schema (how a per-event profile is reported) | [`evaluation-profile-schema.md`](evaluation-profile-schema.md) |
| Decision rubric — comparative, not predictive | [`decision-rubric.md`](decision-rubric.md) |

## Operating the pipeline

| Role | Doc |
| --- | --- |
| Maintainer daily QA loop and promotion gate | [`process-checklist.md`](process-checklist.md) |
| External contributor proposing a new event | [`contributor-guide.md`](contributor-guide.md) |

## Navigation principles

- **Concepts / rules**: `methodology.md` owns. Everything else cross-references it.
- **Paper claims**: `paper_claims.md` owns. Each numerical claim is locked to a specific paper-table artifact under `analysis/paper_tables/`.
- **Actionable steps / checklists**: `process-checklist.md` owns. Reference doc, not a tutorial.
- **One worked example, not many**: `example-tornado-cash-2022.md`. Adding more examples dilutes the anchor.
- **No changelog-style narrative inside reference docs**: landed work → `../CHANGELOG.md`; forward-looking planning → `../../docs/3-TODOs.md`.
