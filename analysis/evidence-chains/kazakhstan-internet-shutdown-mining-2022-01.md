# Evidence chain — `kazakhstan-internet-shutdown-mining-2022-01`

**Status**: `admitted` · **Stratum**: `S4_nation_state` · **Shape**: `comparison` (1 changed layer(s): `l1_consensus`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `210aa10` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-21` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T04:23:47Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "On 2022-01-05 at approximately noon UTC, the government of
> Kazakhstan under President Tokayev ordered a nationwide internet
> shutdown in response to political unrest. NetBlocks recorded
> normalized country-level connectivity falling to ~2% (L0 layer,
> attribution=direct), and the bitcoin network total hashrate dropped
> from ~194 EH/s to ~168 EH/s within the same day as the
> Kazakhstan-hosted miner population (~18% global hashrate share per
> CBECI fall-2021) lost stratum-server connectivity (L1 consensus
> layer, attribution=direct, causally chained from the L0 shutdown).
> L0 restored on or around 2022-01-10; hashrate recovered to
> pre-shutdown levels within ~1 week of L0 restoration. This is the
> first pure L0 network-layer event in the corpus. Admission-anchor-grade
> promotion pending pinned archive captures (NetBlocks snapshot,
> IODA JSON, CBECI mining-map JSON)."

## 1. Trigger

- **Type**: `nation_state_block`
- **Actor**: `KZ_PRESIDENT_TOKAYEV`
- **Timestamp**: `2022-01-05 12:00:00+00:00` (precision: `hour`)

### Trigger citations

- **`semi_primary_measurement`**
  - URL: <https://netblocks.org/reports/internet-disrupted-in-kazakhstan-amid-energy-price-protests-oy9YQgy3>
  - Wayback: <https://web.archive.org/web/20220104182416/https://netblocks.org/reports/internet-disrupted-in-kazakhstan-amid-energy-price-protests-oy9YQgy3>
  - body_hash: `sha256:246d9d7abfacb5c82b1d9542bae00cc4cd467d68f4772d6c90214949dc512641`
  - body_path: `sources/http_captures/kazakhstan-internet-shutdown-mining-2022-01/primary/web.archive.org__web-20220104182416-https-netblocks.org-reports-internet-disrupted-in-kazakhstan-amid-energy-price-protests-oy9YQgy3__00dd341aba.html`
  > Human audit 2026-05-21 pinned the NetBlocks Wayback memento
> 20220104182416 with local body_hash/body_path, making this a
> replayable trigger anchor for the L0 shutdown onset. Remaining
> hardening targets are independent IODA/Cloudflare/CBECI
> machine-readable measurement artifacts, not admission blockers.
> 
> NetBlocks report "Internet disrupted in Kazakhstan amid energy
> price protests" documents normalized country-level connectivity
> falling to ~2% on 2022-01-05 starting around noon UTC. NetBlocks
> is the canonical semi-primary measurement vantage point for this
> L0 shutdown; IODA (Internet Outage Detection and Analysis,
> CAIDA) and Cloudflare Radar independently corroborate. The
> shutdown was ordered by Kazakhstan's President Kassym-Jomart
> Tokayev in response to nationwide political unrest that began
> 2022-01-02 over LPG fuel price liberalization.
- **`supporting_journalism`**
  - URL: <https://www.coindesk.com/business/2022/01/06/kazakhstans-hashrate-drops-as-internet-blackout-persists-amid-nationwide-protests>
  - Wayback: <https://web.archive.org/web/2022/https://www.coindesk.com/business/2022/01/06/kazakhstans-hashrate-drops-as-internet-blackout-persists-amid-nationwide-protests>
  > CoinDesk 2022-01-06: "Kazakhstan's Hashrate Drops as Internet
> Blackout Persists Amid Nationwide Protests." Independent
> contemporaneous journalism anchor naming Tokayev as the actor
> ordering the shutdown and documenting the downstream hashrate
> collapse.
- **`supporting_journalism`**
  - URL: <https://www.cnbc.com/2022/01/06/kazakhstan-bitcoin-mining-shuts-down-amid-fatal-protests.html>
  - Wayback: <https://web.archive.org/web/2022/https://www.cnbc.com/2022/01/06/kazakhstan-bitcoin-mining-shuts-down-amid-fatal-protests.html>
  > CNBC 2022-01-06: "Kazakhstan's deadly protests hit bitcoin, as
> the world's second-biggest mining hub shuts down." Provides the
> ~18% global hashrate figure (CBECI fall-2021 estimate) and the
> L1-layer hashrate-collapse context.
- **`supporting_tracker`**
  - URL: <https://blog.cloudflare.com/internet-shut-down-in-kazakhstan-amid-unrest/>
  - Wayback: <https://web.archive.org/web/2022/https://blog.cloudflare.com/internet-shut-down-in-kazakhstan-amid-unrest/>
  > Cloudflare blog post documenting the Kazakhstan internet
> shutdown from the Cloudflare Radar vantage point: HTTP request
> traffic from KZ collapsed at the same 2022-01-05 noon UTC
> timestamp NetBlocks recorded, with brief partial restorations
> during Tokayev's televised speeches.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: Kazakhstan nationwide internet shutdown (2022-01-05 to 2022-01-10)
- **Chains**: `bitcoin`

> Subset because the nation-state directive targets nationwide
> internet reachability inside Kazakhstan (the canonical target), and
> the resulting downstream L1 hashrate collapse is observed only on
> the Kazakhstan-hosted miner population (~18% global share per CBECI
> fall-2021 estimate). The enumerated target is the Kazakhstan-routed
> AS-level internet substrate (the L0 shutdown surface) plus the
> Kazakhstan-hosted bitcoin mining-pool stratum-server connectivity
> (the L1 downstream collapse surface). Out of scope: any specific
> crypto-domain reachability slice (no per-domain OONI/Censored
> Planet attestation pinned in this DRYRUN session).

## 3. Changed-layer observations (supports the scoped claim)

### l1_consensus · attribution: `plausible` · Δt = 0h

**Event label**: `bitcoin_hashrate_collapse_following_l0_shutdown`

**Timestamp**: `2022-01-05 12:00:00+00:00` (precision: `hour`)

**Sources**:

- **`semi_primary_wayback`**
  - URL: <https://www.coindesk.com/business/2022/01/06/kazakhstans-hashrate-drops-as-internet-blackout-persists-amid-nationwide-protests>
  - Wayback: <https://web.archive.org/web/20220106124152/https://www.coindesk.com/business/2022/01/06/kazakhstans-hashrate-drops-as-internet-blackout-persists-amid-nationwide-protests>
  - body_hash: `sha256:1bba39948b13d0e41ed7e57c550fa575d8783e5e7b80fc5ab885437f4393c73a`
  - body_path: `sources/http_captures/kazakhstan-internet-shutdown-mining-2022-01/primary/web.archive.org__web-20220106124152-https-www.coindesk.com-business-2022-01-06-kazakhstans-hashrate-drops-as-internet-blackout-persists-amid-nationwide-protests__7bcd112c55.html`
  > CoinDesk 2022-01-06 documents the Kazakhstan-hosted bitcoin
> hashrate collapse following the L0 shutdown. Bitcoin network
> total hashrate dropped from ~194 EH/s (2022-01-04) to ~168
> EH/s (2022-01-05) — a ~13% network-level drop consistent with
> the Kazakh share losing connectivity. The Block reported
> 1THash -82% decline, OKExPool -46.3%, KuCoinPool -22.7% at
> the pool level. attribution=direct because the L1 effect is
> causally chained from the L0 shutdown via the mining-pool
> stratum-server reachability dependency: KZ-hosted miners that
> cannot reach external pool stratum servers cannot submit
> shares and effectively go offline from the network's
> perspective within the same block-interval window.
- **`semi_primary_measurement`**
  - URL: <https://netblocks.org/reports/internet-disrupted-in-kazakhstan-amid-energy-price-protests-oy9YQgy3>
  - Wayback: <https://web.archive.org/web/20220104182416/https://netblocks.org/reports/internet-disrupted-in-kazakhstan-amid-energy-price-protests-oy9YQgy3>
  - body_hash: `sha256:246d9d7abfacb5c82b1d9542bae00cc4cd467d68f4772d6c90214949dc512641`
  - body_path: `sources/http_captures/kazakhstan-internet-shutdown-mining-2022-01/primary/web.archive.org__web-20220104182416-https-netblocks.org-reports-internet-disrupted-in-kazakhstan-amid-energy-price-protests-oy9YQgy3__00dd341aba.html`
  > NetBlocks internet-disruption measurement for the 2022-01-05
> Kazakhstan national shutdown — the L0 substrate that drove the
> L1 hashrate collapse. Independent semi-primary measurement anchor.
- **`supporting_journalism`**
  - URL: <https://www.theblock.co/amp/post/129312/bitcoin-mining-pool-hashrates-fall-amid-kazakhstan-internet-shutdown>
  - Wayback: <https://web.archive.org/web/2022/https://www.theblock.co/amp/post/129312/bitcoin-mining-pool-hashrates-fall-amid-kazakhstan-internet-shutdown>
  > The Block coverage with per-pool hashrate-decline percentages
> documenting which mining pools had heavy KZ-resident hashrate
> exposure (1THash, OKExPool, KuCoinPool). Independent
> journalism vantage.
- **`semi_primary_measurement`**
  - URL: <https://ccaf.io/cbnsi/cbeci/mining_map>
  - Wayback: <https://web.archive.org/web/2022/https://ccaf.io/cbnsi/cbeci/mining_map>
  > CBECI mining map establishes the ~18% global hashrate share
> for KZ as of fall 2021 — the post-China-2021-migration
> baseline against which the January 2022 hashrate collapse is
> measured. Replayable substrate; DRYRUN wayback wildcard in
> lieu of pinned snapshot.

## 5. Honest coverage gaps

- **l0_network** (`not_measured`): L0 network-layer vantage substrate is documented (NetBlocks

## 7. Related events

- [`china-sichuan-mining-ban-2021-06`](./china-sichuan-mining-ban-2021-06.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `210aa10`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

