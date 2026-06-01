# Evidence chain — `eu-20th-russia-sanctions-crypto-sectoral-ban-2026`

**Status**: `admitted` · **Stratum**: `S6_supranational` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-02` · **Source commit**: `038e378` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-31` · **Tool version**: `0.1.0` · **Generated**: `2026-06-02T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "The EU's 20th sanctions package (2026-04-23) imposed a total sectoral ban
> on crypto-asset providers and platforms established in Russia that allow
> the transfer and exchange of crypto assets, plus a transaction ban on the
> RUBx stablecoin and a cut of EU support for the digital rouble - the EU's
> first class-wide sectoral crypto provider ban; single-layer offramp_cex
> observed_change with attribution=direct."

## 1. Trigger

- **Type**: `non_us_sanctions`
- **Actor**: `EU_Council`
- **Timestamp**: `2026-04-23 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://www.consilium.europa.eu/en/press/press-releases/2026/04/23/russia-s-war-of-aggression-against-ukraine-20th-round-of-stern-eu-sanctions-hits-energy-military-industrial-complex-trade-and-financial-services-including-crypto/>
  - Wayback: <https://web.archive.org/web/20260428125431/https://www.consilium.europa.eu/en/press/press-releases/2026/04/23/russia-s-war-of-aggression-against-ukraine-20th-round-of-stern-eu-sanctions-hits-energy-military-industrial-complex-trade-and-financial-services-including-crypto/>
  - body_hash: `sha256:dde0761ac107026002e4d2785237be0ae0fbfa45a06401a4b41c134e696e09e7`
  - body_path: `sources/http_captures/eu-20th-russia-sanctions-crypto-sectoral-ban-2026/primary/web.archive.org__web-20260429000000-https-www.consilium.europa.eu-en-press-press-releases-2026-04-23-russia-s-war-of-aggression-against-ukraine-20th-round-of-stern-eu-s__d537f28bcf.html`
  > Council of the EU, 20th sanctions package against Russia (adopted
> 2026-04-23). The captured press release states verbatim: "the EU is
> introducing a total sectoral ban on providers and platforms
> established in Russia that allow the transfer and exchange of crypto
> assets. The EU is also banning transactions in another crypto
> currency (RUBx) and all EU support for the development of the digital
> rouble." It also designates "a Kyrgyz entity which operates a
> platform where significant amounts of the government-backed stablecoin
> A7A5 are traded." This is the EU's first categorical sectoral
> (class-wide) ban on Russia-established crypto-asset providers and
> platforms, plus a transaction ban on the RUBx stablecoin and a cut of
> EU support for the digital-rouble CBDC. Wayback memento
> 20260428125431 pinned.
- **`supporting_journalism`**
  - URL: <https://www.coindesk.com/policy/2026/04/27/eu-s-largest-measures-against-russia-yet-include-escalation-of-crypto-sanctions-evasion>
  - Wayback: <https://web.archive.org/web/20260427194653/https://www.coindesk.com/policy/2026/04/27/eu-s-largest-measures-against-russia-yet-include-escalation-of-crypto-sanctions-evasion>
  - body_hash: `sha256:e500e7176dd644a35d65c3bb48c3c0cfdb646520e3b2d1ce2a2be8cb2bb62992`
  - body_path: `sources/http_captures/eu-20th-russia-sanctions-crypto-sectoral-ban-2026/primary/web.archive.org__web-20260428000000-https-www.coindesk.com-policy-2026-04-27-eu-s-largest-measures-against-russia-yet-include-escalation-of-crypto-sanctions-evasion__07ea43a18f.html`
  > CoinDesk 2026-04-27 corroborating the 20th-package crypto measures,
> quoting the EU's April 23 statement on the "total sectoral ban on
> providers and platforms established in Russia that allow the transfer
> and exchange of crypto assets" and noting the bloc "also banned
> Russia's central bank digital currency (CBDC), the ruble-pegged RUBx
> stablecoin" and designated the Kyrgyz exchange TengriCoin.
> Independent corroborating anchor.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: EU 20th-package sectoral ban on Russia-established crypto providers/platforms

> All crypto-asset providers and platforms established in Russia that allow
> the transfer and exchange of crypto assets (a class-wide / sectoral ban),
> plus a transaction ban on the RUBx stablecoin, a cut of EU support for the
> digital-rouble CBDC, and designation of a Kyrgyz entity operating an
> A7A5-trading platform. subset because the sectoral ban targets the
> Russia-established provider/platform CLASS by criteria rather than an
> exhaustively enumerated provider/address list in this record.

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `direct` · Δt = 0h

**Event label**: `eu_20th_package_total_sectoral_ban_on_russia_crypto_providers_platforms`

**Timestamp**: `2026-04-23 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_legal`**
  - URL: <https://www.consilium.europa.eu/en/press/press-releases/2026/04/23/russia-s-war-of-aggression-against-ukraine-20th-round-of-stern-eu-sanctions-hits-energy-military-industrial-complex-trade-and-financial-services-including-crypto/>
  - Wayback: <https://web.archive.org/web/20260428125431/https://www.consilium.europa.eu/en/press/press-releases/2026/04/23/russia-s-war-of-aggression-against-ukraine-20th-round-of-stern-eu-sanctions-hits-energy-military-industrial-complex-trade-and-financial-services-including-crypto/>
  - body_hash: `sha256:dde0761ac107026002e4d2785237be0ae0fbfa45a06401a4b41c134e696e09e7`
  - body_path: `sources/http_captures/eu-20th-russia-sanctions-crypto-sectoral-ban-2026/primary/web.archive.org__web-20260429000000-https-www.consilium.europa.eu-en-press-press-releases-2026-04-23-russia-s-war-of-aggression-against-ukraine-20th-round-of-stern-eu-s__d537f28bcf.html`
  > EU 20th package (2026-04-23): "the EU is introducing a total
> sectoral ban on providers and platforms established in Russia that
> allow the transfer and exchange of crypto assets. The EU is also
> banning transactions in another crypto currency (RUBx) and all EU
> support for the development of the digital rouble." attribution=
> direct: the EU legal instrument directly imposes a class-wide ban on
> Russia-established crypto providers/platforms and names the
> prohibited RUBx stablecoin. Verbatim language grep-confirmed in the
> captured body (body_hash-pinned).
- **`supporting_journalism`**
  - URL: <https://www.coindesk.com/policy/2026/04/27/eu-s-largest-measures-against-russia-yet-include-escalation-of-crypto-sanctions-evasion>
  - Wayback: <https://web.archive.org/web/20260427194653/https://www.coindesk.com/policy/2026/04/27/eu-s-largest-measures-against-russia-yet-include-escalation-of-crypto-sanctions-evasion>
  - body_hash: `sha256:e500e7176dd644a35d65c3bb48c3c0cfdb646520e3b2d1ce2a2be8cb2bb62992`
  - body_path: `sources/http_captures/eu-20th-russia-sanctions-crypto-sectoral-ban-2026/primary/web.archive.org__web-20260428000000-https-www.coindesk.com-policy-2026-04-27-eu-s-largest-measures-against-russia-yet-include-escalation-of-crypto-sanctions-evasion__07ea43a18f.html`
  > CoinDesk corroboration quoting the EU's "total sectoral ban on
> providers and platforms established in Russia that allow the
> transfer and exchange of crypto assets" and the blocking of the
> digital ruble CBDC and RUBx stablecoin. Independent semi-primary
> anchor.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`eu-19th-russia-sanctions-a7a5-crypto-ban-2025`](./eu-19th-russia-sanctions-a7a5-crypto-ban-2025.md)
- [`eu-18th-russia-sanctions-casp-spfs-2025`](./eu-18th-russia-sanctions-casp-spfs-2025.md)
- [`eu-8th-package-russia-crypto-services-ban-2022-10`](./eu-8th-package-russia-crypto-services-ban-2022-10.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `038e378`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

