# Evidence chain — `china-pboc-banks-alipay-payment-channel-block-2021-06`

**Status**: `admitted` · **Stratum**: `S4_nation_state` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-02` · **Source commit**: `bb7ed29` · **Schema**: `0.2.0` · **Event last_verified**: `2026-06-02` · **Tool version**: `0.1.0` · **Generated**: `2026-06-02T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "On 2021-06-21 the PBOC ordered major PRC banks (ICBC, Agricultural Bank of
> China, et al.) and Alipay to cut off the payment / fund-transfer channels used
> by virtual-currency exchanges and OTC dealers and to close crypto-linked
> accounts. Effect captured at the offramp_cex layer at class level via the
> official PBOC release, with same-day journalism retained as corroboration."

## 1. Trigger

- **Type**: `nation_state_block`
- **Actor**: `CN_PBOC`
- **Timestamp**: `2021-06-21 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_government`**
  - URL: <https://www.pbc.gov.cn/goutongjiaoliu/113456/113469/2025092212551612812/index.html>
  - body_hash: `sha256:4be9779e2b2f10333311958a6aa32e4b5c26b8687b06e3202cbf2cb76e80658b`
  - body_path: `sources/http_captures/china-pboc-banks-alipay-payment-channel-block-2021-06/primary-pboc-repair/www.pbc.gov.cn__goutongjiaoliu-113456-113469-2025092212551612812-index.html__abab2abcf4.html`
  > Official People's Bank of China release, "人民银行就虚拟货币交易炒作问题
> 约谈部分银行和支付机构." Captured 2026-06-01 from pbc.gov.cn. The
> body states that PBOC departments summoned ICBC, Agricultural Bank of
> China, China Construction Bank, Postal Savings Bank, Industrial Bank,
> Alipay and other banks/payment institutions over services for virtual-
> currency trading speculation. It requires banks/payment institutions not
> to provide account opening, registration, trading, clearing, settlement
> or other products/services for such activity, to identify exchange/OTC
> dealer capital accounts, and to cut transaction-funds payment links.
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

### offramp_cex · attribution: `direct` · Δt = 0h

**Event label**: `crypto_payment_channels_cut_and_accounts_closed`

**Timestamp**: `2021-06-21 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_government`**
  - URL: <https://www.pbc.gov.cn/goutongjiaoliu/113456/113469/2025092212551612812/index.html>
  - body_hash: `sha256:4be9779e2b2f10333311958a6aa32e4b5c26b8687b06e3202cbf2cb76e80658b`
  - body_path: `sources/http_captures/china-pboc-banks-alipay-payment-channel-block-2021-06/primary-pboc-repair/www.pbc.gov.cn__goutongjiaoliu-113456-113469-2025092212551612812-index.html__abab2abcf4.html`
  > PBOC official 2021-06-21 release. The captured body explicitly names the
> summoned banks/payment institutions and instructs them not to provide
> account opening, registration, trading, clearing, settlement or related
> services for virtual-currency trading speculation, to identify exchange
> and OTC-dealer capital accounts, and to cut the transaction-funds payment
> links. attribution=direct because the regulator's own release states the
> order and the affected banking/payment-rail conduct.
- **`supporting_journalism`**
  - URL: <https://beincrypto.com/pboc-orders-major-banks-alipay-to-cease-servicing-crypto-companies/>
  - Wayback: <https://web.archive.org/web/20210621175818/https://beincrypto.com/pboc-orders-major-banks-alipay-to-cease-servicing-crypto-companies/>
  - body_hash: `sha256:893e2c9855fd706c7f3e19aaf03544126d5ef3868afff1207a9b732d10f9ad2d`
  - body_path: `sources/http_captures/china-pboc-banks-alipay-payment-channel-block-2021-06/primary/web.archive.org__web-20210621175818-https-beincrypto.com-pboc-orders-major-banks-alipay-to-cease-servicing-crypto-companies__2116be5c41.html`
  > Same-day BeInCrypto report quoting the PBOC 2021-06-21 statement and
> the institutions' responses (AgBank to close crypto-linked accounts;
> banks/Alipay to cut payment channels). Retained as same-day
> corroboration now that the PBOC primary release is pinned locally.
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

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `bb7ed29`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

