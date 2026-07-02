# Evidence chain — `genesis-market-ofac-2023-04`

**Status**: `admitted` · **Stratum**: `S1_ofac_sdn` · **Shape**: `null_event` (0 changed layer(s): none) · **Tier**: `null_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-08` · **Source commit**: `ee7bf1a` · **Schema**: `0.2.0` · **Event last_verified**: `2026-06-02` · **Tool version**: `0.1.0` · **Generated**: `2026-06-25T23:48:26Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "The 2023-04-05 OFAC E.O. 13694 designation of the Genesis Market
> cybercrime marketplace (coordinated with Operation Cookie Monster)
> enumerated no on-chain addresses; no public CEX cascade was documented in
> the 14-day window. null_case: entity target with limited measurable
> cross-layer surface."

## 1. Trigger

- **Type**: `ofac_sdn_designation`
- **Actor**: `US_OFAC`
- **Timestamp**: `2023-04-05 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://home.treasury.gov/news/press-releases/jy1388>
  - Wayback: <https://web.archive.org/web/20230405235346/https://home.treasury.gov/news/press-releases/jy1388>
  - body_hash: `sha256:02e921aab0d82ca5dae0a6e13e721b775f0eaf5837436d4598df3fec30912d1c`
  - body_path: `sources/http_captures/genesis-market-ofac-2023-04/primary/web.archive.org__web-20230405235346-https-home.treasury.gov-news-press-releases-jy1388__f6aa071506.html`
  > U.S. Treasury press release jy1388 (2023-04-05), "Treasury
> Sanctions Illicit Marketplace Genesis Market." OFAC designated
> Genesis Market — a cybercrime marketplace selling stolen device
> credentials / access packages — pursuant to E.O. 13694 (as
> amended), coordinated with the DOJ/FBI Operation Cookie Monster
> takedown and domain seizure. Wayback memento 20230405235346
> pinned.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: Genesis Market

> Genesis Market designated as an SDN entity under E.O. 13694. Marked
> subset because the OFAC entry names the marketplace entity rather than
> enumerating a complete on-chain address cohort. The parallel Operation
> Cookie Monster domain seizure (FBI/DOJ + international partners) is a
> separate legal instrument from the OFAC SDN designation tracked here.

## 3. Changed-layer observations (supports the scoped claim)

*No observed_change entries. This is a `null_event`; see §4 for observed_no_change evidence supporting the null claim.*

## 4. No-change observations (where applicable)

### offramp_cex — `no_public_cex_cascade_documented_in_14d_window`

**Window**: `2023-04-05 00:00:00+00:00` → `2023-04-19 23:59:59+00:00`

**Sources**:

- **`primary_legal`**
  - URL: <https://home.treasury.gov/news/press-releases/jy1388>
  - Wayback: <https://web.archive.org/web/20230405235346/https://home.treasury.gov/news/press-releases/jy1388>
  - body_hash: `sha256:02e921aab0d82ca5dae0a6e13e721b775f0eaf5837436d4598df3fec30912d1c`
  - body_path: `sources/http_captures/genesis-market-ofac-2023-04/primary/web.archive.org__web-20230405235346-https-home.treasury.gov-news-press-releases-jy1388__f6aa071506.html`
  > No public CEX policy statement referencing the Genesis Market
> designation was published by major exchanges in the 14-day post-
> designation window. Observation records the absence of public
> disclosure; private chain-analytics KYT flagging is outside this
> observation's scope. Genesis Market is an entity target with no
> enumerated on-chain addresses, so the measurable offramp-cascade
> surface is structurally limited.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `ee7bf1a`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

