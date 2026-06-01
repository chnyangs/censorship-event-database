# Evidence chain — `china-ndrc-mining-eliminated-industry-notice-2021-09`

**Status**: `admitted` · **Stratum**: `S4_nation_state` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-02` · **Source commit**: `60f1d90` · **Schema**: `0.2.0` · **Event last_verified**: `2026-06-02` · **Tool version**: `0.1.0` · **Generated**: `2026-06-02T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "On 2021-09-24 China's NDRC issued a notice ordering the cryptocurrency-mining industry
> phased out / treated as an eliminated industry and its financial/investment/electricity/tax
> support channels cut. Effect carried at offramp_cex (class-level support severance, measured
> via captured official NDRC pages); l1_consensus hashrate effect is not newly measured here."

## 1. Trigger

- **Type**: `nation_state_block`
- **Actor**: `CN_NDRC`
- **Timestamp**: `2021-09-24 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_government`**
  - URL: <https://www.ndrc.gov.cn/xxgk/zcfb/tz/202109/t20210924_1297474.html>
  - body_hash: `sha256:1ca312cc544d16e6f582911da15e9f65531a965b126423876aa39fcde8095023`
  - body_path: `sources/http_captures/china-ndrc-mining-eliminated-industry-notice-2021-09/primary-ndrc-notice/www.ndrc.gov.cn__xxgk-zcfb-tz-202109-t20210924_1297474.html__fd9fe59fce.html`
  > Official National Development and Reform Commission notice
> "关于整治虚拟货币“挖矿”活动的通知(发改运行〔2021〕1283号)",
> issued by NDRC and ten other departments. The notice orders
> whole-chain regulation of virtual-currency mining, prohibits new
> mining projects, requires orderly exit of existing projects, treats
> mining as an eliminated industry, restricts electricity connections
> and supply, and bars fiscal/financial support and financial services
> for mining projects. Captured live from ndrc.gov.cn on 2026-06-02.
- **`primary_government`**
  - URL: <https://www.ndrc.gov.cn/xxgk/jd/jd/202109/t20210924_1297478.html>
  - body_hash: `sha256:574e87be343b08784b36be665ad885583a6747ce842dc1ee475debf732508369`
  - body_path: `sources/http_captures/china-ndrc-mining-eliminated-industry-notice-2021-09/primary-ndrc-repair/www.ndrc.gov.cn__xxgk-jd-jd-202109-t20210924_1297478.html__c6b5d23876.html`
  > Official NDRC Q&A published 2021-09-24 explaining the same
> Notice. It confirms the eleven-department issuance, the "严禁增量、
> 妥处存量" policy, the ban on new mining investment, the orderly
> exit of existing projects, eliminated-industry treatment, electricity
> restrictions, and withdrawal of fiscal and financial support.
- **`primary_government`**
  - URL: <https://www.gov.cn/zhengce/zhengceku/2021-09/25/content_5639225.htm>
  - body_hash: `sha256:1e5fd8a3c88524a574c1fa3ebad59fd2bbf23115786d608fe658347b48a04619`
  - body_path: `sources/http_captures/china-ndrc-mining-eliminated-industry-notice-2021-09/primary-ndrc-repair/www.gov.cn__zhengce-zhengceku-2021-09-25-content_5639225.htm__41b5b19af7.html`
  > Official State Council / gov.cn departmental-file mirror of the
> same NDRC-led Notice 发改运行〔2021〕1283号. Retained as a durable
> government mirror for the full notice text and issuing-agency list.
- **`supporting_journalism`**
  - URL: <https://www.coindesk.com/policy/2021/09/24/china-tightens-crypto-mining-crackdown-bans-trading>
  - Wayback: <https://web.archive.org/web/20210925053628/https://www.coindesk.com/policy/2021/09/24/china-tightens-crypto-mining-crackdown-bans-trading/>
  - body_hash: `sha256:b505020728a83401e6239e5abc8dffcf164838a7254c78a93d8af14abf8541a9`
  - body_path: `sources/http_captures/china-ndrc-mining-eliminated-industry-notice-2021-09/primary/web.archive.org__web-20210925053628-https-www.coindesk.com-policy-2021-09-24-china-tightens-crypto-mining-crackdown-bans-trading__98e697480d.html`
  > CoinDesk, 2021-09-24, "China Tightens Crypto Mining Crackdown, Bans Trading."
> Reports that China's top state-planning body, the National Development and Reform
> Commission (NDRC), posted a separate "Notice on Rectifying Virtual Currency Mining."
> The notice aims to dispose of the "hidden risks" in crypto mining as China pursues
> its carbon-neutrality goals; while it does not outlaw mining outright, it orders local
> authorities to clamp down on illegal mining and to gradually phase out the industry —
> mining is to be deemed an "outdated" industry. The captured article additionally
> documents that the same day a parallel inter-agency PBOC notice declared all crypto
> transactions illegal (that parallel action is a SEPARATE corpus event,
> china-pboc-crypto-ban-2021; this event is scoped strictly to the NDRC mining notice).
> Wayback snapshot 20210925053628 (replayable body_hash).

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: Chinese cryptocurrency mining enterprises + their financial/energy support channels (class)
- **Chains**: `bitcoin`

> The Chinese cryptocurrency-mining industry as a class — operators, and the financial /
> investment / electricity / tax support channels that sustain them. The NDRC notice
> directs the industry to be phased out (deemed an "outdated" industry) and orders local
> authorities to cut off support to mining enterprises. Class-level target; no enumerated
> roster of mining firms in the captured source. enumeration=subset.

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `direct` · Δt = 0h

**Event label**: `ndrc_ordered_phase_out_and_support_severance_for_mining_industry`

**Timestamp**: `2021-09-24 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_government`**
  - URL: <https://www.ndrc.gov.cn/xxgk/zcfb/tz/202109/t20210924_1297474.html>
  - body_hash: `sha256:1ca312cc544d16e6f582911da15e9f65531a965b126423876aa39fcde8095023`
  - body_path: `sources/http_captures/china-ndrc-mining-eliminated-industry-notice-2021-09/primary-ndrc-notice/www.ndrc.gov.cn__xxgk-zcfb-tz-202109-t20210924_1297474.html__fd9fe59fce.html`
  > Official NDRC notice 发改运行〔2021〕1283号 orders strict monitoring
> and regulation of virtual-currency mining, bans new mining projects,
> accelerates orderly exit of existing projects, treats mining as an
> eliminated industry, restricts electricity connections/supply, and
> stops fiscal/financial support and financial services for mining
> projects. attribution=direct because the state actor's own notice is
> the restriction being coded.
- **`primary_government`**
  - URL: <https://www.ndrc.gov.cn/xxgk/jd/jd/202109/t20210924_1297478.html>
  - body_hash: `sha256:574e87be343b08784b36be665ad885583a6747ce842dc1ee475debf732508369`
  - body_path: `sources/http_captures/china-ndrc-mining-eliminated-industry-notice-2021-09/primary-ndrc-repair/www.ndrc.gov.cn__xxgk-jd-jd-202109-t20210924_1297478.html__c6b5d23876.html`
  > Official NDRC Q&A confirms the Notice's concrete measures for new
> and existing mining projects: eliminated-industry treatment,
> prohibition on new investment, restrictions on electricity supply,
> withdrawal of fiscal/financial support, and stopping financial
> services to mining projects.
- **`supporting_journalism`**
  - URL: <https://www.coindesk.com/policy/2021/09/24/china-tightens-crypto-mining-crackdown-bans-trading>
  - Wayback: <https://web.archive.org/web/20210925053628/https://www.coindesk.com/policy/2021/09/24/china-tightens-crypto-mining-crackdown-bans-trading/>
  - body_hash: `sha256:b505020728a83401e6239e5abc8dffcf164838a7254c78a93d8af14abf8541a9`
  - body_path: `sources/http_captures/china-ndrc-mining-eliminated-industry-notice-2021-09/primary/web.archive.org__web-20210925053628-https-www.coindesk.com-policy-2021-09-24-china-tightens-crypto-mining-crackdown-bans-trading__98e697480d.html`
  > CoinDesk 2021-09-24: NDRC "Notice on Rectifying Virtual Currency Mining" orders the
> industry phased out (deemed "outdated") and support channels (financial, investment,
> electricity, tax) cut. Retained as English-language contemporaneous
> corroboration; the primary NDRC pages above are now load-bearing.

## 5. Honest coverage gaps

- **l1_consensus** (`not_measured`): The notice's downstream effect manifests in global Bitcoin hashrate (China-hosted

## 7. Related events

- [`china-state-council-mining-crackdown-2021-05`](./china-state-council-mining-crackdown-2021-05.md)
- [`china-sichuan-mining-ban-2021-06`](./china-sichuan-mining-ban-2021-06.md)
- [`china-pboc-crypto-ban-2021`](./china-pboc-crypto-ban-2021.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `60f1d90`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

