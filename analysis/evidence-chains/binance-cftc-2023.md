# Evidence chain — `binance-cftc-2023`

**Status**: `admitted` · **Stratum**: `S3_doj_sec_cftc_fiod` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-02` · **Source commit**: `b6c6fae` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-16` · **Tool version**: `0.1.0` · **Generated**: `2026-06-02T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "The 2023-03-27 CFTC civil complaint in N.D. Ill. against Binance
> Holdings + Changpeng Zhao + Samuel Lim (former CCO) is the first of
> four US federal enforcement actions that converge on the 2023-11-21
> multi-agency $4.3B settlement. The CFTC complaint initiates the
> rails-level commodities-derivatives enforcement axis against Binance;
> the structural rails remediation (compliance-monitor regime, $1.35B
> CFTC penalty) attaches to the 2023-11-21 consolidated settlement
> (binance-4framework-2023), not to the 2023-03-27 filing date. One
> observed_change layer (offramp_cex) with direct attribution."

## 1. Trigger

- **Type**: `cftc_action`
- **Actor**: `US_CFTC`
- **Timestamp**: `2023-03-27 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://www.cftc.gov/PressRoom/PressReleases/8680-23>
  - Wayback: <https://web.archive.org/web/20260516000000/https://www.cftc.gov/PressRoom/PressReleases/8680-23>
  > CFTC press release 8680-23 (2023-03-27): "CFTC Charges Binance and
> Its Founder, Changpeng Zhao, with Willful Evasion of Federal Law
> and Operating an Illegal Digital Asset Derivatives Exchange." Civil
> enforcement complaint filed in U.S. District Court for the Northern
> District of Illinois against Binance Holdings Limited, Binance
> Holdings (IE) Limited, Binance (Services) Holdings Limited,
> Changpeng Zhao (CEO/founder), and Samuel Lim (former Chief
> Compliance Officer). Charges include (a) operating an unregistered
> derivatives exchange / DCM / SEF / FCM, (b) offering illegal
> off-exchange commodity-option / leveraged retail commodity
> transactions to US persons, (c) willful evasion of US federal law
> via deliberate VPN-based circumvention guidance to US customers,
> and (d) BSA / AML / KYC failures. Resolved 2023-11-21 via $1.35B
> CFTC monetary penalty as part of the broader multi-agency
> $4.3B settlement (DOJ + FinCEN + OFAC + CFTC).

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: Binance Holdings + Changpeng Zhao + Samuel Lim
- **Canonical domains**: `binance.com`

> Binance Holdings Limited + Binance Holdings (IE) Limited + Binance
> (Services) Holdings Limited (corporate entities operating the global
> Binance platform) + Changpeng Zhao (CEO / founder) + Samuel Lim
> (former Chief Compliance Officer). Canonical domain binance.com
> remained operational throughout the CFTC complaint stage; the
> structural rails-level resolution did not occur until the 2023-11-21
> multi-agency $4.3B settlement (see binance-4framework-2023).

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `direct` · Δt = 0h

**Event label**: `cftc_complaint_initiates_binance_us_rails_enforcement_axis`

**Timestamp**: `2023-03-27 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_legal`**
  - URL: <https://www.cftc.gov/PressRoom/PressReleases/8680-23>
  - Wayback: <https://web.archive.org/web/20260516000000/https://www.cftc.gov/PressRoom/PressReleases/8680-23>
  > CFTC press release 8680-23 anchors the 2023-03-27 commencement
> of the formal CFTC enforcement axis against the Binance
> off-ramp. The complaint pleads operation of an unregistered
> DCM / SEF / FCM offering illegal leveraged retail commodity
> transactions to US persons + willful VPN-based circumvention
> guidance + BSA-AML failures. attribution=direct because the
> CFTC press release / complaint is the legal instrument
> initiating the rails-level enforcement chain that resolves
> 2023-11-21 via the $1.35B CFTC monetary penalty (one of the
> four federal-agency penalties in the $4.3B multi-agency
> settlement). The CFTC complaint is therefore the first of
> the four US federal enforcement actions that converge on the
> 2023-11-21 multi-agency settlement.

## 5. Honest coverage gaps

- **l4_frontend** (`not_measured`): No admission-grade L4 frontend diff is retained for the CFTC

## 7. Related events

- [`binance-4framework-2023`](./binance-4framework-2023.md)
- [`sec-v-binance-2023`](./sec-v-binance-2023.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `b6c6fae`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

