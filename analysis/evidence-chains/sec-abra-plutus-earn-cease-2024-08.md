# Evidence chain — `sec-abra-plutus-earn-cease-2024-08`

**Status**: `admitted` · **Stratum**: `S3_doj_sec_cftc_fiod` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `db44253` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-31` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T04:52:47Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "The 2024-08-26 SEC settlement (press release 2024-105) charging Plutus
> Lending (Abra) with unregistered offers/sales of Abra Earn crypto-asset
> securities forced the wind-down of the Abra Earn product for US customers
> (permanent injunction + civil penalty): a single-layer offramp_cex
> restriction on a legitimate crypto yield/off-ramp product,
> attribution=direct. comparable_main tier."

## 1. Trigger

- **Type**: `sec_action`
- **Actor**: `US_SEC`
- **Timestamp**: `2024-08-26 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://www.sec.gov/newsroom/press-releases/2024-105>
  - Wayback: <https://web.archive.org/web/20240826192230/https://www.sec.gov/newsroom/press-releases/2024-105>
  - body_hash: `sha256:f4ac516f0c286dd3536cdacc3c5c6229f409f57b7dd48063e15b871e8609f4c4`
  - body_path: `sources/http_captures/sec-abra-plutus-earn-cease-2024-08/primary/web.archive.org__web-20240826000000-https-www.sec.gov-newsroom-press-releases-2024-105__9f043af52e.html`
  > SEC press release 2024-105 (2024-08-26): "SEC Charges Abra with
> Unregistered Offers and Sales of Crypto Asset Securities." The SEC
> charged Plutus Lending, LLC (d/b/a Abra) over the Abra Earn retail
> crypto-lending product — investors tendered crypto for Abra's promise
> to pay a variable return — as unregistered securities and an
> unregistered investment company. Abra began winding down Abra Earn for
> US customers. Wayback 20240826192230 pinned. Grep of the captured body
> confirms "Abra Earn", "Plutus", "winding down",
> "500 million", "600 million", "investment company", "Unregistered".

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: Plutus Lending LLC (Abra)
- **Canonical domains**: `abra.com`

> Plutus Lending, LLC (d/b/a Abra) and the Abra Earn retail crypto-lending
> product. Marked subset: the named operator + the Earn product, not an
> enumerated set of Earn depositors. No on-chain addresses named in the
> order (a securities/investment-company action against the operator, not an
> on-chain freeze).

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `direct` · Δt = 0h

**Event label**: `sec_settles_abra_earn_unregistered_securities_us_wind_down`

**Timestamp**: `2024-08-26 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_legal`**
  - URL: <https://www.sec.gov/newsroom/press-releases/2024-105>
  - Wayback: <https://web.archive.org/web/20240826192230/https://www.sec.gov/newsroom/press-releases/2024-105>
  - body_hash: `sha256:f4ac516f0c286dd3536cdacc3c5c6229f409f57b7dd48063e15b871e8609f4c4`
  - body_path: `sources/http_captures/sec-abra-plutus-earn-cease-2024-08/primary/web.archive.org__web-20240826000000-https-www.sec.gov-newsroom-press-releases-2024-105__9f043af52e.html`
  > SEC press release 2024-105 (2024-08-26): Plutus Lending (Abra)
> charged/settled over unregistered Abra Earn crypto-asset securities;
> Abra wound down Abra Earn for US customers. attribution=direct: the
> SEC names the specific target (Plutus Lending / Abra Earn) being
> restricted.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `db44253`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

