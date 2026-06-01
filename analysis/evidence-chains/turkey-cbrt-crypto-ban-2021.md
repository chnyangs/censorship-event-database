# Evidence chain — `turkey-cbrt-crypto-ban-2021`

**Status**: `admitted` · **Stratum**: `S4_nation_state` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-02` · **Source commit**: `279da6b` · **Schema**: `0.2.0` · **Event last_verified**: `2026-04-22` · **Tool version**: `0.1.0` · **Generated**: `2026-06-02T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "CBRT regulation of 2021-04-16 (effective 2021-04-30) prohibited Turkish payment service
> providers from handling crypto-asset-related transactions. Exchanges themselves remained
> operational but direct payment-rail on-ramp was severed. Observational axis at
> offramp_cex layer at national-policy level."

## 1. Trigger

- **Type**: `nation_state_block`
- **Actor**: `TR_CBRT`
- **Timestamp**: `2021-04-16 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://web.archive.org/web/20210416073914/https://www.tcmb.gov.tr/>
  - Wayback: <https://web.archive.org/web/20210416073914/https://www.tcmb.gov.tr/>
  - body_hash: `sha256:43f6e1d01042f479c52a2f281c803e30271557de1b56b81820f08f7921a07360`
  - body_path: `sources/http_captures/turkey-cbrt-crypto-ban-2021/cbrt-regulation/web.archive.org__web-20210416100000-https-www.tcmb.gov.tr__effb7c7ee3.html`
  > Central Bank of the Republic of Turkey (CBRT / TCMB) "Regulation on the
> Disuse of Crypto-Assets in Payments" (Ödemelerde Kripto Varlıkların Kullanılmamasına
> Dair Yönetmelik), published in the Official Gazette 2021-04-16 (No. 31456), effective
> 2021-04-30. Prohibits use of crypto-assets directly or indirectly in payments and
> bans payment service providers from offering any crypto-payment functionality.
> Wayback snapshot of tcmb.gov.tr on 2021-04-16 captures the homepage as primary-source
> anchor; the specific Regulation text is linked from the Official Gazette site
> (pinned archive deferred).

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: Turkish payment service providers (class)

> Turkish payment service providers and users of crypto for payments, as a class.

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `direct` · Δt = 336h

**Event label**: `try_payment_rail_to_crypto_severed`

**Timestamp**: `2021-04-30 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_legal`**
  - URL: <https://web.archive.org/web/20210416073914/https://www.tcmb.gov.tr/>
  - body_hash: `sha256:43f6e1d01042f479c52a2f281c803e30271557de1b56b81820f08f7921a07360`
  - body_path: `sources/http_captures/turkey-cbrt-crypto-ban-2021/cbrt-regulation/web.archive.org__web-20210416100000-https-www.tcmb.gov.tr__effb7c7ee3.html`
  > CBRT homepage snapshot on regulation-publication day as primary anchor.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`india-rbi-crypto-ban-2018`](./india-rbi-crypto-ban-2018.md)
- [`nigeria-cbn-crypto-ban-2021`](./nigeria-cbn-crypto-ban-2021.md)
- [`china-pboc-crypto-ban-2021`](./china-pboc-crypto-ban-2021.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `279da6b`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

