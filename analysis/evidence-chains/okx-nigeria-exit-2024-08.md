# Evidence chain — `okx-nigeria-exit-2024-08`

**Status**: `admitted` · **Stratum**: `S5_corporate` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `e443d6f` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-31` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "OKX's 2024-07-17 announcement to discontinue all Nigeria services
> effective 2024-08-16 (citing changes in local laws and regulations)
> severed the OKX Nigeria off-ramp; single-layer offramp_cex
> observed_change with attribution=plausible (generic local-law rationale,
> no named OKX-specific mandate)."

## 1. Trigger

- **Type**: `corporate_policy_change`
- **Actor**: `okx`
- **Timestamp**: `2024-07-17 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`semi_primary_wayback`**
  - URL: <https://nairametrics.com/2024/07/17/crypto-exchange-okx-to-discontinue-service-in-nigeria/>
  - Wayback: <https://web.archive.org/web/20240718014739/https://nairametrics.com/2024/07/17/crypto-exchange-okx-to-discontinue-service-in-nigeria/>
  - body_hash: `sha256:977c3d73fd84cc5ca7720a6f37f869e31f38045652f2f29d8547e0eda55045db`
  - body_path: `sources/http_captures/okx-nigeria-exit-2024-08/primary/web.archive.org__web-20240718000000-https-nairametrics.com-2024-07-17-crypto-exchange-okx-to-discontinue-service-in-nigeria__32e70fc89f.html`
  > Nairametrics 2024-07-17: OKX to discontinue services in Nigeria
> "effective from August 16, 2024." Captured body verifies: OKX cited
> "recent changes in local laws and regulations ... based on our
> ongoing assessment"; it advised "Nigerian customers to withdraw
> their funds from the platform on or before the said date"; users
> "can still engage in P2P trading using other currencies." Wayback
> 20240718014739.
- **`semi_primary_wayback`**
  - URL: <https://techpoint.africa/2024/07/17/okx-to-discontinue-services-nigeria/>
  - Wayback: <https://web.archive.org/web/20240720075357/https://techpoint.africa/2024/07/17/okx-to-discontinue-services-nigeria/>
  - body_hash: `sha256:78589ec1377fbdfe8659806e158c1caab11368354246c16f43613df8d3e9766e`
  - body_path: `sources/http_captures/okx-nigeria-exit-2024-08/primary/web.archive.org__web-20240718000000-https-techpoint.africa-2024-07-17-okx-to-discontinue-services-nigeria__c8f9ef3450.html`
  > Techpoint Africa 2024-07-17 corroboration: OKX to discontinue
> services in Nigeria from 2024-08-16, citing local-law changes;
> Nigerian users to withdraw funds. Independent second semi-primary
> anchor.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `complete`
- **Actor name**: OKX Nigeria services

> Target is OKX's service surface for Nigerian users — trading and
> account access on okx.com for Nigeria, discontinued effective
> 2024-08-16 (withdrawals/close-out only thereafter). Complete
> enumeration of the Nigeria service set OKX wound down. (NGN/naira fiat
> and Nigerian P2P had already been removed earlier in 2024 per the
> reporting; the censored surface is OKX's Nigeria off-ramp.)

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `plausible` · Δt = 720h

**Event label**: `okx_discontinues_services_for_nigerian_users`

**Timestamp**: `2024-08-16 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`semi_primary_wayback`**
  - URL: <https://nairametrics.com/2024/07/17/crypto-exchange-okx-to-discontinue-service-in-nigeria/>
  - Wayback: <https://web.archive.org/web/20240718014739/https://nairametrics.com/2024/07/17/crypto-exchange-okx-to-discontinue-service-in-nigeria/>
  - body_hash: `sha256:977c3d73fd84cc5ca7720a6f37f869e31f38045652f2f29d8547e0eda55045db`
  - body_path: `sources/http_captures/okx-nigeria-exit-2024-08/primary/web.archive.org__web-20240718000000-https-nairametrics.com-2024-07-17-crypto-exchange-okx-to-discontinue-service-in-nigeria__32e70fc89f.html`
  > Nairametrics 2024-07-17: OKX to discontinue Nigeria services
> effective 2024-08-16, citing "recent changes in local laws and
> regulations"; Nigerian customers to withdraw before that date.
> attribution=plausible: the exit is directly observed but OKX cited
> generic local-law changes; the precise regulatory driver is
> contextual.
- **`semi_primary_wayback`**
  - URL: <https://techpoint.africa/2024/07/17/okx-to-discontinue-services-nigeria/>
  - Wayback: <https://web.archive.org/web/20240720075357/https://techpoint.africa/2024/07/17/okx-to-discontinue-services-nigeria/>
  - body_hash: `sha256:78589ec1377fbdfe8659806e158c1caab11368354246c16f43613df8d3e9766e`
  - body_path: `sources/http_captures/okx-nigeria-exit-2024-08/primary/web.archive.org__web-20240718000000-https-techpoint.africa-2024-07-17-okx-to-discontinue-services-nigeria__c8f9ef3450.html`
  > Techpoint Africa corroboration: OKX discontinuing Nigeria services
> from 2024-08-16, citing local-law changes. Independent second
> semi-primary anchor.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`binance-nigeria-naira-services-end-2024-03`](./binance-nigeria-naira-services-end-2024-03.md)
- [`nigeria-binance-network-block-2024-02`](./nigeria-binance-network-block-2024-02.md)
- [`okx-india-exit-2024-03`](./okx-india-exit-2024-03.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `e443d6f`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

