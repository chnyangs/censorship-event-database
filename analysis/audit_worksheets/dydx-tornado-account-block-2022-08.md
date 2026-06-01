# Audit worksheet — `dydx-tornado-account-block-2022-08`

Dataset snapshot: **v0.2.0-rc-dryrun-11** · cutoff `2026-06-01` · commit `08e3573` · generated `2026-06-01T05:04:01Z`

- **admission_tier**: `anchor_case`
- **research_stratum**: `S5_corporate`
- **empirical_shape**: `comparison`
- **status**: `admitted`
- **last_verified**: `2026-05-21`
- **last_human_audit**: `—`  ← update after sign-off

## 0. How to use this worksheet

Work top-to-bottom. For each row: (a) open the cited source in a browser (or `body_path` on disk) and confirm the passage supports the claim; (b) confirm the timestamp precision is appropriate for the claim; (c) confirm the attribution (`direct` / `plausible` / `none`) is not over-stated; (d) check that `observation_kind` is correct (no-change vs change vs gap). Mark the checkbox when satisfied. Leave a NOTE line if you changed anything. Reject the row (uncheck) if the claim needs revision — do NOT stamp `last_human_audit` until every row is checked.

## 1. Trigger

- **type**: `corporate_policy_change`
- **actor**: `dydx_trading_inc`
- **timestamp**: `2022-08-11 00:00:00+00:00` · precision=`—`

### Trigger citations

- [ ] citation[0]: type=`primary_corporate` · url=<https://dydx.exchange/blog/tornado-cash-update> · wayback=<https://web.archive.org/web/2022/https://dydx.exchange/blog/tornado-cash-update>  · hash_check=`—`
- [ ] citation[1]: type=`supporting_journalism` · url=<https://www.coindesk.com/business/2022/08/11/crypto-exchange-dydx-blocked-accounts-that-received-even-small-amounts-from-tornado-cash> · wayback=<https://web.archive.org/web/2022/https://www.coindesk.com/business/2022/08/11/crypto-exchange-dydx-blocked-accounts-that-received-even-small-amounts-from-tornado-cash>  · hash_check=`—`
- [ ] citation[2]: type=`supporting_journalism` · url=<https://www.theblock.co/post/162928/dydx-confirms-blocking-user-accounts-tied-to-tornado-cash> · wayback=<https://web.archive.org/web/2022/https://www.theblock.co/post/162928/dydx-confirms-blocking-user-accounts-tied-to-tornado-cash>  · hash_check=`—`
- [ ] citation[3]: type=`supporting_journalism` · url=<https://cointelegraph.com/news/dydx-confirms-blocking-and-unblocking-some-accounts-linked-to-tornado-cash> · wayback=<https://web.archive.org/web/2022/https://cointelegraph.com/news/dydx-confirms-blocking-and-unblocking-some-accounts-linked-to-tornado-cash>  · hash_check=`—`

Sign-off rules for the trigger: timestamp precision must match the citation granularity. If the SDN publishes to day precision, **do not** assert hour precision in any downstream observation's `delta_hours`.

## 2. Scoped claim (read carefully)

> "dYdX's 2022-08-11 block of accounts whose wallets had any
> historical interaction with the OFAC-designated Tornado Cash
> contracts — implemented via a third-party compliance vendor
> flag at the dYdX-operated trading UI, with funds remaining
> withdrawable from flagged accounts — documents an L4-frontend
> + offramp_cex dual-layer corporate-compliance action and the
> first major operator-acknowledged history-based 'guilt by
> association' block downstream of the 2022-08-08 OFAC trigger
> (related event tornado-cash-ofac-2022). Paper-relevant as the
> hybrid-CEX vertex of the S5_corporate cascade (alongside
> aave-tornado-frontend-block-2022-08 at L4 and
> uniswap-balancer-tornado-frontend-block-2022-08 at L4)."
> 

- [ ] Scoped claim does NOT overread the evidence (e.g. "the SDN caused X" when attribution is `plausible`).
- [ ] Scoped claim uses the dataset's controlled vocabulary (`observed_change` / `observed_no_change` / `plausible` / `direct`).

## 3. Observations

### 3.1 · `l4_frontend` · actor=`frontend:dydx_trading_inc` · event=`dydx_blocked_accounts_with_any_historical_tornado_cash_interaction`

- **observation_kind**: `observed_change`
- **attribution**: `direct`
- **timestamp**: `2022-08-11 00:00:00+00:00` · precision=`day` · delta_hours=`0`
- **sources** (2):
  - [ ] src[0]: type=`primary_corporate` · url=<https://dydx.exchange/blog/tornado-cash-update> · wayback=<https://web.archive.org/web/20220829214213/https://dydx.exchange/blog/tornado-cash-update> · body_hash=`sha256:e4f66984…b817` · body_path=`sources/http_captures/dydx-tornado-account-block-2022-08/primary/web.archive.org__web-20220812000000-https-dydx.exchange-blog-tornado-cash-update__c44496f200.html`  · hash_check=`ok`
  - [ ] src[1]: type=`semi_primary_wayback` · url=<https://www.coindesk.com/business/2022/08/11/crypto-exchange-dydx-blocked-accounts-that-received-even-small-amounts-from-tornado-cash> · wayback=<https://web.archive.org/web/20220811213559/https://www.coindesk.com/business/2022/08/11/crypto-exchange-dydx-blocked-accounts-that-received-even-small-amounts-from-tornado-cash/> · body_hash=`sha256:4ca9dc3f…4157` · body_path=`sources/http_captures/dydx-tornado-account-block-2022-08/primary/web.archive.org__web-20220812000000-https-www.coindesk.com-business-2022-08-11-crypto-exchange-dydx-blocked-accounts-that-received-even-small-amounts-from-tornado-cash__641b67aa65.html`  · hash_check=`ok`

Audit checks:
- [ ] Passage in each cited source supports `observed_change` for this layer.
- [ ] Attribution `direct` is not over-stated (`direct` requires primary_* source corroborating the causal link).
- [ ] Timestamp precision is sufficient for any `delta_hours` downstream claim (day-precision → NO hour claim).
- [ ] The cited evidence rules out the observed change being caused by an unrelated ecosystem-level shift (especially for `direct` attribution).
- [ ] NOTE: _free-form audit note (if the row was revised)_

### 3.2 · `offramp_cex` · actor=`exchange:dydx` · event=`dydx_off_ramp_trading_restricted_for_tornado_tainted_accounts`

- **observation_kind**: `observed_change`
- **attribution**: `direct`
- **timestamp**: `2022-08-11 00:00:00+00:00` · precision=`day` · delta_hours=`0`
- **sources** (2):
  - [ ] src[0]: type=`primary_corporate` · url=<https://dydx.exchange/blog/tornado-cash-update> · wayback=<https://web.archive.org/web/20220829214213/https://dydx.exchange/blog/tornado-cash-update> · body_hash=`sha256:e4f66984…b817` · body_path=`sources/http_captures/dydx-tornado-account-block-2022-08/primary/web.archive.org__web-20220812000000-https-dydx.exchange-blog-tornado-cash-update__c44496f200.html`  · hash_check=`ok`
  - [ ] src[1]: type=`semi_primary_wayback` · url=<https://www.coindesk.com/business/2022/08/11/crypto-exchange-dydx-blocked-accounts-that-received-even-small-amounts-from-tornado-cash> · wayback=<https://web.archive.org/web/20220811213559/https://www.coindesk.com/business/2022/08/11/crypto-exchange-dydx-blocked-accounts-that-received-even-small-amounts-from-tornado-cash/> · body_hash=`sha256:4ca9dc3f…4157` · body_path=`sources/http_captures/dydx-tornado-account-block-2022-08/primary/web.archive.org__web-20220812000000-https-www.coindesk.com-business-2022-08-11-crypto-exchange-dydx-blocked-accounts-that-received-even-small-amounts-from-tornado-cash__641b67aa65.html`  · hash_check=`ok`

Audit checks:
- [ ] Passage in each cited source supports `observed_change` for this layer.
- [ ] Attribution `direct` is not over-stated (`direct` requires primary_* source corroborating the causal link).
- [ ] Timestamp precision is sufficient for any `delta_hours` downstream claim (day-precision → NO hour claim).
- [ ] The cited evidence rules out the observed change being caused by an unrelated ecosystem-level shift (especially for `direct` attribution).
- [ ] NOTE: _free-form audit note (if the row was revised)_

## 4. Recovery

- [ ] recovery[0]: layer=`l4_frontend` · resolved=`False` · resolved_timestamp=`—`
  - [ ] recovery layer is in `changed_layers` for this event (derived/event_metrics.json intersects recovery with changed_layers; a recovery row on a non-changed layer is silently ignored — revise or remove).
- [ ] recovery[1]: layer=`offramp_cex` · resolved=`False` · resolved_timestamp=`—`
  - [ ] recovery layer is in `changed_layers` for this event (derived/event_metrics.json intersects recovery with changed_layers; a recovery row on a non-changed layer is silently ignored — revise or remove).

## 5. Sign-off

- [ ] Every checkbox above is checked.
- [ ] Update `events/dydx-tornado-account-block-2022-08.yaml`: set `last_human_audit: YYYY-MM-DD` to today's UTC date.
- [ ] Run `make validate` after editing; `make derived` regenerates the derived artifacts consuming `last_human_audit` semantically.
- [ ] Log the audit in `CHANGELOG.md` (one line: `audit: <slug> · <auditor-initials> · <date> · <n-row-changes>`).

If any row could not be signed off, **do not stamp** `last_human_audit`; file the specific blocker as a GitHub issue tagged `audit-blocker` and link it from the event YAML's `analysis_notes` field.
