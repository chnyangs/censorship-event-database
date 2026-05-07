# analysis/

Downstream artifacts built from the curated event corpus. Everything
here is **derivable** from `events/*.yaml` plus the scripts in
`../scripts/`; the directory's job is to be the reader-facing surface
the paper / reviewers / contributors actually look at.

## Subdirectories

| Path | What's there | Regenerate with |
| --- | --- | --- |
| [`trigger_registry/`](trigger_registry/) | Pre-admission trigger registry and v0.2 expansion gaps under the declared sampling frame | `make trigger-registry` |
| [`paper_tables/`](paper_tables/) | The seven paper tables (Tables 1–7) — every number the paper cites comes from here | `make paper-tables` |
| [`evidence-chains/`](evidence-chains/) | One evidence chain per admitted event (51 files): claim → observations → sources (body_hash) → honest gaps | `make render-evidence-all` |
| [`audit_worksheets/`](audit_worksheets/) | Per-event audit worksheets with hash-verification pre-check + sign-off checkboxes (default: anchor cases) | `make audit-worksheets` |
| [`operator_census/`](operator_census/) | Multi-repo git-history scan of operator compliance: 8-repo census, 1 OFAC-keyed substrate found (`flashbots/rpc-endpoint`) | `make operator-census` |
| [`inter_rater/`](inter_rater/) | Cohen's κ infrastructure: stratified blind sample + κ report. Current values are LLM-assisted self-consistency, not independent-human IRR. | `make irr-sample` then `make irr-kappa` |

## Top-level files

| File | What it is | Regenerate with |
| --- | --- | --- |
| [`anchor_gap_fill_log.md`](anchor_gap_fill_log.md) | Per-(anchor × layer) audit trail for the Phase-3 gap-fill (Wayback first-pass + git-history second-pass). Hand-curated record. | hand-edited |
| [`pilot-status.md`](pilot-status.md) | Machine-readable admission status across strata | `make status` |
| [`review-report.md`](review-report.md) | 5-dimension readiness scoring for every event | `make review` |
| [`staleness.md`](staleness.md) | Per-citation freshness / 404 sweep | `make staleness` |

L0 OONI query denominator summaries live under
[`../derived/l0_coverage_summary.md`](../derived/l0_coverage_summary.md)
and regenerate via `make l0-coverage-summary`.

## What this directory is NOT

- Not the place for raw collection logic — that lives under `../scripts/` and `../sources/`.
- Not a manuscript drafting space — paper TeX sources, when they exist, will live in `paper/` (currently absent at v0.1).
- Not a notebook scratchpad — exploratory work happens elsewhere; what lands here is reproducible from the committed YAML corpus.

## Reproducing the entire surface

```bash
make ofac-recent-action-candidates  # only materializes missing OFAC backfill stubs
make regenerate    # rebuilds dataset, derived/, paper_tables/, evidence-chains/, site/
make irr-kappa     # only after analysis/inter_rater/<var>_blind.csv recodes are filled
make operator-census   # only when the public RPC/builder/wallet repos may have changed
```

Set `SOURCE_DATE_EPOCH=<unix-seconds>` before `make regenerate` for byte-stable artifacts; reproduction via the pinned [`Dockerfile`](../Dockerfile) at the repo root.
