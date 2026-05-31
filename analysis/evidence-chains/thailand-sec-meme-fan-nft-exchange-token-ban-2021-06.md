# Evidence chain — `thailand-sec-meme-fan-nft-exchange-token-ban-2021-06`

**Status**: `admitted` · **Stratum**: `S4_nation_state` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `22e4579` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-31` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "On 2021-06-11 the Thai SEC prohibited SEC-licensed digital-asset exchanges
> from listing or trading meme tokens, fan tokens, NFTs and exchange-issued
> tokens, requiring delisting / listing-rule revision within 30 days. Effect
> captured at the offramp_cex layer at class level via same-week journalism
> reporting the SEC decision."

## 1. Trigger

- **Type**: `regulatory_enforcement`
- **Actor**: `TH_SEC`
- **Timestamp**: `2021-06-11 00:00:00+00:00` (precision: `day`)

### Trigger citations

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

### offramp_cex · attribution: `plausible` · Δt = 0h

**Event label**: `meme_fan_nft_exchange_tokens_delisting_mandated`

**Timestamp**: `2021-06-11 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`supporting_journalism`**
  - URL: <https://www.coindesk.com/markets/2021/06/12/no-doge-allowed-thai-sec-bans-meme-fan-and-exchange-tokens-as-well-as-nfts>
  - Wayback: <https://web.archive.org/web/20210927215039/https://www.coindesk.com/markets/2021/06/12/no-doge-allowed-thai-sec-bans-meme-fan-and-exchange-tokens-as-well-as-nfts/>
  - body_hash: `sha256:c51487aa44a751e3b92c62bfbd98f861ceb2d9fa661dc2a7e987eb907ad314d9`
  - body_path: `sources/http_captures/thailand-sec-meme-fan-nft-exchange-token-ban-2021-06/primary/web.archive.org__web-20210612000000-https-www.coindesk.com-markets-2021-06-12-no-doge-allowed-thai-sec-bans-meme-fan-and-exchange-tokens-as-well-as-nfts__d3f6abfc5f.html`
  > CoinDesk report on the Thai SEC's 2021-06-11 prohibition ordering
> licensed exchanges to delist/refuse meme, fan, NFT and exchange-issued
> tokens within 30 days. attribution=direct: the SEC is the named
> regulator and the order names the prohibited token categories and the
> regulated exchanges that must comply. Primary SEC release not separately
> captured; the journalism source is the load-bearing evidence for this
> draft.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`thailand-sec-binance-bybit-c-and-d-2021`](./thailand-sec-binance-bybit-c-and-d-2021.md)
- [`thailand-bot-bitcoin-prohibition-2013`](./thailand-bot-bitcoin-prohibition-2013.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `22e4579`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

