# Evidence chain — `eu-15th-russia-sanctions-2024`

**Status**: `admitted` · **Stratum**: `S6_supranational` · **Shape**: `null_event` (0 changed layer(s): none) · **Tier**: `null_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-02` · **Source commit**: `c3a88e8` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-21` · **Tool version**: `0.1.0` · **Generated**: `2026-06-02T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "EU Council Regulation 2024/3192 (15th Russia-sanctions package),
> adopted 2024-12-16, is a mostly-technical entity-listing / shadow-fleet
> package: 84 new individual / entity designations, 52 new third-country
> vessel listings, and 32 new military-industrial support company
> listings. It introduces NO new horizontal CASP-level or on-chain
> provisions beyond the 12th-package Article 5aa user-class prohibition
> and the 14th-package SPFS / crypto-services tightenings. null_event in
> this corpus: the crypto-relevant footprint is the absorption of 84
> designees into standing CASP screening, which is not separately
> replayable as observed_change at this snapshot."

## 1. Trigger

- **Type**: `non_us_sanctions`
- **Actor**: `EU_Council`
- **Timestamp**: `2024-12-16 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=OJ:L_202403192>
  - Wayback: <https://web.archive.org/web/20241216134134/https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=OJ:L_202403192>
  - body_hash: `sha256:59b79509b6e29303f336a454d223fb8e64ed8a2c8730fc9f844ff38336bd97d7`
  - body_path: `sources/http_captures/eu-15th-russia-sanctions-2024/primary/web.archive.org__web-20241216134134-https-eur-lex.europa.eu-legal-content-EN-TXT__ec54dd0124.html`
  > Council Regulation (EU) 2024/3192 of 16 December 2024 amending
> Regulation (EU) No 833/2014 concerning restrictive measures in view
> of Russia's actions destabilising the situation in Ukraine. The 15th
> EU Russia-sanctions package. Focus is on (1) Russia's "shadow fleet"
> of oil-transport vessels: 52 additional third-country-flagged
> vessels listed (bringing the cumulative total to 79); (2) 84 new
> individual / entity listings (54 natural persons + 30 entities),
> including the first fully-fledged sanctions on Chinese actors
> supplying drone and microelectronic components to Russia; and
> (3) 32 new companies added to the military-industrial support list
> (20 Russian, 7 Chinese/HK, 2 Serbian, 1 each Iranian, Indian, UAE).
> The package is described by the Council and outside counsel
> (Mayer Brown, White & Case, Curtis, Ashurst) as "mostly technical,"
> consolidating circumvention-focused tooling on top of the
> 14th-package SPFS and crypto-services prohibitions; it does NOT
> introduce material new on-chain or CASP-level provisions beyond
> the 14th package. Wayback memento 20241216134134 captured
> 2026-05-21 with replayable body_hash.
- **`primary_legal`**
  - URL: <https://www.consilium.europa.eu/en/press/press-releases/2024/12/16/russia-s-war-of-aggression-against-ukraine-eu-adopts-15th-package-of-restrictive-measures/>
  - Wayback: <https://web.archive.org/web/20241216111014/https://www.consilium.europa.eu/en/press/press-releases/2024/12/16/russia-s-war-of-aggression-against-ukraine-eu-adopts-15th-package-of-restrictive-measures>
  - body_hash: `sha256:ae277f96a189a4f5e219508d77bec3d5c6dbd2da55694644924bd6b7b41817d2`
  - body_path: `sources/http_captures/eu-15th-russia-sanctions-2024/primary/web.archive.org__web-20241216111014-https-www.consilium.europa.eu-en-press-press-releases-2024-12-16-russia-s-war-of-aggression-against-ukraine-eu-adopts-15th-package-o__c151574433.html`
  > Council of the EU press release of 2024-12-16 announcing adoption of
> the 15th package. Confirms shadow-fleet (52 vessels), individual
> / entity listings (54 persons + 30 entities), and military-
> industrial company list expansion (32 firms). Confirms scope is
> entity / vessel listing rather than new horizontal crypto-services
> prohibition.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: 15th-package designees (persons / entities / vessels / companies)

> 84 newly designated natural / legal persons (54 individuals + 30
> entities) plus 52 newly listed third-country shadow-fleet vessels and
> 32 newly listed military-industrial support companies (20 Russian,
> 7 Chinese/HK, 2 Serbian, 1 Iranian, 1 Indian, 1 UAE) under EU
> Regulation 833/2014 and 269/2014. Target class is fundamentally
> entity-level (persons, legal entities, vessels) — no on-chain
> wallet-address enumeration, no new horizontal CASP user-class
> prohibition (the user-class crypto prohibition is already in place
> from the 12th package via Article 5aa of Reg. 833/2014; the SPFS /
> crypto-services tightenings are in the 14th package). subset because
> the 84 + 52 + 32 entries are not exhaustively enumerated in this
> record at the natural-person level.

## 3. Changed-layer observations (supports the scoped claim)

*No observed_change entries. This is a `null_event`; see §4 for observed_no_change evidence supporting the null claim.*

## 4. No-change observations (where applicable)

### offramp_cex — `eu_15th_package_entity_listings_no_new_casp_provisions`

**Window**: `2024-12-16 00:00:00+00:00` → `2026-05-21 00:00:00+00:00`

**Sources**:

- **`primary_legal`**
  - URL: <https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=OJ:L_202403192>
  - Wayback: <https://web.archive.org/web/20241216134134/https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=OJ:L_202403192>
  - body_hash: `sha256:59b79509b6e29303f336a454d223fb8e64ed8a2c8730fc9f844ff38336bd97d7`
  - body_path: `sources/http_captures/eu-15th-russia-sanctions-2024/primary/web.archive.org__web-20241216134134-https-eur-lex.europa.eu-legal-content-EN-TXT__ec54dd0124.html`
  > Council Regulation (EU) 2024/3192 — the 15th EU Russia-sanctions
> package — adopted 2024-12-16. The package focuses on shadow-fleet
> vessel listings (52 new), individual / entity listings (84 new),
> and military-industrial support company listings (32 new). No
> new horizontal crypto-asset-service-provider provisions are
> introduced beyond those already enacted in the 12th package
> (Article 5aa CASP user-class prohibition, 2023-12-18) and 14th
> package (SPFS / further crypto-services tightening, 2024-06-24).
> observation_kind=observed_no_change with attribution=none
> because no separately-attributable artifact of CASP behavioral
> change at the 15th-package adoption date — package's crypto-
> relevant footprint is marginal (entity / vessel listings
> absorbed via standing CASP OFAC-/EU-listing screening). Wayback
> memento 20241216134134 captured 2026-05-21.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`eu-12th-russia-sanctions-2023`](./eu-12th-russia-sanctions-2023.md)
- [`eu-14th-russia-sanctions-spfs-2024`](./eu-14th-russia-sanctions-spfs-2024.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `c3a88e8`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

