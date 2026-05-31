# Evidence chain — `russia-election-interference-ofac-2020`

**Status**: `admitted` · **Stratum**: `S1_ofac_sdn` · **Shape**: `comparison` (1 changed layer(s): `asset_onchain`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `661a63f` · **Schema**: `0.2.0` · **Event last_verified**: `2026-04-22` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "OFAC designation of Russia-linked election interference actors on 2020-09-10 attached 23
> addresses across 6 chains. Demonstrates early OFAC reach across multiple cryptocurrencies
> for individual-level sanctions. Cross-layer measurable only at asset_onchain (3 ETH
> addresses) and offramp_cex layers, both currently unqueried."

## 1. Trigger

- **Type**: `ofac_sdn_designation`
- **Actor**: `US_OFAC`
- **Timestamp**: `2020-09-10 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://ofac.treasury.gov/recent-actions/20200910>
  - Wayback: <https://web.archive.org/web/20260421143427/https://ofac.treasury.gov/recent-actions/20200910>
  - body_hash: `sha256:a29b443ab573d519e2fceb7c7b2b51e60f3ed9d6322b04f8f9e985ad2355d4ef`
  - body_path: `sources/http_captures/russia-election-interference-ofac-2020/ofac-recent-actions/ofac.treasury.gov__recent-actions-20200910__733f4c16cb.html`
  > OFAC Recent Actions page for 2020-09-10. Russia-linked election interference actors,
> primarily individuals associated with the Internet Research Agency: ANDREYEV,
> ASLANOVA, DERKACH, LIFSHITS, and others. Addresses span 6 chains: XBT×14, ETH×3,
> LTC×3, ZEC×1, BSV×1, DASH×1 (23 total). Tags [CYBER2] [ELECTION-EO13848].
- **`primary_legal`**
  - URL: <https://home.treasury.gov/news/press-releases/sm1118>
  > Treasury press release "Treasury Sanctions Russia-Linked Election Interference Actors" (2020-09-10).

## 2. Target

- **Kind**: `address_set`
- **Enumeration**: `complete`
- **Actor name**: Russia-linked election interference actors
- **Chains**: `bitcoin`, `ethereum`, `litecoin`, `zcash`, `bitcoin_sv`, `dash`
- **Addresses**: 23 total (enumerated in event YAML)

> 23 unique addresses across 6 chains distributed across 4 individuals (primarily ANDREYEV and LIFSHITS who carry most addresses).

## 3. Changed-layer observations (supports the scoped claim)

### asset_onchain · attribution: `direct` · Δt = 13560.82h

**Event label**: `circle_blacklist_18_months_after_ofac_designation`

**Timestamp**: `2022-03-29 00:49:00+00:00` (precision: `minute`)

**Sources**:

- **`primary_onchain`**
  - URL: <https://etherscan.io/tx/0x5906c3dac2d75f141b72baa61842a9881e9d31ee36f761ffc7059ffc86c7e452>
  - tx_hash: `0x5906c3dac2d75f141b72baa61842a9881e9d31ee36f761ffc7059ffc86c7e452`
  > USDC Blacklisted() tx for Russia-election ETH address 0x8576... at 2022-03-29 00:49 UTC. Part of Circle 2-address batch 18 months post-OFAC.
- **`primary_corporate`**
  - URL: <https://usdtbanlist.com/address/0x8576acc5c05d6ce88f4e49bf65bdf0c62f91353c>
  - body_hash: `sha256:eb18a808c950839bcd99569230708f68b0fbe8f85c8950deb587d45f9ce44c7b`
  - body_path: `sources/http_captures/russia-election-interference-ofac-2020/asset-layer-check/usdtbanlist.com__address-0x8576acc5c05d6ce88f4e49bf65bdf0c62f91353c.html`
  > Circle USDC blacklisted 2/2 ETH addresses in the Russia-election cluster on
> 2022-03-29 00:49 UTC (identical minute, batch op), ~18 months after the OFAC
> designation. Among the slowest Circle reactions in the dataset — possibly
> reflecting that these individual-designation addresses had no prior USDC
> activity requiring urgent compliance.
- **`primary_corporate`**
  - URL: <https://usdtbanlist.com/address/0x901bb9583b24d97e995513c6778dc6888ab6870e>
  - body_hash: `sha256:20837c17edd081b5988efb870b1db757d483892ac6a03348b16f27b37fa5f17d`
  - body_path: `sources/http_captures/russia-election-interference-ofac-2020/asset-layer-check/usdtbanlist.com__address-0x901bb9583b24d97e995513c6778dc6888ab6870e.html`
  > Second ETH address, same 2022-03-29 00:49 UTC Circle batch.

## 5. Honest coverage gaps

- **offramp_cex** (`not_measured`): Chain-analytics anchors pinned 2026-04-22 as primary_corporate

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `661a63f`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

