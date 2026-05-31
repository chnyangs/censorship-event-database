# Evidence chain — `uniswap-tokenized-stocks-delisting-2021-07`

**Status**: `admitted` · **Stratum**: `S5_corporate` · **Shape**: `comparison` (1 changed layer(s): `l4_frontend`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `a9689fa` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-21` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "Uniswap Labs' 2021-07-23 restriction of approximately 100
> tokenized-equity / option / synthetic-equity tokens from the
> app.uniswap.org frontend UI — taken preemptively, with no SEC
> enforcement instrument issued at that date and without
> corresponding action at the Uniswap Protocol smart-contract layer
> — documents the 2021 antecedent of the 2023 sibling
> uniswap-frontend-delisting-2023 and the cleanest 2021 example in
> the dataset of an L4-only frontend-operator compliance action
> taken in anticipation of (not in reaction to) US
> securities-enforcement pressure."

## 1. Trigger

- **Type**: `corporate_policy_change`
- **Actor**: `uniswap_labs`
- **Timestamp**: `2021-07-23 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_corporate`**
  - URL: <https://app.uniswap.org>
  - Wayback: <https://web.archive.org/web/2021/https://app.uniswap.org>
  > Uniswap Labs operates app.uniswap.org. On 2021-07-23 the frontend
> operator announced that approximately 100 tokens — predominantly
> tokenized-equity exposures (e.g., Mirror Protocol "mAsset" stocks
> such as mTSLA / mAAPL / mAMZN, Synthetix "synthetic equity"
> sAsset pairs), tokenized-option products (Opyn / Hegic style
> option tokens), index / derivative wraps, and insurance-related
> token instruments deemed to have securities-law exposure — would
> no longer be surfaced in the Uniswap-Labs-operated frontend at
> app.uniswap.org. The Uniswap Protocol smart contracts (v2 / v3)
> and the underlying pools remained autonomous and permissionless;
> the action was a frontend token-list filter only. Marked
> evidence_use=contextual_unarchived because in this DRYRUN the
> authoring LLM agent did not personally pin a Wayback snapshot
> timestamp or compute a body_hash of the 2021-07-23 announcement
> copy; the Uniswap-Labs domain is the canonical corporate anchor
> and is routinely captured by Wayback through 2021, but the
> precise announcement page / blog body must be re-anchored
> during human audit before this citation may serve as an
> admission anchor in its own right.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Protocol**: `uniswap_v2_v3`
- **Actor name**: Uniswap Labs (frontend operator, app.uniswap.org)
- **Chains**: `ethereum`
- **Canonical domains**: `app.uniswap.org`

> Approximately 100 tokens removed from the Uniswap Labs-operated
> frontend at app.uniswap.org on 2021-07-23. Named cohorts per
> contemporaneous coverage: Mirror Protocol tokenized-stock "mAssets"
> (mTSLA, mAAPL, mAMZN, mGOOGL, mNFLX, etc.), Synthetix "synthetic
> equity" sAssets (sTSLA, sAAPL, sCOIN, etc.), tokenized-option
> products (Opyn / Hegic option tokens), tokenized-index and
> derivative-wrap instruments, and insurance-related token
> instruments deemed by Uniswap Labs to have potential securities-law
> exposure. enumeration=subset because the full restricted token-list
> diff (against the @uniswap/default-token-list at the relevant
> commit) was not enumerated in the public announcement and must be
> reconstructed by diffing the GitHub repo commit history during
> human audit. Target is the Uniswap Labs frontend operator (the
> entity that controls app.uniswap.org / the default token list),
> not the Uniswap Protocol smart contracts.

## 3. Changed-layer observations (supports the scoped claim)

### l4_frontend · attribution: `direct` · Δt = 0h

**Event label**: `uniswap_labs_restricted_tokenized_equity_cohort_from_frontend_ui_preemptive`

**Timestamp**: `2021-07-23 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_corporate`**
  - URL: <https://github.com/Uniswap/default-token-list>
  - Wayback: <https://web.archive.org/web/20210513063137/https://github.com/uniswap/default-token-list>
  - body_hash: `sha256:038a3a409dc011949d40442199b2170ad63e316ade9335227b767705ad56cd49`
  - body_path: `sources/http_captures/uniswap-tokenized-stocks-delisting-2021-07/primary/web.archive.org__web-20210725000000-https-github.com-Uniswap-default-token-list__2bd9e16cee.html`
  > Uniswap default-token-list official repository - the curation
> mechanism by which Uniswap Labs delisted ~100 tokens (tokenized
> stocks, options, synthetic assets) from the app.uniswap.org frontend
> on 2021-07-23 amid securities-classification concerns. The protocol
> itself remained immutable; only the Labs-operated frontend list
> changed. primary_corporate anchor; attribution=direct. Wayback
> 20210513063137 pinned.
- **`semi_primary_wayback`**
  - URL: <https://cointelegraph.com/news/uniswap-delists-100-tokens-from-interface-including-options-and-indexes>
  - Wayback: <https://web.archive.org/web/20210726060203/https://cointelegraph.com/news/uniswap-delists-100-tokens-from-interface-including-options-and-indexes>
  - body_hash: `sha256:401d1902b8e415dce491c68faa3858db50db74a770b15eb6765a801ef04d9137`
  - body_path: `sources/http_captures/uniswap-tokenized-stocks-delisting-2021-07/primary/web.archive.org__web-20210726000000-https-cointelegraph.com-news-uniswap-delists-100-tokens-from-interface-including-options-and-indexes__770bac922b.html`
  > Cointelegraph 2021-07-26 coverage of the Uniswap interface delisting
> of ~100 tokens. Independent semi-primary anchor.
- **`semi_primary_wayback`**
  - URL: <https://decrypt.co/76793/ethrereum-dex-uniswap-drops-tokenized-stocks-as-regulators-close-in>
  - Wayback: <https://web.archive.org/web/20210725080802/https://decrypt.co/76793/ethrereum-dex-uniswap-drops-tokenized-stocks-as-regulators-close-in>
  - body_hash: `sha256:0d55afdf9127daee7f2e5716c44a8b52206940fdc77ad2e9fe770381edc70647`
  - body_path: `sources/http_captures/uniswap-tokenized-stocks-delisting-2021-07/primary/web.archive.org__web-20210726000000-https-decrypt.co-76793-ethrereum-dex-uniswap-drops-tokenized-stocks-as-regulators-close-in__b2c7fc3508.html`
  > Decrypt 2021-07 coverage of Uniswap dropping tokenized stocks from
> its frontend as regulators close in. Independent semi-primary anchor.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`uniswap-frontend-delisting-2023`](./uniswap-frontend-delisting-2023.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `a9689fa`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

