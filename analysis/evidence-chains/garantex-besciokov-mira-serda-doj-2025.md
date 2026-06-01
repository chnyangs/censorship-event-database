# Evidence chain — `garantex-besciokov-mira-serda-doj-2025`

**Status**: `admitted` · **Stratum**: `S3_doj_sec_cftc_fiod` · **Shape**: `comparison` (2 changed layer(s): `l4_frontend`, `offramp_cex`) · **Tier**: `anchor_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `4acc680` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-31` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T03:34:29Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "The 2025-03-07 coordinated U.S. takedown of Garantex (DOJ E.D. Va.
> indictment of administrators Besciokov and Mira Serda for money laundering
> conspiracy / IEEPA / unlicensed money transmitting + U.S. Secret Service
> seizure of three domains Garantex.org/.io/.academy + >$26M fund freeze)
> produced a 2-layer cascade: l4_frontend (domain seizure) and offramp_cex
> (exchange operational disruption), both attribution=direct. No asset_onchain
> row is asserted (release lists no on-chain addresses/tx_hashes; §1.6 floor
> unmet). Comparable-main tier."

## 1. Trigger

- **Type**: `doj_indictment`
- **Actor**: `US_DOJ`
- **Timestamp**: `2025-03-07 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://web.archive.org/web/20250307000000/https://www.justice.gov/opa/pr/garantex-cryptocurrency-exchange-disrupted-international-operation>
  - Wayback: <https://web.archive.org/web/20250307191431/https://www.justice.gov/opa/pr/garantex-cryptocurrency-exchange-disrupted-international-operation>
  - body_hash: `sha256:ec3f812163ed57d80e8af1d4a66cb9d3d156008e80556df0833e6061bfbb8d8a`
  - body_path: `sources/http_captures/garantex-besciokov-mira-serda-doj-2025/primary/web.archive.org__web-20250307000000-https-www.justice.gov-opa-pr-garantex-cryptocurrency-exchange-disrupted-international-operation__d76e9d3a2a.html`
  > DOJ Office of Public Affairs press release (2025-03-07): "Garantex
> Cryptocurrency Exchange Disrupted in International Operation." Federal
> prosecutors in the Eastern District of Virginia unsealed a three-count
> indictment charging two Garantex administrators — Aleksej Besciokov
> (primary technical administrator) and Aleksandr Mira Serda (co-founder
> and chief commercial officer) — with money laundering conspiracy;
> Besciokov was additionally charged with conspiracy to violate the
> International Emergency Economic Powers Act (IEEPA) and conspiracy to
> operate an unlicensed money transmitting business. The U.S. Secret
> Service seized the online infrastructure used to operate Garantex,
> including three domains (Garantex.org, Garantex.io, Garantex.academy),
> and U.S. law enforcement froze more than $26 million in funds. Garantex
> processed at least $96 billion in cryptocurrency transactions since 2019.
> Wayback memento 20250307191431 pinned; captured body grep-confirmed
> "Besciokov", "Mira Serda", "Garantex.org", "Garantex.io",
> "Garantex.academy", "26 million", "Secret Service", "Eastern District
> of Virginia", "International Emergency Economic Powers Act", "96 billion"
> (no on-chain wallet addresses present in the release; none asserted).

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: Garantex + Aleksej Besciokov & Aleksandr Mira Serda
- **Canonical domains**: `garantex.org`, `garantex.io`, `garantex.academy`

> Garantex (Russia-based centralized cryptocurrency exchange) and two named
> administrators — Aleksej Besciokov and Aleksandr Mira Serda. The Secret
> Service seized three operational domains (Garantex.org, Garantex.io,
> Garantex.academy). Marked subset: targets the named defendants + the
> Garantex corporate operation + its seized domains rather than an enumerated
> complete set of Garantex account holders or on-chain addresses.

## 3. Changed-layer observations (supports the scoped claim)

### l4_frontend · attribution: `direct` · Δt = 0h

**Event label**: `secret_service_seizes_three_garantex_domains`

**Timestamp**: `2025-03-07 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_legal`**
  - URL: <https://web.archive.org/web/20250307000000/https://www.justice.gov/opa/pr/garantex-cryptocurrency-exchange-disrupted-international-operation>
  - Wayback: <https://web.archive.org/web/20250307191431/https://www.justice.gov/opa/pr/garantex-cryptocurrency-exchange-disrupted-international-operation>
  - body_hash: `sha256:ec3f812163ed57d80e8af1d4a66cb9d3d156008e80556df0833e6061bfbb8d8a`
  - body_path: `sources/http_captures/garantex-besciokov-mira-serda-doj-2025/primary/web.archive.org__web-20250307000000-https-www.justice.gov-opa-pr-garantex-cryptocurrency-exchange-disrupted-international-operation__d76e9d3a2a.html`
  > DOJ OPA 2025-03-07: U.S. Secret Service seized the online
> infrastructure operating Garantex, including the domains Garantex.org,
> Garantex.io, and Garantex.academy. attribution=direct: a named state
> action against the named operational domains.

### offramp_cex · attribution: `direct` · Δt = 0h

**Event label**: `garantex_exchange_operations_disrupted_by_indictment_and_seizure`

**Timestamp**: `2025-03-07 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_legal`**
  - URL: <https://web.archive.org/web/20250307000000/https://www.justice.gov/opa/pr/garantex-cryptocurrency-exchange-disrupted-international-operation>
  - Wayback: <https://web.archive.org/web/20250307191431/https://www.justice.gov/opa/pr/garantex-cryptocurrency-exchange-disrupted-international-operation>
  - body_hash: `sha256:ec3f812163ed57d80e8af1d4a66cb9d3d156008e80556df0833e6061bfbb8d8a`
  - body_path: `sources/http_captures/garantex-besciokov-mira-serda-doj-2025/primary/web.archive.org__web-20250307000000-https-www.justice.gov-opa-pr-garantex-cryptocurrency-exchange-disrupted-international-operation__d76e9d3a2a.html`
  > DOJ OPA 2025-03-07: the EDVA indictment of Besciokov and Mira Serda +
> Secret Service infrastructure seizure + >$26M freeze disrupted
> Garantex's centralized exchange / off-ramp operations.
> attribution=direct: the coordinated DOJ/Secret Service action is the
> operative state instrument and names the Garantex operation directly.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`bitzlato-doj-2023`](./bitzlato-doj-2023.md)
- [`garantex-ofac-2022`](./garantex-ofac-2022.md)
- [`grinex-garantex-successor-ofac-2025`](./grinex-garantex-successor-ofac-2025.md)
- [`liberty-reserve-coordinated-takedown-2013-05`](./liberty-reserve-coordinated-takedown-2013-05.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `4acc680`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

