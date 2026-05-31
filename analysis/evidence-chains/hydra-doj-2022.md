# Evidence chain — `hydra-doj-2022`

**Status**: `admitted` · **Stratum**: `S3_doj_sec_cftc_fiod` · **Shape**: `comparison` (1 changed layer(s): `l4_frontend`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `75fb128` · **Schema**: `0.2.0` · **Event last_verified**: `2026-04-22` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "DOJ/BKA takedown of Hydra Market on 2022-04-05 (same day as OFAC SDN designation) was
> a direct infrastructure seizure of the Tor-hosted darknet marketplace. Illustrates
> multi-agency same-day coordination pattern (cf. Samourai 2024, Cryptex 2024)."

## 1. Trigger

- **Type**: `doj_seizure_order`
- **Actor**: `US_DOJ`
- **Timestamp**: `2022-04-05 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://www.justice.gov/archives/opa/pr/justice-department-investigation-leads-takedown-darknet-cryptocurrency-exchange>
  - body_hash: `sha256:04412881444d534db3586f344013b86fa9482a492a22a930a1511c451c2e3819`
  - body_path: `sources/http_captures/hydra-doj-2022/doj-press-release/www.justice.gov__archives-opa-pr-justice-department-investigation-leads-takedown-darknet-cryptocurrency-exchange__b53b192404.html`
  > DOJ press release for the 2022-04-05 Hydra Market takedown — companion action to
> the same-day OFAC SDN designation (see hydra-ofac-2022). Coordinated between DOJ,
> FBI, IRS-CI, and German Bundeskriminalamt (BKA). Infrastructure seized:
> servers, Bitcoin wallets (~$25M). Charges unsealed against Dmitry Pavlov (alleged
> administrator).
- **`primary_legal`**
  - URL: <https://home.treasury.gov/news/press-releases/jy0701>
  > Related Treasury press release on same-day OFAC designation (cross-referenced).

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Protocol**: `hydra_market`
- **Actor name**: Hydra Market
- **Chains**: `bitcoin`

> Hydra Market was the world's largest darknet marketplace at time of takedown, with
> Russian-language user base. Associated addresses are enumerated in the companion
> hydra-ofac-2022 event (17 XBT SDN addresses). This event focuses on the DOJ/BKA
> criminal-seizure action rather than SDN designation.

## 3. Changed-layer observations (supports the scoped claim)

### l4_frontend · attribution: `direct` · Δt = 0h

**Event label**: `tor_infrastructure_seized_by_bka`

**Timestamp**: `2022-04-05 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_legal`**
  - URL: <https://www.justice.gov/archives/opa/pr/justice-department-investigation-leads-takedown-darknet-cryptocurrency-exchange>
  - body_hash: `sha256:04412881444d534db3586f344013b86fa9482a492a22a930a1511c451c2e3819`
  - body_path: `sources/http_captures/hydra-doj-2022/doj-press-release/www.justice.gov__archives-opa-pr-justice-department-investigation-leads-takedown-darknet-cryptocurrency-exchange__b53b192404.html`
  > DOJ press release confirming seizure of Hydra's servers by German BKA in
> coordination with DOJ/FBI/IRS-CI. attribution=direct because the press release
> names the seizure operation and dates.

## 5. Honest coverage gaps

- **offramp_cex** (`not_measured`): Chain-analytics anchors pinned 2026-04-22 as primary_corporate

## 7. Related events

- [`hydra-ofac-2022`](./hydra-ofac-2022.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `75fb128`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

