# Evidence chain — `tether-okx-doj-pig-butchering-225m-freeze-2025-06`

**Status**: `admitted` · **Stratum**: `S3_doj_sec_cftc_fiod` · **Shape**: `comparison` (1 changed layer(s): `asset_onchain`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-08` · **Source commit**: `ee7bf1a` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-31` · **Tool version**: `0.1.0` · **Generated**: `2026-06-25T23:48:26Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "On 2025-06-18 DOJ filed a D.D.C. civil forfeiture complaint against
> 225,364,961 USDT in seven enumerated Ethereum USDT Token Groups A-G; the
> complaint ties those same addresses to a 2023-11-20 USSS-requested Tether
> freeze, and Ethereum logs show Tether burned the blacklisted balances in
> seven DestroyedBlackFunds transactions on 2025-06-18 before reissue
> pursuant to seizure. Single-layer asset_onchain observed_change,
> attribution=direct; kept draft because human admission is required."

## 1. Trigger

- **Type**: `doj_seizure_order`
- **Actor**: `us_doj_dc`
- **Timestamp**: `2025-06-18 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://www.justice.gov/opa/pr/united-states-files-civil-forfeiture-complaint-against-225m-funds-involved-cryptocurrency>
  - body_hash: `sha256:026aa203c614e21003febe02f00b3ef23a65201f68a40284832befe2e26d48b6`
  - body_path: `sources/http_captures/tether-okx-doj-pig-butchering-225m-freeze-2025-06/primary/www.justice.gov__opa-pr-united-states-files-civil-forfeiture-complaint-against-225m-funds-involved-cryptocurrency__881e12c00c.html`
  > DOJ OPA press release 2025-06-18: DOJ filed a civil forfeiture
> complaint in D.D.C. against more than $225.3M in cryptocurrency
> linked to cryptocurrency investment-fraud / confidence-scam money
> laundering. The release names USSS, FBI, USAO-DC, and CCIPS, states
> this was the largest USSS cryptocurrency seizure, and thanks Tether
> for proactive assistance. Local capture 2026-05-31.
- **`primary_legal`**
  - URL: <https://www.justice.gov/usao-dc/media/1403996/dl?inline=>
  - body_hash: `sha256:2134aba63aa003b2574401bb7ba94c10fa54970e82131baa747cdba0ebc8ae0b`
  - body_path: `sources/http_captures/tether-okx-doj-pig-butchering-225m-freeze-2025-06/primary/www.justice.gov__usao-dc-media-1403996-dl__2a4332ecd7.bin`
  > Verified Complaint for Forfeiture In Rem, United States v.
> Approximately 225,364,961 USDT, Civil Action No. 25-cv-1907
> (D.D.C.), filed 2025-06-18. The complaint enumerates seven Subject
> Virtual Currency Addresses (USDT Token Groups A-G), alleges that
> USSS requested Tether freeze approximately 225M USDT at those
> addresses on or around 2023-11-20, and states the token-group
> balances were burned and reissued pursuant to seizure.
- **`semi_primary_wayback`**
  - URL: <https://www.trmlabs.com/resources/blog/us-doj-announces-largest-ever-seizure-of-funds-related-to-crypto-scams>
  - Wayback: <https://web.archive.org/web/20260409233711/https://www.trmlabs.com/resources/blog/us-doj-announces-largest-ever-seizure-of-funds-related-to-crypto-scams>
  - body_hash: `sha256:50ad0a3b08e400b39c65a90948cdca45c725d851b027bd4ae2fbcf65ac9c48e7`
  - body_path: `sources/http_captures/tether-okx-doj-pig-butchering-225m-freeze-2025-06/primary/web.archive.org__web-20260409233711-https-www.trmlabs.com-resources-blog-us-doj-announces-largest-ever-seizure-of-funds-related-to-crypto-scams__0d14d7bd3b.html`
  > TRM Labs corroboration: approximately $225,364,961 USDT held
> across seven wallets ("USDT Token Groups A-G") was frozen with
> assistance from Tether and OKX; Tether burned the frozen tokens and
> reissued equivalent value to the US government.
- **`semi_primary_wayback`**
  - URL: <https://www.cnbc.com/2025/06/18/doj-crypto-scams.html>
  - Wayback: <https://web.archive.org/web/20260128145043/https://www.cnbc.com/2025/06/18/doj-crypto-scams.html>
  - body_hash: `sha256:6d42073efca881f4f19fb822df80a94f79afebfa4e4e4fb2045d32814c2ddb4f`
  - body_path: `sources/http_captures/tether-okx-doj-pig-butchering-225m-freeze-2025-06/primary/web.archive.org__web-20260128145043-https-www.cnbc.com-2025-06-18-doj-crypto-scams.html__e1478807da.html`
  > CNBC 2025-06-18 corroboration for the DOJ-DC civil forfeiture and
> largest-ever US scam-related crypto seizure framing.

## 2. Target

- **Kind**: `address_set`
- **Enumeration**: `complete`
- **Actor name**: Pig-butchering syndicate USDT Token Groups A-G
- **Chains**: `ethereum`
- **Addresses**: 7 total (enumerated in event YAML)

> Complete enumeration of the seven Subject Virtual Currency Addresses
> listed in the D.D.C. verified complaint as USDT Token Groups A-G. This
> is the complete forfeiture-property set, not the broader 144 OKX-account
> laundering network described in the complaint.

## 3. Changed-layer observations (supports the scoped claim)

### asset_onchain · attribution: `direct` · Δt = 8.5h

**Event label**: `tether_destroyed_blacklisted_225m_usdt_for_doj_dc_forfeiture`

**Timestamp**: `2025-06-18 08:29:47+00:00` (precision: `hour_range`)

**Sources**:

- **`primary_legal`**
  - URL: <https://www.justice.gov/usao-dc/media/1403996/dl?inline=>
  - body_hash: `sha256:2134aba63aa003b2574401bb7ba94c10fa54970e82131baa747cdba0ebc8ae0b`
  - body_path: `sources/http_captures/tether-okx-doj-pig-butchering-225m-freeze-2025-06/primary/www.justice.gov__usao-dc-media-1403996-dl__2a4332ecd7.bin`
  > Primary legal anchor for the seven-address target set, the
> 2023-11-20 USSS freeze request to Tether, and the burn/reissue
> framing. The complaint states each token group maintained its
> listed balance before the tokens were burned and reissued pursuant
> to seizure.
- **`primary_onchain`**
  - URL: <https://etherscan.io/tx/0x9236570580a19690a321f47803be08ba58d6d74addc3e54ded0353ce0d5f172d>
  - tx_hash: `0x9236570580a19690a321f47803be08ba58d6d74addc3e54ded0353ce0d5f172d`
  > USDT DestroyedBlackFunds for Token Group E
> 0xc76afbf0f69ae9be5d855239c50673252cf3f26b, amount
> 2,137,276.136 USDT, block 22730179 at 2025-06-18 08:29:47 UTC.
> Receipt cached under sources/onchain_receipts.
- **`primary_onchain`**
  - URL: <https://etherscan.io/tx/0xd2401fdccc2597f6ca00ec2e24ca48ac96310b1100360af0d8337d33cfa21c4b>
  - tx_hash: `0xd2401fdccc2597f6ca00ec2e24ca48ac96310b1100360af0d8337d33cfa21c4b`
  > USDT DestroyedBlackFunds for Token Group F
> 0x99ebaf3661065dc1e44feff4b80365678bdff6ce, amount
> 64,707,708.53 USDT, block 22730180 at 2025-06-18 08:29:59 UTC.
- **`primary_onchain`**
  - URL: <https://etherscan.io/tx/0x8ea3bca78393791db7e8f5e8deb20fd16b4fa654033ec3febd51c8c3fa598abb>
  - tx_hash: `0x8ea3bca78393791db7e8f5e8deb20fd16b4fa654033ec3febd51c8c3fa598abb`
  > USDT DestroyedBlackFunds for Token Group D
> 0x0b5453635e5325f5385ca1643c9e9eb173f9d5a8, amount
> 2,903,914.212488 USDT, block 22730180 at 2025-06-18 08:29:59 UTC.
- **`primary_onchain`**
  - URL: <https://etherscan.io/tx/0xfe6095c3f9cc9184d7620cbcf5eeae95cb8f24b2e63e5fb976bc4ca72a589a71>
  - tx_hash: `0xfe6095c3f9cc9184d7620cbcf5eeae95cb8f24b2e63e5fb976bc4ca72a589a71`
  > USDT DestroyedBlackFunds for Token Group G
> 0x82e1d4ddd636857ebcf6a0e74b9b0929c158d7fb, amount
> 87,464,642.259005 USDT, block 22730180 at 2025-06-18 08:29:59 UTC.
- **`primary_onchain`**
  - URL: <https://etherscan.io/tx/0x1c3feae280871f5638e41b9622e198268e636ea83940ccd2bd9c35c68fa9ff9e>
  - tx_hash: `0x1c3feae280871f5638e41b9622e198268e636ea83940ccd2bd9c35c68fa9ff9e`
  > USDT DestroyedBlackFunds for Token Group B
> 0x564e11ace70bfe6c943a973f1289faa6e8a0fe16, amount
> 30,000,000.35 USDT, block 22730180 at 2025-06-18 08:29:59 UTC.
- **`primary_onchain`**
  - URL: <https://etherscan.io/tx/0x65c93d03c1513045ddb1007e090ea5816b6d68bdef6786517f70b249913932ef>
  - tx_hash: `0x65c93d03c1513045ddb1007e090ea5816b6d68bdef6786517f70b249913932ef`
  > USDT DestroyedBlackFunds for Token Group C
> 0xcab9a8391f765f6beda0b5bad434b10985bdaad0, amount
> 8,737,741.569083 USDT, block 22730181 at 2025-06-18 08:30:11 UTC.
- **`primary_onchain`**
  - URL: <https://etherscan.io/tx/0x198c93baad1d3f7b8149f9c4ad218875e520e05bbd131a503bfca3ba97ab245c>
  - tx_hash: `0x198c93baad1d3f7b8149f9c4ad218875e520e05bbd131a503bfca3ba97ab245c`
  > USDT DestroyedBlackFunds for Token Group A
> 0xc7c8f8284c5360d0086a2f0a05bdd07afde23246, amount
> 29,413,680.82 USDT, block 22731274 at 2025-06-18 12:09:23 UTC.
- **`primary_onchain`**
  - URL: <https://etherscan.io/tx/0x6f2ee4e620f7ad9424746dc66bc0d59177769ab4162c152abc50735a1fb900d9>
  - tx_hash: `0x6f2ee4e620f7ad9424746dc66bc0d59177769ab4162c152abc50735a1fb900d9`
  > Pre-seizure USDT AddedBlackList anchor for Token Group E,
> block 18613308 at 2023-11-20 13:30:11 UTC.
- **`primary_onchain`**
  - URL: <https://etherscan.io/tx/0x27daa9b2a7feecfd9036f4c45eec44e9f06733e074d8ce222637201506855f0c>
  - tx_hash: `0x27daa9b2a7feecfd9036f4c45eec44e9f06733e074d8ce222637201506855f0c`
  > Pre-seizure USDT AddedBlackList anchor for Token Group F,
> block 18613312 at 2023-11-20 13:30:59 UTC.
- **`primary_onchain`**
  - URL: <https://etherscan.io/tx/0x1cba0d1237187bc409bdf02b1b54c2b848ad7e959d7229b48d13e13af042d769>
  - tx_hash: `0x1cba0d1237187bc409bdf02b1b54c2b848ad7e959d7229b48d13e13af042d769`
  > Pre-seizure USDT AddedBlackList anchor for Token Group D,
> block 18613313 at 2023-11-20 13:31:11 UTC.
- **`primary_onchain`**
  - URL: <https://etherscan.io/tx/0x9663efbd994469f8660b26efb553b23b16aa93a7fb531f04639ceaee2f5e4542>
  - tx_hash: `0x9663efbd994469f8660b26efb553b23b16aa93a7fb531f04639ceaee2f5e4542`
  > Pre-seizure USDT AddedBlackList anchor for Token Group G,
> block 18613315 at 2023-11-20 13:31:35 UTC.
- **`primary_onchain`**
  - URL: <https://etherscan.io/tx/0x0af2ed54fae51aab459873f8e97d8996810a7b19bb20615769c81d4a47ebab66>
  - tx_hash: `0x0af2ed54fae51aab459873f8e97d8996810a7b19bb20615769c81d4a47ebab66`
  > Pre-seizure USDT AddedBlackList anchor for Token Group B,
> block 18613316 at 2023-11-20 13:31:47 UTC.
- **`primary_onchain`**
  - URL: <https://etherscan.io/tx/0x4ae05726cfb0dd0c2eaba70fe63a1a7848fb57f8a4f6efb5f72e290bd9141d1e>
  - tx_hash: `0x4ae05726cfb0dd0c2eaba70fe63a1a7848fb57f8a4f6efb5f72e290bd9141d1e`
  > Pre-seizure USDT AddedBlackList anchor for Token Group C,
> block 18613318 at 2023-11-20 13:32:11 UTC.
- **`primary_onchain`**
  - URL: <https://etherscan.io/tx/0x3769cb9daa98464d086855d82f2327864778fe7c9b6bb2109d46b2f6d0900d0e>
  - tx_hash: `0x3769cb9daa98464d086855d82f2327864778fe7c9b6bb2109d46b2f6d0900d0e`
  > Pre-seizure USDT AddedBlackList anchor for Token Group A,
> block 18613319 at 2023-11-20 13:32:23 UTC.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`tether-doj-pig-butchering-freeze-2023`](./tether-doj-pig-butchering-freeze-2023.md)
- [`tether-pig-butchering-second-wave-2024`](./tether-pig-butchering-second-wave-2024.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `ee7bf1a`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

