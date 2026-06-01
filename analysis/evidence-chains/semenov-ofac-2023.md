# Evidence chain — `semenov-ofac-2023`

**Status**: `admitted` · **Stratum**: `S1_ofac_sdn` · **Shape**: `comparison` (1 changed layer(s): `asset_onchain`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `029a430` · **Schema**: `0.2.0` · **Event last_verified**: `2026-04-21` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T14:19:21Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "Individual OFAC designation of Roman Semenov on
> 2023-08-23 did not produce a measurable step change in Ethereum OFAC-compliant relay share
> (37.03% event day; 39.57% ± 1.27 post-event 14d; 38.45% ± 0.96 pre-event 14d)." Other layers
> remain scoped for follow-up.

## 1. Trigger

- **Type**: `ofac_sdn_designation`
- **Actor**: `US_OFAC`
- **Timestamp**: `2023-08-23 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://ofac.treasury.gov/recent-actions/20230823>
  - Wayback: <https://web.archive.org/web/20260421132042/https://ofac.treasury.gov/recent-actions/20230823>
  - body_hash: `sha256:e737ce9ccd1c0df53d103f6bd89836357112eddc8cf1df504d522a4189cce02a`
  - body_path: `sources/http_captures/semenov-ofac-2023/ofac-recent-actions/ofac.treasury.gov__recent-actions-20230823__371ac1b7ba.html`
  > OFAC Recent Actions page for 2023-08-23. The individual designation of Roman Semenov
> (Tornado Cash co-founder; Dubai, UAE; DOB 1987-11-08; [DPRK3] [CYBER2] tags) includes
> 8 ETH addresses extracted verbatim from this archived page. Same-day companion action:
> DOJ SDNY indictment of Roman Storm + Roman Semenov (see related DOJ event — not yet
> admitted as a separate S3 entry).
- **`primary_legal`**
  - URL: <https://home.treasury.gov/news/press-releases/jy1702>
  > Treasury press release "Treasury Designates Roman Semenov, Co-Founder of Sanctioned Virtual Currency Mixer Tornado Cash" (2023-08-23).

## 2. Target

- **Kind**: `address_set`
- **Enumeration**: `complete`
- **Protocol**: `tornado_cash`
- **Actor name**: Roman Semenov
- **Chains**: `ethereum`
- **Addresses**: 8 total (enumerated in event YAML)
- **Canonical domains**: `tornado.cash`, `app.tornado.cash`

> Full set of 8 unique Ethereum addresses attached to the Roman Semenov individual SDN entry,
> extracted verbatim from the OFAC Recent Actions page for 2023-08-23 (see trigger.citation[0]).
> Address casing preserved as published by OFAC. Target is an individual (Semenov) rather than
> a protocol; the canonical_domains list carries the Tornado Cash context for cross-layer
> reasoning.

## 3. Changed-layer observations (supports the scoped claim)

### asset_onchain · attribution: `direct` · Δt = 24.27h

**Event label**: `circle_blacklist_all_8_eth_addresses_within_24h`

**Timestamp**: `2023-08-24 00:16:00+00:00` (precision: `minute`)

**Sources**:

- **`primary_onchain`**
  - URL: <https://etherscan.io/tx/0xe5e3264f0cb5558f2011b65ed231656870ad217e55eff924193860753091448a>
  - tx_hash: `0xe5e3264f0cb5558f2011b65ed231656870ad217e55eff924193860753091448a`
  > USDC Blacklisted() tx for Semenov address 0xdcbEfFBECc... at 2023-08-24 00:16 UTC. First of an 8-address Circle batch executed over 00:16-00:20 UTC on the day after OFAC designation.
- **`primary_corporate`**
  - URL: <https://usdtbanlist.com/address/0x43fa21d92141BA9db43052492E0DeEE5aa5f0A93>
  - body_hash: `sha256:f61b000c0d33c7d2c8094af44eb65f8ece4829b9831c16ae107c916c3a1718e0`
  - body_path: `sources/http_captures/semenov-ofac-2023/asset-layer-check/usdtbanlist.com__address-0x43fa21d92141BA9db43052492E0DeEE5aa5f0A93.html`
  > Aggregated freeze data across all 8 Semenov ETH addresses. Circle USDC freeze
> timestamps: all within 4 minutes on 2023-08-24 (00:16, 00:17, 00:18, 00:19×2,
> 00:20). Archive anchor covers the cohort; per-address captures at
> sources/http_captures/semenov-ofac-2023/asset-layer-check/.

### asset_onchain · attribution: `direct` · Δt = 2596.62h

**Event label**: `tether_retroactive_sweep_semenov_addresses`

**Timestamp**: `2023-12-09 04:37:00+00:00` (precision: `minute`)

**Sources**:

- **`primary_onchain`**
  - URL: <https://etherscan.io/tx/0x5a826f6c6231138d84f9d5bd020417a21b246bc1c3891331377f289e6dd89577>
  - tx_hash: `0x5a826f6c6231138d84f9d5bd020417a21b246bc1c3891331377f289e6dd89577`
  > Tether USDT addBlackList tx for Semenov address 0x6be0ae71... at 2023-12-09 04:37 UTC. Part of Tether's 2023-12-09 retroactive sweep (see tether-retroactive-sweep-2023); all 8 Semenov addresses in that sweep.
- **`primary_corporate`**
  - URL: <https://usdtbanlist.com/address/0x43fa21d92141BA9db43052492E0DeEE5aa5f0A93>
  - body_hash: `sha256:f61b000c0d33c7d2c8094af44eb65f8ece4829b9831c16ae107c916c3a1718e0`
  - body_path: `sources/http_captures/semenov-ofac-2023/asset-layer-check/usdtbanlist.com__address-0x43fa21d92141BA9db43052492E0DeEE5aa5f0A93.html`
  > Cross-reference anchor; 8 Semenov USDT freezes distributed across 2023-12-09 04:37-05:37 UTC batch.

## 4. No-change observations (where applicable)

### l1_consensus — `ofac_compliant_relay_share_stable_through_semenov_designation`

**Window**: `2023-08-09 00:00:00+00:00` → `2023-09-06 23:59:59+00:00`

**Sources**:

- **`semi_primary_measurement`**
  - URL: <https://raw.githubusercontent.com/nerolation/censorship.pics/main/data/relay_censorship_share.csv>
  - body_hash: `sha256:45c1db9ca70491743e2e33c313d7293eed791a82d0ea7313c5241eca9e8b4567`
  - body_path: `sources/l1_datasets/tornado-cash-ofac-2022/relay_censorship_share.csv`
  > Slice [2023-08-09, 2023-09-06] — 29 days × 2 categories = 58 rows. Censoring-relay
> share: pre-event 14d mean 38.45% ± 0.96 (stable), event day (2023-08-23) 37.03%,
> post-event 14d mean 39.57% ± 1.27 (stable). Event-day value is within 1.5 sd of the
> pre-event mean. No step change. The relay-share baseline was materially lower in
> Aug 2023 (~38%) than the 73% peak reached around the 2022-11-08 redesignation,
> reflecting relay-ecosystem changes (MEV-Blocker / ultra-sound / etc.) rather than
> Tornado-specific filtering. The null result here is independent of that baseline
> drift: an individual-level Tornado-adjacent designation did not perturb the aggregate.
- **`semi_primary_measurement`**
  - URL: <https://www.relayscan.io>
  - Wayback: <https://web.archive.org/web/20260421114750/https://www.relayscan.io/>
  - body_hash: `sha256:dc39f55922c657cd3caf22cdd77287f707ddec63ec0510091532f5fadc7aa827`
  - body_path: `sources/http_captures/tornado-cash-ofac-2022/l1-relay-dashboards/www.relayscan.io__capture__1a79bf8cec.html`
  > Relayscan (Flashbots-operated) independent dashboard consistent with the Wahrstätter
> plateau — second source for the observed_no_change claim.

## 5. Honest coverage gaps

- **l0_network** (`not_measured`): No new L0 network-layer artifact attached for the 2023-08-23 Semenov event. tornado.cash is
- **l3_rpc** (`not_measured`): No first-party RPC-filter-list snapshot, provider docs/status
- **l4_frontend** (`not_measured`): Tornado frontends were already offline from the 2022-08-08 cascade; no fresh canonical
- **offramp_cex** (`not_measured`): Chain-analytics anchors pinned 2026-04-22 as primary_corporate

## 7. Related events

- [`tornado-cash-ofac-2022`](./tornado-cash-ofac-2022.md)
- [`tornado-cash-ofac-redesignation-2022`](./tornado-cash-ofac-redesignation-2022.md)
- [`tornado-cash-ofac-delisting-2025`](./tornado-cash-ofac-delisting-2025.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `029a430`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

