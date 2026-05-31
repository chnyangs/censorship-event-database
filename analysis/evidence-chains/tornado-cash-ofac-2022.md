# Evidence chain — `tornado-cash-ofac-2022`

**Status**: `admitted` · **Stratum**: `S1_ofac_sdn` · **Shape**: `cascade` (5 changed layer(s): `asset_onchain`, `l1_consensus`, `l3_rpc`, `l4_frontend`, `offramp_cex`) · **Tier**: `anchor_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `e405eb6` · **Schema**: `0.2.0` · **Event last_verified**: `2026-04-21` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "OFAC designation of Tornado Cash on 2022-08-08 produced the defining
> 3-layer cascade in the dataset: L4 frontend (tornado.cash taken offline
> ≈22h), asset_onchain (Circle USDC batch-blacklisted 19/38 addresses
> within 6h; dYdX closed accounts within 34h), and L1 consensus (censoring-
> relay share rose from 10.80% day-1 of PBS era to 41.10% 18 days later).
> The paper-defining original-cascade event, paired with the 2025-03-21
> delisting reverse-cascade."

## 1. Trigger

- **Type**: `ofac_sdn_designation`
- **Actor**: `US_OFAC`
- **Timestamp**: `2022-08-08 13:30:00+00:00` (precision: `hour`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://ofac.treasury.gov/recent-actions/20220808>
  - Wayback: <https://web.archive.org/web/20260421104932/https://ofac.treasury.gov/recent-actions/20220808>
  - body_hash: `sha256:ae648b941c311222db9899ba95ed4711ef1f8083fe5bf5c89fb5805b0268bc79`
  - body_path: `sources/http_captures/tornado-cash-ofac-2022/ofac-recent-actions/ofac.treasury.gov__recent-actions-20220808__298acbc03a.html`
  > OFAC Recent Actions page for 2022-08-08 Cyber-related Designation naming Tornado Cash; the 38 Ethereum addresses in target.addresses are extracted verbatim from this archived page
- **`primary_legal`**
  - URL: <https://ofac.treasury.gov/specially-designated-nationals-list-sdn-list/archive-of-changes-to-the-sdn-list>
  > Official OFAC archive-of-changes landing page for SDN updates, including the 2022 archive entries that record list additions and modifications

## 2. Target

- **Kind**: `address_set`
- **Enumeration**: `complete`
- **Protocol**: `tornado_cash`
- **Chains**: `ethereum`
- **Addresses**: 38 total (enumerated in event YAML)
- **Canonical domains**: `tornado.cash`, `app.tornado.cash`, `tornadocash.eth.link`

> Full set of 38 unique Ethereum addresses extracted from the OFAC Recent Actions page for 2022-08-08 (archived locally and on Wayback; see trigger.citation[0]). Address casing preserved as published by OFAC. The 2022-11-08 secondary designations are a separate event and are not included here.

## 3. Changed-layer observations (supports the scoped claim)

### l1_consensus · attribution: `plausible` · Δt = 922.5h

**Event label**: `ofac_compliant_relay_share_rises_post_merge`

**Timestamp**: `2022-09-16 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`semi_primary_measurement`**
  - URL: <https://raw.githubusercontent.com/nerolation/censorship.pics/main/data/relay_censorship_share.csv>
  - body_hash: `sha256:45c1db9ca70491743e2e33c313d7293eed791a82d0ea7313c5241eca9e8b4567`
  - body_path: `sources/l1_datasets/tornado-cash-ofac-2022/relay_censorship_share.csv`
  > Daily per-relay OFAC-compliance share from Wahrstätter's
> relay_censorship_share.csv (nerolation/censorship.pics repo, main
> branch). The slice 2022-09-16 to 2022-10-03 has 36 rows (18 days
> × 2 categories {censoring, non-censoring}). Censoring-relay share
> rises from 10.80% on 2022-09-16 (day 1 of the PBS era, 39 days
> post-trigger) to 41.10% on 2022-10-03. Slice query_hash is the
> sha256 of the sorted slice JSON so the exact rows are content-
> addressable. attribution=plausible (downgraded from direct per
> 2026-Q2 adversarial audit): Wahrstätter's classification of a
> block as "censoring" is defined against the Tornado Cash SDN-listed
> addresses, but no primary relay-operator statement in-this-event
> explicitly names Tornado Cash as the reason for filter adoption,
> so per audit protocol §3 direct attribution is not structurally
> earned by semi-primary measurement alone.
- **`semi_primary_measurement`**
  - URL: <https://censorship.pics>
  - Wayback: <https://web.archive.org/web/20260223040258/https://censorship.pics/>
  - body_hash: `sha256:9de85e492e8742bd9870c72cc00c9acfc26044fdcc1b6d1b88a69dda3c0fb5bd`
  - body_path: `sources/http_captures/tornado-cash-ofac-2022/l1-relay-dashboards/censorship.pics__capture__5bc3a85424.html`
  > Operator-facing dashboard rendering of the same underlying daily-share dataset; grouped with the CSV source as one evidence unit.
- **`semi_primary_measurement`**
  - URL: <https://www.relayscan.io>
  - Wayback: <https://web.archive.org/web/20260421114750/https://www.relayscan.io/>
  - body_hash: `sha256:dc39f55922c657cd3caf22cdd77287f707ddec63ec0510091532f5fadc7aa827`
  - body_path: `sources/http_captures/tornado-cash-ofac-2022/l1-relay-dashboards/www.relayscan.io__capture__1a79bf8cec.html`
  > Independent ecosystem ranking page (operated by Flashbots) that tracks per-relay OFAC-compliance over time; independent of Wahrstätter's pipeline and serves as the second admission-grade source for this observation.

### l3_rpc · attribution: `direct` · Δt = 2.85h

**Event label**: `ofac_blacklist_addition_of_tornado_pool_addresses`

**Timestamp**: `2022-08-08 16:20:50+00:00` (precision: `second`)

**Sources**:

- **`primary_corporate`**
  - URL: <https://github.com/flashbots/rpc-endpoint/commit/92ab6b1f9abfc62261f72361e8c8df48f832f2a9>
  - body_hash: `sha256:86c81be4b409fc14aeed31abede8f3b74e7382d128ceec678a4c151ce9a959e7`
  - body_path: `sources/operator_commits/tornado-cash-ofac-2022/ofacblacklist-at-92ab6b1.go`
  > Post-commit state of server/ofacblacklist.go at flashbots/rpc-endpoint
> commit 92ab6b1f (Mon 2022-08-08 16:20:50 UTC). Contains 55
> OFAC SDN addresses including the Tornado Cash pool addresses
> 0x722122df..., 0x8589427..., 0x4736dcf1..., all of which
> appear in this event's target.addresses list. Commit diff
> (sha256:220a5d31560da244c79a2539f4784a394752b0985d4c444a5f61fc664cf9d4f6)
> shows these addresses being added in the same commit; see
> sources/operator_commits/tornado-cash-ofac-2022/commit-92ab6b1.diff.
- **`primary_corporate`**
  - URL: <https://github.com/flashbots/rpc-endpoint/pull/90>
  - body_hash: `sha256:0c4fafa03fe45219b1f7e6d9c6487b05982922ae4104666cba79f098009946b9`
  - body_path: `sources/operator_commits/tornado-cash-ofac-2022/commit-92ab6b1.meta.txt`
  > Commit metadata: title "update ofac black list (#90)", author
> Bhakiyaraj Kalimuthu, commit date 2022-08-08T18:20:50+02:00
> = 2022-08-08T16:20:50Z UTC (cross-checked against GitHub PR
> #90 merged_at). The full diff showing exactly which
> addresses were added is preserved at
> sources/operator_commits/tornado-cash-ofac-2022/commit-92ab6b1.diff.
- **`semi_primary_measurement`**
  - URL: <https://api.github.com/repos/flashbots/rpc-endpoint/pulls/90>
  - body_hash: `sha256:affdc83394ae6abf0c5c549716bd2ae8909800e3466b8149294d394e13fcac41`
  - body_path: `sources/operator_commits/tornado-cash-ofac-2022/github-api/pr-90.response.json`
  > Independent GitHub API confirmation of organizational
> provenance: `base.repo.full_name = "flashbots/rpc-endpoint"`,
> `merged = true`, `merged_at = 2022-08-08T16:20:51Z`,
> `merge_commit_sha = 92ab6b1f…`. Served by GitHub Inc.
> (not Flashbots); the response is a third-party measurement
> of the repository state that rules out the "one developer's
> fork" alternative reading of the git-side sources above.
- **`semi_primary_measurement`**
  - URL: <https://api.github.com/repos/flashbots/rpc-endpoint/commits/92ab6b1f9abfc62261f72361e8c8df48f832f2a9>
  - body_hash: `sha256:5ed6923bcc1c9b3ed33599e20dd5df645930c3c343ffe0e883eb6f62140c99f5`
  - body_path: `sources/operator_commits/tornado-cash-ofac-2022/github-api/commit.response.json`
  > Independent GitHub API confirmation of commit content.
> `sha = 92ab6b1f…`, `commit.author.date = 2022-08-08T16:20:50Z`,
> `commit.message` expands the single-line title into five
> sub-commit descriptions: "update ofac black list", "add more
> address", "more ofac addresses", "convert ofac list to lower
> case", "add ofac test" — the word "ofac" appears four times
> in the committer's own message. This rules out the "incidental
> cleanup that happened to include Tornado addresses"
> alternative reading.

### asset_onchain · attribution: `direct` · Δt = 5.93h

**Event label**: `address_blacklisted`

**Timestamp**: `2022-08-08 19:25:35+00:00` (precision: `second`)

**Sources**:

- **`primary_onchain`**
  - URL: <https://etherscan.io/tx/0xa61326744a21ce8d5397831d107ee14909b3f4eaaaddbf1f3dce879a19e30dd9>
  - tx_hash: `0xa61326744a21ce8d5397831d107ee14909b3f4eaaaddbf1f3dce879a19e30dd9`
  > USDC blacklist transaction for target address 0x8589427373D6D84E98730D7795D8f6f8731FDA16 on 2022-08-08
- **`supporting_community`**
  - URL: <https://usdtbanlist.com/address/0x8589427373d6d84e98730d7795d8f6f8731fda16>
  - Wayback: <https://web.archive.org/web/20260421105443/https://usdtbanlist.com/address/0x8589427373d6d84e98730d7795d8f6f8731fda16>
  - body_hash: `sha256:b37912e4c65777c8c934d2ffcd793506aff9665de6a2f78ab2fdfa3e71a65785`
  - body_path: `sources/http_captures/tornado-cash-ofac-2022/backfill-1.3/usdtbanlist.com__address-0x8589427373d6d84e98730d7795d8f6f8731fda16__1862a2f7aa.html`
  > Third-party cross-check showing the same address was USDC-banned on 2022-08-08 with the matching Etherscan transaction
- **`primary_corporate`**
  - URL: <https://www.circle.com/blog/ofacs-designation-of-tornado-cash-protocols-privacy-and-a-call-to-action>
  - Wayback: <https://web.archive.org/web/20260421105602/https://www.circle.com/blog/ofacs-designation-of-tornado-cash-protocols-privacy-and-a-call-to-action>
  - body_hash: `sha256:fe0c8bbff7b5e96a1c9d94884be7798891926a86beee059268d1377d8ee2e435`
  - body_path: `sources/http_captures/tornado-cash-ofac-2022/backfill-1.3/www.circle.com__blog-ofacs-designation-of-tornado-cash-protocols-privacy-and-a-call-to-action__f24a980b38.html`
  > Circle policy response published on 2022-08-12; corroborates the asset-layer reaction context though the on-chain receipt remains authoritative

### l4_frontend · attribution: `plausible` · Δt = 22.5h

**Event label**: `ui_unavailable`

**Timestamp**: `2022-08-09 12:00:00+00:00` (precision: `hour`)

**Sources**:

- **`semi_primary_measurement`**
  - URL: <https://github.com/tornadocash>
  - Wayback: <https://web.archive.org/web/20260421105622/https://github.com/tornadocash>
  - body_hash: `sha256:c79b19d9b75040f9a6cee65ca8411eff4a450281d3137db08fe9042364931c57`
  - body_path: `sources/http_captures/tornado-cash-ofac-2022/backfill-1.3/github.com__tornadocash__7f33190afd.html`
  > GitHub org availability and repository archival status around the event
- **`semi_primary_measurement`**
  - URL: <https://github.com/tornadocash/tornado-core>
  - Wayback: <https://web.archive.org/web/20260421105714/https://github.com/tornadocash/tornado-core>
  - body_hash: `sha256:9036173422a3031172e9e81999fbf39f801b75e2b4ad245298cb25a0bb268209`
  - body_path: `sources/http_captures/tornado-cash-ofac-2022/backfill-1.3/github.com__tornadocash-tornado-core__9430a15343.html`
  > GitHub repo availability change, archive state, commit history, or bundle diff

### offramp_cex · attribution: `direct` · Δt = 34.5h

**Event label**: `accounts_flagged_and_close_only_mode`

**Timestamp**: `2022-08-10 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_corporate`**
  - URL: <https://dydx.exchange/blog/tornado-outage>
  - body_hash: `sha256:36962450314fb0560074887dffe194a9a7b5b98363ba47e982c4102192d4a904`
  - body_path: `sources/http_captures/tornado-cash-ofac-2022/backfill-1.3/dydx.exchange__blog-tornado-outage__4d80cd1762.html`
  > dYdX post on 2022-08-10 describing account blocks tied to Tornado Cash sanctions exposure
- **`primary_corporate`**
  - URL: <https://dydx.exchange/blog/tornado-cash-update>
  - Wayback: <https://web.archive.org/web/20260421105743/https://dydx.exchange/blog/tornado-cash-update>
  - body_hash: `sha256:1d19ee8f5269e300567286d4fc4f263f8158934cd2d4ef05047dcf54781624dd`
  - body_path: `sources/http_captures/tornado-cash-ofac-2022/backfill-1.3/dydx.exchange__blog-tornado-cash-update__83f9281763.html`
  > dYdX follow-up post on 2022-08-29 describing updated compliance settings and reduced blocking scope

## 5. Honest coverage gaps

- **l0_network** (`not_measured`): L0 network-layer OONI API query performed 2026-04-22. Searched the

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `e405eb6`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

