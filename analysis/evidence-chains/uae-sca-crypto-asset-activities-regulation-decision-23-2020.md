# Evidence chain — `uae-sca-crypto-asset-activities-regulation-decision-23-2020`

**Status**: `admitted` · **Stratum**: `S4_nation_state` · **Shape**: `null_event` (0 changed layer(s): none) · **Tier**: `null_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `a9689fa` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-31` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "The UAE SCA issued Decision No. 23/RM of 2020 (dated 01 November 2020) Concerning
> Crypto Assets Activities Regulation, establishing a federal onshore licensing/
> approval perimeter over crypto-asset offering, issuance, listing, trading, and
> custody in the UAE outside the financial free zones. The row does not claim any
> specific onshore-UAE VASP delisting cascade, on-chain freeze, or frontend takedown
> at issuance; it documents the federal licensing-framework trigger as a null_event,
> distinct from the Dubai-emirate VARA regime and the free-zone frameworks."

## 1. Trigger

- **Type**: `regulatory_enforcement`
- **Actor**: `AE_SCA`
- **Timestamp**: `2020-11-01 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`semi_primary_wayback`**
  - URL: <https://www.charlesrussellspeechlys.com/en/insights/expert-insights/dispute-resolution/2024/in-depth-virtual-currency-regulation-uae/>
  - Wayback: <https://web.archive.org/web/20260129211800/https://www.charlesrussellspeechlys.com/en/insights/expert-insights/dispute-resolution/2024/in-depth-virtual-currency-regulation-uae/>
  - body_hash: `sha256:7419b8504a3f78de213106fd0ba6e889ac0cbee0d8f15ac2c3f47bd5b1462b41`
  - body_path: `sources/http_captures/uae-sca-crypto-asset-activities-regulation-decision-23-2020/primary/web.archive.org__web-20260129211800-https-www.charlesrussellspeechlys.com-en-insights-expert-insights-dispute-resolution-2024-in-depth-virtual-currency-regulation-uae__04e52f3b3a.html`
  > Charles Russell Speechlys "In-Depth Virtual Currency Regulation: United Arab
> Emirates". Captured page states verbatim: "The SCA passed Decision No. 23 of
> 2020 Concerning Crypto Assets Activities Regulation (the SCA Virtual Asset
> Regulation)". Confirms the SCA (Securities and Commodities Authority) federal
> onshore licensing instrument over crypto-asset activities (and that it was
> later superseded by SCA Decisions 26/RM and 27/RM of 2023).
- **`semi_primary_wayback`**
  - URL: <https://galadarilaw.com/news/crypto-asset-regulation-in-the-united-arab-emirates/>
  - Wayback: <https://web.archive.org/web/20241014062220/https://galadarilaw.com/news/crypto-asset-regulation-in-the-united-arab-emirates/>
  - body_hash: `sha256:8b4b05df66b27ed54f9c2145e8cff0f1e2dafe8575eb2a3e97482f70fa80bc4a`
  - body_path: `sources/http_captures/uae-sca-crypto-asset-activities-regulation-decision-23-2020/primary/web.archive.org__web-20241014062220-https-galadarilaw.com-news-crypto-asset-regulation-in-the-united-arab-emirates__6391afc9b6.html`
  > Galadari Law "Crypto Asset Regulation in the United Arab Emirates". Captured
> page states: "the Chairman of the Authority's Board of Directors' Decision
> No. 23 of 2020 concerning Crypto Assets Activities Regulation (Regulation)
> was published" (in 2020). Confirms the Decision number, year, and that it
> imposes an SCA licensing/approval requirement over crypto-asset offering,
> issuance, listing, and trading in onshore UAE (outside the financial free
> zones).

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: UAE onshore crypto-asset service providers (class)

> Class-level subset: all persons/entities offering, issuing, listing, trading,
> or providing custody and related services for crypto assets in onshore UAE
> (outside the ADGM/DIFC financial free zones) — required to obtain SCA approval/
> licensing. No address-level enumeration; this is a federal onshore licensing
> perimeter over the crypto-service class.

## 3. Changed-layer observations (supports the scoped claim)

*No observed_change entries. This is a `null_event`; see §4 for observed_no_change evidence supporting the null claim.*

## 4. No-change observations (where applicable)

### offramp_cex — `sca_federal_crypto_licensing_framework_issued_no_immediate_cascade`

**Window**: `2020-11-01 00:00:00+00:00` → `2021-06-30 23:59:59+00:00`

**Sources**:

- **`semi_primary_wayback`**
  - URL: <https://www.charlesrussellspeechlys.com/en/insights/expert-insights/dispute-resolution/2024/in-depth-virtual-currency-regulation-uae/>
  - Wayback: <https://web.archive.org/web/20260129211800/https://www.charlesrussellspeechlys.com/en/insights/expert-insights/dispute-resolution/2024/in-depth-virtual-currency-regulation-uae/>
  - body_hash: `sha256:7419b8504a3f78de213106fd0ba6e889ac0cbee0d8f15ac2c3f47bd5b1462b41`
  - body_path: `sources/http_captures/uae-sca-crypto-asset-activities-regulation-decision-23-2020/primary/web.archive.org__web-20260129211800-https-www.charlesrussellspeechlys.com-en-insights-expert-insights-dispute-resolution-2024-in-depth-virtual-currency-regulation-uae__04e52f3b3a.html`
  > observed_no_change with attribution=none: SCA Decision 23/2020 establishes
> the federal onshore crypto-licensing perimeter but does not by itself
> produce a measurable onshore-UAE VASP delisting cascade in the issuance
> window — it is an enabling-with-licensing framework. Same null coding
> pattern as uae-vara-licence-issuance-regime-2023.
- **`semi_primary_wayback`**
  - URL: <https://galadarilaw.com/news/crypto-asset-regulation-in-the-united-arab-emirates/>
  - Wayback: <https://web.archive.org/web/20241014062220/https://galadarilaw.com/news/crypto-asset-regulation-in-the-united-arab-emirates/>
  - body_hash: `sha256:8b4b05df66b27ed54f9c2145e8cff0f1e2dafe8575eb2a3e97482f70fa80bc4a`
  - body_path: `sources/http_captures/uae-sca-crypto-asset-activities-regulation-decision-23-2020/primary/web.archive.org__web-20241014062220-https-galadarilaw.com-news-crypto-asset-regulation-in-the-united-arab-emirates__6391afc9b6.html`
  > Companion legal explainer confirming Decision 23/2020 imposes an SCA
> approval/licensing requirement over onshore crypto-asset activities;
> supports the enabling-with-licensing (null_event) reading.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`uae-vara-licence-issuance-regime-2023`](./uae-vara-licence-issuance-regime-2023.md)
- [`qatar-qcb-qfcra-virtual-asset-ban-2019-12`](./qatar-qcb-qfcra-virtual-asset-ban-2019-12.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `a9689fa`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

