# Audit worksheet — `cryptex-ofac-2024`

Dataset snapshot: **v0.2.0-rc-dryrun-11** · cutoff `2026-06-01` · commit `fdd1545` · generated `2026-06-01T00:00:00Z`

- **admission_tier**: `anchor_case`
- **research_stratum**: `S1_ofac_sdn`
- **empirical_shape**: `comparison`
- **status**: `admitted`
- **last_verified**: `2026-04-21`
- **last_human_audit**: `2026-04-22`  ← update after sign-off

## 0. How to use this worksheet

Work top-to-bottom. For each row: (a) open the cited source in a browser (or `body_path` on disk) and confirm the passage supports the claim; (b) confirm the timestamp precision is appropriate for the claim; (c) confirm the attribution (`direct` / `plausible` / `none`) is not over-stated; (d) check that `observation_kind` is correct (no-change vs change vs gap). Mark the checkbox when satisfied. Leave a NOTE line if you changed anything. Reject the row (uncheck) if the claim needs revision — do NOT stamp `last_human_audit` until every row is checked.

## 1. Trigger

- **type**: `ofac_sdn_designation`
- **actor**: `US_OFAC`
- **timestamp**: `2024-09-26 00:00:00+00:00` · precision=`—`

### Trigger citations

- [ ] citation[0]: type=`primary_legal` · url=<https://ofac.treasury.gov/recent-actions/20240926> · wayback=<https://web.archive.org/web/20260421133030/https://ofac.treasury.gov/recent-actions/20240926> · body_hash=`sha256:332252f9…da76` · body_path=`sources/http_captures/cryptex-ofac-2024/ofac-recent-actions/ofac.treasury.gov__recent-actions-20240926__a282f3595b.html`  · hash_check=`ok`
- [ ] citation[1]: type=`primary_legal` · url=<https://home.treasury.gov/news/press-releases/jy2595>  · hash_check=`—`

Sign-off rules for the trigger: timestamp precision must match the citation granularity. If the SDN publishes to day precision, **do not** assert hour precision in any downstream observation's `delta_hours`.

## 2. Scoped claim (read carefully)

> "OFAC designation of the Cryptex Russian exchange on 2024-09-26
> co-occurred (same-day) with a US Secret Service judicial seizure of the canonical cryptex.net
> domain (L4 observed_change, direct attribution), while producing no measurable step change in
> Ethereum aggregate OFAC-compliant relay share (L1 null at day granularity)." Other layers
> remain scoped for follow-up.
> 

- [ ] Scoped claim does NOT overread the evidence (e.g. "the SDN caused X" when attribution is `plausible`).
- [ ] Scoped claim uses the dataset's controlled vocabulary (`observed_change` / `observed_no_change` / `plausible` / `direct`).

## 3. Observations

### 3.1 · `l4_frontend` · actor=`frontend:cryptex_net` · event=`canonical_domain_seized_by_US_Secret_Service`

- **observation_kind**: `observed_change`
- **attribution**: `direct`
- **timestamp**: `2024-09-26 16:05:01+00:00` · precision=`minute` · delta_hours=`16.1`
- **sources** (1):
  - [ ] src[0]: type=`primary_legal` · url=<https://web.archive.org/web/20240930052144/https://cryptex.net/> · body_hash=`sha256:6d119a27…70c7` · body_path=`sources/http_captures/cryptex-ofac-2024/frontend-wayback/web.archive.org__web-20240930052144-https-cryptex.net__a56bfd9215.html`  · hash_check=`ok`

Audit checks:
- [ ] Passage in each cited source supports `observed_change` for this layer.
- [ ] Attribution `direct` is not over-stated (`direct` requires primary_* source corroborating the causal link).
- [ ] Timestamp precision is sufficient for any `delta_hours` downstream claim (day-precision → NO hour claim).
- [ ] The cited evidence rules out the observed change being caused by an unrelated ecosystem-level shift (especially for `direct` attribution).
- [ ] NOTE: _free-form audit note (if the row was revised)_

### 3.2 · `asset_onchain` · actor=`tether_usdt_issuer` · event=`usdt_blacklist_same_day_event`

- **observation_kind**: `observed_change`
- **attribution**: `direct`
- **timestamp**: `2024-09-26 03:37:00+00:00` · precision=`minute` · delta_hours=`3.62`
- **sources** (2):
  - [ ] src[0]: type=`primary_onchain` · url=<https://etherscan.io/tx/0x55c457da2bac2555c666e9948baaa4a5ba66d730033b3684a4aa3c21a964b815>  · hash_check=`—`
  - [ ] src[1]: type=`supporting_community` · url=<https://usdtbanlist.com/address/0x0931cA4D13BB4ba75D9B7132AB690265D749a5E7> · body_hash=`sha256:145f410f…8faa` · body_path=`sources/http_captures/cryptex-ofac-2024/asset-layer-check/usdtbanlist.com__address-0x0931cA4D13BB4ba75D9B7132AB690265D749a5E7__169bb88c26.html`  · hash_check=`ok`

Audit checks:
- [ ] Passage in each cited source supports `observed_change` for this layer.
- [ ] Attribution `direct` is not over-stated (`direct` requires primary_* source corroborating the causal link).
- [ ] Timestamp precision is sufficient for any `delta_hours` downstream claim (day-precision → NO hour claim).
- [ ] The cited evidence rules out the observed change being caused by an unrelated ecosystem-level shift (especially for `direct` attribution).
- [ ] NOTE: _free-form audit note (if the row was revised)_

### 3.3 · `asset_onchain` · actor=`tether_usdt_issuer_tron` · event=`usdt_trc20_blacklist_same_day_event`

- **observation_kind**: `observed_change`
- **attribution**: `direct`
- **timestamp**: `2024-09-26 03:35:00+00:00` · precision=`minute` · delta_hours=`3.58`
- **sources** (2):
  - [ ] src[0]: type=`primary_onchain` · url=<https://tronscan.org/#/transaction/dad0d1dabad6f1727c6ebb3961053f66dd2add3b78def6360e5c2a2a6121cad9>  · hash_check=`—`
  - [ ] src[1]: type=`supporting_community` · url=<https://usdtbanlist.com/address/TTUDyVhhpCC1xJoPmWzdjLAzeoPwbSABdr> · body_hash=`sha256:fcabacd2…0cf0` · body_path=`sources/http_captures/cryptex-ofac-2024/asset-layer-check/usdtbanlist.com__address-TTUDyVhhpCC1xJoPmWzdjLAzeoPwbSABdr.html`  · hash_check=`ok`

Audit checks:
- [ ] Passage in each cited source supports `observed_change` for this layer.
- [ ] Attribution `direct` is not over-stated (`direct` requires primary_* source corroborating the causal link).
- [ ] Timestamp precision is sufficient for any `delta_hours` downstream claim (day-precision → NO hour claim).
- [ ] The cited evidence rules out the observed change being caused by an unrelated ecosystem-level shift (especially for `direct` attribution).
- [ ] NOTE: _free-form audit note (if the row was revised)_

### 3.4 · `asset_onchain` · actor=`circle_usdc_issuer` · event=`usdc_blacklist_next_day_event`

- **observation_kind**: `observed_change`
- **attribution**: `direct`
- **timestamp**: `2024-09-27 03:00:00+00:00` · precision=`minute` · delta_hours=`27.0`
- **sources** (2):
  - [ ] src[0]: type=`primary_onchain` · url=<https://etherscan.io/tx/0xa10d4e1a29a6eb30579b8cba5e1316d27ab120eff5944cce6836c8a837ffd8da>  · hash_check=`—`
  - [ ] src[1]: type=`supporting_community` · url=<https://usdtbanlist.com/address/0x0931cA4D13BB4ba75D9B7132AB690265D749a5E7> · body_hash=`sha256:145f410f…8faa` · body_path=`sources/http_captures/cryptex-ofac-2024/asset-layer-check/usdtbanlist.com__address-0x0931cA4D13BB4ba75D9B7132AB690265D749a5E7__169bb88c26.html`  · hash_check=`ok`

Audit checks:
- [ ] Passage in each cited source supports `observed_change` for this layer.
- [ ] Attribution `direct` is not over-stated (`direct` requires primary_* source corroborating the causal link).
- [ ] Timestamp precision is sufficient for any `delta_hours` downstream claim (day-precision → NO hour claim).
- [ ] The cited evidence rules out the observed change being caused by an unrelated ecosystem-level shift (especially for `direct` attribution).
- [ ] NOTE: _free-form audit note (if the row was revised)_

### 3.5 · `l1_consensus` · actor=`pbs_relay_ecosystem_aggregate` · event=`ofac_compliant_relay_share_stable_through_cryptex_designation`

- **observation_kind**: `observed_no_change`
- **attribution**: `none`
- **timestamp**: `2024-09-26 00:00:00+00:00` · precision=`day` · delta_hours=`0`
- **window**: `2024-09-12 00:00:00+00:00` → `2024-10-10 23:59:59+00:00`
- **sources** (2):
  - [ ] src[0]: type=`semi_primary_measurement` · url=<https://raw.githubusercontent.com/nerolation/censorship.pics/main/data/relay_censorship_share.csv> · body_hash=`sha256:45c1db9c…4567` · body_path=`sources/l1_datasets/tornado-cash-ofac-2022/relay_censorship_share.csv` · query_hash=`sha256:e147ceb6…fef2` · scope_descriptor=(2 keys)  · hash_check=`ok`
  - [ ] src[1]: type=`semi_primary_measurement` · url=<https://www.relayscan.io> · wayback=<https://web.archive.org/web/20260421114750/https://www.relayscan.io/> · body_hash=`sha256:dc39f559…a827` · body_path=`sources/http_captures/tornado-cash-ofac-2022/l1-relay-dashboards/www.relayscan.io__capture__1a79bf8cec.html`  · hash_check=`ok`

Audit checks:
- [ ] Passage in each cited source supports `observed_no_change` for this layer.
- [ ] Attribution `none` is not over-stated (`direct` requires primary_* source corroborating the causal link).
- [ ] Timestamp precision is sufficient for any `delta_hours` downstream claim (day-precision → NO hour claim).
- [ ] `observed_no_change` is bounded by a `window` and at least one falsifiable evidence anchor (query_hash / measurement_ids / body_hash+body_path / scope_descriptor).
- [ ] `attribution` is `none` (no causal claim under null observation).
- [ ] NOTE: _free-form audit note (if the row was revised)_

## 4. Recovery

_No recovery rows on this event._
## 5. Sign-off

- [ ] Every checkbox above is checked.
- [ ] Update `events/cryptex-ofac-2024.yaml`: set `last_human_audit: YYYY-MM-DD` to today's UTC date.
- [ ] Run `make validate` after editing; `make derived` regenerates the derived artifacts consuming `last_human_audit` semantically.
- [ ] Log the audit in `CHANGELOG.md` (one line: `audit: <slug> · <auditor-initials> · <date> · <n-row-changes>`).

If any row could not be signed off, **do not stamp** `last_human_audit`; file the specific blocker as a GitHub issue tagged `audit-blocker` and link it from the event YAML's `analysis_notes` field.
