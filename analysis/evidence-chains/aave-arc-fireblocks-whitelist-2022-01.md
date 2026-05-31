# Evidence chain — `aave-arc-fireblocks-whitelist-2022-01`

**Status**: `admitted` · **Stratum**: `S5_corporate` · **Shape**: `comparison` (1 changed layer(s): `l4_frontend`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `00764cd` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-21` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "On 2022-01-05, Aave Arc — a permissioned-pool fork of the Aave V2
> protocol — went live on Ethereum mainnet with Fireblocks as the first
> active whitelister and 30 KYC-vetted institutional addresses onboarded
> at launch. Address-binary whitelisting is enforced at the
> protocol-contract layer via the PermissionManager contract, making
> this the first major protocol-level (not frontend-level)
> address-binary whitelisting deployment in major DeFi. Observational
> axes at asset_onchain (load-bearing, attribution=direct) and
> l4_frontend (derived from the on-chain permission state,
> attribution=direct). Admission-anchor-grade promotion pending pinned
> archive captures."

## 1. Trigger

- **Type**: `corporate_policy_change`
- **Actor**: `AAVE_DAO_AAVE_COMPANIES`
- **Timestamp**: `2022-01-05 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_corporate`**
  - URL: <https://www.fireblocks.com/press/fireblocks-whitelists-30-licensed-financial-institutions-to-participate-in-permissioned-defi-with-the-launch-of-aave-arc>
  - Wayback: <https://web.archive.org/web/2022/https://www.fireblocks.com/press/fireblocks-whitelists-30-licensed-financial-institutions-to-participate-in-permissioned-defi-with-the-launch-of-aave-arc>
  > Fireblocks corporate press release dated 2022-01-05 announcing the
> launch of Aave Arc as a permissioned DeFi liquidity market with
> Fireblocks as the first active whitelister. Names 30 KYC-vetted
> institutions onboarded into the Aave Arc permissioned pool at
> launch (Anubi Digital, Bluefire Capital, Canvas Digital, Celsius,
> CoinShares, GSR, Hidden Road, Ribbit Capital, Covario, Wintermute,
> and others). The Aave Arc protocol-architecture decision is a
> joint Aave-DAO governance approval + Aave Companies (Aave-Labs)
> engineering deployment; the Fireblocks press item is the first
> active-whitelister anchor. DRYRUN: wayback wildcard
> (web/2022/) pointer in lieu of a pinned-timestamp snapshot;
> evidence_use=contextual_unarchived because no body_hash+body_path
> pair has been captured into
> sources/http_captures/aave-arc-fireblocks-whitelist-2022-01/ in
> this session.
- **`supporting_journalism`**
  - URL: <https://www.coindesk.com/business/2022/01/05/fireblocks-whitelists-30-trading-firms-for-aaves-institutional-defi-debut>
  - Wayback: <https://web.archive.org/web/2022/https://www.coindesk.com/business/2022/01/05/fireblocks-whitelists-30-trading-firms-for-aaves-institutional-defi-debut>
  > CoinDesk 2022-01-05 coverage: "Fireblocks 'Whitelists' 30 Trading
> Firms for Aave's Institutional DeFi Debut." Independent
> confirmation of the launch date, whitelister role, and KYC-only
> institutional access model.
- **`supporting_journalism`**
  - URL: <https://cointelegraph.com/news/aave-launches-its-permissioned-pool-aave-arc-with-30-institutions-set-to-join>
  - Wayback: <https://web.archive.org/web/2022/https://cointelegraph.com/news/aave-launches-its-permissioned-pool-aave-arc-with-30-institutions-set-to-join>
  > Cointelegraph 2022-01-05 coverage of the Aave Arc launch as a
> permissioned pool with 30 institutions onboarded via Fireblocks
> whitelister role.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Protocol**: `aave_arc`
- **Actor name**: Aave Arc (Aave V2 institutional permissioned pool)
- **Chains**: `ethereum`
- **Canonical domains**: `aave.com`, `app.aave.com`

> Aave Arc permissioned pool: the institutional-only Aave V2 fork with a
> PermissionManager contract layer enforcing address-binary whitelisting
> at the protocol-contract level (not frontend-level). Subset because the
> enumerated targets are the 30 KYC-vetted Fireblocks-whitelisted
> institutional addresses at launch (Anubi Digital, Bluefire Capital,
> Canvas Digital, Celsius, CoinShares, GSR, Hidden Road, Ribbit Capital,
> Covario, Wintermute, and others named in the Fireblocks press item),
> plus the broader cohort of non-whitelisted Ethereum addresses that are
> excluded by protocol-contract design from supplying or borrowing in
> the Aave Arc pool. The exclusion class is global (any non-whitelisted
> address) — the whitelisted-inclusion class is the small named cohort.

## 3. Changed-layer observations (supports the scoped claim)

### l4_frontend · attribution: `direct` · Δt = 0h

**Event label**: `aave_arc_frontend_surface_reflects_protocol_whitelist_inclusion_class`

**Timestamp**: `2022-01-05 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_corporate`**
  - URL: <https://www.fireblocks.com/press/fireblocks-whitelists-30-licensed-financial-institutions-to-participate-in-permissioned-defi-with-the-launch-of-aave-arc>
  - Wayback: <https://web.archive.org/web/20240613130657/https://www.fireblocks.com/press/fireblocks-whitelists-30-licensed-financial-institutions-to-participate-in-permissioned-defi-with-the-launch-of-aave-arc/>
  - body_hash: `sha256:7f7255026aa31498113ef97e30d9c1155b6e167e19513c7d471f6fd9cbc72672`
  - body_path: `sources/http_captures/aave-arc-fireblocks-whitelist-2022-01/primary/web.archive.org__web-20220110000000-https-www.fireblocks.com-press-fireblocks-whitelists-30-licensed-financial-institutions-to-participate-in-permissioned-defi-with-the__30e6368e01.html`
  > Fireblocks press release announcing the Aave Arc permissioned-DeFi
> launch with 30 whitelisted (KYC'd) institutions - the whitelist-gated
> frontend access restriction. primary_corporate anchor; attribution=direct.
> Wayback 20240613130657 pinned.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`aave-tornado-frontend-block-2022-08`](./aave-tornado-frontend-block-2022-08.md)
- [`cftc-v-ooki-dao-2022`](./cftc-v-ooki-dao-2022.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `00764cd`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

