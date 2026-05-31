# Evidence chain — `argentina-bcra-banks-crypto-services-ban-2022-05`

**Status**: `admitted` · **Stratum**: `S4_nation_state` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `dbf5e31` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-31` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> BCRA Communication "A" 7506 of 2022-05-05 prohibited all Argentine financial institutions
> from carrying out or facilitating client transactions in digital/crypto assets not regulated
> by a national authority and authorized by the BCRA — a de facto ban that severed the bank
> channel between Argentine users and crypto. The offramp_cex layer carries the load-bearing
> direct-attribution observation; the prohibition remained in force well beyond 2022.

## 1. Trigger

- **Type**: `nation_state_block`
- **Actor**: `AR_BCRA`
- **Timestamp**: `2022-05-05 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`supporting_journalism`**
  - URL: <https://web.archive.org/web/20220510051130/https://www.coindesk.com/policy/2022/05/05/argentinas-central-bank-bans-lenders-from-offering-crypto-services/>
  - Wayback: <https://web.archive.org/web/20220510051130/https://www.coindesk.com/policy/2022/05/05/argentinas-central-bank-bans-lenders-from-offering-crypto-services/>
  - body_hash: `sha256:4ff33339e508064b7a6a279bc3219e43b8f1585904fcf15d425910526b6e0db9`
  - body_path: `sources/http_captures/argentina-bcra-banks-crypto-services-ban-2022-05/primary/web.archive.org__web-20220510051130-https-www.coindesk.com-policy-2022-05-05-argentinas-central-bank-bans-lenders-from-offering-crypto-services__700217215a.html`
  > CoinDesk report (URL-dated 2022-05-05, "Thursday afternoon" = 2022-05-05) titled
> "Argentina's Central Bank Bans Lenders From Offering Crypto Services". Captured
> body verifies the operative facts: "The Central Bank of the Argentine Republic
> (BCRA) announced Thursday afternoon that it has barred banks in the country from
> facilitating for clients the use of crypto assets"; "banks are prohibited from
> offering services for any digital assets not regulated by the central bank, and
> since there currently are no digital assets thus regulated, the move amounts to a
> de facto ban"; and notes the move "comes just days after Banco Galicia ... added
> the option to buy and sell cryptocurrencies on its platform." The underlying
> instrument is BCRA Communication "A" 7506 (2022-05-05). The official BCRA news
> page (https://www.bcra.gob.ar/en/news/the-bcra-discourages-the-offer-of-crypto-
> assets-through-the-financial-system/) carries the same operative language
> ("Financial institutions may not carry out transactions or allow their customers
> to make transactions with digital assets ... not regulated by a national authority
> and authorized by the BCRA") but is not Wayback-archivable; the archived CoinDesk
> report is the replayable anchor.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: Argentine financial institutions (BCRA Communication A 7506 class)

> Canonical target is BCRA Communication "A" 7506, addressed as a class-level
> prohibition to all financial institutions in Argentina, barring them from carrying out
> or facilitating client transactions in digital/crypto assets not regulated by a
> national authority and authorized by the BCRA (a de facto ban, since no such assets
> are BCRA-authorized). The communication does not name specific banks, addresses, or
> domains; enumeration=subset because the prohibition addresses the regulated financial-
> institution class without a fixed enumerated roster, matching the China 2013 /
> Nigeria 2021 banking-rail-severance convention. (Banco Galicia, Brubank and Ualá had
> just launched bank crypto trading, prompting the action, but they are contextual
> rather than named enumerated targets in the communication.)

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `plausible` · Δt = 0h

**Event label**: `bank_crypto_services_prohibited_class_wide_de_facto_ban`

**Timestamp**: `2022-05-05 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_government`**
  - URL: <https://www.bcra.gob.ar/Pdfs/comytexord/A7506.pdf>
  - Wayback: <https://web.archive.org/web/20260531041114/https://www.bcra.gob.ar/archivos/Pdfs/comytexord/A7506.pdf>
  - body_hash: `sha256:09fe0a3415d8e8c574e42aafb454d69758b236187548649d457c9d6d0552bbbe`
  - body_path: `sources/http_captures/argentina-bcra-banks-crypto-services-ban-2022-05/primary/www.bcra.gob.ar__Pdfs-comytexord-A7506.pdf__6a3303756d.bin`
  > BCRA Comunicacion "A" 7506 (2022-05-05) — official primary source: financial
> institutions may not carry out or facilitate clients' crypto-asset operations
> not authorized by the BCRA. Captured 2026-05-31 (PDF, body_hash-pinned;
> Wayback-archived). Extracted text confirms "comunicacion a 7506 05/05/2022 a
> las entidades financieras", criptoactivos, clientes.
- **`supporting_journalism`**
  - URL: <https://web.archive.org/web/20220510051130/https://www.coindesk.com/policy/2022/05/05/argentinas-central-bank-bans-lenders-from-offering-crypto-services/>
  - Wayback: <https://web.archive.org/web/20220510051130/https://www.coindesk.com/policy/2022/05/05/argentinas-central-bank-bans-lenders-from-offering-crypto-services/>
  - body_hash: `sha256:4ff33339e508064b7a6a279bc3219e43b8f1585904fcf15d425910526b6e0db9`
  - body_path: `sources/http_captures/argentina-bcra-banks-crypto-services-ban-2022-05/primary/web.archive.org__web-20220510051130-https-www.coindesk.com-policy-2022-05-05-argentinas-central-bank-bans-lenders-from-offering-crypto-services__700217215a.html`
  > CoinDesk 2022-05-05 report: the BCRA "barred banks in the country from
> facilitating for clients the use of crypto assets"; "banks are prohibited from
> offering services for any digital assets not regulated by the central bank ...
> the move amounts to a de facto ban." attribution=direct because the BCRA
> statement quoted (Communication "A" 7506, the regulatory mandate) names the
> financial-institution prohibition. The official BCRA primary page is not
> Wayback-archivable; this archived report is the replayable anchor.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`argentina-uif-resolution-300-2014`](./argentina-uif-resolution-300-2014.md)
- [`argentina-cnv-psav-registration-2024`](./argentina-cnv-psav-registration-2024.md)
- [`nigeria-cbn-crypto-ban-2021`](./nigeria-cbn-crypto-ban-2021.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `dbf5e31`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

