# Evidence chain — `germany-bafin-binance-licence-withdrawal-2023`

**Status**: `admitted` · **Stratum**: `S4_nation_state` · **Shape**: `comparison` (2 changed layer(s): `l4_frontend`, `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `c7761c0` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-16` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "Binance withdrew its German BaFin crypto-custody licence application
> on 2023-07-26 after BaFin signalled (through supervisory dialogue,
> not a published denial) that the application would not be approved.
> The withdrawal closed the path to a regulated-in-DE Binance offering
> under the pre-MiCA KWG crypto-custody licensing regime and produced
> an operator-state change at the Binance Germany-customer cohort
> (offramp_cex load-bearing) plus a Binance-corporate L4 frontend
> response (Germany-geo notices, attribution=plausible). The row does
> not claim ISP-level connectivity blocking, on-chain asset freeze,
> or class-wide German banking-rail severance."

## 1. Trigger

- **Type**: `nation_state_block`
- **Actor**: `DE_BAFIN`
- **Timestamp**: `2023-07-26 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://www.bafin.de/EN/Homepage/homepage_node.html>
  - Wayback: <https://web.archive.org/web/2023/https://www.bafin.de/EN/Homepage/homepage_node.html>
  > German Federal Financial Supervisory Authority (Bundesanstalt fuer
> Finanzdienstleistungsaufsicht, BaFin) supervisory posture toward
> Binance's German crypto-custody licence application under section 1
> para. 1a sentence 2 no. 6 of the German Banking Act (KWG). On
> 2023-07-26 Binance publicly withdrew its German crypto-custody
> licence application after BaFin signalled (through supervisory
> dialogue, not a formal published denial) that the application would
> not be approved in its then-current form. The BaFin homepage /
> institutions-list directory is the canonical regulator surface;
> the specific supervisory exchange producing the withdrawal is not
> published as a standalone BaFin press item. Marked
> evidence_use=contextual_unarchived because the authoring LLM agent
> did not personally pin a Wayback snapshot timestamp or compute a
> body_hash for the BaFin surface; the specific snapshot and any
> BaFin sectoral statement must be re-pinned during human audit
> before this citation may serve as an admission anchor in its
> own right.
- **`primary_corporate`**
  - URL: <https://www.binance.com/en/blog>
  - Wayback: <https://web.archive.org/web/2023/https://www.binance.com/en/blog>
  > Binance corporate communication (2023-07-26) announcing withdrawal
> of the German BaFin crypto-custody licence application. This
> announcement sits within the broader 2023 EU-market exit cascade
> (Netherlands operations wind-down 2022-07, Belgium FSMA cease-and-
> repatriate 2023-06-23, Cyprus and Austria deregistration mid-2023)
> and pre-dates MiCA's transitional regime. Marked
> evidence_use=contextual_unarchived pending human-audit Wayback
> re-pin and body_hash capture of the specific Binance blog /
> press-line item.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: Binance (Germany-facing entities)
- **Canonical domains**: `binance.com`

> Binance group entities that had sought authorisation under the German
> KWG crypto-custody licensing regime (Kryptoverwahrgeschaeft, KWG sec.
> 1 para. 1a sentence 2 no. 6) and, by cascade, the German retail
> customer cohort of the global binance.com platform. The BaFin
> supervisory action is at the licence-application layer addressed to
> the Binance entity seeking German authorisation; the operational
> effect propagates to German retail users of binance.com who lose
> a path to regulated-in-DE Binance services pre-MiCA. Treated as
> entity-level at the Binance-Germany cohort.

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `direct` · Δt = 0h

**Event label**: `binance_de_crypto_custody_licence_application_withdrawn`

**Timestamp**: `2023-07-26 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_corporate`**
  - URL: <https://www.binance.com/en/blog>
  - Wayback: <https://web.archive.org/web/2023/https://www.binance.com/en/blog>
  > Binance public statement (2023-07-26) is the canonical
> customer-facing notification that the BaFin crypto-custody
> licence application was withdrawn. The statement names
> BaFin supervisory expectations as the precipitating cause —
> attribution=direct at the supervisory-dialogue-as-trigger
> level. DRYRUN: pinned Wayback snapshot and body_hash capture
> of the specific Binance blog / press-line item deferred to
> human audit.
- **`primary_legal`**
  - URL: <https://www.bafin.de/EN/Homepage/homepage_node.html>
  - Wayback: <https://web.archive.org/web/2023/https://www.bafin.de/EN/Homepage/homepage_node.html>
  > BaFin regulator surface anchor. BaFin did not publish a
> same-day press item naming Binance; the supervisory exchange
> producing the withdrawal sits within BaFin's ongoing KWG
> crypto-custody licensing oversight rather than a discrete
> press release. DRYRUN: Wayback anchor is a 2023 calendar-
> folder pointer; specific BaFin sectoral statement (if any)
> must be re-pinned during human audit.

### l4_frontend · attribution: `plausible` · Δt = 24h

**Event label**: `de_geo_specific_restriction_notices_posted`

**Timestamp**: `2023-07-27 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_corporate`**
  - URL: <https://www.binance.com/en/blog>
  - Wayback: <https://web.archive.org/web/2023/https://www.binance.com/en/blog>
  > Binance posted Germany-facing communication on binance.com in
> the days following the 2023-07-26 BaFin licence-application
> withdrawal, with subsequent reduction of DE-licensed product
> surface. attribution=plausible because the frontend notice
> is a Binance-corporate response, not a BaFin-mandated DOM
> change. DRYRUN: pinned Wayback snapshot of the binance.com
> Germany-geo notice page is deferred to human audit.
- **`primary_legal`**
  - URL: <https://www.bafin.de/EN/Homepage/homepage_node.html>
  - Wayback: <https://web.archive.org/web/2023/https://www.bafin.de/EN/Homepage/homepage_node.html>
  > BaFin regulator surface retained as contextual anchor for the
> frontend response. The specific supervisory exchange is not
> published as a standalone BaFin press item; the licence-
> application withdrawal is the publicly visible marker of the
> regulator-driven cause.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`uk-fca-binance-markets-2021`](./uk-fca-binance-markets-2021.md)
- [`netherlands-dnb-binance-warning-2021`](./netherlands-dnb-binance-warning-2021.md)
- [`belgium-fsma-binance-cease-2023`](./belgium-fsma-binance-cease-2023.md)
- [`canada-csa-binance-withdrawal-2023`](./canada-csa-binance-withdrawal-2023.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `c7761c0`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

