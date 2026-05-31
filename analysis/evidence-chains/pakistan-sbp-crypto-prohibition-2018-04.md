# Evidence chain — `pakistan-sbp-crypto-prohibition-2018-04`

**Status**: `admitted` · **Stratum**: `S4_nation_state` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `e43eea7` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-31` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "SBP BPRD Circular No. 03 of 2018 (2018-04-06) barred regulated banks, DFIs,
> microfinance banks and payment-system operators in Pakistan from processing or
> facilitating virtual-currency/ICO-token transactions, severing the PKR fiat
> banking/payment rail for the Pakistani crypto ecosystem. The offramp_cex layer
> carries the load-bearing direct-attribution observation at class level."

## 1. Trigger

- **Type**: `nation_state_block`
- **Actor**: `PK_SBP`
- **Timestamp**: `2018-04-06 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://web.archive.org/web/20180409033815/http://www.sbp.org.pk/bprd/2018/C3.htm>
  - Wayback: <https://web.archive.org/web/20180409033815/http://www.sbp.org.pk/bprd/2018/C3.htm>
  - body_hash: `sha256:7f326e4384a9c3a6f060a2d72326cd09795d56a40ab5a2ae39cce7c1ba81a876`
  - body_path: `sources/http_captures/pakistan-sbp-crypto-prohibition-2018-04/primary/web.archive.org__web-20180409033815-http-www.sbp.org.pk-bprd-2018-C3.htm__5d4efb5b12.html`
  > State Bank of Pakistan BPRD Circular No. 03 of 2018, dated 2018-04-06,
> titled "Prohibition of Dealing in Virtual Currencies/Tokens," addressed
> to the Presidents/Chief Executive Officers of all banks, DFIs,
> microfinance banks, Payment System Operators (PSOs) and Payment System
> Providers (PSPs). The circular advises all such entities to refrain from
> processing, using, trading, holding, transferring value, promoting,
> and investing in virtual currencies/tokens, and directs banks/DFIs not
> to facilitate any customer/account-holder transactions in such currencies.
> Captured from official sbp.org.pk via Wayback memento 2018-04-09.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: PK banks / DFIs / PSOs facilitating crypto (class)

> Pakistani crypto users and the regulated banking/payment-system sector as a
> class. The circular addresses all banks, DFIs, microfinance banks, PSOs and
> PSPs and bars them from facilitating any virtual-currency transactions —
> effectively severing the fiat banking/payment rails for the then-active
> Pakistani crypto ecosystem. No specific exchange is enumerated in the
> circular; target treated as entity-class-level, matching the sibling
> india-rbi-crypto-ban-2018 and nigeria-cbn-crypto-ban-2021 convention.

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `direct` · Δt = 0h

**Event label**: `pkr_banking_payment_channel_severed_industry_wide`

**Timestamp**: `2018-04-06 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_legal`**
  - URL: <https://web.archive.org/web/20180409033815/http://www.sbp.org.pk/bprd/2018/C3.htm>
  - Wayback: <https://web.archive.org/web/20180409033815/http://www.sbp.org.pk/bprd/2018/C3.htm>
  - body_hash: `sha256:7f326e4384a9c3a6f060a2d72326cd09795d56a40ab5a2ae39cce7c1ba81a876`
  - body_path: `sources/http_captures/pakistan-sbp-crypto-prohibition-2018-04/primary/web.archive.org__web-20180409033815-http-www.sbp.org.pk-bprd-2018-C3.htm__5d4efb5b12.html`
  > BPRD Circular No. 03 of 2018 is the legal instrument. attribution=direct
> because the circular explicitly mandates that banks/DFIs/PSOs refrain
> from and not facilitate virtual-currency transactions, cutting the
> banking/payment rail at class level.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`india-rbi-crypto-ban-2018`](./india-rbi-crypto-ban-2018.md)
- [`nigeria-cbn-crypto-ban-2021`](./nigeria-cbn-crypto-ban-2021.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `e43eea7`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

