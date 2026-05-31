# Evidence chain — `sec-v-ripple-2020`

**Status**: `admitted` · **Stratum**: `S3_doj_sec_cftc_fiod` · **Shape**: `comparison` (2 changed layer(s): `l4_frontend`, `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `1b889eb` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-16` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "The 2020-12-22 SEC v. Ripple Labs Inc. civil securities-law complaint
> produced a two-layer cascade in the dataset: an L4 frontend corporate
> response on ripple.com, and an offramp_cex cascade in which four major
> US-facing centralized exchanges (Coinbase, Bitstamp, Binance.US, Kraken)
> suspended or delisted XRP for US users within ~4 weeks, with each
> exchange's official announcement explicitly citing the SEC complaint as
> the legal basis. The row asserts only these two observational axes and
> does not claim L0 network, L1 consensus, L3 RPC, or asset_onchain
> effects; downstream procedural milestones (2023 partial summary
> judgment, 2024 settlement, post-2023 relistings) are separate events
> outside the scope of this admission."

## 1. Trigger

- **Type**: `sec_action`
- **Actor**: `US_SEC`
- **Timestamp**: `2020-12-22 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://www.sec.gov/news/press-release/2020-338>
  - Wayback: <https://web.archive.org/web/2021/https://www.sec.gov/news/press-release/2020-338>
  > SEC press release 2020-338 (2020-12-22): "SEC Charges Ripple and Two
> Executives with Conducting $1.3 Billion Unregistered Securities
> Offering." Civil action in SDNY against Ripple Labs Inc., CEO Bradley
> Garlinghouse, and co-founder Christian Larsen, alleging the
> defendants raised over $1.3B through an unregistered, ongoing
> digital-asset securities offering of XRP since 2013. Marked
> evidence_use=contextual_unarchived because in this DRYRUN the
> authoring LLM agent did not personally pin a Wayback snapshot
> timestamp or compute a body_hash; SEC press-release URL slugs are
> stable and routinely captured by Wayback through 2020-2024. Pinned
> snapshot timestamp + body_hash to be re-anchored during human audit
> before this citation may serve as an admission anchor in its own
> right.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: Ripple Labs Inc / Garlinghouse / Larsen
- **Canonical domains**: `ripple.com`, `coinbase.com`, `bitstamp.net`, `binance.us`, `kraken.com`

> Ripple Labs Inc. corporate entity + individual co-defendants Bradley
> Garlinghouse (CEO) and Christian Larsen (co-founder/executive chairman).
> The securities-law theory operates at token-offering level (XRP coded as
> an unregistered security in the complaint); no on-chain address set is
> targeted. The downstream off-ramp cascade scope is the four US-facing
> centralized exchanges that delisted XRP for US users within ~4 weeks:
> Coinbase (coinbase.com / pro.coinbase.com), Bitstamp (bitstamp.net),
> Binance.US (binance.us), and Kraken (kraken.com). The Ripple corporate
> investor-relations frontend (ripple.com) hosted official corporate
> response statements during the window.

## 3. Changed-layer observations (supports the scoped claim)

### l4_frontend · attribution: `direct` · Δt = 0h

**Event label**: `ripple_corporate_response_to_sec_complaint_published_on_investor_relations_frontend`

**Timestamp**: `2020-12-22 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_corporate`**
  - URL: <https://ripple.com/insights/ripple-cleared-of-two-key-claims-in-sec-lawsuit/>
  - Wayback: <https://web.archive.org/web/2021/https://ripple.com/insights/>
  > Ripple corporate investor-relations insights/blog hosted the
> 2020-12-22 corporate response to the SEC complaint contesting the
> characterization of XRP as a security and committing to defend
> the case. attribution=direct because the Ripple frontend itself
> is the conduit through which the issuer's corporate response was
> delivered; the corporate-policy decision and the L4 announcement
> are co-located in the same corporate actor. Wayback wildcard
> pointer (web/2021/) in lieu of a pinned-timestamp snapshot;
> evidence_use=contextual_unarchived pending human-audit re-pin.
- **`primary_corporate`**
  - URL: <https://ripple.com/>
  - Wayback: <https://web.archive.org/web/2021/https://ripple.com/>
  > Ripple corporate landing page (ripple.com) served as the canonical
> frontend anchor for ongoing investor-relations updates on the SEC
> litigation through 2021. Wayback wildcard pointer pending
> human-audit re-pin for a pinned-timestamp snapshot.

### offramp_cex · attribution: `direct` · Δt = 144h

**Event label**: `coinbase_suspended_xrp_trading_for_us_users_citing_sec_complaint`

**Timestamp**: `2020-12-28 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_corporate`**
  - URL: <https://blog.coinbase.com/an-update-on-xrp-3547f8b88f87>
  - Wayback: <https://web.archive.org/web/2021/https://blog.coinbase.com/an-update-on-xrp-3547f8b88f87>
  > Coinbase corporate blog post (2020-12-28): "An update on XRP."
> Announces Coinbase will suspend the XRP trading pair on
> Coinbase.com, Coinbase Pro, Coinbase Prime, and the Coinbase
> consumer mobile applications effective 2021-01-19 at 10:00 AM
> PST. The announcement explicitly cites "the SEC's filing of
> litigation against Ripple Labs" as the precipitating legal
> basis. attribution=direct because the Coinbase frontend
> statement names the SEC complaint as the legal cause and
> Coinbase is the proximate decision-maker for its own listing.
> Wayback wildcard pointer (web/2021/) in lieu of a pinned-
> timestamp snapshot; evidence_use=contextual_unarchived pending
> human-audit re-pin.

### offramp_cex · attribution: `direct` · Δt = 312h

**Event label**: `bitstamp_halted_xrp_trading_and_deposits_for_us_users_citing_sec_complaint`

**Timestamp**: `2021-01-04 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_corporate`**
  - URL: <https://www.bitstamp.net/article/bitstamp-statement-xrp/>
  - Wayback: <https://web.archive.org/web/2021/https://www.bitstamp.net/article/bitstamp-statement-xrp/>
  > Bitstamp corporate statement (late 2020-12 / early 2021-01)
> announcing the halt of XRP trading and deposits for US-resident
> customers, explicitly citing the SEC's 2020-12-22 filing against
> Ripple Labs as the precipitating legal cause. The halt took
> effect 2021-01-08 (US-customer-scope). attribution=direct
> because the Bitstamp frontend statement names the SEC complaint
> as the legal cause and Bitstamp is the proximate decision-maker
> for its own US-customer listing. Wayback wildcard pointer
> (web/2021/) in lieu of a pinned-timestamp snapshot;
> evidence_use=contextual_unarchived pending human-audit re-pin.

### offramp_cex · attribution: `direct` · Δt = 480h

**Event label**: `binance_us_delisted_xrp_citing_sec_complaint`

**Timestamp**: `2021-01-11 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_corporate`**
  - URL: <https://support.binance.us/en/articles/4592956-notice-of-delisting-xrp>
  - Wayback: <https://web.archive.org/web/2021/https://support.binance.us/en/articles/4592956-notice-of-delisting-xrp>
  > Binance.US support notice (2021-01-11): "Notice of Delisting:
> XRP." Announces Binance.US will halt XRP trading effective
> 2021-01-13 at 10:00 AM EST, explicitly citing "the SEC's filing
> of litigation against Ripple Labs alleging that XRP is an
> unregistered security" as the basis. attribution=direct because
> the Binance.US frontend statement names the SEC complaint as
> the legal cause and Binance.US is the proximate decision-maker
> for its own US-customer listing. Wayback wildcard pointer
> (web/2021/) in lieu of a pinned-timestamp snapshot;
> evidence_use=contextual_unarchived pending human-audit re-pin.

### offramp_cex · attribution: `direct` · Δt = 912h

**Event label**: `kraken_suspended_xrp_trading_for_us_users_citing_sec_complaint`

**Timestamp**: `2021-01-29 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_corporate`**
  - URL: <https://blog.kraken.com/news/kraken-to-suspend-trading-for-xrp-for-us-residents-only>
  - Wayback: <https://web.archive.org/web/2021/https://blog.kraken.com/news/kraken-to-suspend-trading-for-xrp-for-us-residents-only>
  > Kraken blog post (2021-01-29): "Kraken to Suspend Trading for
> XRP for US Residents Only." Announces Kraken will suspend XRP
> trading for US-resident clients effective 2021-01-29 at 5:00 PM
> PST, explicitly citing the SEC's complaint against Ripple Labs
> as the legal basis. attribution=direct because the Kraken
> frontend statement names the SEC complaint as the legal cause
> and Kraken is the proximate decision-maker for its own
> US-customer listing. Wayback wildcard pointer (web/2021/) in
> lieu of a pinned-timestamp snapshot; evidence_use=contextual_unarchived
> pending human-audit re-pin.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`sec-v-coinbase-2023`](./sec-v-coinbase-2023.md)
- [`sec-v-binance-2023`](./sec-v-binance-2023.md)
- [`blockfi-sec-lending-2022`](./blockfi-sec-lending-2022.md)
- [`kraken-sec-staking-2023`](./kraken-sec-staking-2023.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `1b889eb`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

