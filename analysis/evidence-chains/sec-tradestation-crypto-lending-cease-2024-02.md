# Evidence chain — `sec-tradestation-crypto-lending-cease-2024-02`

**Status**: `admitted` · **Stratum**: `S3_doj_sec_cftc_fiod` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-05-31` · **Source commit**: `a331305` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-31` · **Tool version**: `0.1.0` · **Generated**: `2026-05-31T04:56:33Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "The 2024-02-07 SEC order (press release 2024-16) against TradeStation
> Crypto's unregistered crypto-asset lending product accompanied
> TradeStation's 2024-02-22 termination of all US crypto products/services:
> a single-layer offramp_cex effect (US off-ramp exit), attribution=direct.
> comparable_main tier."

## 1. Trigger

- **Type**: `sec_action`
- **Actor**: `US_SEC`
- **Timestamp**: `2024-02-07 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://www.sec.gov/newsroom/press-releases/2024-16>
  - Wayback: <https://web.archive.org/web/20241202223813/https://www.sec.gov/newsroom/press-releases/2024-16>
  - body_hash: `sha256:1957374f06ba27a4bd1967879a822a3419546271a25b2e37c4c43266e4f3988e`
  - body_path: `sources/http_captures/sec-tradestation-crypto-lending-cease-2024-02/primary/web.archive.org__web-20240208000000-https-www.sec.gov-newsroom-press-releases-2024-16__eacc05bdc3.html`
  > SEC press release 2024-16 (2024-02-07): "SEC Charges TradeStation
> Crypto for Unregistered Offer and Sale of Crypto Asset Lending
> Product." The SEC found that TradeStation Crypto, Inc. offered and
> sold a crypto-asset lending product with an interest feature as an
> unregistered security and ordered a cease-and-desist plus a $1.5M
> penalty (parallel state settlement +$1.5M). The same release records
> that "TradeStation announced earlier this year that it intends to
> terminate all its crypto-related products and services in the U.S.
> market on February 22, 2024." Wayback 20241202223813 pinned.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: TradeStation Crypto, Inc.
- **Canonical domains**: `tradestation.com`

> TradeStation Crypto, Inc. (Plantation, Florida) — a US-registered
> crypto brokerage / off-ramp. The SEC order targets the named entity
> and its crypto-asset lending product (interest feature). Marked subset:
> the named operator + its US crypto service line, not an enumerated set
> of customer accounts. No on-chain addresses named (centralized
> brokerage; effect is the US service termination, not an on-chain freeze).

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `direct` · Δt = 360h

**Event label**: `tradestation_terminates_all_us_crypto_products_after_sec_order`

**Timestamp**: `2024-02-22 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_legal`**
  - URL: <https://www.sec.gov/newsroom/press-releases/2024-16>
  - Wayback: <https://web.archive.org/web/20241202223813/https://www.sec.gov/newsroom/press-releases/2024-16>
  - body_hash: `sha256:1957374f06ba27a4bd1967879a822a3419546271a25b2e37c4c43266e4f3988e`
  - body_path: `sources/http_captures/sec-tradestation-crypto-lending-cease-2024-02/primary/web.archive.org__web-20240208000000-https-www.sec.gov-newsroom-press-releases-2024-16__eacc05bdc3.html`
  > SEC press release 2024-16: the SEC's unregistered-securities
> order against the crypto-asset lending product accompanied
> TradeStation's announced termination of all its US crypto
> products and services on 2024-02-22. attribution=direct: the SEC
> press release is the named state instrument and itself states the
> US-market service termination in the same document (the actor's
> release directly references the restriction outcome).

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `a331305`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

