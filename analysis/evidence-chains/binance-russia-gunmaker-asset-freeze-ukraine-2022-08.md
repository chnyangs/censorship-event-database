# Evidence chain — `binance-russia-gunmaker-asset-freeze-ukraine-2022-08`

**Status**: `admitted` · **Stratum**: `S5_corporate` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `eabcaae` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-31` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "Binance's late-August-2022 freeze of Vladislav Lobaev's account
> (~US$21,700 raised for Russian troops) after Ukrainian SSU pressure
> severed his Binance off-ramp; single-layer offramp_cex observed_change,
> attribution=plausible (Binance cited only an 'account review', not the
> SSU request)."

## 1. Trigger

- **Type**: `corporate_policy_change`
- **Actor**: `binance`
- **Timestamp**: `2022-08-31 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`semi_primary_wayback`**
  - URL: <https://www.nasdaq.com/articles/binance-froze-russian-gun-makers-crypto-assets-amid-ukrainian-pressure>
  - Wayback: <https://web.archive.org/web/20220914203535/https://www.nasdaq.com/articles/binance-froze-russian-gun-makers-crypto-assets-amid-ukrainian-pressure>
  - body_hash: `sha256:4a9db4928be5154a6b069d5fea5012cdbdbde5afa7bfe964b0b0c2019af22ccb`
  - body_path: `sources/http_captures/binance-russia-gunmaker-asset-freeze-ukraine-2022-08/primary/web.archive.org__web-20220914203535-https-www.nasdaq.com-articles-binance-froze-russian-gun-makers-crypto-assets-amid-ukrainian-pressure__8e0848db7b.html`
  > CoinDesk (via Nasdaq syndication, 2022-08-31): "Binance, the
> world's largest crypto exchange by volume, froze a wallet related
> to Vladislav Lobaev, a Russian gun manufacturer" who fundraised
> for Russian troops in Ukraine. "CoinDesk has confirmed that ...
> wallet was Lobaev's Binance account." Per a Binance support rep
> the account was "locked due to an account review." The Security
> Service of Ukraine (SSU) had published a release saying it
> "blocked a crypto wallet belonging to a Russian [citizen]"; the
> fundraiser had raised "800,000 Ukrainian hryvnias (US$21,700)."
> Wayback 20220914203535 pinned; the freeze, Lobaev identity, SSU
> pressure and amount are grep-verified in the captured body.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: Vladislav Lobaev (Lobaev Arms) Binance account
- **Chains**: `bitcoin`, `ethereum`

> A single Binance account / wallet controlled by Vladislav Lobaev
> (founder of Lobaev Arms, a Russian firearms manufacturer), used to
> fundraise for Russian troops in Ukraine. The captured source confirms
> the frozen account is Lobaev's Binance account but does not publish the
> on-chain deposit addresses; coded subset (the target account is named,
> the address set is not enumerated in the captured primary).

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `plausible` · Δt = Noneh

**Event label**: `binance_freezes_lobaev_account_after_ukrainian_le_pressure`

**Timestamp**: `2022-08-31 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`semi_primary_wayback`**
  - URL: <https://www.nasdaq.com/articles/binance-froze-russian-gun-makers-crypto-assets-amid-ukrainian-pressure>
  - Wayback: <https://web.archive.org/web/20220914203535/https://www.nasdaq.com/articles/binance-froze-russian-gun-makers-crypto-assets-amid-ukrainian-pressure>
  - body_hash: `sha256:4a9db4928be5154a6b069d5fea5012cdbdbde5afa7bfe964b0b0c2019af22ccb`
  - body_path: `sources/http_captures/binance-russia-gunmaker-asset-freeze-ukraine-2022-08/primary/web.archive.org__web-20220914203535-https-www.nasdaq.com-articles-binance-froze-russian-gun-makers-crypto-assets-amid-ukrainian-pressure__8e0848db7b.html`
  > CoinDesk (Nasdaq syndication) 2022-08-31: Binance froze Lobaev's
> account (~US$21,700 in BTC/ETH/USDT) after the SSU identified his
> fundraising. attribution=plausible: the freeze is directly
> observed and CoinDesk confirmed it is Lobaev's Binance account,
> but Binance's only stated reason to the user was "locked due to
> an account review" (not an explicit citation of the SSU request
> or a sanctions designation), so the Ukrainian-LE-request linkage
> is journalistic inference rather than a Binance-stated cause.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `eabcaae`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

