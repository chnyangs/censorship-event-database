# Evidence chain — `indonesia-kominfo-exchange-social-account-block-2024-07`

**Status**: `admitted` · **Stratum**: `S4_nation_state` · **Shape**: `comparison` (1 changed layer(s): `l4_frontend`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `89285c6` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-31` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "Starting the week of 2024-07-16, Indonesia's Kominfo, coordinating with Bappebti,
> blocked the Indonesian-facing social-media (Instagram) accounts of unlicensed
> foreign crypto exchanges Binance, Kucoin, Bybit and Bitget. The l4_frontend layer
> carries the load-bearing plausible-attribution observation at class level. Distinct
> from the 2023 domain-block event."

## 1. Trigger

- **Type**: `nation_state_block`
- **Actor**: `ID_KOMINFO_BAPPEBTI`
- **Timestamp**: `2024-07-16 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`supporting_journalism`**
  - URL: <https://web.archive.org/web/20240824083712/https://bisnis.tempo.co/read/1893370/kominfo-blokir-akun-medsos-binance-dan-kucoin-ini-penjelasan-bappebti-hingga-tokocrypto>
  - Wayback: <https://web.archive.org/web/20240824083712/https://bisnis.tempo.co/read/1893370/kominfo-blokir-akun-medsos-binance-dan-kucoin-ini-penjelasan-bappebti-hingga-tokocrypto>
  - body_hash: `sha256:c2ff1ea82fa3d2d1b54029f1146d986fe21d3897474058d260f1ed57602efd1a`
  - body_path: `sources/http_captures/indonesia-kominfo-exchange-social-account-block-2024-07/primary/web.archive.org__web-20240824083712-https-bisnis.tempo.co-read-1893370-kominfo-blokir-akun-medsos-binance-dan-kucoin-ini-penjelasan-bappebti-hingga-tokocrypto__e32ab4134f.html`
  > Tempo (Bisnis), "Kominfo Blokir Akun Medsos Binance dan Kucoin, Ini
> Penjelasan Bappebti hingga Tokocrypto." Captured body confirms the
> Ministry of Communication and Informatics (Kominfo) blocked the social-media
> (medsos) accounts — including Instagram — of foreign cryptocurrency
> exchanges Binance, Kucoin, Bybit and Bitget that operate in Indonesia
> without Bappebti (CoFTRA) registration, and that Bappebti supports / coordinates
> the blocking of domains and social accounts of unlicensed entities.
> Blocking began the week of 2024-07-16.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: Foreign unlicensed crypto exchanges (Indonesia cohort)
- **Canonical domains**: `binance.com`, `kucoin.com`, `bybit.com`, `bitget.com`

> Foreign (offshore) cryptocurrency exchanges operating in Indonesia without
> Bappebti (CoFTRA) registration. Captured Tempo body names Binance, Kucoin,
> Bybit and Bitget as having social-media (Instagram) accounts blocked; the wave
> targeted the unlicensed-foreign-exchange class. MEXC is named in corroborating
> journalism (VOI/DFX) but is NOT asserted from the captured primary body.
> Class-level (codebook §7 subset).

## 3. Changed-layer observations (supports the scoped claim)

### l4_frontend · attribution: `plausible` · Δt = 0h

**Event label**: `foreign_exchange_social_media_accounts_blocked`

**Timestamp**: `2024-07-16 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`supporting_journalism`**
  - URL: <https://web.archive.org/web/20240824083712/https://bisnis.tempo.co/read/1893370/kominfo-blokir-akun-medsos-binance-dan-kucoin-ini-penjelasan-bappebti-hingga-tokocrypto>
  - Wayback: <https://web.archive.org/web/20240824083712/https://bisnis.tempo.co/read/1893370/kominfo-blokir-akun-medsos-binance-dan-kucoin-ini-penjelasan-bappebti-hingga-tokocrypto>
  - body_hash: `sha256:c2ff1ea82fa3d2d1b54029f1146d986fe21d3897474058d260f1ed57602efd1a`
  - body_path: `sources/http_captures/indonesia-kominfo-exchange-social-account-block-2024-07/primary/web.archive.org__web-20240824083712-https-bisnis.tempo.co-read-1893370-kominfo-blokir-akun-medsos-binance-dan-kucoin-ini-penjelasan-bappebti-hingga-tokocrypto__e32ab4134f.html`
  > Tempo (Bisnis) captured body confirms Kominfo blocked the social-media
> (medsos/Instagram) accounts of Binance, Kucoin, Bybit and Bitget for
> operating without Bappebti registration, with Bappebti supporting the
> domain/social-account blocking of unlicensed entities.
> attribution=plausible (codebook §1.4/§8.4): the load-bearing captured prose
> is contemporaneous journalism rather than the Kominfo blocking order, and
> the target is class-level. A primary Kominfo/Bappebti order capture would
> be required to elevate to direct.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`indonesia-bappebti-illegal-exchange-block-2023`](./indonesia-bappebti-illegal-exchange-block-2023.md)
- [`malaysia-sc-binance-disable-2021`](./malaysia-sc-binance-disable-2021.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `89285c6`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

