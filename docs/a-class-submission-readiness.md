# A-Class Submission Readiness Plan

Status as of 2026-05-07. This is the submission-focused track for an
A-class measurement / data paper. It deliberately narrows the ambition from
"A* full empirical census" to a defensible paper about a denominator-aware
measurement protocol and reproducible cross-layer event corpus.

> **Status update 2026-05-14**: current repo state should be treated as a working snapshot, not a strict release/submission artifact. Do not mark this plan complete until independent-human IRR, H2 null-case audit, and H3 release metadata/sign-off are complete and the full strict gate passes from a clean intended source tree.

## Submission Thesis

The paper should make one primary claim:

> A cross-layer crypto-censorship event database is useful only when it
> separates observed reactions from missing denominators. This project
> contributes a reproducible protocol, corpus, paper-table generator, and
> artifact package that connect legal / policy triggers to public
> stack-layer evidence without converting unmeasured layers into zeros.

The paper must not claim:

- population prevalence over all crypto-censorship events;
- full six-layer measurement coverage;
- L0 or L3 conditional rates in v0.1;
- private CEX or issuer inaction from public-evidence nulls;
- independent-human reliability until the independent-human IRR gate is
  actually complete.

## Current Baseline

| surface | current state | A-class interpretation |
| --- | --- | --- |
| Corpus | 53 admitted YAML records, 0 drafts | enough for a protocol/data paper; not enough for population inference |
| Case roles | 2 anchor, 38 empirical, 13 null | anchor count is too low for a case-study-heavy paper |
| Review posture | 7 `release_ready_scoped`, 46 `admitted_scope_blocked` | use most records as aggregate datapoints, not narrative claims |
| Trigger frame | 126 trigger-registry rows; 54 distinct in-frame triggers | transparent, but still under the v0.2 target of 150-250 frame units |
| L0 denominator | 0 measured denominators | report observability gap only |
| L3 denominator | 2 named partial Flashbots rows, 0 measured denominators | mechanism exemplar only; no provider rate |
| Reliability | LLM-assisted blinded recode only | self-consistency, not independent-human IRR |
| Artifact gate | `make check` / non-mutating working-snapshot `make paper-check` pass | strict submission gate still blocked until human/release items are complete |

## Phase A0 - Strict Submission Gate

Goal: convert the working snapshot into a submission-ready snapshot without
over-claiming.

Required work:

- Complete independent-human IRR for `coverage_status`,
  `observation_kind`, and `attribution`.
- Generate the H1 blank packet with `make irr-packet`; distribute only
  `site/h1_irr_packet/`, not key files or LLM audit notes.
- Complete the 13 null-case denominator audits listed in
  [`../human-audit.md`](../human-audit.md), or exclude unaudited null cases
  from any stronger narrative/null-denominator claims.
- Fix or re-scope `sec-v-uniswap-wells-notice-2024` before using it in any
  null aggregate that depends on frontend continuity.
- Decide the submission version/date as a human release action; then update
  `CITATION.cff` and regenerate metadata from a clean intended source tree.
- Run the strict gate from a clean checkout or clean committed source tree.

Acceptance gate:

```sh
make check
python3 scripts/validate.py --check-archives events/*.yaml
python3 scripts/check_paper_readiness.py --strict-audit --strict-null-audit --strict-repro --strict-reliability
```

Do not satisfy this phase by relabeling LLM outputs as human work.

## Phase A1 - Claim Lock

Goal: make every paper claim reviewable against a generated artifact.

Required work:

- Keep [`paper_claims.md`](paper_claims.md) as the single source of truth
  for claim wording, table source, case-role scope, and forbidden phrasing.
- Use Table 2 and the coverage matrix for all layer-rate statements.
- Put L0/L3 observability gaps adjacent to the primary result, not only in
  limitations.
- Keep `asset_onchain` rate language retracted because the admission anchor
  is structurally circular in v0.1.
- Cite the trigger registry when discussing sampling, so case selection is
  visibly pre-admission and not a post-hoc list.

Acceptance gate:

```sh
make paper-tables
python3 scripts/check_paper_readiness.py --strict-audit
```

## Phase A2 - Sampling Expansion

Goal: reduce the "cherry-picked 53 cases" objection without pretending the
dataset is a population sample.

Minimum A-class target:

- 70-90 admitted events if time is limited; 80-120 is the stronger v0.2
  target already encoded in [`sampling/frame.yaml`](../sampling/frame.yaml).
- 150-250 distinct in-frame trigger units in the registry.
- Real non-promoted backlog across S2/S3/S4/S5/S6, not only promoted OFAC
  duplicates.

Priority order:

| priority | stratum | why it matters |
| --- | --- | --- |
| P0 | S2 removals / reversals | strengthens recovery and bidirectional mechanism framing |
| P0 | S4 non-US state actions | reduces US-trigger dominance criticism |
| P1 | S3 DOJ / SEC / CFTC / FinCEN | expands enforcement diversity with visible platform surfaces |
| P1 | S6 supranational | tests whether the protocol survives outside national triggers |
| P2 | S5 corporate | improves mechanism comparisons, but only when a concrete policy trigger exists |

Acceptance gate:

- every candidate has source-frame provenance;
- every admitted event has an archival trigger source and at least one
  admissible observation or anchored null denominator;
- new cases do not support rate claims unless their layer rows have
  denominator eligibility.

## Phase A3 - Anchor Promotion

Goal: supply enough audited narrative exemplars for the paper body while
keeping aggregate claims table-driven.

Minimum A-class target:

- `anchor_case >= 6`;
- `release_ready_scoped >= 20`;
- `admitted_scope_blocked <= 30`.

Promotion queue:

| candidate | role |
| --- | --- |
| `tornado-cash-ofac-2022` | forward mechanism exemplar |
| `tornado-cash-ofac-delisting-2025` | reverse mechanism exemplar |
| `chatex-ofac-2021` | multi-layer OFAC exchange response |
| `binance-4framework-2023` | large-scale CEX compliance remediation |
| `circle-usdc-tornado-2022` | direct asset-layer mechanism |
| `semenov-ofac-2023` | non-identical Tornado follow-on with distinct attribution shape |
| one S4 non-US state action | external-validity anchor |
| one S6 supranational action | external-validity anchor |

Each promoted anchor needs:

- `last_human_audit`;
- replayable evidence chain;
- scoped narrative claim;
- no unresolved denominator mismatch;
- no reliance on an empirical/null case for narrative spotlight.

## Phase A4 - L0/L3 Denominator Appendix

Goal: turn missing L0/L3 rates into a methodologically positive result.

Required work:

- Treat [`l0-l3-denominator-appendix.md`](l0-l3-denominator-appendix.md) as
  required paper appendix material, not optional documentation.
- For L0, report OONI zero-result query cells as observability gaps, not
  non-blocking evidence.
- For L3, report Flashbots as named partial mechanism evidence only.
- Preserve the forbidden phrasing list in the paper draft.

Acceptance gate:

- Table 2's `l0_network` and `l3_rpc` cells trace to the appendix and
  generated derived files.
- No paper prose says "L3 changed in 2/9 applicable cases" or "no L0
  censorship occurred."

## Phase A5 - Artifact Package

Goal: make artifact evaluation a strength.

Required release surface:

- `dataset.json`, `dataset.csv`, `dataset.meta.json`;
- `events/*.yaml`;
- derived CSV/JSON/MD tables;
- paper tables;
- evidence chains;
- source manifest;
- static dashboard;
- audit worksheets and IRR report;
- release notes and citation metadata.

Acceptance gate:

```sh
make regenerate
make check
make render-site
python3 scripts/check_paper_readiness.py --strict-audit --strict-null-audit --strict-repro --strict-reliability
```

The final strict gate requires a clean committed source tree; running it
while local edits are uncommitted should fail by design.

## A-Class Go / No-Go

Submit if all are true:

- strict gate passes or the paper is explicitly labeled a non-release working
  paper with reliability claims removed;
- independent-human IRR exists for the variables used in rate/attribution
  claims;
- null denominators are human-audited or excluded from stronger claims;
- at least six anchors are human-audited and narrative-ready;
- sampling frame and backlog are visible;
- L0/L3 are framed as denominator results, not omissions.

Do not submit if any are true:

- the paper calls LLM self-consistency "inter-rater reliability";
- unaudited null cases are used as named narrative examples;
- 53 admitted events are presented as representative population coverage;
- L0/L3 missing denominators are written as zeros;
- the artifact cannot reproduce from a clean checkout.
