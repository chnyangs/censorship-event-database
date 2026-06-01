# Evidence chain — `kingdom-trust-fincen-2021`

**Status**: `admitted` · **Stratum**: `S3_doj_sec_cftc_fiod` · **Shape**: `null_event` (0 changed layer(s): none) · **Tier**: `null_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `558ea65` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-20` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T01:29:23Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> FinCEN's 2023-04-26 $1.5 million civil money penalty against The
> Kingdom Trust Company is a BSA / AML enforcement action targeting
> the entity's non-conventional trust-services line (Latin-American
> international wire and payment processing) and does not, on the
> public record captured in this authoring pass, engage KTC's
> crypto-IRA custody business or produce a strong-attribution
> crypto-censorship cascade observation. Coded as null_event /
> null_case pending primary-source pinning and any captured
> downstream crypto-offramp effect.

## 1. Trigger

- **Type**: `fincen_action`
- **Actor**: `US_FINCEN`
- **Timestamp**: `2023-04-26 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://www.fincen.gov/news/news-releases/fincen-assesses-15-million-civil-money-penalty-against-kingdom-trust-company>
  - Wayback: <https://web.archive.org/web/20230426173248/https://www.fincen.gov/news/news-releases/fincen-assesses-15-million-civil-money-penalty-against-kingdom-trust-company>
  - body_hash: `sha256:fef5774ea0e271857b3ce9d8087a408bfd4dce53fbea529c9b9d1825cbe48115`
  - body_path: `sources/http_captures/kingdom-trust-fincen-2021/primary/web.archive.org__web-20230426173248-https-www.fincen.gov-news-news-releases-fincen-assesses-15-million-civil-money-penalty-against-kingdom-trust-company__3a8d3bca43.html`
  > FinCEN press release dated 2023-04-26 announcing a $1.5 million
> civil money penalty against The Kingdom Trust Company (KTC), a
> South Dakota-chartered trust company headquartered in Sioux Falls,
> SD with a trust services office in Murray, KY. The slug
> "kingdom-trust-fincen-2021" in this draft refers to the END of
> the BSA violation period (2016-02-15 through 2021-03-15) cited
> in the consent order, NOT the date of the enforcement action
> itself, which falls in 2023. The trigger.timestamp is set to
> the FinCEN announcement date 2023-04-26 to reflect the actual
> enforcement event. Unarchived contextual reference; admission
> would require Wayback or body_hash pinning of the FinCEN news
> release and consent order PDF.
- **`primary_legal`**
  - URL: <https://www.fincen.gov/sites/default/files/enforcement_action/2023-04-27/FinCEN_KTC_ConsentOrder_FINAL_042523.pdf>
  - Wayback: <https://web.archive.org/web/2023/https://www.fincen.gov/sites/default/files/enforcement_action/2023-04-27/FinCEN_KTC_ConsentOrder_FINAL_042523.pdf>
  > FinCEN Consent Order Imposing Civil Money Penalty in the Matter
> of The Kingdom Trust Company, signed 2023-04-25 and published
> on the FinCEN enforcement action repository under the
> 2023-04-27 date stamp. Core findings: (i) KTC willfully violated
> the BSA 2016-02-15 through 2021-03-15 by failing to develop and
> implement an effective AML program for its non-conventional
> trust-services line (account and payment processing services to
> foreign securities firms and other businesses in Latin America);
> (ii) KTC processed at least $4 billion in international wires
> during the relevant period; (iii) KTC filed only four SARs
> during the relevant period despite over 600 incidents
> subsequently identified by FinCEN as merging the SAR-filing
> threshold. Unarchived contextual reference.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: The Kingdom Trust Company
- **Canonical domains**: `kingdomtrust.com`

> Single named legal entity: The Kingdom Trust Company (KTC), a South
> Dakota-chartered trust company. The FinCEN consent order targets
> KTC's BSA / AML compliance posture at the entity level rather than
> enumerating specific on-chain addresses or named customers. The
> enforcement theory rests on registration-and-AML-program failure
> in the non-conventional trust services line (international wire
> and payment processing for foreign securities and investment firms
> in Latin America), NOT on KTC's separately reported self-directed
> IRA custody business (which has historically included crypto-IRA
> custody for Bitcoin and other digital assets via partners such as
> BitGo Trust). Subset enumeration: the named entity is enumerated,
> but the underlying transactions and customer set referenced in the
> 600-plus unfiled-SAR finding are not publicly enumerated in the
> consent order.

## 3. Changed-layer observations (supports the scoped claim)

*No observed_change entries. This is a `null_event`; see §4 for observed_no_change evidence supporting the null claim.*

## 4. No-change observations (where applicable)

### offramp_cex — `no_strong_attribution_crypto_offramp_change_captured_for_2023_04_26_fincen_consent_order`

**Window**: `2023-04-26 00:00:00+00:00` → `2023-05-10 23:59:59+00:00`

**Sources**:

- **`primary_legal`**
  - URL: <https://www.fincen.gov/news/news-releases/fincen-assesses-15-million-civil-money-penalty-against-kingdom-trust-company>
  - Wayback: <https://web.archive.org/web/20230426173248/https://www.fincen.gov/news/news-releases/fincen-assesses-15-million-civil-money-penalty-against-kingdom-trust-company>
  - body_hash: `sha256:fef5774ea0e271857b3ce9d8087a408bfd4dce53fbea529c9b9d1825cbe48115`
  - body_path: `sources/http_captures/kingdom-trust-fincen-2021/primary/web.archive.org__web-20230426173248-https-www.fincen.gov-news-news-releases-fincen-assesses-15-million-civil-money-penalty-against-kingdom-trust-company__3a8d3bca43.html`
  > FinCEN press release pinned as contextual reference only. No
> replayable artifact captured at this authoring pass; no
> strong-attribution crypto-offramp observation can be admitted
> in this draft. Coded as coverage_gap with attribution=none
> per codebook §1.1.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `558ea65`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

