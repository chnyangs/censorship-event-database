# Audit worksheet — `tornado-cash-ofac-2022`

Dataset snapshot: **v0.2.0-rc-dryrun-11** · cutoff `2026-06-02` · commit `a7b40fe` · generated `2026-06-02T00:00:00Z`

- **admission_tier**: `anchor_case`
- **research_stratum**: `S1_ofac_sdn`
- **empirical_shape**: `cascade`
- **status**: `admitted`
- **last_verified**: `2026-04-21`
- **last_human_audit**: `2026-04-22`  ← update after sign-off

## 0. How to use this worksheet

Work top-to-bottom. For each row: (a) open the cited source in a browser (or `body_path` on disk) and confirm the passage supports the claim; (b) confirm the timestamp precision is appropriate for the claim; (c) confirm the attribution (`direct` / `plausible` / `none`) is not over-stated; (d) check that `observation_kind` is correct (no-change vs change vs gap). Mark the checkbox when satisfied. Leave a NOTE line if you changed anything. Reject the row (uncheck) if the claim needs revision — do NOT stamp `last_human_audit` until every row is checked.

## 1. Trigger

- **type**: `ofac_sdn_designation`
- **actor**: `US_OFAC`
- **timestamp**: `2022-08-08 13:30:00+00:00` · precision=`—`

### Trigger citations

- [ ] citation[0]: type=`primary_legal` · url=<https://ofac.treasury.gov/recent-actions/20220808> · wayback=<https://web.archive.org/web/20260421104932/https://ofac.treasury.gov/recent-actions/20220808> · body_hash=`sha256:ae648b94…bc79` · body_path=`sources/http_captures/tornado-cash-ofac-2022/ofac-recent-actions/ofac.treasury.gov__recent-actions-20220808__298acbc03a.html`  · hash_check=`ok`
- [ ] citation[1]: type=`primary_legal` · url=<https://ofac.treasury.gov/specially-designated-nationals-list-sdn-list/archive-of-changes-to-the-sdn-list>  · hash_check=`—`

Sign-off rules for the trigger: timestamp precision must match the citation granularity. If the SDN publishes to day precision, **do not** assert hour precision in any downstream observation's `delta_hours`.

## 2. Scoped claim (read carefully)

> "OFAC designation of Tornado Cash on 2022-08-08 produced the defining
> 3-layer cascade in the dataset: L4 frontend (tornado.cash taken offline
> ≈22h), asset_onchain (Circle USDC batch-blacklisted 19/38 addresses
> within 6h; dYdX closed accounts within 34h), and L1 consensus (censoring-
> relay share rose from 10.80% day-1 of PBS era to 41.10% 18 days later).
> The paper-defining original-cascade event, paired with the 2025-03-21
> delisting reverse-cascade."
> 

- [ ] Scoped claim does NOT overread the evidence (e.g. "the SDN caused X" when attribution is `plausible`).
- [ ] Scoped claim uses the dataset's controlled vocabulary (`observed_change` / `observed_no_change` / `plausible` / `direct`).

## 3. Observations

### 3.1 · `l1_consensus` · actor=`pbs_relay_ecosystem_aggregate` · event=`ofac_compliant_relay_share_rises_post_merge`

- **observation_kind**: `observed_change`
- **attribution**: `plausible`
- **timestamp**: `2022-09-16 00:00:00+00:00` · precision=`day` · delta_hours=`922.5`
- **sources** (3):
  - [ ] src[0]: type=`semi_primary_measurement` · url=<https://raw.githubusercontent.com/nerolation/censorship.pics/main/data/relay_censorship_share.csv> · body_hash=`sha256:45c1db9c…4567` · body_path=`sources/l1_datasets/tornado-cash-ofac-2022/relay_censorship_share.csv` · query_hash=`sha256:fec33511…1637` · scope_descriptor=(2 keys)  · hash_check=`ok`
  - [ ] src[1]: type=`semi_primary_measurement` · url=<https://censorship.pics> · wayback=<https://web.archive.org/web/20260223040258/https://censorship.pics/> · body_hash=`sha256:9de85e49…b5bd` · body_path=`sources/http_captures/tornado-cash-ofac-2022/l1-relay-dashboards/censorship.pics__capture__5bc3a85424.html`  · hash_check=`ok`
  - [ ] src[2]: type=`semi_primary_measurement` · url=<https://www.relayscan.io> · wayback=<https://web.archive.org/web/20260421114750/https://www.relayscan.io/> · body_hash=`sha256:dc39f559…a827` · body_path=`sources/http_captures/tornado-cash-ofac-2022/l1-relay-dashboards/www.relayscan.io__capture__1a79bf8cec.html`  · hash_check=`ok`

Audit checks:
- [ ] Passage in each cited source supports `observed_change` for this layer.
- [ ] Attribution `plausible` is not over-stated (`direct` requires primary_* source corroborating the causal link).
- [ ] Timestamp precision is sufficient for any `delta_hours` downstream claim (day-precision → NO hour claim).
- [ ] The cited evidence rules out the observed change being caused by an unrelated ecosystem-level shift (especially for `direct` attribution).
- [ ] NOTE: _free-form audit note (if the row was revised)_

### 3.2 · `l3_rpc` · actor=`flashbots_rpc_endpoint` · event=`ofac_blacklist_addition_of_tornado_pool_addresses`

- **observation_kind**: `observed_change`
- **attribution**: `direct`
- **timestamp**: `2022-08-08 16:20:50+00:00` · precision=`second` · delta_hours=`2.85`
- **sources** (4):
  - [ ] src[0]: type=`primary_corporate` · url=<https://github.com/flashbots/rpc-endpoint/commit/92ab6b1f9abfc62261f72361e8c8df48f832f2a9> · body_hash=`sha256:86c81be4…59e7` · body_path=`sources/operator_commits/tornado-cash-ofac-2022/ofacblacklist-at-92ab6b1.go`  · hash_check=`ok`
  - [ ] src[1]: type=`primary_corporate` · url=<https://github.com/flashbots/rpc-endpoint/pull/90> · body_hash=`sha256:0c4fafa0…46b9` · body_path=`sources/operator_commits/tornado-cash-ofac-2022/commit-92ab6b1.meta.txt`  · hash_check=`ok`
  - [ ] src[2]: type=`semi_primary_measurement` · url=<https://api.github.com/repos/flashbots/rpc-endpoint/pulls/90> · body_hash=`sha256:affdc833…ac41` · body_path=`sources/operator_commits/tornado-cash-ofac-2022/github-api/pr-90.response.json` · query_hash=`sha256:a05fde8d…0af6`  · hash_check=`ok`
  - [ ] src[3]: type=`semi_primary_measurement` · url=<https://api.github.com/repos/flashbots/rpc-endpoint/commits/92ab6b1f9abfc62261f72361e8c8df48f832f2a9> · body_hash=`sha256:5ed6923b…99f5` · body_path=`sources/operator_commits/tornado-cash-ofac-2022/github-api/commit.response.json` · query_hash=`sha256:20971b6f…d0c3`  · hash_check=`ok`
- **note (first line)**: Flashbots' rpc-endpoint service (the backend that later became

Audit checks:
- [ ] Passage in each cited source supports `observed_change` for this layer.
- [ ] Attribution `direct` is not over-stated (`direct` requires primary_* source corroborating the causal link).
- [ ] Timestamp precision is sufficient for any `delta_hours` downstream claim (day-precision → NO hour claim).
- [ ] The cited evidence rules out the observed change being caused by an unrelated ecosystem-level shift (especially for `direct` attribution).
- [ ] NOTE: _free-form audit note (if the row was revised)_

### 3.3 · `asset_onchain` · actor=`circle_usdc` · event=`address_blacklisted`

- **observation_kind**: `observed_change`
- **attribution**: `direct`
- **timestamp**: `2022-08-08 19:25:35+00:00` · precision=`second` · delta_hours=`5.93`
- **sources** (3):
  - [ ] src[0]: type=`primary_onchain` · url=<https://etherscan.io/tx/0xa61326744a21ce8d5397831d107ee14909b3f4eaaaddbf1f3dce879a19e30dd9> · block=`15307826`  · hash_check=`—`
  - [ ] src[1]: type=`supporting_community` · url=<https://usdtbanlist.com/address/0x8589427373d6d84e98730d7795d8f6f8731fda16> · wayback=<https://web.archive.org/web/20260421105443/https://usdtbanlist.com/address/0x8589427373d6d84e98730d7795d8f6f8731fda16> · body_hash=`sha256:b37912e4…5785` · body_path=`sources/http_captures/tornado-cash-ofac-2022/backfill-1.3/usdtbanlist.com__address-0x8589427373d6d84e98730d7795d8f6f8731fda16__1862a2f7aa.html`  · hash_check=`ok`
  - [ ] src[2]: type=`primary_corporate` · url=<https://www.circle.com/blog/ofacs-designation-of-tornado-cash-protocols-privacy-and-a-call-to-action> · wayback=<https://web.archive.org/web/20260421105602/https://www.circle.com/blog/ofacs-designation-of-tornado-cash-protocols-privacy-and-a-call-to-action> · body_hash=`sha256:fe0c8bbf…e435` · body_path=`sources/http_captures/tornado-cash-ofac-2022/backfill-1.3/www.circle.com__blog-ofacs-designation-of-tornado-cash-protocols-privacy-and-a-call-to-action__f24a980b38.html`  · hash_check=`ok`

Audit checks:
- [ ] Passage in each cited source supports `observed_change` for this layer.
- [ ] Attribution `direct` is not over-stated (`direct` requires primary_* source corroborating the causal link).
- [ ] Timestamp precision is sufficient for any `delta_hours` downstream claim (day-precision → NO hour claim).
- [ ] The cited evidence rules out the observed change being caused by an unrelated ecosystem-level shift (especially for `direct` attribution).
- [ ] NOTE: _free-form audit note (if the row was revised)_

### 3.4 · `l4_frontend` · actor=`frontend:tornado_cash_ui` · event=`ui_unavailable`

- **observation_kind**: `observed_change`
- **attribution**: `plausible`
- **timestamp**: `2022-08-09 12:00:00+00:00` · precision=`hour` · delta_hours=`22.5`
- **sources** (2):
  - [ ] src[0]: type=`semi_primary_measurement` · url=<https://github.com/tornadocash> · wayback=<https://web.archive.org/web/20260421105622/https://github.com/tornadocash> · body_hash=`sha256:c79b19d9…1c57` · body_path=`sources/http_captures/tornado-cash-ofac-2022/backfill-1.3/github.com__tornadocash__7f33190afd.html`  · hash_check=`ok`
  - [ ] src[1]: type=`semi_primary_measurement` · url=<https://github.com/tornadocash/tornado-core> · wayback=<https://web.archive.org/web/20260421105714/https://github.com/tornadocash/tornado-core> · body_hash=`sha256:90361734…8209` · body_path=`sources/http_captures/tornado-cash-ofac-2022/backfill-1.3/github.com__tornadocash-tornado-core__9430a15343.html`  · hash_check=`ok`

Audit checks:
- [ ] Passage in each cited source supports `observed_change` for this layer.
- [ ] Attribution `plausible` is not over-stated (`direct` requires primary_* source corroborating the causal link).
- [ ] Timestamp precision is sufficient for any `delta_hours` downstream claim (day-precision → NO hour claim).
- [ ] The cited evidence rules out the observed change being caused by an unrelated ecosystem-level shift (especially for `direct` attribution).
- [ ] NOTE: _free-form audit note (if the row was revised)_

### 3.5 · `offramp_cex` · actor=`exchange:dydx` · event=`accounts_flagged_and_close_only_mode`

- **observation_kind**: `observed_change`
- **attribution**: `direct`
- **timestamp**: `2022-08-10 00:00:00+00:00` · precision=`day` · delta_hours=`34.5`
- **sources** (2):
  - [ ] src[0]: type=`primary_corporate` · url=<https://dydx.exchange/blog/tornado-outage> · body_hash=`sha256:36962450…a904` · body_path=`sources/http_captures/tornado-cash-ofac-2022/backfill-1.3/dydx.exchange__blog-tornado-outage__4d80cd1762.html`  · hash_check=`ok`
  - [ ] src[1]: type=`primary_corporate` · url=<https://dydx.exchange/blog/tornado-cash-update> · wayback=<https://web.archive.org/web/20260421105743/https://dydx.exchange/blog/tornado-cash-update> · body_hash=`sha256:1d19ee8f…24dd` · body_path=`sources/http_captures/tornado-cash-ofac-2022/backfill-1.3/dydx.exchange__blog-tornado-cash-update__83f9281763.html`  · hash_check=`ok`

Audit checks:
- [ ] Passage in each cited source supports `observed_change` for this layer.
- [ ] Attribution `direct` is not over-stated (`direct` requires primary_* source corroborating the causal link).
- [ ] Timestamp precision is sufficient for any `delta_hours` downstream claim (day-precision → NO hour claim).
- [ ] The cited evidence rules out the observed change being caused by an unrelated ecosystem-level shift (especially for `direct` attribution).
- [ ] NOTE: _free-form audit note (if the row was revised)_

## 4. Recovery

- [ ] recovery[0]: layer=`asset_onchain` · resolved=`False` · resolved_timestamp=`—`
  - [ ] recovery layer is in `changed_layers` for this event (derived/event_metrics.json intersects recovery with changed_layers; a recovery row on a non-changed layer is silently ignored — revise or remove).

## 5. Sign-off

- [ ] Every checkbox above is checked.
- [ ] Update `events/tornado-cash-ofac-2022.yaml`: set `last_human_audit: YYYY-MM-DD` to today's UTC date.
- [ ] Run `make validate` after editing; `make derived` regenerates the derived artifacts consuming `last_human_audit` semantically.
- [ ] Log the audit in `CHANGELOG.md` (one line: `audit: <slug> · <auditor-initials> · <date> · <n-row-changes>`).

If any row could not be signed off, **do not stamp** `last_human_audit`; file the specific blocker as a GitHub issue tagged `audit-blocker` and link it from the event YAML's `analysis_notes` field.
