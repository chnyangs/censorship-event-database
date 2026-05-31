# Evidence chain — `oecd-carf-2022`

**Status**: `admitted` · **Stratum**: `S6_supranational` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `9fed8c7` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-16` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "The OECD's 2022-10-10 Crypto-Asset Reporting Framework (CARF)
> publication established the first binding supranational crypto
> tax-reporting standard, mandating that Reporting Crypto-Asset
> Service Providers (RCASPs) — centralized exchanges, brokers,
> dealers, and crypto ATM operators — report relevant crypto-asset
> transactions to domestic tax authorities for automatic exchange
> under CRS-equivalent mechanics. CARF is the third major
> supranational instrument shaping the RCASP / CASP / VASP operating
> environment alongside EU MiCA (eu-mica-2023) and FATF Recommendation
> 15 (fatf-r15-vasp-travel-rule-2019). Empirical_shape=comparison;
> load-bearing axis is offramp_cex at the RCASP reporting-obligation
> layer."

## 1. Trigger

- **Type**: `supranational_regulation`
- **Actor**: `OECD`
- **Timestamp**: `2022-10-10 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://www.oecd.org/tax/exchange-of-tax-information/crypto-asset-reporting-framework-and-amendments-to-the-common-reporting-standard.htm>
  - Wayback: <https://web.archive.org/web/20260516000000/https://www.oecd.org/tax/exchange-of-tax-information/crypto-asset-reporting-framework-and-amendments-to-the-common-reporting-standard.htm>
  > OECD Crypto-Asset Reporting Framework (CARF) published 2022-10-10 by
> the OECD Committee on Fiscal Affairs at the request of the G20. CARF
> is the first binding supranational crypto tax-reporting standard,
> functioning as a companion to the Common Reporting Standard (CRS)
> first published 2014. The instrument mandates that Reporting
> Crypto-Asset Service Providers (RCASPs) — broadly defined to cover
> centralized exchanges, brokers, dealers, and operators of crypto
> ATMs — collect and transmit transaction-level reporting on relevant
> crypto-asset transactions to their domestic tax authorities, which
> then automatically exchange the data with partner jurisdictions
> under the CRS multilateral framework. Companion amendments to CRS
> were issued in the same publication to capture central-bank digital
> currencies and specified electronic money products. The 2022-10-10
> publication is the foundational instrument; subsequent OECD work
> delivered the Multilateral Competent Authority Agreement (MCAA) for
> CARF on 2023-11-10, with the first reporting under CARF scheduled
> for 2027 (covering 2026 calendar-year transactions) in 48+
> jurisdictions that committed to early adoption in the 2023-11-10
> joint statement.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: OECD Reporting Crypto-Asset Service Provider ecosystem (CARF-regulated)

> Reporting Crypto-Asset Service Providers (RCASPs) operating in CARF-
> adopting jurisdictions. RCASPs are defined to include centralized
> crypto exchanges (Coinbase, Kraken, Binance country entities,
> Bitstamp, Bitpanda, etc.), brokers, dealers, and operators of crypto
> ATMs that effectuate relevant exchange transactions in crypto-assets
> as a business. Self-hosted (non-custodial) wallets and most peer-to-
> peer protocol activity remain out of scope at the protocol level,
> but RCASP-intermediated transfers to / from self-custody addresses
> fall within the reporting perimeter when the RCASP is the
> counterparty. No address-level enumeration — this is sector-wide
> tax-reporting regulation operating at the RCASP entity class.

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `direct` · Δt = 0h

**Event label**: `oecd_carf_published_first_binding_supranational_crypto_tax_reporting_standard`

**Timestamp**: `2022-10-10 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_legal`**
  - URL: <https://www.oecd.org/tax/exchange-of-tax-information/crypto-asset-reporting-framework-and-amendments-to-the-common-reporting-standard.htm>
  - Wayback: <https://web.archive.org/web/20260516000000/https://www.oecd.org/tax/exchange-of-tax-information/crypto-asset-reporting-framework-and-amendments-to-the-common-reporting-standard.htm>
  > OECD CARF publication 2022-10-10 is the primary legal instrument.
> The OECD Committee on Fiscal Affairs (acting at G20 instruction)
> is the direct supranational actor. CARF-adopting jurisdictions
> subsequently transpose the framework into domestic law (e.g. EU
> via DAC8 Directive 2023/2226 adopted 2023-10-17; UK via 2024
> Finance Act amendments; 48+ jurisdictions per the 2023-11-10
> joint statement) and impose CARF-equivalent reporting on RCASPs
> domiciled or operating in their territory. attribution=direct
> because the CARF text itself defines the RCASP entity class and
> mandates the reporting behavior; the supranational framework is
> the substantive driver, with subsequent domestic transposition
> acts as direct implementations rather than independent triggers.
- **`primary_legal`**
  - URL: <https://www.oecd.org/tax/exchange-of-tax-information/crypto-asset-reporting-framework-and-amendments-to-the-common-reporting-standard.htm>
  - Wayback: <https://web.archive.org/web/20260516000001/https://www.oecd.org/tax/exchange-of-tax-information/crypto-asset-reporting-framework-and-amendments-to-the-common-reporting-standard.htm>
  > Second anchor to the same OECD CARF publication — covers the
> companion CRS amendments (CBDC + specified electronic money
> coverage) and the foundational definition of "Reporting
> Crypto-Asset" / "Relevant Crypto-Asset" / "Relevant Transaction"
> that govern the RCASP reporting perimeter. Cross-reference
> context for the CARF Multilateral Competent Authority Agreement
> (CARF MCAA) signed 2023-11-10 by 48+ jurisdictions.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`eu-mica-2023`](./eu-mica-2023.md)
- [`fatf-r15-vasp-travel-rule-2019`](./fatf-r15-vasp-travel-rule-2019.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `9fed8c7`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

