# Evidence chain — `nigeria-cbn-crypto-ban-2021`

**Status**: `admitted` · **Stratum**: `S4_nation_state` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `a4484c4` · **Schema**: `0.2.0` · **Event last_verified**: `2026-04-22` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "CBN circular of 2021-02-05 severed Naira banking channels for cryptocurrency exchanges
> in Nigeria. Market substituted P2P trading networks; quantitative impact at the
> offramp_cex layer is captured at class level."

## 1. Trigger

- **Type**: `nation_state_block`
- **Actor**: `NG_CBN`
- **Timestamp**: `2021-02-05 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://web.archive.org/web/20210207202129/https://www.cbn.gov.ng/Out/2021/CCD/Letter%20on%20Crypto.pdf>
  - Wayback: <https://web.archive.org/web/20210207202129/https://www.cbn.gov.ng/Out/2021/CCD/Letter%20on%20Crypto.pdf>
  - body_hash: `sha256:2e556124d8d4dfe65ac1747ef31d9732dd13f09fdc60506baa8e2cd7df232a19`
  - body_path: `sources/http_captures/nigeria-cbn-crypto-ban-2021/cbn-circular/web.archive.org__web-20210208014230-https-www.cbn.gov.ng-Out-2021-CCD-Letter-20on-20Crypto.pdf__7b84a24e69.html`
  > Central Bank of Nigeria (CBN) circular BSD/DIR/PUB/LAB/014/001 dated 2021-02-05,
> titled "Letter to All Deposit Money Banks, Non-Bank Financial Institutions and
> Other Financial Institutions — Re: Letter to All DMBs, NBFIs, and OFIs: Prohibition
> of Dealings in Cryptocurrencies or Facilitation of Payments for Cryptocurrency
> Exchanges." Directed all banks and financial institutions in Nigeria to close
> accounts of persons or entities transacting in cryptocurrencies, and to halt all
> crypto-related facilitation. Archived via Wayback 2021-02-07.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: Nigerian crypto exchanges / users (class)

> Nigerian crypto users and exchanges as a class. Affected the then-active P2P crypto
> trading ecosystem (LocalBitcoins, Paxful, Binance-Nigeria P2P corridor) and domestic
> exchanges. Target treated as entity-class-level; no specific enumeration in the CBN
> letter.

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `direct` · Δt = 0h

**Event label**: `naira_banking_channel_severed_industry_wide`

**Timestamp**: `2021-02-05 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_legal`**
  - URL: <https://web.archive.org/web/20210207202129/https://www.cbn.gov.ng/Out/2021/CCD/Letter%20on%20Crypto.pdf>
  - body_hash: `sha256:2e556124d8d4dfe65ac1747ef31d9732dd13f09fdc60506baa8e2cd7df232a19`
  - body_path: `sources/http_captures/nigeria-cbn-crypto-ban-2021/cbn-circular/web.archive.org__web-20210208014230-https-www.cbn.gov.ng-Out-2021-CCD-Letter-20on-20Crypto.pdf__7b84a24e69.html`
  > CBN circular is the legal instrument. attribution=direct because the letter
> explicitly mandates the banking cut-off.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`india-rbi-crypto-ban-2018`](./india-rbi-crypto-ban-2018.md)
- [`china-pboc-crypto-ban-2021`](./china-pboc-crypto-ban-2021.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `a4484c4`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

