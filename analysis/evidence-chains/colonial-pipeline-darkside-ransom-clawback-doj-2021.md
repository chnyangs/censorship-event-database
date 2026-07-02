# Evidence chain — `colonial-pipeline-darkside-ransom-clawback-doj-2021`

**Status**: `admitted` · **Stratum**: `S3_doj_sec_cftc_fiod` · **Shape**: `comparison` (1 changed layer(s): `asset_onchain`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-08` · **Source commit**: `ee7bf1a` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-31` · **Tool version**: `0.1.0` · **Generated**: `2026-06-25T23:48:26Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "DOJ/FBI's 2021-06-07 Colonial Pipeline DarkSide ransom clawback is
> represented by a one-address Bitcoin seizure draft: tx
> 943f2d576ed8d9f388ba75eb82fe35cce29479b84121827ac368a5a94f44cf7a
> produced a 63.7 BTC net outflow from the address identified by
> Paladin/Elliptic as the DarkSide affiliate share address."

## 1. Trigger

- **Type**: `doj_seizure_order`
- **Actor**: `US_DOJ_FBI`
- **Timestamp**: `2021-06-07 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://www.justice.gov/opa/pr/department-justice-seizes-23-million-cryptocurrency-paid-ransomware-extortionists-darkside>
  - Wayback: <https://web.archive.org/web/20210607195332/https://www.justice.gov/opa/pr/department-justice-seizes-23-million-cryptocurrency-paid-ransomware-extortionists-darkside>
  - body_hash: `sha256:f6b71fdf0965268ed49e0e0cab67fd6cca70d0d1f5e8c4b72b05e1b89aac4d92`
  - body_path: `sources/http_captures/colonial-pipeline-darkside-ransom-clawback-doj-2021/primary/web.archive.org__web-20210607195332-https-www.justice.gov-opa-pr-department-justice-seizes-23-million-cryptocurrency-paid-ransomware-extortionists-darkside__086d33c408.html`
  > DOJ archived press release (2021-06-07): DOJ announced seizure of
> 63.7 bitcoins worth about $2.3M, representing proceeds of the
> Colonial Pipeline ransom paid to DarkSide; the warrant was
> authorized the same day by Magistrate Judge Laurel Beeler in NDCA.
> The release also states that law enforcement identified a specific
> Bitcoin address for which the FBI had the private key.
- **`primary_legal`**
  - URL: <https://www.justice.gov/opa/press-release/file/1402056/download>
  - body_hash: `sha256:4ff9bcbcbfd0fa0459a831f97d0192c4a5d8dbb1cba1a671748af2deb69f6d8f`
  - body_path: `sources/http_captures/colonial-pipeline-darkside-ransom-clawback-doj-2021/primary/www.justice.gov__opa-press-release-file-1402056-download__70bb25919a.bin`
  > DOJ-hosted seizure-affidavit PDF for case 3:21-mj-70945-LB,
> captured as binary. The PDF is scanned/image-heavy, so load-bearing
> text is carried by the replayable Wayback DOJ press release and the
> captured analytics article that identifies the address.
- **`supporting_journalism`**
  - URL: <https://www.paladincapgroup.com/us-authorities-seize-the-affiliates-share-of-the-darkside-ransom-paid-by-colonial-pipeline/>
  - body_hash: `sha256:7ccfb6cfc99a8a86531e1c0f874fbf6b315d02f9f8e0f049399959279f3fad01`
  - body_path: `sources/http_captures/colonial-pipeline-darkside-ransom-clawback-doj-2021/primary/www.paladincapgroup.com__us-authorities-seize-the-affiliates-share-of-the-darkside-ransom-paid-by-colonial-pipeline__819c6a369f.html`
  > Paladin-hosted Elliptic analysis by Tom Robinson links the
> affiliate share of the Colonial ransom to Bitcoin address
> bc1qq2euq8pw950klpjcawuy4uj39ym43hs6cfsegq, describes it as the
> same address mentioned in the seizure affidavit, and reports that
> the address was emptied on 2021-06-07.

## 2. Target

- **Kind**: `address_set`
- **Enumeration**: `complete`
- **Actor name**: DarkSide affiliate Colonial Pipeline ransom address
- **Chains**: `bitcoin`
- **Addresses**: 1 total (enumerated in event YAML)

> Target is the single Bitcoin address identified by Elliptic/Paladin as
> holding the affiliate share of the Colonial Pipeline DarkSide ransom and
> as matching the address in the seizure affidavit. Marked complete for
> this narrowly scoped one-address seizure draft; not a claim to enumerate
> every DarkSide wallet.

## 3. Changed-layer observations (supports the scoped claim)

### asset_onchain · attribution: `plausible` · Δt = 17.76h

**Event label**: `colonial_pipeline_darkside_affiliate_btc_seizure`

**Timestamp**: `2021-06-07 17:45:41+00:00` (precision: `minute`)

**Sources**:

- **`primary_onchain`**
  - URL: <https://blockstream.info/tx/943f2d576ed8d9f388ba75eb82fe35cce29479b84121827ac368a5a94f44cf7a>
  - tx_hash: `943f2d576ed8d9f388ba75eb82fe35cce29479b84121827ac368a5a94f44cf7a`
  > Bitcoin transaction in block 686683 at 2021-06-07 17:45:41 UTC.
> The transaction spends the 69.60422177 BTC UTXO held by
> bc1qq2euq8pw950klpjcawuy4uj39ym43hs6cfsegq and returns
> 5.90422177 BTC to the same address, leaving a 63.7 BTC net outflow.
- **`semi_primary_measurement`**
  - URL: <https://blockstream.info/api/address/bc1qq2euq8pw950klpjcawuy4uj39ym43hs6cfsegq/txs>
  - body_hash: `sha256:fbdfadd09756a9aeae59888279b58c9a85035915b589d943164cef68327887d4`
  - body_path: `sources/http_captures/colonial-pipeline-darkside-ransom-clawback-doj-2021/primary/blockstream.info__api-address-bc1qq2euq8pw950klpjcawuy4uj39ym43hs6cfsegq-txs__7ed12fe3c5.json`
  > Blockstream address API capture confirms four address-history
> rows. Relevant rows: 69.60422177 BTC received in tx
> daf38c7b38eb0a587cf843f47000d5c294affb4f56017370ad48c5147f5e69d9,
> 63.7 BTC net outflow in tx
> 943f2d576ed8d9f388ba75eb82fe35cce29479b84121827ac368a5a94f44cf7a,
> and a later 5.90422177 BTC movement in tx
> 280c5f96397b9502b99703842712b78fda84f1a0faabf826f683448082f46369.
- **`semi_primary_measurement`**
  - URL: <https://mempool.space/api/address/bc1qq2euq8pw950klpjcawuy4uj39ym43hs6cfsegq/txs>
  - body_hash: `sha256:526093099247a7c021ef3bbe5359b21d4ce3674dc552009580e1a9cd804ea853`
  - body_path: `sources/http_captures/colonial-pipeline-darkside-ransom-clawback-doj-2021/primary/mempool.space__api-address-bc1qq2euq8pw950klpjcawuy4uj39ym43hs6cfsegq-txs__3d71e0b7bb.json`
  > Independent mempool.space address API capture matches the
> Blockstream transaction IDs, block heights, timestamps, and
> receive/spend values for the target address.
- **`supporting_journalism`**
  - URL: <https://www.paladincapgroup.com/us-authorities-seize-the-affiliates-share-of-the-darkside-ransom-paid-by-colonial-pipeline/>
  - body_hash: `sha256:7ccfb6cfc99a8a86531e1c0f874fbf6b315d02f9f8e0f049399959279f3fad01`
  - body_path: `sources/http_captures/colonial-pipeline-darkside-ransom-clawback-doj-2021/primary/www.paladincapgroup.com__us-authorities-seize-the-affiliates-share-of-the-darkside-ransom-paid-by-colonial-pipeline__819c6a369f.html`
  > Paladin/Elliptic article links the address to the Colonial ransom
> affiliate share and says it was emptied around 1:40pm Eastern Time
> on 2021-06-07, with a separate 5.9 BTC movement not mentioned in
> the affidavit.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `ee7bf1a`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

