# Evidence chain — `eu-8th-package-russia-crypto-services-ban-2022-10`

**Status**: `admitted` · **Stratum**: `S6_supranational` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-02` · **Source commit**: `a7b40fe` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-31` · **Tool version**: `0.1.0` · **Generated**: `2026-06-02T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "The EU's 8th sanctions package (2022-10-06) completely banned the
> provision of crypto-asset wallet/account/custody services to Russian
> persons (removing the prior EUR 10k cap), severing the EU crypto
> offramp/custody surface for the sanctioned class; single-layer
> offramp_cex observed_change with attribution=direct."

## 1. Trigger

- **Type**: `supranational_regulation`
- **Actor**: `eu_council`
- **Timestamp**: `2022-10-06 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://finance.ec.europa.eu/news/eu-agrees-eighth-package-sanctions-against-russia-2022-10-06_en>
  - Wayback: <https://web.archive.org/web/20250530212527/https://finance.ec.europa.eu/news/eu-agrees-eighth-package-sanctions-against-russia-2022-10-06_en>
  - body_hash: `sha256:25f907f04ba923199960626483b6dcb00b7c79ad39ff73ac2fe13947b6b19b17`
  - body_path: `sources/http_captures/eu-8th-package-russia-crypto-services-ban-2022-10/primary/web.archive.org__web-20221015000000-https-finance.ec.europa.eu-news-eu-agrees-eighth-package-sanctions-against-russia-2022-10-06_en__916ffa41ed.html`
  > European Commission / Council, 8th sanctions package against Russia
> (adopted 2022-10-06): a COMPLETE ban on the provision of crypto-asset
> wallet, account, or custody services to Russian persons and residents,
> removing the prior EUR 10,000 threshold (5th package, April 2022). The
> provision of these crypto-asset services is now entirely prohibited
> regardless of value. Wayback 20250530212527 pinned.
- **`semi_primary_wayback`**
  - URL: <https://www.coindesk.com/policy/2022/10/06/eus-russian-crypto-ban-confirmed-as-bloc-tightens-sanctions>
  - Wayback: <https://web.archive.org/web/20221007045409/https://www.coindesk.com/policy/2022/10/06/eus-russian-crypto-ban-confirmed-as-bloc-tightens-sanctions/>
  - body_hash: `sha256:4c49f5d6214ffd0c8bce614116e817c76a65a1b25d7dfacc7832abdc67ba588f`
  - body_path: `sources/http_captures/eu-8th-package-russia-crypto-services-ban-2022-10/primary/web.archive.org__web-20221008000000-https-www.coindesk.com-policy-2022-10-06-eus-russian-crypto-ban-confirmed-as-bloc-tightens-sanctions__6292511487.html`
  > CoinDesk 2022-10-06 confirming the EU 8th-package total crypto-services
> ban on Russian persons. Independent corroborating anchor.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `complete`
- **Actor name**: EU 8th-package crypto-services ban (Russian persons)

> All crypto-asset wallet / account / custody services provided to Russian
> persons and residents (the prohibited service-to-target-class). Complete
> enumeration of the prohibited service class; the ban applies to all EU
> crypto-asset service providers vis-a-vis Russian persons regardless of
> asset value (removing the prior EUR 10k threshold).

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `direct` · Δt = 0h

**Event label**: `eu_prohibits_all_crypto_services_to_russian_persons`

**Timestamp**: `2022-10-06 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_legal`**
  - URL: <https://finance.ec.europa.eu/news/eu-agrees-eighth-package-sanctions-against-russia-2022-10-06_en>
  - Wayback: <https://web.archive.org/web/20250530212527/https://finance.ec.europa.eu/news/eu-agrees-eighth-package-sanctions-against-russia-2022-10-06_en>
  - body_hash: `sha256:25f907f04ba923199960626483b6dcb00b7c79ad39ff73ac2fe13947b6b19b17`
  - body_path: `sources/http_captures/eu-8th-package-russia-crypto-services-ban-2022-10/primary/web.archive.org__web-20221015000000-https-finance.ec.europa.eu-news-eu-agrees-eighth-package-sanctions-against-russia-2022-10-06_en__916ffa41ed.html`
  > EU 8th-package: complete prohibition on crypto-asset wallet/account/
> custody services to Russian persons (removed the EUR 10k threshold).
> attribution=direct: the EU legal instrument directly and explicitly
> prohibits the offramp/custody service for the named target class.
- **`semi_primary_wayback`**
  - URL: <https://www.coindesk.com/policy/2022/10/06/eus-russian-crypto-ban-confirmed-as-bloc-tightens-sanctions>
  - Wayback: <https://web.archive.org/web/20221007045409/https://www.coindesk.com/policy/2022/10/06/eus-russian-crypto-ban-confirmed-as-bloc-tightens-sanctions/>
  - body_hash: `sha256:4c49f5d6214ffd0c8bce614116e817c76a65a1b25d7dfacc7832abdc67ba588f`
  - body_path: `sources/http_captures/eu-8th-package-russia-crypto-services-ban-2022-10/primary/web.archive.org__web-20221008000000-https-www.coindesk.com-policy-2022-10-06-eus-russian-crypto-ban-confirmed-as-bloc-tightens-sanctions__6292511487.html`
  > CoinDesk corroboration of the EU total crypto-services ban.
> Independent semi-primary anchor.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`mica-l2-esma-eba-rts-2024`](./mica-l2-esma-eba-rts-2024.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `a7b40fe`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

