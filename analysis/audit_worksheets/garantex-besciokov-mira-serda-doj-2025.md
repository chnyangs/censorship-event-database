# Audit worksheet — `garantex-besciokov-mira-serda-doj-2025`

Dataset snapshot: **v0.2.0-rc-dryrun-11** · cutoff `2026-06-01` · commit `ec5c516` · generated `2026-06-01T00:00:00Z`

- **admission_tier**: `anchor_case`
- **research_stratum**: `S3_doj_sec_cftc_fiod`
- **empirical_shape**: `comparison`
- **status**: `admitted`
- **last_verified**: `2026-05-31`
- **last_human_audit**: `—`  ← update after sign-off

## 0. How to use this worksheet

Work top-to-bottom. For each row: (a) open the cited source in a browser (or `body_path` on disk) and confirm the passage supports the claim; (b) confirm the timestamp precision is appropriate for the claim; (c) confirm the attribution (`direct` / `plausible` / `none`) is not over-stated; (d) check that `observation_kind` is correct (no-change vs change vs gap). Mark the checkbox when satisfied. Leave a NOTE line if you changed anything. Reject the row (uncheck) if the claim needs revision — do NOT stamp `last_human_audit` until every row is checked.

## 1. Trigger

- **type**: `doj_indictment`
- **actor**: `US_DOJ`
- **timestamp**: `2025-03-07 00:00:00+00:00` · precision=`—`

### Trigger citations

- [ ] citation[0]: type=`primary_legal` · url=<https://web.archive.org/web/20250307000000/https://www.justice.gov/opa/pr/garantex-cryptocurrency-exchange-disrupted-international-operation> · wayback=<https://web.archive.org/web/20250307191431/https://www.justice.gov/opa/pr/garantex-cryptocurrency-exchange-disrupted-international-operation> · body_hash=`sha256:ec3f8121…8d8a` · body_path=`sources/http_captures/garantex-besciokov-mira-serda-doj-2025/primary/web.archive.org__web-20250307000000-https-www.justice.gov-opa-pr-garantex-cryptocurrency-exchange-disrupted-international-operation__d76e9d3a2a.html`  · hash_check=`ok`

Sign-off rules for the trigger: timestamp precision must match the citation granularity. If the SDN publishes to day precision, **do not** assert hour precision in any downstream observation's `delta_hours`.

## 2. Scoped claim (read carefully)

> "The 2025-03-07 coordinated U.S. takedown of Garantex (DOJ E.D. Va.
> indictment of administrators Besciokov and Mira Serda for money laundering
> conspiracy / IEEPA / unlicensed money transmitting + U.S. Secret Service
> seizure of three domains Garantex.org/.io/.academy + >$26M fund freeze)
> produced a 2-layer cascade: l4_frontend (domain seizure) and offramp_cex
> (exchange operational disruption), both attribution=direct. No asset_onchain
> row is asserted (release lists no on-chain addresses/tx_hashes; §1.6 floor
> unmet). Comparable-main tier."
> 

- [ ] Scoped claim does NOT overread the evidence (e.g. "the SDN caused X" when attribution is `plausible`).
- [ ] Scoped claim uses the dataset's controlled vocabulary (`observed_change` / `observed_no_change` / `plausible` / `direct`).

## 3. Observations

### 3.1 · `l4_frontend` · actor=`us_secret_service` · event=`secret_service_seizes_three_garantex_domains`

- **observation_kind**: `observed_change`
- **attribution**: `direct`
- **timestamp**: `2025-03-07 00:00:00+00:00` · precision=`day` · delta_hours=`0`
- **sources** (1):
  - [ ] src[0]: type=`primary_legal` · url=<https://web.archive.org/web/20250307000000/https://www.justice.gov/opa/pr/garantex-cryptocurrency-exchange-disrupted-international-operation> · wayback=<https://web.archive.org/web/20250307191431/https://www.justice.gov/opa/pr/garantex-cryptocurrency-exchange-disrupted-international-operation> · body_hash=`sha256:ec3f8121…8d8a` · body_path=`sources/http_captures/garantex-besciokov-mira-serda-doj-2025/primary/web.archive.org__web-20250307000000-https-www.justice.gov-opa-pr-garantex-cryptocurrency-exchange-disrupted-international-operation__d76e9d3a2a.html` · scope_descriptor=(3 keys)  · hash_check=`ok`

Audit checks:
- [ ] Passage in each cited source supports `observed_change` for this layer.
- [ ] Attribution `direct` is not over-stated (`direct` requires primary_* source corroborating the causal link).
- [ ] Timestamp precision is sufficient for any `delta_hours` downstream claim (day-precision → NO hour claim).
- [ ] The cited evidence rules out the observed change being caused by an unrelated ecosystem-level shift (especially for `direct` attribution).
- [ ] NOTE: _free-form audit note (if the row was revised)_

### 3.2 · `offramp_cex` · actor=`us_doj` · event=`garantex_exchange_operations_disrupted_by_indictment_and_seizure`

- **observation_kind**: `observed_change`
- **attribution**: `direct`
- **timestamp**: `2025-03-07 00:00:00+00:00` · precision=`day` · delta_hours=`0`
- **sources** (1):
  - [ ] src[0]: type=`primary_legal` · url=<https://web.archive.org/web/20250307000000/https://www.justice.gov/opa/pr/garantex-cryptocurrency-exchange-disrupted-international-operation> · wayback=<https://web.archive.org/web/20250307191431/https://www.justice.gov/opa/pr/garantex-cryptocurrency-exchange-disrupted-international-operation> · body_hash=`sha256:ec3f8121…8d8a` · body_path=`sources/http_captures/garantex-besciokov-mira-serda-doj-2025/primary/web.archive.org__web-20250307000000-https-www.justice.gov-opa-pr-garantex-cryptocurrency-exchange-disrupted-international-operation__d76e9d3a2a.html` · scope_descriptor=(3 keys)  · hash_check=`ok`

Audit checks:
- [ ] Passage in each cited source supports `observed_change` for this layer.
- [ ] Attribution `direct` is not over-stated (`direct` requires primary_* source corroborating the causal link).
- [ ] Timestamp precision is sufficient for any `delta_hours` downstream claim (day-precision → NO hour claim).
- [ ] The cited evidence rules out the observed change being caused by an unrelated ecosystem-level shift (especially for `direct` attribution).
- [ ] NOTE: _free-form audit note (if the row was revised)_

## 4. Recovery

_No recovery rows on this event._
## 5. Sign-off

- [ ] Every checkbox above is checked.
- [ ] Update `events/garantex-besciokov-mira-serda-doj-2025.yaml`: set `last_human_audit: YYYY-MM-DD` to today's UTC date.
- [ ] Run `make validate` after editing; `make derived` regenerates the derived artifacts consuming `last_human_audit` semantically.
- [ ] Log the audit in `CHANGELOG.md` (one line: `audit: <slug> · <auditor-initials> · <date> · <n-row-changes>`).

If any row could not be signed off, **do not stamp** `last_human_audit`; file the specific blocker as a GitHub issue tagged `audit-blocker` and link it from the event YAML's `analysis_notes` field.
