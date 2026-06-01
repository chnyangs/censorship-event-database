# Evidence chain — `thailand-sec-meme-fan-nft-exchange-token-ban-2021-06`

**Status**: `admitted` · **Stratum**: `S4_nation_state` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `143c3a7` · **Schema**: `0.2.0` · **Event last_verified**: `2026-06-01` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T12:56:36Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "On 2021-06-11 the Thai SEC prohibited SEC-licensed digital-asset exchanges
> from listing or trading meme tokens, fan tokens, NFTs and exchange-issued
> tokens, requiring delisting / listing-rule revision within 30 days. Effect
> captured at the offramp_cex layer at class level via the official SEC
> release."

## 1. Trigger

- **Type**: `regulatory_enforcement`
- **Actor**: `TH_SEC`
- **Timestamp**: `2021-06-11 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_government`**
  - URL: <https://www.sec.or.th/EN/Pages/News_Detail.aspx?SECID=8994>
  - Wayback: <https://web.archive.org/web/20210613190001/https://www.sec.or.th/EN/Pages/News_Detail.aspx?SECID=8994>
  - body_hash: `sha256:482e94e3ddc1b77d51f615cd80f40444db8f3b183f5bfbcb99eb1676a62e0c45`
  - body_path: `sources/http_captures/thailand-sec-meme-fan-nft-exchange-token-ban-2021-06/official-sec/web.archive.org__web-20210613190001id_-https-www.sec.or.th-EN-Pages-News_Detail.aspx__23a08a3b6b.html`
  > Thai Securities and Exchange Commission news release No. 114/2021,
> dated Saturday 2021-06-12 and datelined Bangkok 2021-06-11. The
> captured official SEC body states that SEC Board Meeting No. 12/2564
> approved Notification No. Kor Thor. 18/2564; that after Government
> Gazette publication the notification became effective from 2021-06-11
> without retrospective effect; that digital asset exchanges are
> prohibited from providing services for meme tokens, fan tokens, NFTs,
> and blockchain-transaction tokens issued by exchanges or related
> persons; and that exchanges must revise listing rules within 30 days.
> Live sec.or.th blocked the local capture agent with HTTP 403, so the
> replayable artifact is the earliest available 2021-06-13 Wayback
> memento of the official SEC page.
- **`supporting_journalism`**
  - URL: <https://www.coindesk.com/markets/2021/06/12/no-doge-allowed-thai-sec-bans-meme-fan-and-exchange-tokens-as-well-as-nfts>
  - Wayback: <https://web.archive.org/web/20210927215039/https://www.coindesk.com/markets/2021/06/12/no-doge-allowed-thai-sec-bans-meme-fan-and-exchange-tokens-as-well-as-nfts/>
  - body_hash: `sha256:c51487aa44a751e3b92c62bfbd98f861ceb2d9fa661dc2a7e987eb907ad314d9`
  - body_path: `sources/http_captures/thailand-sec-meme-fan-nft-exchange-token-ban-2021-06/primary/web.archive.org__web-20210612000000-https-www.coindesk.com-markets-2021-06-12-no-doge-allowed-thai-sec-bans-meme-fan-and-exchange-tokens-as-well-as-nfts__d3f6abfc5f.html`
  > CoinDesk, "No DOGE Allowed? Thai SEC Bans Meme, Fan and Exchange Tokens
> as Well as NFTs" (article dated 2021-06-12, reporting the Thai SEC's
> 2021-06-11 board decision). Thailand's Securities and Exchange Commission
> prohibited SEC-licensed digital-asset exchanges from listing or trading
> four token categories: (1) meme tokens (no clear objective/substance,
> price driven by social-media trends), (2) fan tokens tokenising the fame
> of influencers, (3) non-fungible tokens (NFTs), and (4) digital tokens
> issued by digital-asset exchanges or related persons (exchange tokens).
> Licensed exchanges were given 30 days from the effective date to revise
> their listing rules to comply (i.e. delist non-compliant tokens). The ban
> is prospective (no retroactive effect on tokens already listed prior).
> Captured HTML verified to contain "Thai SEC", the four token categories,
> and the 30-day compliance window. Archived via Wayback 2021-09-27.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: Thai SEC-licensed digital-asset exchanges (class)

> Thai SEC-licensed digital-asset exchanges as a class, and the meme / fan /
> NFT / exchange-issued token categories they could previously list. No
> individual exchange or token is enumerated in the order; the prohibition
> binds all licensed exchanges. Treated as entity-class-level.

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `direct` · Δt = 0h

**Event label**: `meme_fan_nft_exchange_tokens_delisting_mandated`

**Timestamp**: `2021-06-11 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_government`**
  - URL: <https://www.sec.or.th/EN/Pages/News_Detail.aspx?SECID=8994>
  - Wayback: <https://web.archive.org/web/20210613190001/https://www.sec.or.th/EN/Pages/News_Detail.aspx?SECID=8994>
  - body_hash: `sha256:482e94e3ddc1b77d51f615cd80f40444db8f3b183f5bfbcb99eb1676a62e0c45`
  - body_path: `sources/http_captures/thailand-sec-meme-fan-nft-exchange-token-ban-2021-06/official-sec/web.archive.org__web-20210613190001id_-https-www.sec.or.th-EN-Pages-News_Detail.aspx__23a08a3b6b.html`
  > Official Thai SEC No. 114/2021 release. The captured body identifies
> Notification No. Kor Thor. 18/2564, its 2021-06-11 effective date,
> the four prohibited categories (meme token, fan token, NFT, and
> exchange-/related-person-issued blockchain transaction tokens), and
> the requirement that digital asset exchanges revise their listing
> rules within 30 days. attribution=direct: the regulator's own release
> names both the regulated exchange class and the prohibited token
> categories.
- **`supporting_journalism`**
  - URL: <https://www.coindesk.com/markets/2021/06/12/no-doge-allowed-thai-sec-bans-meme-fan-and-exchange-tokens-as-well-as-nfts>
  - Wayback: <https://web.archive.org/web/20210927215039/https://www.coindesk.com/markets/2021/06/12/no-doge-allowed-thai-sec-bans-meme-fan-and-exchange-tokens-as-well-as-nfts/>
  - body_hash: `sha256:c51487aa44a751e3b92c62bfbd98f861ceb2d9fa661dc2a7e987eb907ad314d9`
  - body_path: `sources/http_captures/thailand-sec-meme-fan-nft-exchange-token-ban-2021-06/primary/web.archive.org__web-20210612000000-https-www.coindesk.com-markets-2021-06-12-no-doge-allowed-thai-sec-bans-meme-fan-and-exchange-tokens-as-well-as-nfts__d3f6abfc5f.html`
  > CoinDesk report on the Thai SEC's 2021-06-11 prohibition ordering
> licensed exchanges to delist/refuse meme, fan, NFT and exchange-issued
> tokens within 30 days. Retained as same-week corroboration for the
> official SEC anchor.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`thailand-sec-binance-bybit-c-and-d-2021`](./thailand-sec-binance-bybit-c-and-d-2021.md)
- [`thailand-bot-bitcoin-prohibition-2013`](./thailand-bot-bitcoin-prohibition-2013.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `143c3a7`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

