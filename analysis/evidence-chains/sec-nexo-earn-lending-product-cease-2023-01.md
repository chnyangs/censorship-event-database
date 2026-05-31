# Evidence chain — `sec-nexo-earn-lending-product-cease-2023-01`

**Status**: `admitted` · **Stratum**: `S3_doj_sec_cftc_fiod` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `cd67682` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-31` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "The SEC settlement of 2023-01-19 ($22.5M SEC penalty; $45M total with
> parallel state penalties) directly ordered Nexo Capital Inc. to cease its
> unregistered offer and sale of the Earn Interest Product (ruled an
> unregistered security) to U.S. investors and led Nexo to permanently cease
> offering the EIP to all U.S. investors and phase out all of its products and
> services in the United States — a regulator-forced U.S. retail-market exit at
> the off-ramp/yield-product perimeter (offramp_cex load-bearing,
> attribution=direct). The row does not claim ISP-level blocking, on-chain asset
> freeze, frontend DOM block, or the full enumeration of the parallel
> multistate (NASAA) state orders."

## 1. Trigger

- **Type**: `sec_action`
- **Actor**: `US_SEC`
- **Timestamp**: `2023-01-19 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_government`**
  - URL: <https://www.sec.gov/newsroom/press-releases/2023-11>
  - Wayback: <https://web.archive.org/web/20240704131027/https://www.sec.gov/newsroom/press-releases/2023-11>
  - body_hash: `sha256:ef328758b02afdc231dc972516c5a3644eee0d63ad7b89c2127a125e9d851614`
  - body_path: `sources/http_captures/sec-nexo-earn-lending-product-cease-2023-01/primary/web.archive.org__web-20230120000000-https-www.sec.gov-newsroom-press-releases-2023-11__77d9b92c8e.html`
  > SEC press release 2023-11 (dated "Jan. 19, 2023"): "Nexo Agrees to
> Pay $45 Million in Penalties and Cease Unregistered Offering of Crypto
> Asset Lending Product." The SEC charged Nexo Capital Inc. with failing
> to register the offer and sale of its retail crypto asset lending
> product, the Earn Interest Product (EIP). Captured page text reads
> that Nexo agreed "to pay a $22.5 million penalty and cease its
> unregistered offer and sale of the EIP to U.S. investors" (a parallel
> $22.5 million in state penalties brings the total to $45 million), and
> that Nexo "announced ... permanently ceasing to offer the EIP to all
> U.S. investors" and "phasing out all of its products and services in
> the United States." Grep-confirmed in captured body: "Nexo", "Earn
> Interest Product", "45 Million", "U.S. investors", "cease its
> unregistered offer and sale of the EIP", "Jan. 19, 2023". Wayback
> memento 20240704131027 captured 2026-05-31 (earliest available memento
> of the SEC press-release URL; SEC newsroom paths were reorganized after
> 2023, so no 2023-dated memento of this canonical path exists).

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: Nexo Capital Inc. (Nexo Earn Interest Product / EIP)
- **Canonical domains**: `nexo.com`

> Nexo Capital Inc. — specifically the Nexo Earn Interest Product (EIP), the
> retail crypto-asset lending/yield product offered to U.S. investors from
> around June 2020. The SEC order names Nexo Capital Inc. as the respondent
> and the EIP as the unregistered security being ceased. The parallel
> multistate component (a NASAA-coordinated $22.5 million settlement across
> state securities regulators) is carried as context; the load-bearing
> captured instrument is the SEC press release, so the enumeration is coded
> subset and the per-state cohort is not enumerated order-by-order in this
> draft.

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `direct` · Δt = 0h

**Event label**: `nexo_earn_interest_product_ordered_to_cease_us_investors`

**Timestamp**: `2023-01-19 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_government`**
  - URL: <https://www.sec.gov/newsroom/press-releases/2023-11>
  - Wayback: <https://web.archive.org/web/20240704131027/https://www.sec.gov/newsroom/press-releases/2023-11>
  - body_hash: `sha256:ef328758b02afdc231dc972516c5a3644eee0d63ad7b89c2127a125e9d851614`
  - body_path: `sources/http_captures/sec-nexo-earn-lending-product-cease-2023-01/primary/web.archive.org__web-20230120000000-https-www.sec.gov-newsroom-press-releases-2023-11__77d9b92c8e.html`
  > SEC press release 2023-11 ("Jan. 19, 2023") is the legal instrument
> naming Nexo Capital Inc. as respondent and ordering it to cease its
> unregistered offer and sale of the Earn Interest Product to U.S.
> investors, against a $22.5 million SEC penalty (plus $22.5 million in
> parallel state penalties = $45 million total). The captured body also
> records Nexo "permanently ceasing to offer the EIP to all U.S.
> investors" and "phasing out all of its products and services in the
> United States." attribution=direct per codebook §1.1 — the named
> actor (SEC) issues the order and the order names the target (Nexo /
> EIP) being acted upon. delta_hours=0 (settlement announced and
> effective at the order date).

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`blockfi-sec-lending-2022`](./blockfi-sec-lending-2022.md)
- [`blockfi-multistate-cease-desist-bia-2021-07`](./blockfi-multistate-cease-desist-bia-2021-07.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `cd67682`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

