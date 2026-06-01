# Evidence chain — `binance-privacy-coin-delisting-2023`

**Status**: `admitted` · **Stratum**: `S5_corporate` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `1c9c65c` · **Schema**: `0.2.0` · **Event last_verified**: `2026-06-01` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T12:19:10Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "Binance Holdings Limited's final 2023-06-26 privacy-asset restriction for
> users in France, Italy, Poland, and Spain is represented here as an
> attested_secondary S5 corporate exchange-access event. After a broader May
> plan to restrict 12 privacy assets, contemporaneous reporting of Binance's
> June 26 revision says seven assets were spared and Beam, Monero, MobileCoin,
> Firo, and Horizen remained included in the restrictions. The only
> changed-layer claim retained is the centralized-exchange off-ramp catalogue
> restriction for that final five-asset cohort; attribution is plausible
> because the replayable artifacts are journalistic reports carrying Binance
> statements rather than a public first-party Binance notice."

## 1. Trigger

- **Type**: `corporate_policy_change`
- **Actor**: `binance_holdings_limited`
- **Timestamp**: `2023-06-26 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`supporting_journalism`**
  - URL: <https://www.theblock.co/post/236340/binance-privacy-coins>
  - Wayback: <https://web.archive.org/web/20230626230325/https://www.theblock.co/amp/post/236340/binance-privacy-coins>
  - body_hash: `sha256:b88e4a673b199fd4a7b6f655f06cbba54db22330b412b43a83602920bd7d4d7d`
  - body_path: `sources/http_captures/binance-privacy-coin-delisting-2023/secondary/web.archive.org__web-20230626230325-https-www.theblock.co-amp-post-236340-binance-privacy-coins__21c914e44d.html`
  > The Block, archived 2023-06-26 23:03:25 UTC, reports Binance's
> June 26 reversal of the broader May delisting plan. The article
> says Binance would spare Decred, Dash, Zcash, PIVX, Navcoin,
> Secret, and Verge, while "Beam, Monero, MobileCoin, Firo and
> Horizen are still included in the restrictions." The article also
> carries a Binance spokesperson statement that the classification
> revision was made to comply with EU-wide regulatory requirements.
> This is contemporaneous but not a public first-party Binance page,
> so the event is retained as attested_secondary and attribution is
> coded plausible rather than direct.
- **`supporting_journalism`**
  - URL: <https://www.theblock.co/post/232751/binance-privacy-coins-delisting-europe>
  - Wayback: <https://web.archive.org/web/20230601034432/https://www.theblock.co/amp/post/232751/binance-privacy-coins-delisting-europe>
  - body_hash: `sha256:8bfb9f11b5166ea504a570dab808a49bb12254ed35e70cfb0fbd21f7cf093afc`
  - body_path: `sources/http_captures/binance-privacy-coin-delisting-2023/secondary/web.archive.org__web-20230601034432-https-www.theblock.co-amp-post-232751-binance-privacy-coins-delisting-europe__d2c944110b.html`
  > The Block's 2023-05-31 article records the original Binance plan:
> the measure would take effect on 2023-06-26 for France, Italy,
> Poland, and Spain, and would cover Decred, Dash, Zcash, Horizen,
> PIVX, Navcoin, Secret, Verge, Firo, Beam, Monero, and MobileCoin.
> This citation is used to document the pre-reversal plan and timing,
> not to support the final restricted asset set by itself.

## 2. Target

- **Kind**: `asset`
- **Enumeration**: `subset`
- **Actor name**: Binance Holdings Limited (EU-member-state user cohort)
- **Chains**: `beam`, `monero`, `mobilecoin`, `firo`, `horizen`
- **Canonical domains**: `binance.com`

> Final restricted cohort after Binance revised its May 2023 plan on
> 2023-06-26. The May plan reportedly covered 12 privacy assets, but
> Binance's June 26 statement spared Decred, Dash, Zcash, PIVX,
> Navcoin, Secret, and Verge. The retained target set is therefore only
> the five assets still reported as subject to restrictions: Beam,
> Monero, MobileCoin, Firo, and Horizen, for users in France, Italy,
> Poland, and Spain. The row is intentionally scoped to this final
> restricted cohort and does not claim that the seven spared assets were
> actually removed.

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `plausible` · Δt = 0h

**Event label**: `binance_privacy_asset_restriction_eu4_final_cohort`

**Timestamp**: `2023-06-26 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`supporting_journalism`**
  - URL: <https://www.theblock.co/post/236340/binance-privacy-coins>
  - Wayback: <https://web.archive.org/web/20230626230325/https://www.theblock.co/amp/post/236340/binance-privacy-coins>
  - body_hash: `sha256:b88e4a673b199fd4a7b6f655f06cbba54db22330b412b43a83602920bd7d4d7d`
  - body_path: `sources/http_captures/binance-privacy-coin-delisting-2023/secondary/web.archive.org__web-20230626230325-https-www.theblock.co-amp-post-236340-binance-privacy-coins__21c914e44d.html`
  > Load-bearing contemporaneous report of Binance's June 26 revision:
> seven assets were spared from the May plan, while Beam, Monero,
> MobileCoin, Firo, and Horizen remained in the restrictions for
> France, Italy, Poland, and Spain. The source carries Binance's
> emailed spokesperson statement, but the artifact is journalistic
> rather than a first-party Binance notice; attribution is therefore
> plausible.
- **`supporting_journalism`**
  - URL: <https://blockworks.co/news/binance-backtracks-delisting-privacy-coins>
  - Wayback: <https://web.archive.org/web/20230627030458/https://blockworks.co/news/binance-backtracks-delisting-privacy-coins>
  - body_hash: `sha256:b8f3945743ec0ec5fd288521e087e72e38bd678502ebbab455ce2398859156dd`
  - body_path: `sources/http_captures/binance-privacy-coin-delisting-2023/secondary/web.archive.org__web-20230627030458-https-blockworks.co-news-binance-backtracks-delisting-privacy-coins__cec8c15106.html`
  > Blockworks, archived 2023-06-27, independently reports the same
> Binance reversal and quotes Binance's explanation that it had
> revised privacy-coin classification to comply with EU-wide
> regulatory requirements. This source corroborates the operator
> rationale but does not itself enumerate the final five restricted
> assets, so The Block's June 26 article remains the scope anchor.
- **`supporting_journalism`**
  - URL: <https://www.theblock.co/post/232751/binance-privacy-coins-delisting-europe>
  - Wayback: <https://web.archive.org/web/20230601034432/https://www.theblock.co/amp/post/232751/binance-privacy-coins-delisting-europe>
  - body_hash: `sha256:8bfb9f11b5166ea504a570dab808a49bb12254ed35e70cfb0fbd21f7cf093afc`
  - body_path: `sources/http_captures/binance-privacy-coin-delisting-2023/secondary/web.archive.org__web-20230601034432-https-www.theblock.co-amp-post-232751-binance-privacy-coins-delisting-europe__d2c944110b.html`
  > Original May 31 plan and June 26 effective-date context. Retained
> as a before-state anchor because the June 26 revision changed the
> asset scope from the initially reported 12 assets to the final five
> assets still included in restrictions.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`okx-privacy-token-delist-2024`](./okx-privacy-token-delist-2024.md)
- [`eu-mica-2023`](./eu-mica-2023.md)
- [`kraken-monero-eu-delisting-2024`](./kraken-monero-eu-delisting-2024.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `1c9c65c`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

