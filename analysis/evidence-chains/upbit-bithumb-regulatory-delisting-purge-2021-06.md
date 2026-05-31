# Evidence chain — `upbit-bithumb-regulatory-delisting-purge-2021-06`

**Status**: `admitted` · **Stratum**: `S5_corporate` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `1929490` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-31` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "Upbit's 2021-06-18 removal of 24 markets and Bithumb's termination of 4
> (effective 2021-07-05) — a regulatory-driven delisting purge that
> included dark/privacy coins (e.g. Monero) ahead of the FIU registration
> deadline — severed the two largest South Korean CEX off-ramps for the
> affected altcoins; single-layer offramp_cex observed_change,
> attribution=plausible (no per-token regulatory order stated)."

## 1. Trigger

- **Type**: `corporate_policy_change`
- **Actor**: `upbit_bithumb`
- **Timestamp**: `2021-06-18 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`semi_primary_wayback`**
  - URL: <https://www.coindesk.com/policy/2021/06/24/upbit-bithumb-delist-numerous-coins-ahead-of-south-korean-regulatory-review>
  - Wayback: <https://web.archive.org/web/20250830094223/https://www.coindesk.com/policy/2021/06/24/upbit-bithumb-delist-numerous-coins-ahead-of-south-korean-regulatory-review>
  - body_hash: `sha256:d4be38d2b326184e24c7c4aa8db32a22a7e3908a7e577a7a31e3756016f8bfac`
  - body_path: `sources/http_captures/upbit-bithumb-regulatory-delisting-purge-2021-06/primary/web.archive.org__web-20250830094223-https-www.coindesk.com-policy-2021-06-24-upbit-bithumb-delist-numerous-coins-ahead-of-south-korean-regulatory-review__b05e4830e7.html`
  > CoinDesk 2021-06-24: "On June 11, Upbit announced ... a watchlist
> of 25 tokens. On June 18, it delisted 24 of them. On June 17,
> Bithumb [announced terminating trading for four tokens effective]
> July 5." Delisted tokens "generally fall into one of the following
> categories: tokens that are listed on less than five exchanges,
> dark coins (privacy coins like monero), tokens directly issued by
> exchanges and tokens whose protocols are no longer being
> developed." Driven by FIU/FSC "recommended guidelines" ahead of
> the Sept. 24 registration deadline; "Delisting announcements have
> caused prices for many altcoins to plummet by 50% or more." Wayback
> 20250830094223 pinned; claims grep-verified in captured body.

## 2. Target

- **Kind**: `asset`
- **Enumeration**: `subset`
- **Actor name**: Upbit/Bithumb delisted altcoins incl. dark/privacy coins (KR)
- **Chains**: `monero`

> Non-exhaustive: Upbit removed fiat (KRW) markets for 5 tokens and
> posted a 25-token watchlist on 2021-06-11, then delisted 24 of them on
> 2021-06-18; Bithumb announced termination of 4 tokens on 2021-06-17
> (effective 2021-07-05). The captured CoinDesk source does not
> enumerate every individual ticker but characterises the delisted set
> as including "dark coins (privacy coins like monero)" alongside
> low-liquidity / exchange-issued / abandoned tokens. Coded subset
> because the class is named ("dark coins / privacy coins like monero")
> but the full per-ticker list is not enumerated in the captured
> primary.

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `plausible` · Δt = Noneh

**Event label**: `upbit_bithumb_delist_altcoins_and_dark_coins_pre_fiu_registration`

**Timestamp**: `2021-06-18 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`semi_primary_wayback`**
  - URL: <https://www.coindesk.com/policy/2021/06/24/upbit-bithumb-delist-numerous-coins-ahead-of-south-korean-regulatory-review>
  - Wayback: <https://web.archive.org/web/20250830094223/https://www.coindesk.com/policy/2021/06/24/upbit-bithumb-delist-numerous-coins-ahead-of-south-korean-regulatory-review>
  - body_hash: `sha256:d4be38d2b326184e24c7c4aa8db32a22a7e3908a7e577a7a31e3756016f8bfac`
  - body_path: `sources/http_captures/upbit-bithumb-regulatory-delisting-purge-2021-06/primary/web.archive.org__web-20250830094223-https-www.coindesk.com-policy-2021-06-24-upbit-bithumb-delist-numerous-coins-ahead-of-south-korean-regulatory-review__b05e4830e7.html`
  > CoinDesk 2021-06-24: Upbit delisted 24 tokens (2021-06-18) from a
> 25-token watchlist; Bithumb terminated 4 (effective 2021-07-05).
> Delisted set characterised as including "dark coins (privacy
> coins like monero)". attribution=plausible: the delistings are
> directly observed and the FIU/FSC "recommended guidelines" /
> Sept. 24 registration context is explicit, but the exchanges did
> not publish a per-token rationale tying each removal to a named
> regulatory order, so the compliance motive is the contextual
> inference rather than a per-target stated cause.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`bittrex-privacy-coin-delisting-2021-01`](./bittrex-privacy-coin-delisting-2021-01.md)
- [`binance-privacy-coin-delisting-2023`](./binance-privacy-coin-delisting-2023.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `1929490`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

