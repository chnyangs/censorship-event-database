# Evidence chain — `china-weibo-crypto-exchange-purge-2021-03`

**Status**: `admitted` · **Stratum**: `S4_nation_state` · **Shape**: `comparison` (1 changed layer(s): `l4_frontend`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `e2b6fd9` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-21` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> On 2021-03-11 morning (Beijing time), the official Chinese-
> language Sina Weibo accounts of Binance, Huobi (HTX) and OKEx
> (OKX) were rendered inaccessible with the standard PRC content-
> takedown formula, eliminating the search/social discovery path
> to those exchanges' Chinese-language official content. The
> takedowns are coded attribution=plausible (CAC-coordinated
> inference) per codebook §1.4 because no public per-account CAC
> directive was archived; the cascade surface is L4 frontend at
> the discovery layer only.

## 1. Trigger

- **Type**: `nation_state_block`
- **Actor**: `CN_WEIBO_CAC`
- **Timestamp**: `2021-03-11 07:15:00+00:00` (precision: `minute`)

### Trigger citations

- **`supporting_journalism`**
  - URL: <https://www.coindesk.com/policy/2021/03/11/weibo-suspends-huobi-binance-okex-accounts-after-bitcoin-surge>
  - Wayback: <https://web.archive.org/web/2021/https://www.coindesk.com/policy/2021/03/11/weibo-suspends-huobi-binance-okex-accounts-after-bitcoin-surge>
  > CoinDesk report dated 2021-03-11 titled "Weibo Suspends Huobi,
> Binance, OKEx Accounts After Bitcoin Surge". Documents that the
> official Chinese-language Weibo accounts of Huobi, Binance and
> OKEx were rendered inaccessible the morning of 2021-03-11 with
> a Weibo system notice stating the accounts violated "relevant
> laws and regulations" (the standard Weibo takedown formula
> used to enforce Cyberspace Administration of China — CAC —
> content directives). Timestamp anchor 2021-03-11T07:15Z
> (~02:15 ET / 15:15 Beijing) is taken from contemporaneous
> coverage citing the morning of 2021-03-11 Beijing time as the
> outage window. Wayback snapshot URL given as year-resolved
> prefix per codebook wayback-discipline; precise snapshot
> timestamp requires re-pinning in human audit.
- **`supporting_journalism`**
  - URL: <https://www.globaltimes.cn/page/202103/1218100.shtml>
  - Wayback: <https://web.archive.org/web/2021/https://www.globaltimes.cn/page/202103/1218100.shtml>
  > Global Times (PRC state-affiliated English-language outlet)
> report dated 2021-03-11 titled "Weibo deactivates major
> Bitcoin trading platforms in China". State-affiliated framing
> is corroborative on the actor-side: the article notes that
> the accounts had "violated laws and community rules" per
> Weibo's notice. Used as state-press corroboration of the
> takedown window and content-directive framing typical of
> CAC-coordinated platform enforcement. Specific Wayback
> snapshot timestamp requires re-pinning in human audit.
- **`supporting_journalism`**
  - URL: <https://forkast.news/weibo-takedown-huobi-binance-okex-crypto-china/>
  - Wayback: <https://web.archive.org/web/2021/https://forkast.news/weibo-takedown-huobi-binance-okex-crypto-china/>
  > Forkast News analysis (2021-03) titled "What Weibo's takedown
> of Binance & Huobi means for crypto in China". Provides
> regional-press context on the policy reading that the
> platform-level takedown was consistent with prior CAC
> content directives against crypto-trading promotion. Specific
> Wayback snapshot timestamp requires re-pinning in human
> audit.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: Sina Weibo official accounts of Binance / Huobi / OKEx
- **Canonical domains**: `weibo.com/binancezh`, `weibo.com/huobiglobalofficial`, `weibo.com/okexchina`

> Named targets are the official Chinese-language Weibo accounts of
> three major crypto exchanges — Binance, Huobi (HTX) and OKEx
> (OKX) — that were rendered inaccessible on 2021-03-11. Finance
> Magnates reporting indicates the purge extended to 12+ crypto-
> related Weibo accounts in the surrounding window, so subset
> rather than complete: the three named exchange accounts are a
> defensible slice of the broader Weibo crypto-account purge but
> do not enumerate every affected account. canonical_domains lists
> the Weibo profile URLs of the three named exchanges; the
> underlying off-exchange brand domains are tracked separately on
> sibling events.

## 3. Changed-layer observations (supports the scoped claim)

### l4_frontend · attribution: `plausible` · Δt = 0.0h

**Event label**: `binance_official_weibo_account_inaccessible`

**Timestamp**: `2021-03-11 07:15:00+00:00` (precision: `minute`)

**Sources**:

- **`semi_primary_wayback`**
  - URL: <https://www.coindesk.com/policy/2021/03/11/weibo-suspends-huobi-binance-okex-accounts-after-bitcoin-surge>
  - Wayback: <https://web.archive.org/web/20210924122319/https://www.coindesk.com/policy/2021/03/11/weibo-suspends-huobi-binance-okex-accounts-after-bitcoin-surge>
  - body_hash: `sha256:f0e6472e00c1935e316f2e10cb759e253cc3dd3e1a90590264f7c873ac00953c`
  - body_path: `sources/http_captures/china-weibo-crypto-exchange-purge-2021-03/primary/web.archive.org__web-20210924122319-https-www.coindesk.com-policy-2021-03-11-weibo-suspends-huobi-binance-okex-accounts-after-bitcoin-surge__980be17d26.html`
  > CoinDesk 2021-03-11 report documents that Binance's
> official Chinese-language Weibo account returned a Weibo
> takedown notice on 2021-03-11 morning, with the standard
> "violated relevant laws and regulations" formula. The
> CAC-direction inference is plausible rather than direct:
> neither CAC nor Weibo publicly published a per-account
> directive linking the takedown to a specific CAC content
> order, but the formula and the simultaneity across three
> exchange accounts are consistent with CAC-coordinated
> content enforcement under §1.4 codebook reasoning for
> discovery-layer attribution.
- **`semi_primary_wayback`**
  - URL: <https://ambcrypto.com/china-weibo-deactivates-accounts-of-huobi-okex-binance/>
  - Wayback: <https://web.archive.org/web/20210311120450/https://ambcrypto.com/china-weibo-deactivates-accounts-of-huobi-okex-binance/>
  - body_hash: `sha256:25844db1b7fc789cb548fd8879f79fd8d30abf60cbeb26f9bd866409aaf19967`
  - body_path: `sources/http_captures/china-weibo-crypto-exchange-purge-2021-03/primary/web.archive.org__web-20210311120450-https-ambcrypto.com-china-weibo-deactivates-accounts-of-huobi-okex-binance__88af85fc5c.html`
  > AMBCrypto corroboration of the 2021-03-11 Binance Weibo
> account deactivation.

### l4_frontend · attribution: `plausible` · Δt = 0.0h

**Event label**: `huobi_official_weibo_account_inaccessible`

**Timestamp**: `2021-03-11 07:15:00+00:00` (precision: `minute`)

**Sources**:

- **`semi_primary_wayback`**
  - URL: <https://www.coindesk.com/policy/2021/03/11/weibo-suspends-huobi-binance-okex-accounts-after-bitcoin-surge>
  - Wayback: <https://web.archive.org/web/20210924122319/https://www.coindesk.com/policy/2021/03/11/weibo-suspends-huobi-binance-okex-accounts-after-bitcoin-surge>
  - body_hash: `sha256:f0e6472e00c1935e316f2e10cb759e253cc3dd3e1a90590264f7c873ac00953c`
  - body_path: `sources/http_captures/china-weibo-crypto-exchange-purge-2021-03/primary/web.archive.org__web-20210924122319-https-www.coindesk.com-policy-2021-03-11-weibo-suspends-huobi-binance-okex-accounts-after-bitcoin-surge__980be17d26.html`
  > CoinDesk 2021-03-11 report documents that Huobi's official
> Chinese-language Weibo account returned a Weibo notice
> stating the account had "abnormal practices" and
> contained safety risks — a slightly different Weibo
> takedown phrasing than Binance/OKEx but the same
> inaccessibility outcome on the same day.
- **`semi_primary_wayback`**
  - URL: <https://www.globaltimes.cn/page/202103/1218100.shtml>
  - Wayback: <https://web.archive.org/web/20210311115433/https://www.globaltimes.cn/page/202103/1218100.shtml>
  - body_hash: `sha256:52c3a8339c7f032e9bf4f36555cfee156f4923cfe511e6030bbcf5711a1efbfc`
  - body_path: `sources/http_captures/china-weibo-crypto-exchange-purge-2021-03/primary/web.archive.org__web-20210311115433-https-www.globaltimes.cn-page-202103-1218100.shtml__cc628cad9c.html`
  > Global Times (PRC state-affiliated) report quotes a Huobi
> spokesperson stating the issue had just come to their
> attention and that they were "actively communicating with
> Weibo".

### l4_frontend · attribution: `plausible` · Δt = 0.0h

**Event label**: `okex_official_weibo_account_inaccessible`

**Timestamp**: `2021-03-11 07:15:00+00:00` (precision: `minute`)

**Sources**:

- **`semi_primary_wayback`**
  - URL: <https://www.coindesk.com/policy/2021/03/11/weibo-suspends-huobi-binance-okex-accounts-after-bitcoin-surge>
  - Wayback: <https://web.archive.org/web/20210924122319/https://www.coindesk.com/policy/2021/03/11/weibo-suspends-huobi-binance-okex-accounts-after-bitcoin-surge>
  - body_hash: `sha256:f0e6472e00c1935e316f2e10cb759e253cc3dd3e1a90590264f7c873ac00953c`
  - body_path: `sources/http_captures/china-weibo-crypto-exchange-purge-2021-03/primary/web.archive.org__web-20210924122319-https-www.coindesk.com-policy-2021-03-11-weibo-suspends-huobi-binance-okex-accounts-after-bitcoin-surge__980be17d26.html`
  > CoinDesk 2021-03-11 report documents that OKEx's official
> Chinese-language Weibo account was rendered inaccessible
> on 2021-03-11 morning with the same Weibo takedown
> framing.
- **`semi_primary_wayback`**
  - URL: <https://www.financemagnates.com/cryptocurrency/news/weibo-bans-more-than-12-crypto-related-accounts-amid-chinas-crypto-crackdown/>
  - Wayback: <https://web.archive.org/web/20210607085825/https://www.financemagnates.com/cryptocurrency/news/weibo-bans-more-than-12-crypto-related-accounts-amid-chinas-crypto-crackdown/>
  - body_hash: `sha256:2baf04a1846f0f1d170c4bfcbeaeb3ca016b0e7c609935cebbb8d148d865aa67`
  - body_path: `sources/http_captures/china-weibo-crypto-exchange-purge-2021-03/primary/web.archive.org__web-20210607085825-https-www.financemagnates.com-cryptocurrency-news-weibo-bans-more-than-12-crypto-related-accounts-amid-chinas-crypto-crackdown__a75acc1d2b.html`
  > Finance Magnates reporting frames the 2021-03-11 OKEx /
> Binance / Huobi Weibo account takedowns as part of a
> broader purge of 12+ crypto-related Weibo accounts in the
> same window — useful as the subset-enumeration rationale
> for target.enumeration=subset.

## 5. Honest coverage gaps

- **offramp_cex** (`not_measured`): The 2021-03-11 Weibo purge is a discovery-layer signal and

## 7. Related events

- [`china-pboc-crypto-ban-2021`](./china-pboc-crypto-ban-2021.md)
- [`china-state-council-mining-crackdown-2021-05`](./china-state-council-mining-crackdown-2021-05.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `e2b6fd9`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

