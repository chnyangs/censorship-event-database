# Evidence chain — `eu-mica-2023`

**Status**: `admitted` · **Stratum**: `S6_supranational` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `029a430` · **Schema**: `0.2.0` · **Event last_verified**: `2026-04-22` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T14:19:21Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "EU MiCA Regulation 2023/1114 publication on 2023-06-09 established the
> first supranational unified crypto regulatory framework globally, with
> phased rollout through 2024-12-30. Represents a regulatory-framework-
> trigger event distinct from SDN-style enforcement; downstream CASP-
> specific compliance actions are expected as follow-on events through
> 2025."

## 1. Trigger

- **Type**: `supranational_regulation`
- **Actor**: `EU_Council`
- **Timestamp**: `2023-06-09 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://eur-lex.europa.eu/eli/reg/2023/1114/oj>
  - body_hash: `sha256:07e4a5574cc57713ecd12cb3d214843d916a5efc8919e67afc744ef5d35129a1`
  - body_path: `sources/http_captures/eu-mica-2023/primary/eur-lex.europa.eu__eli-reg-2023-1114-oj__2fcc7e5369.html`
  > Regulation (EU) 2023/1114 of the European Parliament and of the
> Council of 31 May 2023 on Markets in Crypto-Assets (MiCA), published
> in the Official Journal of the European Union on 2023-06-09.
> Establishes comprehensive EU-wide regulatory framework for crypto-
> asset service providers (CASPs), stablecoin issuers (ARTs / EMTs),
> and custodial wallet providers. Phased application: stablecoin
> provisions effective 2024-06-30; full CASP licensing regime effective
> 2024-12-30. First supranational (EU-27) unified crypto regulatory
> framework globally.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: EU Crypto-Asset Service Provider ecosystem (MiCA-regulated)

> All EU-operating Crypto-Asset Service Providers (CASPs) and stablecoin
> issuers (Asset-Referenced Tokens ARTs + E-Money Tokens EMTs). Affects
> USDC, USDT, DAI, and any other stablecoin issuer distributing to EU
> users. CASPs under MiCA include exchanges (e.g. Binance, Coinbase
> EU operations), custodians, portfolio managers, advisors. No address-
> level enumeration — this is sector-wide regulation.

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `direct` · Δt = 0h

**Event label**: `eu_mica_regulation_published_phased_rollout_begins`

**Timestamp**: `2023-06-09 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_legal`**
  - URL: <https://eur-lex.europa.eu/eli/reg/2023/1114/oj>
  - body_hash: `sha256:07e4a5574cc57713ecd12cb3d214843d916a5efc8919e67afc744ef5d35129a1`
  - body_path: `sources/http_captures/eu-mica-2023/primary/eur-lex.europa.eu__eli-reg-2023-1114-oj__2fcc7e5369.html`
  > MiCA OJ publication is the primary legal instrument. EU Council +
> European Parliament are direct actors. CASPs subject to licensing,
> capital, custody, and transparency requirements phased through
> 2024-12-30. Direct attribution: the regulation itself mandates
> the behavior of affected entities.
- **`primary_legal`**
  - URL: <https://eur-lex.europa.eu/eli/reg/2023/1114/oj>
  - body_hash: `sha256:07e4a5574cc57713ecd12cb3d214843d916a5efc8919e67afc744ef5d35129a1`
  - body_path: `sources/http_captures/eu-mica-2023/primary/eur-lex.europa.eu__eli-reg-2023-1114-oj__2fcc7e5369.html`
  > Second anchor to the same OJ publication — MiCA Title III (ART),
> Title IV (EMT), and Title V (CASP) provisions. Cross-reference
> context for downstream CASP-registration events (2024-12 effective).

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `029a430`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

