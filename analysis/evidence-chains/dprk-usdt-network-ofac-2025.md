# Evidence chain — `dprk-usdt-network-ofac-2025`

**Status**: `admitted` · **Stratum**: `S1_ofac_sdn` · **Shape**: `comparison` (1 changed layer(s): `asset_onchain`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `e443d6f` · **Schema**: `0.2.0` · **Event last_verified**: `2026-04-22` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "OFAC's 2025-11-04 DPRK laundering-network designation attached 53 USDT-TRC20 addresses
> to SDN, giving the first single-token / single-chain target shape in the dataset. Asset-
> layer cascade observation (Tether freeze response) is the natural experiment this event
> sets up; empirical query pending."

## 1. Trigger

- **Type**: `ofac_sdn_designation`
- **Actor**: `US_OFAC`
- **Timestamp**: `2025-11-04 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://ofac.treasury.gov/recent-actions/20251104>
  - Wayback: <https://web.archive.org/web/20260421141948/https://ofac.treasury.gov/recent-actions/20251104>
  - body_hash: `sha256:bb2182e7e64bdcbf5af219ac2475a0ccd8981024d9681675fa9c748dc4694ad7`
  - body_path: `sources/http_captures/dprk-usdt-network-ofac-2025/ofac-recent-actions/ofac.treasury.gov__recent-actions-20251104__f087ecdd9f.html`
  > OFAC Recent Actions page for 2025-11-04. DPRK financial-institution / IT-worker
> laundering network designations including Korea Daesong Bank, Koryo Commercial Bank,
> Foreign Trade Bank of DPRK, Ryujong Credit Bank, Korea Mangyongdae Computer Technology
> Co., and multiple subsidiary entities. **Structurally distinctive: all 53 designated
> digital-currency addresses are USDT on TRON (token prefix 'T...'), with no BTC/ETH
> addresses whatsoever.** Per-token concentration is a paper-worthy shape — the first
> SDN action where the entire on-chain footprint is single-token-on-single-chain.
- **`primary_legal`**
  - URL: <https://home.treasury.gov/news/press-releases/sb0298>
  > Treasury press release "Treasury Sanctions DPRK Bankers and Institutions Involved in Laundering Cybercrime Proceeds and IT Worker Funds" (2025-11-04).

## 2. Target

- **Kind**: `address_set`
- **Enumeration**: `complete`
- **Actor name**: DPRK Laundering Network
- **Chains**: `tron`
- **Addresses**: 53 total (enumerated in event YAML)

> 53 unique USDT-on-TRON addresses across multiple DPRK-related entity SDN entries. Zero BTC/ETH/other-chain addresses on the page.

## 3. Changed-layer observations (supports the scoped claim)

### asset_onchain · attribution: `direct` · Δt = 21.63h

**Event label**: `tether_ofac_day_reactive_freeze_28_of_53_addresses`

**Timestamp**: `2025-11-04 21:38:00+00:00` (precision: `minute`)

**Sources**:

- **`primary_onchain`**
  - URL: <https://tronscan.org/#/transaction/713fe39c5d578c1db8a754ce9d30e43ec41fabe19e02a833f943657df08a74e5>
  - tx_hash: `713fe39c5d578c1db8a754ce9d30e43ec41fabe19e02a833f943657df08a74e5`
  > Tether USDT-TRC20 addBlackList tx on TRON for DPRK address TA39q3p75XRSWYAEaSF7dANtyksoa3sLge at 2025-11-04 21:38 UTC (one of 28-batch OFAC-day reactive).
- **`primary_corporate`**
  - URL: <https://usdtbanlist.com/address/TA3941uFAvmVibSkQ6fMJXxmaSNovX86mz>
  - body_hash: `sha256:5d6317eb4970c6d1f570dc8b37892db66664fd3fab838a1ce879341facf32e50`
  - body_path: `sources/http_captures/dprk-usdt-network-ofac-2025/asset-layer-check/usdtbanlist.com__address-TA3941uFAvmVibSkQ6fMJXxmaSNovX86mz__a69f3029ba.html`
  > Full 53-address scan summary (sources/asset_layer_scan/
> dprk-usdt-network-ofac-2025.json): of 53 addresses, **28 were frozen by Tether
> on 2025-11-04 21:38-21:39 UTC (same day as OFAC designation, ~21 hours after
> the day began)**. This batch constitutes an OFAC-day reactive freeze with
> direct attribution. Individual address HTML captures per-address under
> sources/http_captures/.../asset-layer-check/.
- **`primary_corporate`**
  - URL: <https://usdtbanlist.com/address/TYxwUhoLPF7AgfG9GaXFEp8CQi8K8KG1m3>
  - body_hash: `sha256:200f60acba98b02da2d51134a4d5b8b731d571ebde3c95bea99402e52462300b`
  - body_path: `sources/http_captures/dprk-usdt-network-ofac-2025/asset-layer-check/usdtbanlist.com__address-TYxwUhoLPF7AgfG9GaXFEp8CQi8K8KG1m3__f1f6804eff.html`
  > Second-sampled-address archival anchor. Note this specific address was in the
> PRE-OFAC batch (2025-04-30 07:05 UTC) rather than the OFAC-day reactive batch;
> retained as part of the 53-address scan body-hash evidence group.

## 4. No-change observations (where applicable)

### asset_onchain — `tether_pre_ofac_intelligence_freeze_25_of_53_addresses`

**Window**: `2025-11-04 00:00:00+00:00` → `2025-11-18 23:59:59+00:00`

**Sources**:

- **`primary_onchain`**
  - URL: <https://tronscan.org/#/transaction/29c22d0444c84f77a861064285093eb005cef4ffd656944645766480bcd0bc78>
  - tx_hash: `29c22d0444c84f77a861064285093eb005cef4ffd656944645766480bcd0bc78`
  > Tether USDT-TRC20 addBlackList tx for DPRK address TA3941uF... at 2025-04-30 07:05 UTC — 188 days pre-OFAC. Cross-chain anchor for the pre-OFAC cohort; see also ce364ad921e0a531371a8f5be7ccbba7f971e90d0460a76298b51219370b6434 for the 2025-05-08 10:20 UTC batch.
- **`primary_corporate`**
  - URL: <https://usdtbanlist.com/address/TA3941uFAvmVibSkQ6fMJXxmaSNovX86mz>
  - body_hash: `sha256:5d6317eb4970c6d1f570dc8b37892db66664fd3fab838a1ce879341facf32e50`
  - body_path: `sources/http_captures/dprk-usdt-network-ofac-2025/asset-layer-check/usdtbanlist.com__address-TA3941uFAvmVibSkQ6fMJXxmaSNovX86mz__a69f3029ba.html`
  > Of the 53 designated addresses, **25 were already frozen by Tether in batches
> on 2025-04-30 (17 addresses at 07:04-07:05 UTC) and 2025-05-08 (8 addresses at
> 10:20-10:21 UTC) — 180-188 days BEFORE the OFAC designation**. For this cohort
> the 2025-11-04 designation produced no incremental Tether action: they were
> already in the frozen state. See tether-dprk-precommit-freeze-2025 for the
> cross-linked pre-OFAC freeze event anchoring those two batches.
- **`primary_legal`**
  - URL: <https://ofac.treasury.gov/recent-actions/20251104>
  - body_hash: `sha256:bb2182e7e64bdcbf5af219ac2475a0ccd8981024d9681675fa9c748dc4694ad7`
  - body_path: `sources/http_captures/dprk-usdt-network-ofac-2025/ofac-recent-actions/ofac.treasury.gov__recent-actions-20251104__f087ecdd9f.html`
  > OFAC SDN entry as the legal reference-point.

## 5. Honest coverage gaps

- **offramp_cex** (`not_measured`): Chain-analytics anchors pinned 2026-04-22 as primary_corporate

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `e443d6f`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

