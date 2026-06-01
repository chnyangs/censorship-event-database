# Evidence chain — `eu-14th-russia-sanctions-spfs-2024`

**Status**: `admitted` · **Stratum**: `S6_supranational` · **Shape**: `null_event` (0 changed layer(s): none) · **Tier**: `null_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `34b152d` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-21` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T05:22:19Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "Council Regulation (EU) 2024/1745, adopted on 2024-06-24
> as the EU's 14th Russia-sanctions package, introduced the
> first explicit EU prohibition on connecting to Russia's
> SPFS financial-messaging network and extended the crypto-
> asset provisions framework via new Article 5ad (Annex XLV
> class for non-EU CASPs facilitating Russian defence-
> industrial procurement). Coded as null_event / null_case
> at the corpus's resolution: the regulation is framework-
> level with Annex XLV listings populated by subsequent
> implementing decisions; no per-event observed_change
> cascade is directly attributable to the 2024-06-24
> adoption date."

## 1. Trigger

- **Type**: `non_us_sanctions`
- **Actor**: `EU_COUNCIL`
- **Timestamp**: `2024-06-24 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://eur-lex.europa.eu/eli/reg/2024/1745/oj>
  - Wayback: <https://web.archive.org/web/20240624181905/https://eur-lex.europa.eu/eli/reg/2024/1745/oj>
  - body_hash: `sha256:dd8eed371b6cba0a6193afb1b8b616ccab9855c4f4032679bbc4ddb401f49328`
  - body_path: `sources/http_captures/eu-14th-russia-sanctions-spfs-2024/primary/web.archive.org__web-20240624181905-https-eur-lex.europa.eu-eli-reg-2024-1745-oj__58e36ac7f5.html`
  > Council Regulation (EU) 2024/1745 of 24 June 2024
> amending Regulation (EU) No 833/2014 concerning
> restrictive measures in view of Russia's actions
> destabilising the situation in Ukraine. Fourteenth EU
> Russia-sanctions package. Two crypto-relevant
> innovations: (i) explicit prohibition on EU entities
> operating outside of Russia from connecting to the
> Russian Central Bank's System for Transfer of Financial
> Messages (SPFS, Russia's SWIFT alternative) or
> equivalent specialised financial messaging services,
> and (ii) new Article 5ad extending the crypto-asset
> provisions framework by banning EU persons from
> transacting with non-EU credit/financial institutions
> and crypto-asset service providers that facilitate
> Russia's defence-industrial base procurement of dual-
> use items (Annex XLV listing). Regulation entered into
> force 2024-06-25 (day after Official Journal
> publication).
- **`primary_legal`**
  - URL: <https://www.consilium.europa.eu/en/press/press-releases/2024/06/24/russia-s-war-of-aggression-against-ukraine-comprehensive-eu-s-14th-package-of-sanctions-cracks-down-on-circumvention-and-adopts-energy-measures/>
  - Wayback: <https://web.archive.org/web/20240624072140/https://www.consilium.europa.eu/en/press/press-releases/2024/06/24/russia-s-war-of-aggression-against-ukraine-comprehensive-eu-s-14th-package-of-sanctions-cracks-down-on-circumvention-and-adopts-energy-measures/>
  - body_hash: `sha256:e4ef800529e7c8149c0b2faea33569544bb699cb47d0398a824849c0f42e2314`
  - body_path: `sources/http_captures/eu-14th-russia-sanctions-spfs-2024/primary/web.archive.org__web-20240624072140-https-www.consilium.europa.eu-en-press-press-releases-2024-06-24-russia-s-war-of-aggression-against-ukraine-comprehensive-eu-s-14th__9fe377a46e.html`
  > Council of the EU press release (2024-06-24)
> accompanying the 14th package adoption. Enumerates the
> SPFS prohibition (EU entities outside Russia forbidden
> from connecting to SPFS or equivalents), Article 5ad
> crypto-asset-provider transaction ban with Annex XLV
> listings, and the anti-circumvention thrust of the
> package. Wayback memento 20240624072140 captured
> 2026-05-21.
- **`supporting_journalism`**
  - URL: <https://enlargement.ec.europa.eu/news/eu-adopts-14th-package-sanctions-against-russia-its-continued-illegal-war-against-ukraine-2024-06-24_en>
  - Wayback: <https://web.archive.org/web/2024/https://enlargement.ec.europa.eu/news/eu-adopts-14th-package-sanctions-against-russia-its-continued-illegal-war-against-ukraine-2024-06-24_en>
  > European Commission DG NEAR news summary of the 14th
> package adoption, confirming the SPFS prohibition and
> crypto-asset-provider extension. Retained as
> contextual_unarchived; primary anchoring lives on the
> EUR-Lex + Council press release citations above.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: SPFS financial-messaging network + non-EU CASPs facilitating Russian defence procurement (Annex XLV class)

> Class-level EU sanctions instrument with two distinct
> target sub-classes: (i) the Russian Central Bank's SPFS
> financial-messaging network and any equivalent
> specialised messaging services, with EU entities operating
> outside Russia as the prohibited connecting party; and
> (ii) non-EU credit/financial institutions and crypto-
> asset service providers facilitating Russia's defence-
> industrial procurement, enumerated in Annex XLV (Article
> 5ad). Per §7 codebook, class-level regulatory targets are
> encoded as enumeration=subset with the class-level
> rationale documented here. Specific Annex XLV listings
> populate over time via Council implementing decisions;
> this event records the framework-level prohibition, not
> a per-listing enumeration.

## 3. Changed-layer observations (supports the scoped claim)

*No observed_change entries. This is a `null_event`; see §4 for observed_no_change evidence supporting the null claim.*

## 4. No-change observations (where applicable)

### offramp_cex — `eu_14th_package_spfs_and_article_5ad_framework_adoption_2024`

**Window**: `2024-06-24 00:00:00+00:00` → `2024-12-31 23:59:59+00:00`

**Sources**:

- **`primary_legal`**
  - URL: <https://eur-lex.europa.eu/eli/reg/2024/1745/oj>
  - Wayback: <https://web.archive.org/web/20240624181905/https://eur-lex.europa.eu/eli/reg/2024/1745/oj>
  - body_hash: `sha256:dd8eed371b6cba0a6193afb1b8b616ccab9855c4f4032679bbc4ddb401f49328`
  - body_path: `sources/http_captures/eu-14th-russia-sanctions-spfs-2024/primary/web.archive.org__web-20240624181905-https-eur-lex.europa.eu-eli-reg-2024-1745-oj__58e36ac7f5.html`
  > Council Regulation (EU) 2024/1745 (2024-06-24) is a
> framework-level extension of the Russia sanctions
> architecture. SPFS prohibition and Article 5ad
> crypto-asset-provider transaction ban operate
> class-level via Annex XLV listings populated by
> subsequent Council implementing decisions. No per-
> event observed_change cascade at the offramp_cex
> layer is directly attributable to the 2024-06-24
> adoption date at the corpus's resolution.
> observed_no_change / attribution=none per §1.1
> codebook. Wayback memento 20240624181905 captured
> 2026-05-21.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`eu-12th-russia-sanctions-2023`](./eu-12th-russia-sanctions-2023.md)
- [`eu-russia-crypto-wallet-cap-2022`](./eu-russia-crypto-wallet-cap-2022.md)
- [`eu-russia-full-crypto-wallet-ban-2022`](./eu-russia-full-crypto-wallet-ban-2022.md)
- [`eu-15th-russia-sanctions-2024`](./eu-15th-russia-sanctions-2024.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `34b152d`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

