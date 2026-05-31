# Evidence chain — `netherlands-dnb-binance-warning-2021`

**Status**: `admitted` · **Stratum**: `S4_nation_state` · **Shape**: `comparison` (2 changed layer(s): `l4_frontend`, `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-05-31` · **Source commit**: `b34ad1c` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-16` · **Tool version**: `0.1.0` · **Generated**: `2026-05-31T15:13:25Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "DNB public warning of 2021-08-18 that Binance was offering crypto
> services in the Netherlands without legally-required Wwft
> registration precipitated a slow-cascade NL-cohort offramp
> severance, culminating in a DNB EUR 3.3M fine (2022-04) and
> Binance's announced withdrawal of NL operations (2022-07).
> Load-bearing observational axes are L4 frontend (NL-user notices
> on binance.com) and offramp_cex (NL-user rail restrictions) at
> the Binance-NL cohort level."

## 1. Trigger

- **Type**: `nation_state_block`
- **Actor**: `NL_DNB`
- **Timestamp**: `2021-08-18 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://www.dnb.nl/en/>
  - Wayback: <https://web.archive.org/web/20210818000000*/dnb.nl>
  > De Nederlandsche Bank (DNB) public warning dated 2021-08-18 that
> Binance was offering crypto services in the Netherlands without
> the legally-required registration as a custodian / crypto-service
> provider under the Dutch Anti-Money Laundering and Anti-Terrorist
> Financing Act (Wwft). DRYRUN promotion: real anchor (DNB press
> release index) asserted with Wayback URL pattern; body-hash
> capture deferred to non-DRYRUN release. Marked
> contextual_unarchived to flag the unarchived state explicitly.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: Binance Holdings Ltd. (NL cohort)
- **Canonical domains**: `binance.com`

> Binance Holdings Ltd. / Binance.com cohort serving Dutch retail
> customers. DNB warning targets the global Binance entity (no
> Dutch-registered Binance legal entity existed at the time of the
> warning) and, by cascade, Dutch retail customers of binance.com.
> Target treated as entity-level at the Binance-NL cohort.

## 3. Changed-layer observations (supports the scoped claim)

### l4_frontend · attribution: `direct` · Δt = 7608h

**Event label**: `nl_user_facing_notices_and_2022_07_withdrawal`

**Timestamp**: `2022-07-01 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_legal`**
  - URL: <https://www.dnb.nl/en/>
  - Wayback: <https://web.archive.org/web/20210818000000*/dnb.nl>
  > DNB 2021-08-18 warning is the regulatory anchor. Binance NL
> withdrawal announced 2022-07 cited DNB registration
> requirements; attribution=direct at the DNB-warning-as-
> trigger level. DRYRUN: pinned Wayback captures for the
> Binance 2022-07 withdrawal notice deferred; body-hash
> capture deferred.

### offramp_cex · attribution: `direct` · Δt = 7608h

**Event label**: `nl_user_rail_restrictions_and_eventual_exit`

**Timestamp**: `2022-07-01 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_legal`**
  - URL: <https://www.dnb.nl/en/>
  - Wayback: <https://web.archive.org/web/20220401000000*/dnb.nl>
  > DNB 2022-04 fine (EUR 3.3M) and Binance 2022-07 NL-exit
> announcement evidence the cascade from the 2021-08-18
> warning. NL retail users of binance.com lost native rail
> access. DRYRUN: pinned Wayback captures for the 2022-04
> fine decision and 2022-07 withdrawal notice deferred;
> body-hash capture deferred.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`uk-fca-binance-markets-2021`](./uk-fca-binance-markets-2021.md)
- [`singapore-mas-binance-services-2021`](./singapore-mas-binance-services-2021.md)
- [`malaysia-sc-binance-disable-2021`](./malaysia-sc-binance-disable-2021.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `b34ad1c`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

