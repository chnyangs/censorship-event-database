# Evidence chain — `iran-cbi-exchange-payment-gateway-block-2024-12`

**Status**: `admitted` · **Stratum**: `S4_nation_state` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `f1c99dd` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-31` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "On/around 2024-12-28 the Central Bank of Iran blocked the Iranian-rial payment
> gateways used by domestic cryptocurrency exchanges for deposits, as a rial-defense
> measure amid the currency's record low (withdrawal functions reportedly remained
> operational). The offramp_cex layer carries the load-bearing plausible-attribution
> observation at class level."

## 1. Trigger

- **Type**: `nation_state_block`
- **Actor**: `IR_CBI`
- **Timestamp**: `2024-12-28 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`supporting_journalism`**
  - URL: <https://web.archive.org/web/20251226045735/https://www.intellinews.com/iran-central-bank-blocks-crypto-payments-amid-industry-backlash-359655/>
  - Wayback: <https://web.archive.org/web/20251226045735/https://www.intellinews.com/iran-central-bank-blocks-crypto-payments-amid-industry-backlash-359655/>
  - body_hash: `sha256:057a38614a03a5546d2264c6ddd4f97bc91cef7c3dfa8e860adae87e2b087952`
  - body_path: `sources/http_captures/iran-cbi-exchange-freeze-2024-10/secondary/web.archive.org__web-20251226045735-https-www.intellinews.com-iran-central-bank-blocks-crypto-payments-amid-industry-backlash-359655__60b8322af4.html`
  > bne IntelliNews, "Iran central bank blocks crypto payments amid industry
> backlash." Captured body confirms the Central Bank of Iran (CBI) abruptly
> blocked the Iranian-rial payment channels used by digital-currency
> exchanges as the rial hit a record low against the US dollar on
> December 28 (2024), and that withdrawal functions remained operational.
> Crypto-platform operators warned in an open letter to President Pezeshkian
> that the restrictions threatened skilled jobs and knowledge-based
> companies. Carries the trigger date.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: Iranian crypto exchanges (rial payment-gateway class)

> Cryptocurrency exchanges operating in Iran with rial payment gateways, as a
> class. No specific exchange enumerated in the captured sources; the CBI action
> targets the rial deposit/payment rail used by the domestic exchange ecosystem
> at large. Class-level (codebook §7 subset).

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `plausible` · Δt = 0h

**Event label**: `rial_payment_gateways_to_crypto_exchanges_blocked`

**Timestamp**: `2024-12-28 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`supporting_journalism`**
  - URL: <https://web.archive.org/web/20260115120806/https://www.nobsbitcoin.com/iran-central-bank-blocks-payment-gateways-to-cryptocurrency-exchanges-amid-currency-crisis/>
  - Wayback: <https://web.archive.org/web/20260115120806/https://www.nobsbitcoin.com/iran-central-bank-blocks-payment-gateways-to-cryptocurrency-exchanges-amid-currency-crisis/>
  - body_hash: `sha256:ff9701436ebf8cf9f79379e4bfa4a0b2a5a4808d169e50703ae2c9b6d7119e22`
  - body_path: `sources/http_captures/iran-cbi-exchange-freeze-2024-10/primary/web.archive.org__web-20260115120806-https-www.nobsbitcoin.com-iran-central-bank-blocks-payment-gateways-to-cryptocurrency-exchanges-amid-currency-crisis__910c1da0f2.html`
  > nobsbitcoin (2025-01-14), "Iran's Central Bank Blocks Payment Gateways to
> Cryptocurrency Exchanges Amid Currency Crisis." Captured body confirms the
> CBI "abruptly blocked payment gateways for cryptocurrency exchanges
> without prior notice," following the rial's 37% 2024 devaluation, and
> references a government plan for a centralized crypto-management system
> "similar to Shaparak." attribution=plausible (codebook §1.5/§8.4): the
> load-bearing captured prose is contemporaneous journalism, not the CBI
> directive text, and the target is class-level (no exchange enumerated).
- **`supporting_journalism`**
  - URL: <https://web.archive.org/web/20251226045735/https://www.intellinews.com/iran-central-bank-blocks-crypto-payments-amid-industry-backlash-359655/>
  - Wayback: <https://web.archive.org/web/20251226045735/https://www.intellinews.com/iran-central-bank-blocks-crypto-payments-amid-industry-backlash-359655/>
  - body_hash: `sha256:057a38614a03a5546d2264c6ddd4f97bc91cef7c3dfa8e860adae87e2b087952`
  - body_path: `sources/http_captures/iran-cbi-exchange-freeze-2024-10/secondary/web.archive.org__web-20251226045735-https-www.intellinews.com-iran-central-bank-blocks-crypto-payments-amid-industry-backlash-359655__60b8322af4.html`
  > bne IntelliNews corroboration: CBI intervention "specifically targets the
> Iranian rial payment channels used by digital currency exchanges, though
> withdrawal functions remain operational"; announcement coincided with the
> rial's record low on December 28 and the government's foreign-currency
> rate reunification.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`iran-cbi-crypto-banking-prohibition-2018`](./iran-cbi-crypto-banking-prohibition-2018.md)
- [`nigeria-cbn-crypto-ban-2021`](./nigeria-cbn-crypto-ban-2021.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `f1c99dd`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

