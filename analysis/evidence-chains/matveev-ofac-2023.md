# Evidence chain — `matveev-ofac-2023`

**Status**: `admitted` · **Stratum**: `S1_ofac_sdn` · **Shape**: `null_event` (0 changed layer(s): none) · **Tier**: `null_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `97f58fa` · **Schema**: `0.2.0` · **Event last_verified**: `2026-04-22` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "OFAC designation of WAZAWAKA/Matveev on 2023-05-16 targeted a Russian ransomware
> individual. Per-address cross-reference to SDN XML pending; cross-layer observations
> limited by individual-level targeting."

## 1. Trigger

- **Type**: `ofac_sdn_designation`
- **Actor**: `US_OFAC`
- **Timestamp**: `2023-05-16 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://ofac.treasury.gov/recent-actions/20230516>
  - Wayback: <https://web.archive.org/web/20260421145250/https://ofac.treasury.gov/recent-actions/20230516>
  - body_hash: `sha256:b6786db721a64066b90f9d3e975cf7ca67440ab122ec338efd67a53850327b1c`
  - body_path: `sources/http_captures/matveev-ofac-2023/ofac-recent-actions/ofac.treasury.gov__recent-actions-20230516__215bc3f851.html`
  > OFAC Recent Actions page for 2023-05-16. Mikhail MATVEEV (aka WAZAWAKA / BORISELCIN /
> UHODIRANSOMWAR / M1X), Russia-based ransomware individual (Babuk / Hive / LockBit
> affiliate). No digital-currency addresses attached to the RA page itself (addresses
> would be in the SDN XML entry). Tag [CYBER2].
- **`primary_legal`**
  - URL: <https://home.treasury.gov/news/press-releases/jy1455>
  > Treasury press release "Treasury Sanctions Russian Ransomware Actor Complicit in Attacks on Police and U.S. Critical Infrastructure" (2023-05-16).

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: Mikhail Matveev (WAZAWAKA)

> Individual designation of Mikhail Matveev. No digital-currency addresses on the
> Recent Actions page; per-address SDN XML cross-reference would be needed to produce
> an address_set.

## 3. Changed-layer observations (supports the scoped claim)

*No observed_change entries. This is a `null_event`; see §4 for observed_no_change evidence supporting the null claim.*

## 4. No-change observations (where applicable)

### offramp_cex — `no_public_cex_cascade_documented_in_14d_window`

**Window**: `2023-05-16 00:00:00+00:00` → `2023-05-30 23:59:59+00:00`

**Sources**:

- **`primary_legal`**
  - URL: <https://ofac.treasury.gov/recent-actions/20230516>
  - body_hash: `sha256:b6786db721a64066b90f9d3e975cf7ca67440ab122ec338efd67a53850327b1c`
  - body_path: `sources/http_captures/matveev-ofac-2023/ofac-recent-actions/ofac.treasury.gov__recent-actions-20230516__215bc3f851.html`
  > No public CEX policy statement referencing Matveev (WAZAWAKA) individual designation was published by major
> exchanges (Binance, Kraken, Coinbase, Bybit) in the 14-day post-designation
> window. Observation records the absence of public disclosure; private
> chain-analytics flagging workflows (Chainalysis / Elliptic / TRM) are outside
> the scope of this observation and may have produced unpublished KYT flags.

## 5. Honest coverage gaps

- **asset_onchain** (`not_measured`): SDN XML addresses (not on RA page) would be cross-referenced to run freeze queries.

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `97f58fa`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

