# Evidence chain — `sichuan-silence-ofac-2024`

**Status**: `admitted` · **Stratum**: `S1_ofac_sdn` · **Shape**: `null_event` (0 changed layer(s): none) · **Tier**: `null_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `ad93b7f` · **Schema**: `0.2.0` · **Event last_verified**: `2026-04-22` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "OFAC designation of Sichuan Silence Info Tech on 2024-12-10 targeted a Chinese
> cybersecurity firm; entity-level with no enumerated on-chain addresses on the RA page.
> Datapoint for the China-cyber-actor class."

## 1. Trigger

- **Type**: `ofac_sdn_designation`
- **Actor**: `US_OFAC`
- **Timestamp**: `2024-12-10 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://ofac.treasury.gov/recent-actions/20241210>
  - Wayback: <https://web.archive.org/web/20260421150212/https://ofac.treasury.gov/recent-actions/20241210>
  - body_hash: `sha256:959ccd0526adb6bd66d8d75daedf3b1701ee7f818f8f6220ef3d7f427bcc1437`
  - body_path: `sources/http_captures/sichuan-silence-ofac-2024/ofac-recent-actions/ofac.treasury.gov__recent-actions-20241210__856b917cb9.html`
  > OFAC Recent Actions page for 2024-12-10. Chinese cybersecurity firm Sichuan Silence
> Information Technology Co., Ltd. + employee GUAN Tianfeng designated for involvement
> in 2020 Sophos firewall exploit campaign. No digital-currency addresses attached
> to the RA page itself (entity-level designation). Tag [CYBER2].
- **`primary_legal`**
  - URL: <https://home.treasury.gov/news/press-releases/jy2731>
  > Treasury press release "Treasury Sanctions Cybersecurity Company Involved in Compromise of Firewall Products and Attempted Ransomware Attacks" (2024-12-10).

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: Sichuan Silence Info Tech + GUAN Tianfeng

> Sichuan Silence Information Technology Co., Ltd. (entity) + GUAN Tianfeng (individual).
> No on-chain addresses enumerated on the RA page; SDN XML cross-reference would be
> needed to surface any addresses (if present).

## 3. Changed-layer observations (supports the scoped claim)

*No observed_change entries. This is a `null_event`; see §4 for observed_no_change evidence supporting the null claim.*

## 4. No-change observations (where applicable)

### offramp_cex — `no_public_cex_cascade_documented_in_14d_window`

**Window**: `2024-12-10 00:00:00+00:00` → `2024-12-24 23:59:59+00:00`

**Sources**:

- **`primary_legal`**
  - URL: <https://ofac.treasury.gov/recent-actions/20241210>
  - body_hash: `sha256:959ccd0526adb6bd66d8d75daedf3b1701ee7f818f8f6220ef3d7f427bcc1437`
  - body_path: `sources/http_captures/sichuan-silence-ofac-2024/ofac-recent-actions/ofac.treasury.gov__recent-actions-20241210__856b917cb9.html`
  > No public CEX policy statement referencing Sichuan Silence entity designation (no on-chain addresses) was published by major
> exchanges (Binance, Kraken, Coinbase, Bybit) in the 14-day post-designation
> window. Observation records the absence of public disclosure; private
> chain-analytics flagging workflows (Chainalysis / Elliptic / TRM) are outside
> the scope of this observation and may have produced unpublished KYT flags.

## 5. Honest coverage gaps

- **asset_onchain** (`not_measured`): SDN XML cross-reference pending to determine whether per-entity addresses exist.

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `ad93b7f`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

