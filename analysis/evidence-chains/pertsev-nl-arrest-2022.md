# Evidence chain — `pertsev-nl-arrest-2022`

**Status**: `admitted` · **Stratum**: `S3_doj_sec_cftc_fiod` · **Shape**: `null_event` (0 changed layer(s): none) · **Tier**: `null_case`

**Dataset version**: `unknown` · **Schema**: `0.2.0` · **Event last_verified**: `2026-04-22` · **Tool version**: `0.1.0` · **Generated**: `2026-04-22T05:44:02Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "FIOD arrest of Alexey Pertsev on 2022-08-10 in Amsterdam — 2 days after
> the OFAC Tornado Cash designation — was the first cross-border arrest of
> a crypto privacy-tool developer. Non-US jurisdiction (NL) extension of the
> Tornado Cash OFAC cascade; individual-developer-level enforcement
> downstream of protocol-level OFAC action."

## 1. Trigger

- **Type**: `doj_indictment`
- **Actor**: `NL_FIOD`
- **Timestamp**: `2022-08-10 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://www.fiod.nl/arrest-of-suspected-developer-of-tornado-cash/>
  - body_hash: `sha256:213fa9ac504b216e4522420e3a8308b9983d521acdb2d7342d147931c5f279cb`
  - body_path: `sources/http_captures/pertsev-nl-arrest-2022/primary/www.fiod.nl__arrest-of-suspected-developer-of-tornado-cash__85a8894c8d.html`
  > FIOD (Fiscal Information and Investigation Service, Netherlands) press release
> "Arrest of suspected developer of Tornado Cash" (2022-08-10). Alexey Pertsev
> arrested in Amsterdam 2 days after the 2022-08-08 OFAC Tornado Cash
> designation. FIOD — not a US-jurisdiction action — the first cross-border
> enforcement arrest of a crypto privacy-tool developer. Investigation by
> FIOD's multi-disciplinary Financial Advanced Cyber Team (FACT), Amsterdam.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `complete`
- **Protocol**: `tornado_cash`
- **Actor name**: Alexey Pertsev

> Alexey Pertsev (Russian national, resident in Netherlands). Tornado Cash
> developer / contributor. No on-chain addresses in the FIOD press release —
> the arrest is person-level, with investigation ongoing re. specific
> transactions. Dutch prosecution under Money Laundering Act.

## 3. Changed-layer observations (supports the scoped claim)

*No observed_change entries. This is a `null_event`; see §4 for observed_no_change evidence supporting the null claim.*

## 4. No-change observations (where applicable)

### offramp_cex — `no_public_cex_cascade_for_individual_developer_arrest`

**Window**: `2022-08-10 00:00:00+00:00` → `2022-08-24 23:59:59+00:00`

**Sources**:

- **`primary_legal`**
  - URL: <https://www.fiod.nl/arrest-of-suspected-developer-of-tornado-cash/>
  - body_hash: `sha256:213fa9ac504b216e4522420e3a8308b9983d521acdb2d7342d147931c5f279cb`
  - body_path: `sources/http_captures/pertsev-nl-arrest-2022/primary/www.fiod.nl__arrest-of-suspected-developer-of-tornado-cash__85a8894c8d.html`
  > No CEX policy statement referencing Pertsev individually (vs. the 2022-08-08
> protocol-level OFAC cascade) in the 14-day window. Observation records the
> absence of developer-individual-level cascade; the Tornado Cash protocol-
> level cascade from 2022-08-08 absorbed the CEX-response bandwidth.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`tornado-cash-ofac-2022`](./tornado-cash-ofac-2022.md)
- [`storm-semenov-doj-2023`](./storm-semenov-doj-2023.md)
- [`semenov-ofac-2023`](./semenov-ofac-2023.md)

## 8. How to audit this chain

1. Clone the repository at `unknown`.
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

