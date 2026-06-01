# Evidence chain — `singapore-mas-retail-crypto-restriction-2022`

**Status**: `admitted` · **Stratum**: `S4_nation_state` · **Shape**: `comparison` (2 changed layer(s): `l4_frontend`, `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `f70cc98` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-21` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T00:48:55Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "MAS issued guidelines on 2022-01-17 prohibiting Digital Payment
> Token (DPT) service providers from marketing DPT services to the
> Singapore general public (public-area advertising, social media,
> broadcast / print media, third-party influencers, physical DPT
> ATMs), and followed with a 2022-07-06 consultation paper
> proposing retail-investor suitability assessment, leverage /
> credit restrictions, and enhanced KYC + risk-disclosure
> obligations. Load-bearing observational axes are L4 frontend
> (cohort-wide DPT public-marketing takedown, direct attribution)
> and offramp_cex (SG retail DPT onboarding friction, plausible
> attribution)."

## 1. Trigger

- **Type**: `regulatory_enforcement`
- **Actor**: `SG_MAS`
- **Timestamp**: `2022-01-17 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://www.mas.gov.sg/news/media-releases/2022/mas-issues-guidelines-to-discourage-cryptocurrency-trading-by-general-public>
  - Wayback: <https://web.archive.org/web/20220117093725/https://www.mas.gov.sg/news/media-releases/2022/mas-issues-guidelines-to-discourage-cryptocurrency-trading-by-general-public>
  - body_hash: `sha256:30120aa224be1cfab16a625973a3a9d0faa2ee818f3281264f7207f208fa05fa`
  - body_path: `sources/http_captures/singapore-mas-retail-crypto-restriction-2022/primary/web.archive.org__web-20220117093725-https-www.mas.gov.sg-news-media-releases-2022-mas-issues-guidelines-to-discourage-cryptocurrency-trading-by-general-public__e920350241.html`
  > Monetary Authority of Singapore (MAS) media release dated
> 2022-01-17 announcing guidelines that Digital Payment Token
> (DPT) service providers should not promote DPT services to the
> general public in Singapore. Restrictions include: no
> advertising on public transport / venues, public websites,
> social media platforms, broadcast and print media; no
> third-party promotion (e.g., social media influencers); no
> physical DPT ATMs in public areas. Marketing limited to a
> provider's own corporate website, mobile applications, and
> official social media accounts. Guidelines took effect
> immediately on issuance. Follow-on 2022-07-06 MAS consultation
> paper subsequently proposed binding measures including
> retail-customer suitability tests, restrictions on retail
> access to leverage and credit for DPT trading, and enhanced
> risk-disclosure / KYC obligations, culminating in MAS final
> rules published from 2022-10 onwards (effective in phases
> through 2023-2024). DRYRUN: pinned Wayback / body-hash
> captures of the 2022-01-17 MAS media release, the 2022-07-06
> consultation paper, and the 2022-10 final response paper
> deferred to a non-DRYRUN release. Marked
> evidence_use=contextual_unarchived to flag the unarchived
> state explicitly.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: SG DPT service providers (class)

> The MAS guidelines apply class-wide to all Digital Payment Token
> (DPT) service providers offering DPT services to Singapore
> retail customers. Subset enumeration captures the regulated
> cohort: PSA-licensed DPT providers and unlicensed offshore DPT
> providers soliciting Singapore retail users. Class-level
> rationale documented here rather than via a forbidden
> enumeration=class_level value (per codebook §7). Named cohort
> members observable in the public record include Binance.com,
> Bybit, Crypto.com, Coinhako, Independent Reserve, and DBS
> Digital Exchange, among others; only their compliance-driven
> marketing and onboarding posture is in scope.

## 3. Changed-layer observations (supports the scoped claim)

### l4_frontend · attribution: `direct` · Δt = 0h

**Event label**: `sg_dpt_public_marketing_takedown`

**Timestamp**: `2022-01-17 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_legal`**
  - URL: <https://www.mas.gov.sg/news/media-releases/2022/mas-issues-guidelines-to-discourage-cryptocurrency-trading-by-general-public>
  - Wayback: <https://web.archive.org/web/20220117093725/https://www.mas.gov.sg/news/media-releases/2022/mas-issues-guidelines-to-discourage-cryptocurrency-trading-by-general-public>
  - body_hash: `sha256:30120aa224be1cfab16a625973a3a9d0faa2ee818f3281264f7207f208fa05fa`
  - body_path: `sources/http_captures/singapore-mas-retail-crypto-restriction-2022/primary/web.archive.org__web-20220117093725-https-www.mas.gov.sg-news-media-releases-2022-mas-issues-guidelines-to-discourage-cryptocurrency-trading-by-general-public__e920350241.html`
  > MAS 2022-01-17 guidelines forbid DPT service providers from
> promoting DPT services to the Singapore general public via
> public-area advertising, social media, broadcast and print
> media, third-party influencers, and physical DPT ATMs.
> Marketing restricted to providers' own corporate websites,
> mobile applications, and official social media accounts.
> Guidelines took effect immediately; supporting journalism
> (Morgan Lewis, Lexology, GlobalComplianceNews) documents
> rapid cohort-wide compliance posture changes (e.g.,
> Daenerys & Co / Crypto.com ATM removal). Attribution=direct
> per codebook §1.4: the MAS guideline explicitly cites the
> DPT-marketing scope, and the cohort response was within
> the publicly-knowable compliance window. DRYRUN: pinned
> Wayback captures of representative DPT-provider SG-geo
> landing pages and physical-ATM removal photographs
> deferred.
- **`semi_primary_wayback`**
  - URL: <https://www.morganlewis.com/pubs/2022/01/new-guidelines-discourage-cryptocurrency-trading-by-general-public-in-singapore>
  - Wayback: <https://web.archive.org/web/20220119220822/https://www.morganlewis.com/pubs/2022/01/new-guidelines-discourage-cryptocurrency-trading-by-general-public-in-singapore>
  - body_hash: `sha256:793116a281346bd1365b04f7838bf9b5a8e59788f007d03bf211c2baadd73b62`
  - body_path: `sources/http_captures/singapore-mas-retail-crypto-restriction-2022/primary/web.archive.org__web-20220119220822-https-www.morganlewis.com-pubs-2022-01-new-guidelines-discourage-cryptocurrency-trading-by-general-public-in-singapore__233a5bb278.html`
  > Morgan Lewis 2022-01 client alert summarising the MAS
> guidelines and the immediate-effect compliance expectation.
> DRYRUN: archived snapshot pending.

### offramp_cex · attribution: `plausible` · Δt = 4080h

**Event label**: `sg_dpt_retail_onboarding_friction_increase`

**Timestamp**: `2022-07-06 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_legal`**
  - URL: <https://www.mas.gov.sg/news/media-releases/2022/mas-proposes-measures-to-reduce-risks-to-consumers-from-cryptocurrency-trading-and-enhance-standards-of-stablecoin-related-activities>
  - Wayback: <https://web.archive.org/web/2022*/mas.gov.sg/news/media-releases/2022/mas-proposes-measures-to-reduce-risks-to-consumers-from-cryptocurrency-trading-and-enhance-standards-of-stablecoin-related-activities>
  > MAS 2022-07-06 consultation paper proposing retail-investor
> access measures including customer-suitability assessment,
> restrictions on use of leverage / credit for DPT trading,
> and enhanced risk-disclosure / KYC obligations at the
> onboarding gate. Attribution=plausible: the consultation
> paper is the proximate regulatory instrument and is
> publicly cited by SG DPT providers in their onboarding-
> flow updates, but individual provider implementation dates
> and per-provider direct citations are not yet pinned per-
> event; provider-level compliance was inferential from the
> MAS-program scope. DRYRUN: pinned Wayback capture of the
> MAS consultation paper and per-provider onboarding-flow
> anchors deferred.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`singapore-mas-binance-services-2021`](./singapore-mas-binance-services-2021.md)
- [`bybit-singapore-exit-2022`](./bybit-singapore-exit-2022.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `f70cc98`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

