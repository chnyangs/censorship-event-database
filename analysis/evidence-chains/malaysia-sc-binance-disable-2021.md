# Evidence chain — `malaysia-sc-binance-disable-2021`

**Status**: `admitted` · **Stratum**: `S4_nation_state` · **Shape**: `comparison` (2 changed layer(s): `l4_frontend`, `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-4` · **Dataset cutoff**: `2026-05-16` · **Source commit**: `a0d61e2` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-16` · **Tool version**: `0.1.0` · **Generated**: `2026-05-20T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "Malaysia SC enforcement order of 2021-07-30 directly compelled Binance
> to disable its website (binance.com) and mobile applications (iOS /
> Android) for Malaysian users within a 14-business-day compliance
> window, producing a regulator-mandated operator-state change at the
> Binance Malaysian-customer cohort (L4 frontend load-bearing) with
> cascading severance of the Binance-MY MYR on/off-ramp rail
> (offramp_cex, attribution=plausible because the rail severance is
> downstream of the frontend disable rather than a direct
> banking-prohibition directive). The row does not claim ISP / DNS-level
> connectivity blocking, on-chain asset freeze, or class-wide Malaysian
> banking-rail severance."

## 1. Trigger

- **Type**: `nation_state_block`
- **Actor**: `MY_SC`
- **Timestamp**: `2021-07-30 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://www.sc.com.my/resources/media/media-release>
  - Wayback: <https://web.archive.org/web/2021/https://www.sc.com.my/resources/media/media-release>
  > Malaysia Securities Commission (SC) public reprimand and enforcement
> action dated 2021-07-30 against Binance for illegally operating a
> Recognized Market without registration in Malaysia. The SC ordered
> Binance to (1) disable the Binance website (binance.com) for
> Malaysian users, (2) disable the Binance mobile applications
> (Binance iOS and Android apps) in Malaysia, (3) cease circulation of
> marketing/promotional content directed at Malaysian investors, and
> (4) restrict access to the Binance Telegram group for Malaysian
> users. Binance had been on the SC's Investor Alert List since
> 2020-07. DRYRUN promotion: real anchor (SC press-release index)
> asserted with a 2021-calendar-folder Wayback pointer; pinned
> snapshot timestamp and body_hash capture deferred to non-DRYRUN
> release. Marked evidence_use=contextual_unarchived to flag the
> unarchived state explicitly per validator policy.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: Binance Holdings Ltd. (MY cohort)
- **Canonical domains**: `binance.com`

> Binance group entities (binance.com global platform and Binance iOS /
> Android mobile applications) serving Malaysian retail customers, and
> (by cascade) the Malaysian retail customer cohort of binance.com.
> SC order names Binance as addressee of the disable-for-Malaysian-users
> directive; operational effect is on Malaysian retail users of the
> Binance website, mobile apps, and Telegram channel. Treated as
> entity-level at the Binance-Malaysia cohort.

## 3. Changed-layer observations (supports the scoped claim)

### l4_frontend · attribution: `direct` · Δt = 0h

**Event label**: `binance_my_website_and_apps_disabled_per_sc_order`

**Timestamp**: `2021-07-30 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_legal`**
  - URL: <https://www.sc.com.my/resources/media/media-release>
  - Wayback: <https://web.archive.org/web/2021/https://www.sc.com.my/resources/media/media-release>
  > SC press release is the legal instrument naming Binance as
> addressee of the disable-for-Malaysian-users directive
> (website + iOS/Android apps + Telegram group). attribution=
> direct because the SC order itself compels the operator-state
> change (disablement of the Malaysian-facing Binance frontend
> surface) within the 14-business-day compliance window from the
> publication date. DRYRUN: Wayback anchor is a 2021-calendar-
> folder pointer at sc.com.my/resources/media/media-release;
> pinned snapshot timestamp and body_hash capture deferred to
> human audit.

### offramp_cex · attribution: `plausible` · Δt = 0h

**Event label**: `binance_my_myr_rail_severance_cascade`

**Timestamp**: `2021-07-30 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_legal`**
  - URL: <https://www.sc.com.my/resources/media/media-release>
  - Wayback: <https://web.archive.org/web/2021/https://www.sc.com.my/resources/media/media-release>
  > SC disable order cascades into MYR-rail severance at the
> Binance-MY cohort because the disabled frontend surface
> (website + mobile apps) is the access path through which
> Malaysian retail customers used Binance's P2P MYR-to-crypto
> rails and card/bank deposit channels. attribution=plausible
> because the offramp severance is a downstream consequence of
> the frontend disablement rather than a direct SC-mandated
> banking-rail action (SC has no direct banking-prohibition
> authority over Malaysian retail banks; the cascade is via
> Binance compliance with the frontend disable rather than via
> a Malaysia-Bank-Negara-style directive to banks). DRYRUN:
> pinned anchors for the Binance-MY MYR-rail withdrawal flow
> deferred to human audit.

## 5. Honest coverage gaps

- **l0_network** (`not_measured`): SC enforcement action is a regulator-directed disable order targeting

## 7. Related events

- [`uk-fca-binance-markets-2021`](./uk-fca-binance-markets-2021.md)
- [`singapore-mas-binance-services-2021`](./singapore-mas-binance-services-2021.md)
- [`netherlands-dnb-binance-warning-2021`](./netherlands-dnb-binance-warning-2021.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-4` (commit `a0d61e2`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

