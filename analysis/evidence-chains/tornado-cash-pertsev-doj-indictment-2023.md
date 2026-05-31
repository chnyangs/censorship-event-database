# Evidence chain — `tornado-cash-pertsev-doj-indictment-2023`

**Status**: `admitted` · **Stratum**: `S3_doj_sec_cftc_fiod` · **Shape**: `null_event` (0 changed layer(s): none) · **Tier**: `null_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `8e29b8d` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-21` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "The 2023-08-23 SDNY Tornado Cash indictment named Alexey Pertsev as
> Co-Conspirator-1 without charging him (deferring to the ongoing Dutch
> prosecution from pertsev-nl-arrest-2022); the CC-1 designation produced no
> separately-disclosed cross-layer cascade beyond the same-day OFAC Semenov
> SDN and storm-semenov-doj-2023 indictment captured in companion events."

## 1. Trigger

- **Type**: `doj_indictment`
- **Actor**: `US_DOJ_SDNY`
- **Timestamp**: `2023-08-23 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://www.justice.gov/usao-sdny/pr/tornado-cash-founders-charged-money-laundering-and-sanctions-violations>
  - Wayback: <https://web.archive.org/web/20230823170656/https://www.justice.gov/usao-sdny/pr/tornado-cash-founders-charged-money-laundering-and-sanctions-violations>
  - body_hash: `sha256:d12edb384523f297c646c1abf52dd65657e3f29aaa52c8ef89ee4fb3792d0801`
  - body_path: `sources/http_captures/tornado-cash-pertsev-doj-indictment-2023/primary/web.archive.org__web-20230823170656-https-www.justice.gov-usao-sdny-pr-tornado-cash-founders-charged-money-laundering-and-sanctions-violations__7a19009784.html`
  > DOJ USAO-SDNY press release "Tornado Cash Founders Charged With Money
> Laundering And Sanctions Violations" (2023-08-23). The unsealed SDNY
> indictment names Roman Storm and Roman Semenov as defendants; Alexey
> Pertsev is referenced as "CC-1" (Co-Conspirator-1), the Dutch-resident
> Tornado Cash co-developer already in NL FIOD custody since 2022-08-10.
> Pertsev is NOT charged in this SDNY indictment — DOJ deferred to the
> ongoing Dutch prosecution. This event captures the US-side CC-1
> designation of Pertsev as the third major cross-jurisdictional
> Tornado Cash developer-enforcement node (alongside storm-semenov-doj-2023
> and pertsev-nl-arrest-2022).
- **`supporting_journalism`**
  - URL: <https://www.lawfaremedia.org/article/tornado-hit-by-the-department-of-justice>
  - Wayback: <https://web.archive.org/web/20230830223925/https://www.lawfaremedia.org/article/tornado-hit-by-the-department-of-justice>
  - body_hash: `sha256:67cd0c9c41248796c76591d1a775a0420d5c96e1b482156ff37de1c90288e859`
  - body_path: `sources/http_captures/tornado-cash-pertsev-doj-indictment-2023/primary/web.archive.org__web-20230830223925-https-www.lawfaremedia.org-article-tornado-hit-by-the-department-of-justice__349a790dca.html`
  > Lawfare analysis of the 2023-08-23 SDNY indictment, including discussion
> of Pertsev's status as un-charged co-conspirator in the US filing while
> being separately prosecuted in the Netherlands.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Protocol**: `tornado_cash`
- **Actor name**: Alexey Pertsev (CC-1)

> Alexey Pertsev (Russian national, NL resident) — listed as CC-1 in the SDNY
> indictment but not charged. Subset: this event documents only the Pertsev-
> CC-1 slice of the larger indictment; the charged-defendant slice (Storm,
> Semenov) is captured separately in storm-semenov-doj-2023. No on-chain
> addresses tied to Pertsev specifically in the DOJ filing.

## 3. Changed-layer observations (supports the scoped claim)

*No observed_change entries. This is a `null_event`; see §4 for observed_no_change evidence supporting the null claim.*

## 4. No-change observations (where applicable)

### offramp_cex — `no_public_cex_cascade_for_pertsev_cc1_designation_2023`

**Window**: `2023-08-23 00:00:00+00:00` → `2023-09-06 23:59:59+00:00`

**Sources**:

- **`primary_legal`**
  - URL: <https://www.justice.gov/usao-sdny/pr/tornado-cash-founders-charged-money-laundering-and-sanctions-violations>
  - Wayback: <https://web.archive.org/web/20230823170656/https://www.justice.gov/usao-sdny/pr/tornado-cash-founders-charged-money-laundering-and-sanctions-violations>
  - body_hash: `sha256:d12edb384523f297c646c1abf52dd65657e3f29aaa52c8ef89ee4fb3792d0801`
  - body_path: `sources/http_captures/tornado-cash-pertsev-doj-indictment-2023/primary/web.archive.org__web-20230823170656-https-www.justice.gov-usao-sdny-pr-tornado-cash-founders-charged-money-laundering-and-sanctions-violations__7a19009784.html`
  > No CEX policy statement referencing Pertsev individually downstream of the
> SDNY CC-1 designation. The 2023-08-23 CEX bandwidth was absorbed by the
> same-day OFAC Semenov SDN (Circle 8/8 USDC batch-freeze; see semenov-ofac-2023);
> the Pertsev CC-1 slice produced no separately-disclosed exchange action.
> 14-day observation window matches storm-semenov-doj-2023 convention.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`pertsev-nl-arrest-2022`](./pertsev-nl-arrest-2022.md)
- [`semenov-ofac-2023`](./semenov-ofac-2023.md)
- [`storm-semenov-doj-2023`](./storm-semenov-doj-2023.md)
- [`tornado-cash-storm-conviction-2025`](./tornado-cash-storm-conviction-2025.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `8e29b8d`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

