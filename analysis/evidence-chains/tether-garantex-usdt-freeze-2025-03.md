# Evidence chain — `tether-garantex-usdt-freeze-2025-03`

**Status**: `admitted` · **Stratum**: `S5_corporate` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `5cd78e4` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-31` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T00:23:54Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "Tether's 2025-03-06 freeze of ~$27M USDT in Garantex's wallets
> (precipitated by the EU's 2025-02-26 16th-package sanctioning of
> Garantex) forced Garantex to suspend all services and halt
> withdrawals; single-layer offramp_cex observed_change,
> attribution=plausible (no primary order naming the specific frozen
> addresses reproduced in the captured coverage). Asset-layer freeze
> carried as a coverage note pending a pinned freeze tx_hash."

## 1. Trigger

- **Type**: `corporate_policy_change`
- **Actor**: `tether_usdt_issuer`
- **Timestamp**: `2025-03-06 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`semi_primary_wayback`**
  - URL: <https://cointelegraph.com/news/tether-freezes-27-million-usdt-sanctions-garantex-russia>
  - Wayback: <https://web.archive.org/web/20251230143611/https://cointelegraph.com/news/tether-freezes-27-million-usdt-sanctions-garantex-russia>
  - body_hash: `sha256:7fac161b542140e576ba6984a1f9c30726d243d73ffe2043b20fac544b6e277c`
  - body_path: `sources/http_captures/tether-garantex-usdt-freeze-2025-03/primary/web.archive.org__web-20251230143611-https-cointelegraph.com-news-tether-freezes-27-million-usdt-sanctions-garantex-russia__2dfac54eda.html`
  > Cointelegraph 2025-03-06: Garantex announced "Tether has entered
> the war against the Russian crypto market and blocked our wallets
> worth more than 2.5 billion rubles [$27 million]." Garantex
> temporarily suspended all services, including withdrawals, with
> its website under maintenance. The freeze followed the EU
> sanctioning Garantex on 2025-02-26 as part of its 16th package
> of sanctions on Russia (the EU's first crypto-exchange listing).
> Wayback 20251230143611 pinned.
- **`primary_corporate`**
  - URL: <https://tether.io/news/tether-recognized-for-assisting-the-united-states-secret-service-in-23m-freeze-related-to-transfers-on-sanctioned-exchange-garantex/>
  - Wayback: <https://web.archive.org/web/20260306082124/https://tether.io/news/tether-recognized-for-assisting-the-united-states-secret-service-in-23m-freeze-related-to-transfers-on-sanctioned-exchange-garantex/>
  - body_hash: `sha256:94138908ffbc2cf82148c6465988b2b0304d7f9ae9b530bc15a5f4df0f25e7dd`
  - body_path: `sources/http_captures/tether-garantex-usdt-freeze-2025-03/primary/web.archive.org__web-20260306082124-https-tether.io-news-tether-recognized-for-assisting-the-united-states-secret-service-in-23m-freeze-related-to-transfers-on-sanction__f4b7d2b2aa.html`
  > Tether official blog corroborating Tether's compliance freeze
> action against the sanctioned exchange Garantex (Tether-assisted
> US Secret Service freeze related to transfers on Garantex).
> Independent primary-corporate anchor confirming the actor
> (Tether) and target (sanctioned Garantex) of the freeze.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `complete`
- **Actor name**: Garantex (USDT wallets / offramp)
- **Chains**: `tron`, `ethereum`

> Garantex's USDT holdings / operating wallets frozen by Tether,
> forcing the exchange to suspend all services and halt withdrawals.
> Target is the Garantex exchange offramp; the specific frozen
> on-chain addresses are not individually enumerated in the captured
> coverage.

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `plausible` · Δt = 0h

**Event label**: `garantex_suspends_all_services_after_tether_usdt_freeze`

**Timestamp**: `2025-03-06 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`semi_primary_wayback`**
  - URL: <https://cointelegraph.com/news/tether-freezes-27-million-usdt-sanctions-garantex-russia>
  - Wayback: <https://web.archive.org/web/20251230143611/https://cointelegraph.com/news/tether-freezes-27-million-usdt-sanctions-garantex-russia>
  - body_hash: `sha256:7fac161b542140e576ba6984a1f9c30726d243d73ffe2043b20fac544b6e277c`
  - body_path: `sources/http_captures/tether-garantex-usdt-freeze-2025-03/primary/web.archive.org__web-20251230143611-https-cointelegraph.com-news-tether-freezes-27-million-usdt-sanctions-garantex-russia__2dfac54eda.html`
  > Cointelegraph 2025-03-06: Tether froze ~$27M USDT
> ("2.5 billion rubles") on Garantex; Garantex suspended all
> services including withdrawals. attribution=plausible: the
> freeze is causally tied to the EU's 2025-02-26 16th-package
> sanctioning of Garantex (reported context), and the captured
> coverage attributes the service suspension to Tether's freeze
> rather than reproducing a primary order naming the specific
> frozen addresses.
- **`primary_corporate`**
  - URL: <https://tether.io/news/tether-recognized-for-assisting-the-united-states-secret-service-in-23m-freeze-related-to-transfers-on-sanctioned-exchange-garantex/>
  - Wayback: <https://web.archive.org/web/20260306082124/https://tether.io/news/tether-recognized-for-assisting-the-united-states-secret-service-in-23m-freeze-related-to-transfers-on-sanctioned-exchange-garantex/>
  - body_hash: `sha256:94138908ffbc2cf82148c6465988b2b0304d7f9ae9b530bc15a5f4df0f25e7dd`
  - body_path: `sources/http_captures/tether-garantex-usdt-freeze-2025-03/primary/web.archive.org__web-20260306082124-https-tether.io-news-tether-recognized-for-assisting-the-united-states-secret-service-in-23m-freeze-related-to-transfers-on-sanction__f4b7d2b2aa.html`
  > Tether official blog confirming Tether's freeze action against
> the sanctioned Garantex exchange. Primary-corporate anchor for
> the actor + target of the action.

## 5. Honest coverage gaps

- **asset_onchain** (`not_measured`): Tether froze ~$27M USDT in Garantex's wallets (the mechanism). No

## 7. Related events

- [`garantex-ofac-2022`](./garantex-ofac-2022.md)
- [`grinex-garantex-successor-ofac-2025`](./grinex-garantex-successor-ofac-2025.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `5cd78e4`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

