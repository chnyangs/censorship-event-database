# Evidence chain — `tornado-cash-ofac-redesignation-2022`

**Status**: `admitted` · **Stratum**: `S1_ofac_sdn` · **Shape**: `comparison` (1 changed layer(s): `asset_onchain`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `80b0ca3` · **Schema**: `0.2.0` · **Event last_verified**: `2026-04-21` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "Expansion of the Tornado Cash SDN entry on 2022-11-08
> from 38 to 98 addresses did not cause a measurable step change in Ethereum OFAC-compliant
> relay share (72.00% event day; 73.48% ± 2.23 post-event 14d; 65.96% ± 5.31 pre-event 14d)."
> Other layers remain scoped for follow-up.

## 1. Trigger

- **Type**: `ofac_sdn_designation`
- **Actor**: `US_OFAC`
- **Timestamp**: `2022-11-08 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://ofac.treasury.gov/recent-actions/20221108>
  - Wayback: <https://web.archive.org/web/20260421130935/https://ofac.treasury.gov/recent-actions/20221108>
  - body_hash: `sha256:39f2b5333cd03c3a0bb3a91ef913a756efcb34b004c32bcfef75aaa23f4ac4e5`
  - body_path: `sources/http_captures/tornado-cash-ofac-redesignation-2022/ofac-recent-actions/ofac.treasury.gov__recent-actions-20221108__29cc0b1876.html`
  > OFAC Recent Actions page for 2022-11-08, which simultaneously (a) removes the original 2022-08-08
> Cyber-related Tornado Cash designation and (b) redesignates Tornado Cash (including TORNADO CASH,
> TORNADO CASH CLASSIC, TORNADO CASH NOVA variants) under DPRK-related authorities with an expanded
> address list. The 98 unique digital-currency addresses in target.addresses are extracted verbatim
> from this archived page (92 ETH + 6 USDC).
- **`primary_legal`**
  - URL: <https://home.treasury.gov/news/press-releases/jy1087>
  > Treasury press release "Treasury Designates DPRK Weapons Representatives; Tornado Cash Redesignated with Additional DPRK Authorities" (2022-11-08). Describes the legal-authority shift from EO 13694 (Cyber-related) to DPRK-related authorities.

## 2. Target

- **Kind**: `address_set`
- **Enumeration**: `complete`
- **Protocol**: `tornado_cash`
- **Chains**: `ethereum`
- **Addresses**: 92 total (enumerated in event YAML)
- **Canonical domains**: `tornado.cash`, `app.tornado.cash`, `tornadocash.eth.link`

> Full set of 98 unique digital-currency addresses (92 ETH + 6 USDC) extracted from the OFAC Recent
> Actions page for 2022-11-08 (archived locally and on Wayback; see trigger.citation[0]). Set is the
> union of addresses listed under the TORNADO CASH, TORNADO CASH CLASSIC, and TORNADO CASH NOVA SDN
> entries on that page. Address casing preserved as published by OFAC (note: OFAC lists 0xCa0840...
> twice under different casings — preserved as two entries to mirror the authoritative page). The
> original 2022-08-08 designation of 38 ETH addresses is a proper subset of this 98-address set; 60
> addresses are net-new additions on 2022-11-08.

## 3. Changed-layer observations (supports the scoped claim)

### asset_onchain · attribution: `direct` · Δt = 9509.3h

**Event label**: `tether_froze_one_of_92_tornado_addresses_in_retroactive_sweep`

**Timestamp**: `2023-12-09 05:18:00+00:00` (precision: `minute`)

**Sources**:

- **`primary_onchain`**
  - URL: <https://etherscan.io/tx/0x5b4c60abaf4807eba903877835a301d08d8e51f6fd89f1c69657659f90e18f70>
  - tx_hash: `0x5b4c60abaf4807eba903877835a301d08d8e51f6fd89f1c69657659f90e18f70`
  > Tether USDT addBlackList tx for Tornado Cash pool address 0x905b63Fff465B9fFBF41DeA908CEb12478ec7601
> at 2023-12-09 05:18 UTC. Part of Tether's 2023-12-09 retroactive sweep of historical
> OFAC-SDN addresses. This is the ONLY one of 92 ETH addresses in the 2022-11-08
> redesignation that has been Tether-blacklisted — an asymmetry-paper-relevant finding.
- **`primary_corporate`**
  - URL: <https://usdtbanlist.com/address/0x905b63Fff465B9fFBF41DeA908CEb12478ec7601>
  - body_hash: `sha256:427bc5305a387ea370850bc58b3127d49389b5726110e10ed74cbbbcb640de7e`
  - body_path: `sources/http_captures/tornado-cash-ofac-redesignation-2022/asset-layer-check/usdtbanlist.com__address-0x905b63Fff465B9fFBF41DeA908CEb12478ec7601.html`
  > usdtbanlist.com anchor. The remaining 91 Tornado-redesignation addresses are on OFAC SDN but NOT on Tether/Circle blacklists, establishing the smart-contract asymmetry finding.

## 4. No-change observations (where applicable)

### l1_consensus — `ofac_compliant_relay_share_stable_through_redesignation`

**Window**: `2022-10-25 00:00:00+00:00` → `2022-11-22 23:59:59+00:00`

**Sources**:

- **`semi_primary_measurement`**
  - URL: <https://raw.githubusercontent.com/nerolation/censorship.pics/main/data/relay_censorship_share.csv>
  - body_hash: `sha256:45c1db9ca70491743e2e33c313d7293eed791a82d0ea7313c5241eca9e8b4567`
  - body_path: `sources/l1_datasets/tornado-cash-ofac-2022/relay_censorship_share.csv`
  > Slice [2022-10-25, 2022-11-22] — 29 days × 2 categories (censoring / non-censoring) =
> 58 rows. Censoring-relay share: pre-event 14d mean 65.96% ± 5.31 (rising trend near
> saturation); event day (2022-11-08) 72.00%; post-event 14d mean 73.48% ± 2.23 (stable
> plateau). The event-day value is within 0.67 sd of the post-event mean, and the
> continuation of the pre-event trajectory without inflection is the expected null shape.
> Treated as observed_no_change: SDN-list expansion did not induce a step in relay OFAC-
> compliance. attribution=none because no step change was observed — the observation is
> a null result, not a causal claim.
- **`semi_primary_measurement`**
  - URL: <https://www.relayscan.io>
  - Wayback: <https://web.archive.org/web/20260421114750/https://www.relayscan.io/>
  - body_hash: `sha256:dc39f55922c657cd3caf22cdd77287f707ddec63ec0510091532f5fadc7aa827`
  - body_path: `sources/http_captures/tornado-cash-ofac-2022/l1-relay-dashboards/www.relayscan.io__capture__1a79bf8cec.html`
  > Relayscan (Flashbots-operated) dashboard independently tracks per-relay OFAC compliance
> over time; its historical curve is consistent with Wahrstätter's plateau, serving as a
> second admission-grade source for the observed_no_change claim.

## 5. Honest coverage gaps

- **l0_network** (`not_measured`): OONI volunteer coverage of tornado.cash was effectively absent for the 2022-08-08 parent event
- **l3_rpc** (`not_measured`): No event-specific RPC-provider rejection, docs/status change, or
- **l4_frontend** (`not_measured`): Tornado frontend (tornado.cash / app.tornado.cash) had already been taken offline or
- **offramp_cex** (`not_measured`): Chain-analytics anchors pinned 2026-04-22 as primary_corporate

## 7. Related events

- [`tornado-cash-ofac-2022`](./tornado-cash-ofac-2022.md)
- [`tornado-cash-ofac-delisting-2025`](./tornado-cash-ofac-delisting-2025.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `80b0ca3`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

