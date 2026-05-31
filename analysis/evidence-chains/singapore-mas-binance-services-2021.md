# Evidence chain — `singapore-mas-binance-services-2021`

**Status**: `admitted` · **Stratum**: `S4_nation_state` · **Shape**: `comparison` (2 changed layer(s): `l4_frontend`, `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `8583894` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-16` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "MAS Investor Alert List placement of Binance.com on 2021-09-02
> plus the accompanying Payment Services Act warning precipitated
> a fast L4-frontend response (Binance announced SG-user product
> restrictions 2021-09-05, three days later) and a slow-cascade
> offramp severance routing through the local Binance entity
> (Binance Asia Services withdrew its PSA licence application
> 2021-12; binance.sg ceased SG operations 2022-02). Load-bearing
> observational axes are L4 frontend (Binance SG-user product
> restrictions) and offramp_cex (SGD rails) at the Binance-SG
> cohort level."

## 1. Trigger

- **Type**: `nation_state_block`
- **Actor**: `SG_MAS`
- **Timestamp**: `2021-09-02 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://www.mas.gov.sg/news/>
  - Wayback: <https://web.archive.org/web/20210902000000*/mas.gov.sg>
  > Monetary Authority of Singapore (MAS) press release dated
> 2021-09-02 placing Binance.com on the MAS Investor Alert List
> (IAL) and warning that Binance may be in breach of the Payment
> Services Act (PSA) by providing payment services to Singapore
> residents without the required licence. The IAL listing is
> Singapore's standard investor-protection mechanism flagging
> unregulated entities soliciting Singapore residents. DRYRUN
> promotion: real anchor (MAS press release index) asserted;
> Wayback / body-hash capture deferred to non-DRYRUN release.
> Marked contextual_unarchived to flag the unarchived state
> explicitly.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: Binance.com (SG cohort)
- **Canonical domains**: `binance.com`

> Binance.com global platform serving Singapore retail customers.
> The MAS IAL listing targets the global Binance.com entity (no
> Singapore-licensed Binance legal entity at the time of listing;
> Binance Asia Services Pte Ltd, the local entity, held an
> in-principle PSA licence application that was later withdrawn
> 2021-12). Target treated as entity-level at the Binance-SG
> cohort.

## 3. Changed-layer observations (supports the scoped claim)

### l4_frontend · attribution: `direct` · Δt = 72h

**Event label**: `sg_user_product_restrictions_announced`

**Timestamp**: `2021-09-05 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_legal`**
  - URL: <https://www.mas.gov.sg/news/>
  - Wayback: <https://web.archive.org/web/20210902000000*/mas.gov.sg>
  > MAS 2021-09-02 IAL listing is the regulatory anchor. Binance
> 2021-09-05 announcement to restrict Singapore-resident user
> access to certain product types on binance.com cited the
> MAS notice; attribution=direct at the MAS-listing-as-trigger
> level. DRYRUN: pinned Wayback captures for the Binance
> 2021-09-05 restriction announcement deferred.

### offramp_cex · attribution: `direct` · Δt = 3648h

**Event label**: `sgd_rails_and_binance_sg_operational_exit`

**Timestamp**: `2022-02-01 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_legal`**
  - URL: <https://www.mas.gov.sg/news/>
  - Wayback: <https://web.archive.org/web/20220201000000*/mas.gov.sg>
  > MAS 2021-09-02 IAL listing initiated a cascade culminating
> in Binance Asia Services Pte Ltd withdrawing its PSA licence
> application (2021-12) and binance.sg ceasing SG operations
> (2022-02). SG retail users of binance.com lost SGD rail
> access. DRYRUN: pinned anchors for the 2021-12 licence
> withdrawal and 2022-02 binance.sg exit announcements
> deferred.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`uk-fca-binance-markets-2021`](./uk-fca-binance-markets-2021.md)
- [`netherlands-dnb-binance-warning-2021`](./netherlands-dnb-binance-warning-2021.md)
- [`malaysia-sc-binance-disable-2021`](./malaysia-sc-binance-disable-2021.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `8583894`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

