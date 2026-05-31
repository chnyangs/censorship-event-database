# Evidence chain — `blockfi-multistate-cease-desist-bia-2021-07`

**Status**: `admitted` · **Stratum**: `S4_nation_state` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `80b0ca3` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-31` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "The New Jersey Bureau of Securities Summary Cease and Desist Order of
> 2021-07-19 (effective 2021-07-22) directly ordered BlockFi to cease offering
> its BlockFi Interest Account (BIA) — ruled an unregistered security — for sale
> to or from New Jersey, producing a regulator-mandated severance of the BIA
> crypto yield/off-ramp at the NJ-customer perimeter (offramp_cex load-bearing,
> attribution=direct). The row does not claim ISP-level blocking, on-chain asset
> freeze, or the full enumeration of the parallel multi-state (TX/AL/KY/VT)
> actions."

## 1. Trigger

- **Type**: `regulatory_enforcement`
- **Actor**: `US_NJ_BUREAU_OF_SECURITIES`
- **Timestamp**: `2021-07-19 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://www.nj.gov/oag/newsreleases21/BlockFi-Cease-and-Desist-Order.pdf>
  - Wayback: <https://web.archive.org/web/20210731004209id_/https://www.nj.gov/oag/newsreleases21/BlockFi-Cease-and-Desist-Order.pdf>
  - body_hash: `sha256:b235ce2adf08dcfd40e5f38fc9c262407c0dc60cfbddd1d887baa75f67209771`
  - body_path: `sources/http_captures/blockfi-multistate-cease-desist-bia-2021-07/primary/web.archive.org__web-20210801000000id_-https-www.nj.gov-oag-newsreleases21-BlockFi-Cease-and-Desist-Order.pdf__5e0feb98af.bin`
  > State of New Jersey Bureau of Securities Summary Cease and Desist Order
> (Bureau Chief Christopher W. Gerold, Uniform Securities Law N.J.S.A.
> 49:3-47 et seq.) "In the Matter of: BlockFi Inc., BlockFi Lending, LLC,
> and BlockFi Trading, LLC." Captured PDF (15 pages) text reads: "THEREFORE,
> it is on this 19th day of July 2021, ORDERED that: 39. Effective on July
> 22, 2021, BlockFi, Trading and BFI ... shall CEASE AND DESIST from: a)
> offering for sale any security, including any BIA [BlockFi Interest
> Account], to or from New Jersey unless the security is registered ... or
> is exempt from registration under the Securities Law." Findings: since
> 2019-03-04 BlockFi funded its lending/proprietary-trading through the
> sale of unregistered securities (the interest-earning accounts).
> Wayback memento 20210731004209 captured 2026-05-31.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: BlockFi (BlockFi Interest Account / BIA)
- **Canonical domains**: `blockfi.com`

> BlockFi Inc. and its affiliates BlockFi Lending, LLC and BlockFi Trading,
> LLC — specifically the BlockFi Interest Account (BIA) product offered to New
> Jersey residents. Named as the immediate addressee of the NJ order. The
> candidate's multi-state framing (additional cease/show-cause actions by
> Texas, Alabama, Kentucky, Vermont regulators in the same July 2021 window)
> is carried as context only; the load-bearing captured instrument is the NJ
> order, so the enumeration is coded subset and the multi-state cohort is not
> enumerated order-by-order in this draft.

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `direct` · Δt = 72h

**Event label**: `blockfi_interest_account_offering_ordered_to_cease_new_jersey`

**Timestamp**: `2021-07-22 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_legal`**
  - URL: <https://www.nj.gov/oag/newsreleases21/BlockFi-Cease-and-Desist-Order.pdf>
  - Wayback: <https://web.archive.org/web/20210731004209id_/https://www.nj.gov/oag/newsreleases21/BlockFi-Cease-and-Desist-Order.pdf>
  - body_hash: `sha256:b235ce2adf08dcfd40e5f38fc9c262407c0dc60cfbddd1d887baa75f67209771`
  - body_path: `sources/http_captures/blockfi-multistate-cease-desist-bia-2021-07/primary/web.archive.org__web-20210801000000id_-https-www.nj.gov-oag-newsreleases21-BlockFi-Cease-and-Desist-Order.pdf__5e0feb98af.bin`
  > NJ Bureau of Securities Summary Cease and Desist Order is the legal
> instrument naming BlockFi as addressee and ordering it to cease
> offering the BIA for sale to/from New Jersey effective 2021-07-22.
> attribution=direct per codebook §1.1 — the named actor (NJ Bureau of
> Securities) issues the order and the order names the target (BlockFi /
> BIA) being acted upon. delta_hours=72 from the order-entry timestamp
> (2021-07-19) to the effective severance (2021-07-22).
- **`primary_government`**
  - URL: <https://www.njoag.gov/new-jersey-bureau-of-securities-orders-cryptocurrency-company-blockfi-to-stop-offering-interest-bearing-accounts/>
  - Wayback: <https://web.archive.org/web/20210721210617/https://www.njoag.gov/new-jersey-bureau-of-securities-orders-cryptocurrency-company-blockfi-to-stop-offering-interest-bearing-accounts/>
  - body_hash: `sha256:a4248a370d087feaf5bbdaa79493dc041013d07033f7df178624a5ea9a5f3a22`
  - body_path: `sources/http_captures/blockfi-multistate-cease-desist-bia-2021-07/primary/web.archive.org__web-20210722000000-https-www.njoag.gov-new-jersey-bureau-of-securities-orders-cryptocurrency-company-blockfi-to-stop-offering-interest-bearing-accounts__6397a0cfdd.html`
  > NJ Office of Attorney General press release corroborating the Summary
> Cease and Desist Order against BlockFi for selling unregistered
> securities (interest-earning crypto accounts; $14.7 billion raised
> worldwide). Captured HTML grep-confirms "Summary Cease and Desist",
> "BlockFi", "unregistered securities", "14.7". Wayback memento
> 20210721210617 captured 2026-05-31.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`blockfi-sec-lending-2022`](./blockfi-sec-lending-2022.md)
- [`bitfinex-tether-nyag-2021`](./bitfinex-tether-nyag-2021.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `80b0ca3`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

