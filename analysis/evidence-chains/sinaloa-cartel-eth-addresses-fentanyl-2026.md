# Evidence chain — `sinaloa-cartel-eth-addresses-fentanyl-2026`

**Status**: `admitted` · **Stratum**: `S1_ofac_sdn` · **Shape**: `null_event` (0 changed layer(s): none) · **Tier**: `null_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-08` · **Source commit**: `ee7bf1a` · **Schema**: `0.2.0` · **Event last_verified**: `2026-06-08` · **Tool version**: `0.1.0` · **Generated**: `2026-06-25T23:48:26Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "OFAC's 2026-05-20 SDN designation of a Sinaloa Cartel fentanyl cell (sb0503)
> added six Ethereum addresses to the SDN list; no public CEX cascade was
> documented in the 14-day window. attested_secondary null_case."

## 1. Trigger

- **Type**: `ofac_sdn_designation`
- **Actor**: `US_OFAC`
- **Timestamp**: `2026-05-20 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_government`**
  - URL: <https://home.treasury.gov/news/press-releases/sb0503>
  > OFAC press release sb0503 (2026-05-20) "Treasury Disrupts Sinaloa Cartel
> Narco-Terrorist Fentanyl Trafficking Operations" — 11 individuals + 2 entities,
> 6 Ethereum addresses to the SDN list. treasury.gov blocks automated capture, so
> this primary is cited contextually; the captured TRM Labs analysis carries the
> enumerated addresses and anchors the attested_secondary admission.
- **`supporting_tracker`**
  - URL: <https://www.trmlabs.com/resources/blog/ofac-sanctions-sinaloa-cartel-network-including-six-ethereum-addresses>
  - body_hash: `sha256:8456cbe000486fc421a2d00f1c171224e70df3afa894159fc7285a8ec9caac68`
  - body_path: `sources/http_captures/sinaloa-cartel-eth-addresses-fentanyl-2026/secondary/www.trmlabs.com__resources-blog-ofac-sanctions-sinaloa-cartel-network-including-six-ethereum-addresses__0979a17909.html`
  > TRM Labs analysis (captured 2026-06-08) enumerating the six designated ETH
> addresses: five to Armando de Jesus Ojeda Aviles, one to Liliana Orozco Romero.

## 2. Target

- **Kind**: `address_set`
- **Enumeration**: `complete`
- **Chains**: `ethereum`
- **Addresses**: 6 total (enumerated in event YAML)

## 3. Changed-layer observations (supports the scoped claim)

*No observed_change entries. This is a `null_event`; see §4 for observed_no_change evidence supporting the null claim.*

## 4. No-change observations (where applicable)

### offramp_cex — `no_public_cex_cascade_documented_in_14d_window`

**Window**: `2026-05-20 00:00:00+00:00` → `2026-06-03 23:59:59+00:00`

**Sources**:

- **`supporting_tracker`**
  - URL: <https://www.trmlabs.com/resources/blog/ofac-sanctions-sinaloa-cartel-network-including-six-ethereum-addresses>
  - body_hash: `sha256:8456cbe000486fc421a2d00f1c171224e70df3afa894159fc7285a8ec9caac68`
  - body_path: `sources/http_captures/sinaloa-cartel-eth-addresses-fentanyl-2026/secondary/www.trmlabs.com__resources-blog-ofac-sanctions-sinaloa-cartel-network-including-six-ethereum-addresses__0979a17909.html`
  > null_event anchor (attested_secondary): TRM Labs analysis of the
> 2026-05-20 OFAC SDN designation of the Sinaloa Cartel fentanyl cell
> (six ETH addresses). No public CEX cascade explicitly naming the SDN
> entries was documented in the 14-day window.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `ee7bf1a`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

