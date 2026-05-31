# Evidence chain — `cftc-v-ooki-dao-2022`

**Status**: `admitted` · **Stratum**: `S3_doj_sec_cftc_fiod` · **Shape**: `comparison` (1 changed layer(s): `l4_frontend`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-05-31` · **Source commit**: `ad034bc` · **Schema**: `0.2.0` · **Event last_verified**: `2026-04-22` · **Tool version**: `0.1.0` · **Generated**: `2026-05-31T13:58:50Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "CFTC v. Ooki DAO (2022-09-22 filing; 2023-06-08 default judgment) is
> the first and only CFTC enforcement action against a DAO in the
> dataset. Default judgment mandated US-user frontend geo-blocking with
> the on-chain protocol remaining functional, demonstrating the
> frontend/protocol split under DAO-as-legal-person enforcement."

## 1. Trigger

- **Type**: `cftc_action`
- **Actor**: `US_CFTC`
- **Timestamp**: `2022-09-22 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://www.cftc.gov/PressRoom/PressReleases/8590-22>
  - body_hash: `sha256:a241fc6b6dc9ff3a73c8a9a39fe49032c591a62ca4c84841521b532c26f0ed3d`
  - body_path: `sources/http_captures/cftc-v-ooki-dao-2022/primary/www.cftc.gov__PressRoom-PressReleases-8590-22__bd77d22b3b.html`
  > CFTC press release 8590-22 (2022-09-22): "CFTC Imposes $250,000
> Penalty Against bZeroX, LLC and Its Founders and Charges Successor
> Ooki DAO for Offering Illegal, Off-Exchange Digital-Asset Trading,
> Registration Violations, and Failing to Comply with Bank Secrecy
> Act." Historic action: **first CFTC enforcement action against a
> DAO as a legal person**. Served via the Ooki DAO Help Chat Box
> (accepted as service of process). Charges include offering
> illegal leveraged retail commodity transactions, failing to
> register as FCM/DCO, and BSA/AML violations. Default judgment
> entered 2023-06-08 (Judge Orrick, N.D. Cal).

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `complete`
- **Protocol**: `ooki_protocol`
- **Actor name**: Ooki DAO (formerly bZeroX)
- **Canonical domains**: `ooki.com`, `app.ooki.com`

> Ooki DAO (as legal person) + bZeroX LLC (predecessor entity) +
> co-founders Tom Bean and Kyle Kistner (individuals). No on-chain
> addresses in the CFTC filing — the action targets the DAO-as-person
> legal theory rather than specific addresses. Ooki Protocol smart
> contracts remained on-chain and functional despite the legal action
> against the DAO.

## 3. Changed-layer observations (supports the scoped claim)

### l4_frontend · attribution: `direct` · Δt = 6192.0h

**Event label**: `cftc_enforced_frontend_geo_blocking_us_via_default_judgment`

**Timestamp**: `2023-06-08 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_legal`**
  - URL: <https://www.cftc.gov/media/8741/enfookidaojudgment060923/download>
  - Wayback: <https://web.archive.org/web/20230610092333/https://www.cftc.gov/media/8741/enfookidaojudgment060923/download>
  - body_hash: `sha256:cb8789ad3283645a8ffef6ce726701e72373417a781c48097237685135e37673`
  - body_path: `sources/http_captures/cftc-v-ooki-dao-2022/cftc_judgment_pdf/cftc_v_ooki_dao_judgment_20230608.pdf`
  > CFTC v. Ooki DAO default judgment PDF (N.D. Cal. Case 22-cv-05416,
> Judge Orrick, 4 pages, 100132 bytes). Wayback-captured 2023-06-10
> (~2 days post-judgment). v0.3 audit 2026-05-20 repair: added per
> Session 2 Block D NO decision (qid=38) which flagged the original
> observation row for citing only the 2022-09-22 filing release as
> source for judgment-specific facts 258 days later. pypdf-extracted
> content substantiates: 19xOoki + 16xDAO + 1xdefault judgment +
> 1x$643,542 + 1xOrrick + 5xNorthern District. attribution=direct
> sound: the default judgment IS the legal instrument that mandated
> US-user frontend geo-blocking + $643,542 monetary penalty +
> cessation of Ooki DAO activities.
- **`primary_legal`**
  - URL: <https://www.cftc.gov/media/8736/enfookidaoorder060923/download>
  - Wayback: <https://web.archive.org/web/20230609212231/https://www.cftc.gov/media/8736/enfookidaoorder060923/download>
  - body_hash: `sha256:370136f5c29b0a814c8142c454f678111ee0610b4aad9eff6c8a943b7972bbc1`
  - body_path: `sources/http_captures/cftc-v-ooki-dao-2022/cftc_order_pdf/cftc_v_ooki_dao_order_20230608.pdf`
  > CFTC v. Ooki DAO underlying court order PDF (N.D. Cal., 16 pages,
> 227826 bytes). Wayback-captured 2023-06-09 (~1 day post-judgment).
> pypdf-extracted content substantiates: 64xOoki + 71xDAO +
> 20xdefault judgment + 80xU.S. + 2x$643,542 + 1xOrrick + 18xNorthern
> District. Provides the substantive judicial reasoning and remedy
> structure backing the judgment PDF above.
- **`primary_legal`**
  - URL: <https://www.cftc.gov/PressRoom/PressReleases/8590-22>
  - body_hash: `sha256:a241fc6b6dc9ff3a73c8a9a39fe49032c591a62ca4c84841521b532c26f0ed3d`
  - body_path: `sources/http_captures/cftc-v-ooki-dao-2022/primary/www.cftc.gov__PressRoom-PressReleases-8590-22__bd77d22b3b.html`
  > CFTC initial 2022-09-22 filing release (8590-22) — retained as
> context anchor for the trigger event but NOT load-bearing for
> the 2023-06-08 default judgment outcome (which is anchored to
> the Order + Judgment PDFs above per v0.3 audit 2026-05-20 repair).

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `ad034bc`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

