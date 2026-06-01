# Evidence chain — `japan-fsa-zaif-orders-2018-09`

**Status**: `admitted` · **Stratum**: `S4_nation_state` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `575b085` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-21` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T11:33:54Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "Japan FSA's 2018-09-25 business-improvement order against
> Tech Bureau, Inc. (the third 2018 FSA supervisory order against
> the Zaif operator, following the 2018-09-14 hack of approximately
> ¥7 billion / USD 60-67M in BTC, BCH, and MONA) directly compelled
> the Zaif operator-state change of customer-withdrawal-rail freeze
> and the forced asset-and-business transfer to Fisco Cryptocurrency
> Exchange completed in late 2018. The row does not claim
> frontend-disable, ISP/DNS-level connectivity blocking, on-chain
> asset-layer freeze, or class-wide Japanese VASP-cohort suspension —
> only the single-entity Tech Bureau/Zaif-cohort offramp_cex
> load-bearing axis under the Payment Services Act supervisory
> regime."

## 1. Trigger

- **Type**: `regulatory_enforcement`
- **Actor**: `JP_FSA`
- **Timestamp**: `2018-09-25 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://www.fsa.go.jp/news/30/sonota/>
  - Wayback: <https://web.archive.org/web/2018/https://www.fsa.go.jp/news/30/sonota/>
  > Japan Financial Services Agency (金融庁 / FSA) press-release index for
> Heisei-30 (2018/2019) "sonota" (その他 / "other") notices. On
> 2018-09-25 the FSA issued a 業務改善命令 (gyomu-kaizen-meirei /
> business-improvement order) under the Payment Services Act (資金決済法)
> against Tech Bureau, Inc., the Osaka-based operator of the Zaif
> cryptocurrency exchange, following the 2018-09-14 hack in which
> approximately ¥7 billion (~USD 60-67M) of Bitcoin (BTC), Bitcoin
> Cash (BCH), and Monacoin (MONA) was stolen from Zaif hot wallets
> (¥2.2B of Tech Bureau's own funds and the balance from customer
> deposits). This was the third FSA supervisory order against
> Tech Bureau in calendar year 2018 (after 2018-03-08 and
> 2018-06-22 orders), positioning it within the broader Japan
> FSA registered-VASP supervisory cascade following the
> 2018-01-26 Coincheck NEM hack. The order required Tech Bureau
> to (1) submit a facts-finding and root-cause report, (2)
> construct a victim-compensation plan, and (3) strengthen its
> system-risk and customer-protection framework. Tech Bureau
> subsequently entered a forced corporate restructuring under
> which Fisco Cryptocurrency Exchange (a subsidiary of
> Japan-listed Fisco Ltd) injected ¥5B and acquired the Zaif
> exchange business, with the asset/customer-base transfer
> completed in late 2018. DRYRUN promotion: real anchor is an
> FSA press-release index folder pointer; pinned snapshot
> timestamp and body_hash capture for the specific 2018-09-25
> release permalink deferred to non-DRYRUN release. Marked
> evidence_use=contextual_unarchived to flag the unarchived
> state per validator policy.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: Tech Bureau, Inc. (Zaif)
- **Canonical domains**: `zaif.jp`

> Tech Bureau, Inc. (株式会社テックビューロ) — an Osaka-based crypto-asset
> exchange operator (Zaif exchange brand), treated at the entity-level
> as the named addressee of the FSA's 2018-09-25 業務改善命令
> (business-improvement order). Tech Bureau was a registered crypto-
> asset exchange service provider under the Payment Services Act
> (資金決済法) revision effective 2017-04 and had received prior FSA
> business-improvement orders on 2018-03-08 and 2018-06-22 prior to
> the 2018-09-14 hack. Downstream operational effect: Tech Bureau
> suspended customer crypto deposits/withdrawals on Zaif following
> the hack, executed a forced asset-and-business transfer to Fisco
> Cryptocurrency Exchange (Fisco Ltd subsidiary) closing in late
> 2018, and ultimately ceased independent operations.

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `plausible` · Δt = 0h

**Event label**: `zaif_withdrawal_rail_frozen_per_fsa_order_and_fisco_transfer`

**Timestamp**: `2018-09-25 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_legal`**
  - URL: <https://www.fsa.go.jp/news/30/sonota/>
  - Wayback: <https://web.archive.org/web/2018/https://www.fsa.go.jp/news/30/sonota/>
  > FSA's 2018-09-25 業務改善命令 (third business-improvement order
> to Tech Bureau in 2018, after 2018-03-08 and 2018-06-22) is
> the legal instrument that compelled the post-hack
> customer-protection / remediation regime at Zaif following
> the 2018-09-14 hack (~¥7B / USD 60-67M in BTC, BCH, MONA).
> attribution=direct because the operator-state change
> (withdrawal-rail freeze and forced Fisco asset-transfer) is
> the regulatory compliance with the FSA supervisory directive,
> not a downstream cascade. DRYRUN: Wayback anchor is an FSA
> press-index folder pointer at fsa.go.jp/news/30/sonota;
> pinned snapshot timestamp and body_hash capture for the
> specific 2018-09-25 release permalink deferred to human
> audit.
- **`semi_primary_wayback`**
  - URL: <https://www.coindesk.com/markets/2018/09/25/japan-regulators-seek-answers-in-wake-of-zaifs-60-million-crypto-hack/>
  - Wayback: <https://web.archive.org/web/20210926141325/https://www.coindesk.com/markets/2018/09/25/japan-regulators-seek-answers-in-wake-of-zaifs-60-million-crypto-hack/>
  - body_hash: `sha256:1592d2eb9e576f8b2a68c7c2921a1e5c581bccc08f0043aec95e1afcbb6371a6`
  - body_path: `sources/http_captures/japan-fsa-zaif-orders-2018-09/primary/web.archive.org__web-20210926141325-https-www.coindesk.com-markets-2018-09-25-japan-regulators-seek-answers-in-wake-of-zaifs-60-million-crypto-hack__bb711bc54f.html`
  > CoinDesk 2018-09-25 contemporaneous coverage of the FSA's
> third business-improvement order to Tech Bureau and the
> ~USD 60M Zaif hack disclosure (BTC + BCH + MONA loss
> composition). Supporting context for the trigger-day
> framing. DRYRUN: wayback wildcard pointer in lieu of
> pinned-timestamp snapshot.
- **`semi_primary_wayback`**
  - URL: <https://cointelegraph.com/news/forced-deal-and-fsa-scrutiny-what-do-we-know-about-japans-latest-hack>
  - Wayback: <https://web.archive.org/web/20180921215359/https://cointelegraph.com/news/forced-deal-and-fsa-scrutiny-what-do-we-know-about-japans-latest-hack>
  - body_hash: `sha256:59d887df8bd70dcdeb37cbedef26f73a1c2db74af893760ae35567ea73fec911`
  - body_path: `sources/http_captures/japan-fsa-zaif-orders-2018-09/primary/web.archive.org__web-20180921215359-https-cointelegraph.com-news-forced-deal-and-fsa-scrutiny-what-do-we-know-about-japans-latest-hack__68893c9567.html`
  > Cointelegraph September-2018 coverage of the Fisco
> Cryptocurrency Exchange ¥5B investment / forced asset-and-
> business acquisition of Zaif from Tech Bureau, situating
> the FSA supervisory cascade in the broader Japan-VASP
> regulatory frame post-Coincheck. DRYRUN: wayback wildcard
> pointer in lieu of pinned-timestamp snapshot.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`japan-fsa-coincheck-orders-2018`](./japan-fsa-coincheck-orders-2018.md)
- [`japan-fsa-six-exchange-orders-2018-06`](./japan-fsa-six-exchange-orders-2018-06.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `575b085`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

