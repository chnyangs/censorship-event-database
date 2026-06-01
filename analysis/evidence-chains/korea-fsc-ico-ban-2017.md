# Evidence chain — `korea-fsc-ico-ban-2017`

**Status**: `admitted` · **Stratum**: `S4_nation_state` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-02` · **Source commit**: `fd81985` · **Schema**: `0.2.0` · **Event last_verified**: `2026-06-01` · **Tool version**: `0.1.0` · **Generated**: `2026-06-02T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> The KR FSC 2017-09-29 joint virtual-currency TF statement imposed a
> full ban on all forms of ICO fundraising and prohibited credit-extension
> products such as money lending / coin-margin trading by virtual-currency
> handlers, including blocking related financial-company business
> partnerships. The retained measured surface is the off-ramp / regulated-
> financial-institution policy prohibition itself; this event does not
> claim separately observed exchange-frontend changes.

## 1. Trigger

- **Type**: `nation_state_block`
- **Actor**: `KR_FSC`
- **Timestamp**: `2017-09-29 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_government`**
  - URL: <https://fsc.go.kr/comm/getFile?srvcId=BBSTY1&upperNo=72848&fileTy=ATTACH&fileNo=2>
  - body_hash: `sha256:978442427b2eeb4d4ed3d7d542962099322979b6212e5a1fbe0b2fe329f30d04`
  - body_path: `sources/http_captures/korea-fsc-ico-ban-2017/primary/fsc.go.kr__comm-getFile__ad65ee6d53.bin`
  > Financial Services Commission (FSC) official 2017-09-29 Korean
> press-release PDF for the virtual-currency joint TF meeting. The
> PDF states that the meeting adopted "all forms of ICO prohibition"
> and prohibited credit extension such as money lending / coin-margin
> trading by virtual-currency handlers, including blocking related
> financial-company business partnerships. Captured 2026-06-01 from
> FSC attachment fileNo=2; PDF text was extracted locally and grepped
> for ICO, all-forms prohibition, credit-extension prohibition, and
> margin-trading terms. This replaces the old drifted English press
> index pointer.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: KR ICO + crypto-margin sector (class)

> Canonical target is the KR FSC policy directive itself, addressed to
> (a) Korean crypto token issuers and ICO promoters (full ban on
> token-issuance fundraising), and (b) Korean financial institutions
> offering margin/lending products for crypto-assets (prohibition).
> The retained target is class-level rather than a named-exchange
> census: the FSC source governs ICO fundraising and virtual-currency-
> handler credit extension / coin-margin trading without enumerating
> platform domains. Any Upbit / Bithumb / Coinone / Korbit platform
> reaction would require a separate operator or Wayback evidence pass.

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `direct` · Δt = 0h

**Event label**: `ico_fundraising_and_crypto_margin_prohibited_sector_wide`

**Timestamp**: `2017-09-29 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_government`**
  - URL: <https://fsc.go.kr/comm/getFile?srvcId=BBSTY1&upperNo=72848&fileTy=ATTACH&fileNo=2>
  - body_hash: `sha256:978442427b2eeb4d4ed3d7d542962099322979b6212e5a1fbe0b2fe329f30d04`
  - body_path: `sources/http_captures/korea-fsc-ico-ban-2017/primary/fsc.go.kr__comm-getFile__ad65ee6d53.bin`
  > FSC official 2017-09-29 Korean press-release PDF. Load-bearing
> lines state that all forms of ICO are prohibited regardless of
> technical terminology and that credit extension by virtual-
> currency handlers, including money lending / coin-margin trading,
> is not permitted, with related financial-company partnerships
> blocked. Direct attribution is to the FSC joint-TF announcement
> itself; this row does not claim separately observed exchange
> homepage changes.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`china-pboc-crypto-ban-2021`](./china-pboc-crypto-ban-2021.md)
- [`korea-travel-rule-2022`](./korea-travel-rule-2022.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `fd81985`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

