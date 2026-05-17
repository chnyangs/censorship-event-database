# Evidence chain — `lockbit-affiliates-ofac-2024`

**Status**: `admitted` · **Stratum**: `S1_ofac_sdn` · **Shape**: `comparison` (1 changed layer(s): `asset_onchain`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-05-17` · **Source commit**: `35cd33f` · **Schema**: `0.2.0` · **Event last_verified**: `2026-04-22` · **Tool version**: `0.1.0` · **Generated**: `2026-05-25T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "LockBit-affiliate individual OFAC designation (2024-02-20) produced no measurable step
> change in Ethereum aggregate relay OFAC-compliance share. Other layers are either
> structurally not_applicable (individuals, no frontend) or pending empirical query."

## 1. Trigger

- **Type**: `ofac_sdn_designation`
- **Actor**: `US_OFAC`
- **Timestamp**: `2024-02-20 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://ofac.treasury.gov/recent-actions/20240220>
  - Wayback: <https://web.archive.org/web/20260421141319/https://ofac.treasury.gov/recent-actions/20240220>
  - body_hash: `sha256:c01b2472ae47003d8af55e03b97c445166bb1e359cc5861617035241ce0b2bbe`
  - body_path: `sources/http_captures/lockbit-affiliates-ofac-2024/ofac-recent-actions/ofac.treasury.gov__recent-actions-20240220__ece0e9f7ef.html`
  > OFAC Recent Actions page for 2024-02-20. Two LockBit ransomware affiliates designated:
> Ivan KONDRATIEV (aka BASSTERLORD; aka multiple Telegram/Discord handles) with 8 XBT
> + 1 ETH, and Artur SUNGATOV with 1 XBT. Part of joint US/UK/Australia/EU/CA Operation
> Cronos takedown of LockBit infrastructure. Tags [CYBER2] + Russia EO14024.
- **`primary_legal`**
  - URL: <https://home.treasury.gov/news/press-releases/jy2114>
  > Treasury press release "United States Sanctions Affiliates of Russia-Based LockBit Ransomware Group" (2024-02-20).

## 2. Target

- **Kind**: `address_set`
- **Enumeration**: `complete`
- **Actor name**: KONDRATIEV + SUNGATOV
- **Chains**: `bitcoin`, `ethereum`
- **Addresses**: 10 total (enumerated in event YAML)

> 10 unique addresses across 2 individuals (KONDRATIEV 9, SUNGATOV 1). 9 XBT + 1 ETH.

## 3. Changed-layer observations (supports the scoped claim)

### asset_onchain · attribution: `direct` · Δt = 24.32h

**Event label**: `circle_usdc_blacklist_next_day`

**Timestamp**: `2024-02-21 00:19:00+00:00` (precision: `minute`)

**Sources**:

- **`primary_onchain`**
  - URL: <https://etherscan.io/tx/0x11311fbe5e82aadecdd456fb5c09b46c2dca5474793aa8c4c9a2d8a48806c774>
  - tx_hash: `0x11311fbe5e82aadecdd456fb5c09b46c2dca5474793aa8c4c9a2d8a48806c774`
  > USDC Blacklisted() tx for KONDRATIEV's ETH address 0xf370... at 2024-02-21 00:19 UTC.
- **`primary_corporate`**
  - URL: <https://usdtbanlist.com/address/0xf3701f445b6bdafedbca97d1e477357839e4120d>
  - body_hash: `sha256:1a004d4c1d397b1a2d0e7dcd2b2bdd08c1b8cc5338619f755e0059a639690acf`
  - body_path: `sources/http_captures/lockbit-affiliates-ofac-2024/asset-layer-check/usdtbanlist.com__address-0xf3701f445b6bdafedbca97d1e477357839e4120d.html`
  > KONDRATIEV's ETH address 0xf370... blacklisted by Circle USDC on 2024-02-21 00:19
> UTC and by Tether USDT on 2024-02-21 03:21 UTC — same day, ~24-27h after OFAC
> designation. Single-address data; full scan at
> sources/asset_layer_scan/lockbit-affiliates-ofac-2024.json.
- **`primary_legal`**
  - URL: <https://ofac.treasury.gov/recent-actions/20240220>
  - body_hash: `sha256:c01b2472ae47003d8af55e03b97c445166bb1e359cc5861617035241ce0b2bbe`
  - body_path: `sources/http_captures/lockbit-affiliates-ofac-2024/ofac-recent-actions/ofac.treasury.gov__recent-actions-20240220__ece0e9f7ef.html`
  > OFAC SDN entry as cross-reference anchor for the primary_corporate observation.

## 4. No-change observations (where applicable)

### l1_consensus — `ofac_compliant_relay_share_stable_through_lockbit_affiliate_designation`

**Window**: `2024-02-06 00:00:00+00:00` → `2024-03-05 23:59:59+00:00`

**Sources**:

- **`semi_primary_measurement`**
  - URL: <https://raw.githubusercontent.com/nerolation/censorship.pics/main/data/relay_censorship_share.csv>
  - body_hash: `sha256:45c1db9ca70491743e2e33c313d7293eed791a82d0ea7313c5241eca9e8b4567`
  - body_path: `sources/l1_datasets/tornado-cash-ofac-2022/relay_censorship_share.csv`
  > Censoring-relay share: pre-event 14d mean 53.13% ± 2.40, event day 48.75%, post-event
> 14d mean 50.39% ± 1.47. Event-day value is within 2 sd of pre-event mean; post-event
> mean lower than pre (signaling slight gradual decline trend unrelated to event).
> Null shape.
- **`semi_primary_measurement`**
  - URL: <https://www.relayscan.io>
  - Wayback: <https://web.archive.org/web/20260421114750/https://www.relayscan.io/>
  - body_hash: `sha256:dc39f55922c657cd3caf22cdd77287f707ddec63ec0510091532f5fadc7aa827`
  - body_path: `sources/http_captures/tornado-cash-ofac-2022/l1-relay-dashboards/www.relayscan.io__capture__1a79bf8cec.html`
  > Relayscan independent dashboard — second source for the null claim.

## 5. Honest coverage gaps

- **l3_rpc** (`not_measured`): No pinned RPC-provider rejection, docs/status change, or
- **offramp_cex** (`not_measured`): Chain-analytics anchors pinned 2026-04-22 as primary_corporate

## 7. Related events

- [`lockbit-leader-ofac-2024`](./lockbit-leader-ofac-2024.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `35cd33f`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

