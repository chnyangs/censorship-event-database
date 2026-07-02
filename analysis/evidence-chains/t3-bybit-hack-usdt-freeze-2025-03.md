# Evidence chain — `t3-bybit-hack-usdt-freeze-2025-03`

**Status**: `admitted` · **Stratum**: `S5_corporate` · **Shape**: `comparison` (1 changed layer(s): `asset_onchain`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-08` · **Source commit**: `ee7bf1a` · **Schema**: `0.2.0` · **Event last_verified**: `2026-06-01` · **Tool version**: `0.1.0` · **Generated**: `2026-06-25T23:48:26Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "T3 FCU/Tether froze a measured subset of Bybit-hack-linked USDT addresses between
> 2025-03-01 and 2025-03-21, with 18 Bybit/LazarusBounty API addresses pinned to
> USDT AddedBlackList receipts on TRON and Ethereum. Tether's 2025-03-26 primary
> announcement reports the broader operation as nearly $9M; this draft carries only
> the pinned subset and remains non-admitted pending human review."

## 1. Trigger

- **Type**: `corporate_policy_change`
- **Actor**: `tether_tron_trm_labs`
- **Timestamp**: `2025-03-01 19:58:24+00:00` (precision: `second`)

### Trigger citations

- **`primary_corporate`**
  - URL: <https://tether.io/news/t3-fcu-freezes-nearly-9-million-linked-to-record-breaking-bybit-hack-bringing-crime-units-total-to-over-150-million/>
  - body_hash: `sha256:0960e54b028e5f6a3bb8d3790c7a993f90a6d05411c5b099325918fd6195374d`
  - body_path: `sources/http_captures/t3-bybit-hack-usdt-freeze-2025-03/primary/tether.io__news-t3-fcu-freezes-nearly-9-million-linked-to-record-breaking-bybit-hack-bringing-crime-units-total-to-over-150-million__d6bb1e1bf7.html`
  > Official Tether.io announcement dated 2025-03-26: T3 Financial Crime Unit
> (Tether + TRON + TRM Labs) announced the successful freezing of nearly
> $9 million connected to the Bybit hack. The same source frames Bybit as
> the record-breaking theft and reports T3 FCU's cumulative freeze total
> exceeding $150M.
- **`semi_primary_measurement`**
  - URL: <https://hackscan.hackbounty.io/public/hack-address.json>
  - body_hash: `sha256:eef1d0d6bca71edc7c27d4131f2548df79787c2318449448c99bab85aa43660f`
  - body_path: `sources/http_captures/t3-bybit-hack-usdt-freeze-2025-03/primary/hackscan.hackbounty.io__public-hack-address.json__dbb3efd2b5.json`
  > Public Bybit/LazarusBounty hacker-address API snapshot. It enumerates
> the Bybit-hack address universe used here to link the 13 TRON and five
> Ethereum blacklist receipts below to the Bybit/Lazarus hack cluster.

## 2. Target

- **Kind**: `address_set`
- **Enumeration**: `subset`
- **Actor name**: Bybit/Lazarus hack wallet cluster (T3 FCU pinned subset)
- **Chains**: `tron`, `ethereum`
- **Addresses**: 18 total (enumerated in event YAML)

> The full T3/Bybit freeze target set is not enumerated by Tether's public
> announcement. This draft pins a measured subset of 18 Bybit/LazarusBounty
> API addresses with USDT blacklist receipts: 13 on TRON and five on
> Ethereum. usdtbanlist tracker balances for the pinned subset sum to
> 7,454,738.93 USDT; Tether's primary-corporate announcement reports the
> broader operation as nearly $9M. The gap is deliberately retained as
> subset enumeration rather than inferred away.

## 3. Changed-layer observations (supports the scoped claim)

### asset_onchain · attribution: `plausible` · Δt = 0h

**Event label**: `t3_fcu_freezes_bybit_hack_usdt_subset`

**Timestamp**: `2025-03-01 19:58:24+00:00` (precision: `second`)

**Sources**:

- **`primary_corporate`**
  - URL: <https://tether.io/news/t3-fcu-freezes-nearly-9-million-linked-to-record-breaking-bybit-hack-bringing-crime-units-total-to-over-150-million/>
  - body_hash: `sha256:0960e54b028e5f6a3bb8d3790c7a993f90a6d05411c5b099325918fd6195374d`
  - body_path: `sources/http_captures/t3-bybit-hack-usdt-freeze-2025-03/primary/tether.io__news-t3-fcu-freezes-nearly-9-million-linked-to-record-breaking-bybit-hack-bringing-crime-units-total-to-over-150-million__d6bb1e1bf7.html`
  > Tether primary-corporate anchor for the T3 FCU / Bybit-hack freeze
> framing and nearly $9M aggregate. Coded plausible rather than direct
> for the row-level observation because the public announcement does
> not enumerate the full address set; the address linkage is supplied
> by the Bybit/LazarusBounty API plus the receipt-level sources below.
- **`semi_primary_measurement`**
  - URL: <https://hackscan.hackbounty.io/public/hack-address.json>
  - body_hash: `sha256:eef1d0d6bca71edc7c27d4131f2548df79787c2318449448c99bab85aa43660f`
  - body_path: `sources/http_captures/t3-bybit-hack-usdt-freeze-2025-03/primary/hackscan.hackbounty.io__public-hack-address.json__dbb3efd2b5.json`
  > Public Bybit/LazarusBounty address-set anchor used to link the
> pinned blacklist receipts to the Bybit/Lazarus hack cluster.
- **`primary_onchain`**
  - URL: <https://tronscan.org/#/transaction/e55f21880eb4b58aace813b1350776b085194af613f3fdd9ff38bd328399fe80>
  - tx_hash: `e55f21880eb4b58aace813b1350776b085194af613f3fdd9ff38bd328399fe80`
  > USDT-TRON AddedBlackList(address) for TEa1NpRPax9KiRXF2WBhcPfU4B8jt8zUiQ,
> 44,974.57 USDT tracker balance, block 70068840 at 2025-03-01 19:58:24 UTC.
- **`primary_onchain`**
  - URL: <https://tronscan.org/#/transaction/c0591a35651d622d19ed27b1e1961dc005e7a84074ecca2012eac4505c296a5e>
  - tx_hash: `c0591a35651d622d19ed27b1e1961dc005e7a84074ecca2012eac4505c296a5e`
  > USDT-TRON AddedBlackList(address) for TPy7UReJj62TDvVhH1CMGYNRdP4kAhT3wy,
> 1,387.43 USDT tracker balance, block 70180719 at 2025-03-05 17:13:51 UTC.
- **`primary_onchain`**
  - URL: <https://tronscan.org/#/transaction/0e0cd72fcbf09fb17d7acff188328c7b6c6734463ef1e266727f523fa284674f>
  - tx_hash: `0e0cd72fcbf09fb17d7acff188328c7b6c6734463ef1e266727f523fa284674f`
  > USDT-TRON AddedBlackList(address) for TLZiKkccnBs2hg21dD55HZJLhQWFEgkjVU,
> 500,001.06 USDT tracker balance, block 70581335 at 2025-03-19 15:10:15 UTC.
- **`primary_onchain`**
  - URL: <https://tronscan.org/#/transaction/aeaac3dcd1e2d9ac92a01a4ffea1bbebc248410859d21327a29645ccca92e3f0>
  - tx_hash: `aeaac3dcd1e2d9ac92a01a4ffea1bbebc248410859d21327a29645ccca92e3f0`
  > USDT-TRON AddedBlackList(address) for TBh5t6Gy46ae48uaFTWij1u5RGLswWjvrt,
> 1,000,000.00 USDT tracker balance, block 70581335 at 2025-03-19 15:10:15 UTC.
- **`primary_onchain`**
  - URL: <https://tronscan.org/#/transaction/6084da483740a6d10b14310974cc9077f6e6ed30c665556f7953677bbdac3990>
  - tx_hash: `6084da483740a6d10b14310974cc9077f6e6ed30c665556f7953677bbdac3990`
  > USDT-TRON AddedBlackList(address) for TGYB5nyy6DyrmZv7U6a4egX35jomz67R2t,
> 1,000,000.00 USDT tracker balance, block 70583046 at 2025-03-19 16:35:48 UTC.
- **`primary_onchain`**
  - URL: <https://tronscan.org/#/transaction/b021c6a691a51a1007558dfcfb99de79c3f9a56c13724d136720c5cf38ad3a65>
  - tx_hash: `b021c6a691a51a1007558dfcfb99de79c3f9a56c13724d136720c5cf38ad3a65`
  > USDT-TRON AddedBlackList(address) for TXjmb1gnkjMorvFS4ytDT79MN9HMDfHVsY,
> 1,000,000.00 USDT tracker balance, block 70583045 at 2025-03-19 16:35:45 UTC.
- **`primary_onchain`**
  - URL: <https://tronscan.org/#/transaction/04ff6378e56cc6614fda40145a98adf218586ac499309dae2e6bd6bdf9b27d23>
  - tx_hash: `04ff6378e56cc6614fda40145a98adf218586ac499309dae2e6bd6bdf9b27d23`
  > USDT-TRON AddedBlackList(address) for TPykroq1Hc7G58mFfPsyUCkoVXWFXMf64N,
> 1,000,000.00 USDT tracker balance, block 70583047 at 2025-03-19 16:35:51 UTC.
- **`primary_onchain`**
  - URL: <https://tronscan.org/#/transaction/b59eb7f5edb2101726f00e19722d7b24a064cbbde5d704f6b042c5c35d1cad5f>
  - tx_hash: `b59eb7f5edb2101726f00e19722d7b24a064cbbde5d704f6b042c5c35d1cad5f`
  > USDT-TRON AddedBlackList(address) for TJxe6da2LcPPXe8VZJYAA9v9F1bwJhX4i2,
> 400,996.68 USDT tracker balance, block 70581341 at 2025-03-19 15:10:33 UTC.
- **`primary_onchain`**
  - URL: <https://tronscan.org/#/transaction/7034e8e7f93511259f3ce384eb0d328ec885d5dbd627e6541213567b994de8cd>
  - tx_hash: `7034e8e7f93511259f3ce384eb0d328ec885d5dbd627e6541213567b994de8cd`
  > USDT-TRON AddedBlackList(address) for TCwrBc8fBnLTAQQENwkTLP4UEESM9Ksg6n,
> 1,079,953.26 USDT tracker balance, block 70581340 at 2025-03-19 15:10:30 UTC.
- **`primary_onchain`**
  - URL: <https://tronscan.org/#/transaction/c5223e2f8fe9fbfc4e57fe9bd4b0e4e4b7bde289ed4fcdb319414ae60e1bc5ad>
  - tx_hash: `c5223e2f8fe9fbfc4e57fe9bd4b0e4e4b7bde289ed4fcdb319414ae60e1bc5ad`
  > USDT-TRON AddedBlackList(address) for THpynByUg6JZ8uQeqFNFzEFtCzi9NcWxud,
> 8.07 USDT tracker balance, block 70634998 at 2025-03-21 11:54:06 UTC.
- **`primary_onchain`**
  - URL: <https://tronscan.org/#/transaction/b4feadd44e2e9378797e50a4150e8f73cc9ceadaf924b76dcf2b860421eb1d5b>
  - tx_hash: `b4feadd44e2e9378797e50a4150e8f73cc9ceadaf924b76dcf2b860421eb1d5b`
  > USDT-TRON AddedBlackList(address) for TSbT8sqSiDjQPL7iHcRgzRnNTLRK8qhMf7,
> 11.09 USDT tracker balance, block 70635005 at 2025-03-21 11:54:27 UTC.
- **`primary_onchain`**
  - URL: <https://tronscan.org/#/transaction/759ff42fc6554ba3f8816c7eee40b94dfdf44cf74f0efefd70b363d06cac8e41>
  - tx_hash: `759ff42fc6554ba3f8816c7eee40b94dfdf44cf74f0efefd70b363d06cac8e41`
  > USDT-TRON AddedBlackList(address) for TGjMuqfgBbs9PqD5uJDAE9zVysdnGwMk12,
> 883,070.00 USDT tracker balance, block 70635009 at 2025-03-21 11:54:39 UTC.
- **`primary_onchain`**
  - URL: <https://tronscan.org/#/transaction/8fdd5aac1f1aedfd71a72dbf5bb60815db1a2c03a511a39b344aeb30f29b44ac>
  - tx_hash: `8fdd5aac1f1aedfd71a72dbf5bb60815db1a2c03a511a39b344aeb30f29b44ac`
  > USDT-TRON AddedBlackList(address) for TFq8nBxgbb9pjMw9fjT2uNRNuuhTgDdBed,
> 426,183.08 USDT tracker balance, block 70635013 at 2025-03-21 11:54:51 UTC.
- **`primary_onchain`**
  - URL: <https://etherscan.io/tx/0xb6bc7e5f79e9c7ed91db7a917f01633e8b7a39fbc9d2713db667c336c304a0e0>
  - tx_hash: `0xb6bc7e5f79e9c7ed91db7a917f01633e8b7a39fbc9d2713db667c336c304a0e0`
  > Ethereum USDT AddedBlackList(address) for 0xedcf79de5347a81d9329951ed78f6215cfb27b3c,
> 19,696.79 USDT tracker balance, block 22095092 at 2025-03-21 11:57:35 UTC.
- **`primary_onchain`**
  - URL: <https://etherscan.io/tx/0x970af0dc17ff56a1846b59bfc0d347f6615fdb940bca5ca2258b0bdfdcb46edb>
  - tx_hash: `0x970af0dc17ff56a1846b59bfc0d347f6615fdb940bca5ca2258b0bdfdcb46edb`
  > Ethereum USDT AddedBlackList(address) for 0xcd69f8ec7d6b03e66bd13f2829cbc00a416420d6,
> 19,691.69 USDT tracker balance, block 22095092 at 2025-03-21 11:57:35 UTC.
- **`primary_onchain`**
  - URL: <https://etherscan.io/tx/0xa71f1a9da815b86cee18e3628e967b85409ae366050f522452e0f5471838cdd3>
  - tx_hash: `0xa71f1a9da815b86cee18e3628e967b85409ae366050f522452e0f5471838cdd3`
  > Ethereum USDT AddedBlackList(address) for 0x8f836b2122da07d8a20f71856e676f086c7c84b8,
> 19,694.80 USDT tracker balance, block 22095092 at 2025-03-21 11:57:35 UTC.
- **`primary_onchain`**
  - URL: <https://etherscan.io/tx/0xb36caaaad90f4fe9e194882086194671b827fed86e8af571c6d974a910f276e1>
  - tx_hash: `0xb36caaaad90f4fe9e194882086194671b827fed86e8af571c6d974a910f276e1`
  > Ethereum USDT AddedBlackList(address) for 0xc8bd2fbfe0437f38394c5d504221fc01cc8df92a,
> 19,730.41 USDT tracker balance, block 22095093 at 2025-03-21 11:57:47 UTC.
- **`primary_onchain`**
  - URL: <https://etherscan.io/tx/0x3ec45ce2716355ccfabf5f26a5c91acfe9cd58e8b4d806f3a56283663bd30ee3>
  - tx_hash: `0x3ec45ce2716355ccfabf5f26a5c91acfe9cd58e8b4d806f3a56283663bd30ee3`
  > Ethereum USDT AddedBlackList(address) for 0xe761bcec17380181d99ebcabd0d2a65b7ab64c6f,
> 39,340.00 USDT tracker balance, block 22095093 at 2025-03-21 11:57:47 UTC.
- **`supporting_tracker`**
  - URL: <https://usdtbanlist.com/address/TLZiKkccnBs2hg21dD55HZJLhQWFEgkjVU>
  - body_hash: `sha256:a1ab069c077c34fc519fcb1bf39ef8c206fa8a40901cf2dc73a727620698894a`
  - body_path: `sources/http_captures/t3-bybit-hack-usdt-freeze-2025-03/primary/usdtbanlist.com__address-TLZiKkccnBs2hg21dD55HZJLhQWFEgkjVU__84239a2658.html`
  > Representative usdtbanlist tracker capture showing the address-level
> frozen balance and linked Tronscan AddedBlackList tx. The full local
> capture bundle includes tracker pages for all 18 pinned addresses.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`t3-financial-crime-unit-launch-2024-09`](./t3-financial-crime-unit-launch-2024-09.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `ee7bf1a`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

