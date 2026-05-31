# Evidence chain — `eu-19th-russia-sanctions-a7a5-crypto-ban-2025`

**Status**: `admitted` · **Stratum**: `S6_supranational` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `7542617` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-31` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "The EU's 19th sanctions package (2025-10-23) prohibited transactions
> involving the A7A5 rouble-backed stablecoin across the EU and designated
> its developer, Kyrgyz issuer, and trading-platform operator - the EU's
> first transaction ban on a specific named crypto-asset; single-layer
> offramp_cex observed_change with attribution=direct."

## 1. Trigger

- **Type**: `non_us_sanctions`
- **Actor**: `EU_Council`
- **Timestamp**: `2025-10-23 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://www.consilium.europa.eu/en/press/press-releases/2025/10/23/19th-package-of-sanctions-against-russia-eu-targets-russian-energy-third-country-banks-and-crypto-providers/>
  - Wayback: <https://web.archive.org/web/20251023125146/https://www.consilium.europa.eu/en/press/press-releases/2025/10/23/19th-package-of-sanctions-against-russia-eu-targets-russian-energy-third-country-banks-and-crypto-providers/>
  - body_hash: `sha256:405b69089a485505187b39ad3b3c07f3fdb305d340e70eabba1c46f12bb81a8d`
  - body_path: `sources/http_captures/eu-19th-russia-sanctions-a7a5-crypto-ban-2025/primary/web.archive.org__web-20251024000000-https-www.consilium.europa.eu-en-press-press-releases-2025-10-23-19th-package-of-sanctions-against-russia-eu-targets-russian-energy__cd341e65af.html`
  > Council of the EU, 19th sanctions package against Russia (adopted
> 2025-10-23). The captured press release states verbatim: "the
> stablecoin A7A5 - created with Russian state support - has emerged
> as a prominent tool for financing activities supporting the war of
> aggression. Therefore, today's package introduces sanctions on the
> developer of A7A5, the Kyrgyz issuer of that coin, and the operator
> of a platform where significant volumes of A7A5 is traded.
> Transactions involving this stablecoin have also been prohibited
> across the EU." This is the EU's first prohibition on transacting a
> specific named crypto-asset (the A7A5 rouble-backed stablecoin),
> plus designations of its developer / Kyrgyz issuer / trading-platform
> operator. Wayback memento 20251023125146 pinned.
- **`supporting_journalism`**
  - URL: <https://www.elliptic.co/blog/crypto-regulatory-affairs-eu-sanctions-target-a7a5-ruble-backed-stablecoin>
  - Wayback: <https://web.archive.org/web/20260207172617/https://www.elliptic.co/blog/crypto-regulatory-affairs-eu-sanctions-target-a7a5-ruble-backed-stablecoin>
  - body_hash: `sha256:489642274d0efd48b47f7c5941630e7455583e6005c71e7138a71fa97538fabc`
  - body_path: `sources/http_captures/eu-19th-russia-sanctions-a7a5-crypto-ban-2025/primary/web.archive.org__web-20260207000000-https-www.elliptic.co-blog-crypto-regulatory-affairs-eu-sanctions-target-a7a5-ruble-backed-stablecoin__fdc0f33728.html`
  > Elliptic analysis corroborating the 19th-package A7A5 prohibition:
> "the EU's sanctions prohibit persons within the EU from engaging in
> any transactions, directly or indirectly, involving the A7A5
> ruble-backed stablecoin." Captured body further notes A7A5 is a
> stablecoin available on the Ethereum and Tron blockchains, issued by
> a Kyrgyzstan-based company (Old Vector LLC). Independent corroborating
> anchor.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: EU 19th-package A7A5 stablecoin transaction ban + designations

> The A7A5 rouble-backed stablecoin (transactions involving it prohibited
> across the EU), plus the designated developer of A7A5, its Kyrgyz issuer,
> and the operator of a platform where significant volumes of A7A5 are
> traded. subset because the captured EU primary names the target class /
> designees descriptively (A7A5 + developer/issuer/platform-operator)
> rather than enumerating specific on-chain addresses in this record.

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `direct` · Δt = 0h

**Event label**: `eu_19th_package_prohibits_transactions_in_a7a5_stablecoin`

**Timestamp**: `2025-10-23 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_legal`**
  - URL: <https://www.consilium.europa.eu/en/press/press-releases/2025/10/23/19th-package-of-sanctions-against-russia-eu-targets-russian-energy-third-country-banks-and-crypto-providers/>
  - Wayback: <https://web.archive.org/web/20251023125146/https://www.consilium.europa.eu/en/press/press-releases/2025/10/23/19th-package-of-sanctions-against-russia-eu-targets-russian-energy-third-country-banks-and-crypto-providers/>
  - body_hash: `sha256:405b69089a485505187b39ad3b3c07f3fdb305d340e70eabba1c46f12bb81a8d`
  - body_path: `sources/http_captures/eu-19th-russia-sanctions-a7a5-crypto-ban-2025/primary/web.archive.org__web-20251024000000-https-www.consilium.europa.eu-en-press-press-releases-2025-10-23-19th-package-of-sanctions-against-russia-eu-targets-russian-energy__cd341e65af.html`
  > EU 19th package (2025-10-23): "Transactions involving this
> stablecoin [A7A5] have also been prohibited across the EU"; the
> package "introduces sanctions on the developer of A7A5, the Kyrgyz
> issuer of that coin, and the operator of a platform where
> significant volumes of A7A5 is traded." attribution=direct: the EU
> legal instrument directly names the prohibited crypto-asset (A7A5)
> and its service infrastructure. Verbatim language grep-confirmed in
> the captured body (body_hash-pinned).
- **`supporting_journalism`**
  - URL: <https://www.elliptic.co/blog/crypto-regulatory-affairs-eu-sanctions-target-a7a5-ruble-backed-stablecoin>
  - Wayback: <https://web.archive.org/web/20260207172617/https://www.elliptic.co/blog/crypto-regulatory-affairs-eu-sanctions-target-a7a5-ruble-backed-stablecoin>
  - body_hash: `sha256:489642274d0efd48b47f7c5941630e7455583e6005c71e7138a71fa97538fabc`
  - body_path: `sources/http_captures/eu-19th-russia-sanctions-a7a5-crypto-ban-2025/primary/web.archive.org__web-20260207000000-https-www.elliptic.co-blog-crypto-regulatory-affairs-eu-sanctions-target-a7a5-ruble-backed-stablecoin__fdc0f33728.html`
  > Elliptic corroboration: "the EU's sanctions prohibit persons within
> the EU from engaging in any transactions, directly or indirectly,
> involving the A7A5 ruble-backed stablecoin." Independent
> semi-primary anchor.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`eu-18th-russia-sanctions-casp-spfs-2025`](./eu-18th-russia-sanctions-casp-spfs-2025.md)
- [`eu-8th-package-russia-crypto-services-ban-2022-10`](./eu-8th-package-russia-crypto-services-ban-2022-10.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `7542617`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

