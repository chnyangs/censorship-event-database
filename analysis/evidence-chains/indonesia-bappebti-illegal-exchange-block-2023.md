# Evidence chain — `indonesia-bappebti-illegal-exchange-block-2023`

**Status**: `admitted` · **Stratum**: `S4_nation_state` · **Shape**: `comparison` (2 changed layer(s): `l4_frontend`, `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-02` · **Source commit**: `3f1a9f2` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-21` · **Tool version**: `0.1.0` · **Generated**: `2026-06-02T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "BAPPEBTI's 2023-04-21 enforcement wave, routed via Kominfo ISP-level
> domain blocking, directly compelled Indonesian-geo unreachability of
> unlicensed offshore crypto-exchange frontends (binance.com, bybit.com,
> okx.com, kucoin.com, mexc.com) under BAPPEBTI Regulation No. 8/2021
> Article 5 (CPFAK licensing requirement), producing an L4 frontend
> observed_change (attribution=direct) with cascading IDR on/off-ramp
> severance at the named offshore-CEX cohort (offramp_cex
> attribution=plausible because the rail severance is downstream of the
> frontend block rather than a direct banking-prohibition directive).
> The row does not claim L0 network-level connectivity measurement (no
> OONI / Censored Planet slice captured this session; per Kazakhstan
> honesty rule l0_network is `not_measured`), nor on-chain asset freeze,
> nor banking-rail prohibition on Indonesian banks."

## 1. Trigger

- **Type**: `nation_state_block`
- **Actor**: `ID_BAPPEBTI`
- **Timestamp**: `2023-04-21 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://bappebti.go.id/>
  - Wayback: <https://web.archive.org/web/2023/https://bappebti.go.id/>
  > BAPPEBTI (Badan Pengawas Perdagangan Berjangka Komoditi / Commodity
> Futures Trading Regulatory Agency) coordinated enforcement action
> with Kominfo (Ministry of Communication and Informatics) blocking
> web/app access to foreign cryptocurrency exchanges that operate
> without a BAPPEBTI license to conduct physical crypto asset
> trading in Indonesia, including binance.com, bybit.com, okx.com,
> kucoin.com, mexc.com, and others. Legal basis: BAPPEBTI Regulation
> No. 8 of 2021 (as amended by Regulation No. 13 of 2022), Article
> 5, restricting Indonesian physical crypto market trading to
> BAPPEBTI-licensed (CPFAK) traders. Indonesian users must use
> BAPPEBTI-licensed local exchanges (Tokocrypto, Indodax, et al.).
> DRYRUN: pinned snapshot timestamp and body_hash capture deferred
> to non-DRYRUN release; the 2023-04-21 day-level anchor approximates
> BAPPEBTI's mid-2023 PASTI Task Force enforcement wave reported in
> Indonesian press (detik.com "Ratusan Exchanger Kripto 'Nakal'
> Diblokir Kominfo" wave) and follows the July 2022 binance.com PSE
> block precedent. Wayback anchor is a 2023-calendar-folder pointer
> at bappebti.go.id; pinned snapshot timestamp / body_hash capture
> deferred to human audit. evidence_use=contextual_unarchived per
> validator policy.
- **`supporting_journalism`**
  - URL: <https://inet.detik.com/law-and-policy/d-6685046/ratusan-exchanger-kripto-nakal-diblokir-kominfo>
  - Wayback: <https://web.archive.org/web/2023/https://inet.detik.com/law-and-policy/d-6685046/ratusan-exchanger-kripto-nakal-diblokir-kominfo>
  > detik.com reporting on the BAPPEBTI-Kominfo coordinated block of
> hundreds of unlicensed foreign crypto exchanges in Indonesia (2023
> enforcement wave). DRYRUN: 2023-calendar-folder Wayback pointer;
> pinned snapshot deferred to human audit.
- **`supporting_journalism`**
  - URL: <https://kumparan.com/kumparanbisnis/bappebti-gandeng-kominfo-blokir-platform-kripto-luar-negeri-239TA5gFYDn>
  - Wayback: <https://web.archive.org/web/2023/https://kumparan.com/kumparanbisnis/bappebti-gandeng-kominfo-blokir-platform-kripto-luar-negeri-239TA5gFYDn>
  > Kumparan reporting on BAPPEBTI partnering with Kominfo to block
> foreign crypto platforms operating without BAPPEBTI registration.
> DRYRUN: 2023-calendar-folder Wayback pointer; pinned snapshot
> deferred to human audit.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: Foreign unlicensed crypto exchanges (ID cohort)
- **Canonical domains**: `binance.com`, `bybit.com`, `okx.com`, `kucoin.com`, `mexc.com`

> Class of foreign (offshore) cryptocurrency exchanges operating without
> BAPPEBTI CPFAK licensing in Indonesia. Named exemplars per BAPPEBTI/
> Kominfo press cycle and follow-on enforcement: Binance (binance.com),
> Bybit (bybit.com), OKX (okx.com), KuCoin (kucoin.com), MEXC (mexc.com).
> Subset enumeration: BAPPEBTI's enforcement targets the unlicensed-
> foreign-exchange class as a whole (hundreds of entities per detik.com
> reporting); the named exemplars are the largest by Indonesian user
> base. Indonesian users channeled to BAPPEBTI-licensed domestic
> exchanges (Tokocrypto, Indodax).

## 3. Changed-layer observations (supports the scoped claim)

### l4_frontend · attribution: `direct` · Δt = 0h

**Event label**: `offshore_cex_frontends_blocked_id_via_kominfo`

**Timestamp**: `2023-04-21 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_legal`**
  - URL: <https://bappebti.go.id/>
  - Wayback: <https://web.archive.org/web/20230128094038/https://bappebti.go.id/>
  - body_hash: `sha256:e01b8550f8c09ad60f34ad155707003fc2b680ccfa95520e670397acd2f0bca1`
  - body_path: `sources/http_captures/indonesia-bappebti-illegal-exchange-block-2023/primary/web.archive.org__web-20230128094038-https-bappebti.go.id__3e3508bf50.html`
  > BAPPEBTI enforcement order (operationalized via Kominfo ISP-
> level domain blocking) is the legal instrument compelling the
> Indonesian-geo unreachability of the named offshore-CEX
> frontends. attribution=direct because the BAPPEBTI order names
> the unlicensed-foreign-exchange class as the addressee and the
> Kominfo routing is the operative state-change instrument.
> DRYRUN: 2023-calendar-folder Wayback pointer; pinned Wayback /
> body_hash anchors for BAPPEBTI press release enumerating the
> blocked domains deferred to human audit.
- **`semi_primary_wayback`**
  - URL: <https://inet.detik.com/law-and-policy/d-6685046/ratusan-exchanger-kripto-nakal-diblokir-kominfo>
  - Wayback: <https://web.archive.org/web/20230425201141/https://inet.detik.com/law-and-policy/d-6685046/ratusan-exchanger-kripto-nakal-diblokir-kominfo>
  - body_hash: `sha256:d74c0ed2a12a34bb21882eb4a859c0c09c2106209917804268f41071ac4af59b`
  - body_path: `sources/http_captures/indonesia-bappebti-illegal-exchange-block-2023/primary/web.archive.org__web-20230425201141-https-inet.detik.com-law-and-policy-d-6685046-ratusan-exchanger-kripto-nakal-diblokir-kominfo__48f00e04c6.html`
  > detik.com reporting (published 2023-04-21) confirms Kominfo's
> coordinated block of hundreds of unlicensed crypto exchangers
> (incl. Binance) per BAPPEBTI request. This is the verifiable,
> memento-backed April 2023 enforcement wave the event is
> re-scoped to; Wayback 20230425201141 pinned.

### offramp_cex · attribution: `plausible` · Δt = 0h

**Event label**: `offshore_cex_idr_rail_severance_cascade`

**Timestamp**: `2023-04-21 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_legal`**
  - URL: <https://bappebti.go.id/>
  - Wayback: <https://web.archive.org/web/20230128094038/https://bappebti.go.id/>
  - body_hash: `sha256:e01b8550f8c09ad60f34ad155707003fc2b680ccfa95520e670397acd2f0bca1`
  - body_path: `sources/http_captures/indonesia-bappebti-illegal-exchange-block-2023/primary/web.archive.org__web-20230128094038-https-bappebti.go.id__3e3508bf50.html`
  > BAPPEBTI-Kominfo block cascades into IDR-rail severance at the
> offshore-CEX cohort because the blocked frontends are the
> access path through which Indonesian retail customers used the
> foreign CEXs' IDR P2P / card / bank deposit channels.
> attribution=plausible because the offramp severance is a
> downstream consequence of the frontend block rather than a
> direct BAPPEBTI-mandated banking-rail prohibition on Indonesian
> banks (BAPPEBTI's authority runs through commodity-futures
> licensing, not direct banking prohibition; cascade is via the
> unlicensed-exchange enforcement rather than a Bank-Indonesia
> banking-prohibition directive). DRYRUN: 2023-calendar-folder
> Wayback pointer; pinned anchors for offshore-CEX IDR-rail
> withdrawal flow deferred to human audit.

## 5. Honest coverage gaps

- **l0_network** (`not_measured`): BAPPEBTI-Kominfo block is routed via Kominfo ISP-level domain

## 7. Related events

- [`malaysia-sc-binance-disable-2021`](./malaysia-sc-binance-disable-2021.md)
- [`india-rbi-crypto-ban-2018`](./india-rbi-crypto-ban-2018.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `3f1a9f2`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

