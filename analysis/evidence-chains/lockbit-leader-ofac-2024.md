# Evidence chain — `lockbit-leader-ofac-2024`

**Status**: `admitted` · **Stratum**: `S1_ofac_sdn` · **Shape**: `null_event` (0 changed layer(s): none) · **Tier**: `null_case`

**Dataset version**: `0.1.0` · **Dataset cutoff**: `2026-04-22` · **Source commit**: `229adc4` · **Schema**: `0.2.0` · **Event last_verified**: `2026-04-22` · **Tool version**: `0.1.0` · **Generated**: `2026-04-24T03:16:27Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "OFAC individual designation of LockBit leader KHOROSHEV on 2024-05-07 attached 1 BTC
> address. Datapoint in the LockBit cluster (paired with 2024-02-20 affiliates)."

## 1. Trigger

- **Type**: `ofac_sdn_designation`
- **Actor**: `US_OFAC`
- **Timestamp**: `2024-05-07 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://ofac.treasury.gov/recent-actions/20240507>
  - Wayback: <https://web.archive.org/web/20260421144016/https://ofac.treasury.gov/recent-actions/20240507>
  - body_hash: `sha256:ad9801e6a24a935db2ad1619e78e79d6cccb851c98bf312cbaf774e3f992d07e`
  - body_path: `sources/http_captures/lockbit-leader-ofac-2024/ofac-recent-actions/ofac.treasury.gov__recent-actions-20240507__04a826f9a2.html`
  > OFAC Recent Actions page for 2024-05-07. Dmitry KHOROSHEV (aka "LockBitSupp"),
> Russia-based leader of the LockBit ransomware group, designated. 1 XBT address
> attached. Tag [CYBER2]. Follows 2024-02-20 LockBit-affiliates designation + Operation
> Cronos infrastructure takedown — KHOROSHEV was named as the unmasked operator in the
> Cronos follow-on action.
- **`primary_legal`**
  - URL: <https://home.treasury.gov/news/press-releases/jy2328>
  > Treasury press release "United States Sanctions Senior Leader of the LockBit Ransomware Group" (2024-05-07).

## 2. Target

- **Kind**: `address_set`
- **Enumeration**: `complete`
- **Actor name**: Dmitry KHOROSHEV ("LockBitSupp")
- **Chains**: `bitcoin`
- **Addresses**: 1 total (enumerated in event YAML)

> 1 XBT address attached to KHOROSHEV's individual SDN entry.

## 3. Changed-layer observations (supports the scoped claim)

*No observed_change entries. This is a `null_event`; see §4 for observed_no_change evidence supporting the null claim.*

## 4. No-change observations (where applicable)

### offramp_cex — `no_public_cex_cascade_documented_in_14d_window`

**Window**: `2024-05-07 00:00:00+00:00` → `2024-05-21 23:59:59+00:00`

**Sources**:

- **`primary_legal`**
  - URL: <https://ofac.treasury.gov/recent-actions/20240507>
  - body_hash: `sha256:ad9801e6a24a935db2ad1619e78e79d6cccb851c98bf312cbaf774e3f992d07e`
  - body_path: `sources/http_captures/lockbit-leader-ofac-2024/ofac-recent-actions/ofac.treasury.gov__recent-actions-20240507__04a826f9a2.html`
  > No public CEX policy statement referencing KHOROSHEV's 1 BTC address was published by major
> exchanges (Binance, Kraken, Coinbase, Bybit) in the 14-day post-designation
> window. Observation records the absence of public disclosure; private
> chain-analytics flagging workflows (Chainalysis / Elliptic / TRM) are outside
> the scope of this observation and may have produced unpublished KYT flags.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`lockbit-affiliates-ofac-2024`](./lockbit-affiliates-ofac-2024.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.1.0` (commit `229adc4`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

