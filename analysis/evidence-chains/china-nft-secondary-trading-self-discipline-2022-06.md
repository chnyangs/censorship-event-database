# Evidence chain — `china-nft-secondary-trading-self-discipline-2022-06`

**Status**: `admitted` · **Stratum**: `S4_nation_state` · **Shape**: `comparison` (1 changed layer(s): `l4_frontend`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `b3ed1c5` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-21` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> On 2022-06-30, three PRC industry self-regulatory bodies (China
> Banking Association, Internet Society of China, Securities
> Association of China) issued a 14-article self-discipline
> initiative co-signed by approximately 30 platform signatories
> (including Tencent Huanhe and Alibaba/Ant Group Phoenix) that
> banned secondary trading of NFTs ("digital collectibles") and
> restricted primary sales to RMB-denominated, real-name-authenticated
> flows on permissioned consortium chains. Observational axes at
> l4_frontend (secondary-trading UI removal) and asset_onchain
> (issuance restricted to primary-only). Admission-anchor-grade
> promotion pending pinned platform / consortium-chain artifacts.

## 1. Trigger

- **Type**: `nation_state_block`
- **Actor**: `CN_BANKING_ASSOC + CN_INTERNET_SOC + CN_SAC`
- **Timestamp**: `2022-06-30 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`supporting_journalism`**
  - URL: <https://www.scmp.com/tech/big-tech/article/3184021/china-nfts-tencent-and-ant-group-join-industry-pledge-ban>
  - Wayback: <https://web.archive.org/web/2022/https://www.scmp.com/tech/big-tech/article/3184021/china-nfts-tencent-and-ant-group-join-industry-pledge-ban>
  > South China Morning Post 2022-06-30 reporting on the "Digital
> Collectible Industry Self-Discipline Development Initiative"
> signed by approximately 30 Chinese firms and institutions
> including Tencent, Ant Group, JD.com, and Baidu. The pact's
> 14 articles ban secondary trading of NFTs ("digital
> collectibles"), require real-name authentication for issuers,
> sellers, and buyers, and restrict denomination/settlement to
> RMB legal tender. Issued under the umbrella of three
> industry self-regulatory bodies (China Banking Association,
> Internet Society of China, Securities Association of China)
> coordinating with the Chinese Cultural Industry Association.
> Wayback wildcard pointer in lieu of pinned-timestamp snapshot;
> evidence_use=contextual_unarchived because no body_hash+body_path
> pair has been captured into
> sources/http_captures/china-nft-secondary-trading-self-discipline-2022-06/
> in this session.
- **`supporting_journalism`**
  - URL: <https://www.euronews.com/next/2022/06/30/china-tech-nfts>
  - Wayback: <https://web.archive.org/web/2022/https://www.euronews.com/next/2022/06/30/china-tech-nfts>
  > Euronews / Reuters 2022-06-30 reporting confirming Chinese tech
> giants' pledge to halt NFT secondary trading. Wayback wildcard
> pointer in lieu of pinned snapshot.
- **`supporting_journalism`**
  - URL: <https://www.asiafinancial.com/chinas-big-tech-groups-pledge-to-help-ban-nft-trading>
  - Wayback: <https://web.archive.org/web/2022/https://www.asiafinancial.com/chinas-big-tech-groups-pledge-to-help-ban-nft-trading>
  > Asia Financial 2022-06-30 corroboration of the self-discipline
> initiative, naming the three industry associations and listing
> platform-level signatories. Wayback wildcard pointer in lieu of
> pinned snapshot.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: PRC digital-collectibles platforms (Tencent Huanhe, Alibaba Phoenix, JD Lingxi, Baidu, etc.)
- **Canonical domains**: `h.qq.com`, `jingtan.taobao.com`

> PRC NFT ("digital collectibles") permissioned-platform cohort
> bound by the self-discipline initiative. Named platform signatories
> include Tencent Huanhe (幻核), Alibaba/Ant Group Phoenix (鲸探),
> JD.com Lingxi (灵稀), and Baidu's digital collectibles platform.
> Subset rather than complete: approximately 30 firms and institutes
> are reported as signatories but the full enumeration is not yet
> pinned to a primary-source signatory list in this session.

## 3. Changed-layer observations (supports the scoped claim)

### l4_frontend · attribution: `plausible` · Δt = 0h

**Event label**: `secondary_trading_ui_removed_on_permissioned_nft_platforms`

**Timestamp**: `2022-06-30 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`semi_primary_wayback`**
  - URL: <https://www.scmp.com/tech/big-tech/article/3184021/china-nfts-tencent-and-ant-group-join-industry-pledge-ban>
  - Wayback: <https://web.archive.org/web/20220704063908/https://www.scmp.com/tech/big-tech/article/3184021/china-nfts-tencent-and-ant-group-join-industry-pledge-ban>
  - body_hash: `sha256:ac27466af354d93275c187d729312d84c215a3aadb3effde9fb4742cee08006c`
  - body_path: `sources/http_captures/china-nft-secondary-trading-self-discipline-2022-06/primary/web.archive.org__web-20220704063908-https-www.scmp.com-tech-big-tech-article-3184021-china-nfts-tencent-and-ant-group-join-industry-pledge-ban__78af278bf5.html`
  > SCMP 2022-06-30 reporting that Tencent, Ant Group, and other
> signatories committed to halting secondary-trading flows for
> digital collectibles on their permissioned-platform frontends
> and to restricting primary sales to RMB-denominated payments
> with real-name authentication. Attribution=plausible because
> the initiative is industry self-regulation under state
> direction rather than a binding state order, and per-platform
> UI-removal Wayback diffs are not pinned in this session.
- **`semi_primary_wayback`**
  - URL: <https://www.euronews.com/next/2022/06/30/china-tech-nfts>
  - Wayback: <https://web.archive.org/web/20230927063655/https://www.euronews.com/next/2022/06/30/china-tech-nfts>
  - body_hash: `sha256:38ea040ca96c51a7a274657321492ad5e29312623b3290e0f5d143eaf677affd`
  - body_path: `sources/http_captures/china-nft-secondary-trading-self-discipline-2022-06/primary/web.archive.org__web-20230927063655-https-www.euronews.com-next-2022-06-30-china-tech-nfts__192df1ba93.html`
  > Euronews / Reuters 2022-06-30 confirmation of the
> secondary-trading halt pledge from PRC tech-platform
> signatories.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`china-pboc-crypto-ban-2021`](./china-pboc-crypto-ban-2021.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `b3ed1c5`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

