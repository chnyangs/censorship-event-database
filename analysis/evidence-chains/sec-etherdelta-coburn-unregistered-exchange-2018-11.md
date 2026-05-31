# Evidence chain — `sec-etherdelta-coburn-unregistered-exchange-2018-11`

**Status**: `admitted` · **Stratum**: `S3_doj_sec_cftc_fiod` · **Shape**: `comparison` (1 changed layer(s): `l4_frontend`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `8583894` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-31` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "The 2018-11-08 SEC settled order against Zachary Coburn for operating
> EtherDelta as an unregistered national securities exchange (order-book
> website + Ethereum smart contract) is the first SEC action treating a DEX /
> smart-contract order book as an unregistered exchange. Effect carried at
> l4_frontend (trading-frontend restriction), attribution=direct.
> Comparable-main tier."

## 1. Trigger

- **Type**: `sec_action`
- **Actor**: `US_SEC`
- **Timestamp**: `2018-11-08 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_government`**
  - URL: <https://web.archive.org/web/20181109000000/https://www.sec.gov/news/press-release/2018-258>
  - Wayback: <https://web.archive.org/web/20181109010148/https://www.sec.gov/news/press-release/2018-258>
  - body_hash: `sha256:79bb92ec4ab7497cfdc9461c1c3f26311760b1e398c09efee9ef0e690745ca4b`
  - body_path: `sources/http_captures/sec-etherdelta-coburn-unregistered-exchange-2018-11/primary/web.archive.org__web-20181109000000-https-www.sec.gov-news-press-release-2018-258__5a2a0563a9.html`
  > SEC press release 2018-258 (2018-11-08): "SEC Charges EtherDelta
> Founder With Operating an Unregistered Exchange." Settled charges
> against Zachary Coburn, founder of EtherDelta — an online platform for
> secondary-market trading of ERC20 tokens combining an order book, a
> website that displayed orders, and a smart contract on Ethereum. The
> SEC found EtherDelta operated as an unregistered national securities
> exchange; over ~18 months users executed 3.6 million+ orders for ERC20
> tokens including securities. Coburn consented (without admit/deny) to
> $300,000 disgorgement + $13,000 interest + $75,000 penalty. First SEC
> enforcement action treating a decentralized token-trading platform /
> DEX as an unregistered exchange. Wayback memento 20181109010148 pinned;
> captured body contains "EtherDelta", "Coburn", "unregistered national
> securities exchange", "ERC20", "3.6 million", "smart contract".

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Protocol**: `etherdelta`
- **Actor name**: EtherDelta / Zachary Coburn
- **Chains**: `ethereum`
- **Canonical domains**: `etherdelta.com`

> Zachary Coburn (founder/operator of EtherDelta) and the EtherDelta
> trading platform (order book + order-display website + Ethereum smart
> contract). Subset: the named founder + the platform he operated, not an
> enumeration of the platform's users or the ERC20 token set traded.

## 3. Changed-layer observations (supports the scoped claim)

### l4_frontend · attribution: `direct` · Δt = 0h

**Event label**: `sec_charges_etherdelta_operator_unregistered_securities_exchange`

**Timestamp**: `2018-11-08 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_government`**
  - URL: <https://web.archive.org/web/20181109000000/https://www.sec.gov/news/press-release/2018-258>
  - Wayback: <https://web.archive.org/web/20181109010148/https://www.sec.gov/news/press-release/2018-258>
  - body_hash: `sha256:79bb92ec4ab7497cfdc9461c1c3f26311760b1e398c09efee9ef0e690745ca4b`
  - body_path: `sources/http_captures/sec-etherdelta-coburn-unregistered-exchange-2018-11/primary/web.archive.org__web-20181109000000-https-www.sec.gov-news-press-release-2018-258__5a2a0563a9.html`
  > SEC press release 2018-258 (2018-11-08). attribution=direct: the SEC's
> own settled order is the operative instrument and names Coburn /
> EtherDelta directly as having operated an unregistered national
> securities exchange (order-book website + Ethereum smart contract).

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`sec-tokenlot-unregistered-broker-2018-09`](./sec-tokenlot-unregistered-broker-2018-09.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `8583894`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

