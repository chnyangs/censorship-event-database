# Evidence chain — `welcome-to-video-doj-2019`

**Status**: `admitted` · **Stratum**: `S3_doj_sec_cftc_fiod` · **Shape**: `comparison` (1 changed layer(s): `l4_frontend`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `432aaf5` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-16` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "The 2019-10-16 DOJ unsealing of the indictment of Jong Woo Son for
> operating the Welcome to Video Tor marketplace produced an L4
> frontend seizure of the marketplace's Tor hidden-service
> infrastructure, in a joint operation with IRS-Criminal
> Investigation, UK NCA, and Korean NPA. The row claims only this
> single-layer marketplace-takedown observation; the asset_onchain
> BTC-seizure receipts that structurally anchor the case's
> address-traceability framing are held at not_measured pending
> human audit of forfeiture filings."

## 1. Trigger

- **Type**: `doj_seizure_order`
- **Actor**: `US_DOJ`
- **Timestamp**: `2019-10-16 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://www.justice.gov/opa/pr/south-korean-national-and-hundreds-others-charged-worldwide-takedown-largest-darknet-child>
  - Wayback: <https://web.archive.org/web/20260516000000/https://www.justice.gov/opa/pr/south-korean-national-and-hundreds-others-charged-worldwide-takedown-largest-darknet-child>
  > DOJ Office of Public Affairs press release announcing the
> 2019-10-16 unsealing of the indictment of Jong Woo Son, a South
> Korean national, for operating "Welcome to Video", described in
> the release as the world's largest darknet child sexual abuse
> material marketplace at the time of takedown. The release
> describes a joint operation between US DOJ + IRS-Criminal
> Investigation + UK National Crime Agency + Korean National
> Police Agency, with 337 arrests across 38 jurisdictions and
> approximately $370K in Bitcoin seized. The wayback URL above is
> a DRYRUN stub; the live justice.gov URL is retained as
> evidence_use=contextual_unarchived per the authoring brief,
> which forbade fabricating a body_hash. A real release must
> replace this stub with a human-verified Wayback memento and a
> body_hash + body_path artifact captured from a re-archived
> DOJ snapshot.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: Welcome to Video (operated by Jong Woo Son)
- **Chains**: `bitcoin`

> Jong Woo Son (named operator) and the Welcome to Video darknet
> marketplace (Tor hidden service accepting Bitcoin payments). The
> DOJ release identifies 337 arrests globally across 38 jurisdictions
> and approximately $370K in Bitcoin seized; this event does not
> enumerate the per-defendant arrest list or an SDN-style address
> set. canonical_domains is left empty because no verified .onion
> address is pinned in this DRYRUN row.

## 3. Changed-layer observations (supports the scoped claim)

### l4_frontend · attribution: `direct` · Δt = 0h

**Event label**: `tor_marketplace_seized_in_joint_us_uk_kr_operation`

**Timestamp**: `2019-10-16 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_legal`**
  - URL: <https://www.justice.gov/opa/pr/south-korean-national-and-hundreds-others-charged-worldwide-takedown-largest-darknet-child>
  - Wayback: <https://web.archive.org/web/20260516000000/https://www.justice.gov/opa/pr/south-korean-national-and-hundreds-others-charged-worldwide-takedown-largest-darknet-child>
  > DOJ press release names the Welcome to Video Tor marketplace
> as taken down on 2019-10-16 in coordination with IRS-CI,
> UK NCA, and Korean NPA. attribution=direct because the
> primary-legal DOJ source names the seized service and the
> marketplace operator. The wayback URL is a DRYRUN stub;
> real release must replace with a human-verified Wayback
> memento plus body_hash + body_path artifact. The live
> justice.gov URL is retained as the canonical pointer.

## 5. Honest coverage gaps

- **asset_onchain** (`not_measured`): The DOJ release describes approximately $370K in Bitcoin seized

## 7. Related events

- [`silk-road-doj-seizure-2013`](./silk-road-doj-seizure-2013.md)
- [`alphabay-hansa-doj-2017`](./alphabay-hansa-doj-2017.md)
- [`hydra-doj-2022`](./hydra-doj-2022.md)
- [`bitzlato-doj-2023`](./bitzlato-doj-2023.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `432aaf5`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

