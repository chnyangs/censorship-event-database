# Evidence chain — `japan-fsa-binance-warning-2018`

**Status**: `admitted` · **Stratum**: `S4_nation_state` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `75fb128` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-21` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "Japan FSA's 2018-03-23 public warning to Binance under the Payment
> Services Act for operating a crypto-asset exchange business targeted
> at Japanese residents without registration directly compelled
> Binance's operator-side exit from the Japanese market and relocation
> of its headquarters from Tokyo to Malta in March 2018. The row does
> not claim frontend-disable, ISP/DNS-level connectivity blocking of
> binance.com from Japan, on-chain asset-layer freeze, or any
> customer-funds freeze — only the single-entity Binance-cohort
> offramp_cex load-bearing axis of JP-resident-access deprecation and
> HQ relocation under the Payment Services Act registration regime."

## 1. Trigger

- **Type**: `regulatory_enforcement`
- **Actor**: `JP_FSA`
- **Timestamp**: `2018-03-23 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://www.fsa.go.jp/news/29/sonota/>
  - Wayback: <https://web.archive.org/web/2018/https://www.fsa.go.jp/news/29/sonota/>
  > Japan Financial Services Agency (金融庁 / FSA) press-release index for
> Heisei-29 "sonota" (その他 / "other") notices. On 2018-03-23 the FSA
> issued a public warning under the Payment Services Act (資金決済法)
> against Binance (Hong Kong-domiciled crypto-asset exchange operated
> at the time by Binance Holdings) for operating a crypto-asset
> exchange business targeted at Japanese residents without
> registration with the FSA. The warning stated Binance would face
> criminal charges if it continued unregistered operations. In
> response, Binance CEO Changpeng Zhao announced the company would
> relocate its headquarters out of Japan; Binance subsequently
> announced its move to Malta in March 2018. First major FSA
> enforcement against an offshore crypto exchange after the
> Coincheck supervisory cascade (sibling event
> japan-fsa-coincheck-orders-2018). DRYRUN: real anchor is the FSA
> press-release index folder pointer; pinned snapshot timestamp and
> body_hash capture for the specific 2018-03-23 release permalink
> deferred to non-DRYRUN release.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: Binance Holdings Ltd.
- **Canonical domains**: `binance.com`

> Binance (Binance Holdings Ltd., Hong Kong-domiciled at the time of the
> 2018-03-23 FSA warning) — treated at the entity-level as the named
> addressee of the FSA's 2018-03-23 public warning for operating a
> crypto-asset exchange business targeted at Japanese residents without
> Payment Services Act registration. Subset enumeration: only Binance is
> enumerated here; the 2018-06-22 FSA business-improvement orders
> against six registered Japanese exchanges (sibling event
> japan-fsa-six-exchange-orders-2018-06) is a separate row.
> Downstream operational effect: Binance ceased serving Japan residents
> from its Tokyo-based operations and relocated headquarters to Malta
> in March 2018; Japanese-resident access to Binance via direct
> onboarding was wound down as a registered-VASP-regime compliance
> response.

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `plausible` · Δt = 0h

**Event label**: `binance_jp_resident_access_deprecation_and_hq_relocation_to_malta`

**Timestamp**: `2018-03-23 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_legal`**
  - URL: <https://www.fsa.go.jp/news/29/sonota/>
  - Wayback: <https://web.archive.org/web/2018/https://www.fsa.go.jp/news/29/sonota/>
  > FSA's 2018-03-23 public warning is the legal instrument that
> named Binance and compelled the operator-side exit from the
> Japanese market. attribution=plausible (no pinned FSA primary_* source; FSA index is 403/no-Wayback): the
> actor (Binance) publicly cited the trigger (FSA warning) via
> CEO Changpeng Zhao's public statement that company lawyers
> called JFSA immediately, AND the JP-resident access wind-down
> plus Malta relocation occurred within days of the trigger
> (well inside the typical ≤7-day compliance window for
> frontend/CEX trigger-attributed actions). DRYRUN: Wayback
> anchor is an FSA press-index folder pointer at
> fsa.go.jp/news/29/sonota; pinned snapshot timestamp and
> body_hash capture for the specific 2018-03-23 release
> permalink deferred to human audit.
- **`semi_primary_wayback`**
  - URL: <https://cointelegraph.com/news/binance-served-warning-by-japan-s-fsa-for-operating-without-authorization>
  - Wayback: <https://web.archive.org/web/20210625160823/https://cointelegraph.com/news/binance-served-warning-by-japan-s-fsa-for-operating-without-authorization>
  - body_hash: `sha256:df79ae5ec58b8dbb331bfb7c68c1d0c1d2e34f8967dbed77eb879be5621b702b`
  - body_path: `sources/http_captures/japan-fsa-binance-warning-2018/primary/web.archive.org__web-20210625160823-https-cointelegraph.com-news-binance-served-warning-by-japan-s-fsa-for-operating-without-authorization__41cf65184a.html`
  > Cointelegraph contemporaneous reporting dated 2018-03-23
> corroborates the FSA warning and Binance's announced response
> (CEO statement, intent to relocate). DRYRUN: pinned snapshot
> anchor deferred to human audit.
- **`semi_primary_wayback`**
  - URL: <https://www.cnbc.com/2018/03/23/japanese-regulator-warns-major-cryptocurrency-exchange-for-operating-without-a-license-bitcoin-falls.html>
  - Wayback: <https://web.archive.org/web/20180325055254/https://www.cnbc.com/2018/03/23/japanese-regulator-warns-major-cryptocurrency-exchange-for-operating-without-a-license-bitcoin-falls.html>
  - body_hash: `sha256:d30eaaa00b67baeda8e11e91bf11554f71bb2950ffaa584694d1a4a51f2e361d`
  - body_path: `sources/http_captures/japan-fsa-binance-warning-2018/primary/web.archive.org__web-20180325055254-https-www.cnbc.com-2018-03-23-japanese-regulator-warns-major-cryptocurrency-exchange-for-operating-without-a-license-bitcoin-falls.h__4ef3720a1f.html`
  > CNBC contemporaneous reporting dated 2018-03-23: Japan FSA
> warned Binance of criminal charges if it continued operating
> in Japan without registration. DRYRUN: pinned snapshot anchor
> deferred to human audit.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`japan-fsa-coincheck-orders-2018`](./japan-fsa-coincheck-orders-2018.md)
- [`japan-fsa-six-exchange-orders-2018-06`](./japan-fsa-six-exchange-orders-2018-06.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `75fb128`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

