# Evidence chain — `china-pboc-banks-alipay-payment-channel-block-2021-06`

**Status**: `admitted` · **Stratum**: `S4_nation_state` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `661a63f` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-31` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "On 2021-06-21 the PBOC ordered major PRC banks (ICBC, Agricultural Bank of
> China, et al.) and Alipay to cut off the payment / fund-transfer channels used
> by virtual-currency exchanges and OTC dealers and to close crypto-linked
> accounts. Effect captured at the offramp_cex layer at class level via a
> same-day journalism source quoting the PBOC directive."

## 1. Trigger

- **Type**: `nation_state_block`
- **Actor**: `CN_PBOC`
- **Timestamp**: `2021-06-21 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`supporting_journalism`**
  - URL: <https://beincrypto.com/pboc-orders-major-banks-alipay-to-cease-servicing-crypto-companies/>
  - Wayback: <https://web.archive.org/web/20210621175818/https://beincrypto.com/pboc-orders-major-banks-alipay-to-cease-servicing-crypto-companies/>
  - body_hash: `sha256:893e2c9855fd706c7f3e19aaf03544126d5ef3868afff1207a9b732d10f9ad2d`
  - body_path: `sources/http_captures/china-pboc-banks-alipay-payment-channel-block-2021-06/primary/web.archive.org__web-20210621175818-https-beincrypto.com-pboc-orders-major-banks-alipay-to-cease-servicing-crypto-companies__2116be5c41.html`
  > BeInCrypto, "PBOC Orders Major Banks, Alipay to Cease Servicing Crypto
> Companies" (same-day Wayback capture 2021-06-21 17:58 UTC). Reports that
> on 2021-06-21 the People's Bank of China summoned major state banks —
> including the Industrial and Commercial Bank of China (ICBC) and the
> Agricultural Bank of China — together with Ant Group's Alipay, and
> ordered them to (i) not provide crypto-related products/services
> (account opening, clearing, settlement), (ii) investigate and identify
> virtual-currency-exchange and OTC-dealer capital accounts, and (iii) cut
> off the payment/fund-transfer channels for those accounts. AgBank stated
> it would immediately close the account of any client found involved in
> crypto trading. Captured HTML verified to contain PBOC, Alipay,
> Agricultural Bank, ICBC, "cut off", and "close the account".

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: PRC banks & payment institutions (ICBC, AgBank, Alipay, et al.) / crypto exchange capital accounts

> Chinese banks and payment institutions named/summoned by the PBOC (ICBC,
> Agricultural Bank of China, China Construction Bank, Postal Savings Bank,
> Industrial Bank, Alipay) and, derivatively, the virtual-currency exchanges /
> OTC dealers whose bank and payment-app channels were ordered cut. Treated as
> entity-class-level; the named institutions are a non-exhaustive subset.

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `plausible` · Δt = 0h

**Event label**: `crypto_payment_channels_cut_and_accounts_closed`

**Timestamp**: `2021-06-21 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`supporting_journalism`**
  - URL: <https://beincrypto.com/pboc-orders-major-banks-alipay-to-cease-servicing-crypto-companies/>
  - Wayback: <https://web.archive.org/web/20210621175818/https://beincrypto.com/pboc-orders-major-banks-alipay-to-cease-servicing-crypto-companies/>
  - body_hash: `sha256:893e2c9855fd706c7f3e19aaf03544126d5ef3868afff1207a9b732d10f9ad2d`
  - body_path: `sources/http_captures/china-pboc-banks-alipay-payment-channel-block-2021-06/primary/web.archive.org__web-20210621175818-https-beincrypto.com-pboc-orders-major-banks-alipay-to-cease-servicing-crypto-companies__2116be5c41.html`
  > Same-day BeInCrypto report quoting the PBOC 2021-06-21 statement and
> the institutions' responses (AgBank to close crypto-linked accounts;
> banks/Alipay to cut payment channels). attribution=direct: the PBOC is
> the named authority and the directive explicitly orders the named
> banks/Alipay to cut crypto payment channels and close accounts. Primary
> PBOC release (pbc.gov.cn) not separately captured in this pass; the
> same-day journalism source is the load-bearing evidence for this draft.
- **`supporting_journalism`**
  - URL: <https://www.regulationasia.com/pboc-directs-banks-alipay-to-stamp-out-crypto-activity/>
  - Wayback: <https://web.archive.org/web/20210623023627/https://www.regulationasia.com/pboc-directs-banks-alipay-to-stamp-out-crypto-activity/>
  - body_hash: `sha256:92f8db927b56a6d37b3a2e4648f6c85b4d39ef362efe9e4558f6155af6b62117`
  - body_path: `sources/http_captures/china-pboc-banks-alipay-payment-channel-block-2021-06/primary/web.archive.org__web-20210623023627-https-www.regulationasia.com-pboc-directs-banks-alipay-to-stamp-out-crypto-activity__dc6a276e02.html`
  > Regulation Asia, "PBOC Directs Banks & Alipay to Stamp Out Crypto
> Activity" (Wayback 2021-06-23). The captured lede states financial
> institutions were asked to "identify the capital accounts of crypto
> exchanges and OTC dealers, and cut off their payment channels"; the
> captured article tags name Agricultural Bank of China, Alipay, China
> Construction Bank, ICBC, Industrial Bank, Postal Savings Bank of China
> and the PBOC — corroborating the named institutions in target
> enumeration. (Article body is partly paywalled below the lede; the
> captured lede + tags carry the cited facts.)

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`china-pboc-crypto-ban-2021`](./china-pboc-crypto-ban-2021.md)
- [`china-state-council-mining-crackdown-2021-05`](./china-state-council-mining-crackdown-2021-05.md)
- [`nigeria-cbn-crypto-ban-2021`](./nigeria-cbn-crypto-ban-2021.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `661a63f`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

