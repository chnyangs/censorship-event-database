# Evidence chain — `eu-16th-russia-sanctions-2025`

**Status**: `admitted` · **Stratum**: `S6_supranational` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `80b0ca3` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-31` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "The EU's 16th sanctions package (2025-02-24) extended the transaction ban
> to enable listing of financial institutions and crypto-asset providers
> (including Russian crypto-asset exchanges) participating in sanctions
> circumvention, and added banks to the transaction ban for SPFS use,
> debanking that class from the EU transaction surface; single-layer
> offramp_cex observed_change with attribution=direct."

## 1. Trigger

- **Type**: `non_us_sanctions`
- **Actor**: `EU_Council`
- **Timestamp**: `2025-02-24 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://finance.ec.europa.eu/news/eu-adopts-16th-package-sanctions-against-russia-2025-02-24_en>
  - Wayback: <https://web.archive.org/web/20250318121030/https://finance.ec.europa.eu/news/eu-adopts-16th-package-sanctions-against-russia-2025-02-24_en>
  - body_hash: `sha256:e635751e58a561c556ba39ccac4a6b8ffbc0c249c5833e5530cbe8bbcb82dac6`
  - body_path: `sources/http_captures/eu-16th-russia-sanctions-2025/primary/web.archive.org__web-20250301000000-https-finance.ec.europa.eu-news-eu-adopts-16th-package-sanctions-against-russia-2025-02-24_en__ef32c394a1.html`
  > European Commission / Council, 16th sanctions package against Russia
> (adopted 2025-02-24). The captured page records two crypto-relevant
> measures: (1) addition of banks to the transaction ban "due to their
> use of the Financial Messaging System of the Central Bank of Russia
> (SPFS) system to circumvent EU sanctions"; and (2) extension of the
> transaction ban to enable the EU to list financial institutions and
> crypto-asset providers that participate in circumventing the Oil Price
> Cap / facilitate transactions with shadow-fleet vessels, with listings
> including "Russian crypto assets exchanges." Wayback memento
> 20250318121030 pinned.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: EU 16th-package CASP/SPFS transaction-ban extension

> Financial institutions and crypto-asset providers (including Russian
> crypto-asset exchanges) listable under the extended transaction ban for
> participating in sanctions circumvention (Oil Price Cap / shadow fleet),
> plus banks added to the transaction ban for SPFS use. subset because the
> listable CASP/financial-operator class is defined by criteria and the
> individual designations are not exhaustively enumerated in this record.

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `direct` · Δt = 0h

**Event label**: `eu_16th_package_extends_transaction_ban_to_casps_and_spfs_banks`

**Timestamp**: `2025-02-24 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_legal`**
  - URL: <https://finance.ec.europa.eu/news/eu-adopts-16th-package-sanctions-against-russia-2025-02-24_en>
  - Wayback: <https://web.archive.org/web/20250318121030/https://finance.ec.europa.eu/news/eu-adopts-16th-package-sanctions-against-russia-2025-02-24_en>
  - body_hash: `sha256:e635751e58a561c556ba39ccac4a6b8ffbc0c249c5833e5530cbe8bbcb82dac6`
  - body_path: `sources/http_captures/eu-16th-russia-sanctions-2025/primary/web.archive.org__web-20250301000000-https-finance.ec.europa.eu-news-eu-adopts-16th-package-sanctions-against-russia-2025-02-24_en__ef32c394a1.html`
  > EU 16th package (2025-02-24): extends the transaction ban to enable
> listing of "financial institutions and crypto asset providers" that
> participate in sanctions circumvention, lists "Russian crypto assets
> exchanges," and adds banks to the transaction ban for use of the
> "Financial Messaging System of the Central Bank of Russia (SPFS)."
> attribution=direct: the EU legal instrument directly and explicitly
> names crypto-asset providers / exchanges and SPFS as the operative
> targets. Verbatim language confirmed in the captured body
> (body_hash-pinned).

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`eu-14th-russia-sanctions-spfs-2024`](./eu-14th-russia-sanctions-spfs-2024.md)
- [`eu-15th-russia-sanctions-2024`](./eu-15th-russia-sanctions-2024.md)
- [`eu-18th-russia-sanctions-casp-spfs-2025`](./eu-18th-russia-sanctions-casp-spfs-2025.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `80b0ca3`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

