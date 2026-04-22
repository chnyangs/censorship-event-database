# Evidence chain — `tornado-cash-ofac-delisting-2025`

**Status**: `admitted` · **Stratum**: `S2_ofac_removal` · **Shape**: `cascade` (3 changed layer(s): `asset_onchain`, `l1_consensus`, `l4_frontend`) · **Tier**: `anchor_case`

**Dataset version**: `unknown` · **Schema**: `0.2.0` · **Event last_verified**: `2026-04-21` · **Tool version**: `0.1.0` · **Generated**: `2026-04-22T05:44:02Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "OFAC delisting of Tornado Cash on 2025-03-21 (Van Loon-litigation driven)
> is the first reverse-cascade event in the dataset, producing observed_change
> on 3 layers: L1 consensus censoring-relay share dropped ≈25pp within 14
> days; Circle USDC unblacklisted at least one historical address; L4
> frontend remained partially absent (tornado.cash domain never restored).
> Establishes structural asymmetry between cascade and reverse-cascade
> shapes — the latter is slower and patchier than the former."

## 1. Trigger

- **Type**: `ofac_sdn_removal`
- **Actor**: `US_OFAC`
- **Timestamp**: `2025-03-21 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://ofac.treasury.gov/recent-actions/20250321>
  - Wayback: <https://web.archive.org/web/20260421111710/https://ofac.treasury.gov/recent-actions/20250321>
  - body_hash: `sha256:bb3a6660863f0ebadbe7a8f1b072a0f999b433579886106c5097311c1e1764e4`
  - body_path: `sources/http_captures/tornado-cash-ofac-delisting-2025/ofac-recent-actions/ofac.treasury.gov__recent-actions-20250321__a54f76a3e2.html`
  > OFAC Recent Actions page for the 2025-03-21 Tornado Cash deletion entry; the 98 Ethereum addresses in target.addresses are extracted verbatim from this archived page
- **`primary_legal`**
  - URL: <https://home.treasury.gov/news/press-releases/sb0057>
  > Treasury press release announcing Tornado Cash delisting on 2025-03-21

## 2. Target

- **Kind**: `address_set`
- **Enumeration**: `complete`
- **Protocol**: `tornado_cash`
- **Chains**: `ethereum`
- **Addresses**: 98 total (enumerated in event YAML)
- **Canonical domains**: `tornado.cash`, `app.tornado.cash`, `tornadocash.eth.link`

> Full set of 98 unique Ethereum addresses extracted from the OFAC Recent Actions page for 2025-03-21 (archived locally and on Wayback; see trigger.citation[0]). Set is the union of every Tornado-Cash-associated address OFAC had designated across 2022-08-08, 2022-11-08, and later additions, all removed by this single delisting action. Address casing preserved as published by OFAC.

## 3. Changed-layer observations (supports the scoped claim)

### l4_frontend · attribution: `direct` · Δt = 110.53h

**Event label**: `access_or_listing_reemerges`

**Timestamp**: `2025-03-25 14:31:33+00:00` (precision: `minute`)

**Sources**:

- **`primary_corporate`**
  - URL: <https://git.tornado.ws/tornadocash/docs/blame/branch/master/book/README.md>
  - Wayback: <https://web.archive.org/web/20260421101538/https://git.tornado.ws/tornadocash/docs/blame/branch/master/book/README.md>
  > Official Tornado Cash documentation states that user interfaces are hosted on IPFS by the community and that the latest IPFS content hashes are published via tornadocash.eth and nova.tornadocash.eth, providing a first-party statement about the frontend distribution path
- **`primary_corporate`**
  - URL: <https://git.tornado.ws/tornadocash/classic-ui/commit/2437ecc426>
  - body_hash: `sha256:61113286ed87fac777e474c648b60f0857a7825977f6fac7d682ce68db575eda`
  - body_path: `sources/operator_commits/tornado-cash-ofac-delisting-2025/2437ecc426.diff`
  > Operator-authored commit by Theo on the maintained classic-ui Gitea
> repo, dated 2025-03-25 22:31:33 +08:00 (14:31:33 UTC), four days
> after the 2025-03-21 OFAC delisting. Two decisive hunks explicitly
> undo the sanctions-era frontend freeze:
> (1) networkConfig.js removes the block comment "Instances frozen
> due to sanctions" that had wrapped the USDC pool instance
> configuration, restoring the USDC deposit/withdraw path;
> (2) head title, og:url, og:image, preventMultitabs.js,
> pages/index.vue, and all six localized compliance_warning strings
> (en/es/fr/ru/tr/zh) swap the sanctions-era backup domain
> "2.torndao.eth.limo" out for the original "tornadocash.eth.limo".
> Full diff archived locally at
> sources/operator_commits/tornado-cash-ofac-delisting-2025/2437ecc426.diff
> (body_hash above) for reproducibility.
- **`semi_primary_measurement`**
  - URL: <https://git.tornado.ws/tornadocash/classic-ui/commits/branch/master>
  - Wayback: <https://web.archive.org/web/20260421101653/https://git.tornado.ws/tornadocash/classic-ui/commits/branch/master>
  > Gitea commit history shows commit 2437ecc426 at 2025-03-25 22:31:33 +08:00 referencing a move to tornadocash.eth.limo together with USDC and USDT unlock messaging, providing a repo-side anchor for frontend rollback work after the delisting
- **`semi_primary_measurement`**
  - URL: <https://git.tornado.ws/tornadocash/classic-ui/src/branch/master>
  - Wayback: <https://web.archive.org/web/20260421101721/https://git.tornado.ws/tornadocash/classic-ui/src/branch/master>
  > The branch view attributes nuxt.config.js to the same 2025-03-25 22:31:33 +08:00 commit, tying the rollback anchor to a frontend configuration file rather than only a generic repo commit list
- **`semi_primary_measurement`**
  - URL: <https://git.tornado.ws/tornadosto/classic-ui>
  - Wayback: <https://web.archive.org/web/20260421101749/https://git.tornado.ws/tornadosto/classic-ui>
  > Mirror repository page shows the same 2437ecc426 commit and timestamp on the master branch, corroborating the frontend reconfiguration anchor
- **`semi_primary_measurement`**
  - URL: <https://git.tornado.ws/tornadosto/classic-ui/src/branch/master>
  - Wayback: <https://web.archive.org/web/20260421101816/https://git.tornado.ws/tornadosto/classic-ui/src/branch/master>
  > Mirror branch view attributes both networkConfig.js and nuxt.config.js to the same 2025-03-25 22:31:33 +08:00 commit, reinforcing that the rollback anchor touched frontend configuration rather than only repository metadata
- **`supporting_community`**
  - URL: <https://git.tornado.ws/tornadocash/classic-ui/actions>
  - Wayback: <https://web.archive.org/web/20260421101845/https://git.tornado.ws/tornadocash/classic-ui/actions>
  > Actions page records commit 2437ecc426 as pushed by Theo to master, which corroborates that the 2025-03-25 frontend-related commit entered the maintained branch
- **`semi_primary_measurement`**
  - URL: <https://app.tornado.cash>
  - Wayback: <https://web.archive.org/web/20260421105831/https://tornadocash.eth.limo/>
  - body_hash: `sha256:7b7a330aff8657dc258a60f91aad4766c1a742e3603f394f1e484482ee95e216`
  - body_path: `sources/http_captures/tornado-cash-ofac-delisting-2025/backfill-1.3/app.tornado.cash__capture__b2ee302b2f.html`
  > Verified on 2026-04-21 that app.tornado.cash redirects to a live UI served from tornadocash.eth.limo, showing that the frontend reconfiguration remained publicly reachable after the 2025 rollback work; local capture bundle stored under sources/http_captures/tornado-cash-ofac-delisting-2025/2026-04-21-frontends/
- **`semi_primary_measurement`**
  - URL: <https://tornadocash.eth.limo/>
  - Wayback: <https://web.archive.org/web/20260421105831/https://tornadocash.eth.limo/>
  - body_hash: `sha256:7b7a330aff8657dc258a60f91aad4766c1a742e3603f394f1e484482ee95e216`
  - body_path: `sources/http_captures/tornado-cash-ofac-delisting-2025/backfill-1.3/tornadocash.eth.limo__capture__158c013abd.html`
  > Verified on 2026-04-21 that the redirected endpoint returns active Tornado Cash UI content rather than an error or parked page (same underlying content as app.tornado.cash above — grouped as one evidence unit); see local capture bundle under sources/http_captures/tornado-cash-ofac-delisting-2025/2026-04-21-frontends/
- **`semi_primary_measurement`**
  - URL: <https://github.com/tornadocash>
  - Wayback: <https://web.archive.org/web/20260421105622/https://github.com/tornadocash>
  - body_hash: `sha256:d690ed08734c1942dc9dd4325efe07066922cd3accab06d99273cc835a0afc7a`
  - body_path: `sources/http_captures/tornado-cash-ofac-delisting-2025/backfill-1.3/github.com__tornadocash__7f33190afd.html`
  > Verified on 2026-04-21 that the GitHub organization is publicly reachable again after the delisting; see local capture bundle under sources/http_captures/tornado-cash-ofac-delisting-2025/2026-04-21-frontends/
- **`semi_primary_measurement`**
  - URL: <https://github.com/tornadocash/tornado-core>
  - Wayback: <https://web.archive.org/web/20260421105714/https://github.com/tornadocash/tornado-core>
  - body_hash: `sha256:eae716bb77d0dc187b11c4c5348b725397a02bfeb143c4110c077841076c8900`
  - body_path: `sources/http_captures/tornado-cash-ofac-delisting-2025/backfill-1.3/github.com__tornadocash-tornado-core__9430a15343.html`
  > Verified on 2026-04-21 that the archived tornado-core repository remains publicly accessible; see local capture bundle under sources/http_captures/tornado-cash-ofac-delisting-2025/2026-04-21-frontends/

### asset_onchain · attribution: `direct` · Δt = 25.37h

**Event label**: `address_unblacklisted`

**Timestamp**: `2025-03-22 01:22:00+00:00` (precision: `minute`)

**Sources**:

- **`primary_onchain`**
  - URL: <https://etherscan.io/tx/0x1c2fbd8b25f201327e0b469164ab753c89a802de7e0768e4e278d224cc10b25a>
  - tx_hash: `12749109753864282829776519000802659275877034053568520406018765398351910318682`
  > USDC unblacklist transaction for target address 0x47CE0C6eD5B0Ce3d3A51fdb1C52DC66a7c3c2936 on 2025-03-22
- **`supporting_community`**
  - URL: <https://usdtbanlist.com/address/0x47CE0C6eD5B0Ce3d3A51fdb1C52DC66a7c3c2936>
  - Wayback: <https://web.archive.org/web/20260421105924/https://usdtbanlist.com/address/0x47CE0C6eD5B0Ce3d3A51fdb1C52DC66a7c3c2936>
  - body_hash: `sha256:796e56678deaefeb73773354336dcb4f75b0770e7ebc3c45f3e9dedc1fd73363`
  - body_path: `sources/http_captures/tornado-cash-ofac-delisting-2025/backfill-1.3/usdtbanlist.com__address-0x47CE0C6eD5B0Ce3d3A51fdb1C52DC66a7c3c2936__a06f6feca5.html`
  > Third-party cross-check showing the same address was USDC-unbanned on 2025-03-22 with the matching Etherscan transaction

### l1_consensus · attribution: `direct` · Δt = 0h

**Event label**: `censoring_relay_share_dropped_post_delisting`

**Timestamp**: `2025-03-21 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`semi_primary_measurement`**
  - URL: <https://raw.githubusercontent.com/nerolation/censorship.pics/main/data/relay_censorship_share.csv>
  - body_hash: `sha256:45c1db9ca70491743e2e33c313d7293eed791a82d0ea7313c5241eca9e8b4567`
  - body_path: `sources/l1_datasets/tornado-cash-ofac-2022/relay_censorship_share.csv`
  > Slice [2025-03-07, 2025-04-04] — 29 days × 2 categories = 58 rows.
> Censoring-relay share: pre-event 14d mean 48.89% ± 1.21 (stable
> pre-delisting baseline); event-day (2025-03-21) 46.87%; post-event
> 14d mean 23.30% ± 23.87. The ≈25 pp post-event drop with high sd
> indicates bimodal days — some relays continued Tornado-filtering
> while others unwound within days. **First observed_change at
> L1 consensus tied to an OFAC delisting** in the dataset.
> attribution=direct because Wahrstätter's censoring-relay
> classifier is defined against the Tornado Cash SDN-listed
> addresses themselves, so a post-delisting drop in that specific
> metric is structurally tied to the delisting event.
- **`semi_primary_measurement`**
  - URL: <https://www.relayscan.io>
  - Wayback: <https://web.archive.org/web/20260421114750/https://www.relayscan.io/>
  - body_hash: `sha256:dc39f55922c657cd3caf22cdd77287f707ddec63ec0510091532f5fadc7aa827`
  - body_path: `sources/http_captures/tornado-cash-ofac-2022/l1-relay-dashboards/www.relayscan.io__capture__1a79bf8cec.html`
  > Relayscan independent dashboard — second source for the
> observed_change claim. Corroborates the post-delisting drop
> signal in the independent relay-monitoring pipeline.

## 4. No-change observations (where applicable)

### l3_rpc — `mev_blocker_filter_list_in_effect_no_step_change_attributable_to_this_event`

**Window**: `2025-03-21 00:00:00+00:00` → `2025-03-21 23:59:59+00:00`

**Sources**:

- **`primary_corporate`**
  - URL: <https://web.archive.org/web/20250111000329/https://mevblocker.io/>
  - Wayback: <https://web.archive.org/web/20250111000329/https://mevblocker.io/>
  - body_hash: `sha256:0d2b4d7e23011413f484943f6b9e1a28f4cf613f047e7e31d9c4daec7941bda3`
  - body_path: `sources/http_captures/_shared/l3-rpc-filter-list/web.archive.org__web-20250601000000-mevblocker.io__8282802587.html`
  > MEV-Blocker landing-page Wayback snapshot (2025-01-11) closest to
> event date 2025-03-21. MEV-Blocker (launched 2023-03-27) filters
> OFAC-SDN-listed addresses from the RPC substrate it serves. The
> snapshot documents that MEV-Blocker was in effect as a public
> OFAC-compliant RPC provider bracketing this event. No per-transaction
> receipt of filter-list application is published; the observation
> is the presence of the provider + filter-list at event time, not
> a step change attributable to this specific designation.
- **`primary_corporate`**
  - URL: <https://docs.flashbots.net/flashbots-protect/quick-start>
  - body_hash: `sha256:b937ed96974815d638d2db412ad674d417ae71f0295f625c8cec839638307282`
  - body_path: `sources/http_captures/_shared/l3-rpc-filter-list/docs.flashbots.net__flashbots-protect-quick-start__362faba1ef.html`
  > Second L3 anchor: Flashbots Protect documentation. Flashbots Protect
> (launched 2022-11) is the second major OFAC-compliance-adjacent
> public Ethereum RPC substrate. Together with MEV-Blocker these
> cover the overwhelming majority of public OFAC-compliant Ethereum
> RPC traffic in the 2023-2025 period.

## 5. Honest coverage gaps

- **l0_network** (`not_measured`): Reverse-cascade network effects have not been queried against Censored Planet / OONI and are plausibly sparse; no measurement artifact is attached so the layer is explicitly unmeasured
- **offramp_cex** (`not_measured`): Chain-analytics anchors pinned 2026-04-22 as primary_corporate

## 8. How to audit this chain

1. Clone the repository at `unknown`.
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

