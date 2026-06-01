# Evidence chain — `ecuador-national-assembly-bitcoin-ban-2014-07`

**Status**: `admitted` · **Stratum**: `S4_nation_state` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-02` · **Source commit**: `3a48c00` · **Schema**: `0.2.0` · **Event last_verified**: `2026-06-01` · **Tool version**: `0.1.0` · **Generated**: `2026-06-02T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "Ecuador's National Assembly (2014-07-23) amended the monetary/financial code to prohibit
> the circulation of decentralized digital currencies (Bitcoin) in Ecuador while creating a
> state-run electronic money system; impact captured at class level at the payment-rail
> (offramp_cex) layer."

## 1. Trigger

- **Type**: `nation_state_block`
- **Actor**: `EC_NATIONAL_ASSEMBLY`
- **Timestamp**: `2014-07-23 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://www.cosede.gob.ec/wp-content/uploads/2018/08/COMF.pdf>
  - Wayback: <https://web.archive.org/web/20260531042728/https://www.cosede.gob.ec/wp-content/uploads/2018/08/COMF.pdf>
  - body_hash: `sha256:f8ca23dec7c8d481e9bc5e5ac284e465ae7c9b6908474d76d319fc988f188478`
  - body_path: `sources/http_captures/ecuador-national-assembly-bitcoin-ban-2014-07/primary/www.cosede.gob.ec__wp-content-uploads-2018-08-COMF.pdf__ce39262a7f.bin`
  > Codigo Organico Monetario y Financiero (Registro Oficial 2014-09-12)
> primary legal text. Local PDF extraction verifies the Asamblea Nacional
> certification, the monetary/financial-code instrument, US-dollar legal-
> tender framing, and prohibition of monetary/payment circulation not
> authorized by the Junta de Politica y Regulacion Monetaria y Financiera.
> This primary_legal artifact anchors the legal instrument and class-level
> payment-rail restriction. The exact 2014-07-23 assembly-vote timestamp
> remains anchored by contemporaneous reporting; the legal text itself
> certifies first/second debate dates and later publication/objection dates.
- **`supporting_journalism`**
  - URL: <https://web.archive.org/web/20140725000000/https://www.coindesk.com/markets/2014/07/25/ecuador-bans-bitcoin-plans-own-digital-money>
  - Wayback: <https://web.archive.org/web/20211018105941/https://www.coindesk.com/markets/2014/07/25/ecuador-bans-bitcoin-plans-own-digital-money/>
  - body_hash: `sha256:f1b980f4d1e23822b5b771209bbb54688c388a1e109a22ea3edac51007556fbf`
  - body_path: `sources/http_captures/ecuador-national-assembly-bitcoin-ban-2014-07/primary/web.archive.org__web-20140725000000-https-www.coindesk.com-markets-2014-07-25-ecuador-bans-bitcoin-plans-own-digital-money__3ec3340cd2.html`
  > National Assembly of Ecuador approved amendments to the country's monetary and
> financial laws (91 votes in favor) that prohibit decentralized digital currencies
> (Bitcoin) while authorizing a state-run electronic money system (Dinero
> Electronico). Reported 2014-07-25 by CoinDesk; the assembly vote occurred
> 2014-07-23. The amended Codigo Organico Monetario y Financiero bars the
> circulation of non-sanctioned digital currencies through any channel.

## 2. Target

- **Kind**: `asset`
- **Enumeration**: `subset`
- **Actor name**: Bitcoin / decentralized digital currency users in Ecuador (class)

> Decentralized digital currencies (Bitcoin and equivalents) as an asset class
> barred from circulation in Ecuador by the amended monetary/financial code. No
> specific platform or address is named in the legislation; treated at class level.

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `plausible` · Δt = 0h

**Event label**: `decentralized_digital_currency_circulation_prohibited`

**Timestamp**: `2014-07-23 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_legal`**
  - URL: <https://www.cosede.gob.ec/wp-content/uploads/2018/08/COMF.pdf>
  - Wayback: <https://web.archive.org/web/20260531042728/https://www.cosede.gob.ec/wp-content/uploads/2018/08/COMF.pdf>
  - body_hash: `sha256:f8ca23dec7c8d481e9bc5e5ac284e465ae7c9b6908474d76d319fc988f188478`
  - body_path: `sources/http_captures/ecuador-national-assembly-bitcoin-ban-2014-07/primary/www.cosede.gob.ec__wp-content-uploads-2018-08-COMF.pdf__ce39262a7f.bin`
  > Codigo Organico Monetario y Financiero (Registro Oficial 2014-09-12) — the
> primary_legal basis: establishes the US dollar as sole legal tender (curso
> legal) and prohibits ("se prohibe") payment methods not authorized by the
> Junta de Politica Monetaria (medios de pago no autorizados). Captured 2026-05-31
> (156-page PDF, full text extracted+grepped: se prohibe / no autorizado / medios
> de pago / curso legal / dolar / junta de politica all present; Wayback-archived).
> attribution=plausible: the Code is the legal basis but does not name bitcoin/crypto
> explicitly — the prohibition of crypto as an unauthorized payment method is the
> documented BCE interpretation.
- **`supporting_journalism`**
  - URL: <https://web.archive.org/web/20140725000000/https://www.coindesk.com/markets/2014/07/25/ecuador-bans-bitcoin-plans-own-digital-money>
  - body_hash: `sha256:f1b980f4d1e23822b5b771209bbb54688c388a1e109a22ea3edac51007556fbf`
  - body_path: `sources/http_captures/ecuador-national-assembly-bitcoin-ban-2014-07/primary/web.archive.org__web-20140725000000-https-www.coindesk.com-markets-2014-07-25-ecuador-bans-bitcoin-plans-own-digital-money__3ec3340cd2.html`
  > attribution=plausible (codebook §1.1): the verifying source is journalism,
> not the primary legal instrument, and the prohibition is class-level (no
> named target). Conservative choice pending primary-text verification.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`bolivia-bcb-crypto-prohibition-2014`](./bolivia-bcb-crypto-prohibition-2014.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `3a48c00`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

