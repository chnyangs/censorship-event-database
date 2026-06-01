# Evidence chain — `sec-consensys-metamask-staking-swaps-2024-06`

**Status**: `admitted` · **Stratum**: `S3_doj_sec_cftc_fiod` · **Shape**: `comparison` (1 changed layer(s): `l4_frontend`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-02` · **Source commit**: `60f1d90` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-31` · **Tool version**: `0.1.0` · **Generated**: `2026-06-02T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "The 2024-06-28 SEC suit (press release 2024-79) charging Consensys with
> operating MetaMask Swaps/Staking as an unregistered broker and as
> underwriter of Lido/Rocket Pool liquid-staking securities is a single-layer
> l4_frontend restriction targeting the dominant Ethereum wallet's in-app
> swap/staking surface, attribution=direct. comparable_main tier."

## 1. Trigger

- **Type**: `sec_action`
- **Actor**: `US_SEC`
- **Timestamp**: `2024-06-28 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://www.sec.gov/newsroom/press-releases/2024-79>
  - Wayback: <https://web.archive.org/web/20240629094936/https://www.sec.gov/newsroom/press-releases/2024-79>
  - body_hash: `sha256:3e14ed53e6026439354070c4725a41112c0c360f09863e629f7045a6dfa24567`
  - body_path: `sources/http_captures/sec-consensys-metamask-staking-swaps-2024-06/primary/web.archive.org__web-20240628000000-https-www.sec.gov-newsroom-press-releases-2024-79__71103c869f.html`
  > SEC press release 2024-79 (2024-06-28): "SEC Charges Consensys
> Software for Unregistered Offers and Sales of Securities Through Its
> MetaMask Staking Service." The SEC filed suit alleging Consensys
> Software, Inc. (developer of the MetaMask self-custody wallet) acted
> as an unregistered broker through MetaMask's Swaps and Staking
> services, and engaged in unregistered offers and sales of securities
> with respect to the Lido and Rocket Pool liquid-staking programs.
> Wayback 20240629094936 pinned. Grep of the captured body confirms
> "MetaMask", "Broker", "Staking", "Lido", "Rocket Pool",
> "Unregistered".

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: Consensys Software Inc. (MetaMask)
- **Canonical domains**: `metamask.io`

> Consensys Software, Inc. (developer of the MetaMask self-custody Ethereum
> wallet) and the MetaMask Swaps and Staking services. Marked subset: the
> named operator + its in-wallet swap/staking surfaces, not an enumerated
> set of users or routed staking programs. No on-chain addresses named in
> the complaint (a securities suit against the operator, not an on-chain
> freeze).

## 3. Changed-layer observations (supports the scoped claim)

### l4_frontend · attribution: `direct` · Δt = 0h

**Event label**: `sec_sues_consensys_metamask_unregistered_broker_swaps_staking`

**Timestamp**: `2024-06-28 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_legal`**
  - URL: <https://www.sec.gov/newsroom/press-releases/2024-79>
  - Wayback: <https://web.archive.org/web/20240629094936/https://www.sec.gov/newsroom/press-releases/2024-79>
  - body_hash: `sha256:3e14ed53e6026439354070c4725a41112c0c360f09863e629f7045a6dfa24567`
  - body_path: `sources/http_captures/sec-consensys-metamask-staking-swaps-2024-06/primary/web.archive.org__web-20240628000000-https-www.sec.gov-newsroom-press-releases-2024-79__71103c869f.html`
  > SEC press release 2024-79 (2024-06-28): suit charging Consensys with
> operating MetaMask Swaps/Staking as an unregistered broker and with
> unregistered offers/sales of Lido and Rocket Pool liquid-staking
> securities. attribution=direct: the SEC names the specific target
> (Consensys / MetaMask) and its swap/staking frontend conduct being
> acted upon.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `60f1d90`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

