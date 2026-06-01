# Evidence chain — `thailand-sec-binance-bybit-c-and-d-2021`

**Status**: `admitted` · **Stratum**: `S4_nation_state` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `1a4f712` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-21` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T10:02:21Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "Thailand SEC criminal complaint filed 2021-07-02 against Binance
> with the Royal Thai Police Economic Crime Suppression Division (and
> the contemporaneous TH SEC unlicensed-operator enforcement posture
> extending to Bybit) under the Emergency Decree on Digital Asset
> Businesses Act B.E. 2561 produced a plausible-attribution
> constraint on the Thai THB on/off-ramp rails accessible via
> binance.com and bybit.com (offramp_cex load-bearing), without an
> accompanying regulator-directed L4-frontend disable order, L0
> network block, or on-chain asset freeze. The row does not claim a
> direct Thai-banking-rail severance directive from TH SEC."

## 1. Trigger

- **Type**: `regulatory_enforcement`
- **Actor**: `TH_SEC`
- **Timestamp**: `2021-07-02 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://www.sec.or.th/EN/Pages/News_Detail.aspx?SECID=9017>
  - Wayback: <https://web.archive.org/web/20210702090802/https://www.sec.or.th/EN/Pages/News_Detail.aspx?SECID=9017>
  - body_hash: `sha256:ccde39d696241c09db1794f3ad90c7203603d170f724379b43dd2b62f147fe77`
  - body_path: `sources/http_captures/thailand-sec-binance-bybit-c-and-d-2021/primary/web.archive.org__web-20210702090802-https-www.sec.or.th-EN-Pages-News_Detail.aspx__8f919efcf2.html`
  > Thailand Securities and Exchange Commission (TH SEC) news release
> dated 2021-07-02 announcing that the SEC has filed a criminal
> complaint against Binance with the Economic Crime Suppression
> Division (ECD) of the Royal Thai Police for operating a digital
> asset exchange business in Thailand without a licence in violation
> of the Emergency Decree on Digital Asset Businesses Act B.E. 2561
> (2018). The complaint follows an SEC warning letter dated
> 2021-04-05 that gave Binance a 15-day window to respond regarding
> unlicensed solicitation of the Thai public via binance.com and the
> Binance Thai Community Facebook page. Bybit is named in this
> record under the same TH SEC enforcement posture (TH SEC
> contemporaneous public warning list of unlicensed digital asset
> operators serving Thai residents); the analogous formal TH SEC
> criminal complaint against Bybit Fintech Limited was filed later
> (operative window starting 2022-01-25), recorded here as a
> cross-target subset because the user-anchored event scope binds
> Binance + Bybit under the 2021-07 TH SEC enforcement wave.
> Evidence repair 2026-06-01: TH SEC News_Detail SECID=9017 is
> locally captured from Wayback memento 20210702090802 with
> body_hash/body_path, so it is claim-usable for the Binance
> criminal-complaint trigger. It does not independently prove a
> direct TH SEC banking-rail severance directive.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: Binance Holdings Ltd. (TH cohort) + Bybit Fintech Limited (TH cohort)
- **Canonical domains**: `binance.com`, `bybit.com`

> Binance group entities (binance.com global platform and the Binance
> Thai Community Facebook page solicitation channel) serving Thai
> retail customers, plus Bybit (bybit.com) under the same TH SEC
> enforcement posture for operating a digital asset exchange business
> without a Thai licence per Emergency Decree on Digital Asset
> Businesses Act B.E. 2561. enumeration=subset because (a) the named
> TH SEC criminal complaint of 2021-07-02 is addressed to Binance
> specifically, with Bybit included here as a class-level
> cross-target on the basis of the TH SEC public-warning posture
> against unlicensed operators serving Thai residents (the formal
> TH SEC criminal complaint against Bybit Fintech Limited was filed
> later, operative window 2022-01-25), and (b) only the two
> user-anchored target entities are enumerated; the broader TH SEC
> investor-alert universe of unlicensed digital-asset operators
> serving Thai residents is class-level context, not enumerated here.

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `plausible` · Δt = 0h

**Event label**: `th_thb_rail_constraint_under_th_sec_unlicensed_status`

**Timestamp**: `2021-07-02 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_legal`**
  - URL: <https://www.sec.or.th/EN/Pages/News_Detail.aspx?SECID=9017>
  - Wayback: <https://web.archive.org/web/20210702090802/https://www.sec.or.th/EN/Pages/News_Detail.aspx?SECID=9017>
  - body_hash: `sha256:ccde39d696241c09db1794f3ad90c7203603d170f724379b43dd2b62f147fe77`
  - body_path: `sources/http_captures/thailand-sec-binance-bybit-c-and-d-2021/primary/web.archive.org__web-20210702090802-https-www.sec.or.th-EN-Pages-News_Detail.aspx__8f919efcf2.html`
  > TH SEC News_Detail SECID=9017 (2021-07-02) is the legal
> anchor naming Binance as the addressee of the criminal
> complaint filed with the Royal Thai Police ECD for unlicensed
> digital-asset-exchange operations under the Emergency Decree
> on Digital Asset Businesses Act B.E. 2561. attribution=
> plausible (not direct) because the rail constraint is a
> downstream consequence of the unlicensed-status finding
> rather than a TH SEC banking-prohibition directive to Thai
> banks (TH SEC does not have direct banking-prohibition
> authority over Thai retail banks; the cascade is via
> Binance / Bybit operator-side compliance posture and Thai
> retail customer risk-perception update following the public
> criminal complaint). The local Wayback body_hash/body_path
> capture makes this a claim-usable legal anchor for the
> regulator action, but operator-side Binance-TH / Bybit-TH
> THB-rail notices remain unpinned.
- **`semi_primary_wayback`**
  - URL: <https://www.coindesk.com/markets/2021/07/02/thailand-sec-files-criminal-complaint-against-binance>
  - Wayback: <https://web.archive.org/web/20210916230514/https://www.coindesk.com/markets/2021/07/02/thailand-sec-files-criminal-complaint-against-binance>
  - body_hash: `sha256:a6dc09bc43c53c367f358a6a2c7f6fa8c000ec344a3e104af09063d974429b81`
  - body_path: `sources/http_captures/thailand-sec-binance-bybit-c-and-d-2021/primary/web.archive.org__web-20210916230514-https-www.coindesk.com-markets-2021-07-02-thailand-sec-files-criminal-complaint-against-binance__7c956e0ae9.html`
  > Coindesk 2021-07-02 reporting corroborates the TH SEC's
> criminal-complaint anchor and the unlicensed-operator
> framing (15-day SEC warning issued 2021-04-05; Binance
> failed to respond within the deadline; complaint then filed
> with the Royal Thai Police ECD). Locally captured from
> Wayback memento 20210916230514 with body_hash/body_path.
- **`supporting_journalism`**
  - URL: <https://www.bangkokpost.com/business/2142503/sec-files-criminal-complaint-against-binance>
  - Wayback: <https://web.archive.org/web/2021/https://www.bangkokpost.com/business/2142503/sec-files-criminal-complaint-against-binance>
  > Bangkok Post 2021-07-02 reporting same-day-of-record on the
> TH SEC criminal complaint against Binance, useful as Thai
> domestic-press corroboration. DRYRUN: contextual unarchived
> pending pinned Wayback capture.

## 5. Honest coverage gaps

- **l0_network** (`not_measured`): TH SEC criminal complaint is a regulator-directed legal-process
- **l4_frontend** (`not_measured`): No regulator-directed disable order on the binance.com or

## 7. Related events

- [`malaysia-sc-binance-disable-2021`](./malaysia-sc-binance-disable-2021.md)
- [`singapore-mas-binance-services-2021`](./singapore-mas-binance-services-2021.md)
- [`thailand-bot-bitcoin-prohibition-2013`](./thailand-bot-bitcoin-prohibition-2013.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `1a4f712`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

