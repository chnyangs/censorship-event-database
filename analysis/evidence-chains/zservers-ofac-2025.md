# Evidence chain — `zservers-ofac-2025`

**Status**: `admitted` · **Stratum**: `S1_ofac_sdn` · **Shape**: `null_event` (0 changed layer(s): none) · **Tier**: `null_case`

**Dataset version**: `0.2.0-rc-dryrun-8` · **Dataset cutoff**: `2026-05-16` · **Source commit**: `f18bc7a` · **Schema**: `0.2.0` · **Event last_verified**: `2026-04-22` · **Tool version**: `0.1.0` · **Generated**: `2026-05-22T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "Joint US/UK/AU OFAC designation of Zservers on 2025-02-11 attached 4 BTC addresses.
> Infrastructure-provider target with limited cross-layer measurable surface."

## 1. Trigger

- **Type**: `ofac_sdn_designation`
- **Actor**: `US_OFAC`
- **Timestamp**: `2025-02-11 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://ofac.treasury.gov/recent-actions/20250211>
  - Wayback: <https://web.archive.org/web/20260421144035/https://ofac.treasury.gov/recent-actions/20250211>
  - body_hash: `sha256:b00e6923a6af0d7887fd2a92d2ab3520939c451ebcc1bdfea43589dbcdd0879f`
  - body_path: `sources/http_captures/zservers-ofac-2025/ofac-recent-actions/ofac.treasury.gov__recent-actions-20250211__478b1f5c3d.html`
  > OFAC Recent Actions page for 2025-02-11. Joint US/UK/Australia action against Russian
> bulletproof-hosting provider ZSERVERS + operators KOLESNIKOV Alexander / MISHIN
> Alexander (aka ALEX560560 / TRIPLEX560 / etc.). 4 XBT addresses attached. Tag [CYBER3].
- **`primary_legal`**
  - URL: <https://home.treasury.gov/news/press-releases/sb0012>
  > Treasury press release "United States, Australia, and the United Kingdom Jointly Sanction Key Infrastructure that Enables Ransomware Actors" (2025-02-11).

## 2. Target

- **Kind**: `address_set`
- **Enumeration**: `complete`
- **Actor name**: Zservers
- **Chains**: `bitcoin`
- **Addresses**: 4 total (enumerated in event YAML)

> 4 unique XBT addresses attached to the ZSERVERS / MISHIN / KOLESNIKOV SDN entries.

## 3. Changed-layer observations (supports the scoped claim)

*No observed_change entries. This is a `null_event`; see §4 for observed_no_change evidence supporting the null claim.*

## 4. No-change observations (where applicable)

### offramp_cex — `no_public_cex_cascade_documented_in_14d_window`

**Window**: `2025-02-11 00:00:00+00:00` → `2025-02-25 23:59:59+00:00`

**Sources**:

- **`primary_legal`**
  - URL: <https://ofac.treasury.gov/recent-actions/20250211>
  - body_hash: `sha256:b00e6923a6af0d7887fd2a92d2ab3520939c451ebcc1bdfea43589dbcdd0879f`
  - body_path: `sources/http_captures/zservers-ofac-2025/ofac-recent-actions/ofac.treasury.gov__recent-actions-20250211__478b1f5c3d.html`
  > No public CEX policy statement referencing Zservers 4 BTC addresses was published by major
> exchanges (Binance, Kraken, Coinbase, Bybit) in the 14-day post-designation
> window. Observation records the absence of public disclosure; private
> chain-analytics flagging workflows (Chainalysis / Elliptic / TRM) are outside
> the scope of this observation and may have produced unpublished KYT flags.

## 5. Honest coverage gaps

- **l0_network** (`not_measured`): No OONI / Censored Planet query attempted for hosting-related domains within the event window; substrate-shaped gap, not a coverage_gap observation. Sibling `sinbad-ofac-2023` sets the L0-honesty bar with an attested OONI-negative query — applying the same standard would require either an OONI/CP probe of `zservers.ru` or an explicit "no domain to probe" justification.

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-8` (commit `f18bc7a`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

