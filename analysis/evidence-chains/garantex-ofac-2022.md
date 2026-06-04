# Evidence chain — `garantex-ofac-2022`

**Status**: `admitted` · **Stratum**: `S1_ofac_sdn` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-05` · **Source commit**: `5fba5c6` · **Schema**: `0.2.0` · **Event last_verified**: `2026-06-02` · **Tool version**: `0.1.0` · **Generated**: `2026-06-05T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "OFAC/Treasury's 2022-04-05 designation of Garantex documents a
> Russia-operated virtual-currency exchange SDN and directly constrains
> U.S.-person dealings with the venue. This release treats the row as a
> venue/off-ramp legal-constraint datapoint only. It does not claim an
> ISP/DNS block, garantex.io frontend takedown or persistence outcome,
> issuer-side token freeze, consensus-layer filtering, or RPC filtering."

## 1. Trigger

- **Type**: `ofac_sdn_designation`
- **Actor**: `US_OFAC`
- **Timestamp**: `2022-04-05 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://ofac.treasury.gov/recent-actions/20220405>
  - Wayback: <https://web.archive.org/web/20260421105315/https://ofac.treasury.gov/recent-actions/20220405>
  - body_hash: `sha256:540aea9310913b96971bd7351997b4acdc869ca53b9f5c1b94914c3385d3dcc1`
  - body_path: `sources/http_captures/garantex-ofac-2022/backfill-1.3/ofac.treasury.gov__recent-actions-20220405__594c05f6bc.html`
  > OFAC Recent Actions entry for the 2022-04-05 Garantex designation
- **`primary_legal`**
  - URL: <https://home.treasury.gov/news/press-releases/jy0701>
  - Wayback: <https://web.archive.org/web/20260421105351/https://home.treasury.gov/news/press-releases/jy0701>
  - body_hash: `sha256:0dfef579a81b5d191a82e76f2be1fedec10dbf1192665d69584501cee46f22cd`
  - body_path: `sources/http_captures/garantex-ofac-2022/backfill-1.3/home.treasury.gov__news-press-releases-jy0701__1d13c92377.html`
  > Treasury press release announcing sanctions on Hydra and Garantex

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `complete`
- **Chains**: `bitcoin`, `ethereum`
- **Canonical domains**: `garantex.io`

> Single named entity (Garantex) fully specified; associated SDN address set is not enumerated at this event level.

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `direct` · Δt = Noneh

**Event label**: `exchange_designated_and_operations_constrained`

**Timestamp**: `2022-04-05 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_legal`**
  - URL: <https://ofac.treasury.gov/recent-actions/20220405>
  - Wayback: <https://web.archive.org/web/20260421105315/https://ofac.treasury.gov/recent-actions/20220405>
  - body_hash: `sha256:540aea9310913b96971bd7351997b4acdc869ca53b9f5c1b94914c3385d3dcc1`
  - body_path: `sources/http_captures/garantex-ofac-2022/backfill-1.3/ofac.treasury.gov__recent-actions-20220405__594c05f6bc.html`
  > OFAC designation entry listing Garantex and associated addresses
- **`primary_legal`**
  - URL: <https://home.treasury.gov/news/press-releases/jy0701>
  - Wayback: <https://web.archive.org/web/20260421105351/https://home.treasury.gov/news/press-releases/jy0701>
  - body_hash: `sha256:0dfef579a81b5d191a82e76f2be1fedec10dbf1192665d69584501cee46f22cd`
  - body_path: `sources/http_captures/garantex-ofac-2022/backfill-1.3/home.treasury.gov__news-press-releases-jy0701__1d13c92377.html`
  > Treasury press release describing Garantex as a ransomware-enabling virtual currency exchange

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `5fba5c6`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

