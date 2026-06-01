# Evidence chain — `sec-tokenlot-unregistered-broker-2018-09`

**Status**: `admitted` · **Stratum**: `S3_doj_sec_cftc_fiod` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `08e3573` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-31` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T05:04:01Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "The 2018-09-11 SEC settled order against TokenLot LLC (the 'ICO Superstore')
> and its owners for unregistered broker-dealer activity forced the secondary-
> token trading platform to wind down and ordered destruction of its remaining
> digital-asset inventory. Effect carried at offramp_cex (token-trading surface
> shutdown), attribution=direct. Comparable-main tier."

## 1. Trigger

- **Type**: `sec_action`
- **Actor**: `US_SEC`
- **Timestamp**: `2018-09-11 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_government`**
  - URL: <https://web.archive.org/web/20181001000000/https://www.sec.gov/news/press-release/2018-185>
  - Wayback: <https://web.archive.org/web/20180918060505/https://www.sec.gov/news/press-release/2018-185>
  - body_hash: `sha256:cb8bea72cdfe48dfc8ae7bfd30c99868d12adb61100442231b864700606b9711`
  - body_path: `sources/http_captures/sec-tokenlot-unregistered-broker-2018-09/primary/web.archive.org__web-20181001000000-https-www.sec.gov-news-press-release-2018-185__25dbcfa7c3.html`
  > SEC press release 2018-185 (2018-09-11): "SEC Charges ICO Superstore
> and Owners With Operating As Unregistered Broker-Dealers." The settled
> cease-and-desist order found that TokenLot LLC (a self-described "ICO
> Superstore") and owners Lenny Kugel and Eli L. Lewitt acted as
> unregistered broker-dealers, taking orders from 6,100+ retail investors
> and handling 200+ different digital tokens (including securities).
> Settlement: $471,000 disgorgement + interest, owner penalties, industry
> and penny-stock bars, AND retention of an independent third party to
> destroy TokenLot's remaining inventory of digital assets. TokenLot is
> winding down. First SEC case charging unregistered broker-dealers for
> selling digital tokens after the 2017 DAO Report. Wayback memento
> 20180918060505 pinned; captured body contains "TokenLot", "ICO
> Superstore", "broker-dealer", "winding down", "6,100", "200 different".

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: TokenLot LLC (Kugel / Lewitt)
- **Canonical domains**: `tokenlot.com`

> TokenLot LLC (Michigan-based "ICO Superstore" secondary-token trading
> platform) and its two owners Lenny Kugel and Eli L. Lewitt. Subset: the
> named corporate vehicle + two named principals, not an enumerated set of
> the 6,100+ retail customers or 200+ token issuers transacted.

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `direct` · Δt = 0h

**Event label**: `tokenlot_token_trading_platform_wound_down_inventory_destroyed`

**Timestamp**: `2018-09-11 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_government`**
  - URL: <https://web.archive.org/web/20181001000000/https://www.sec.gov/news/press-release/2018-185>
  - Wayback: <https://web.archive.org/web/20180918060505/https://www.sec.gov/news/press-release/2018-185>
  - body_hash: `sha256:cb8bea72cdfe48dfc8ae7bfd30c99868d12adb61100442231b864700606b9711`
  - body_path: `sources/http_captures/sec-tokenlot-unregistered-broker-2018-09/primary/web.archive.org__web-20181001000000-https-www.sec.gov-news-press-release-2018-185__25dbcfa7c3.html`
  > SEC press release 2018-185 (2018-09-11). attribution=direct: the SEC's
> own settled order is the operative instrument that ended TokenLot's
> service (winding down) and ordered destruction of its remaining
> digital-asset inventory, and the order names TokenLot LLC and its two
> owners directly.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`sec-etherdelta-coburn-unregistered-exchange-2018-11`](./sec-etherdelta-coburn-unregistered-exchange-2018-11.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `08e3573`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

