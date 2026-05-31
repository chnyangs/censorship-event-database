# Evidence chain — `japan-fsa-six-exchange-orders-2018-06`

**Status**: `admitted` · **Stratum**: `S4_nation_state` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `e43eea7` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-21` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "On 2018-06-22, the Japan FSA simultaneously issued business-
> improvement orders under the Payment Services Act to six registered
> crypto-asset exchanges — bitFlyer, Quoine, BTC Box, Bit Bank,
> BitPoint, and Tech Bureau (Zaif) — citing inadequate AML/CFT and
> KYC frameworks, compelling each operator to file a remediation plan
> by 2018-07-23 and to report monthly thereafter. bitFlyer
> additionally voluntarily suspended new-customer registrations the
> same day pending re-verification of existing customers' KYC data.
> The row does not claim frontend-disable, ISP/DNS-level connectivity
> blocking, on-chain asset-layer freeze, or any full withdrawal-rail
> suspension — only the single-day six-way offramp_cex supervisory-
> order load-bearing axis and bitFlyer's same-day onboarding pause."

## 1. Trigger

- **Type**: `regulatory_enforcement`
- **Actor**: `JP_FSA`
- **Timestamp**: `2018-06-22 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://www.fsa.go.jp/news/30/sonota/>
  - Wayback: <https://web.archive.org/web/2018/https://www.fsa.go.jp/news/30/sonota/>
  > Japan Financial Services Agency (金融庁 / FSA) press-release index
> for Heisei-30 (2018/2019) "sonota" (その他 / "other") notices. On
> 2018-06-22 the FSA issued 業務改善命令 (gyomu-kaizen-meirei /
> business-improvement orders) under the Payment Services Act
> (資金決済法) simultaneously against six registered crypto-asset
> exchanges — bitFlyer, Quoine (QUOINEX operator), BTC Box, Bit
> Bank (bitbank), BitPoint Japan, and Tech Bureau (Zaif operator).
> The orders followed FSA on-site inspections that found inadequate
> AML/CFT (anti-money-laundering / countering financing of
> terrorism) and KYC frameworks and required each operator to (1)
> file a written business-improvement plan by 2018-07-23 and (2)
> report monthly progress to the FSA by the 10th of each
> subsequent month. Largest post-Coincheck single-day FSA
> enforcement wave against the registered-VASP cohort. DRYRUN
> promotion: real anchor is an FSA press-release index folder
> pointer; pinned snapshot timestamp and body_hash capture for the
> specific 2018-06-22 six-firm release permalinks deferred to
> non-DRYRUN release. Marked evidence_use=contextual_unarchived
> per validator policy.
- **`supporting_journalism`**
  - URL: <https://www.coindesk.com/markets/2018/06/22/japans-financial-watchdog-orders-aml-shake-up-at-6-crypto-exchanges/>
  - Wayback: <https://web.archive.org/web/2018/https://www.coindesk.com/markets/2018/06/22/japans-financial-watchdog-orders-aml-shake-up-at-6-crypto-exchanges/>
  > CoinDesk 2018-06-22 "Japan's Financial Watchdog Orders AML
> Shake-Up at 6 Crypto Exchanges" — contemporaneous reporting
> enumerating the six named exchanges (bitFlyer, Quoine, BTC
> Box, Bit Bank, BitPoint, Tech Bureau) and confirming the
> AML/CFT framework-deficiency basis of the orders.
- **`supporting_journalism`**
  - URL: <https://cointelegraph.com/news/japan-hits-6-more-crypto-exchanges-with-business-improvement-orders>
  - Wayback: <https://web.archive.org/web/2018/https://cointelegraph.com/news/japan-hits-6-more-crypto-exchanges-with-business-improvement-orders>
  > Cointelegraph 2018-06-22 reporting on the FSA six-firm
> business-improvement-order wave; corroborates the same
> six-exchange enumeration and 2018-07-23 plan-filing deadline.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: JP FSA 2018-06-22 six-exchange business-improvement-order cohort
- **Canonical domains**: `bitflyer.com`, `quoine.com`, `btcbox.co.jp`, `bitbank.cc`, `bitpoint.co.jp`, `zaif.jp`

> Subset enumeration of six registered Japanese crypto-asset exchanges
> receiving FSA business-improvement orders simultaneously on
> 2018-06-22:
>   (1) bitFlyer, Inc. (株式会社bitFlyer) — Tokyo, largest JP-domestic
>       BTC/JPY exchange by volume at the time.
>   (2) Quoine Corporation (QUOINE株式会社) — operator of QUOINEX,
>       Singapore-headquartered with FSA-registered JP entity.
>   (3) BTC Box Co., Ltd. (株式会社BTCボックス) — Tokyo.
>   (4) Bit Bank, Inc. (ビットバンク株式会社) — Tokyo, operator of
>       bitbank.cc.
>   (5) BitPoint Japan Co., Ltd. (株式会社ビットポイントジャパン) — Tokyo,
>       subsidiary of Remixpoint, Inc.
>   (6) Tech Bureau Corp. (テックビューロ株式会社) — Osaka, operator of
>       Zaif (this is the operator entity that received the
>       subsequent 2018-09 follow-on order after the Zaif hack;
>       tracked as sibling event japan-fsa-zaif-orders-2018-09).
> Subset (not complete): there were additional FSA-registered VASPs
> (e.g. GMO Coin, DMM Bitcoin, Fisco, etc.) not named in the
> 2018-06-22 wave. The six named addressees of the 2018-06-22 orders
> are the defensible analytic slice.

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `plausible` · Δt = 0h

**Event label**: `six_exchange_aml_cft_business_improvement_orders_issued_simultaneously`

**Timestamp**: `2018-06-22 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_legal`**
  - URL: <https://www.fsa.go.jp/news/30/sonota/>
  - Wayback: <https://web.archive.org/web/2018/https://www.fsa.go.jp/news/30/sonota/>
  > FSA's 2018-06-22 業務改善命令 release wave is the legal
> instrument compelling AML/CFT and KYC framework remediation
> across the six named registered VASPs simultaneously.
> attribution=direct because the operator-side compliance
> actions (plan filings, monthly reporting, bitFlyer's
> voluntary new-customer suspension) are the regulatory
> response to the FSA supervisory directives, not a downstream
> cascade. DRYRUN: Wayback anchor is the FSA H30 sonota
> press-release index folder; pinned snapshot timestamp and
> body_hash capture for the specific 2018-06-22 release
> permalinks deferred to human audit.
- **`semi_primary_wayback`**
  - URL: <https://www.coindesk.com/markets/2018/06/22/japans-financial-watchdog-orders-aml-shake-up-at-6-crypto-exchanges/>
  - Wayback: <https://web.archive.org/web/20210923064637/https://www.coindesk.com/markets/2018/06/22/japans-financial-watchdog-orders-aml-shake-up-at-6-crypto-exchanges/>
  - body_hash: `sha256:58ed1bceab4d3bb1dc64def18ec456f4cb5eb26d2036a778200579aaf480347e`
  - body_path: `sources/http_captures/japan-fsa-six-exchange-orders-2018-06/primary/web.archive.org__web-20210923064637-https-www.coindesk.com-markets-2018-06-22-japans-financial-watchdog-orders-aml-shake-up-at-6-crypto-exchanges__68d4362819.html`
  > CoinDesk 2018-06-22 contemporaneous reporting enumerating
> the six addressee exchanges and the AML/CFT framework-
> deficiency basis of the FSA's orders.
- **`semi_primary_wayback`**
  - URL: <https://cointelegraph.com/news/japan-hits-6-more-crypto-exchanges-with-business-improvement-orders>
  - Wayback: <https://web.archive.org/web/20180622154214/https://cointelegraph.com/news/japan-hits-6-more-crypto-exchanges-with-business-improvement-orders>
  - body_hash: `sha256:afa5b71e2fe008ccb52d68f9d6a02303ee6798ca251ebe5519e5d11e986afaf7`
  - body_path: `sources/http_captures/japan-fsa-six-exchange-orders-2018-06/primary/web.archive.org__web-20180622154214-https-cointelegraph.com-news-japan-hits-6-more-crypto-exchanges-with-business-improvement-orders__797301cacf.html`
  > Cointelegraph 2018-06-22 corroborating coverage; same
> six-exchange enumeration and 2018-07-23 plan-filing deadline.

### offramp_cex · attribution: `plausible` · Δt = 0h

**Event label**: `bitflyer_voluntary_new_customer_registration_suspension`

**Timestamp**: `2018-06-22 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`semi_primary_wayback`**
  - URL: <https://www.coindesk.com/markets/2018/06/22/japans-financial-watchdog-orders-aml-shake-up-at-6-crypto-exchanges/>
  - Wayback: <https://web.archive.org/web/20210923064637/https://www.coindesk.com/markets/2018/06/22/japans-financial-watchdog-orders-aml-shake-up-at-6-crypto-exchanges/>
  - body_hash: `sha256:58ed1bceab4d3bb1dc64def18ec456f4cb5eb26d2036a778200579aaf480347e`
  - body_path: `sources/http_captures/japan-fsa-six-exchange-orders-2018-06/primary/web.archive.org__web-20210923064637-https-www.coindesk.com-markets-2018-06-22-japans-financial-watchdog-orders-aml-shake-up-at-6-crypto-exchanges__68d4362819.html`
  > CoinDesk coverage of bitFlyer's same-day announcement
> voluntarily suspending new-customer registrations and
> re-examining existing-customer ID verification.
- **`semi_primary_wayback`**
  - URL: <https://news.bitcoin.com/japanese-crypto-exchanges-regulators-improvement-orders/>
  - Wayback: <https://web.archive.org/web/20180626142058/https://news.bitcoin.com/japanese-crypto-exchanges-regulators-improvement-orders/>
  - body_hash: `sha256:abca7fc1a99e54d5ccd54982889af2831e297d525d9efdfc056687c114316832`
  - body_path: `sources/http_captures/japan-fsa-six-exchange-orders-2018-06/primary/web.archive.org__web-20180626142058-https-news.bitcoin.com-japanese-crypto-exchanges-regulators-improvement-orders__7680a5bd33.html`
  > Bitcoin.com summary of each of the six exchanges' responses
> to the FSA improvement orders, including bitFlyer's
> new-customer-onboarding suspension.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`japan-fsa-coincheck-orders-2018`](./japan-fsa-coincheck-orders-2018.md)
- [`japan-fsa-zaif-orders-2018-09`](./japan-fsa-zaif-orders-2018-09.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `e43eea7`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

