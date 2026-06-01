# Evidence chain — `pancakeswap-sanctioned-country-frontend-geofence-2022`

**Status**: `admitted` · **Stratum**: `S5_corporate` · **Shape**: `comparison` (1 changed layer(s): `l4_frontend`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `210aa10` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-31` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T04:23:47Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "PancakeSwap's reported 2022-03-09 frontend IP geofence against Iran and
> nine other OFAC-sanctioned jurisdictions denied those users UI access to
> the leading BNB-chain DEX (contracts remained directly reachable
> on-chain); single-layer l4_frontend observed_change,
> attribution=plausible (reported, no captured first-party notice)."

## 1. Trigger

- **Type**: `corporate_policy_change`
- **Actor**: `pancakeswap`
- **Timestamp**: `2022-03-09 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`semi_primary_wayback`**
  - URL: <https://www.theblock.co/linked/133904/pancakeswap-dex-reportedly-set-to-block-users-from-iran>
  - Wayback: <https://web.archive.org/web/20260217132905/https://www.theblock.co/linked/133904/pancakeswap-dex-reportedly-set-to-block-users-from-iran>
  - body_hash: `sha256:574429bc1d4b30014b98930cbb13b6df9e22e0a330cf178929cd25e466bb6988`
  - body_path: `sources/http_captures/pancakeswap-sanctioned-country-frontend-geofence-2022/primary/web.archive.org__web-20260217132905-https-www.theblock.co-linked-133904-pancakeswap-dex-reportedly-set-to-block-users-from-iran__0c9239bd6e.html`
  > The Block (Feb 2022): "decentralized exchange platform PancakeSwap
> will reportedly start blocking access to Iranian IP addresses ...
> PancakeSwap will begin geoblocking users [from] other jurisdictions
> on March 9. The other countries included [in] PancakeSwap's
> geofencing are Belarus, Cuba, The Democratic Republic [of Congo],
> ... North Korea, Sudan, Syria, Zimbabwe, and Crimea." Report based
> on a Persian-language screenshot of a PancakeSwap message; no
> first-party PancakeSwap notice captured, hence "reportedly". Wayback
> 20260217132905 pinned; the March 9 cutoff and country list are
> grep-verified in the captured body.

## 2. Target

- **Kind**: `domain`
- **Enumeration**: `subset`
- **Actor name**: PancakeSwap frontend geofence of OFAC-sanctioned jurisdictions
- **Chains**: `bnb_smart_chain`
- **Canonical domains**: `app.pancakeswap.finance`

> PancakeSwap's frontend (app.pancakeswap.finance) geofence against
> users in OFAC-sanctioned jurisdictions. The captured source names
> Iran (primary), Belarus, Cuba, the Democratic Republic of Congo, Iraq,
> North Korea, Sudan, Syria, Zimbabwe and Crimea. Coded subset: the
> blocked-jurisdiction class is named but the controlling sanctions list
> is the OFAC comprehensive-sanctions set rather than a closed
> enumeration fixed by PancakeSwap.

## 3. Changed-layer observations (supports the scoped claim)

### l4_frontend · attribution: `plausible` · Δt = Noneh

**Event label**: `pancakeswap_frontend_geoblocks_ofac_sanctioned_jurisdictions`

**Timestamp**: `2022-03-09 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`semi_primary_wayback`**
  - URL: <https://www.theblock.co/linked/133904/pancakeswap-dex-reportedly-set-to-block-users-from-iran>
  - Wayback: <https://web.archive.org/web/20260217132905/https://www.theblock.co/linked/133904/pancakeswap-dex-reportedly-set-to-block-users-from-iran>
  - body_hash: `sha256:574429bc1d4b30014b98930cbb13b6df9e22e0a330cf178929cd25e466bb6988`
  - body_path: `sources/http_captures/pancakeswap-sanctioned-country-frontend-geofence-2022/primary/web.archive.org__web-20260217132905-https-www.theblock.co-linked-133904-pancakeswap-dex-reportedly-set-to-block-users-from-iran__0c9239bd6e.html`
  > The Block: PancakeSwap reportedly began geoblocking Iran and nine
> other OFAC-sanctioned jurisdictions on 2022-03-09.
> attribution=plausible: the geofence is reported (Persian-language
> screenshot of a PancakeSwap message), not a captured first-party
> PancakeSwap compliance notice citing a specific sanctions trigger,
> so per §1.4 the provider does not publicly cite the trigger in a
> captured statement — plausible is required.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`1inch-us-geofence-2021-09`](./1inch-us-geofence-2021-09.md)
- [`opensea-iran-cuba-sanctions-block-2022`](./opensea-iran-cuba-sanctions-block-2022.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `210aa10`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

