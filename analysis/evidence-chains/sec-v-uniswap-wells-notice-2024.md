# Evidence chain — `sec-v-uniswap-wells-notice-2024`

**Status**: `admitted` · **Stratum**: `S3_doj_sec_cftc_fiod` · **Shape**: `null_event` (0 changed layer(s): none) · **Tier**: `null_case`

**Dataset version**: `0.1.0` · **Dataset cutoff**: `2026-04-22` · **Source commit**: `6857971` · **Schema**: `0.2.0` · **Event last_verified**: `2026-04-22` · **Tool version**: `0.1.0` · **Generated**: `2026-04-24T00:21:35Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "SEC Wells notice against Uniswap Labs (disclosed 2024-04-10, dropped
> 2025-02-25) was the lowest-enforcement-intensity SEC crypto event in the
> dataset, producing no L4 cascade. Demonstrates that SEC pre-enforcement
> signals alone — without formal complaint filing — do NOT produce
> measurable censorship effects at the frontend or off-ramp layers."

## 1. Trigger

- **Type**: `sec_action`
- **Actor**: `US_SEC`
- **Timestamp**: `2024-04-10 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_corporate`**
  - URL: <https://blog.uniswap.org/fighting-for-defi>
  - body_hash: `sha256:19c7774af50f60cb0acf14edd8a3784ca199301e257bd6e3fd436c2960913638`
  - body_path: `sources/http_captures/sec-v-uniswap-wells-notice-2024/primary/blog.uniswap.org__fighting-for-defi__2b28cd4e31.html`
  > Uniswap Labs blog post "Fighting for DeFi" (2024-04-10) — the primary
> corporate disclosure that Uniswap Labs received a Wells notice from
> the SEC on 2024-04-10. Wells notice is a pre-enforcement SEC staff
> letter indicating intent to recommend formal enforcement. Uniswap Labs
> publicly committed to "fight" any action and framed the notice as a
> jurisdiction-exceeding SEC reach. **No formal SEC complaint was ever
> filed**; SEC formally dropped the matter on 2025-02-25 under the new
> administration.
- **`primary_legal`**
  - URL: <https://www.sec.gov/newsroom/press-releases>
  - body_hash: `sha256:0723d2cb0d308353d4a0584a49bedf28fe6c0ebe9179d2b758c5651fabb2374a`
  - body_path: `sources/http_captures/sec-v-uniswap-wells-notice-2024/primary/www.sec.gov__newsroom-press-releases__17015ee9c7.html`
  > SEC Newsroom press-releases index captured 2026-04-22 as corroborating
> archival anchor — no SEC press release was ever issued about the
> Uniswap Wells notice (Wells notices are pre-enforcement private
> correspondence, not announced publicly by the SEC). The absence of
> an SEC press release is itself the paper-worthy signal distinguishing
> this event from the 2023-06-05/06 SEC v. Binance/Coinbase formal
> filings.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `complete`
- **Protocol**: `uniswap_v2_v3`
- **Actor name**: Uniswap Labs
- **Canonical domains**: `app.uniswap.org`

> Uniswap Labs (the frontend-operator entity; distinct from the underlying
> Uniswap Protocol smart contracts). No tokens named, no on-chain addresses
> attached — the Wells notice is a pre-enforcement signal re. the
> unregistered-broker / unregistered-exchange theory applied to Uniswap
> Labs' frontend operations.

## 3. Changed-layer observations (supports the scoped claim)

*No observed_change entries. This is a `null_event`; see §4 for observed_no_change evidence supporting the null claim.*

## 4. No-change observations (where applicable)

### l4_frontend — `uniswap_frontend_remained_operational_through_wells_notice_period`

**Window**: `2024-04-10 00:00:00+00:00` → `2025-02-25 23:59:59+00:00`

**Sources**:

- **`primary_corporate`**
  - URL: <https://blog.uniswap.org/fighting-for-defi>
  - body_hash: `sha256:19c7774af50f60cb0acf14edd8a3784ca199301e257bd6e3fd436c2960913638`
  - body_path: `sources/http_captures/sec-v-uniswap-wells-notice-2024/primary/blog.uniswap.org__fighting-for-defi__2b28cd4e31.html`
  > Uniswap Labs publicly committed to continuing operations during the
> Wells-notice period. app.uniswap.org frontend remained operational;
> Uniswap Labs pursued litigation-readiness rather than compliance
> remediation. Paper-worthy contrast to the Binance.US fiat-rail
> collapse triggered by the formal SEC complaint (2023-06-05): Wells
> notice alone does NOT produce L4 cascade; formal complaint (especially
> one bundled with asset-freeze motion) does.
- **`primary_legal`**
  - URL: <https://www.sec.gov/newsroom/press-releases>
  - body_hash: `sha256:0723d2cb0d308353d4a0584a49bedf28fe6c0ebe9179d2b758c5651fabb2374a`
  - body_path: `sources/http_captures/sec-v-uniswap-wells-notice-2024/primary/www.sec.gov__newsroom-press-releases__17015ee9c7.html`
  > SEC press-releases index — absence-of-notice anchor. The Wells notice
> is private correspondence; the SEC never filed a formal complaint,
> making this the lowest-enforcement-intensity SEC regulatory-pressure
> event in the dataset.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`sec-v-binance-2023`](./sec-v-binance-2023.md)
- [`sec-v-coinbase-2023`](./sec-v-coinbase-2023.md)
- [`uniswap-frontend-delisting-2023`](./uniswap-frontend-delisting-2023.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.1.0` (commit `6857971`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

