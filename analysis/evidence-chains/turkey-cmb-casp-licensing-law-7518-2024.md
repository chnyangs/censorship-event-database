# Evidence chain — `turkey-cmb-casp-licensing-law-7518-2024`

**Status**: `admitted` · **Stratum**: `S4_nation_state` · **Shape**: `null_event` (0 changed layer(s): none) · **Tier**: `null_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `3b37c3e` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-21` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "Turkey's Law No. 7518 of 2024-07-02 amended the Capital Markets
> Law to establish a CASP licensing regime under the Capital
> Markets Board (CMB), granting licensing, supervisory, and
> sanctioning authority over Crypto Asset Service Providers
> operating in Turkey, with a transition window for incumbent
> operators and an asset-segregation obligation. Anchored as an
> offramp-layer null_event in the Turkish nation-state cascade
> alongside turkey-cbrt-crypto-ban-2021 (payment-rail parent)."

## 1. Trigger

- **Type**: `regulatory_enforcement`
- **Actor**: `TR_CMB`
- **Timestamp**: `2024-07-02 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://www.resmigazete.gov.tr/eskiler/2024/07/20240702.htm>
  - body_hash: `sha256:ed04b5a959c6af7fb7458f3765dfb21be44bcaad4e35e845ff3dfb073d52ea0f`
  - body_path: `sources/http_captures/turkey-cmb-casp-licensing-law-7518-2024/v0_3_repair/www.resmigazete.gov.tr__eskiler-2024-07-20240702.htm__f1bf1bc7cb.html`
  > **NEW EVENT AUTHORED — DRYRUN 2026-05-17** (Phase F follow-on
> to turkey-cbrt-crypto-ban-2021; lean run): authored by LLM agent
> without personally verifying Wayback / body_hash. origin=agent_draft
> and status=draft pending human audit.
> 
> Turkey Law No. 7518 ("Sermaye Piyasası Kanununda Değişiklik
> Yapılmasına Dair Kanun" — Law on Amendments to the Capital
> Markets Law) enacted 2024-07-02 and published in the Resmi
> Gazete (Official Gazette) on the same date. The law amends
> the Capital Markets Law (CMK / Law No. 6362) to introduce a
> comprehensive licensing regime for Crypto Asset Service
> Providers (CASPs / Kripto Varlık Hizmet Sağlayıcıları),
> granting the Capital Markets Board of Türkiye (Sermaye
> Piyasası Kurulu / CMB / SPK) authority to license, supervise,
> and sanction CASPs operating in Turkey. Establishes a
> transition period for incumbent platforms (BtcTurk, Paribu,
> Binance TR, etc.) to apply for licensure; unlicensed
> operations after the transition window are treated as
> illegal. Minimum charter capital thresholds (TRY 100M for
> platforms, TRY 50M for custody-only) and operational
> requirements were later specified via CMB Communiqués
> III-35/B.1 and III-35/B.2 published 2025-03-13.
> Human auditor must pin a verified Resmi Gazete / CMB
> primary-legal URL (specific Law 7518 text) and reconcile
> the transition-period dates.
- **`primary_legal`**
  - URL: <https://www.resmigazete.gov.tr/eskiler/2024/07/20240702.htm>
  - body_hash: `sha256:ed04b5a959c6af7fb7458f3765dfb21be44bcaad4e35e845ff3dfb073d52ea0f`
  - body_path: `sources/http_captures/turkey-cmb-casp-licensing-law-7518-2024/v0_3_repair/www.resmigazete.gov.tr__eskiler-2024-07-20240702.htm__f1bf1bc7cb.html`
  > Second pointer to the Resmi Gazete 2024-07-02 daily index
> as the primary-legal anchor for the Law 7518
> publication. Human auditor must replace with the specific
> Law 7518 text URL and a verified Wayback / body_hash.
- **`supporting_journalism`**
  - URL: <https://kesikli.com/news-insight/2024-07-26-turkiyes-new-crypto-law-transforming-the-turkish-crypto-market/>
  - body_hash: `sha256:cf94f2abf3db27c710990cd7145c74f2969bb2af85c417b674a952fa179e1367`
  - body_path: `sources/http_captures/turkey-cmb-casp-licensing-law-7518-2024/v0_3_repair/kesikli.com__news-insight-2024-07-26-turkiyes-new-crypto-law-transforming-the-turkish-crypto-market__9cb1a126ad.html`
  > Kesikli Law Firm explainer 2024-07-26 summarizing Law 7518
> scope, CMB licensing authority, segregation obligation, and
> transition period. DRYRUN context only — not personally
> archive-verified by the LLM agent.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: Turkish Crypto Asset Service Providers (class)

> Turkish Crypto Asset Service Providers (CASPs / Kripto Varlık
> Hizmet Sağlayıcıları) operating in Turkey as of 2024-07-02 —
> primarily the incumbent domestic exchange/custody operators
> (BtcTurk, Paribu, ICRYPEX, Bitexen, Binance TR, etc.). The
> licensing obligation operates at the VASP/sector level rather
> than via address enumeration: CASPs must obtain a CMB license
> or cease operations after the transition window. Class-level
> rationale: full enumeration deferred pending CMB's published
> license-applicant register.

## 3. Changed-layer observations (supports the scoped claim)

*No observed_change entries. This is a `null_event`; see §4 for observed_no_change evidence supporting the null claim.*

## 4. No-change observations (where applicable)

### offramp_cex — `tr_casp_licensing_regime_established`

**Window**: `2024-07-02 00:00:00+00:00` → `2025-03-13 23:59:59+00:00`

**Sources**:

- **`primary_legal`**
  - URL: <https://www.resmigazete.gov.tr/eskiler/2024/07/20240702.htm>
  - body_hash: `sha256:ed04b5a959c6af7fb7458f3765dfb21be44bcaad4e35e845ff3dfb073d52ea0f`
  - body_path: `sources/http_captures/turkey-cmb-casp-licensing-law-7518-2024/v0_3_repair/www.resmigazete.gov.tr__eskiler-2024-07-20240702.htm__f1bf1bc7cb.html`
  > observed_no_change at the offramp_cex layer: Law 7518
> establishes a CMB licensing regime for CASPs from
> 2024-07-02 forward, with secondary regulations
> (Communiqués III-35/B.1 and III-35/B.2) following on
> 2025-03-13. The corpus has no replayable measurement of
> downstream CASP exit or withdrawal-behavior change. The
> trigger is the regulatory enactment date itself; this row
> anchors the licensing requirement as an offramp-layer
> null_event in the Turkey nation-state cascade alongside
> turkey-cbrt-crypto-ban-2021 (parent payment-rail
> severance). Pre-pinned v0_3_repair body_hash; live
> Resmi Gazete / CMB primary-legal capture during human
> audit.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`turkey-cbrt-crypto-ban-2021`](./turkey-cbrt-crypto-ban-2021.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `3b37c3e`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

