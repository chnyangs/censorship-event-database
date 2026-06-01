# Evidence chain — `china-search-engine-social-keyword-exchange-block-2021-06`

**Status**: `admitted` · **Stratum**: `S4_nation_state` · **Shape**: `comparison` (1 changed layer(s): `l4_frontend`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `0785824` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-31` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T12:44:40Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "On 2021-06-09, China's major search and social platforms (Baidu, Weibo,
> Sogou, Zhihu) suppressed search results for the crypto exchanges Binance,
> Huobi and OKEx, with Weibo citing 'relevant laws, regulations, and policies'.
> Effect captured at the l4_frontend layer via two same-day journalism sources;
> attribution plausible (state-directed, class-level)."

## 1. Trigger

- **Type**: `nation_state_block`
- **Actor**: `CN_CAC`
- **Timestamp**: `2021-06-09 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`supporting_journalism`**
  - URL: <https://www.aljazeera.com/economy/2021/6/9/searches-for-crypto-exchanges-currently-blocked-in-china>
  - Wayback: <https://web.archive.org/web/20210609164859/https://www.aljazeera.com/economy/2021/6/9/searches-for-crypto-exchanges-currently-blocked-in-china>
  - body_hash: `sha256:e8573402493c3e3443a340e27eec4231f07bde2ec659cd3ede9c374dec9cd419`
  - body_path: `sources/http_captures/china-search-engine-social-keyword-exchange-block-2021-06/primary/web.archive.org__web-20210609164859-https-www.aljazeera.com-economy-2021-6-9-searches-for-crypto-exchanges-currently-blocked-in-china__c4c365caac.html`
  > Al Jazeera, "Searches for crypto exchanges currently blocked in China"
> (dated 2021-06-09, Wayback snapshot captured same day 16:48 UTC).
> Reports that on China's major search engines and social platforms —
> Baidu, Weibo, Sogou and Zhihu — searches for the Chinese or English
> names of Binance, Huobi and OKEx returned zero / suppressed results,
> with Weibo's search page citing "relevant laws, regulations, and
> policies" as the reason results were not displayed. State-directed
> keyword censorship (CAC content directive) during the June-2021 PRC
> crypto crackdown. Captured HTML verified to contain Baidu / Weibo /
> Sogou / Zhihu and Binance / Huobi / OKEx references.

## 2. Target

- **Kind**: `domain`
- **Enumeration**: `subset`
- **Actor name**: Baidu / Weibo / Sogou / Zhihu (state-directed keyword suppression)
- **Canonical domains**: `binance.com`, `huobi.com`, `okex.com`

> Keyword/search queries for the three named crypto exchanges (Binance, Huobi,
> OKEx) on the four named PRC search/social platforms (Baidu, Weibo, Sogou,
> Zhihu). The suppression is keyword-class-level; no exhaustive enumeration of
> all affected queries exists in the sources.

## 3. Changed-layer observations (supports the scoped claim)

### l4_frontend · attribution: `plausible` · Δt = 0h

**Event label**: `exchange_name_search_results_suppressed`

**Timestamp**: `2021-06-09 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`supporting_journalism`**
  - URL: <https://www.aljazeera.com/economy/2021/6/9/searches-for-crypto-exchanges-currently-blocked-in-china>
  - Wayback: <https://web.archive.org/web/20210609164859/https://www.aljazeera.com/economy/2021/6/9/searches-for-crypto-exchanges-currently-blocked-in-china>
  - body_hash: `sha256:e8573402493c3e3443a340e27eec4231f07bde2ec659cd3ede9c374dec9cd419`
  - body_path: `sources/http_captures/china-search-engine-social-keyword-exchange-block-2021-06/primary/web.archive.org__web-20210609164859-https-www.aljazeera.com-economy-2021-6-9-searches-for-crypto-exchanges-currently-blocked-in-china__c4c365caac.html`
  > Al Jazeera same-day report documenting suppressed search results for
> Binance/Huobi/OKEx on Baidu/Weibo/Sogou/Zhihu, with Weibo citing
> "relevant laws, regulations, and policies". attribution=plausible: the
> platforms implemented the suppression consistent with a CAC content
> directive, but no public order naming the specific queries is captured
> (class-level inference per §1.1).
- **`supporting_journalism`**
  - URL: <https://www.coindesk.com/markets/2021/06/09/chinese-internet-services-are-censoring-binance-huobi-and-okex-related-keywords>
  - Wayback: <https://web.archive.org/web/20210924222230/https://www.coindesk.com/markets/2021/06/09/chinese-internet-services-are-censoring-binance-huobi-and-okex-related-keywords/>
  - body_hash: `sha256:6d652d18d15f2b3ca09e5b364deb68a749707c490bf26ef13e5a51f17ca4ca99`
  - body_path: `sources/http_captures/china-search-engine-social-keyword-exchange-block-2021-06/primary/web.archive.org__web-20210924222230-https-www.coindesk.com-markets-2021-06-09-chinese-internet-services-are-censoring-binance-huobi-and-okex-related-keywords__33292c0ec4.html`
  > CoinDesk corroboration (article dated 2021-06-09; Wayback 2021-09-24
> snapshot — the earliest archived 200 capture of the article). Confirms
> Baidu/Weibo/Zhihu/Sogou keyword censorship of the three exchanges.

## 5. Honest coverage gaps

- **l0_network** (`not_measured`): No replayable OONI / Censored Planet / Cloudflare Radar slice captured for

## 7. Related events

- [`china-weibo-crypto-exchange-purge-2021-03`](./china-weibo-crypto-exchange-purge-2021-03.md)
- [`china-pboc-crypto-ban-2021`](./china-pboc-crypto-ban-2021.md)
- [`china-state-council-mining-crackdown-2021-05`](./china-state-council-mining-crackdown-2021-05.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `0785824`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

