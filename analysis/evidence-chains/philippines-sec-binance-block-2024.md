# Evidence chain — `philippines-sec-binance-block-2024`

**Status**: `admitted` · **Stratum**: `S4_nation_state` · **Shape**: `comparison` (2 changed layer(s): `l0_network`, `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `db44253` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-21` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T04:52:47Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "The 2024-03-25 Philippines NTC blocking order, following the 2023-11
> SEC Notice of Warning Against Binance, severed PH-vantage network access
> to binance.com / binance.org and closed Binance PHP peso on/off-ramps to
> Philippine users. Observational axes at l0_network (PH-ISP blocking) and
> offramp_cex (PHP rail closure). L0 admission-anchor-grade promotion
> pending OONI Probe PH / Censored Planet follow-up batch query."

## 1. Trigger

- **Type**: `nation_state_block`
- **Actor**: `PH_NTC`
- **Timestamp**: `2024-03-25 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://www.sec.gov.ph/notice-of-warning/notice-of-warning-against-binance/>
  - Wayback: <https://web.archive.org/web/2024/https://www.sec.gov.ph/notice-of-warning/notice-of-warning-against-binance/>
  > Philippines Securities and Exchange Commission (SEC) Notice of Warning
> Against Binance (issued 2023-11). The SEC declared that Binance was
> operating without proper licensing as a broker-dealer of securities in
> the Philippines and formally requested the National Telecommunications
> Commission (NTC) and Google Play / Apple App Store to block local
> access. Wayback wildcard pointer (web/2024/) is in lieu of a pinned-
> timestamp snapshot; evidence_use=contextual_unarchived because a
> body_hash+body_path pair has not been captured into
> sources/http_captures/philippines-sec-binance-block-2024/ in this
> session. Pinned archive deferred to follow-up authoring pass.
- **`semi_primary_wayback`**
  - URL: <https://www.gmanetwork.com/news/money/companies/901661/sec-formally-requests-ntc-to-block-binance-in-ph/story/>
  - Wayback: <https://web.archive.org/web/20240326182724/https://www.gmanetwork.com/news/money/companies/901661/sec-formally-requests-ntc-to-block-binance-in-ph/story/>
  - body_hash: `sha256:6e15b7585387cd53250a957d04616da64b80530622c2e8e61caa3c1974bd44a6`
  - body_path: `sources/http_captures/philippines-sec-binance-block-2024/primary/web.archive.org__web-20240326182724-https-www.gmanetwork.com-news-money-companies-901661-sec-formally-requests-ntc-to-block-binance-in-ph-story__e7790a2d2e.html`
  > GMA News coverage of the SEC's formal request to the NTC. The NTC
> block order was effective 2024-03-25; Philippine ISPs began blocking
> binance.com / binance.org access in late March 2024. Contextual
> anchor for the NTC blocking-effective date. Wayback wildcard
> pointer in lieu of pinned-timestamp snapshot.

## 2. Target

- **Kind**: `domain`
- **Enumeration**: `subset`
- **Actor name**: Binance (PH-vantage access)
- **Canonical domains**: `binance.com`, `binance.org`

> Binance global consumer domains (binance.com primary; binance.org secondary)
> as accessed from Philippine IP ranges. The target is the user-facing
> Binance web/app surface restricted via ISP-level DNS / TCP blocking under
> NTC order. App-store regional removal (Google Play / Apple App Store PH)
> is a sibling enforcement vector outside the scope of this admission.

## 3. Changed-layer observations (supports the scoped claim)

### l0_network · attribution: `plausible` · Δt = 358h

**Event label**: `ph_vantage_dns_blocking_of_binance_domain`

**Timestamp**: `?` (precision: `second`)

**Sources**:

- **`semi_primary_measurement`**
  - URL: <https://api.ooni.io/api/v1/measurements?probe_cc=PH&test_name=web_connectivity&input=https%3A%2F%2Fwww.binance.com%2F&since=2024-03-25&until=2024-04-25&limit=5>
  - body_hash: `sha256:84c5a6c569687491a273bf4e7a1ff3b1c402552e2d6ca0393908958eaa8c38dc`
  - body_path: `sources/http_captures/philippines-sec-binance-block-2024/v0_3_primary_repair/api.ooni.io__api-v1-measurements__80d9945fd5.json`
  > OONI PH web_connectivity query for https://www.binance.com/
> returns DNS-blocking anomaly rows on AS17639 (2024-04-24
> 07:23:45Z and 08:06:18Z) and AS9299 (2024-04-23
> 08:38:26Z). The same query includes non-anomalous PH rows
> on AS135582 and AS56099, so attribution is plausible and
> coverage is partially_measured rather than a universal PH
> blocking claim.
- **`semi_primary_measurement`**
  - URL: <https://api.ooni.io/api/v1/raw_measurement?measurement_uid=20240424080618.964439_PH_webconnectivity_3cf0c805db36e199>
  - body_hash: `sha256:c3094b9f18502864875a6c2cbb8f33846ce0e37513701d364584cd5b53e20b88`
  - body_path: `sources/http_captures/philippines-sec-binance-block-2024/v0_3_primary_repair/api.ooni.io__api-v1-raw_measurement__a9835d6578.json`
  > Raw OONI measurement body for AS17639. The measurement records
> `dns_nxdomain_error`, `dns_consistency=inconsistent`,
> `accessible=false`, and `blocking=dns` for
> https://www.binance.com/.
- **`semi_primary_measurement`**
  - URL: <https://api.ooni.io/api/v1/raw_measurement?measurement_uid=20240423083827.114575_PH_webconnectivity_24d659a5d6f91cd8>
  - body_hash: `sha256:8b8dee0c2ccda2c0325747932d780adff5d586e3e0edda80aaa82ae4eeb469fc`
  - body_path: `sources/http_captures/philippines-sec-binance-block-2024/v0_3_primary_repair/api.ooni.io__api-v1-raw_measurement__4fe39ba48a.json`
  > Raw OONI measurement body for AS9299. The measurement records
> `android_dns_cache_no_data`, `dns_consistency=inconsistent`,
> `accessible=false`, and `blocking=dns` for
> https://www.binance.com/.

### offramp_cex · attribution: `plausible` · Δt = 0h

**Event label**: `php_peso_onramp_offramp_closed_for_ph_users`

**Timestamp**: `2024-03-25 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`semi_primary_wayback`**
  - URL: <https://www.gmanetwork.com/news/money/companies/901661/sec-formally-requests-ntc-to-block-binance-in-ph/story/>
  - Wayback: <https://web.archive.org/web/20240326182724/https://www.gmanetwork.com/news/money/companies/901661/sec-formally-requests-ntc-to-block-binance-in-ph/story/>
  - body_hash: `sha256:6e15b7585387cd53250a957d04616da64b80530622c2e8e61caa3c1974bd44a6`
  - body_path: `sources/http_captures/philippines-sec-binance-block-2024/primary/web.archive.org__web-20240326182724-https-www.gmanetwork.com-news-money-companies-901661-sec-formally-requests-ntc-to-block-binance-in-ph-story__e7790a2d2e.html`
  > Binance PHP peso on/off-ramp closure to Philippine users
> following the NTC blocking order. Attribution annotated
> plausible because the supporting-journalism source documents
> the regulatory cascade but no archived Binance corporate
> notice has been pinned. Replayable Binance help-center /
> regional-notice archive deferred to follow-up authoring pass.
> Wayback wildcard pointer in lieu of a pinned-timestamp
> snapshot.
- **`semi_primary_measurement`**
  - URL: <https://api.ooni.io/api/v1/measurements?probe_cc=PH&test_name=web_connectivity&input=https%3A%2F%2Fwww.binance.com%2F&since=2024-03-25&until=2024-04-25&limit=5>
  - body_hash: `sha256:84c5a6c569687491a273bf4e7a1ff3b1c402552e2d6ca0393908958eaa8c38dc`
  - body_path: `sources/http_captures/philippines-sec-binance-block-2024/v0_3_primary_repair/api.ooni.io__api-v1-measurements__80d9945fd5.json`
  > OONI PH web_connectivity DNS-block measurement is the mechanism
> severing PH-user access to binance.com (and thus the PHP peso
> on/off-ramp). Independent semi-primary measurement anchor.

## 5. Honest coverage gaps

- **l4_frontend** (`not_measured`): Binance regional notices reportedly displayed to PH-located users

## 7. Related events

- [`india-rbi-crypto-ban-2018`](./india-rbi-crypto-ban-2018.md)
- [`turkey-cbrt-crypto-ban-2021`](./turkey-cbrt-crypto-ban-2021.md)
- [`korea-travel-rule-2022`](./korea-travel-rule-2022.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `db44253`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

