# Evidence chain — `g7-hiroshima-crypto-statement-2023`

**Status**: `admitted` · **Stratum**: `S6_supranational` · **Shape**: `null_event` (0 changed layer(s): none) · **Tier**: `null_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `cd97438` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-21` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "The G7 Hiroshima Leaders' Communiqué, issued at the Hiroshima
> Summit on 2023-05-20, is a class-level G7 coordination instrument
> endorsing accelerated global implementation of FATF Standards on
> virtual assets (including the Travel Rule) and the OECD Crypto-
> Asset Reporting Framework (CARF) for tax transparency. Coded as
> null_event / null_case at the corpus's resolution: no per-event
> observed_change cascade is directly attributable to the 2023-05-20
> communiqué date; downstream FATF, OECD CARF, and G20 endorsement
> cascades are tracked as separate child events."

## 1. Trigger

- **Type**: `supranational_regulation`
- **Actor**: `G7`
- **Timestamp**: `2023-05-20 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://www.mofa.go.jp/policy/economy/summit/hiroshima23/documents/pdf/Leaders_Communique_01_en.pdf>
  - Wayback: <https://web.archive.org/web/20240315111921id_/https://www.mofa.go.jp/policy/economy/summit/hiroshima23/documents/pdf/Leaders_Communique_01_en.pdf>
  - body_hash: `sha256:dbadd7042f21aabf09f9d0545d340a7f1a1e7fcfe3972264459953ea392903df`
  - body_path: `sources/http_captures/g7-hiroshima-crypto-statement-2023/primary/web.archive.org__web-20240315111921id_-https-www.mofa.go.jp-policy-economy-summit-hiroshima23-documents-pdf-Leaders_Communique_01_en.pdf__8325dd9829.bin`
  > G7 Hiroshima Leaders' Communiqué (issued 2023-05-20 at the
> G7 Hiroshima Summit, Japan, 19-21 May 2023). The communiqué
> addresses crypto-asset regulation, expressing G7 support for
> FATF Standards on virtual assets including the Travel Rule,
> accelerating global implementation against money-laundering /
> terrorism-financing risks, and endorsing the OECD Crypto-
> Asset Reporting Framework (CARF) for tax transparency.
> Foundational G7-level policy statement coordinating high-
> income jurisdiction approaches; downstream effects cascade
> via FATF R.15 INR updates, OECD CARF national adoption, and
> G20 endorsement work (g20-roadmap-crypto-asset-policy-2023).
- **`primary_legal`**
  - URL: <https://www.consilium.europa.eu/media/64497/g7-2023-hiroshima-leaders-communique.pdf>
  - Wayback: <https://web.archive.org/web/2023/https://www.consilium.europa.eu/media/64497/g7-2023-hiroshima-leaders-communique.pdf>
  > Mirror of the G7 Hiroshima Leaders' Communiqué hosted by the
> Council of the European Union (consilium.europa.eu). Used as
> secondary primary_legal anchor; same instrument as the MOFA
> version. Retained as contextual_unarchived (no CDX memento);
> primary anchoring lives on the MOFA PDF above.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: G7-jurisdiction crypto-asset ecosystem

> Class-level G7-coordination instrument addressing crypto-asset
> activities and markets across G7-member jurisdictions (US, UK,
> Canada, France, Germany, Italy, Japan + EU as non-enumerated
> member). Per §7 codebook, class-level regulatory coordination is
> encoded as enumeration=subset with the class-level rationale
> documented here. No address-level enumeration; binding force is
> via FATF Travel Rule (R.15) implementation work and OECD CARF
> national adoption, plus FSB recommendations work which the G7
> communiqué endorses. Downstream affected entities include
> centralized exchanges and custodians (VASPs under FATF R.15),
> stablecoin issuers (under FSB recommendations the G7 endorses),
> and tax-reporting CASPs under OECD CARF.

## 3. Changed-layer observations (supports the scoped claim)

*No observed_change entries. This is a `null_event`; see §4 for observed_no_change evidence supporting the null claim.*

## 4. No-change observations (where applicable)

### offramp_cex — `g7_2023_hiroshima_communique_crypto_asset_statement`

**Window**: `2023-05-20 00:00:00+00:00` → `2024-12-31 23:59:59+00:00`

**Sources**:

- **`primary_legal`**
  - URL: <https://www.mofa.go.jp/policy/economy/summit/hiroshima23/documents/pdf/Leaders_Communique_01_en.pdf>
  - Wayback: <https://web.archive.org/web/20240315111921id_/https://www.mofa.go.jp/policy/economy/summit/hiroshima23/documents/pdf/Leaders_Communique_01_en.pdf>
  - body_hash: `sha256:dbadd7042f21aabf09f9d0545d340a7f1a1e7fcfe3972264459953ea392903df`
  - body_path: `sources/http_captures/g7-hiroshima-crypto-statement-2023/primary/web.archive.org__web-20240315111921id_-https-www.mofa.go.jp-policy-economy-summit-hiroshima23-documents-pdf-Leaders_Communique_01_en.pdf__8325dd9829.bin`
  > G7 Hiroshima Leaders' Communiqué (2023-05-20) endorsement of
> FATF Standards on virtual assets including the Travel Rule
> and the OECD Crypto-Asset Reporting Framework for tax
> transparency is a class-level coordination instrument. No
> per-event observed_change cascade attributable to this
> trigger at the corpus's resolution; downstream effects
> manifest via FATF R.15 INR updates, OECD CARF national
> implementations, and the September 2023 G20 endorsement
> tracked as separate child events. Wayback memento
> 20240315111921 (raw-resource form) captured 2026-05-21.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`g20-roadmap-crypto-asset-policy-2023`](./g20-roadmap-crypto-asset-policy-2023.md)
- [`fatf-r15-vasp-travel-rule-2019`](./fatf-r15-vasp-travel-rule-2019.md)
- [`oecd-carf-2022`](./oecd-carf-2022.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `cd97438`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

