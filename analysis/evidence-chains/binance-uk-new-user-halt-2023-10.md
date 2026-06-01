# Evidence chain — `binance-uk-new-user-halt-2023-10`

**Status**: `admitted` · **Stratum**: `S5_corporate` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `4ee1e3c` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-31` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T03:53:57Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "Binance's 2023-10-16 halt on accepting new UK users (to comply with
> the FCA financial-promotions regime after its approver REBS was barred
> on 2023-10-10) severed the Binance off-ramp for new UK customers;
> single-layer offramp_cex observed_change, attribution=plausible (a
> self-imposed corporate compliance step, not a direct FCA order against
> Binance)."

## 1. Trigger

- **Type**: `corporate_policy_change`
- **Actor**: `binance`
- **Timestamp**: `2023-10-16 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`semi_primary_wayback`**
  - URL: <https://www.theblock.co/post/257721/binance-to-temporarily-stop-accepting-new-uk-users-after-fca-restriction>
  - Wayback: <https://web.archive.org/web/20231018060034/https://www.theblock.co/post/257721/binance-to-temporarily-stop-accepting-new-uk-users-after-fca-restriction>
  - body_hash: `sha256:8dd55e39e5f52cbe99f24c92a7a599d107ca39f501dacbdd16f2918b70d7433c`
  - body_path: `sources/http_captures/binance-uk-new-user-halt-2023-10/primary/web.archive.org__web-20231018060034-https-www.theblock.co-post-257721-binance-to-temporarily-stop-accepting-new-uk-users-after-fca-restriction__e41e95ff76.html`
  > The Block 2023-10-16: Binance will temporarily stop accepting new
> UK users effective 16 October 2023 to comply with the UK FCA
> financial-promotions regime. Binance's FCA-approved promotions
> approver, Rebuildingsociety.com, was barred by the FCA (10 Oct
> 2023) from greenlighting crypto financial promotions, forcing
> Binance to halt new-user onboarding while it sought a new
> authorized approver. Existing UK users could not access new
> products/services during the interim. Wayback 20231018060034.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `complete`
- **Actor name**: Binance (new UK-user onboarding)

> Binance's new-user onboarding surface for users resident in the
> United Kingdom. The action geofences new UK customer access to the
> Binance offramp pending a new FCA-authorized financial-promotions
> approver; not an asset-level delisting and not a freeze of existing
> UK balances.

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `plausible` · Δt = 0h

**Event label**: `binance_stops_accepting_new_uk_users_fca_promotions_regime`

**Timestamp**: `2023-10-16 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`semi_primary_wayback`**
  - URL: <https://www.theblock.co/post/257721/binance-to-temporarily-stop-accepting-new-uk-users-after-fca-restriction>
  - Wayback: <https://web.archive.org/web/20231018060034/https://www.theblock.co/post/257721/binance-to-temporarily-stop-accepting-new-uk-users-after-fca-restriction>
  - body_hash: `sha256:8dd55e39e5f52cbe99f24c92a7a599d107ca39f501dacbdd16f2918b70d7433c`
  - body_path: `sources/http_captures/binance-uk-new-user-halt-2023-10/primary/web.archive.org__web-20231018060034-https-www.theblock.co-post-257721-binance-to-temporarily-stop-accepting-new-uk-users-after-fca-restriction__e41e95ff76.html`
  > The Block 2023-10-16: Binance temporarily stops accepting new UK
> users from 16 Oct 2023 to comply with the FCA financial-
> promotions regime after its approver Rebuildingsociety.com was
> barred (10 Oct 2023). attribution=plausible: the halt is directly
> observed and Binance attributes it to FCA promotions-regime
> compliance, but the action is a self-imposed corporate
> compliance step, not a direct FCA order naming Binance — the
> regulator-causation chain runs through the REBS approver bar.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`uk-fca-binance-markets-2021`](./uk-fca-binance-markets-2021.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `4ee1e3c`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

