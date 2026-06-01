# Evidence chain — `russia-mining-legalization-law-2024-08`

**Status**: `admitted` · **Stratum**: `S4_nation_state` · **Shape**: `null_event` (0 changed layer(s): none) · **Tier**: `null_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `4acc680` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-21` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T03:34:29Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> *(no scoped_claim recorded — event not paper-ready)*

## 1. Trigger

- **Type**: `regulatory_enforcement`
- **Actor**: `RU_FEDERAL_LAW`
- **Timestamp**: `2024-08-08 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`semi_primary_wayback`**
  - URL: <https://tass.com/economy/1826725>
  - Wayback: <https://web.archive.org/web/20240808183801/https://tass.com/economy/1826725>
  - body_hash: `sha256:86e1df49cc1a8f46eb4ae6af5fa30153edd8834806cb237971da4c00aca7a4ab`
  - body_path: `sources/http_captures/russia-mining-legalization-law-2024-08/primary/web.archive.org__web-20240808183801-https-tass.com-economy-1826725__265b736651.html`
  > TASS English-language announcement dated 2024-08-08 reporting
> that Russian President Vladimir Putin signed Federal Law
> No. 221-FZ "On Amendments to Certain Legislative Acts of the
> Russian Federation," legalizing cryptocurrency mining in
> Russia. The law introduces statutory definitions of "digital
> currency mining," "mining pool," and "mining infrastructure
> operator," permits Russian legal entities and individual
> entrepreneurs registered on a special Federal Tax Service
> registry to engage in industrial-scale mining, and allows
> individual non-registered miners to participate within
> government-set electricity-consumption limits. Effective dates
> are staggered: most provisions enter into force ten days after
> publication, and the special-registry provisions take effect
> 2024-11-01. Wayback anchor uses the year-prefix lookup form
> and requires human-audit re-pinning before any
> admission-anchor use; evidence_use=contextual_unarchived in
> the interim.
- **`semi_primary_wayback`**
  - URL: <https://bitcoinmagazine.com/business/putin-signs-law-legalizing-cryptocurrency-mining-in-russia>
  - Wayback: <https://web.archive.org/web/20240808145931/https://bitcoinmagazine.com/business/putin-signs-law-legalizing-cryptocurrency-mining-in-russia>
  - body_hash: `sha256:5baf01f176986fa9e9f1006fc0353e58c5623ce7a786bdeb7693e999e96a536c`
  - body_path: `sources/http_captures/russia-mining-legalization-law-2024-08/primary/web.archive.org__web-20240808145931-https-bitcoinmagazine.com-business-putin-signs-law-legalizing-cryptocurrency-mining-in-russia__f9146cd7b5.html`
  > Bitcoin Magazine contemporaneous English-language coverage of
> the 2024-08-08 Putin signature of Federal Law No. 221-FZ,
> corroborating the 2024-11-01 effective date for the
> special-registry regime and the industrial-scale mining
> framework. Wayback anchor pending human-audit re-pinning;
> evidence_use=contextual_unarchived.
- **`supporting_journalism`**
  - URL: <https://interfax.com/newsroom/top-stories/104968/>
  - Wayback: <https://web.archive.org/web/2024/https://interfax.com/newsroom/top-stories/104968/>
  > Interfax English-language coverage dated 2024-08-08 confirming
> Putin's signature of the bill legalizing cryptocurrency mining
> in Russia, corroborating the staggered effective dates and the
> registration regime. Used as a triangulation anchor for the
> TASS primary source. Wayback anchor uses the year-prefix
> lookup form; evidence_use=contextual_unarchived pending
> human-audit re-pinning.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: Cryptocurrency-mining activity within the Russian Federation (industrial-scale registered + individual within consumption limits)
- **Chains**: `bitcoin`

> Canonical target is the regulatory class of cryptocurrency-mining
> activity within Russia: industrial-scale mining performed by
> Russian legal entities and individual entrepreneurs (subject to
> inclusion on the Federal Tax Service special registry) and
> individual-scale mining by Russian citizens (subject to
> government-set electricity-consumption limits). The law does not
> enumerate specific named mining operators; enumeration=subset
> rather than complete because the addressed population is a
> statutory class (all in-Russia mining activity) rather than a
> closed roster, matching the convention used by the sibling
> russia-dfa-law-2020 (Federal Law No. 259-FZ) and the sibling
> russia-mining-regional-ban-2024-12 (regional-activity-class
> target).

## 3. Changed-layer observations (supports the scoped claim)

*No observed_change entries. This is a `null_event`; see §4 for observed_no_change evidence supporting the null claim.*

## 4. No-change observations (where applicable)

### l1_consensus — `russia_federal_law_221_fz_legalizes_industrial_mining_under_registration_regime`

**Window**: `2024-08-08 00:00:00+00:00` → `2024-12-31 23:59:59+00:00`

**Sources**:

- **`semi_primary_wayback`**
  - URL: <https://tass.com/economy/1826725>
  - Wayback: <https://web.archive.org/web/20240808183801/https://tass.com/economy/1826725>
  - body_hash: `sha256:86e1df49cc1a8f46eb4ae6af5fa30153edd8834806cb237971da4c00aca7a4ab`
  - body_path: `sources/http_captures/russia-mining-legalization-law-2024-08/primary/web.archive.org__web-20240808183801-https-tass.com-economy-1826725__265b736651.html`
  > TASS reporting establishes that Federal Law No. 221-FZ is a
> permissive framework law: it legalizes (does not prohibit)
> industrial-scale Bitcoin mining in Russia, recognizes
> mining as part of statutory turnover, and routes
> industrial-scale operators through a Federal Tax Service
> registry. Wayback anchor uses the year-prefix lookup form;
> evidence_use=contextual_unarchived pending human-audit
> re-pinning.
- **`semi_primary_wayback`**
  - URL: <https://bitcoinmagazine.com/business/putin-signs-law-legalizing-cryptocurrency-mining-in-russia>
  - Wayback: <https://web.archive.org/web/20240808145931/https://bitcoinmagazine.com/business/putin-signs-law-legalizing-cryptocurrency-mining-in-russia>
  - body_hash: `sha256:5baf01f176986fa9e9f1006fc0353e58c5623ce7a786bdeb7693e999e96a536c`
  - body_path: `sources/http_captures/russia-mining-legalization-law-2024-08/primary/web.archive.org__web-20240808145931-https-bitcoinmagazine.com-business-putin-signs-law-legalizing-cryptocurrency-mining-in-russia__f9146cd7b5.html`
  > Bitcoin Magazine contemporaneous coverage corroborates the
> permissive (legalization) character of the statute and the
> staggered effective-date schedule (most provisions T+10
> days, special-registry provisions 2024-11-01). Retained as a
> triangulation anchor; evidence_use=contextual_unarchived
> pending human-audit re-pinning of the Wayback snapshot.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`russia-mining-regional-ban-2024-12`](./russia-mining-regional-ban-2024-12.md)
- [`russia-dfa-law-2020`](./russia-dfa-law-2020.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `4acc680`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

