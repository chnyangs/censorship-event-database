# Evidence chain — `shapeshift-mandatory-kyc-anonymity-end-2018-09`

**Status**: `admitted` · **Stratum**: `S5_corporate` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `80b0ca3` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-31` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "ShapeShift's 2018-09-04 mandatory-KYC membership scheme ended its anonymous
> no-account swap model, removing anonymous access to the ShapeShift swap/off-
> ramp; single-layer offramp_cex observed_change, attribution=plausible
> (Voorhees framed it as proactive, citing no enforcement-action trigger)."

## 1. Trigger

- **Type**: `corporate_policy_change`
- **Actor**: `shapeshift`
- **Timestamp**: `2018-09-04 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`semi_primary_wayback`**
  - URL: <https://bitcoinist.com/shapeshift-ends-anonymity-with-announcement-of-mandatory-kyc-data-collection/>
  - Wayback: <https://web.archive.org/web/20251017143246/https://bitcoinist.com/shapeshift-ends-anonymity-with-announcement-of-mandatory-kyc-data-collection/>
  - body_hash: `sha256:8ff6e8ad8917401286503df16e08cda75abcca2b55c81908969cfee155669b95`
  - body_path: `sources/http_captures/shapeshift-mandatory-kyc-anonymity-end-2018-09/primary/web.archive.org__web-20251017143246-https-bitcoinist.com-shapeshift-ends-anonymity-with-announcement-of-mandatory-kyc-data-collection__37ef4733b2.html`
  > Bitcoinist 2018-09: CEO Erik Voorhees announced on 2018-09-04 that all
> ShapeShift users would face mandatory KYC, packaged as a "membership"
> scheme — ending the pioneering "exchange without accounts" anonymous
> no-account swap model. Body grep-confirmed: "mandatory", "membership",
> "without accounts". Wayback 20251017143246 pinned.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `complete`
- **Actor name**: ShapeShift anonymous swap users
- **Chains**: `bitcoin`, `ethereum`

> Single class: ShapeShift's anonymous (no-account) swap users. The mandatory
> KYC membership scheme ended the no-account anonymous-swap model the platform
> pioneered, removing anonymous access to the ShapeShift off-ramp/swap surface
> globally.

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `plausible` · Δt = Noneh

**Event label**: `shapeshift_mandatory_kyc_ends_anonymous_swaps`

**Timestamp**: `2018-09-04 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`semi_primary_wayback`**
  - URL: <https://bitcoinist.com/shapeshift-ends-anonymity-with-announcement-of-mandatory-kyc-data-collection/>
  - Wayback: <https://web.archive.org/web/20251017143246/https://bitcoinist.com/shapeshift-ends-anonymity-with-announcement-of-mandatory-kyc-data-collection/>
  - body_hash: `sha256:8ff6e8ad8917401286503df16e08cda75abcca2b55c81908969cfee155669b95`
  - body_path: `sources/http_captures/shapeshift-mandatory-kyc-anonymity-end-2018-09/primary/web.archive.org__web-20251017143246-https-bitcoinist.com-shapeshift-ends-anonymity-with-announcement-of-mandatory-kyc-data-collection__37ef4733b2.html`
  > Bitcoinist 2018-09: Voorhees announced mandatory KYC membership,
> ending the "exchange without accounts" anonymous-swap model.
> attribution=plausible: the policy change is directly observed, but
> per Voorhees it was a proactive de-risking step "not added as a result
> of any enforcement action" — i.e. no specific named trigger, so the
> regulatory-compliance motive is contextual class-level inference (§1.1).
- **`semi_primary_wayback`**
  - URL: <https://www.coindesk.com/markets/2018/09/24/crypto-exchange-shapeshifts-ceo-says-move-to-collect-ids-was-proactive>
  - Wayback: <https://web.archive.org/web/20240812225720/https://www.coindesk.com/markets/2018/09/24/crypto-exchange-shapeshifts-ceo-says-move-to-collect-ids-was-proactive/>
  - body_hash: `sha256:8d0b5798555272ad7d9f991919ab1786f879d1558f5675096e2805fe66d58e06`
  - body_path: `sources/http_captures/shapeshift-mandatory-kyc-anonymity-end-2018-09/primary/web.archive.org__web-20240812225720-https-www.coindesk.com-markets-2018-09-24-crypto-exchange-shapeshifts-ceo-says-move-to-collect-ids-was-proactive__650b51aebe.html`
  > CoinDesk 2018-09-24: Voorhees says the move to collect IDs was
> "proactive," not the result of an enforcement action. Independent
> second semi-primary anchor; supports attribution=plausible (no named
> trigger). Body grep-confirmed: "proactive", "Voorhees".

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`consensys-metamask-infura-rpc-data-collection-2022-11`](./consensys-metamask-infura-rpc-data-collection-2022-11.md)
- [`kraken-monero-eu-delisting-2024`](./kraken-monero-eu-delisting-2024.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `80b0ca3`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

