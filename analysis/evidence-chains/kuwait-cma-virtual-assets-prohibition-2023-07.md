# Evidence chain — `kuwait-cma-virtual-assets-prohibition-2023-07`

**Status**: `admitted` · **Stratum**: `S4_nation_state` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-08` · **Source commit**: `ee7bf1a` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-31` · **Tool version**: `0.1.0` · **Generated**: `2026-06-25T23:48:26Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "Kuwait's 2023-07-17 virtual-assets circular prohibited use of virtual assets
> as payment instruments, dealing with them as investment media, granting VASP
> commercial licenses, and virtual-asset mining activity. The event is modeled
> as a single-layer S4 nation-state payment/commercial-rail restriction at
> offramp_cex; no L0/L1/L3/L4 or asset-onchain effect is claimed."

## 1. Trigger

- **Type**: `nation_state_block`
- **Actor**: `KW_CMA_CBK`
- **Timestamp**: `2023-07-17 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://www.cbk.gov.kw/en/images/16part1-2788_v60_tcm10-2788.pdf>
  - body_hash: `sha256:eaceca4e2bdb5843915f04a62a0fe441015fe087e6e699e82eb5983a8494dc6c`
  - body_path: `sources/http_captures/kuwait-cma-virtual-assets-prohibition-2023-07/primary/www.cbk.gov.kw__en-images-16part1-2788_v60_tcm10-2788.pdf__f60cea3fb8.bin`
  > Central Bank of Kuwait AML/CFT instructions PDF, section Q, reproduces
> the 2023-07-17 circular to local banks, financing companies, and
> exchange companies concerning virtual-assets transaction procedures.
> `pdftotext` on the captured PDF confirms the circular title and the
> load-bearing restrictions: strict prohibition of using virtual assets as
> a payment instrument, prohibition on dealing with virtual assets as an
> investment medium, no natural or legal person in Kuwait to be granted a
> virtual-asset-service license, and absolute prohibition of virtual-asset
> mining activities.
- **`primary_government`**
  - URL: <https://www.cma.gov.kw/en/web/cma/cma-board-releases/resolutions-and-regulations/-/cmaboardreleases/detail/1384960>
  > Kuwait Capital Markets Authority circular page for Circular No. 10 of
> 2023. Live inspection on 2026-05-31 confirms the same restrictions and
> publication metadata, but local capture timed out from the CLI; do not
> use this URL as the sole replay anchor until it is captured.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: Kuwait virtual-asset payment, investment, VASP, and mining activity

> Kuwait financial institutions, specified financial businesses, exchange
> companies, prospective VASPs, and local virtual-asset mining activity. The
> circular is class-level and does not enumerate individual exchanges,
> miners, users, domains, tokens, or addresses; subset records the addressed
> regulated-institution / commercial-activity class without claiming a
> complete roster.

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `direct` · Δt = 0h

**Event label**: `virtual_asset_payment_investment_vasp_and_mining_prohibited`

**Timestamp**: `2023-07-17 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_legal`**
  - URL: <https://www.cbk.gov.kw/en/images/16part1-2788_v60_tcm10-2788.pdf>
  - body_hash: `sha256:eaceca4e2bdb5843915f04a62a0fe441015fe087e6e699e82eb5983a8494dc6c`
  - body_path: `sources/http_captures/kuwait-cma-virtual-assets-prohibition-2023-07/primary/www.cbk.gov.kw__en-images-16part1-2788_v60_tcm10-2788.pdf__f60cea3fb8.bin`
  > The captured CBK PDF is the replayable legal anchor. It instructs the
> addressed Kuwaiti financial institutions to refrain from virtual-asset
> payment and investment transactions, states that no VASP commercial
> licenses will be issued, and prohibits all virtual-asset mining
> activity. attribution=direct because the regulatory instrument itself
> names the restricted activity class.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- `saudi-standing-committee-crypto-illegal-2018-08` (not found; no rendered admitted-chain link)
- [`qatar-qcb-qfcra-virtual-asset-ban-2019-12`](./qatar-qcb-qfcra-virtual-asset-ban-2019-12.md)
- `bahrain-cbb-crypto-asset-module-2019` (not found; no rendered admitted-chain link)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `ee7bf1a`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

