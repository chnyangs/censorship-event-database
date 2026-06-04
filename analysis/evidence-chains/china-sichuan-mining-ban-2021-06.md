# Evidence chain — `china-sichuan-mining-ban-2021-06`

**Status**: `admitted` · **Stratum**: `S4_nation_state` · **Shape**: `comparison` (1 changed layer(s): `l1_consensus`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-02` · **Source commit**: `f54a8ae` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-21` · **Tool version**: `0.1.0` · **Generated**: `2026-06-04T09:44:11Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> *(no scoped_claim recorded — event not paper-ready)*

## 1. Trigger

- **Type**: `nation_state_block`
- **Actor**: `CN_SICHUAN_GOVT_NDRC_ENERGY_BUREAU`
- **Timestamp**: `2021-06-18 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`supporting_journalism`**
  - URL: <https://www.scmp.com/tech/policy/article/3137988/chinas-cryptocurrency-crackdown-intensifies-sichuan-province-orders>
  - Wayback: <https://web.archive.org/web/20211013145459/https://www.scmp.com/tech/policy/article/3137988/chinas-cryptocurrency-crackdown-intensifies-sichuan-province-orders>
  > South China Morning Post, 2021-06-20, reports the Sichuan
> provincial branch of the National Development and Reform
> Commission (NDRC) and the Sichuan Energy Bureau jointly
> issued the notice on Friday 2021-06-18. The notice required
> 26 companies "inspected and reported as potential
> cryptocurrency mining enterprises" to be closed by Sunday
> 2021-06-20; electricity providers (State Grid Corp of
> China's Sichuan branch) had to report inspection results
> by 2021-06-25. Wayback snapshot 2021-10-13 14:54 UTC. The
> underlying Sichuan provincial NDRC / Energy Bureau Chinese-
> language primary_legal notice is not yet pinned and remains
> a follow-up item; the SCMP archived body is the load-bearing
> contextual evidence for trigger date anchoring in this draft.
- **`supporting_journalism`**
  - URL: <https://www.theblock.co/post/108916/sichuan-orders-state-power-grid-to-cut-supply-for-26-bitcoin-mining-farms>
  - Wayback: <https://web.archive.org/web/20220819210027/https://www.theblock.co/post/108916/sichuan-orders-state-power-grid-to-cut-supply-for-26-bitcoin-mining-farms>
  > The Block, 2021-06-19, corroborates that the Sichuan Energy
> Bureau and the Sichuan Development and Reformation
> Commission jointly issued the notice on 2021-06-18,
> ordering state-owned power generators and distributors
> (incl. State Grid) to cut hydroelectricity supply to 26
> bitcoin mining facilities by 2021-06-20. Wayback snapshot
> 2022-08-19 (live URL bot-blocks fetch in 2026).

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Chains**: `bitcoin`

> The 26 named "potential cryptocurrency mining enterprises"
> identified by the Sichuan provincial NDRC inspection as the
> initial subjects of the State Grid power cut, plus follow-on
> inspection sweeps of privately powered facilities, are the
> enumerated subset. The full list of 26 entities is not pinned
> in this draft (the underlying provincial notice in Chinese
> has not yet been archived). enumeration=subset reflects that
> we are recording a defensible slice of the targeted Sichuan-
> hosted bitcoin mining population rather than asserting a
> complete enumeration of all Sichuan mining capacity at event
> time.

## 3. Changed-layer observations (supports the scoped claim)

### l1_consensus · attribution: `plausible` · Δt = Noneh

**Event label**: `global_hashrate_collapse_following_sichuan_power_cut`

**Timestamp**: `?` (precision: `day`)

**Sources**:

- **`supporting_journalism`**
  - URL: <https://www.theblock.co/post/109030/chinese-bitcoin-mining-pools-hash-rate-plunge-sichuan-shutdown>
  - Wayback: <https://web.archive.org/web/20220825183717/https://www.theblock.co/post/109030/chinese-bitcoin-mining-pools-hash-rate-plunge-sichuan-shutdown>
  > The Block, 2021-06-22, reports Chinese bitcoin mining
> pools (notably Sichuan-hosted pools and pool-level
> aggregates) saw further hash-rate plunge in the days
> immediately following the 2021-06-18 Sichuan
> shutdown order, with the global Bitcoin hashrate
> continuing its multi-week drawdown from the
> mid-May peak. Wayback snapshot 2022-08-25.
- **`semi_primary_measurement`**
  - URL: <https://www.jbs.cam.ac.uk/2021/new-data-reveals-timeline-of-chinas-bitcoin-mining-exodus/>
  - Wayback: <https://web.archive.org/web/20230930161939/https://www.jbs.cam.ac.uk/2021/new-data-reveals-timeline-of-chinas-bitcoin-mining-exodus/>
  - body_hash: `sha256:732d8c9dc3374bcc7264662884c0decb99f59f8ba9f350cd818e4b405fc1ea30`
  - body_path: `sources/http_captures/china-sichuan-mining-ban-2021-06/v0_3_primary_repair/www.jbs.cam.ac.uk__2021-new-data-reveals-timeline-of-chinas-bitcoin-mining-exodus__17671bfc39.html`
  > Cambridge Judge Business School / Cambridge Centre
> for Alternative Finance commentary (2021-07-15)
> confirms that the June 2021 government crackdown
> "has effectively led to all of China's hashrate
> disappearing overnight"; the CBECI Mining Map was
> discontinued from June 2021 onward because
> Chinese-pool geolocation data became unreliable
> after the exodus. Wayback snapshot 2023-09-30. The
> Current article body_hash was pinned in v0.3 source repair.
> CBECI time-series body_hash / measurement_id pinning remains
> deferred to a human-audit pass.
- **`semi_primary_wayback`**
  - URL: <https://www.cnbc.com/2021/06/21/bitcoin-btc-price-drops-on-china-crypto-mining-crackdown.html>
  - Wayback: <https://web.archive.org/web/20210625233627/https://www.cnbc.com/2021/06/21/bitcoin-btc-price-drops-on-china-crypto-mining-crackdown.html>
  - body_hash: `sha256:d1bd2329dbc7d08f742f5ca9c54f8c502de83f3c4e85b3e93a53a4a28f140f04`
  - body_path: `sources/http_captures/china-sichuan-mining-ban-2021-06/primary/web.archive.org__web-20210625233627-https-www.cnbc.com-2021-06-21-bitcoin-btc-price-drops-on-china-crypto-mining-crackdown.html__158915acb4.html`
  > CNBC, 2021-06-21, contemporaneous coverage of the
> Bitcoin price drop following the Sichuan mining
> crackdown, noting that more than half the world's
> bitcoin miners faced shutdown. Wayback snapshot
> 2021-06-25, four days post-publication.

## 5. Honest coverage gaps

- **offramp_cex** (`not_measured`): Mainland-Chinese exchanges (Huobi, OKEx, Binance China-

## 7. Related events

- [`china-pboc-crypto-ban-2021`](./china-pboc-crypto-ban-2021.md)
- [`china-state-council-mining-crackdown-2021-05`](./china-state-council-mining-crackdown-2021-05.md)
- [`china-inner-mongolia-mining-ban-2021-05`](./china-inner-mongolia-mining-ban-2021-05.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `f54a8ae`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

