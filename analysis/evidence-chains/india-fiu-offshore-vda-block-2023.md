# Evidence chain — `india-fiu-offshore-vda-block-2023`

**Status**: `admitted` · **Stratum**: `S4_nation_state` · **Shape**: `comparison` (2 changed layer(s): `l4_frontend`, `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-05-31` · **Source commit**: `a331305` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-16` · **Tool version**: `0.1.0` · **Generated**: `2026-05-31T04:56:33Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "The FIU-IND 2023-12-28 show-cause notices and the subsequent MEITY
> section 69A URL blocking order severed Indian-vantage access to nine
> named offshore VDA exchange domains (Binance, Kraken, KuCoin, Huobi,
> OKX, Bitstamp, MEXC Global, BitTrex, Gate.io) and removed corresponding
> apps from Apple App Store IN and Google Play IN regional storefronts in
> mid-January 2024. Observational axes at l4_frontend (app-store regional
> removal) and offramp_cex (INR rail severance). L0 admission-anchor-grade
> promotion pending OONI Probe IN / Censored Planet follow-up batch query
> for the nine domains over 2024-01 to 2024-02."

## 1. Trigger

- **Type**: `nation_state_block`
- **Actor**: `IN_FIU`
- **Timestamp**: `2023-12-28 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://www.pib.gov.in/Pressreleaseshare.aspx?PRID=1991372>
  - Wayback: <https://web.archive.org/web/2024/https://www.pib.gov.in/Pressreleaseshare.aspx?PRID=1991372>
  > FIU-IND (Financial Intelligence Unit, India) press release dated
> 2023-12-28 announcing compliance show-cause notices issued to nine
> offshore Virtual Digital Asset (VDA) service providers — Binance,
> Kraken, KuCoin, Huobi, OKX, Bitstamp, MEXC Global, BitTrex, and
> Gate.io — for operating in India without registration as Reporting
> Entities under the Prevention of Money Laundering Act (PMLA). The
> FIU-IND further wrote to the Ministry of Electronics and Information
> Technology (MEITY) recommending URL blocking under section 69A of
> the IT Act. Wayback wildcard pointer (web/2024/) in lieu of a
> pinned-timestamp snapshot; evidence_use=contextual_unarchived
> because a body_hash+body_path pair has not been captured into
> sources/http_captures/india-fiu-offshore-vda-block-2023/ in this
> session. Pinned archive deferred to follow-up authoring pass.
- **`primary_legal`**
  - URL: <https://www.meity.gov.in/>
  > Ministry of Electronics and Information Technology (MEITY) URL
> blocking order issued in early January 2024 implementing the FIU-IND
> recommendation. ISPs in India were directed to block access to the
> nine named offshore VDA exchange domains; Apple App Store (IN) and
> Google Play (IN) removed the corresponding apps from the Indian
> regional storefronts in mid-January 2024. Specific blocking-order
> document not publicly released; contextual_unarchived in lieu of a
> pinned primary-legal anchor.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: Offshore VDA exchanges (FIU-IND show-cause class, IN-vantage access)
- **Canonical domains**: `binance.com`, `kraken.com`, `kucoin.com`, `huobi.com`, `okx.com`, `bitstamp.net`, `mexc.com`, `bittrex.com`, `gate.io`

> Nine named offshore Virtual Digital Asset (VDA) service providers as
> accessed from Indian IP ranges: Binance, Kraken, KuCoin, Huobi, OKX,
> Bitstamp, MEXC Global, BitTrex, and Gate.io. Enumeration is the FIU-IND
> show-cause notice population; not all named platforms may show
> identical app-store / web / re-registration outcomes (e.g., Binance
> and KuCoin subsequently re-registered with FIU-IND in 2024 and were
> unblocked, while others remained blocked).

## 3. Changed-layer observations (supports the scoped claim)

### l4_frontend · attribution: `plausible` · Δt = 432h

**Event label**: `nine_offshore_vda_apps_removed_from_in_regional_storefronts`

**Timestamp**: `2024-01-15 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_legal`**
  - URL: <https://www.pib.gov.in/Pressreleaseshare.aspx?PRID=1991372>
  - Wayback: <https://web.archive.org/web/2024/https://www.pib.gov.in/Pressreleaseshare.aspx?PRID=1991372>
  > App-store regional removal of the nine offshore VDA apps from
> Apple App Store IN and Google Play IN in mid-January 2024
> implementing the FIU-IND / MEITY enforcement cascade.
> Attribution annotated plausible because the FIU-IND PIB press
> release is the load-bearing regulatory anchor but no archived
> app-store regional-availability snapshot has been pinned in
> this session. Replayable archive deferred.

### offramp_cex · attribution: `plausible` · Δt = 432h

**Event label**: `inr_rails_severed_for_in_users_of_named_offshore_vda_exchanges`

**Timestamp**: `2024-01-15 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_legal`**
  - URL: <https://www.pib.gov.in/Pressreleaseshare.aspx?PRID=1991372>
  - Wayback: <https://web.archive.org/web/2024/https://www.pib.gov.in/Pressreleaseshare.aspx?PRID=1991372>
  > INR on/off-ramp severance for Indian users of the nine named
> offshore VDA exchanges following the MEITY URL block and
> app-store regional removals. Attribution=plausible because
> the regulatory cascade is documented but no archived exchange
> corporate notice has been pinned. Wayback wildcard pointer
> in lieu of a pinned-timestamp snapshot.

## 5. Honest coverage gaps

- **l0_network** (`not_measured`): ISP-level blocking of nine offshore VDA exchange domains from Indian

## 7. Related events

- [`india-rbi-crypto-ban-2018`](./india-rbi-crypto-ban-2018.md)
- [`philippines-sec-binance-block-2024`](./philippines-sec-binance-block-2024.md)
- [`turkey-cbrt-crypto-ban-2021`](./turkey-cbrt-crypto-ban-2021.md)
- [`korea-travel-rule-2022`](./korea-travel-rule-2022.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `a331305`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

