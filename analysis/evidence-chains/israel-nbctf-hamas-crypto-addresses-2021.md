# Evidence chain — `israel-nbctf-hamas-crypto-addresses-2021`

**Status**: `admitted` · **Stratum**: `S4_nation_state` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `71ac901` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-21` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> *(no scoped_claim recorded — event not paper-ready)*

## 1. Trigger

- **Type**: `regulatory_enforcement`
- **Actor**: `IL_NBCTF`
- **Timestamp**: `2021-07-08 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://www.chainalysis.com/blog/israel-hamas-cryptocurrency-seizure-july-2021/>
  - Wayback: <https://web.archive.org/web/2021/https://www.chainalysis.com/blog/israel-hamas-cryptocurrency-seizure-july-2021/>
  > Chainalysis 2021-07 blog "Israeli Government Seizes Cryptocurrency
> Addresses Associated with Hamas Donation Campaigns" summarises the
> NBCTF (National Bureau for Counter Terror Financing, an arm of
> Israel's Ministry of Defense) Administrative Seizure Order issued
> 2021-07-08 against 84 crypto addresses spanning BTC, ETH, USDT,
> DOGE, XRP, LTC, TRX, BSC, XLM and LSK, attributed to seven
> Palestinian-national individuals associated with Hamas's al-Qassam
> Brigades donation campaigns. The order is the first documented
> nation-state administrative seizure order against a Hamas-linked
> crypto-address cluster, predating the post-October-7 OFAC Hamas
> cascade (ofac-hamas-buy-cash-msb-2023-10 et seq.) by ~2.3 years.
> DRYRUN: pinned Wayback snapshot and body_hash for the Chainalysis
> post are deferred to the human-audit pass; marked
> evidence_use=contextual_unarchived per validator policy for
> unarchived sources.
- **`primary_legal`**
  - URL: <https://www.merklescience.com/blog/israel-issues-seizure-orders>
  - Wayback: <https://web.archive.org/web/2021/https://www.merklescience.com/blog/israel-issues-seizure-orders>
  > Merkle Science 2021-07 blog "Israeli Authorities Issue Seizure
> Order Against 84 Hamas-linked Crypto Wallets that Received Over
> $11 Million Since October 2015" anchors the legal authority
> (Administrative Seizure Order under Section 66 of Israel's
> Anti-Terrorism Law of 2016, signed by then-Defense-Minister
> Benny Gantz acting on NBCTF analysis) and the cluster economics
> (37 BTC addresses receiving 3,758.828 BTC ≈ $9.89M; 8 Ethereum
> addresses receiving 202.246 ETH + 1,182,038.889 USDT ≈ $1.23M;
> 93.43% of BTC concentrated in a single address
> 19D1iGzDr7FyAdiy3ZZdxMd6ttHj1kj6WW). Triangulation source for
> the trigger's legal-authority framing. DRYRUN: pinned Wayback
> snapshot deferred to human audit.
- **`supporting_journalism`**
  - URL: <https://www.theblock.co/post/110725/israeli-counterterror-authority-seizes-84-crypto-addresses-it-says-belong-to-hamas>
  - Wayback: <https://web.archive.org/web/2021/https://www.theblock.co/post/110725/israeli-counterterror-authority-seizes-84-crypto-addresses-it-says-belong-to-hamas>
  > The Block 2021-07-08 coverage of the NBCTF Administrative
> Seizure Order. Triangulation source for the trigger date and
> the 84-address scope. DRYRUN: pinned Wayback snapshot deferred
> to human audit.

## 2. Target

- **Kind**: `address_set`
- **Enumeration**: `subset`
- **Actor name**: Hamas al-Qassam Brigades donation-campaign address cluster
- **Chains**: `bitcoin`, `ethereum`, `tron`, `binance_smart_chain`, `dogecoin`, `xrp`, `litecoin`, `stellar`, `lisk`
- **Addresses**: 1 total (enumerated in event YAML)

> The 2021-07-08 NBCTF Administrative Seizure Order targets 84 crypto
> addresses across BTC, ETH, USDT, DOGE, XRP, LTC, TRX, BSC, XLM, and
> LSK, attributed by NBCTF analysis to seven named Palestinian
> nationals associated with Hamas's al-Qassam Brigades donation
> campaigns (Ali Ismail Shafiq Abualkas; Mahmoud Madhat Ahmed Baroud;
> Tareq Alla Mohammedali Baraaasi; Mahmoud Mohammed Mahmoud Ayesh;
> Karem Munir Mohammed Abed; Mohammed Ramadan Hasan Abukwaik;
> Mohammed Nasser Ibrahim Abulaila). Only one canonical BTC address
> (19D1iGzDr7FyAdiy3ZZdxMd6ttHj1kj6WW; the 93.43%-concentration
> consolidation address) is pinned in target.addresses at draft time;
> the full 84-address roster from the order itself is deferred to
> the human-audit pass. enumeration=subset reflects that intentional
> scoping.

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `plausible` · Δt = 0h

**Event label**: `nbctf_seizure_order_severs_il_ramp_access_for_named_hamas_cluster`

**Timestamp**: `2021-07-08 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`semi_primary_measurement`**
  - URL: <https://www.chainalysis.com/blog/israel-hamas-cryptocurrency-seizure-july-2021/>
  - Wayback: <https://web.archive.org/web/20230830011908/https://www.chainalysis.com/blog/israel-hamas-cryptocurrency-seizure-july-2021/>
  - body_hash: `sha256:1524ddad7cf55ba046c48450c21bdc1ed4a12041c79c6fd3c21d3413189bbe6b`
  - body_path: `sources/http_captures/israel-nbctf-hamas-crypto-addresses-2021/primary/web.archive.org__web-20230830011908-https-www.chainalysis.com-blog-israel-hamas-cryptocurrency-seizure-july-2021__e64fe1175d.html`
  > Chainalysis forensic writeup traces consolidation flows into
> deposit addresses at a major mainstream exchange.
> attribution=plausible (not direct) per the codebook: the NBCTF
> order names the source-side addresses but does not publicly
> name the downstream CEX, and the receiving exchange did not
> make a public compliance statement tying its account freezes
> to the order in the immediate 2021-07 window. Reclassified
> semi_primary_measurement (forensic-firm on-chain tracing) at
> audit; Wayback 20230830011908 pinned.
- **`semi_primary_wayback`**
  - URL: <https://www.dlnews.com/articles/regulation/israeli-police-seize-binance-account-linked-to-hamas/>
  - Wayback: <https://web.archive.org/web/20231010141013/https://www.dlnews.com/articles/regulation/israeli-police-seize-binance-account-linked-to-hamas/>
  - body_hash: `sha256:d9e0c13db40200c6c4f62d03cb86c6307c39ccc9570cf409c82ed3f8c76e5bba`
  - body_path: `sources/http_captures/israel-nbctf-hamas-crypto-addresses-2021/primary/web.archive.org__web-20231010141013-https-www.dlnews.com-articles-regulation-israeli-police-seize-binance-account-linked-to-hamas__947af0b9f5.html`
  > DL News 2023-10 coverage retroactively confirms the
> downstream-CEX leg (Israeli police seizures of Binance
> accounts linked to Hamas) and references the earlier 2021
> NBCTF action as precedent ("Israeli authorities blocked 84
> addresses believed to be linked to Hamas that had received
> $7.7 million in crypto assets"). Independent second
> semi-primary anchor; Wayback 20231010141013 pinned.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`ofac-hamas-buy-cash-msb-2023-10`](./ofac-hamas-buy-cash-msb-2023-10.md)
- `ofac-hamas-irgc-virtual-currency-network-2024-01` (rejected; no rendered admitted-chain link)
- [`ofac-hamas-gaza-now-2024-03`](./ofac-hamas-gaza-now-2024-03.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `71ac901`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

