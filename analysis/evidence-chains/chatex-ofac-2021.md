# Evidence chain — `chatex-ofac-2021`

**Status**: `admitted` · **Stratum**: `S1_ofac_sdn` · **Shape**: `comparison` (2 changed layer(s): `asset_onchain`, `l4_frontend`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `f70cc98` · **Schema**: `0.2.0` · **Event last_verified**: `2026-04-22` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T00:48:55Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "OFAC designation of Chatex on 2021-11-08 produced a direct L4 frontend change within
> 9 days in the form of an operator-posted compliance notice freezing customer withdrawals,
> mechanistically distinct from the same-quarter SUEX case (no frontend reaction) despite
> both being foreign exchange entities sanctioned under the same policy push."

## 1. Trigger

- **Type**: `ofac_sdn_designation`
- **Actor**: `US_OFAC`
- **Timestamp**: `2021-11-08 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://ofac.treasury.gov/recent-actions/20211108>
  - Wayback: <https://web.archive.org/web/20260421140140/https://ofac.treasury.gov/recent-actions/20211108>
  - body_hash: `sha256:12b576be0cd5dbc1a0b763151d13a0c53e16e507cc02298dd27be47bca971942`
  - body_path: `sources/http_captures/chatex-ofac-2021/ofac-recent-actions/ofac.treasury.gov__recent-actions-20211108__a1d41cd3cf.html`
  > OFAC Recent Actions page for 2021-11-08. CHATEX designated as a SUEX successor exchange.
> Entity CHATEX (Estonia; Latvia; Saint Vincent and the Grenadines; website chatex.com)
> with 30 digital-currency addresses across XBT×22, ETH×6, USDT×1 (Omni), XRP×1. Related
> entities also designated: CHATEXTECH SIA (Latvia), plus 4 individual designees. Tag
> [CYBER2].
- **`primary_legal`**
  - URL: <https://home.treasury.gov/news/press-releases/jy0471>
  > Treasury press release "Treasury Continues to Counter Ransomware as Part of Whole-of-Government Effort; Sanctions Ransomware Operators and Virtual Currency Exchange" (2021-11-08).

## 2. Target

- **Kind**: `address_set`
- **Enumeration**: `complete`
- **Protocol**: `chatex_exchange`
- **Actor name**: Chatex
- **Chains**: `bitcoin`, `ethereum`, `ripple`
- **Addresses**: 30 total (enumerated in event YAML)
- **Canonical domains**: `chatex.com`

> 30 unique digital-currency addresses attached to the CHATEX SDN entity entry, extracted
> verbatim from 2021-11-08 page. Multi-chain: 22 XBT (mix of P2SH + Bech32), 6 ETH, 1 USDT
> (Omni on XBT chain), 1 XRP. The related CHATEXTECH SIA and individual designees do not
> carry additional on-chain addresses in this page.

## 3. Changed-layer observations (supports the scoped claim)

### asset_onchain · attribution: `direct` · Δt = 28.25h

**Event label**: `usdc_blacklist_next_day_5_of_6_eth_addresses`

**Timestamp**: `2021-11-09 04:15:00+00:00` (precision: `minute`)

**Sources**:

- **`primary_onchain`**
  - URL: <https://etherscan.io/tx/0x14a97060a7370f5c88573f7d01391f6767133cfa596be9e2985ff57c042dfc23>
  - tx_hash: `0x14a97060a7370f5c88573f7d01391f6767133cfa596be9e2985ff57c042dfc23`
  > USDC Blacklisted() tx for address 0x67d40EE1... at 2021-11-09 04:15 UTC. Canonical chain receipt; full 64-char tx available via sources/asset_layer_scan/chatex-ofac-2021.json.
- **`primary_corporate`**
  - URL: <https://usdtbanlist.com/address/0x67d40EE1A85bf4a4Bb7Ffae16De985e8427B6b45>
  - body_hash: `sha256:307d2114e16ee087eb53d9c0cf5b72e19d064338dc6da708abb08fb92a3cc7e7`
  - body_path: `sources/http_captures/chatex-ofac-2021/asset-layer-check/usdtbanlist.com__address-0x67d40EE1A85bf4a4Bb7Ffae16De985e8427B6b45.html`
  > Circle USDC batch-blacklisted 5 of 6 Chatex ETH addresses on 2021-11-09 04:15
> UTC (identical minute-level timestamp, indicating single-batch operation),
> ~28 hours after the 2021-11-08 OFAC designation. The address
> 0x6acdfba02d390b97ac2b2d42a63e85293bcc160e is the single outlier not present
> on Circle's blacklist — reason unknown (possibly never held USDC so Circle
> had no coverage action to take). Full data at
> sources/asset_layer_scan/chatex-ofac-2021.json.
- **`primary_corporate`**
  - URL: <https://usdtbanlist.com/address/0x6f1ca141a28907f78ebaa64fb83a9088b02a8352>
  - body_hash: `sha256:dd37dbf628f1947f8b88964e4c88d457a9c3e7bb2366c44ee5726910db0f20ad`
  - body_path: `sources/http_captures/chatex-ofac-2021/asset-layer-check/usdtbanlist.com__address-0x6f1ca141a28907f78ebaa64fb83a9088b02a8352.html`
  > Second-sampled address (Chatex cluster) frozen in the same 2021-11-09 04:15 UTC Circle batch.

### l4_frontend · attribution: `direct` · Δt = 233.99h

**Event label**: `operator_compliance_notice_and_withdrawal_freeze`

**Timestamp**: `2021-11-17 17:59:45+00:00` (precision: `minute`)

**Sources**:

- **`primary_corporate`**
  - URL: <https://web.archive.org/web/20211117175945/https://chatex.com/>
  - body_hash: `sha256:6bc86f40095c66b3a0161ce7716baa2a27c49973d64fde7bb8832e90fbf94a77`
  - body_path: `sources/http_captures/chatex-ofac-2021/frontend-wayback/web.archive.org__web-20211117175945-https-chatex.com__918765a11d.html`
  > Wayback snapshot 2021-11-17 17:59 UTC (≈9 days post-event) of chatex.com displaying
> verbatim operator statement: "Important Chatex Announcement. CHTX Token sale is
> canceled. Chatex is listed on the U.S. Sanctions List under Executive Order 13694 on
> suspicion of supporting Suex company. [...] All customers' funds are safe and secure,
> but restricted to be moved during the legal case proceeding." This is a first-party
> operator corporate communication naming the legal trigger (EO 13694) and explicitly
> imposing a customer-fund freeze — primary_corporate source.
- **`primary_corporate`**
  - URL: <https://web.archive.org/web/20211202224324/https://chatex.com/>
  - body_hash: `sha256:6d83f3106f760999b1c959f6ebb946815169c65164fb853caf9783d145f564f8`
  - body_path: `sources/http_captures/chatex-ofac-2021/frontend-wayback/web.archive.org__web-20211202224324-https-chatex.com__6965640198.html`
  > Second Wayback snapshot 2021-12-02 (24 days post-event). Same operator notice persists;
> demonstrates the compliance posture was sustained rather than transient. Independent
> archival anchor.

## 5. Honest coverage gaps

- **l0_network** (`not_measured`): L0 network-layer OONI API query performed 2026-04-22. Searched the
- **offramp_cex** (`not_measured`): Chain-analytics anchors pinned 2026-04-22 as primary_corporate

## 6. Follow-on reactions (informational, not causally attributed)

> These are cross-event reactions observed after the trigger but with `attribution: unknown` or temporal gap too large for direct causation. **They do NOT support the scoped claim above.** Tracked for cross-event anchor purposes only.

### asset_onchain — `tether_retroactive_sweep_5_of_6_chatex_addresses`

- Attribution: `unknown`
- Relationship: `cross_event_anchor`
- Δt from trigger: `18268.6h`

> Tether USDT retroactively froze the same 5 Chatex ETH addresses on
> 2023-12-09 04:35-05:31 UTC — **750 days after the OFAC designation**.
> Moved out of observations[] per reviewer Action 4 because the 2-year
> gap rules out direct causation from this event's trigger. The action
> is its own corporate-policy event (see
> `tether-retroactive-sweep-2023`); tracking it here as a follow-on
> reaction is informational, not a changed-layer claim for Chatex's
> statistics.

- **`primary_onchain`**
  - URL: <https://etherscan.io/tx/0xd98d2633eb11bbac6955b6d58911ee45e4612efb352f4bcb3cf4063fc0cb98d5>
  - tx_hash: `0xd98d2633eb11bbac6955b6d58911ee45e4612efb352f4bcb3cf4063fc0cb98d5`
  > Tether addBlackList tx for Chatex address 0x67d40EE1 at 2023-12-09 04:36 UTC.

## 7. Related events

- [`suex-ofac-2021`](./suex-ofac-2021.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `f70cc98`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

