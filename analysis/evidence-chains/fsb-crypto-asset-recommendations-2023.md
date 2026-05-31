# Evidence chain — `fsb-crypto-asset-recommendations-2023`

**Status**: `admitted` · **Stratum**: `S6_supranational` · **Shape**: `null_event` (0 changed layer(s): none) · **Tier**: `null_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `8e29b8d` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-21` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "The FSB's 2023-07-17 finalised global regulatory framework for
> crypto-asset activities (nine recommendations) and global
> stablecoin arrangements (ten recommendations) is a class-level
> supranational regulatory consensus by the G20 financial-stability
> authority. Coded as null_event / null_case at the corpus's
> resolution: no per-event observed_change cascade is directly
> attributable to the 2023-07-17 publication date; downstream
> FSB-member jurisdiction implementations are tracked as separate
> child events."

## 1. Trigger

- **Type**: `supranational_regulation`
- **Actor**: `FSB`
- **Timestamp**: `2023-07-17 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://www.fsb.org/2023/07/fsb-finalises-global-regulatory-framework-for-crypto-asset-activities/>
  - body_hash: `sha256:041a92923f92b2708c80628ef91371a8388b6882a3b62daa047646d51a6d5b47`
  - body_path: `sources/http_captures/fsb-crypto-asset-recommendations-2023/primary/www.fsb.org__2023-07-fsb-finalises-global-regulatory-framework-for-crypto-asset-activities__c2646966de.html`
  > FSB press release announcing finalisation of the global regulatory
> framework for crypto-asset activities, dated 2023-07-17. The
> framework consists of two distinct sets of high-level
> recommendations: (1) nine recommendations on the regulation,
> supervision and oversight of crypto-asset activities and markets,
> and (2) ten recommendations on the regulation, supervision and
> oversight of global stablecoin arrangements (GSCs). Built on the
> principle of "same activity, same risk, same regulation" and
> strengthened in three areas post-FTX: client-asset safeguarding,
> conflicts-of-interest, and cross-border cooperation.
- **`primary_legal`**
  - URL: <https://www.fsb.org/2023/07/high-level-recommendations-for-the-regulation-supervision-and-oversight-of-crypto-asset-activities-and-markets-final-report/>
  - Wayback: <https://web.archive.org/web/2023*/https://www.fsb.org/2023/07/high-level-recommendations-for-the-regulation-supervision-and-oversight-of-crypto-asset-activities-and-markets-final-report/>
  > FSB "High-level Recommendations for the Regulation, Supervision
> and Oversight of Crypto-asset Activities and Markets: Final
> Report" published 2023-07-17. Nine recommendations covering
> regulatory powers and tools, cross-border cooperation,
> governance, risk management, data reporting, disclosures,
> addressing financial-stability risks of interconnections, and
> comprehensive regulation of crypto-asset service providers with
> multiple functions.
- **`primary_legal`**
  - URL: <https://www.fsb.org/2023/07/high-level-recommendations-for-the-regulation-supervision-and-oversight-of-global-stablecoin-arrangements-final-report/>
  - Wayback: <https://web.archive.org/web/2023*/https://www.fsb.org/2023/07/high-level-recommendations-for-the-regulation-supervision-and-oversight-of-global-stablecoin-arrangements-final-report/>
  > FSB "High-level Recommendations for the Regulation, Supervision
> and Oversight of Global Stablecoin Arrangements: Final Report"
> published 2023-07-17. Ten recommendations for GSC arrangements,
> addressing financial-stability risks at both domestic and
> international levels.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: FSB-member-jurisdiction crypto-asset / stablecoin ecosystem

> Class-level supranational regulatory consensus targeting the global
> crypto-asset ecosystem: (1) crypto-asset service providers (CASPs),
> centralized exchanges, custodians, trading platforms, and providers
> with multiple functions; and (2) global stablecoin arrangements
> (GSCs) including issuers, governance bodies, and reserve managers
> (Tether, Circle, Paxos, and any cross-jurisdictionally significant
> stablecoin arrangement). Per §7 codebook, class-level regulatory
> consensus is encoded as enumeration=subset with the class-level
> rationale documented here. No address-level enumeration; binding
> force is via FSB-member jurisdiction implementation (G20 endorsement
> cycle, IMF-FSB joint synthesis paper, and IOSCO/BCBS/CPMI parallel
> standard-setting). Downstream affected entities span FSB-member
> jurisdictions' regulatory implementations.

## 3. Changed-layer observations (supports the scoped claim)

*No observed_change entries. This is a `null_event`; see §4 for observed_no_change evidence supporting the null claim.*

## 4. No-change observations (where applicable)

### offramp_cex — `fsb_2023_global_regulatory_framework_class_level_consensus`

**Window**: `2023-07-17 00:00:00+00:00` → `2024-12-31 23:59:59+00:00`

**Sources**:

- **`primary_legal`**
  - URL: <https://www.fsb.org/2023/07/fsb-finalises-global-regulatory-framework-for-crypto-asset-activities/>
  - body_hash: `sha256:041a92923f92b2708c80628ef91371a8388b6882a3b62daa047646d51a6d5b47`
  - body_path: `sources/http_captures/fsb-crypto-asset-recommendations-2023/primary/www.fsb.org__2023-07-fsb-finalises-global-regulatory-framework-for-crypto-asset-activities__c2646966de.html`
  > FSB 2023-07-17 final reports finalise the global regulatory
> framework for crypto-asset activities (9 recommendations) and
> global stablecoin arrangements (10 recommendations). No
> per-event observed_change cascade attributable to this
> trigger at the corpus's resolution — downstream effects
> manifest via FSB-member jurisdiction implementations (EU MiCA
> transitional, IOSCO crypto policy, national CASP rule
> updates), tracked as separate child events. Coverage_gap /
> attribution=none per §1.1 codebook (observed_no_change-style
> row at the class-level standard layer; admission requires
> admission-grade sources, which are not asserted here pending
> human-auditor anchor pinning).

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`g20-roadmap-crypto-asset-policy-2023`](./g20-roadmap-crypto-asset-policy-2023.md)
- [`fatf-targeted-update-va-vasp-2023`](./fatf-targeted-update-va-vasp-2023.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `8e29b8d`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

