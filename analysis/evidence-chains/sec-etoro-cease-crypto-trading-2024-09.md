# Evidence chain — `sec-etoro-cease-crypto-trading-2024-09`

**Status**: `admitted` · **Stratum**: `S3_doj_sec_cftc_fiod` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-02` · **Source commit**: `038e378` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-31` · **Tool version**: `0.1.0` · **Generated**: `2026-06-02T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "The 2024-09-12 SEC settlement (press release 2024-125) forced eToro USA to
> cease trading in nearly all crypto assets for US customers (restricting to
> BTC/BCH/ETH + liquidating other holdings within ~180 days; cease-and-desist
> + $1.5M): a single-layer offramp_cex delisting/restriction on a legitimate
> US trading platform, attribution=direct. comparable_main tier."

## 1. Trigger

- **Type**: `sec_action`
- **Actor**: `US_SEC`
- **Timestamp**: `2024-09-12 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://www.sec.gov/newsroom/press-releases/2024-125>
  - Wayback: <https://web.archive.org/web/20240912140445/https://www.sec.gov/newsroom/press-releases/2024-125>
  - body_hash: `sha256:e0308b141b3c67a33041186574d9450d15c89aa275729e4811eb19e4bdcdbdd5`
  - body_path: `sources/http_captures/sec-etoro-cease-crypto-trading-2024-09/primary/web.archive.org__web-20240912000000-https-www.sec.gov-newsroom-press-releases-2024-125__41be25e11d.html`
  > SEC press release 2024-125 (2024-09-12): "eToro Reaches Settlement
> with SEC and Will Cease Trading Activity in Nearly All Crypto Assets."
> eToro USA LLC settled charges of operating as an unregistered broker
> and clearing agency, agreed to a cease-and-desist plus a $1.5M penalty,
> and agreed to cease trading in nearly all crypto assets for US
> customers — restricting them to Bitcoin, Bitcoin Cash, and Ether — and
> to liquidate other crypto-asset securities it could not transfer to
> customers within ~180 days. Wayback 20240912140445 pinned. Grep of the
> captured body confirms "eToro", "1.5 million", "Bitcoin",
> "Bitcoin Cash", "Ether", "cease", "liquidate", "180 days", "broker",
> "clearing".

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: eToro USA LLC
- **Canonical domains**: `etoro.com`

> eToro USA LLC and its US crypto-trading service. Marked subset: the named
> operator + its US crypto-trading surface, not an enumerated set of the
> delisted crypto assets or affected customers. The BTC/ETH/BCH whitelist is
> named in the order; the broad set of removed assets is not individually
> enumerated. No on-chain addresses named (a securities cease-and-desist, not
> an on-chain freeze).

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `direct` · Δt = 0h

**Event label**: `sec_settles_etoro_cease_nearly_all_crypto_trading_us_customers`

**Timestamp**: `2024-09-12 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_legal`**
  - URL: <https://www.sec.gov/newsroom/press-releases/2024-125>
  - Wayback: <https://web.archive.org/web/20240912140445/https://www.sec.gov/newsroom/press-releases/2024-125>
  - body_hash: `sha256:e0308b141b3c67a33041186574d9450d15c89aa275729e4811eb19e4bdcdbdd5`
  - body_path: `sources/http_captures/sec-etoro-cease-crypto-trading-2024-09/primary/web.archive.org__web-20240912000000-https-www.sec.gov-newsroom-press-releases-2024-125__41be25e11d.html`
  > SEC press release 2024-125 (2024-09-12): eToro USA settled
> unregistered-broker/clearing-agency charges and agreed to cease
> trading in nearly all crypto assets for US customers (restricting to
> BTC/BCH/ETH) + liquidate other holdings within ~180 days
> (cease-and-desist + $1.5M). attribution=direct: the SEC names the
> specific target (eToro USA) and its crypto-trading service being
> restricted.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `038e378`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

