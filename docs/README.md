# P1 Documentation

Reference documentation for the Cross-Layer Censorship Event Study Database. Already-landed changes are recorded in [`../CHANGELOG.md`](../CHANGELOG.md). Portfolio-level planning (roadmap, priorities, decisions) lives in [`../../docs/3-TODOs.md`](../../docs/3-TODOs.md).

## Start here

| If you want to… | Read |
| --- | --- |
| Understand what this project is and why | [`../README.md`](../README.md) |
| See a real event end-to-end before reading rules | [`example-tornado-cash-2022.md`](example-tornado-cash-2022.md) |

## Reference (the authoritative docs)

| Topic | Doc |
| --- | --- |
| What counts as an event, how it is reconstructed and verified | [`methodology.md`](methodology.md) |
| URLs and endpoints for every external data source | [`data-sources.md`](data-sources.md) |
| 5-dimension readiness rubric used by `review_report.py` | [`case-review-rubric.md`](case-review-rubric.md) |

## Operating the pipeline

| Role | Doc |
| --- | --- |
| Maintainer daily QA loop and promotion gate | [`process-checklist.md`](process-checklist.md) |
| External contributor proposing a new event | [`contributor-guide.md`](contributor-guide.md) |

## Navigation principles

- **Concepts / rules**: `methodology.md` owns. Everything else cross-references it.
- **Actionable steps / checklists**: `process-checklist.md` owns. Reference doc, not a tutorial.
- **One worked example, not many**: `example-tornado-cash-2022.md`. Adding more examples dilutes the anchor.
- **No changelog-style narrative inside reference docs**: landed work → `../CHANGELOG.md`; forward-looking planning → `../../docs/3-TODOs.md`.
