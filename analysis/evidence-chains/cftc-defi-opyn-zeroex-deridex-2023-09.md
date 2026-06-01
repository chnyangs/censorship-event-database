# Evidence chain — `cftc-defi-opyn-zeroex-deridex-2023-09`

**Status**: `admitted` · **Stratum**: `S3_doj_sec_cftc_fiod` · **Shape**: `comparison` (1 changed layer(s): `l4_frontend`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-02` · **Source commit**: `295a15d` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-31` · **Tool version**: `0.1.0` · **Generated**: `2026-06-02T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "The CFTC's 2023-09-07 simultaneous settlement orders (press release 8774-23)
> against three DeFi-protocol operators — Opyn, Inc. ($250,000), ZeroEx, Inc. /
> 0x ($200,000), and Deridex, Inc. ($100,000) — ordered each to cease and
> desist from offering unregistered leveraged digital-asset-derivatives trading
> to U.S. persons, operationalizing a register-or-geoblock-US-users restriction
> on legitimate DeFi protocols at the operator frontend / U.S.-person access
> layer (l4_frontend load-bearing, attribution=direct). The row does not claim
> ISP-level blocking, on-chain asset freeze, or a CEX off-ramp action."

## 1. Trigger

- **Type**: `cftc_action`
- **Actor**: `US_CFTC`
- **Timestamp**: `2023-09-07 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_government`**
  - URL: <https://www.cftc.gov/PressRoom/PressReleases/8774-23>
  - Wayback: <https://web.archive.org/web/20230908043407/https://www.cftc.gov/PressRoom/PressReleases/8774-23>
  - body_hash: `sha256:a013f296efc95d37f306e1a41c1f9cacb9510e4eab2745b4cf4eaed40b535918`
  - body_path: `sources/http_captures/cftc-defi-opyn-zeroex-deridex-2023-09/primary/web.archive.org__web-20230908000000-https-www.cftc.gov-PressRoom-PressReleases-8774-23__1c73b942d5.html`
  > CFTC press release 8774-23 (dated "September 07, 2023"): "CFTC Issues
> Orders Against Operators of Three DeFi Protocols for Offering Illegal
> Digital Asset Derivatives Trading." The CFTC simultaneously filed and
> settled charges against Opyn, Inc., ZeroEx, Inc. (0x), and Deridex,
> Inc., requiring each to "cease and desist from violating the Commodity
> Exchange Act" and pay civil monetary penalties of $250,000, $200,000,
> and $100,000 respectively. Charges include operating unregistered
> platforms that allow U.S. persons to trade leveraged/margined retail
> commodity transactions and digital-asset derivatives, and failing to
> register as a swap execution facility (SEF) / designated contract
> market (DCM) / futures commission merchant (FCM). Captured body notes
> that Opyn "took certain steps to exclude U.S. persons from accessing
> the Opyn Protocol, such as block[ing US IP addresses]" (found
> insufficient) while Deridex "took no steps to exclude U.S. persons."
> Grep-confirmed in captured body: "Opyn", "ZeroEx", "Deridex", "cease
> and desist", "$250,000", "$200,000", "$100,000", "September 07, 2023",
> "swap execution facility", "U.S. persons", "register". Wayback memento
> 20230908043407 captured 2026-05-31.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: Opyn, Inc. + ZeroEx, Inc. (0x) + Deridex, Inc.
- **Chains**: `ethereum`
- **Canonical domains**: `opyn.co`, `0x.org`, `deridex.io`

> Three DeFi-protocol operating companies named in CFTC press release
> 8774-23: Opyn, Inc. (Delaware-registered, California-based; operator of the
> Opyn Protocol), ZeroEx, Inc. (operator of the 0x / Matcha protocol), and
> Deridex, Inc. (operator of the Deridex perpetual-contracts protocol). The
> CFTC orders name these three operators as respondents; the underlying
> smart-contract protocols and their broader user cohorts are not enumerated
> address-by-address, so the enumeration is coded subset.

## 3. Changed-layer observations (supports the scoped claim)

### l4_frontend · attribution: `direct` · Δt = 0h

**Event label**: `cftc_orders_three_defi_operators_to_cease_offering_to_us_persons`

**Timestamp**: `2023-09-07 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_government`**
  - URL: <https://www.cftc.gov/PressRoom/PressReleases/8774-23>
  - Wayback: <https://web.archive.org/web/20230908043407/https://www.cftc.gov/PressRoom/PressReleases/8774-23>
  - body_hash: `sha256:a013f296efc95d37f306e1a41c1f9cacb9510e4eab2745b4cf4eaed40b535918`
  - body_path: `sources/http_captures/cftc-defi-opyn-zeroex-deridex-2023-09/primary/web.archive.org__web-20230908000000-https-www.cftc.gov-PressRoom-PressReleases-8774-23__1c73b942d5.html`
  > CFTC press release 8774-23 ("September 07, 2023") is the set of legal
> instruments naming Opyn, Inc., ZeroEx, Inc. (0x), and Deridex, Inc. as
> respondents and ordering each to cease and desist from violating the
> Commodity Exchange Act — i.e. to stop offering their unregistered
> leveraged/margined digital-asset-derivatives protocols to U.S.
> persons absent registration. Penalties: $250,000 (Opyn), $200,000
> (ZeroEx), $100,000 (Deridex). The captured body anchors the
> U.S.-person access gate (Opyn IP-block steps deemed insufficient;
> Deridex took none). attribution=direct per codebook §1.1 — the named
> actor (CFTC) issues the orders and the orders name the targets (the
> three operators) being acted upon. delta_hours=0 (orders filed and
> settled simultaneously at the order date).

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`cftc-v-ooki-dao-2022`](./cftc-v-ooki-dao-2022.md)
- [`binance-cftc-2023`](./binance-cftc-2023.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `295a15d`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

