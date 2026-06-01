# Evidence chain — `fincen-eric-powers-p2p-exchanger-2019-04`

**Status**: `admitted` · **Stratum**: `S3_doj_sec_cftc_fiod` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `9494486` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-31` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T10:34:09Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "The 2019-04-18 FinCEN assessment against Eric Powers — its first-ever civil
> penalty against an individual peer-to-peer convertible-virtual-currency
> exchanger — imposed a civil money penalty (the $35,350 figure is set in the FinCEN assessment document, not restated on the captured page) and an industry bar prohibiting any
> money-services-business activity, terminating his P2P bitcoin exchange
> service. Effect carried at offramp_cex (off-ramp operator termination),
> attribution=direct. Comparable-main tier."

## 1. Trigger

- **Type**: `fincen_action`
- **Actor**: `US_FinCEN`
- **Timestamp**: `2019-04-18 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_government`**
  - URL: <https://web.archive.org/web/20190419000000/https://www.fincen.gov/news/news-releases/fincen-penalizes-peer-peer-virtual-currency-exchanger-violations-anti-money>
  - Wayback: <https://web.archive.org/web/20190418184452/https://www.fincen.gov/news/news-releases/fincen-penalizes-peer-peer-virtual-currency-exchanger-violations-anti-money>
  - body_hash: `sha256:e659ccd83ccf34bd79c7f6d13bc5f9ef638eae731d1643ada13ff9ea0c0e389c`
  - body_path: `sources/http_captures/fincen-eric-powers-p2p-exchanger-2019-04/primary/web.archive.org__web-20190419000000-https-www.fincen.gov-news-news-releases-fincen-penalizes-peer-peer-virtual-currency-exchanger-violations-anti-money__358b1c9f9a.html`
  > FinCEN news release (2019-04-18): "FinCEN Penalizes Peer-to-Peer
> Virtual Currency Exchanger for Violations of Anti-Money Laundering
> Laws." FinCEN assessed its first-ever civil money penalty against an
> individual peer-to-peer convertible-virtual-currency exchanger (Eric
> Powers) for willfully violating the Bank Secrecy Act's MSB
> registration, AML-program, and reporting (CTR/SAR) requirements. The
> action includes a $35,000 penalty AND an industry bar prohibiting
> Powers from engaging in any activity that would make him a money
> services business. First FinCEN enforcement against a P2P virtual-
> currency exchanger. Wayback memento 20190418184452 pinned; captured
> body contains "Eric Powers", "Peer-to-Peer", "exchanger", "Money
> Services Business", "industry bar", "registration".

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `complete`
- **Actor name**: Eric Powers
- **Chains**: `bitcoin`

> Eric Powers, an individual operating as a peer-to-peer exchanger of
> convertible virtual currency (bitcoin). Complete: the action names the
> single individual operator who is the entire target.

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `direct` · Δt = 0h

**Event label**: `fincen_industry_bar_terminates_p2p_bitcoin_exchanger`

**Timestamp**: `2019-04-18 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_government`**
  - URL: <https://web.archive.org/web/20190419000000/https://www.fincen.gov/news/news-releases/fincen-penalizes-peer-peer-virtual-currency-exchanger-violations-anti-money>
  - Wayback: <https://web.archive.org/web/20190418184452/https://www.fincen.gov/news/news-releases/fincen-penalizes-peer-peer-virtual-currency-exchanger-violations-anti-money>
  - body_hash: `sha256:e659ccd83ccf34bd79c7f6d13bc5f9ef638eae731d1643ada13ff9ea0c0e389c`
  - body_path: `sources/http_captures/fincen-eric-powers-p2p-exchanger-2019-04/primary/web.archive.org__web-20190419000000-https-www.fincen.gov-news-news-releases-fincen-penalizes-peer-peer-virtual-currency-exchanger-violations-anti-money__358b1c9f9a.html`
  > FinCEN news release (2019-04-18). attribution=direct: the FinCEN
> assessment is the operative instrument and names Eric Powers directly;
> the industry bar prohibits him from any MSB activity, terminating his
> P2P virtual-currency exchange service.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`liberty-reserve-coordinated-takedown-2013-05`](./liberty-reserve-coordinated-takedown-2013-05.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `9494486`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

