# Evidence chain — `coinbase-japan-exit-2023`

**Status**: `admitted` · **Stratum**: `S5_corporate` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `97f58fa` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-21` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "Coinbase KK's 2023-01-18 wind-down of Japan retail operations
> illustrates a registered-exchange market exit driven by corporate
> restructuring (2022 crypto-winter cost-cutting) rather than by a
> jurisdiction-specific enforcement order, complementing the India 2022
> informal-pressure exit and the JP FSA 2018 administrative-enforcement
> baseline."

## 1. Trigger

- **Type**: `corporate_policy_change`
- **Actor**: `coinbase_inc`
- **Timestamp**: `2023-01-18 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_corporate`**
  - URL: <https://www.coinbase.com/en-gb/blog/halting-operations-in-japan>
  - Wayback: <https://web.archive.org/web/2023/https://www.coinbase.com/en-gb/blog/halting-operations-in-japan>
  > Coinbase corporate blog post "Halting Operations in Japan" (2023-01-18)
> announcing the wind-down of Coinbase KK retail operations. Cited as
> contextual_unarchived per evidence_use rule; not used to support
> admission claims at this draft stage. Wayback anchor pinned at year-
> level; per-snapshot body_hash pinned in the observation sources.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: Coinbase KK (Coinbase Japan)
- **Canonical domains**: `coinbase.com`

> Target is Coinbase KK (Coinbase Japan retail entity), a registered Japan
> FSA crypto-asset exchange service provider. Subset enumeration because
> the wind-down enumerates the Japan-market retail product surface
> (new-account suspension, fiat-deposit removal, customer-withdrawal
> deadline) rather than a complete on-chain address set. No address-level
> targets; the action is a market-level exit by a registered exchange.

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `direct` · Δt = Noneh

**Event label**: `japan_retail_operations_wind_down_announced`

**Timestamp**: `2023-01-18 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_corporate`**
  - URL: <https://www.coinbase.com/blog/halting-operations-in-japan>
  - Wayback: <https://web.archive.org/web/20230119233917/https://www.coinbase.com/blog/halting-operations-in-japan>
  - body_hash: `sha256:b8fc687804f4d4a623e3ac85660dc4c95c64d5187a7aeee8b47735728cd56dff`
  - body_path: `sources/http_captures/coinbase-japan-exit-2023/primary/web.archive.org__web-20230120000000-https-www.coinbase.com-blog-halting-operations-in-japan__f443c99105.html`
  > Coinbase official blog (2023-01-18) announcing the decision to halt
> operations in Japan, remove fiat deposits 2023-01-20 JST, and require
> customer withdrawals by 2023-02-16. primary_corporate anchor;
> attribution=direct. Wayback 20230119233917 pinned.
- **`semi_primary_wayback`**
  - URL: <https://www.bloomberg.com/news/articles/2023-01-18/coinbase-stops-japan-operations-after-slump-in-digital-assets>
  - Wayback: <https://web.archive.org/web/20230118133921/https://www.bloomberg.com/news/articles/2023-01-18/coinbase-stops-japan-operations-after-slump-in-digital-assets>
  - body_hash: `sha256:5a056053ead4fc5bdbd355805c2ee780cf88b5aa2ffd5568236ddbca797344ba`
  - body_path: `sources/http_captures/coinbase-japan-exit-2023/primary/web.archive.org__web-20230119000000-https-www.bloomberg.com-news-articles-2023-01-18-coinbase-stops-japan-operations-after-slump-in-digital-assets__7f818d23ab.html`
  > Bloomberg 2023-01-18 coverage of the Coinbase Japan operations halt.
> Independent semi-primary anchor.
- **`semi_primary_wayback`**
  - URL: <https://www.coindesk.com/business/2023/01/18/coinbase-confirms-it-is-halting-operations-in-japan>
  - Wayback: <https://web.archive.org/web/20230120164642/https://www.coindesk.com/business/2023/01/18/coinbase-confirms-it-is-halting-operations-in-japan/>
  - body_hash: `sha256:690cbaa26c428aca877ee8272b259122ba8cbaddb239994ba87e71c8fcaa18dc`
  - body_path: `sources/http_captures/coinbase-japan-exit-2023/primary/web.archive.org__web-20230120000000-https-www.coindesk.com-business-2023-01-18-coinbase-confirms-it-is-halting-operations-in-japan__399e2c1572.html`
  > CoinDesk 2023-01-18 confirmation of the Coinbase Japan shutdown.
> Independent semi-primary anchor.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`coinbase-india-exit-2022`](./coinbase-india-exit-2022.md)
- [`japan-fsa-coincheck-orders-2018`](./japan-fsa-coincheck-orders-2018.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `97f58fa`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

