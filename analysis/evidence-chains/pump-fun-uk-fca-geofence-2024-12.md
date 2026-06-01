# Evidence chain — `pump-fun-uk-fca-geofence-2024-12`

**Status**: `admitted` · **Stratum**: `S5_corporate` · **Shape**: `comparison` (1 changed layer(s): `l4_frontend`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-02` · **Source commit**: `c3a88e8` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-17` · **Tool version**: `0.1.0` · **Generated**: `2026-06-02T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "On 2024-12-06 the Pump.fun frontend operators added a UK-
> vantage IP-detection geofence pop-up and a UK exclusion clause
> in the site terms of service, three calendar days after the UK
> FCA's 2024-12-03 unauthorised-firm warning naming Pump.fun;
> the underlying Pump.fun bonding-curve / memecoin launch
> program on Solana remained unaffected. Load-bearing axis is
> l4_frontend on a UK-vantage subset; attribution=direct under
> §1.4 (operator publicly cited FCA warning; block within ≤7-day
> compliance window)."

## 1. Trigger

- **Type**: `corporate_policy_change`
- **Actor**: `PUMP_FUN_OPERATORS`
- **Timestamp**: `2024-12-06 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_corporate`**
  - URL: <https://pump.fun/>
  - Wayback: <https://web.archive.org/web/2024/https://pump.fun/>
  > **NEW EVENT AUTHORED — DRYRUN 2026-05-17** (Phase E S5
> corporate-frontend discovery): authored by LLM agent without
> personally verifying Wayback/body_hash; origin=agent_draft and
> status=draft pending human review. Real release must replace
> this DRYRUN marker with a human-verified audit after pinning
> real archive anchors.
> 
> On 2024-12-06 the Pump.fun frontend operators updated the
> site terms of service to exclude UK-vantage users and
> deployed a UK-IP geofence pop-up on the pump.fun frontend.
> The change followed the UK FCA's 2024-12-03 unauthorised-
> firm warning naming Pump.fun. The Solana on-chain bonding-
> curve / memecoin launch program contracts themselves were
> not affected; the restriction is exclusively a frontend
> application-layer gate.
- **`primary_legal`**
  - URL: <https://www.fca.org.uk/news/warnings/pumpfun>
  - Wayback: <https://web.archive.org/web/2024/https://www.fca.org.uk/news/warnings/pumpfun>
  > FCA unauthorised-firm warning page for Pump.fun (issued
> 2024-12-03). The FCA states Pump.fun is not authorised or
> registered by the FCA and may be promoting or providing
> financial services in the UK without permission. This is
> the public regulator pressure that the Pump.fun operators
> cited as the proximate cause of the 2024-12-06 UK-vantage
> terms-of-service exclusion. DRYRUN: Wayback anchor
> unverified.
- **`supporting_journalism`**
  - URL: <https://www.theblock.co/post/329804/uk-top-financial-regulator-says-pump-fun-doesnt-have-its-permission-to-do-business-in-the-country>
  - Wayback: <https://web.archive.org/web/2024/https://www.theblock.co/post/329804/uk-top-financial-regulator-says-pump-fun-doesnt-have-its-permission-to-do-business-in-the-country>
  > The Block (2024-12-03) coverage of the FCA warning naming
> Pump.fun and quoting the FCA statement that Pump.fun does
> not have permission to do business in the UK.
- **`supporting_journalism`**
  - URL: <https://cryptoslate.com/pump-fun-updates-terms-to-block-uk-users-days-after-fca-warning/>
  - Wayback: <https://web.archive.org/web/2024/https://cryptoslate.com/pump-fun-updates-terms-to-block-uk-users-days-after-fca-warning/>
  > CryptoSlate (2024-12-06) reports the Pump.fun terms-of-
> service update excluding UK users and the UK-vantage
> geofence pop-up implementation on the pump.fun frontend,
> three days after the FCA warning. DRYRUN: Wayback anchor
> unverified.
- **`supporting_journalism`**
  - URL: <https://www.cryptotimes.io/2024/12/06/pump-fun-bans-uk-traders-in-response-to-fca-warning/>
  - Wayback: <https://web.archive.org/web/2024/https://www.cryptotimes.io/2024/12/06/pump-fun-bans-uk-traders-in-response-to-fca-warning/>
  > Crypto Times (2024-12-06) independent contemporaneous
> coverage of the Pump.fun UK ban citing the FCA warning as
> the trigger. DRYRUN: Wayback anchor unverified.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Protocol**: `pump_fun_launchpad`
- **Actor name**: Pump.fun (frontend operators)
- **Chains**: `solana`
- **Canonical domains**: `pump.fun`

> Class-level target: UK-vantage users (clients with UK-geolocated
> IPs) of the Pump.fun memecoin launchpad frontend. The
> restriction is an application-layer IP-gate combined with a
> terms-of-service exclusion clause; not enumerated by user
> account because Pump.fun is non-custodial / wallet-connect. The
> Solana on-chain Pump.fun bonding-curve / launch program
> contracts remain reachable to UK-vantage users via alternative
> frontends, direct program calls, and self-hosted UI mirrors —
> the restriction is exclusively at the Pump.fun-operated
> frontend.

## 3. Changed-layer observations (supports the scoped claim)

### l4_frontend · attribution: `plausible` · Δt = 0h

**Event label**: `pump_fun_geofenced_uk_vantage_users_from_pump_fun_frontend`

**Timestamp**: `2024-12-06 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`semi_primary_wayback`**
  - URL: <https://cryptoslate.com/pump-fun-updates-terms-to-block-uk-users-days-after-fca-warning/>
  - Wayback: <https://web.archive.org/web/20241207231750/https://cryptoslate.com/pump-fun-updates-terms-to-block-uk-users-days-after-fca-warning/>
  - body_hash: `sha256:c89e8a19841cb5f02b437f51e6ebd165397c02fbacf2fcbbc458dbc905ff6282`
  - body_path: `sources/http_captures/pump-fun-uk-fca-geofence-2024-12/primary/web.archive.org__web-20241207000000-https-cryptoslate.com-pump-fun-updates-terms-to-block-uk-users-days-after-fca-warning__eabad3caba.html`
  > CryptoSlate 2024-12-07: Pump.fun updated its terms to block UK
> users days after the FCA warning. Independent semi-primary anchor
> (replaces non-specific pump.fun homepage primary).
- **`semi_primary_wayback`**
  - URL: <https://www.cryptotimes.io/2024/12/06/pump-fun-bans-uk-traders-in-response-to-fca-warning/>
  - Wayback: <https://web.archive.org/web/20250904185529/https://www.cryptotimes.io/2024/12/06/pump-fun-bans-uk-traders-in-response-to-fca-warning/>
  - body_hash: `sha256:771240e85b52250fb07f3ff3388fc0e177ba1f4bc1fb9739e52237295158ba5e`
  - body_path: `sources/http_captures/pump-fun-uk-fca-geofence-2024-12/primary/web.archive.org__web-20241207000000-https-www.cryptotimes.io-2024-12-06-pump-fun-bans-uk-traders-in-response-to-fca-warning__7c3039752d.html`
  > The Crypto Times 2024-12-06 corroboration of the Pump.fun UK
> geofence. Independent second semi-primary anchor.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`1inch-us-geofence-2021-09`](./1inch-us-geofence-2021-09.md)
- [`opensea-iran-cuba-sanctions-block-2022`](./opensea-iran-cuba-sanctions-block-2022.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `c3a88e8`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

