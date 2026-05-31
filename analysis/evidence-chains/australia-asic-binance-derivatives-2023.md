# Evidence chain — `australia-asic-binance-derivatives-2023`

**Status**: `admitted` · **Stratum**: `S4_nation_state` · **Shape**: `comparison` (2 changed layer(s): `l4_frontend`, `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `7542617` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-16` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "ASIC media release 23-079MR of 2023-04-06 cancelled the AFSL of
> Oztures Trading Pty Ltd (trading as Binance Australia Derivatives)
> after a targeted review found ~500 retail clients had been wrongly
> classified as wholesale clients, directly compelling the shutdown of
> Binance's Australian derivatives operations (effective 2023-04-14
> with transitional close-out through 2023-04-21). Primary
> observational axis is offramp_cex at the Binance-Australia-derivatives
> cohort level; secondary L4-frontend response (AU-geo derivatives-
> shutdown banners on binance.com) attached with plausible attribution.
> The row does not claim ISP-level connectivity blocking, on-chain
> asset freeze, or cancellation of Binance Australia's separate spot-
> exchange AUSTRAC registration."

## 1. Trigger

- **Type**: `nation_state_block`
- **Actor**: `AU_ASIC`
- **Timestamp**: `2023-04-06 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://asic.gov.au/about-asic/news-centre/find-a-media-release/2023-releases/23-079mr-asic-cancels-binance-australia-afs-licence/>
  - Wayback: <https://web.archive.org/web/2023/https://asic.gov.au/about-asic/news-centre/find-a-media-release/2023-releases/23-079mr-asic-cancels-binance-australia-afs-licence/>
  > Australian Securities and Investments Commission (ASIC) media
> release 23-079MR dated 2023-04-06, "ASIC cancels Binance Australia
> AFS licence." ASIC cancelled the Australian Financial Services
> Licence (AFSL) of Oztures Trading Pty Ltd, trading as Binance
> Australia Derivatives, after a targeted review found that Binance
> had wrongly classified approximately 500 retail clients as
> wholesale clients, thereby denying them the consumer protections
> afforded to retail clients under the Corporations Act. The
> cancellation took effect on 2023-04-14, forcing the shutdown of
> Binance Australia Derivatives operations to Australian users.
> Wayback anchor is a 2023 calendar-folder pointer to the ASIC media
> release URL rather than a pinned snapshot; the authoring LLM agent
> did not personally pin a Wayback timestamp or compute a body_hash
> for the ASIC media release page. Marked evidence_use=
> contextual_unarchived to flag the unarchived state explicitly; the
> specific snapshot and body_hash must be re-pinned during human
> audit before this citation may serve as an admission anchor in
> its own right.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: Oztures Trading Pty Ltd (Binance Australia Derivatives)
- **Canonical domains**: `binance.com`

> Oztures Trading Pty Ltd (trading as Binance Australia Derivatives), the
> AFSL-holding Australian entity of the Binance group authorised to offer
> derivative products to Australian clients, and (by cascade) the
> Australian retail derivatives customer cohort of the Binance platform.
> The ASIC cancellation names a single legal entity (Oztures Trading Pty
> Ltd) as the immediate addressee; the operational effect is on
> Australian users of Binance derivatives, including the ~500 misclassified
> retail clients who were the focus of the ASIC targeted review.
> Treated as entity-level at the Binance-Australia-derivatives cohort.

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `direct` · Δt = 0h

**Event label**: `binance_australia_derivatives_afsl_cancelled_operations_shut_down`

**Timestamp**: `2023-04-06 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_legal`**
  - URL: <https://asic.gov.au/about-asic/news-centre/find-a-media-release/2023-releases/23-079mr-asic-cancels-binance-australia-afs-licence/>
  - Wayback: <https://web.archive.org/web/2023/https://asic.gov.au/about-asic/news-centre/find-a-media-release/2023-releases/23-079mr-asic-cancels-binance-australia-afs-licence/>
  > ASIC media release 23-079MR is the legal instrument cancelling
> the Oztures Trading Pty Ltd AFSL. attribution=direct because
> the AFSL cancellation itself compels the operator-state change
> (cessation of Australian-facing derivatives service): without
> an AFSL, the entity may not lawfully offer derivative products
> to Australian clients under the Corporations Act. The
> transitional close-out window (2023-04-14 effective date,
> 2023-04-21 limited close-out deadline) flows directly from the
> ASIC order. DRYRUN: Wayback anchor is a 2023 calendar-folder
> pointer; pinned snapshot timestamp and body_hash capture
> deferred to human audit.

### l4_frontend · attribution: `plausible` · Δt = 24h

**Event label**: `au_geo_specific_derivatives_shutdown_notices_posted`

**Timestamp**: `2023-04-07 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_legal`**
  - URL: <https://asic.gov.au/about-asic/news-centre/find-a-media-release/2023-releases/23-079mr-asic-cancels-binance-australia-afs-licence/>
  - Wayback: <https://web.archive.org/web/2023/https://asic.gov.au/about-asic/news-centre/find-a-media-release/2023-releases/23-079mr-asic-cancels-binance-australia-afs-licence/>
  > ASIC media release is the regulatory anchor for the Binance-AU
> frontend response: Binance posted Australia-specific derivatives-
> shutdown notices and account close-out flows in the days
> following the AFSL cancellation. attribution=plausible because
> the frontend banner / regional notice is a Binance-corporate
> response, not a regulator-mandated DOM change. DRYRUN: pinned
> Wayback snapshot of the binance.com Australia-geo notice page
> is deferred to human audit; the ASIC media release is retained
> here as the contextual anchor for the frontend response.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`uk-fca-binance-markets-2021`](./uk-fca-binance-markets-2021.md)
- [`germany-bafin-binance-licence-withdrawal-2023`](./germany-bafin-binance-licence-withdrawal-2023.md)
- [`belgium-fsma-binance-cease-2023`](./belgium-fsma-binance-cease-2023.md)
- [`netherlands-dnb-binance-warning-2021`](./netherlands-dnb-binance-warning-2021.md)
- [`malaysia-sc-binance-disable-2021`](./malaysia-sc-binance-disable-2021.md)
- [`singapore-mas-binance-services-2021`](./singapore-mas-binance-services-2021.md)
- [`binance-4framework-2023`](./binance-4framework-2023.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `7542617`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

