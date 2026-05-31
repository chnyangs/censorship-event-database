# Evidence chain — `tornado-cash-storm-conviction-2025`

**Status**: `admitted` · **Stratum**: `S3_doj_sec_cftc_fiod` · **Shape**: `comparison` (1 changed layer(s): `l4_frontend`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-05-31` · **Source commit**: `c9831a8` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-16` · **Tool version**: `0.1.0` · **Generated**: `2026-05-31T12:53:21Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "The 2025-08-06 SDNY jury verdict convicted Roman Storm on Count 1 of
> the 2023 Tornado Cash indictment (conspiracy to operate an unlicensed
> money transmitting business, 18 U.S.C. § 1960) while hanging on the
> money-laundering and IEEPA-sanctions counts. The conviction produced
> observed_no_change on the asset_onchain layer (the 98 Tornado Cash
> mixer contracts continued live, attribution=none) and a plausible
> observed_change on the L4 operator-narrative axis (first US developer-
> criminal-conviction precedent for non-custodial privacy-protocol
> authoring; personal-risk reassessment channel for similar developers).
> Empirical_shape=comparison; structurally separates developer-criminal-
> liability from protocol-substrate-availability."

## 1. Trigger

- **Type**: `doj_indictment`
- **Actor**: `US_DOJ_SDNY`
- **Timestamp**: `2025-08-06 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://www.justice.gov/usao-sdny/pr/roman-storm-convicted-conspiracy-charge-relating-tornado-cash>
  - Wayback: <https://web.archive.org/web/20260516000000/https://www.justice.gov/usao-sdny/pr/roman-storm-convicted-conspiracy-charge-relating-tornado-cash>
  > DOJ USAO-SDNY press release (2025-08-06): "Roman Storm Convicted Of
> Conspiracy Charge Relating To Tornado Cash." SDNY jury returned a
> partial verdict convicting Storm on Count 1 of the 2023 indictment
> — conspiracy to operate an unlicensed money transmitting business
> (18 U.S.C. § 1960). The jury hung on Count 2 (conspiracy to commit
> money laundering, 18 U.S.C. § 1956(h)) and Count 3 (conspiracy to
> violate the International Emergency Economic Powers Act / IEEPA,
> 50 U.S.C. § 1705). This event captures the **conviction milestone**
> downstream of the 2023-08-23 indictment (storm-semenov-doj-2023,
> admitted as null_case). trigger.type=doj_indictment is retained
> because the conviction is a downstream stage of the same DOJ
> criminal-prosecution chain (no separate trigger taxon exists for
> verdicts in the schema enum).

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `complete`
- **Protocol**: `tornado_cash`
- **Actor name**: Roman Storm
- **Chains**: `ethereum`

> One individual: Roman STORM (Tornado Cash co-founder, US arrest 2023).
> The 2025-08-06 SDNY jury verdict applies only to Storm; co-defendant
> Roman SEMENOV remained at large (Dubai) and was not tried at this
> proceeding. The conviction is on Count 1 only (conspiracy to operate
> an unlicensed money transmitting business); jury hung on Counts 2-3
> (money-laundering conspiracy + IEEPA-sanctions-violation conspiracy).

## 3. Changed-layer observations (supports the scoped claim)

### l4_frontend · attribution: `plausible` · Δt = 0h

**Event label**: `operator_narrative_personal_risk_reassessment_post_storm_conviction`

**Timestamp**: `2025-08-06 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_legal`**
  - URL: <https://www.justice.gov/usao-sdny/pr/roman-storm-convicted-conspiracy-charge-relating-tornado-cash>
  - Wayback: <https://web.archive.org/web/20260516000000/https://www.justice.gov/usao-sdny/pr/roman-storm-convicted-conspiracy-charge-relating-tornado-cash>
  > The 2025-08-06 conviction is the first US criminal verdict
> against a developer of a non-custodial privacy protocol on
> the basis of 18 U.S.C. § 1960 (unlicensed money transmitting
> business). attribution=plausible because the chilling-effect
> / personal-risk-reassessment channel on similar protocol
> authors operates at the narrative / ecosystem level rather
> than via a primary operator artifact (no specific
> repository-archival or developer-departure commit is pinned
> in this DRYRUN). For a real release, candidate primary
> artifacts to pin would be: (a) public statements by other
> privacy-tool maintainers (e.g. Railgun, Aztec, Privacy Pools)
> referencing the Storm verdict; (b) commit-history evidence
> of repository archival or maintainer transitions in the
> 90 days post-verdict; (c) EFF / Coin Center amicus filings
> framing the verdict as a developer-liability precedent.

## 5. Honest coverage gaps

- **asset_onchain** (`not_measured`): Load-bearing layer for this event in narrative terms (the Tornado
- **offramp_cex** (`not_measured`): No public CEX policy statement referencing the 2025-08-06 verdict is

## 7. Related events

- [`storm-semenov-doj-2023`](./storm-semenov-doj-2023.md)
- [`tornado-cash-ofac-2022`](./tornado-cash-ofac-2022.md)
- [`tornado-cash-ofac-delisting-2025`](./tornado-cash-ofac-delisting-2025.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `c9831a8`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

