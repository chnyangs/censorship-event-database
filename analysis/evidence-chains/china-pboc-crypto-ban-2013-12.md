# Evidence chain — `china-pboc-crypto-ban-2013-12`

**Status**: `admitted` · **Stratum**: `S4_nation_state` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-05-31` · **Source commit**: `b71c00e` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-16` · **Tool version**: `0.1.0` · **Generated**: `2026-05-31T13:15:30Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> PBOC Notice 2013/289 of 2013-12-05 directed Chinese banks and payment
> service providers to refuse Bitcoin-related accounts and services; within
> ~13 days the PRC Bitcoin-exchange triad (BTC China, OKCoin, Huobi) paused
> CNY deposit channels in compliance. The offramp_cex layer carries the
> load-bearing direct-attribution observation; L4 frontend reactions are
> consistent with the cascade but require a Wayback-capture pass before they
> may anchor a separate observed_change row.

## 1. Trigger

- **Type**: `nation_state_block`
- **Actor**: `CN_PBOC`
- **Timestamp**: `2013-12-05 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <http://www.pbc.gov.cn/goutongjiaoliu/113456/113469/2982357/index.html>
  - Wayback: <https://web.archive.org/web/2014/http://www.pbc.gov.cn/goutongjiaoliu/113456/113469/2982357/index.html>
  > PBOC original publication of Notice 2013/289 (公告 [2013]289号 /
> "Notice on Preventing Bitcoin Risks" / 关于防范比特币风险的通知),
> issued 2013-12-05 jointly by five PRC ministries: People's Bank
> of China (PBOC), Ministry of Industry and Information Technology
> (MIIT), China Banking Regulatory Commission (CBRC), China
> Securities Regulatory Commission (CSRC), and China Insurance
> Regulatory Commission (CIRC). Core provisions: (1) classified
> Bitcoin as a "virtual commodity" rather than legal-tender
> currency; (2) prohibited financial institutions and payment
> service providers from buying/selling Bitcoin or providing
> Bitcoin-related custody, payment, conversion, or insurance
> services; (3) required Bitcoin exchanges to register with MIIT
> as "internet information service providers" and to comply with
> anti-money-laundering identification rules; (4) directed banks
> to refuse Bitcoin-related accounts. The pbc.gov.cn URL path
> format has changed since 2013; the provisional wayback
> anchor uses Wayback Machine year-prefix lookup and the specific
> capture timestamp requires re-pinning during human audit before
> this citation may serve as an admission anchor in its own right.
> Marked evidence_use=contextual_unarchived pending that re-pin.
- **`primary_legal`**
  - URL: <http://www.gov.cn/gzdt/2013-12/05/content_2542584.htm>
  > State Council (gov.cn) reproduction of the joint five-ministry
> announcement of Notice 2013/289 on 2013-12-05. Marked
> evidence_use=contextual_unarchived; the live gov.cn URL has
> path-format drift since 2013 and the specific Wayback snapshot
> timestamp is to be re-pinned during human audit.
- **`supporting_tracker`**
  - URL: <https://www.loc.gov/item/global-legal-monitor/2014-01-13/china-regulators-issue-notice-on-bitcoin-risks/>
  - Wayback: <https://web.archive.org/web/2020/https://www.loc.gov/item/global-legal-monitor/2014-01-13/china-regulators-issue-notice-on-bitcoin-risks/>
  > US Library of Congress Global Legal Monitor entry titled
> "China: Regulators Issue Notice on Bitcoin Risks" dated
> 2014-01-13, providing an English-language summary of Notice
> 2013/289 and naming all five issuing PRC ministries. Used
> here as a contextual translation anchor; the live loc.gov URL
> format is stable and routinely captured by Wayback, but the
> specific snapshot timestamp is to be re-pinned during human
> audit. Marked evidence_use=contextual_unarchived pending that
> re-pin.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: PRC financial-institution + exchange ecosystem (class)
- **Chains**: `bitcoin`

> Canonical target is the PRC policy directive itself, addressed to
> (a) Chinese financial institutions and payment service providers
> (prohibited from Bitcoin-related services), and (b) Chinese
> Bitcoin exchanges (required to register with MIIT and apply AML
> identification). Named affected exchanges in the 2013-12 window
> include BTC China (btcchina.com), OKCoin (okcoin.cn / okcoin.com),
> and Huobi (huobi.com); these are recorded as implicit second-order
> targets in observations.scope_descriptor rather than enumerated
> in canonical_domains, matching the sibling
> china-pboc-crypto-ban-2021 convention.

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `direct` · Δt = 312h

**Event label**: `cny_deposit_channels_paused_industry_wide`

**Timestamp**: `2013-12-18 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_legal`**
  - URL: <http://www.pbc.gov.cn/goutongjiaoliu/113456/113469/2982357/index.html>
  - Wayback: <https://web.archive.org/web/2014/http://www.pbc.gov.cn/goutongjiaoliu/113456/113469/2982357/index.html>
  > PBOC Notice 2013/289 is the legal instrument. The notice
> explicitly prohibits PRC financial institutions and payment
> service providers from offering Bitcoin-related custody,
> payment, conversion, or insurance services, and directs banks
> to refuse Bitcoin-related accounts; this is the regulatory
> mandate that drove the observed industry-wide CNY-deposit
> pause at BTC China, OKCoin, and Huobi. attribution=direct
> because the notice text names the regulatory mandate.
> Provisional wayback anchor; specific snapshot timestamp
> requires human-audit re-pinning before this citation may
> carry an admission anchor on its own.
- **`supporting_tracker`**
  - URL: <https://www.loc.gov/item/global-legal-monitor/2014-01-13/china-regulators-issue-notice-on-bitcoin-risks/>
  - Wayback: <https://web.archive.org/web/2020/https://www.loc.gov/item/global-legal-monitor/2014-01-13/china-regulators-issue-notice-on-bitcoin-risks/>
  > Library of Congress Global Legal Monitor 2014-01-13 English
> summary of Notice 2013/289, naming all five issuing
> ministries and the four core provisions. Corroborates the
> regulatory mandate behind the observed CNY-deposit pause at
> the PRC exchange triad. Specific Wayback snapshot timestamp
> requires re-pinning in human audit.

## 5. Honest coverage gaps

- **l4_frontend** (`not_measured`): Chinese Bitcoin exchange frontends (BTC China, OKCoin, Huobi) did

## 7. Related events

- [`china-pboc-crypto-ban-2021`](./china-pboc-crypto-ban-2021.md)
- [`india-rbi-crypto-ban-2018`](./india-rbi-crypto-ban-2018.md)
- [`nigeria-cbn-crypto-ban-2021`](./nigeria-cbn-crypto-ban-2021.md)
- [`turkey-cbrt-crypto-ban-2021`](./turkey-cbrt-crypto-ban-2021.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `b71c00e`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

