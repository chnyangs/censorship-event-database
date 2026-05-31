# Evidence chain — `bitstamp-greece-portugal-exit-2023`

**Status**: `admitted` · **Stratum**: `S5_corporate` · **Shape**: `null_event` (0 changed layer(s): none) · **Tier**: `null_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-05-31` · **Source commit**: `9849c58` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-21` · **Tool version**: `0.1.0` · **Generated**: `2026-05-31T12:14:39Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "As of the 2026-05-17 authoring pass, no specific 2023 Bitstamp
> Greece-or-Portugal exit action attributable to MiCA-prep or
> national-regulator constraints could be pinned by the authoring
> agent; the Banco de Portugal authorized-entity registry continues
> to list Bitstamp Europe S.A. as authorized, which is positive
> evidence against a clean Portugal exit. Slug is retained as a
> documented null_event record for future evidence surfacing."

## 1. Trigger

- **Type**: `corporate_policy_change`
- **Actor**: `BITSTAMP_EXCHANGE`
- **Timestamp**: `2023-01-01 00:00:00+00:00` (precision: `week`)

### Trigger citations

- **`primary_corporate`**
  - URL: <https://www.bitstamp.net/faq/which-countries-are-the-bitstamp-apps-available-in/>
  - Wayback: <https://web.archive.org/web/2023/https://www.bitstamp.net/faq/which-countries-are-the-bitstamp-apps-available-in/>
  > Bitstamp's published country-availability FAQ. Used here as a
> contextual reference for Bitstamp's EU/EEA service footprint;
> the authoring agent could not pin a specific 2023 announcement
> of a Greece-or-Portugal exit. Marked
> evidence_use=contextual_unarchived because no Wayback snapshot
> was hand-pinned, no body_hash was computed, and — most
> importantly — the page does not by itself constitute evidence
> of a specific 2023 Greece/Portugal exit action by Bitstamp.
- **`primary_legal`**
  - URL: <https://www.bportugal.pt/en/entidadeautorizada/bitstamp-europe-sa>
  - Wayback: <https://web.archive.org/web/20230323174741/https://www.bportugal.pt/en/entidadeautorizada/bitstamp-europe-sa>
  - body_hash: `sha256:1824fc1311d6736e9483e95a8fae2f2856ddec3469902b1de649bedf74bb45f3`
  - body_path: `sources/http_captures/bitstamp-greece-portugal-exit-2023/primary/web.archive.org__web-20230323174741-https-www.bportugal.pt-en-entidadeautorizada-bitstamp-europe-sa__daac2f34b8.html`
  > Banco de Portugal authorized-entity registry entry for Bitstamp
> Europe S.A. Contradicts the slug's premise: as of the public
> web search conducted on 2026-05-17, Bitstamp Europe S.A. is
> listed as an authorized VASP under the Banco de Portugal
> register, which is inconsistent with a clean 2023 Portugal
> exit. Recorded here as load-bearing context for the null_event
> coding: the authoring agent could not pin a specific 2023
> announcement closing Greek or Portuguese services attributable
> to MiCA-prep or national-regulator constraints, and the
> publicly-available regulator registry suggests the opposite
> (continued Portuguese authorization).

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: Bitstamp (Greece + Portugal user cohorts, hypothesized)
- **Canonical domains**: `bitstamp.net`

> Hypothesized Bitstamp Greek-and-Portuguese-resident user cohorts.
> Subset-enumerated because the slug postulates two specific EU
> member-state retail cohorts (Greece and Portugal) as targets of a
> 2023 Bitstamp corporate-policy exit ostensibly framed by MiCA-prep
> and national-regulator constraints. The authoring agent could not
> pin specific exit-announcement evidence for either jurisdiction in
> 2023; coded as null_event per the authoring instruction's null
> fallback clause.

## 3. Changed-layer observations (supports the scoped claim)

*No observed_change entries. This is a `null_event`; see §4 for observed_no_change evidence supporting the null claim.*

## 4. No-change observations (where applicable)

### offramp_cex — `bitstamp_greece_portugal_exit_2023_unpinned`

**Window**: `2023-01-01 00:00:00+00:00` → `2023-12-31 23:59:59+00:00`

**Sources**:

- **`primary_legal`**
  - URL: <https://www.bportugal.pt/en/entidadeautorizada/bitstamp-europe-sa>
  - Wayback: <https://web.archive.org/web/20230323174741/https://www.bportugal.pt/en/entidadeautorizada/bitstamp-europe-sa>
  - body_hash: `sha256:1824fc1311d6736e9483e95a8fae2f2856ddec3469902b1de649bedf74bb45f3`
  - body_path: `sources/http_captures/bitstamp-greece-portugal-exit-2023/primary/web.archive.org__web-20230323174741-https-www.bportugal.pt-en-entidadeautorizada-bitstamp-europe-sa__daac2f34b8.html`
  > Banco de Portugal authorized-entity registry entry for
> Bitstamp Europe S.A. — positive evidence that Bitstamp
> retained Portuguese VASP authorization, which is the
> inverse of what the slug's Portugal-exit premise predicts.
- **`primary_corporate`**
  - URL: <https://www.bitstamp.net/faq/which-countries-are-the-bitstamp-apps-available-in/>
  - Wayback: <https://web.archive.org/web/2023/https://www.bitstamp.net/faq/which-countries-are-the-bitstamp-apps-available-in/>
  > Bitstamp's published country-availability FAQ; contextual
> reference for the absence of any pinned 2023 Greece-or-
> Portugal exclusion announcement attributable to MiCA-prep
> or national-regulator constraints.

## 5. Honest coverage gaps

- **l4_frontend** (`not_measured`): No geo-gated bitstamp.net frontend state diff was captured for

## 7. Related events

- [`bybit-singapore-exit-2022`](./bybit-singapore-exit-2022.md)
- [`kucoin-canada-exit-2023`](./kucoin-canada-exit-2023.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `9849c58`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

