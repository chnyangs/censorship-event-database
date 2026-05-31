# Evidence chain — `tether-doj-pig-butchering-freeze-2023`

**Status**: `admitted` · **Stratum**: `S5_corporate` · **Shape**: `comparison` (2 changed layer(s): `asset_onchain`, `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `eabcaae` · **Schema**: `0.2.0` · **Event last_verified**: `2026-04-22` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "Tether's 2023-11-20 freeze of $225M USDT linked to a Southeast Asia
> pig-butchering syndicate — executed at DOJ/USSS request without any
> corresponding OFAC SDN listing — documents the DOJ-request-driven mode of
> stablecoin-issuer freeze action. A later D.D.C. complaint enumerates seven
> USDT Token Group addresses in this path, and the seven corresponding
> Tether AddedBlackList transactions are pinned as primary_onchain
> evidence. Completes the 3-mode Tether compliance spectrum
> (OFAC-reactive / OFAC-preemptive / DOJ-request-only) at S5."

## 1. Trigger

- **Type**: `corporate_policy_change`
- **Actor**: `tether_usdt_issuer`
- **Timestamp**: `2023-11-20 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_corporate`**
  - URL: <https://tether.to/en/tether-freezes-225-million-linked-to-international-human-trafficking-syndicate/>
  - body_hash: `sha256:c37819595db98b24face1d35241c4c62a5fe0dc3fa6606450e17c25c6505c114`
  - body_path: `sources/http_captures/tether-doj-pig-butchering-freeze-2023/primary/tether.to__en-tether-freezes-225-million-linked-to-international-human-trafficking-syndicate__ae3e393bc3.html`
  > Tether official blog post (2023-11-20): "Tether Freezes $225 Million
> Linked to International Human Trafficking Syndicate." First publicly
> announced Tether freeze action **explicitly at DOJ request** rather
> than in response to OFAC SDN designation. Coordination partners
> named: U.S. Secret Service (USSS), U.S. Department of Justice DOJ,
> and OKX exchange. Freeze covers wallets linked to "pig butchering"
> romance-scam syndicate in Southeast Asia. **No OFAC SDN listing was
> issued for the target addresses** — this is pure DOJ-request-driven
> freeze, distinct from all prior Tether freeze events in the dataset.
- **`primary_legal`**
  - URL: <https://www.justice.gov/usao-edva/pr/united-states-files-civil-forfeiture-complaint-seeking-recovery-over-112-million-crypto>
  - body_hash: `sha256:be9f63130d3a946049f43e8cb2d8a2a4bbeb0b21fcff76600646f9a141a7d9f0`
  - body_path: `sources/http_captures/tether-doj-pig-butchering-freeze-2023/primary/www.justice.gov__usao-edva-pr-united-states-files-civil-forfeiture-complaint-seeking-recovery-over-112-million-crypto__3f4a45e92b.html`
  > DOJ EDVA civil forfeiture companion filing — parallel DOJ action
> seeking recovery of $112M+ in crypto connected to the same
> pig-butchering scam network. Confirms the DOJ-request framing of
> the Tether freeze: DOJ identifies targets + files civil forfeiture;
> Tether freezes USDT holdings of those targets. Second-anchor
> primary_legal artifact for the freeze's causal chain.
- **`primary_legal`**
  - URL: <https://www.justice.gov/usao-dc/media/1403996/dl?inline=>
  - body_hash: `sha256:2134aba63aa003b2574401bb7ba94c10fa54970e82131baa747cdba0ebc8ae0b`
  - body_path: `sources/http_captures/tether-doj-pig-butchering-freeze-2023/primary/www.justice.gov__usao-dc-media-1403996-dl__2a4332ecd7.bin`
  > D.D.C. verified complaint filed 2025-06-18 in United States v.
> Approximately 225,364,961 USDT. Retrospective primary_legal anchor:
> the complaint enumerates seven Subject Virtual Currency Addresses
> (USDT Token Groups A-G) and states that on or around 2023-11-20 USSS
> requested Tether voluntarily freeze approximately 225M USDT at
> those addresses.

## 2. Target

- **Kind**: `address_set`
- **Enumeration**: `subset`
- **Actor name**: Pig-butchering / romance-scam network
- **Chains**: `ethereum`
- **Addresses**: 7 total (enumerated in event YAML)

> Pig-butchering syndicate wallet cluster with ~$225M USDT total frozen.
> Tether's 2023 blog reports the aggregate freeze but does not enumerate
> every wallet. The later D.D.C. verified complaint enumerates seven
> Subject Virtual Currency Addresses (USDT Token Groups A-G) within the
> same $225M freeze / forfeiture path; those seven are pinned below.
> Other wallets in the broader 37-39 wallet freeze cohort remain
> unenumerated here, so enumeration stays subset rather than complete.

## 3. Changed-layer observations (supports the scoped claim)

### asset_onchain · attribution: `direct` · Δt = 13.5h

**Event label**: `tether_added_blacklist_for_doj_usss_pig_butchering_cluster`

**Timestamp**: `2023-11-20 13:30:11+00:00` (precision: `hour_range`)

**Sources**:

- **`primary_legal`**
  - URL: <https://www.justice.gov/usao-dc/media/1403996/dl?inline=>
  - body_hash: `sha256:2134aba63aa003b2574401bb7ba94c10fa54970e82131baa747cdba0ebc8ae0b`
  - body_path: `sources/http_captures/tether-doj-pig-butchering-freeze-2023/primary/www.justice.gov__usao-dc-media-1403996-dl__2a4332ecd7.bin`
  > The D.D.C. complaint provides the retrospective primary_legal
> bridge between the 2023 Tether/USSS freeze and the seven
> enumerated USDT Token Group addresses. It states USSS requested
> Tether voluntarily freeze approximately 225M USDT at the Subject
> Virtual Currency Addresses on or around 2023-11-20.
- **`primary_onchain`**
  - URL: <https://etherscan.io/tx/0x6f2ee4e620f7ad9424746dc66bc0d59177769ab4162c152abc50735a1fb900d9>
  - tx_hash: `0x6f2ee4e620f7ad9424746dc66bc0d59177769ab4162c152abc50735a1fb900d9`
  > USDT AddedBlackList for Token Group E
> 0xc76afbf0f69ae9be5d855239c50673252cf3f26b, block 18613308 at
> 2023-11-20 13:30:11 UTC. Receipt cached under
> sources/onchain_receipts/tether-doj-pig-butchering-freeze-2023/.
- **`primary_onchain`**
  - URL: <https://etherscan.io/tx/0x27daa9b2a7feecfd9036f4c45eec44e9f06733e074d8ce222637201506855f0c>
  - tx_hash: `0x27daa9b2a7feecfd9036f4c45eec44e9f06733e074d8ce222637201506855f0c`
  > USDT AddedBlackList for Token Group F
> 0x99ebaf3661065dc1e44feff4b80365678bdff6ce, block 18613312 at
> 2023-11-20 13:30:59 UTC.
- **`primary_onchain`**
  - URL: <https://etherscan.io/tx/0x1cba0d1237187bc409bdf02b1b54c2b848ad7e959d7229b48d13e13af042d769>
  - tx_hash: `0x1cba0d1237187bc409bdf02b1b54c2b848ad7e959d7229b48d13e13af042d769`
  > USDT AddedBlackList for Token Group D
> 0x0b5453635e5325f5385ca1643c9e9eb173f9d5a8, block 18613313 at
> 2023-11-20 13:31:11 UTC.
- **`primary_onchain`**
  - URL: <https://etherscan.io/tx/0x9663efbd994469f8660b26efb553b23b16aa93a7fb531f04639ceaee2f5e4542>
  - tx_hash: `0x9663efbd994469f8660b26efb553b23b16aa93a7fb531f04639ceaee2f5e4542`
  > USDT AddedBlackList for Token Group G
> 0x82e1d4ddd636857ebcf6a0e74b9b0929c158d7fb, block 18613315 at
> 2023-11-20 13:31:35 UTC.
- **`primary_onchain`**
  - URL: <https://etherscan.io/tx/0x0af2ed54fae51aab459873f8e97d8996810a7b19bb20615769c81d4a47ebab66>
  - tx_hash: `0x0af2ed54fae51aab459873f8e97d8996810a7b19bb20615769c81d4a47ebab66`
  > USDT AddedBlackList for Token Group B
> 0x564e11ace70bfe6c943a973f1289faa6e8a0fe16, block 18613316 at
> 2023-11-20 13:31:47 UTC.
- **`primary_onchain`**
  - URL: <https://etherscan.io/tx/0x4ae05726cfb0dd0c2eaba70fe63a1a7848fb57f8a4f6efb5f72e290bd9141d1e>
  - tx_hash: `0x4ae05726cfb0dd0c2eaba70fe63a1a7848fb57f8a4f6efb5f72e290bd9141d1e`
  > USDT AddedBlackList for Token Group C
> 0xcab9a8391f765f6beda0b5bad434b10985bdaad0, block 18613318 at
> 2023-11-20 13:32:11 UTC.
- **`primary_onchain`**
  - URL: <https://etherscan.io/tx/0x3769cb9daa98464d086855d82f2327864778fe7c9b6bb2109d46b2f6d0900d0e>
  - tx_hash: `0x3769cb9daa98464d086855d82f2327864778fe7c9b6bb2109d46b2f6d0900d0e`
  > USDT AddedBlackList for Token Group A
> 0xc7c8f8284c5360d0086a2f0a05bdd07afde23246, block 18613319 at
> 2023-11-20 13:32:23 UTC.

### offramp_cex · attribution: `direct` · Δt = 0h

**Event label**: `tether_froze_225m_at_doj_request_non_ofac_trigger`

**Timestamp**: `2023-11-20 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_corporate`**
  - URL: <https://tether.to/en/tether-freezes-225-million-linked-to-international-human-trafficking-syndicate/>
  - body_hash: `sha256:c37819595db98b24face1d35241c4c62a5fe0dc3fa6606450e17c25c6505c114`
  - body_path: `sources/http_captures/tether-doj-pig-butchering-freeze-2023/primary/tether.to__en-tether-freezes-225-million-linked-to-international-human-trafficking-syndicate__ae3e393bc3.html`
  > Tether blog explicitly announces the freeze + names USSS, DOJ,
> and OKX as coordination partners. Direct attribution: issuer
> itself is the actor; the action is announced simultaneously with
> execution. First concrete public example in the dataset of Tether
> executing a non-OFAC-driven freeze.
- **`primary_legal`**
  - URL: <https://www.justice.gov/usao-edva/pr/united-states-files-civil-forfeiture-complaint-seeking-recovery-over-112-million-crypto>
  - body_hash: `sha256:be9f63130d3a946049f43e8cb2d8a2a4bbeb0b21fcff76600646f9a141a7d9f0`
  - body_path: `sources/http_captures/tether-doj-pig-butchering-freeze-2023/primary/www.justice.gov__usao-edva-pr-united-states-files-civil-forfeiture-complaint-seeking-recovery-over-112-million-crypto__3f4a45e92b.html`
  > DOJ EDVA civil-forfeiture filing corroborating the DOJ-driven
> framing. Independent primary_legal artifact.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`tether-retroactive-sweep-2023`](./tether-retroactive-sweep-2023.md)
- [`tether-dprk-precommit-freeze-2025`](./tether-dprk-precommit-freeze-2025.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `eabcaae`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

