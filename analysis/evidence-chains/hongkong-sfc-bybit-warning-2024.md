# Evidence chain — `hongkong-sfc-bybit-warning-2024`

**Status**: `admitted` · **Stratum**: `S4_nation_state` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-02` · **Source commit**: `3a48c00` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-21` · **Tool version**: `0.1.0` · **Generated**: `2026-06-02T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> *(no scoped_claim recorded — event not paper-ready)*

## 1. Trigger

- **Type**: `regulatory_enforcement`
- **Actor**: `HK_SFC`
- **Timestamp**: `2024-03-14 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://apps.sfc.hk/edistributionWeb/api/news/list-content?refNo=24PR47&lang=EN>
  - Wayback: <https://web.archive.org/web/2024/https://apps.sfc.hk/edistributionWeb/api/news/list-content?refNo=24PR47&lang=EN>
  > Hong Kong Securities and Futures Commission (SFC) press release
> 24PR47 "SFC warns public against unlicensed virtual asset
> trading platform Bybit", dated 2024-03-14. The SFC publicly
> warned that no entity in the Bybit group is licensed by or
> registered with the SFC to conduct any regulated activity in
> Hong Kong, and that Bybit's crypto-related products (including
> Bybit Futures Contracts, Inverse Futures Contracts, options,
> leveraged tokens, and Bybit Wealth Management) have been
> offered to HK investors without authorisation. Bybit was added
> to the SFC Suspicious Virtual Asset Trading Platforms Alert
> List and its products to the Suspicious Investment Products
> Alert List on the same day.
- **`supporting_journalism`**
  - URL: <https://www.coindesk.com/policy/2024/03/14/hong-kongs-markets-regulator-issues-warning-against-crypto-exchange-bybit>
  - Wayback: <https://web.archive.org/web/2024/https://www.coindesk.com/policy/2024/03/14/hong-kongs-markets-regulator-issues-warning-against-crypto-exchange-bybit>
  > CoinDesk 2024-03-14 reporting on the SFC public warning against
> Bybit and the addition to the Suspicious VATP Alert List;
> contextualises Bybit's pending Hong Kong VATP licence
> application (filed February 2024 via Spark Fintech Limited).
- **`supporting_journalism`**
  - URL: <https://www.blockhead.co/2024/03/18/hong-kong-regulator-warns-public-against-bybit-adds-it-to-suspicious-vatp-list/>
  - Wayback: <https://web.archive.org/web/2024/https://www.blockhead.co/2024/03/18/hong-kong-regulator-warns-public-against-bybit-adds-it-to-suspicious-vatp-list/>
  > Blockhead summary of the SFC Bybit warning and Suspicious VATP
> Alert List listing; corroborates the enumerated product list
> (futures, inverse futures, options, leveraged tokens, wealth
> management) the SFC flagged as offered to HK investors.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: Bybit
- **Canonical domains**: `bybit.com`

> Subset enumeration: Bybit is the named enforcement target of the
> SFC 2024-03-14 public warning and the Suspicious VATP Alert List
> listing. The named Bybit group entity covered by the warning is
> not exhaustively enumerated by the SFC release (the SFC refers to
> "the Bybit group" generically); Bybit's HK licence applicant
> Spark Fintech Limited (February 2024 VATP application) is the
> related corporate vehicle. The full universe of unlicensed VATPs
> marketing to HK is broader; this event records the Bybit-specific
> slice. Bybit's subsequent full HK exit / VATP-licence-application
> withdrawal (later in 2024) is a downstream event outside this
> row's scope.

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `plausible` · Δt = 0h

**Event label**: `bybit_unlicensed_vatp_public_warning_and_alert_list_listing`

**Timestamp**: `2024-03-14 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_legal`**
  - URL: <https://apps.sfc.hk/edistributionWeb/api/news/list-content?refNo=24PR47&lang=EN>
  - Wayback: <https://web.archive.org/web/2024/https://apps.sfc.hk/edistributionWeb/api/news/list-content?refNo=24PR47&lang=EN>
  > SFC press release 24PR47 "SFC warns public against unlicensed
> virtual asset trading platform Bybit" 2024-03-14 — the named
> public warning that anchors the offramp restriction.
- **`semi_primary_wayback`**
  - URL: <https://www.coindesk.com/policy/2024/03/14/hong-kongs-markets-regulator-issues-warning-against-crypto-exchange-bybit>
  - Wayback: <https://web.archive.org/web/20240314130925/https://www.coindesk.com/policy/2024/03/14/hong-kongs-markets-regulator-issues-warning-against-crypto-exchange-bybit>
  - body_hash: `sha256:e6295170e2cde625d3dd02adfd12b77fb26a3752ec9acf1fc2ef7c04ad119b60`
  - body_path: `sources/http_captures/hongkong-sfc-bybit-warning-2024/primary/web.archive.org__web-20240314130925-https-www.coindesk.com-policy-2024-03-14-hong-kongs-markets-regulator-issues-warning-against-crypto-exchange-bybit__823e677f5e.html`
  > CoinDesk 2024-03-14 reporting confirming the SFC warning and
> alert-list listing. Independent semi-primary anchor 1 of 2.
- **`semi_primary_wayback`**
  - URL: <https://www.blockhead.co/2024/03/18/hong-kong-regulator-warns-public-against-bybit-adds-it-to-suspicious-vatp-list/>
  - Wayback: <https://web.archive.org/web/20240416205311/https://www.blockhead.co/2024/03/18/hong-kong-regulator-warns-public-against-bybit-adds-it-to-suspicious-vatp-list/>
  - body_hash: `sha256:19a333207433aa3934bbbaa594f510061ee15880bfe91504dc89b908dcd4a492`
  - body_path: `sources/http_captures/hongkong-sfc-bybit-warning-2024/primary/web.archive.org__web-20240416205311-https-www.blockhead.co-2024-03-18-hong-kong-regulator-warns-public-against-bybit-adds-it-to-suspicious-vatp-list__30a5e1bf53.html`
  > Blockhead 2024-03-18 reporting on the SFC Bybit warning +
> Suspicious VATP listing. Independent semi-primary anchor 2 of 2.
- **`supporting_journalism`**
  - URL: <https://dailycoin.com/hong-kong-flags-bybit-as-suspicious-on-warning-list/>
  - Wayback: <https://web.archive.org/web/2024/https://dailycoin.com/hong-kong-flags-bybit-as-suspicious-on-warning-list/>
  > Dailycoin reporting on the SFC Bybit Suspicious VATP listing
> situating it within the broader 2024 HK enforcement cleanse
> (parallel to the post-JPEX SFC posture).

## 4. No-change observations (where applicable)

### l4_frontend — `bybit_hk_frontend_no_immediate_block_post_sfc_warning`

**Window**: `2024-03-14 00:00:00+00:00` → `2024-03-31 23:59:59+00:00`

**Sources**:

- **`semi_primary_wayback`**
  - URL: <https://www.coindesk.com/policy/2024/03/14/hong-kongs-markets-regulator-issues-warning-against-crypto-exchange-bybit>
  - Wayback: <https://web.archive.org/web/20240314130925/https://www.coindesk.com/policy/2024/03/14/hong-kongs-markets-regulator-issues-warning-against-crypto-exchange-bybit>
  - body_hash: `sha256:e6295170e2cde625d3dd02adfd12b77fb26a3752ec9acf1fc2ef7c04ad119b60`
  - body_path: `sources/http_captures/hongkong-sfc-bybit-warning-2024/primary/web.archive.org__web-20240314130925-https-www.coindesk.com-policy-2024-03-14-hong-kongs-markets-regulator-issues-warning-against-crypto-exchange-bybit__823e677f5e.html`
  > CoinDesk reporting confirms no immediate Bybit HK frontend
> block in the post-warning window. Semi-primary anchor 1 of 2.
- **`semi_primary_wayback`**
  - URL: <https://www.blockhead.co/2024/03/18/hong-kong-regulator-warns-public-against-bybit-adds-it-to-suspicious-vatp-list/>
  - Wayback: <https://web.archive.org/web/20240416205311/https://www.blockhead.co/2024/03/18/hong-kong-regulator-warns-public-against-bybit-adds-it-to-suspicious-vatp-list/>
  - body_hash: `sha256:19a333207433aa3934bbbaa594f510061ee15880bfe91504dc89b908dcd4a492`
  - body_path: `sources/http_captures/hongkong-sfc-bybit-warning-2024/primary/web.archive.org__web-20240416205311-https-www.blockhead.co-2024-03-18-hong-kong-regulator-warns-public-against-bybit-adds-it-to-suspicious-vatp-list__30a5e1bf53.html`
  > Blockhead reporting corroborates the no-immediate-block
> frontend posture. Semi-primary anchor 2 of 2.
- **`supporting_journalism`**
  - URL: <https://blockchain.news/news/breaking-bybit-receives-unlicensed-operation-warning-from-hk-sfc>
  - Wayback: <https://web.archive.org/web/2024/https://blockchain.news/news/breaking-bybit-receives-unlicensed-operation-warning-from-hk-sfc>
  > Blockchain.News reporting on the SFC Bybit warning;
> describes the regulator-side action but does not document
> a Bybit-side HK frontend block in the immediate post-warning
> window.
- **`supporting_journalism`**
  - URL: <https://www.charltonslaw.com/sfc-warns-unlicensed-crypto-exchanges-of-legal-consequences/>
  - Wayback: <https://web.archive.org/web/2024/https://www.charltonslaw.com/sfc-warns-unlicensed-crypto-exchanges-of-legal-consequences/>
  > Charltons Law summary of the SFC 2024 posture toward
> unlicensed VATPs including Bybit; contextualises the
> enforcement chain leading to Bybit's later HK exit.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`hongkong-sfc-jpex-block-2023`](./hongkong-sfc-jpex-block-2023.md)
- [`hongkong-sfc-vatp-licensing-2023-06`](./hongkong-sfc-vatp-licensing-2023-06.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `3a48c00`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

