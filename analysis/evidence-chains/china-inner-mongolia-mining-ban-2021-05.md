# Evidence chain — `china-inner-mongolia-mining-ban-2021-05`

**Status**: `admitted` · **Stratum**: `S4_nation_state` · **Shape**: `comparison` (1 changed layer(s): `l1_consensus`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `7542617` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-21` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "On 2021-05-25, the Inner Mongolia Autonomous Region Development and
> Reform Commission published a draft enforcement notice
> ('Eight Measures on Resolutely Investigating, Punishing and
> Rectifying Virtual Currency Mining Behavior') enumerating four
> classes of mining-related targets, announcing a public reporting
> hotline + email channel for citizens, and specifying penalties
> (power-trading bans, business-license revocations, enterprise
> shutdowns). The notice operationalizes the 2021-02-25 Inner
> Mongolia NDRC mandate that all bitcoin mining cease by end of
> April 2021 and is the first concrete province-level enforcement
> framework in the 2021 CN mining-ban cascade. Observational axis at
> l1_consensus (attribution=direct on the policy-instrument anchor;
> downstream physical-effect observations such as mining-rig
> confiscations and hashrate migration are documented in
> contemporaneous reporting but not load-bearing in this scoped
> claim). Admission-anchor-grade promotion pending pinned archive
> captures."

## 1. Trigger

- **Type**: `nation_state_block`
- **Actor**: `CN_INNER_MONGOLIA_NDRC`
- **Timestamp**: `2021-05-25 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://fgw.nmg.gov.cn/>
  - Wayback: <https://web.archive.org/web/2021/https://fgw.nmg.gov.cn/>
  > Inner Mongolia Autonomous Region Development and Reform Commission
> (内蒙古自治区发展和改革委员会) draft notice "Eight Measures on
> Resolutely Investigating, Punishing and Rectifying Virtual
> Currency 'Mining' Behavior" (关于坚决查处惩戒整治虚拟货币
> "挖矿"行为八项措施(征求意见稿)), issued 2021-05-25 with a
> public-comment window 2021-05-25 to 2021-06-01. The notice
> enumerates four crackdown target classes (mining enterprises;
> miners disguised as data centres; landlords housing mining
> activities; entities obtaining electricity illegally for mining)
> and announces a public reporting hotline + email address for
> citizens to report mining operations. This follows a 2021-02-25
> Inner Mongolia NDRC notice ordering all mining to cease by end of
> April 2021. DRYRUN: wayback wildcard pointer in lieu of pinned
> snapshot of the Inner Mongolia NDRC origin page (the draft notice
> was hosted on the regional NDRC site at fgw.nmg.gov.cn and the
> pinned-page URL is not yet captured in this session);
> evidence_use=contextual_unarchived per validator policy.
- **`supporting_journalism`**
  - URL: <https://www.coindesk.com/policy/2021/05/25/inner-mongolia-outlines-how-it-may-ban-crypto-mining/>
  - Wayback: <https://web.archive.org/web/2021/https://www.coindesk.com/policy/2021/05/25/inner-mongolia-outlines-how-it-may-ban-crypto-mining/>
  > CoinDesk 2021-05-25 coverage: "Inner Mongolia Outlines How It May
> Ban Crypto Mining." Confirms the Inner Mongolia NDRC draft notice
> date (2021-05-25), the public-comment window (2021-05-25 to
> 2021-06-01), the four enumerated crackdown target classes, and
> the existence of a public reporting channel (hotline + email)
> for citizens to report mining operations. DRYRUN wayback
> wildcard pointer.
- **`supporting_journalism`**
  - URL: <https://www.scmp.com/economy/china-economy/article/3134058/chinas-cryptocurrency-crackdown-sees-inner-mongolia-call>
  - Wayback: <https://web.archive.org/web/2021/https://www.scmp.com/economy/china-economy/article/3134058/chinas-cryptocurrency-crackdown-sees-inner-mongolia-call>
  > South China Morning Post 2021-05-25 coverage on Inner Mongolia
> calling on the public to report illegal mining operations.
> Independent corroboration of the public-reporting-hotline
> mechanism. DRYRUN wayback wildcard pointer.
- **`supporting_journalism`**
  - URL: <https://www.cnbc.com/2021/05/26/major-china-bitcoin-mining-hub-lays-out-harsher-crackdown-measures.html>
  - Wayback: <https://web.archive.org/web/2021/https://www.cnbc.com/2021/05/26/major-china-bitcoin-mining-hub-lays-out-harsher-crackdown-measures.html>
  > CNBC 2021-05-26 coverage: "Major bitcoin mining region in China
> sets tough penalties for cryptocurrency activities." Confirms
> penalty schedule (banning offenders from regional power-trading
> scheme, revoking business licenses, shutting businesses down)
> targeting industrial parks, data centres, telecoms companies,
> internet firms, and cybercafes. DRYRUN wayback wildcard pointer.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: Inner Mongolia Autonomous Region Development and Reform Commission (内蒙古自治区发展和改革委员会)
- **Chains**: `bitcoin`

> Sub-national (province-level) policy directive targeting cryptocurrency
> mining operations physically located within the Inner Mongolia
> Autonomous Region. Subset because the enumerated targets are the four
> crackdown target classes named in the 2021-05-25 NDRC draft notice:
> (1) mining enterprises, (2) miners disguised as data centres /
> industrial parks claiming preferential tax/land/energy policies,
> (3) landlords housing mining operations, and (4) entities obtaining
> electricity supply illegally for mining. The broader class of all
> bitcoin mining hashpower physically located in Inner Mongolia is
> the implicit exclusion target. Jurisdiction stays [CN] but actor is
> province-level (Inner Mongolia Autonomous Region NDRC), not the
> central PRC government.

## 3. Changed-layer observations (supports the scoped claim)

### l1_consensus · attribution: `plausible` · Δt = 0h

**Event label**: `inner_mongolia_provincial_mining_ban_enforcement_notice_published_with_public_reporting_hotline`

**Timestamp**: `2021-05-25 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_legal`**
  - URL: <https://fgw.nmg.gov.cn/>
  - Wayback: <https://web.archive.org/web/2021/https://fgw.nmg.gov.cn/>
  > Inner Mongolia NDRC 2021-05-25 draft notice constitutes the
> enforcement-framework anchor for the provincial mining-ban
> regime: it enumerates the four target classes, specifies the
> public reporting hotline + email channel, and announces
> penalties (power-trading ban, business-license revocation,
> enterprise shutdown). attribution=direct: the published
> enforcement notice is the observed change itself at the
> policy-instrument layer; the load-bearing physical-effect
> observation (mining-rig confiscations, hashrate-migration) is
> a downstream cascade well-documented in 2021-Q2/Q3 reporting
> (CryptoPotato: "Over 10,000 Mining Rigs Confiscated in Inner
> Mongolia"; Forkast: bitcoin miners fleeing Inner Mongolia
> ahead of crypto mining ban). DRYRUN: wayback wildcard pointer
> in lieu of pinned snapshot of the Inner Mongolia NDRC origin
> page; pinned-snapshot + body_hash capture deferred to human
> audit.
- **`semi_primary_wayback`**
  - URL: <https://www.coindesk.com/policy/2021/05/25/inner-mongolia-outlines-how-it-may-ban-crypto-mining/>
  - Wayback: <https://web.archive.org/web/20211009120544/https://www.coindesk.com/policy/2021/05/25/inner-mongolia-outlines-how-it-may-ban-crypto-mining/>
  - body_hash: `sha256:3653ba7dd17cb7227fd62bbb1afcf73cfc291620fb8124aa77899f6457f44b6f`
  - body_path: `sources/http_captures/china-inner-mongolia-mining-ban-2021-05/primary/web.archive.org__web-20211009120544-https-www.coindesk.com-policy-2021-05-25-inner-mongolia-outlines-how-it-may-ban-crypto-mining__a6d5cd5aca.html`
  > CoinDesk 2021-05-25 contemporaneous coverage confirming notice
> date, target classes, public-comment window, and reporting
> channel. DRYRUN wayback wildcard pointer.
- **`semi_primary_wayback`**
  - URL: <https://www.cnbc.com/2021/05/26/major-china-bitcoin-mining-hub-lays-out-harsher-crackdown-measures.html>
  - Wayback: <https://web.archive.org/web/20210526031619/https://www.cnbc.com/2021/05/26/major-china-bitcoin-mining-hub-lays-out-harsher-crackdown-measures.html>
  - body_hash: `sha256:39cc001b9025c12bceebf5ed9ab2474d22db86b24c318cce8dab746b0b177c02`
  - body_path: `sources/http_captures/china-inner-mongolia-mining-ban-2021-05/primary/web.archive.org__web-20210526031619-https-www.cnbc.com-2021-05-26-major-china-bitcoin-mining-hub-lays-out-harsher-crackdown-measures.html__b5996837bb.html`
  > CNBC 2021-05-26 contemporaneous coverage of the Inner Mongolia
> harsher-crackdown measures. Independent semi-primary anchor.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`china-pboc-crypto-ban-2021`](./china-pboc-crypto-ban-2021.md)
- [`china-state-council-mining-crackdown-2021-05`](./china-state-council-mining-crackdown-2021-05.md)
- [`china-sichuan-mining-ban-2021-06`](./china-sichuan-mining-ban-2021-06.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `7542617`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

