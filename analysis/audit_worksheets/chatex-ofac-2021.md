# Audit worksheet — `chatex-ofac-2021`

Dataset snapshot: **v0.1.0** · cutoff `2026-04-22` · commit `8cadf3a` · generated `2026-04-24T00:30:31Z`

- **admission_tier**: `anchor_case`
- **research_stratum**: `S1_ofac_sdn`
- **empirical_shape**: `comparison`
- **status**: `admitted`
- **last_verified**: `2026-04-22`
- **last_human_audit**: `—`  ← update after sign-off

## 0. How to use this worksheet

Work top-to-bottom. For each row: (a) open the cited source in a browser (or `body_path` on disk) and confirm the passage supports the claim; (b) confirm the timestamp precision is appropriate for the claim; (c) confirm the attribution (`direct` / `plausible` / `none`) is not over-stated; (d) check that `observation_kind` is correct (no-change vs change vs gap). Mark the checkbox when satisfied. Leave a NOTE line if you changed anything. Reject the row (uncheck) if the claim needs revision — do NOT stamp `last_human_audit` until every row is checked.

## 1. Trigger

- **type**: `ofac_sdn_designation`
- **actor**: `US_OFAC`
- **timestamp**: `2021-11-08 00:00:00+00:00` · precision=`—`

### Trigger citations

- [ ] citation[0]: type=`primary_legal` · url=<https://ofac.treasury.gov/recent-actions/20211108> · wayback=<https://web.archive.org/web/20260421140140/https://ofac.treasury.gov/recent-actions/20211108> · body_hash=`sha256:12b576be…1942` · body_path=`sources/http_captures/chatex-ofac-2021/ofac-recent-actions/ofac.treasury.gov__recent-actions-20211108__a1d41cd3cf.html`  · hash_check=`ok`
- [ ] citation[1]: type=`primary_legal` · url=<https://home.treasury.gov/news/press-releases/jy0471>  · hash_check=`—`

Sign-off rules for the trigger: timestamp precision must match the citation granularity. If the SDN publishes to day precision, **do not** assert hour precision in any downstream observation's `delta_hours`.

## 2. Scoped claim (read carefully)

> "OFAC designation of Chatex on 2021-11-08 produced a direct L4 frontend change within
> 9 days in the form of an operator-posted compliance notice freezing customer withdrawals,
> mechanistically distinct from the same-quarter SUEX case (no frontend reaction) despite
> both being foreign exchange entities sanctioned under the same policy push."
> 

- [ ] Scoped claim does NOT overread the evidence (e.g. "the SDN caused X" when attribution is `plausible`).
- [ ] Scoped claim uses the dataset's controlled vocabulary (`observed_change` / `observed_no_change` / `plausible` / `direct`).

## 3. Observations

### 3.1 · `asset_onchain` · actor=`circle_usdc_issuer` · event=`usdc_blacklist_next_day_5_of_6_eth_addresses`

- **observation_kind**: `observed_change`
- **attribution**: `direct`
- **timestamp**: `2021-11-09 04:15:00+00:00` · precision=`minute` · delta_hours=`28.25`
- **sources** (3):
  - [ ] src[0]: type=`primary_onchain` · url=<https://etherscan.io/tx/0x14a97060a7370f5c88573f7d01391f6767133cfa596be9e2985ff57c042dfc23>  · hash_check=`—`
  - [ ] src[1]: type=`primary_corporate` · url=<https://usdtbanlist.com/address/0x67d40EE1A85bf4a4Bb7Ffae16De985e8427B6b45> · body_hash=`sha256:307d2114…c7e7` · body_path=`sources/http_captures/chatex-ofac-2021/asset-layer-check/usdtbanlist.com__address-0x67d40EE1A85bf4a4Bb7Ffae16De985e8427B6b45.html`  · hash_check=`ok`
  - [ ] src[2]: type=`primary_corporate` · url=<https://usdtbanlist.com/address/0x6f1ca141a28907f78ebaa64fb83a9088b02a8352> · body_hash=`sha256:dd37dbf6…20ad` · body_path=`sources/http_captures/chatex-ofac-2021/asset-layer-check/usdtbanlist.com__address-0x6f1ca141a28907f78ebaa64fb83a9088b02a8352.html`  · hash_check=`ok`

Audit checks:
- [ ] Passage in each cited source supports `observed_change` for this layer.
- [ ] Attribution `direct` is not over-stated (`direct` requires primary_* source corroborating the causal link).
- [ ] Timestamp precision is sufficient for any `delta_hours` downstream claim (day-precision → NO hour claim).
- [ ] The cited evidence rules out the observed change being caused by an unrelated ecosystem-level shift (especially for `direct` attribution).
- [ ] NOTE: _free-form audit note (if the row was revised)_

### 3.2 · `l4_frontend` · actor=`frontend:chatex_com` · event=`operator_compliance_notice_and_withdrawal_freeze`

- **observation_kind**: `observed_change`
- **attribution**: `direct`
- **timestamp**: `2021-11-17 17:59:45+00:00` · precision=`minute` · delta_hours=`233.99`
- **sources** (2):
  - [ ] src[0]: type=`primary_corporate` · url=<https://web.archive.org/web/20211117175945/https://chatex.com/> · body_hash=`sha256:6bc86f40…4a77` · body_path=`sources/http_captures/chatex-ofac-2021/frontend-wayback/web.archive.org__web-20211117175945-https-chatex.com__918765a11d.html`  · hash_check=`ok`
  - [ ] src[1]: type=`primary_corporate` · url=<https://web.archive.org/web/20211202224324/https://chatex.com/> · body_hash=`sha256:6d83f310…64f8` · body_path=`sources/http_captures/chatex-ofac-2021/frontend-wayback/web.archive.org__web-20211202224324-https-chatex.com__6965640198.html`  · hash_check=`ok`

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
- [ ] Update `events/chatex-ofac-2021.yaml`: set `last_human_audit: YYYY-MM-DD` to today's UTC date.
- [ ] Run `make validate` after editing; `make derived` regenerates the derived artifacts consuming `last_human_audit` semantically.
- [ ] Log the audit in `CHANGELOG.md` (one line: `audit: <slug> · <auditor-initials> · <date> · <n-row-changes>`).

If any row could not be signed off, **do not stamp** `last_human_audit`; file the specific blocker as a GitHub issue tagged `audit-blocker` and link it from the event YAML's `analysis_notes` field.
