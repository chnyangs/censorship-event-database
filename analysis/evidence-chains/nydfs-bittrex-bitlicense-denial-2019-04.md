# Evidence chain — `nydfs-bittrex-bitlicense-denial-2019-04`

**Status**: `admitted` · **Stratum**: `S4_nation_state` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-08` · **Source commit**: `ee7bf1a` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-31` · **Tool version**: `0.1.0` · **Generated**: `2026-06-25T23:48:26Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "On 2019-04-10 NYDFS denied Bittrex, Inc.'s New York virtual-currency and
> money-transmission license applications and required Bittrex, effective
> 2019-04-11, to cease operating in New York and wind down its New York
> business within 60 days. The event is modeled only as a state-regulator
> exchange/off-ramp restriction for New York residents; no L0/L1/L3/L4 or
> asset-onchain effect is claimed."

## 1. Trigger

- **Type**: `regulatory_enforcement`
- **Actor**: `US_NYDFS`
- **Timestamp**: `2019-04-10 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_government`**
  - URL: <https://www.dfs.ny.gov/reports_and_publications/press_releases/pr1904101>
  - body_hash: `sha256:89f736f0b629a5508e964a52c891964514094cd233aa1d4fa74995bedd1855d0`
  - body_path: `sources/http_captures/nydfs-bittrex-bitlicense-denial-2019-04/primary/www.dfs.ny.gov__reports_and_publications-press_releases-pr1904101__4656340989.html`
  > NYDFS press release dated 2019-04-10 announcing denial of Bittrex,
> Inc.'s applications for New York virtual-currency-business and money-
> transmission licenses. The captured body states that Bittrex had about
> 35,000 New York consumers and that, effective 2019-04-11, Bittrex must
> immediately cease operating in New York State and, within 60 days,
> wind down its New York business, including transferring positions and
> transactions and providing safe custody of New York resident assets.
- **`primary_legal`**
  - URL: <https://www.dfs.ny.gov/system/files/documents/2019/04/dfs-bittrex-letter-41019.pdf>
  - body_hash: `sha256:8f7cbaa0bfdcb6bc43eedc644e013b817918efcd5cebf25e3faa10a20838b251`
  - body_path: `sources/http_captures/nydfs-bittrex-bitlicense-denial-2019-04/primary/www.dfs.ny.gov__system-files-documents-2019-04-dfs-bittrex-letter-41019.pdf__e23b8845b4.bin`
  > Official NYDFS denial-letter PDF linked from the press release and
> captured locally. The HTML press release is the grep-verified text
> anchor for the wind-down dates and consumer count; the letter is kept
> as the underlying legal-action artifact.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `complete`
- **Actor name**: Bittrex, Inc. New York operations
- **Canonical domains**: `bittrex.com`

> Bittrex, Inc. New York virtual currency and money-transmission activity.
> The NYDFS action is entity-specific: it denies Bittrex's license
> applications and orders Bittrex to cease New York operations and wind down
> business with New York residents. It is not a class-wide BitLicense event.

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `direct` · Δt = 24h

**Event label**: `bittrex_new_york_operations_cease_and_60_day_wind_down`

**Timestamp**: `2019-04-11 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_government`**
  - URL: <https://www.dfs.ny.gov/reports_and_publications/press_releases/pr1904101>
  - body_hash: `sha256:89f736f0b629a5508e964a52c891964514094cd233aa1d4fa74995bedd1855d0`
  - body_path: `sources/http_captures/nydfs-bittrex-bitlicense-denial-2019-04/primary/www.dfs.ny.gov__reports_and_publications-press_releases-pr1904101__4656340989.html`
  > NYDFS states that Bittrex must immediately cease operating in New
> York effective 2019-04-11 and wind down within 60 days. attribution
> is direct because the regulator's own action names the entity and the
> required operational cessation.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`nydfs-bitlicense-2015-06`](./nydfs-bitlicense-2015-06.md)
- [`sec-v-bittrex-2023`](./sec-v-bittrex-2023.md)
- `bittrex-global-shutdown-2023-11` (rejected; no rendered admitted-chain link)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `ee7bf1a`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

