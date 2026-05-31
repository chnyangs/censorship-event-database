# Evidence chain — `china-pboc-exchange-shutdown-2017-09`

**Status**: `admitted` · **Stratum**: `S4_nation_state` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `a09b90d` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-21` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> In mid-September 2017 the PBOC and affiliated PRC regulators
> instructed domestic cryptocurrency exchanges to cease CNY-paired
> trading and wind down domestic operations; within ~2 weeks the
> PRC exchange triad (BTCC, OKCoin, Huobi) had announced and
> executed cessation of domestic CNY-paired trading, with BTCC
> ceasing all trading on 2017-09-30 and Huobi / OKCoin completing
> staged shutdown by end of October. The offramp_cex layer carries
> the load-bearing direct-attribution observation; L4 frontend
> reactions are consistent with the cascade but require a Wayback-
> capture pass before they may anchor a separate observed_change row.

## 1. Trigger

- **Type**: `nation_state_block`
- **Actor**: `CN_PBOC`
- **Timestamp**: `2017-09-29 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <http://www.pbc.gov.cn/>
  - Wayback: <https://web.archive.org/web/2017/http://www.pbc.gov.cn/>
  > DRYRUN 2026-05-16. Canonical primary instrument is the
> mid-September 2017 PBOC-led joint instruction directing all
> domestic Chinese cryptocurrency exchanges to cease CNY-paired
> trading and wind down domestic operations. The instruction was
> delivered via the PBOC Business Management Department (Beijing)
> and the Shanghai Municipal Financial Services Office in the
> days following the 2017-09-04 ICO ban (China's "Notice on
> Preventing Risks of Token Issuance Financing", 关于防范代币发行
> 融资风险的公告). Unlike the 2013-12 and 2021-09 notices, the
> 2017-09 exchange-shutdown directive was not published as a
> single named ministerial notice; it was issued verbally /
> administratively to named exchanges and corroborated via the
> exchanges' own shutdown announcements and contemporaneous
> Chinese-language and English-language press coverage. The PBOC
> primary URL is a provisional anchor (homepage) pending a re-pin of
> the original 2017-09 PBOC business-management-department
> communication or its archival surrogate. Marked
> evidence_use=contextual_unarchived.
- **`supporting_journalism`**
  - URL: <https://www.coindesk.com/markets/2017/09/15/chinas-bitcoin-exchanges-receive-shutdown-orders-and-closure-timeline/>
  - Wayback: <https://web.archive.org/web/2017/https://www.coindesk.com/markets/2017/09/15/chinas-bitcoin-exchanges-receive-shutdown-orders-and-closure-timeline/>
  > CoinDesk 2017-09-15 report "China's Bitcoin Exchanges Receive
> Shutdown Orders and Closure Timeline" giving English-language
> contemporaneous coverage of the PBOC-led shutdown order and
> the closure-deadline timeline communicated to BTCC, OKCoin,
> and Huobi. Used here as a contextual translation anchor; the
> specific Wayback snapshot timestamp is to be re-pinned during
> human audit. Marked evidence_use=contextual_unarchived.
- **`supporting_journalism`**
  - URL: <https://www.coindesk.com/markets/2017/09/15/huobi-okcoin-to-stop-yuan-to-bitcoin-trading-by-octobers-end/>
  - Wayback: <https://web.archive.org/web/2017/https://www.coindesk.com/markets/2017/09/15/huobi-okcoin-to-stop-yuan-to-bitcoin-trading-by-octobers-end/>
  > CoinDesk 2017-09-15 report "Huobi, OKCoin to Stop Yuan-to-Bitcoin
> Trading By October's End" documenting the staged shutdown
> commitments of the two largest remaining domestic exchanges in
> direct response to the regulator instruction. Marked
> evidence_use=contextual_unarchived pending human-audit re-pin
> of the Wayback snapshot timestamp.
- **`supporting_journalism`**
  - URL: <https://qz.com/1079908/huobi-and-okcoin-chinas-two-biggest-bitcoin-exchanges-will-halt-all-trading-services-for-local-customers>
  - Wayback: <https://web.archive.org/web/2017/https://qz.com/1079908/huobi-and-okcoin-chinas-two-biggest-bitcoin-exchanges-will-halt-all-trading-services-for-local-customers>
  > Quartz report "It's over: China's biggest bitcoin exchanges
> will halt all trading services for local customers" covering
> the final shutdown of domestic CNY trading services at Huobi
> and OKCoin. Used as English-language journalistic
> corroboration. Marked evidence_use=contextual_unarchived.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: PRC domestic crypto-exchange triad (BTCC, OKCoin, Huobi)
- **Chains**: `bitcoin`, `ethereum`
- **Canonical domains**: `btcc.com`, `btcchina.com`, `okcoin.cn`, `huobi.com`

> Canonical target is the cluster of three dominant PRC domestic
> cryptocurrency exchanges operating in 2017: BTCC (btcc.com /
> btcchina.com), OKCoin (okcoin.cn), and Huobi (huobi.com). The
> PBOC-led shutdown instruction also affected smaller venues (ViaBTC,
> YoBTC, Yunbi, etc.) but those are out of scope for this subset.
> Marked enumeration=subset because the named cluster (BTCC, OKCoin,
> Huobi) is a defensible slice representing the dominant ~90%+ of
> domestic CNY-paired Bitcoin trading volume at the time, rather
> than a full enumeration of every Chinese venue affected. Some
> cluster members migrated offshore in response (Huobi → Singapore,
> OKCoin spinoff OKEx → offshore; Binance moved from China to
> Malta in early 2018).

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `plausible` · Δt = Noneh

**Event label**: `cny_paired_trading_ceased_domestic_shutdown`

**Timestamp**: `2017-09-29 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`semi_primary_wayback`**
  - URL: <https://web.archive.org/web/20170928090826id_/https://www.btcchina.com/>
  - Wayback: <https://web.archive.org/web/20170928090826/https://www.btcchina.com/>
  - body_hash: `sha256:ab4798c8baaa1efb74ae71b3ce98a4f3fd516b77be60ca04d6a8824e5a1b7fd5`
  - body_path: `sources/http_captures/china-pboc-exchange-shutdown-2017-09/v0_3_primary_repair/web.archive.org__web-20170928090826id_-https-www.btcchina.com__40bc25c910.html`
  > Captured Wayback memento of the BTCChina platform surface
> shortly before the 2017-09-30 shutdown deadline. The snapshot
> is a platform-state semi-primary observation: it preserves the
> BTCChina/BTCC web surface and CNY-pair exchange widgets during
> the wind-down window. It does not, by itself, prove the PBOC
> administrative instruction or the Huobi/OKCoin legs of the
> cluster; those still require exchange-announcement or agency
> anchors in human review. Used here only to replace the prior
> supporting-journalism-only observation with one replayable
> platform-state artifact for the BTCChina slice.
- **`semi_primary_wayback`**
  - URL: <https://web.archive.org/web/20171014094506id_/https://www.btcchina.com/>
  - Wayback: <https://web.archive.org/web/20171014094506/https://www.btcchina.com/>
  - body_hash: `sha256:f62795572a145030797fa9a0f035195798bd761ab70b94d81689836235202634`
  - body_path: `sources/http_captures/china-pboc-exchange-shutdown-2017-09/v0_3_primary_repair/web.archive.org__web-20171014094506id_-https-www.btcchina.com__960d3ee20e.html`
  > Captured Wayback memento of the BTCChina platform surface after
> the final 2017-09-30 domestic trading deadline. The replayable
> page pair is useful for a BTCChina platform-state audit but is
> intentionally grouped with the 2017-09-28 memento as a single
> evidence group, because both artifacts come from the same domain
> and do not independently establish the full exchange triad.
- **`semi_primary_wayback`**
  - URL: <https://www.coindesk.com/markets/2017/09/15/chinas-bitcoin-exchanges-receive-shutdown-orders-and-closure-timeline/>
  - Wayback: <https://web.archive.org/web/20210919090731/https://www.coindesk.com/markets/2017/09/15/chinas-bitcoin-exchanges-receive-shutdown-orders-and-closure-timeline/>
  - body_hash: `sha256:a9aee20a19c03500e416cfdb15f8762bffb16f0358978cc14f19584d767e1189`
  - body_path: `sources/http_captures/china-pboc-exchange-shutdown-2017-09/primary/web.archive.org__web-20210919090731-https-www.coindesk.com-markets-2017-09-15-chinas-bitcoin-exchanges-receive-shutdown-orders-and-closure-timeline__a7913f1395.html`
  > CoinDesk 2017-09-15 report giving the staged closure-deadline
> timeline communicated by Chinese regulators to BTCC, OKCoin,
> and Huobi. Specific Wayback snapshot timestamp requires
> re-pinning in human audit.
- **`semi_primary_wayback`**
  - URL: <https://www.coindesk.com/markets/2017/09/15/huobi-okcoin-to-stop-yuan-to-bitcoin-trading-by-octobers-end/>
  - Wayback: <https://web.archive.org/web/20210920212107/https://www.coindesk.com/markets/2017/09/15/huobi-okcoin-to-stop-yuan-to-bitcoin-trading-by-octobers-end/>
  - body_hash: `sha256:f4c6e516a5e12e75595c3e53352ba979cfc0cb99c069f1f61482bd4a9c0eaca2`
  - body_path: `sources/http_captures/china-pboc-exchange-shutdown-2017-09/primary/web.archive.org__web-20210920212107-https-www.coindesk.com-markets-2017-09-15-huobi-okcoin-to-stop-yuan-to-bitcoin-trading-by-octobers-end__48e43adec1.html`
  > CoinDesk 2017-09-15 report documenting Huobi and OKCoin's
> commitment to halt yuan-paired bitcoin trading by end of
> October 2017 in direct response to the regulator
> instruction. Specific Wayback snapshot timestamp requires
> re-pinning in human audit.
- **`supporting_journalism`**
  - URL: <https://qz.com/1079908/huobi-and-okcoin-chinas-two-biggest-bitcoin-exchanges-will-halt-all-trading-services-for-local-customers>
  - Wayback: <https://web.archive.org/web/2017/https://qz.com/1079908/huobi-and-okcoin-chinas-two-biggest-bitcoin-exchanges-will-halt-all-trading-services-for-local-customers>
  > Quartz report covering the final shutdown of domestic
> trading services at Huobi and OKCoin. Corroborates the
> observed industry-wide CNY-paired trading cessation.
> Specific Wayback snapshot timestamp requires re-pinning
> in human audit.
- **`supporting_journalism`**
  - URL: <https://www.coindesk.com/markets/2017/09/27/bitcoin-exchange-btcc-sets-deadline-for-yuan-withdrawals>
  - Wayback: <https://web.archive.org/web/2017/https://www.coindesk.com/markets/2017/09/27/bitcoin-exchange-btcc-sets-deadline-for-yuan-withdrawals>
  > CoinDesk 2017-09-27 report "Bitcoin Exchange BTCC Sets
> Deadline for Yuan Withdrawals" documenting the BTCC
> wind-down operational timeline, including the
> 2017-09-30 final-shutdown deadline. Specific Wayback
> snapshot timestamp requires re-pinning in human audit.

## 5. Honest coverage gaps

- **l4_frontend** (`not_measured`): The three named domestic exchanges (BTCC, OKCoin, Huobi)

## 7. Related events

- [`china-ico-ban-2017-09`](./china-ico-ban-2017-09.md)
- [`china-pboc-crypto-ban-2013-12`](./china-pboc-crypto-ban-2013-12.md)
- [`china-pboc-crypto-ban-2021`](./china-pboc-crypto-ban-2021.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `a09b90d`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

