# Evidence chain — `grinex-garantex-successor-ofac-2025`

**Status**: `admitted` · **Stratum**: `S1_ofac_sdn` · **Shape**: `comparison` (1 changed layer(s): `asset_onchain`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-05-31` · **Source commit**: `1e151cd` · **Schema**: `0.2.0` · **Event last_verified**: `2026-04-21` · **Tool version**: `0.1.0` · **Generated**: `2026-05-31T12:31:46Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "OFAC designation of the Grinex / Old Vector /
> A7 Russian exchange successor network on 2025-08-14 coincided with a sharp step-up in
> Ethereum aggregate OFAC-compliant relay share (0% → 86% over 2025-08-14 → 2025-08-17),
> although attribution to Grinex-address-list updates specifically is not established.
> Asset-layer and off-ramp-CEX reactions have not yet been measured."

## 1. Trigger

- **Type**: `ofac_sdn_designation`
- **Actor**: `US_OFAC`
- **Timestamp**: `2025-08-14 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://ofac.treasury.gov/recent-actions/20250814>
  - Wayback: <https://web.archive.org/web/20260421133548/https://ofac.treasury.gov/recent-actions/20250814>
  - body_hash: `sha256:60cd8ebfaa899001aefcfdaf456c1ace5e356d2c677390ac53f53017dbe7b2ce`
  - body_path: `sources/http_captures/grinex-garantex-successor-ofac-2025/ofac-recent-actions/ofac.treasury.gov__recent-actions-20250814__4cb08c46f7.html`
  > OFAC Recent Actions page for 2025-08-14. Designates a Russia-linked virtual-currency
> network treated as Garantex's operational successor, including entities GRINEX, OLD
> VECTOR LLC, A7 LIMITED LIABILITY COMPANY, and multiple individuals (Sergey MENDELEEV,
> Aleksandr MIRA SERDA). Tags include [CYBER4] and Russia/Ukraine-related authorities.
> 21 unique digital-currency addresses attached across the network entities (TRX×11,
> ETH×8, XBT×1, USDT-TRC20×1). No canonical frontend domain published in the SDN entries
> themselves (Grinex does not appear to list a web presence in the OFAC entry).
- **`primary_legal`**
  - URL: <https://home.treasury.gov/news/press-releases/sb0266>
  > Treasury press release "Treasury Sanctions Cryptocurrency Exchange and Network Enabling Sanctions Evasion and Cyber Criminals" (2025-08-14).

## 2. Target

- **Kind**: `address_set`
- **Enumeration**: `complete`
- **Protocol**: `garantex_successor_network`
- **Chains**: `tron`, `ethereum`, `bitcoin`
- **Addresses**: 21 total (enumerated in event YAML)

> Full set of 21 unique digital-currency addresses extracted verbatim from the OFAC Recent
> Actions page for 2025-08-14, aggregated across the Grinex / Old Vector / A7 /
> individual-designee SDN entity entries. Per-chain breakdown: 11 TRX + 8 ETH + 1 XBT + 1
> USDT (TRC20). Addresses are mapped to multiple named legal entities within the Garantex
> successor network — this target set treats them as one cluster consistent with the
> Treasury press release's framing of a single coordinated evasion network.

## 3. Changed-layer observations (supports the scoped claim)

### asset_onchain · attribution: `direct` · Δt = 21.25h

**Event label**: `tether_batch_froze_all_11_trx_addresses_same_day_as_ofac`

**Timestamp**: `2025-08-14 21:15:00+00:00` (precision: `minute`)

**Sources**:

- **`primary_onchain`**
  - URL: <https://tronscan.org/#/transaction/075d10048c048e755d1d7a9d97eb2a1ab4f94cf8b42cea920267caff1492d0a3>
  - tx_hash: `075d10048c048e755d1d7a9d97eb2a1ab4f94cf8b42cea920267caff1492d0a3`
  > Tether USDT-TRC20 addBlackList tx on TRON for Grinex address TAYhjpL8pPs8T84FSM329nffQpc6jD8GBM at 2025-08-14 21:15 UTC (one of 11-batch).
- **`primary_corporate`**
  - URL: <https://usdtbanlist.com/address/TAYhjpL8pPs8T84FSM329nffQpc6jD8GBM>
  - body_hash: `sha256:b035c13a23c2cce841cfb8ed9dd83e72e4f3c2c0afc2ee1c5df901a6ecbca9f9`
  - body_path: `sources/http_captures/grinex-garantex-successor-ofac-2025/asset-layer-check/usdtbanlist.com__address-TAYhjpL8pPs8T84FSM329nffQpc6jD8GBM.html`
  > Tether froze all 11 TRX addresses in the Grinex network on 2025-08-14 21:15 UTC.
> Identical freeze timestamp across all 11 addresses (batch operation). Full batch
> data at sources/asset_layer_scan/grinex-garantex-successor-ofac-2025.json.
- **`primary_corporate`**
  - URL: <https://usdtbanlist.com/address/TC8axQvzJEVR3NKN6mZnJtGy7537GEmh38>
  - body_hash: `sha256:b3627756930222c327cea84fb956fc38a271ab7970c1375d98abb431a08511ad`
  - body_path: `sources/http_captures/grinex-garantex-successor-ofac-2025/asset-layer-check/usdtbanlist.com__address-TC8axQvzJEVR3NKN6mZnJtGy7537GEmh38.html`
  > Second-sampled TRX address anchor (Grinex cluster), same 2025-08-14 21:15 UTC batch.

## 5. Honest coverage gaps

- **l0_network** (`not_measured`): No OONI / Censored Planet artifact tied to a canonical Grinex-network frontend (the SDN
- **l1_consensus** (`not_measured`): Wahrstätter data shows a post-event step (0% → 86% at +3d) but attribution
- **l3_rpc** (`not_measured`): No pinned RPC-provider rejection, docs/status change, or
- **offramp_cex** (`not_measured`): Chain-analytics anchors pinned 2026-04-22 as primary_corporate

## 6. Follow-on reactions (informational, not causally attributed)

> These are cross-event reactions observed after the trigger but with `attribution: unknown` or temporal gap too large for direct causation. **They do NOT support the scoped claim above.** Tracked for cross-event anchor purposes only.

### l1_consensus — `ofac_compliant_relay_share_stepped_up_three_days_post_event`

- Attribution: `unknown`
- Relationship: `temporal_coincidence_not_causal`
- Δt from trigger: `72h`

> Wahrstätter slice [2025-07-31, 2025-08-28] shows a step in
> censoring-relay share from 0% (event day 2025-08-14) to 86% at
> 2025-08-17 (3 days post-event). Moved out of observations[] per
> reviewer Action 4 because the step shape is consistent with a
> relay-ecosystem composition change (e.g. a single dominant relay
> re-enabling its filter list) rather than a direct Grinex-address-
> driven effect; distinguishing these hypotheses requires per-relay
> block-filter-list inspection which has not been done. Retained as
> a follow_on_reaction informational datapoint, NOT as a changed-
> layer claim for this event's cascade statistics.

- **`semi_primary_measurement`**
  - URL: <https://raw.githubusercontent.com/nerolation/censorship.pics/main/data/relay_censorship_share.csv>
  - body_hash: `sha256:45c1db9ca70491743e2e33c313d7293eed791a82d0ea7313c5241eca9e8b4567`
  - body_path: `sources/l1_datasets/tornado-cash-ofac-2022/relay_censorship_share.csv`
  > Wahrstätter relay-censorship-share CSV slice for the 2025-08-14 event window.

## 7. Related events

- [`garantex-ofac-2022`](./garantex-ofac-2022.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `1e151cd`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

