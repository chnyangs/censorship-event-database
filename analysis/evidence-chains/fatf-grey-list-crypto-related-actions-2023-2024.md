# Evidence chain — `fatf-grey-list-crypto-related-actions-2023-2024`

**Status**: `admitted` · **Stratum**: `S6_supranational` · **Shape**: `null_event` (0 changed layer(s): none) · **Tier**: `null_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `698540a` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-21` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "Across the 2023-2024 FATF plenary cycle, two grey-list
> adjustments foregrounded explicit crypto / VASP compliance
> findings: the United Arab Emirates (action-plan progress
> recognised at the October 2023 plenary, formal removal
> 2024-02-23) and Türkiye (removed 2024-06-28 following passage of
> the 2024-06-26 SPK crypto-asset licensing law). Coded as
> null_event / null_case at the corpus's resolution: no per-event
> observed_change cascade is directly attributable to the
> grey-list adjustments themselves; downstream member-state VASP
> enforcement actions are tracked as separate child events."

## 1. Trigger

- **Type**: `supranational_regulation`
- **Actor**: `FATF`
- **Timestamp**: `2023-10-27 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://www.fatf-gafi.org/en/the-fatf/news.html>
  - Wayback: <https://web.archive.org/web/2023/https://www.fatf-gafi.org/en/the-fatf/news.html>
  > Aggregate event covering 2023-2024 FATF plenary outputs that
> materially adjusted the "jurisdictions under increased
> monitoring" (grey) list with explicit crypto / VASP compliance
> findings. Trigger anchored to the October 2023 plenary date
> (2023-10-27) at which the FATF recognised UAE progress on
> AML/CFT (including VASP supervision) leading to the formal UAE
> removal on 2024-02-23. Additional in-window grey-list actions
> with explicit VASP framing include the 2024-06-28 removal of
> Türkiye (preceded by the 2024-06-26 Turkish parliament's
> crypto-asset law mandating SPK licensing of crypto-asset
> service providers).
- **`primary_legal`**
  - URL: <https://www.fatf-gafi.org/content/dam/fatf-gafi/recommendations/2024-Targeted-Update-VA-VASP.pdf.coredownload.inline.pdf>
  - Wayback: <https://web.archive.org/web/20240709172512/https://www.fatf-gafi.org/content/dam/fatf-gafi/recommendations/2024-Targeted-Update-VA-VASP.pdf.coredownload.inline.pdf>
  - body_hash: `sha256:68f2412dad2af07ed5c3e33c8f8bac5a2bcbbfa62f87db85e3bbd0c8e2bfc8c6`
  - body_path: `sources/http_captures/fatf-grey-list-crypto-related-actions-2023-2024/primary/web.archive.org__web-20240709172512-https-www.fatf-gafi.org-content-dam-fatf-gafi-recommendations-2024-Targeted-Update-VA-VASP.pdf.coredownload.inline.pdf__d8a92ad85c.html`
  > June 2024 FATF Targeted Update on VA/VASPs — anchors the
> grey-list crypto framing across the 2023-2024 window. Wayback
> memento 20240709172512 captured 2026-05-21.
- **`supporting_journalism`**
  - URL: <https://complyadvantage.com/insights/fatf-plenary-june-2024/>
  - Wayback: <https://web.archive.org/web/2024/https://complyadvantage.com/insights/fatf-plenary-june-2024/>
  > Supporting journalism summarising the June 2024 plenary
> outcome — Türkiye + Jamaica removed from grey list; explicit
> reference to Türkiye's crypto-asset supervision deficiency as
> a 2021 grey-listing factor. ComplyAdvantage URL retained as
> contextual_unarchived; primary anchoring lives on the FATF
> Targeted Update + Norton Rose Fulbright sources.
- **`supporting_journalism`**
  - URL: <https://www.nortonrosefulbright.com/en/knowledge/publications/eb06aa7c/uae-removed-from-the-fatf-grey-list>
  - Wayback: <https://web.archive.org/web/20240707233919/https://www.nortonrosefulbright.com/en/knowledge/publications/eb06aa7c/uae-removed-from-the-fatf-grey-list>
  - body_hash: `sha256:afea9ce22045f6672271afd257933a80b01c383ea1b0876eb127af5bcd42d856`
  - body_path: `sources/http_captures/fatf-grey-list-crypto-related-actions-2023-2024/primary/web.archive.org__web-20240707233919-https-www.nortonrosefulbright.com-en-knowledge-publications-eb06aa7c-uae-removed-from-the-fatf-grey-list__31f064c5a6.html`
  > Supporting law-firm note documenting the 2024-02-23 UAE
> removal and the VASP-supervision component of the underlying
> action plan. Wayback memento 20240707233919 captured 2026-05-21.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: FATF grey-list member states (UAE, Türkiye in-scope subset)

> Class-level grey-list adjustment with explicit VASP compliance
> framing. Per §7 codebook, class-level regulatory updates are
> encoded as enumeration=subset with class-level rationale here.
> Named in-scope jurisdictions: United Arab Emirates (removed
> 2024-02-23 after October 2023 plenary recognition) and Türkiye
> (removed 2024-06-28 after passage of the SPK crypto-asset
> licensing law on 2024-06-26). Other 2023-2024 grey-list deltas
> (e.g., 2023-06 additions of Cameroon, Croatia, Vietnam; 2024-02
> additions of Kenya, Namibia) are not in scope: their FATF action
> plans do not foreground a VA/VASP compliance finding. Binding
> force is via member-state VASP licensing / Travel Rule
> implementation and reputational pressure on correspondent
> banking; no direct on-chain or off-ramp action is mandated by
> the FATF grey-list mechanism itself.

## 3. Changed-layer observations (supports the scoped claim)

*No observed_change entries. This is a `null_event`; see §4 for observed_no_change evidence supporting the null claim.*

## 4. No-change observations (where applicable)

### offramp_cex — `fatf_grey_list_crypto_related_actions_2023_2024`

**Window**: `2023-02-01 00:00:00+00:00` → `2024-10-31 23:59:59+00:00`

**Sources**:

- **`primary_legal`**
  - URL: <https://www.fatf-gafi.org/content/dam/fatf-gafi/recommendations/2024-Targeted-Update-VA-VASP.pdf.coredownload.inline.pdf>
  - Wayback: <https://web.archive.org/web/20240709172512/https://www.fatf-gafi.org/content/dam/fatf-gafi/recommendations/2024-Targeted-Update-VA-VASP.pdf.coredownload.inline.pdf>
  - body_hash: `sha256:68f2412dad2af07ed5c3e33c8f8bac5a2bcbbfa62f87db85e3bbd0c8e2bfc8c6`
  - body_path: `sources/http_captures/fatf-grey-list-crypto-related-actions-2023-2024/primary/web.archive.org__web-20240709172512-https-www.fatf-gafi.org-content-dam-fatf-gafi-recommendations-2024-Targeted-Update-VA-VASP.pdf.coredownload.inline.pdf__d8a92ad85c.html`
  > Aggregate window covering FATF plenaries Feb 2023 -- Oct
> 2024 with explicit crypto / VASP compliance framing
> (UAE 2024-02-23 removal, Türkiye 2024-06-28 removal). No
> per-event observed_change cascade attributable to these
> grey-list deltas at the corpus's resolution — downstream
> effects manifest via national VASP enforcement (UAE 2024
> exchange Travel Rule fines; Türkiye SPK licensing regime)
> tracked separately. observed_no_change / attribution=none
> per §1.1 codebook. Wayback memento 20240709172512 captured
> 2026-05-21.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`fatf-r15-vasp-travel-rule-2019`](./fatf-r15-vasp-travel-rule-2019.md)
- [`fatf-targeted-update-va-vasp-2021`](./fatf-targeted-update-va-vasp-2021.md)
- [`fatf-targeted-update-va-vasp-2023`](./fatf-targeted-update-va-vasp-2023.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `698540a`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

