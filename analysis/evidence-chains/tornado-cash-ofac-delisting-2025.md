# Evidence chain — `tornado-cash-ofac-delisting-2025`

**Status**: `admitted` · **Stratum**: `S2_ofac_removal` · **Shape**: `cascade` (4 changed layer(s): `asset_onchain`, `l1_consensus`, `l3_rpc`, `l4_frontend`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-02` · **Source commit**: `c736a32` · **Schema**: `0.2.0` · **Event last_verified**: `2026-04-21` · **Tool version**: `0.1.0` · **Generated**: `2026-06-02T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "OFAC delisting of Tornado Cash on 2025-03-21 (Van Loon-litigation driven)
> is the first reverse-cascade event in the dataset, producing observed_change
> on 3 layers: L1 consensus censoring-relay share dropped ≈25pp within 14
> days; Circle USDC unblacklisted at least one historical address; and L4
> frontend access/listing partially reemerged via maintained UI paths while
> canonical-domain restoration remained incomplete. Establishes structural
> asymmetry between cascade and reverse-cascade shapes: rollback is slower and
> patchier than the original cascade."

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
  - tx_hash: `0x1c2fbd8b25f201327e0b469164ab753c89a802de7e0768e4e278d224cc10b25a`
  > USDC unblacklist transaction for target address 0x47CE0C6eD5B0Ce3d3A51fdb1C52DC66a7c3c2936 on 2025-03-22
- **`supporting_community`**
  - URL: <https://usdtbanlist.com/address/0x47CE0C6eD5B0Ce3d3A51fdb1C52DC66a7c3c2936>
  - Wayback: <https://web.archive.org/web/20260421105924/https://usdtbanlist.com/address/0x47CE0C6eD5B0Ce3d3A51fdb1C52DC66a7c3c2936>
  - body_hash: `sha256:796e56678deaefeb73773354336dcb4f75b0770e7ebc3c45f3e9dedc1fd73363`
  - body_path: `sources/http_captures/tornado-cash-ofac-delisting-2025/backfill-1.3/usdtbanlist.com__address-0x47CE0C6eD5B0Ce3d3A51fdb1C52DC66a7c3c2936__a06f6feca5.html`
  > Third-party cross-check showing the same address was USDC-unbanned on 2025-03-22 with the matching Etherscan transaction

### l3_rpc · attribution: `plausible` · Δt = 283.47h

**Event label**: `ofac_blacklist_deletion`

**Timestamp**: `2025-04-01 19:28:21+00:00` (precision: `second`)

**Sources**:

- **`primary_corporate`**
  - URL: <https://github.com/flashbots/rpc-endpoint/commit/1e9c29c5d3896bdc661805f4995b4d65834db6e4>
  - body_hash: `sha256:429579b63e4b00b580aa4588af966e0762a4d1b6eb88984888289c3d689638c3`
  - body_path: `sources/operator_commits/tornado-cash-ofac-delisting-2025/ofacblacklist-at-1e9c29c.go`
  > Post-commit state of server/ofacblacklist.go at commit 1e9c29c:
> file reduced to a 205-byte stub with zero addresses. Diff
> removes the `ofacBlacklist` map (135 lines deleted, 0 added;
> `rg '"0x[0-9a-f]{40}"' count = 0`). Pre-deletion state (at
> commit 1e9c29c^) preserved locally at
> sources/operator_commits/tornado-cash-ofac-delisting-2025/ofacblacklist-pre-1e9c29c.go
> (body_hash sha256:9f609132996f37febf1de1283a44b34b0e77fb80324dfc747231dfb16281c54a,
> 132 addresses including Tornado pools).
- **`primary_corporate`**
  - URL: <https://github.com/flashbots/rpc-endpoint/pull/173>
  - body_hash: `sha256:75c7c402e89b2f0ec46fe8baac4e6f9b64023c2f62580e5424eeaa10349393d3`
  - body_path: `sources/operator_commits/tornado-cash-ofac-delisting-2025/commit-1e9c29c.meta.txt`
  > Commit metadata: title "Cleanup unused and unmaintained
> blacklist file (#173)", PR title "Cleanup unused, outdated
> blacklist defaults", author Chris Hager (metachris), merged
> 2025-04-01T19:28:21Z UTC (11 days 19 hours 28 minutes after
> OFAC delisted Tornado Cash on 2025-03-21). Full diff at
> sources/operator_commits/tornado-cash-ofac-delisting-2025/commit-1e9c29c.diff.
- **`semi_primary_measurement`**
  - URL: <https://api.github.com/repos/flashbots/rpc-endpoint/pulls/173>
  - body_hash: `sha256:a800191f0391c2304542a60647bc3a0ca2db76a60fbc636d83d7bdfcd9bef9e3`
  - body_path: `sources/operator_commits/tornado-cash-ofac-delisting-2025/github-api/pr-173.response.json`
  > Independent GitHub API confirmation of organizational
> provenance: `base.repo.full_name = "flashbots/rpc-endpoint"`,
> `merged = true`, `merged_at = 2025-04-01T19:28:21Z`,
> `merge_commit_sha = 1e9c29c…`. Served by GitHub Inc.
> (not Flashbots); rules out fork / unofficial-commit readings.
- **`semi_primary_measurement`**
  - URL: <https://api.github.com/repos/flashbots/rpc-endpoint/commits/1e9c29c5d3896bdc661805f4995b4d65834db6e4>
  - body_hash: `sha256:63d666d38777830bd3c2962df0b96d6966c0e464de78bf0df82b2a5c653315bb`
  - body_path: `sources/operator_commits/tornado-cash-ofac-delisting-2025/github-api/commit.response.json`
  > Independent GitHub API commit confirmation:
> `sha = 1e9c29c…`, `commit.author.date = 2025-04-01T19:28:21Z`.
> The commit message and PR title both frame the deletion as
> operational cleanup ("Cleanup unused and unmaintained
> blacklist file"), NOT as an explicit policy response to the
> Tornado delisting — this is why the observation's attribution
> stays `plausible` rather than `direct`.

### l1_consensus · attribution: `plausible` · Δt = 0h

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
> attribution=plausible (not direct) because the only evidence
> anchors are two semi-primary measurement sources; no primary
> relay/builder policy statement corroborates the drop. The
> classifier's definition against the Tornado-Cash SDN addresses
> makes the signal structurally meaningful, but under the validator's
> attribution=direct ⇒ primary_* rule (added 2026-04-22) this
> observation is retained at the plausible tier.
- **`semi_primary_measurement`**
  - URL: <https://www.relayscan.io>
  - Wayback: <https://web.archive.org/web/20260421114750/https://www.relayscan.io/>
  - body_hash: `sha256:dc39f55922c657cd3caf22cdd77287f707ddec63ec0510091532f5fadc7aa827`
  - body_path: `sources/http_captures/tornado-cash-ofac-2022/l1-relay-dashboards/www.relayscan.io__capture__1a79bf8cec.html`
  > Relayscan independent dashboard — second source for the
> observed_change claim. Corroborates the post-delisting drop
> signal in the independent relay-monitoring pipeline.

## 5. Honest coverage gaps

- **l0_network** (`not_measured`): L0 coverage is an explicit measurement gap, framed to match the
- **offramp_cex** (`not_measured`): Chain-analytics anchors pinned 2026-04-22 as primary_corporate

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `c736a32`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

