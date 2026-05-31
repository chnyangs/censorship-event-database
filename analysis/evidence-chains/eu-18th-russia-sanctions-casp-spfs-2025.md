# Evidence chain — `eu-18th-russia-sanctions-casp-spfs-2025`

**Status**: `admitted` · **Stratum**: `S6_supranational` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `128e1e1` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-31` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "The EU's 18th sanctions package (2025-07-18) broadened the transaction ban
> for third-country financial operators to expressly include crypto-asset
> service providers connected to Russia's SPFS or circumventing sanctions,
> banning EU operators from transacting with any such listed CASP; single-layer
> offramp_cex observed_change with attribution=direct."

## 1. Trigger

- **Type**: `non_us_sanctions`
- **Actor**: `EU_Council`
- **Timestamp**: `2025-07-18 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://finance.ec.europa.eu/news/eu-adopts-18th-package-sanctions-against-russia-2025-07-18_en>
  - Wayback: <https://web.archive.org/web/20250805164642/https://finance.ec.europa.eu/news/eu-adopts-18th-package-sanctions-against-russia-2025-07-18_en>
  - body_hash: `sha256:48205d9d6c844e0ae49f09c880e95ec65ac77c978e557d801861f1b6919dfcb1`
  - body_path: `sources/http_captures/eu-18th-russia-sanctions-casp-spfs-2025/primary/web.archive.org__web-20250801000000-https-finance.ec.europa.eu-news-eu-adopts-18th-package-sanctions-against-russia-2025-07-18_en__17e8fac1f5.html`
  > European Commission / Council, 18th sanctions package against Russia
> (adopted 2025-07-18). The captured page states verbatim: "Broadening
> the transaction ban for third-country financial operators, including
> crypto-asset providers who help circumvent sanctions, support Russia's
> war of aggression against Ukraine, or are connected to Russia's
> financial messaging service. EU operators are banned from carrying out
> transactions with any of those financial operators." The package
> lowers the threshold to impose a full transaction ban on third-country
> crypto-asset service providers connected to Russia's SPFS (System for
> Transfer of Financial Messages) or otherwise frustrating EU sanctions,
> widening the grounds for listing such entities. Wayback memento
> 20250805164642 pinned.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: EU 18th-package CASP/SPFS transaction-ban broadening

> Third-country crypto-asset service providers (and other third-country
> financial operators) connected to Russia's SPFS financial-messaging
> system or otherwise helping circumvent EU sanctions. The 18th package
> broadens the transaction ban so that EU operators are prohibited from
> transacting with any such listed CASP/financial operator, and widens the
> grounds for listing. subset because the listable CASP/operator class is
> defined by criteria (SPFS connection / circumvention) rather than an
> exhaustively enumerated address or provider list in this record.

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `direct` · Δt = 0h

**Event label**: `eu_18th_package_broadens_transaction_ban_on_spfs_connected_casps`

**Timestamp**: `2025-07-18 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_legal`**
  - URL: <https://finance.ec.europa.eu/news/eu-adopts-18th-package-sanctions-against-russia-2025-07-18_en>
  - Wayback: <https://web.archive.org/web/20250805164642/https://finance.ec.europa.eu/news/eu-adopts-18th-package-sanctions-against-russia-2025-07-18_en>
  - body_hash: `sha256:48205d9d6c844e0ae49f09c880e95ec65ac77c978e557d801861f1b6919dfcb1`
  - body_path: `sources/http_captures/eu-18th-russia-sanctions-casp-spfs-2025/primary/web.archive.org__web-20250801000000-https-finance.ec.europa.eu-news-eu-adopts-18th-package-sanctions-against-russia-2025-07-18_en__17e8fac1f5.html`
  > EU 18th package (2025-07-18): broadens the transaction ban for
> third-country financial operators "including crypto-asset providers
> who help circumvent sanctions ... or are connected to Russia's
> financial messaging service" (SPFS); EU operators are banned from
> transacting with any such operator. attribution=direct: the EU legal
> instrument directly and explicitly names crypto-asset providers as
> the prohibited transaction counterparty class. Verbatim language
> confirmed in the captured body (body_hash-pinned).

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`eu-14th-russia-sanctions-spfs-2024`](./eu-14th-russia-sanctions-spfs-2024.md)
- [`eu-15th-russia-sanctions-2024`](./eu-15th-russia-sanctions-2024.md)
- [`eu-16th-russia-sanctions-2025`](./eu-16th-russia-sanctions-2025.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `128e1e1`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

