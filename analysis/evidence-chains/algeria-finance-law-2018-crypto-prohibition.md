# Evidence chain — `algeria-finance-law-2018-crypto-prohibition`

**Status**: `admitted` · **Stratum**: `S4_nation_state` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `34b152d` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-31` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T05:22:19Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "Algeria's Finance Law 2018 (Article 117), published 2017-12-28 in Journal Officiel No. 76,
> prohibited the purchase, sale, use and possession of virtual currency nationwide. Coded as
> a nation-state off-ramp prohibition at class level; primary source is the law text itself."

## 1. Trigger

- **Type**: `nation_state_block`
- **Actor**: `DZ_GOVT`
- **Timestamp**: `2017-12-28 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://www.joradp.dz/FTP/jo-francais/2017/F2017076.pdf>
  - Wayback: <https://web.archive.org/web/20190312173325id_/https://www.joradp.dz/FTP/jo-francais/2017/F2017076.pdf>
  - body_hash: `sha256:0e73a9f71de0d7514761b7667ac22d9ceeafb13b408fd4e98ec8072eb4bdb2a7`
  - body_path: `sources/http_captures/algeria-finance-law-2018-crypto-prohibition/primary/web.archive.org__web-20190312173325id_-https-www.joradp.dz-FTP-jo-francais-2017-F2017076.pdf__6c420ff786.bin`
  > Journal Officiel de la République Algérienne No. 76 (French edition), dated
> 2017-12-28, carrying Loi de finances pour 2018 (Loi n° 17-11 du 27 décembre 2017).
> Article 117 reads verbatim: "L'achat, la vente, l'utilisation et la détention de la
> monnaie dite virtuelle est interdite. La monnaie virtuelle est celle utilisée par
> les internautes à travers le web. ... Toute infraction à cette disposition est punie
> conformément aux lois et règlements en vigueur." (Purchase, sale, use and holding of
> so-called virtual currency is prohibited.) This is the primary legal instrument — the
> law itself. Verified by full-text extraction of the captured PDF.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: Algerian crypto users / exchanges / merchants (class)

> Algerian crypto users / exchanges / merchants as a class. Article 117 prohibits the
> purchase, sale, use and possession of virtual currency by any person within Algeria;
> no specific platform or address is enumerated in the law. Coded subset at entity-class
> level. (Prohibition later hardened by Law No. 25-10 in July 2025 — a separate, out-of-
> scope-of-this-event later action.)

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `direct` · Δt = 0h

**Event label**: `virtual_currency_purchase_sale_use_possession_prohibited_by_statute`

**Timestamp**: `2017-12-28 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_legal`**
  - URL: <https://www.joradp.dz/FTP/jo-francais/2017/F2017076.pdf>
  - Wayback: <https://web.archive.org/web/20190312173325id_/https://www.joradp.dz/FTP/jo-francais/2017/F2017076.pdf>
  - body_hash: `sha256:0e73a9f71de0d7514761b7667ac22d9ceeafb13b408fd4e98ec8072eb4bdb2a7`
  - body_path: `sources/http_captures/algeria-finance-law-2018-crypto-prohibition/primary/web.archive.org__web-20190312173325id_-https-www.joradp.dz-FTP-jo-francais-2017-F2017076.pdf__6c420ff786.bin`
  > attribution=direct: the named actor (Algerian state, via Loi de finances 2018)
> publicly references the prohibition in the law text itself, and the instrument
> names the target class (all holders/users of virtual currency in Algeria). The
> law IS the censorship action. Per codebook §1 the actor's own instrument citing
> the restriction satisfies direct attribution.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `34b152d`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

