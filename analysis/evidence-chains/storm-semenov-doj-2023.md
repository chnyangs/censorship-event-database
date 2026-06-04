# Evidence chain — `storm-semenov-doj-2023`

**Status**: `admitted` · **Stratum**: `S3_doj_sec_cftc_fiod` · **Shape**: `null_event` (0 changed layer(s): none) · **Tier**: `null_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-02` · **Source commit**: `47f4858` · **Schema**: `0.2.0` · **Event last_verified**: `2026-04-22` · **Tool version**: `0.1.0` · **Generated**: `2026-06-04T14:27:22Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "DOJ SDNY indictment of Roman Storm and Roman Semenov on 2023-08-23 —
> co-occurring with the same-day OFAC individual designation of Semenov —
> documented US criminal-law enforcement of crypto privacy-tool developers,
> paired with the 2022-08-10 NL FIOD Pertsev arrest as the second major
> cross-jurisdictional Tornado Cash developer-enforcement event."

## 1. Trigger

- **Type**: `doj_indictment`
- **Actor**: `US_DOJ_SDNY`
- **Timestamp**: `2023-08-23 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://www.justice.gov/usao-sdny/pr/tornado-cash-founders-charged-money-laundering-and-sanctions-violations>
  - Wayback: <https://web.archive.org/web/20230823170656/https://www.justice.gov/usao-sdny/pr/tornado-cash-founders-charged-money-laundering-and-sanctions-violations>
  - body_hash: `sha256:21a46072ff95909fa240c324573502f77ce5d60044a6b0f120fdd7a8bf2b8de2`
  - body_path: `sources/http_captures/storm-semenov-doj-2023/wayback_doj_press_snapshot/web.archive.org__web-20230823170656-https-www.justice.gov-usao-sdny-pr-tornado-cash-founders-charged-money-laundering-and-sanctions-violations__7a19009784.html`
  > Wayback memento (2023-08-23 17:06 UTC, ~event-day publishing
> window) of DOJ USAO-SDNY press release "Tornado Cash Founders
> Charged With Money Laundering And Sanctions Violations"
> (2023-08-23). Unsealed indictment against Roman Storm and Roman
> Semenov — co-founders of Tornado Cash — charging: conspiracy
> to commit money laundering; conspiracy to commit sanctions
> violations (IEEPA); conspiracy to operate an unlicensed
> money-transmitting business. Storm arrested in US (WA);
> Semenov at large in Dubai, UAE. **Same-day as the 2023-08-23
> OFAC designation of Semenov** — coordinated OFAC + DOJ action.
> v0.3 audit 2026-05-20 repair: body_path swapped to Wayback
> memento (166567 bytes real content) replacing prior Akamai-stub
> capture (sha256:67150f10..., 2879 bytes, retained on-disk as
> sources/http_captures/storm-semenov-doj-2023/primary/...__6b7b0d611f.html
> but no longer cited). Grep confirms: 73xsdny + 47xTornado/tornado
> + 47xCash/cash + 40xsanctions variants + 31xfounder variants +
> 22xMoney Laundering + 10xconspiracy + 8xSTORM + 8xSEMENOV.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `complete`
- **Protocol**: `tornado_cash`
- **Actor name**: Roman Storm + Roman Semenov

> Two individuals: Roman STORM (US arrest, Washington state) + Roman SEMENOV
> (Dubai, at large). Both named as Tornado Cash co-founders. No on-chain
> addresses in the DOJ press release; the Semenov 8 ETH addresses are on the
> same-day OFAC RA (see semenov-ofac-2023). This event captures the DOJ
> indictment side.

## 3. Changed-layer observations (supports the scoped claim)

*No observed_change entries. This is a `null_event`; see §4 for observed_no_change evidence supporting the null claim.*

## 4. No-change observations (where applicable)

### offramp_cex — `no_public_cex_cascade_for_doj_indictment_2023`

**Window**: `2023-08-23 00:00:00+00:00` → `2023-09-06 23:59:59+00:00`

**Sources**:

- **`primary_legal`**
  - URL: <https://www.justice.gov/usao-sdny/pr/tornado-cash-founders-charged-money-laundering-and-sanctions-violations>
  - Wayback: <https://web.archive.org/web/20230823170656/https://www.justice.gov/usao-sdny/pr/tornado-cash-founders-charged-money-laundering-and-sanctions-violations>
  - body_hash: `sha256:21a46072ff95909fa240c324573502f77ce5d60044a6b0f120fdd7a8bf2b8de2`
  - body_path: `sources/http_captures/storm-semenov-doj-2023/wayback_doj_press_snapshot/web.archive.org__web-20230823170656-https-www.justice.gov-usao-sdny-pr-tornado-cash-founders-charged-money-laundering-and-sanctions-violations__7a19009784.html`
  > No fresh CEX policy statement referencing the DOJ indictment (distinct from
> the same-day OFAC Semenov SDN, which triggered the Circle 8/8 USDC
> batch-freeze within 24h — see semenov-ofac-2023). CEX cascade bandwidth
> on 2023-08-23 was absorbed by the OFAC side; the DOJ side alone produced
> no separately-disclosed exchange action. v0.3 audit 2026-05-20 repair:
> body_path swapped to Wayback memento (166567 bytes real content) which
> substantiates the DOJ indictment trigger event itself (grep-verified
> 73xsdny + 47xTornado + 40xsanctions + 31xfounder + 22xMoney Laundering +
> 10xconspiracy + 8xSTORM + 8xSEMENOV); the observed_no_change null
> finding remains the same.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`tornado-cash-ofac-2022`](./tornado-cash-ofac-2022.md)
- [`tornado-cash-ofac-redesignation-2022`](./tornado-cash-ofac-redesignation-2022.md)
- [`semenov-ofac-2023`](./semenov-ofac-2023.md)
- [`pertsev-nl-arrest-2022`](./pertsev-nl-arrest-2022.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `47f4858`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

