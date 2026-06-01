# Evidence chain — `australia-asic-binance-derivatives-2023`

**Status**: `admitted` · **Stratum**: `S4_nation_state` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `2079264` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-16` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T05:11:38Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "ASIC media release 23-091MR of 2023-04-06 cancelled the AFSL of
> Oztures Trading Pty Ltd (trading as Binance Australia Derivatives)
> and directly compelled the shutdown of Binance's Australian derivatives
> operations for opening or increasing positions from 2023-04-14
> with transitional close-out through 2023-04-21. Primary
> observational axis is offramp_cex at the Binance-Australia-derivatives
> cohort level. The row does not claim ISP-level connectivity blocking,
> a measured Binance AU-geo frontend banner, on-chain asset freeze, or
> cancellation of Binance Australia's separate spot-exchange AUSTRAC
> registration."

## 1. Trigger

- **Type**: `nation_state_block`
- **Actor**: `AU_ASIC`
- **Timestamp**: `2023-04-06 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://asic.gov.au/about-asic/news-centre/find-a-media-release/2023-releases/23-091mr-binance-australia-derivatives-afs-licence-cancelled/>
  - Wayback: <https://web.archive.org/web/2023/https://asic.gov.au/about-asic/news-centre/find-a-media-release/2023-releases/23-091mr-binance-australia-derivatives-afs-licence-cancelled/>
  - body_hash: `sha256:697f54c2792390c0ebf27994c3d15079598372cf6799662fb9c5210262b889ed`
  - body_path: `sources/http_captures/australia-asic-binance-derivatives-2023/asic-media-release/asic.gov.au__about-asic-news-centre-find-a-media-release-2023-releases-23-091mr-binance-australia-derivatives-afs-licence-cancelled__5f5971f9a2.html`
  > ASIC media release 23-091MR dated 2023-04-06, "Binance Australia
> Derivatives - AFS licence cancelled." ASIC cancelled the Australian
> Financial Services licence of Oztures Trading Pty Ltd, trading as
> Binance Australia Derivatives. The release states that, following
> cancellation, clients could not increase or open derivatives
> positions from 2023-04-14, existing positions had to be closed
> before 2023-04-21, and remaining positions would be closed on
> 2023-04-21. The release also records ASIC's targeted review of
> Binance's Australian financial-services business, including retail
> and wholesale client classification.

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
> Australian users of Binance derivatives. The release also records an
> ASIC targeted review of Binance's Australian financial-services business,
> including its classification of retail and wholesale clients.
> Treated as entity-level at the Binance-Australia-derivatives cohort.

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `direct` · Δt = 0h

**Event label**: `binance_australia_derivatives_afsl_cancelled_operations_shut_down`

**Timestamp**: `2023-04-06 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_legal`**
  - URL: <https://asic.gov.au/about-asic/news-centre/find-a-media-release/2023-releases/23-091mr-binance-australia-derivatives-afs-licence-cancelled/>
  - Wayback: <https://web.archive.org/web/2023/https://asic.gov.au/about-asic/news-centre/find-a-media-release/2023-releases/23-091mr-binance-australia-derivatives-afs-licence-cancelled/>
  - body_hash: `sha256:697f54c2792390c0ebf27994c3d15079598372cf6799662fb9c5210262b889ed`
  - body_path: `sources/http_captures/australia-asic-binance-derivatives-2023/asic-media-release/asic.gov.au__about-asic-news-centre-find-a-media-release-2023-releases-23-091mr-binance-australia-derivatives-afs-licence-cancelled__5f5971f9a2.html`
  > ASIC media release 23-091MR is the legal instrument cancelling
> the Oztures Trading Pty Ltd AFSL. attribution=direct because
> the AFSL cancellation itself compels the operator-state change
> (cessation of Australian-facing derivatives service): without
> an AFSL, the entity may not lawfully offer derivative products
> to Australian clients under the Corporations Act. The
> transitional close-out window (2023-04-14 effective date,
> 2023-04-21 limited close-out deadline) flows directly from the
> ASIC order.

## 5. Honest coverage gaps

- **l4_frontend** (`not_measured`): No replayable Binance AU-geo frontend notice is retained in this

## 7. Related events

- [`uk-fca-binance-markets-2021`](./uk-fca-binance-markets-2021.md)
- [`germany-bafin-binance-licence-withdrawal-2023`](./germany-bafin-binance-licence-withdrawal-2023.md)
- [`belgium-fsma-binance-cease-2023`](./belgium-fsma-binance-cease-2023.md)
- [`netherlands-dnb-binance-warning-2021`](./netherlands-dnb-binance-warning-2021.md)
- [`malaysia-sc-binance-disable-2021`](./malaysia-sc-binance-disable-2021.md)
- [`singapore-mas-binance-services-2021`](./singapore-mas-binance-services-2021.md)
- [`binance-4framework-2023`](./binance-4framework-2023.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `2079264`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

