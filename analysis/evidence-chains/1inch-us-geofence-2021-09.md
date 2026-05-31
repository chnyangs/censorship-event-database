# Evidence chain — `1inch-us-geofence-2021-09`

**Status**: `admitted` · **Stratum**: `S5_corporate` · **Shape**: `comparison` (1 changed layer(s): `l4_frontend`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `22e4579` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-21` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "On 2021-09-29 the 1inch Network / 1inch Foundation frontend
> operator added a pop-up notification and an IP-based technical
> layer that geofenced US-vantage users from the app.1inch.io
> frontend, while the underlying 1inch Aggregation Protocol
> smart-contract layer remained unaffected. The restriction was
> voluntary (no specific US regulator trigger named); the
> operator's stated rationale was perceived US regulatory risk
> pending a US-targeted 1inch Pro product. Load-bearing axis is
> l4_frontend on a US-vantage subset."

## 1. Trigger

- **Type**: `corporate_policy_change`
- **Actor**: `1INCH_FOUNDATION`
- **Timestamp**: `2021-09-29 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_corporate`**
  - URL: <https://help.1inch.io/en/articles/5099197-which-countries-are-restricted-from-using-the-1inch-dapp>
  - Wayback: <https://web.archive.org/web/2021/https://help.1inch.io/en/articles/5099197-which-countries-are-restricted-from-using-the-1inch-dapp>
  > **NEW EVENT AUTHORED — DRYRUN 2026-05-16** (Phase A.3 S5
> corporate-frontend discovery; lean run): authored by LLM agent
> without personally verifying Wayback/body_hash; origin=agent_draft
> and status=draft pending human review. Real release must replace
> this DRYRUN marker with a human-verified audit after pinning real
> archive anchors.
> 
> 1inch Help Center article on country restrictions for the
> app.1inch.io dApp. On 2021-09-29 the 1inch Foundation /
> 1inch Network frontend operator added a pop-up notification
> and a technical IP-detection layer that geofenced US-vantage
> users out of the app.1inch.io frontend UI; the underlying
> 1inch Aggregation Protocol (smart contracts on Ethereum and
> other chains) was not affected. This is a *voluntary*
> corporate-policy frontend restriction — no specific US
> regulator named a 1inch enforcement action; the operator's
> own public explanation cited perceived US regulatory risk
> and a forthcoming 1inch Pro product for the US market under
> the Series B announcement.
- **`supporting_journalism`**
  - URL: <https://cryptoslate.com/1inch-geofences-us-ip-addresses-says-new-product-for-the-american-market-is-in-prep/>
  - Wayback: <https://web.archive.org/web/2021/https://cryptoslate.com/1inch-geofences-us-ip-addresses-says-new-product-for-the-american-market-is-in-prep/>
  > CryptoSlate coverage (2021-09-30) of the 1inch US-IP geofence
> announcement, citing the 1inch Network blog post / public
> statements that frame the restriction as a voluntary terms-of-
> use compliance step pending the launch of a US-targeted 1inch
> Pro product. DRYRUN: Wayback anchor unverified by LLM agent
> at authoring time.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Protocol**: `1inch_aggregation_protocol`
- **Actor name**: 1inch Network / 1inch Foundation (frontend operator)
- **Chains**: `ethereum`
- **Canonical domains**: `app.1inch.io`

> Class-level target: US-vantage users (clients with US-geolocated
> IPs) of the 1inch Network's app.1inch.io frontend. The restriction
> is a client-side / edge-detection IP-gate combined with a
> terms-of-use pop-up; not enumerated by user account because the
> 1inch dApp is non-custodial. The 1inch Aggregation Protocol
> smart contracts on Ethereum / other chains remain reachable to
> US-vantage users via alternative frontends, direct contract calls,
> and self-hosted UI mirrors — the restriction is exclusively at
> the 1inch-operated frontend.

## 3. Changed-layer observations (supports the scoped claim)

### l4_frontend · attribution: `plausible` · Δt = 0h

**Event label**: `1inch_network_geofenced_us_vantage_users_from_app_1inch_io`

**Timestamp**: `2021-09-29 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`semi_primary_wayback`**
  - URL: <https://cryptoslate.com/1inch-geofences-us-ip-addresses-says-new-product-for-the-american-market-is-in-prep/>
  - Wayback: <https://web.archive.org/web/20210930195439/https://cryptoslate.com/1inch-geofences-us-ip-addresses-says-new-product-for-the-american-market-is-in-prep/>
  - body_hash: `sha256:87ad7bd98fcbbe6a4e6be4640ac3cbdf7e8577970bac02469ab9d48445ad86c9`
  - body_path: `sources/http_captures/1inch-us-geofence-2021-09/primary/web.archive.org__web-20210901000000-https-cryptoslate.com-1inch-geofences-us-ip-addresses-says-new-product-for-the-american-market-is-in-prep__c72e4057ad.html`
  > CryptoSlate 2021-09-30: 1inch began geofencing US IP addresses from
> the 1inch dApp (effective ~2021-09-29), pending a separate US-market
> product. Independent semi-primary anchor (the help.1inch.io restricted-
> countries primary URL has no Wayback memento).
- **`semi_primary_wayback`**
  - URL: <https://www.theblock.co/linked/119055/dex-aggregator-1inch-blocks-out-us-trades-in-preparation-for-separate-american-platform>
  - Wayback: <https://web.archive.org/web/20211001000000/https://www.theblock.co/linked/119055/dex-aggregator-1inch-blocks-out-us-trades-in-preparation-for-separate-american-platform>
  - body_hash: `sha256:4af48ed8d37143a6efaad103fe89456aa9963e4ea1e56c52a3494cfd96f58b58`
  - body_path: `sources/http_captures/1inch-us-geofence-2021-09/primary/web.archive.org__web-20211001000000-https-www.theblock.co-linked-119055-dex-aggregator-1inch-blocks-out-us-trades-in-preparation-for-separate-american-platform__a0864347cd.html`
  > The Block 2021-09-30 corroboration of the 1inch US geofence ahead of
> a separate American platform. Independent second semi-primary anchor.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`uniswap-frontend-delisting-2023`](./uniswap-frontend-delisting-2023.md)
- [`aave-tornado-frontend-block-2022-08`](./aave-tornado-frontend-block-2022-08.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `22e4579`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

