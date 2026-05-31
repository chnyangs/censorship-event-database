# Evidence chain — `china-state-council-mining-crackdown-2021-05`

**Status**: `admitted` · **Stratum**: `S4_nation_state` · **Shape**: `comparison` (2 changed layer(s): `l1_consensus`, `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `7542617` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-21` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> Within hours-to-days of the PRC State Council Financial
> Stability and Development Committee's 2021-05-21 directive
> to "crack down on bitcoin mining and trading behavior",
> China's share of global Bitcoin hashrate began a multi-
> month decline (Cambridge CBECI: ~46% April 2021 → ~0%
> July-August 2021) and named PRC-facing mining and trading
> services (Huobi miner hosting, HashCow machine sales,
> BTC.TOP pool) publicly paused operations within 48-72
> hours. Attribution is plausible rather than direct because
> the cascade is jointly produced by this directive plus the
> province-level implementing bans recorded as sibling
> related_events.

## 1. Trigger

- **Type**: `nation_state_block`
- **Actor**: `CN_STATE_COUNCIL`
- **Timestamp**: `2021-05-21 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <http://www.gov.cn/guowuyuan/2021-05/21/content_5610192.htm>
  - Wayback: <https://web.archive.org/web/2021/http://www.gov.cn/guowuyuan/2021-05/21/content_5610192.htm>
  - body_hash: `sha256:0dc104d32ebe49522590e6f1b999aac1a88304a93c84b85db74857499d6bb2c4`
  - body_path: `sources/http_captures/china-state-council-mining-crackdown-2021-05/primary/web.archive.org__web-20210521153842-http-www.gov.cn-guowuyuan-2021-05-21-content_5610192.htm__a4e95ada52.html`
  > State Council Financial Stability and Development Committee
> (国务院金融稳定发展委员会, FSDC) 51st meeting, chaired by Vice
> Premier Liu He (member of the Politburo, Director of the
> Committee), held 2021-05-21. The published readout includes the
> load-bearing sentence "打击比特币挖矿和交易行为，坚决防范个人风险向社会
> 领域传递" ("crack down on bitcoin mining and trading behavior;
> resolutely prevent the transmission of individual risks to the
> social sector"). This is the highest-ranking PRC organ to
> explicitly name bitcoin mining as a target and is the immediate
> precursor to the province-level mining-ban cascade (Inner
> Mongolia 2021-05-25, Qinghai 2021-06-09, Yunnan/Xinjiang/Sichuan
> 2021-06). evidence_use=contextual_unarchived because no
> body_hash+body_path archival capture was pinned in this
> DRYRUN authoring pass; the gov.cn origin URL and the Xinhua
> English readout remain publicly reachable and Wayback
> bracketing of the 2021-05-21 publication window is straightforward
> in a follow-up human-audit pass.
- **`supporting_journalism`**
  - URL: <https://www.reuters.com/technology/chinese-financial-payment-bodies-barred-cryptocurrency-business-2021-05-18/>
  - Wayback: <https://web.archive.org/web/2021/https://www.reuters.com/technology/chinese-financial-payment-bodies-barred-cryptocurrency-business-2021-05-18/>
  > Reuters 2021-05-21 wire coverage of the FSDC statement.
> Provides English-language journalist-attested corroboration
> of the Chinese-language readout and explicitly identifies
> Liu He as the chair and the FSDC as the issuing body.
- **`supporting_journalism`**
  - URL: <https://www.cnbc.com/2021/05/21/bitcoin-falls-after-china-calls-for-crackdown-on-bitcoin-mining-and-trading-behavior.html>
  - Wayback: <https://web.archive.org/web/2021/https://www.cnbc.com/2021/05/21/bitcoin-falls-after-china-calls-for-crackdown-on-bitcoin-mining-and-trading-behavior.html>
  > CNBC 2021-05-21 contemporaneous market-reaction coverage.
> Cited for the immediate (intra-day) BTC spot price decline of
> ≥6% following circulation of the FSDC statement; supports
> plausible attribution for downstream observations.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: PRC State Council Financial Stability and Development Committee (FSDC) 51st meeting directive
- **Chains**: `bitcoin`

> Canonical target is the FSDC policy directive itself, naming two
> activity classes: (1) bitcoin mining ("挖矿") operating within
> PRC borders, and (2) bitcoin trading ("交易") behavior touching
> PRC residents. The named-class enumeration is a defensible
> subset rather than a complete exchange/miner roster because the
> directive does not enumerate specific firms, addresses, or
> canonical domains; the implementing province-level bans
> (Inner Mongolia 2021-05-25, Qinghai 2021-06-09, Yunnan,
> Xinjiang, Sichuan 2021-06) enumerate the actual mining sites
> they shut down, and those carry their own load-bearing
> observed_change rows in their own event files.

## 3. Changed-layer observations (supports the scoped claim)

### l1_consensus · attribution: `plausible` · Δt = Noneh

**Event label**: `cn_bitcoin_hashrate_share_collapse`

**Timestamp**: `?` (precision: `day`)

**Sources**:

- **`primary_legal`**
  - URL: <http://www.gov.cn/guowuyuan/2021-05/21/content_5610192.htm>
  - Wayback: <https://web.archive.org/web/20210521153842/http://www.gov.cn/guowuyuan/2021-05/21/content_5610192.htm>
  - body_hash: `sha256:0dc104d32ebe49522590e6f1b999aac1a88304a93c84b85db74857499d6bb2c4`
  - body_path: `sources/http_captures/china-state-council-mining-crackdown-2021-05/primary/web.archive.org__web-20210521153842-http-www.gov.cn-guowuyuan-2021-05-21-content_5610192.htm__a4e95ada52.html`
  > State Council Financial Stability and Development Committee
> (FSDC) statement 2021-05-21 calling to "crack down on Bitcoin
> mining and trading behavior". Primary directive anchor for the
> hashrate-share collapse cascade. Wayback memento 20210521153842
> captured 2026-05-21.
- **`semi_primary_measurement`**
  - URL: <https://ccaf.io/cbnsi/cbeci/mining_map>
  - Wayback: <https://web.archive.org/web/2021/https://ccaf.io/cbnsi/cbeci/mining_map>
  > Cambridge Centre for Alternative Finance (CCAF) Bitcoin
> Mining Map. CN share of global Bitcoin hashrate
> declined from ≈46% (April 2021) to ≈0% (July-August
> 2021), per the geographically-attributed hashrate
> dataset CCAF publishes from pool-level IP geolocation.
> attribution=plausible because the FSDC directive plus
> the implementing province-level bans (Inner Mongolia
> 2021-05-25, Qinghai 2021-06-09, Sichuan 2021-06) are
> the joint proximate cause; the directive alone does
> not have direct on-chain hashrate-attribution evidence
> and the cascade is shared across the related_events
> siblings. evidence_use=contextual_unarchived because
> CCAF country-share JSON body_hash is not pinned in
> this DRYRUN pass.
- **`supporting_journalism`**
  - URL: <https://www.scmp.com/tech/policy/article/3141231/china-widens-crackdown-cryptocurrency-miners-shrinking-countrys-share>
  - Wayback: <https://web.archive.org/web/2021/https://www.scmp.com/tech/policy/article/3141231/china-widens-crackdown-cryptocurrency-miners-shrinking-countrys-share>
  > South China Morning Post coverage documenting the
> China share-of-global-hashrate decline through 2021,
> providing journalist-attested corroboration for the
> CCAF tracker series. Cited for narrative anchoring
> only; the load-bearing measurement is the CCAF
> tracker above.

### offramp_cex · attribution: `plausible` · Δt = Noneh

**Event label**: `cn_mining_service_and_trading_pause_announcements`

**Timestamp**: `?` (precision: `day`)

**Sources**:

- **`primary_legal`**
  - URL: <http://www.gov.cn/guowuyuan/2021-05/21/content_5610192.htm>
  - Wayback: <https://web.archive.org/web/20210521153842/http://www.gov.cn/guowuyuan/2021-05/21/content_5610192.htm>
  - body_hash: `sha256:0dc104d32ebe49522590e6f1b999aac1a88304a93c84b85db74857499d6bb2c4`
  - body_path: `sources/http_captures/china-state-council-mining-crackdown-2021-05/primary/web.archive.org__web-20210521153842-http-www.gov.cn-guowuyuan-2021-05-21-content_5610192.htm__a4e95ada52.html`
  > State Council FSDC 2021-05-21 statement is the primary directive
> driving the mining-service + trading pause announcements.
> Wayback memento 20210521153842 captured 2026-05-21.
- **`semi_primary_wayback`**
  - URL: <https://www.cnbc.com/2021/05/21/bitcoin-falls-after-china-calls-for-crackdown-on-bitcoin-mining-and-trading-behavior.html>
  - Wayback: <https://web.archive.org/web/20210521160706/https://www.cnbc.com/2021/05/21/bitcoin-falls-after-china-calls-for-crackdown-on-bitcoin-mining-and-trading-behavior.html>
  - body_hash: `sha256:dd0f548582f23ecad905039c1e4aeba7fbb49a7aac10482edc94a059fcd5f47c`
  - body_path: `sources/http_captures/china-state-council-mining-crackdown-2021-05/primary/web.archive.org__web-20210521160706-https-www.cnbc.com-2021-05-21-bitcoin-falls-after-china-calls-for-crackdown-on-bitcoin-mining-and-trading-behavior.html__1d9eaab499.html`
  > CNBC 2021-05-21 contemporaneous coverage of the FSDC crackdown
> call and the Bitcoin price drop. Independent semi-primary anchor.
- **`supporting_journalism`**
  - URL: <https://www.aljazeera.com/economy/2021/5/24/china-crackdown-forces-crypto-mining-operators-to-end-operations>
  - Wayback: <https://web.archive.org/web/2021/https://www.aljazeera.com/economy/2021/5/24/china-crackdown-forces-crypto-mining-operators-to-end-operations>
  > Al Jazeera contemporaneous coverage (2021-05-24)
> documenting that within 48-72 hours of the FSDC
> statement: (a) Huobi suspended miner hosting services
> and Bitcoin futures/leverage trading for new mainland
> PRC accounts, (b) HashCow halted mining-machine sales
> to PRC clients, and (c) BTC.TOP founder Jiang Zhuoer
> announced PRC operations would wind down. These are
> named primary_corporate actions cited via journalism
> in this DRYRUN pass; replayable announcement anchors
> (body_hash + Wayback) are deferred to human-audit.
- **`supporting_journalism`**
  - URL: <https://www.cnbc.com/2021/05/21/bitcoin-falls-after-china-calls-for-crackdown-on-bitcoin-mining-and-trading-behavior.html>
  - Wayback: <https://web.archive.org/web/2021/https://www.cnbc.com/2021/05/21/bitcoin-falls-after-china-calls-for-crackdown-on-bitcoin-mining-and-trading-behavior.html>
  > CNBC 2021-05-21 market-reaction coverage; cited again
> here at observation level for the intra-day BTC spot
> price decline that followed circulation of the
> statement.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`china-pboc-crypto-ban-2021`](./china-pboc-crypto-ban-2021.md)
- [`china-inner-mongolia-mining-ban-2021-05`](./china-inner-mongolia-mining-ban-2021-05.md)
- [`china-sichuan-mining-ban-2021-06`](./china-sichuan-mining-ban-2021-06.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `7542617`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

