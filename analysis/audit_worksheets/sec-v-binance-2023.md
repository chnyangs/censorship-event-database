# Audit worksheet — `sec-v-binance-2023`

Dataset snapshot: **v0.1.0** · cutoff `2026-04-22` · commit `8cadf3a` · generated `2026-04-24T00:30:31Z`

- **admission_tier**: `anchor_case`
- **research_stratum**: `S3_doj_sec_cftc_fiod`
- **empirical_shape**: `comparison`
- **status**: `admitted`
- **last_verified**: `2026-04-22`
- **last_human_audit**: `—`  ← update after sign-off

## 0. How to use this worksheet

Work top-to-bottom. For each row: (a) open the cited source in a browser (or `body_path` on disk) and confirm the passage supports the claim; (b) confirm the timestamp precision is appropriate for the claim; (c) confirm the attribution (`direct` / `plausible` / `none`) is not over-stated; (d) check that `observation_kind` is correct (no-change vs change vs gap). Mark the checkbox when satisfied. Leave a NOTE line if you changed anything. Reject the row (uncheck) if the claim needs revision — do NOT stamp `last_human_audit` until every row is checked.

## 1. Trigger

- **type**: `sec_action`
- **actor**: `US_SEC`
- **timestamp**: `2023-06-05 00:00:00+00:00` · precision=`—`

### Trigger citations

- [ ] citation[0]: type=`primary_legal` · url=<https://www.sec.gov/newsroom/press-releases/2023-101-sec-files-13-charges-against-binance-entities-founder-changpeng-zhao> · body_hash=`sha256:f1aeedd4…6665` · body_path=`sources/http_captures/sec-v-binance-2023/primary/www.sec.gov__news-press-release-2023-101__a38c3e222c.html`  · hash_check=`ok`

Sign-off rules for the trigger: timestamp precision must match the citation granularity. If the SDN publishes to day precision, **do not** assert hour precision in any downstream observation's `delta_hours`.

## 2. Scoped claim (read carefully)

> "SEC v. Binance (2023-06-05) was the first SEC civil-enforcement event in
> the dataset targeting a major crypto exchange; the asset-freeze motion
> produced a direct L4 + offramp cascade at Binance.US within 4 days
> (2023-06-09 fiat-rail suspension). Demonstrates securities-law
> enforcement as a distinct censorship-cascade trigger from OFAC SDN."
> 

- [ ] Scoped claim does NOT overread the evidence (e.g. "the SDN caused X" when attribution is `plausible`).
- [ ] Scoped claim uses the dataset's controlled vocabulary (`observed_change` / `observed_no_change` / `plausible` / `direct`).

## 3. Observations

### 3.1 · `l4_frontend` · actor=`frontend:binance_us` · event=`binance_us_suspended_usd_fiat_rails_within_4d`

- **observation_kind**: `observed_change`
- **attribution**: `direct`
- **timestamp**: `2023-06-09 00:00:00+00:00` · precision=`day` · delta_hours=`96.0`
- **sources** (1):
  - [ ] src[0]: type=`primary_legal` · url=<https://www.sec.gov/newsroom/press-releases/2023-101-sec-files-13-charges-against-binance-entities-founder-changpeng-zhao> · body_hash=`sha256:f1aeedd4…6665` · body_path=`sources/http_captures/sec-v-binance-2023/primary/www.sec.gov__news-press-release-2023-101__a38c3e222c.html`  · hash_check=`ok`

Audit checks:
- [ ] Passage in each cited source supports `observed_change` for this layer.
- [ ] Attribution `direct` is not over-stated (`direct` requires primary_* source corroborating the causal link).
- [ ] Timestamp precision is sufficient for any `delta_hours` downstream claim (day-precision → NO hour claim).
- [ ] The cited evidence rules out the observed change being caused by an unrelated ecosystem-level shift (especially for `direct` attribution).
- [ ] NOTE: _free-form audit note (if the row was revised)_

### 3.2 · `offramp_cex` · actor=`exchange:binance_us` · event=`binance_us_offramp_crippled_post_sec_freeze`

- **observation_kind**: `observed_change`
- **attribution**: `direct`
- **timestamp**: `2023-06-09 00:00:00+00:00` · precision=`day` · delta_hours=`96.0`
- **sources** (2):
  - [ ] src[0]: type=`primary_legal` · url=<https://www.sec.gov/newsroom/press-releases/2023-101-sec-files-13-charges-against-binance-entities-founder-changpeng-zhao> · body_hash=`sha256:f1aeedd4…6665` · body_path=`sources/http_captures/sec-v-binance-2023/primary/www.sec.gov__news-press-release-2023-101__a38c3e222c.html` · scope_descriptor=(3 keys)  · hash_check=`ok`
  - [ ] src[1]: type=`primary_legal` · url=<https://www.sec.gov/newsroom/press-releases/2023-101-sec-files-13-charges-against-binance-entities-founder-changpeng-zhao> · body_hash=`sha256:f1aeedd4…6665` · body_path=`sources/http_captures/sec-v-binance-2023/primary/www.sec.gov__news-press-release-2023-101__a38c3e222c.html`  · hash_check=`ok`

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
- [ ] Update `events/sec-v-binance-2023.yaml`: set `last_human_audit: YYYY-MM-DD` to today's UTC date.
- [ ] Run `make validate` after editing; `make derived` regenerates the derived artifacts consuming `last_human_audit` semantically.
- [ ] Log the audit in `CHANGELOG.md` (one line: `audit: <slug> · <auditor-initials> · <date> · <n-row-changes>`).

If any row could not be signed off, **do not stamp** `last_human_audit`; file the specific blocker as a GitHub issue tagged `audit-blocker` and link it from the event YAML's `analysis_notes` field.
