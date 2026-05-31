# Evidence chain — `okx-india-exit-2024-03`

**Status**: `admitted` · **Stratum**: `S5_corporate` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `b3ed1c5` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-31` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "OKX's 2024-03-21 cessation of CeFi services for Indian users (close
> positions + withdraw by 2024-04-30), following FIU-IND illegal-operation
> notices and Apple/Google app removals, severed the OKX CeFi off-ramp in
> India; single-layer offramp_cex observed_change with attribution=
> plausible (OKX cited generic local regulations, not a named OKX-specific
> mandate)."

## 1. Trigger

- **Type**: `corporate_policy_change`
- **Actor**: `okx`
- **Timestamp**: `2024-03-21 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`semi_primary_wayback`**
  - URL: <https://techcrunch.com/2024/03/21/crypto-exchange-okx-ceases-services-in-india/>
  - Wayback: <https://web.archive.org/web/20240322011034/https://techcrunch.com/2024/03/21/crypto-exchange-okx-ceases-services-in-india/>
  - body_hash: `sha256:6f72148e83e27a3771872eafc7f1c69ca71150084132832a6488ad6e16203519`
  - body_path: `sources/http_captures/okx-india-exit-2024-03/primary/web.archive.org__web-20240322000000-https-techcrunch.com-2024-03-21-crypto-exchange-okx-ceases-services-in-india__074c6e5c64.html`
  > TechCrunch 2024-03-21: OKX ceased services for users in India,
> advising them to withdraw all funds by April 30 and citing "local
> regulations." Captured body verifies: "withdraw all funds by April
> 30"; "The move follows Apple and Google pulling the eponymous app of
> OKX in the country after" an Indian government agency said many
> crypto exchanges were operating illegally; FIU IND context. Wayback
> 20240322011034.
- **`semi_primary_wayback`**
  - URL: <https://www.coindesk.com/policy/2024/03/21/crypto-exchange-okx-to-end-services-in-india>
  - Wayback: <https://web.archive.org/web/20240322070830/https://www.coindesk.com/policy/2024/03/21/crypto-exchange-okx-to-end-services-in-india/>
  - body_hash: `sha256:19fe144df0e5608b5cf4938c24d2836650c7be3c7f88b32fef1c831669332fd2`
  - body_path: `sources/http_captures/okx-india-exit-2024-03/primary/web.archive.org__web-20240322000000-https-www.coindesk.com-policy-2024-03-21-crypto-exchange-okx-to-end-services-in-india__afcb77b3d0.html`
  > CoinDesk 2024-03-21 corroboration: OKX users in India "have until
> April 30 to close out their positions"; must "close all margin
> positions, as well as positions in perpetuals, futures and options"
> and then "only be able to withdraw their funds"; OKX "is responding
> to regulations" targeting exchanges operating illegally; "The FIU
> IND issued a notice in December to nine exchanges." Independent
> second semi-primary anchor.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `complete`
- **Actor name**: OKX India (CeFi) services

> Target is OKX's centralized (CeFi) service surface for Indian users —
> spot/margin/derivatives trading and account access on okx.com for India.
> Complete enumeration of the India CeFi service set OKX wound down;
> users required to close positions and withdraw by 2024-04-30. (OKX's
> DeFi Web3 wallet remained available per the reporting; the censored
> surface is the CeFi off-ramp.)

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `plausible` · Δt = 0h

**Event label**: `okx_ceases_cefi_services_for_indian_users`

**Timestamp**: `2024-03-21 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`semi_primary_wayback`**
  - URL: <https://techcrunch.com/2024/03/21/crypto-exchange-okx-ceases-services-in-india/>
  - Wayback: <https://web.archive.org/web/20240322011034/https://techcrunch.com/2024/03/21/crypto-exchange-okx-ceases-services-in-india/>
  - body_hash: `sha256:6f72148e83e27a3771872eafc7f1c69ca71150084132832a6488ad6e16203519`
  - body_path: `sources/http_captures/okx-india-exit-2024-03/primary/web.archive.org__web-20240322000000-https-techcrunch.com-2024-03-21-crypto-exchange-okx-ceases-services-in-india__074c6e5c64.html`
  > TechCrunch 2024-03-21: OKX ceased India services, withdraw by
> April 30, citing local regulations after FIU-IND notices and
> Apple/Google app removals. attribution=plausible: the exit is
> directly observed, but OKX cited "local regulations" generically;
> the specific regulatory driver is contextual.
- **`semi_primary_wayback`**
  - URL: <https://www.coindesk.com/policy/2024/03/21/crypto-exchange-okx-to-end-services-in-india>
  - Wayback: <https://web.archive.org/web/20240322070830/https://www.coindesk.com/policy/2024/03/21/crypto-exchange-okx-to-end-services-in-india/>
  - body_hash: `sha256:19fe144df0e5608b5cf4938c24d2836650c7be3c7f88b32fef1c831669332fd2`
  - body_path: `sources/http_captures/okx-india-exit-2024-03/primary/web.archive.org__web-20240322000000-https-www.coindesk.com-policy-2024-03-21-crypto-exchange-okx-to-end-services-in-india__afcb77b3d0.html`
  > CoinDesk corroboration: India users close positions and withdraw
> by 2024-04-30; OKX responding to regulations targeting exchanges
> operating illegally; FIU IND December notice to nine exchanges.
> Independent second semi-primary anchor.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`coinbase-india-exit-2022`](./coinbase-india-exit-2022.md)
- [`okx-nigeria-exit-2024-08`](./okx-nigeria-exit-2024-08.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `b3ed1c5`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

