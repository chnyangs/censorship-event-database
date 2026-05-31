# Evidence chain — `venezuela-sunacrip-mining-exchange-halt-2023-03`

**Status**: `admitted` · **Stratum**: `S4_nation_state` · **Shape**: `comparison` (1 changed layer(s): `l1_consensus`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-05-31` · **Source commit**: `939a17f` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-31` · **Tool version**: `0.1.0` · **Generated**: `2026-05-31T14:50:46Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "During the March 2023 SUNACRIP corruption reorganization, Venezuela's
> crypto regulator ordered the physical shutdown of licensed crypto mining
> facilities in Carabobo, Lara and Bolívar (l1_consensus observed_change,
> plausible attribution). A separately-reported order to close all
> registered exchanges was officially unconfirmed/denied and is not carried
> as an observed_change."

## 1. Trigger

- **Type**: `nation_state_block`
- **Actor**: `VE_SUNACRIP`
- **Timestamp**: `2023-03-17 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`supporting_journalism`**
  - URL: <https://decrypt.co/124525/shut-down-mining-farms-exchanges-venezuela>
  - Wayback: <https://web.archive.org/web/20230324212438/https://decrypt.co/124525/shut-down-mining-farms-exchanges-venezuela>
  - body_hash: `sha256:6212c4c67fb167ce0222dd865cd2d37eb62d0cebcd575f5ca219186ff1de3c18`
  - body_path: `sources/http_captures/venezuela-sunacrip-mining-exchange-halt-2023-03/primary/web.archive.org__web-20230324212438-https-decrypt.co-124525-shut-down-mining-farms-exchanges-venezuela__ed95e252dd.html`
  > Decrypt, captured 2023-03-24, reports that amid the SUNACRIP
> corruption scandal (SUNACRIP reorganized/closed March 2023; ≥10
> people arrested incl. former superintendent Joselit Ramirez
> Camacho) the new superintendent ordered the closure of large
> cryptocurrency mining farms — the captured body confirms
> shutdowns of mining farms in the states of Carabobo, Lara and
> Bolívar, affecting licensed, tax-paying operations (per
> Asonacrip, the National Association of Cryptocurrencies). The
> captured body ALSO reports a separate order to close "all
> cryptocurrency exchanges registered in Venezuela," but states
> this has "not been officially confirmed"; the exchange-closure
> claim is therefore contested and is NOT carried as an
> observed_change (see analysis_notes). Wayback snapshot
> 2023-03-24 21:24 UTC. body_hash pinned in this census wave.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: Venezuelan licensed crypto mining operations (Carabobo / Lara / Bolívar, class)

> Venezuelan licensed cryptocurrency mining operations as a class,
> with confirmed facility shutdowns in the states of Carabobo, Lara
> and Bolívar per the captured source. enumeration=subset because the
> affected facilities are recorded at the state/class level rather
> than as a complete enumeration of every shut-down operation. The
> separately-reported (and officially-unconfirmed) order against
> registered exchanges is excluded from the enumerated target.

## 3. Changed-layer observations (supports the scoped claim)

### l1_consensus · attribution: `plausible` · Δt = 0h

**Event label**: `state_ordered_mining_facility_shutdown_carabobo_lara_bolivar`

**Timestamp**: `2023-03-17 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`supporting_journalism`**
  - URL: <https://decrypt.co/124525/shut-down-mining-farms-exchanges-venezuela>
  - Wayback: <https://web.archive.org/web/20230324212438/https://decrypt.co/124525/shut-down-mining-farms-exchanges-venezuela>
  - body_hash: `sha256:6212c4c67fb167ce0222dd865cd2d37eb62d0cebcd575f5ca219186ff1de3c18`
  - body_path: `sources/http_captures/venezuela-sunacrip-mining-exchange-halt-2023-03/primary/web.archive.org__web-20230324212438-https-decrypt.co-124525-shut-down-mining-farms-exchanges-venezuela__ed95e252dd.html`
  > Decrypt archived body confirms SUNACRIP-ordered closures of
> large mining farms in Carabobo, Lara and Bolívar, affecting
> licensed, tax-paying operations (per Asonacrip). attribution=
> plausible (not direct): the closures are reported by Asonacrip
> and contemporaneous journalism rather than by a pinned
> SUNACRIP primary order, and SUNACRIP made contradictory public
> statements during the reorganization (it did not publicly
> confirm a cessation order). Conservative per codebook §8.4.

## 5. Honest coverage gaps

- **offramp_cex** (`not_measured`): Decrypt reports a separate order to close "all cryptocurrency

## 7. Related events

- [`china-sichuan-mining-ban-2021-06`](./china-sichuan-mining-ban-2021-06.md)
- [`nigeria-cbn-crypto-ban-2021`](./nigeria-cbn-crypto-ban-2021.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `939a17f`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

