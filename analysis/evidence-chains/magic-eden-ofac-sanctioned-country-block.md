# Evidence chain — `magic-eden-ofac-sanctioned-country-block`

**Status**: `admitted` · **Stratum**: `S5_corporate` · **Shape**: `comparison` (1 changed layer(s): `l4_frontend`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-08` · **Source commit**: `ee7bf1a` · **Schema**: `0.2.0` · **Event last_verified**: `2026-06-01` · **Tool version**: `0.1.0` · **Generated**: `2026-06-25T23:48:26Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> By at least the 2023-09-29 Wayback memento, Magic Eden's official help-center
> documentation stated that Magic Eden services were prohibited in certain
> countries due to existing regulations and OFAC sanctions obligations. This
> draft models the policy as a single-layer l4_frontend marketplace access
> restriction; no on-chain NFT or token transfer effect is claimed.

## 1. Trigger

- **Type**: `corporate_policy_change`
- **Actor**: `MAGIC_EDEN`
- **Timestamp**: `2023-09-29 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_corporate`**
  - URL: <https://help.magiceden.io/en/articles/8115154-restricted-access-for-ofac-sanctioned-countries>
  - Wayback: <https://web.archive.org/web/20230929123242/https://help.magiceden.io/en/articles/8115154-restricted-access-for-ofac-sanctioned-countries>
  - body_hash: `sha256:e799d99ef5d9d24bbeb732f37cb0c4a29177847b15127501a03b303589ec5624`
  - body_path: `sources/http_captures/magic-eden-ofac-sanctioned-country-block/primary/web.archive.org__web-20230929123242-https-help.magiceden.io-en-articles-8115154-restricted-access-for-ofac-sanctioned-countries__393f250088.html`
  > Magic Eden Help Center page "Restricted Access for OFAC Sanctioned
> Countries", captured from the earliest successful Wayback memento found
> in CDX during review (2023-09-29). The captured body states that Magic
> Eden services are prohibited in certain countries due to existing
> regulations and OFAC sanctions obligations. The 2023-09-29 timestamp is
> a first-archived lower-bound for the policy, not a claim that the
> geofence was first implemented on that exact day.
- **`primary_corporate`**
  - URL: <https://magiceden.io/terms-of-service.pdf>
  - body_hash: `sha256:a0bcbc8315b64ac2484a62d2aef9e0ce1c58ee61eec151f2259e16058040ba59`
  - body_path: `sources/http_captures/magic-eden-ofac-sanctioned-country-block/primary/magiceden.io__terms-of-service.pdf__2c7172fcab.bin`
  > Magic Eden Terms of Service PDF, last updated 2024-01-29. The captured
> PDF states that services are available only where permitted by
> applicable law, users represent that they are not located in a country
> subject to a U.S. Government embargo, VPN/geolocation circumvention is
> prohibited, and Magic Eden reserves the right to block access by
> geographic location, IP addresses, device identifiers, or users in
> breach of the terms.

## 2. Target

- **Kind**: `domain`
- **Enumeration**: `subset`
- **Protocol**: `magic_eden_marketplace`
- **Actor name**: Magic Eden marketplace / frontend services
- **Chains**: `solana`, `ethereum`, `bitcoin`, `polygon`
- **Canonical domains**: `magiceden.io`, `help.magiceden.io`

> Class-level target: users attempting to access Magic Eden services from
> OFAC-sanctioned or otherwise restricted countries/regions. The captured
> help-center page and terms do not enumerate the full jurisdiction roster in
> a stable list, so the target is coded as a sanctions-jurisdiction class
> rather than a country-by-country complete enumeration.

## 3. Changed-layer observations (supports the scoped claim)

### l4_frontend · attribution: `direct` · Δt = 0h

**Event label**: `magic_eden_services_blocked_for_ofac_sanctioned_countries`

**Timestamp**: `2023-09-29 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_corporate`**
  - URL: <https://help.magiceden.io/en/articles/8115154-restricted-access-for-ofac-sanctioned-countries>
  - Wayback: <https://web.archive.org/web/20230929123242/https://help.magiceden.io/en/articles/8115154-restricted-access-for-ofac-sanctioned-countries>
  - body_hash: `sha256:e799d99ef5d9d24bbeb732f37cb0c4a29177847b15127501a03b303589ec5624`
  - body_path: `sources/http_captures/magic-eden-ofac-sanctioned-country-block/primary/web.archive.org__web-20230929123242-https-help.magiceden.io-en-articles-8115154-restricted-access-for-ofac-sanctioned-countries__393f250088.html`
  > Official Magic Eden help-center anchor, pinned to a 2023-09-29
> Wayback memento, stating that Magic Eden services are prohibited in
> certain countries because of existing regulations and OFAC sanctions
> obligations.
- **`primary_corporate`**
  - URL: <https://magiceden.io/terms-of-service.pdf>
  - body_hash: `sha256:a0bcbc8315b64ac2484a62d2aef9e0ce1c58ee61eec151f2259e16058040ba59`
  - body_path: `sources/http_captures/magic-eden-ofac-sanctioned-country-block/primary/magiceden.io__terms-of-service.pdf__2c7172fcab.bin`
  > Official Magic Eden Terms of Service corroborating the sanctions /
> embargo eligibility terms and geographic/IP/device blocking authority.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`opensea-iran-cuba-sanctions-block-2022`](./opensea-iran-cuba-sanctions-block-2022.md)
- [`pump-fun-uk-fca-geofence-2024-12`](./pump-fun-uk-fca-geofence-2024-12.md)
- [`pancakeswap-sanctioned-country-frontend-geofence-2022`](./pancakeswap-sanctioned-country-frontend-geofence-2022.md)
- [`1inch-us-geofence-2021-09`](./1inch-us-geofence-2021-09.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `ee7bf1a`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

