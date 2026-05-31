# Evidence chain — `binance-privacy-coin-delisting-2023`

**Status**: `admitted` · **Stratum**: `S5_corporate` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `ec5c516` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-16` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "Binance Holdings Limited's 2023-06-26 spot-trading-pair removals
> on binance.com for users resident in France, Italy, Poland, and
> Spain — covering the privacy-asset cohort (Monero/XMR, Zcash/ZEC,
> Dash/DASH, MobileCoin/MOB, Beam/BEAM, Horizen/ZEN, NAV Coin/NAV,
> Firo/FIRO) — narrow the centralized-exchange off-ramp surface for
> the affected privacy assets in the Binance EU-member-state
> corridor. The offramp_cex layer carries the load-bearing
> direct-attribution observation; L0 / L1 / L3 / l4_frontend /
> asset_onchain are not_applicable for a geofenced exchange-
> listing-only action. The row is the cohort-leader anchor for the
> 2023-2024 privacy-coin-delisting wave on centralized exchanges
> (followed by okx-privacy-token-delist-2024 and the Kraken-EU
> 2024 follow-on, coded separately)."

## 1. Trigger

- **Type**: `corporate_policy_change`
- **Actor**: `binance_holdings_limited`
- **Timestamp**: `2023-06-26 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_corporate`**
  - URL: <https://www.binance.com/en/support>
  - Wayback: <https://web.archive.org/web/2023/https://www.binance.com/en/support>
  > Binance customer-support notice (2023-06-26) announcing the
> delisting of privacy-asset spot trading pairs — Monero (XMR),
> Zcash (ZEC), Dash (DASH), MobileCoin (MOB), Beam (BEAM),
> Horizen (ZEN), NAV Coin (NAV), and Firo (FIRO) — for users
> resident in France, Italy, Poland, and Spain. The notice cited
> EU-member-state regulatory expectations ahead of the MiCA
> framework (Regulation (EU) 2023/1114, OJ publication
> 2023-06-09; see related_events: eu-mica-2023) as the
> compliance rationale. Marked evidence_use=contextual_unarchived
> because in this DRYRUN the authoring LLM agent did not
> personally pin a Wayback snapshot timestamp or compute a
> body_hash; the Binance customer-help support hub URL is the
> canonical corporate anchor and is routinely captured by
> Wayback through 2023, but the precise notice-page URL slug
> for the privacy-coin-delisting announcement must be
> re-anchored during human audit before this citation may
> serve as an admission anchor in its own right.

## 2. Target

- **Kind**: `asset`
- **Enumeration**: `subset`
- **Actor name**: Binance Holdings Limited (EU-member-state user cohort)
- **Chains**: `monero`, `zcash`, `dash`, `mobilecoin`, `beam`, `horizen`, `nav`, `firo`
- **Canonical domains**: `binance.com`

> Privacy-asset cohort delisted from Binance spot-trading for users
> resident in France (FR), Italy (IT), Poland (PL), and Spain (ES).
> Named affected assets per the 2023-06-26 customer notice: Monero
> (XMR), Zcash (ZEC), Dash (DASH), MobileCoin (MOB), Beam (BEAM),
> Horizen (ZEN), NAV Coin (NAV), and Firo (FIRO). Recorded as
> enumeration=subset because the geofenced action is scoped to four
> EU-member-state user cohorts rather than a global delisting, and
> Binance's broader 2023-2024 privacy-asset compliance program
> extended through later batches (Belgium, Poland-expansion, and
> other jurisdictions) coded elsewhere or pending in the candidate
> ledger.

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `direct` · Δt = 0h

**Event label**: `binance_spot_pair_removal_privacy_asset_cohort_eu_member_state_users`

**Timestamp**: `2023-06-26 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_corporate`**
  - URL: <https://www.binance.com/en/support>
  - Wayback: <https://web.archive.org/web/2023/https://www.binance.com/en/support>
  > Binance customer-support notice is the corporate-policy
> anchor. The 2023-06-26 announcement names the privacy-asset
> cohort (XMR/ZEC/DASH/MOB/BEAM/ZEN/NAV/FIRO) slated for
> spot-pair removal for users resident in France, Italy,
> Poland, and Spain and gives Binance-direct attribution for
> the off-ramp catalogue change. attribution=direct because
> Binance is both the announcing actor and the operator of
> the affected spot-trading product. Compliance rationale
> per Binance ties the action to EU-member-state regulator
> expectations ahead of the MiCA framework (OJ publication
> 2023-06-09; see eu-mica-2023). Wayback wildcard pointer
> (web/2023/) in lieu of a pinned-timestamp snapshot;
> evidence_use=contextual_unarchived pending human-audit
> re-pin of the precise notice-page URL slug and body_hash.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`okx-privacy-token-delist-2024`](./okx-privacy-token-delist-2024.md)
- [`eu-mica-2023`](./eu-mica-2023.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `ec5c516`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

