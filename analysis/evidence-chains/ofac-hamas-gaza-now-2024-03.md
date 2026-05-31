# Evidence chain — `ofac-hamas-gaza-now-2024-03`

**Status**: `admitted` · **Stratum**: `S1_ofac_sdn` · **Shape**: `null_event` (0 changed layer(s): none) · **Tier**: `null_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-05-31` · **Source commit**: `939a17f` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-20` · **Tool version**: `0.1.0` · **Generated**: `2026-05-31T14:50:46Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "OFAC's 2024-03-27 SDN designation of Gaza Now (a Gaza-based pro-Hamas
> news / social-media brand exploited as a crypto donation funnel) added
> 8 digital-currency addresses (1 BTC empty + 2 ETH + 5 USDT, ~USD 13K
> combined funded balance) to the SDN list as part of a joint US OFAC +
> UK OFSI action under EO 13224. Cascade evaluation conditional on
> pinned post-event usdtbanlist.com and Chainalysis slice anchors."

## 1. Trigger

- **Type**: `ofac_sdn_designation`
- **Actor**: `US_OFAC`
- **Timestamp**: `2024-03-27 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://home.treasury.gov/news/press-releases/jy2213>
  - Wayback: <https://web.archive.org/web/20240327145200/https://home.treasury.gov/news/press-releases/jy2213>
  - body_hash: `sha256:a0910742ffa37ccb08b4da2af4b2c64626cd390e6bfc4820aa4516b1d3271894`
  - body_path: `sources/http_captures/ofac-hamas-gaza-now-2024-03/primary/web.archive.org__web-20240327145200-https-home.treasury.gov-news-press-releases-jy2213__59d46e3aec.html`
  > US Treasury press release jy2213 "Treasury Sanctions Hamas-Aligned
> Terrorist Fundraising Network" (2024-03-27). Joint US OFAC + UK OFSI
> action designating Gaza Now (a Gaza-based pro-Hamas news / social-
> media brand), its founder Mustafa Ayash, and two London-based
> companies (Al-Qureshi Executives Ltd and Aakhirah Limited) plus
> their director Aozma Sultana. v0.3 audit 2026-05-20 (c) Batch C-1:
> Wayback memento 20240327145200 pinned (174138 bytes), grep verifies
> 34xHamas + 18xGaza Now + 14xjy2213 + 12xSultana + 6xAl-Qureshi +
> 6xAakhirah + 4xAyash + 4xMarch 27 + 4xUnited Kingdom.
- **`primary_legal`**
  - URL: <https://ofac.treasury.gov/recent-actions/20240327>
  - Wayback: <https://web.archive.org/web/20240328103219/https://ofac.treasury.gov/recent-actions/20240327>
  - body_hash: `sha256:c7a2a75c50da39fc5e0d9495296a88a60c1583051a75d214a2b74153ed4f3d1a`
  - body_path: `sources/http_captures/ofac-hamas-gaza-now-2024-03/primary/web.archive.org__web-20240328103219-https-ofac.treasury.gov-recent-actions-20240327__343d176540.html`
  > OFAC Recent Actions page for 2024-03-27 listing the Counter Terrorism
> Designations under [SDGT] tag (Gaza Now entity entry + Mustafa Ayash
> + Al-Qureshi Executives Ltd + Aakhirah Limited + Aozma Sultana) and
> the 8 attached digital-currency addresses verbatim. v0.3 audit
> 2026-05-20 (c) Batch C-1: Wayback memento 20240328103219 pinned
> (94358 bytes). Address enumeration extracted from this capture:
> 1 BTC (3Q8H2ZWMtc4R1M3mkmhnTjCoYKTeCFigDP) + 2 ETH
> (0xE950DC316b836e4EeFb8308bf32Bf7C72a1358FF +
> 0x21B8d56BDA776bbE68655A16895afd96F5534feD) + 4 USDT-TRC20
> (TTgcTTNbNuFdbrhvbjMZVrdU5KALyzDaPw +
> TGJVc32ig2u8tQsYMLE7KXHT5NDQroaVNU +
> TXEsK1sEsKjZ1xtHitnyAAoqw3WLdYdRNW +
> TH96tFMn8KGiYSLiwcV3E2UiaJc8jmcbz3) + 1 USDT-ERC20
> (0x175d44451403Edf28469dF03A9280c1197ADb92c) = 8 total.
- **`supporting_journalism`**
  - URL: <https://www.chainalysis.com/blog/ofac-ofsi-gaza-now-sanctions/>
  - Wayback: <https://web.archive.org/web/2024/https://www.chainalysis.com/blog/ofac-ofsi-gaza-now-sanctions/>
  > Chainalysis post-action analysis "U.S. Sanctions Gaza Now, Others for
> Hamas Crypto Fundraising" (2024-03). Substrate anchor naming the
> joint US/UK action, the cohort composition (8 digital-currency
> addresses spanning BTC / ETH / USDT), and the cross-rail fundraising
> pattern (Gaza Now solicits donations via the news brand; Al-Qureshi
> Executives / Aakhirah Limited route value via UK-side MSB / commerce
> shells). Cited here as contextual substrate; per-event chain-analytics
> report-slice naming the specific SDN addresses deferred.
- **`supporting_journalism`**
  - URL: <https://www.coindesk.com/policy/2024/03/27/us-uk-issue-joint-sanctions-of-hamas-aligned-gaza-now>
  - Wayback: <https://web.archive.org/web/2024/https://www.coindesk.com/policy/2024/03/27/us-uk-issue-joint-sanctions-of-hamas-aligned-gaza-now>
  > CoinDesk 2024-03-27 same-day coverage corroborating the joint US OFAC
> + UK OFSI designation and the inclusion of crypto wallets in the SDN
> action.
- **`supporting_journalism`**
  - URL: <https://www.elliptic.co/blog/crypto-regulatory-affairs-the-us-treasurys-intense-week-of-crypto-related-sanctions-actions>
  - Wayback: <https://web.archive.org/web/2024/https://www.elliptic.co/blog/crypto-regulatory-affairs-the-us-treasurys-intense-week-of-crypto-related-sanctions-actions>
  > Elliptic crypto-regulatory-affairs 2024-03 brief contextualising the
> Gaza Now designation inside a multi-action week of OFAC crypto-
> sanctions activity and confirming the per-cohort balance breakdown
> (1 empty BTC + 2 funded ETH + 5 USDT of which 2 funded).

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `complete`
- **Protocol**: `gaza_now_fundraising_brand`
- **Actor name**: Gaza Now (Hamas-aligned media / crypto fundraising network)
- **Chains**: `bitcoin`, `ethereum`, `tron`
- **Addresses**: 8 total (enumerated in event YAML)

> Gaza Now (Gaza-based pro-Hamas social-media news brand operated by
> Mustafa Ayash) is treated as the entity-level cascade target. The
> March 27, 2024 SDN action enumerates: (1) the Gaza Now entity itself,
> (2) Mustafa Ayash (founder, individual), (3) Al-Qureshi Executives
> (London-based UK company), (4) Aakhirah Limited (London-based UK
> company), (5) Aozma Sultana (UK individual, director of #3 and #4).
> Eight digital-currency addresses attached to the Gaza Now SDN entry,
> enumerated verbatim from OFAC RA Wayback capture 20240328103219
> (v0.3 audit 2026-05-20): 1 BTC + 2 ETH + 4 USDT-TRC20 + 1 USDT-ERC20
> = 8 total. enumeration=complete (was subset). Third major post-Oct-7
> OFAC action targeting Hamas crypto fundraising, after the 2023-10
> Buy Cash Money Transfer designation
> (`ofac-hamas-buy-cash-msb-2023-10`) and the 2024-01 IRGC virtual-
> currency-network designation
> (`ofac-hamas-irgc-virtual-currency-network-2024-01`).

## 3. Changed-layer observations (supports the scoped claim)

*No observed_change entries. This is a `null_event`; see §4 for observed_no_change evidence supporting the null claim.*

## 4. No-change observations (where applicable)

### offramp_cex — `no_public_cex_cascade_documented_in_14d_window`

**Window**: `2024-03-27 00:00:00+00:00` → `2024-04-10 23:59:59+00:00`

**Sources**:

- **`primary_legal`**
  - URL: <https://home.treasury.gov/news/press-releases/jy2213>
  - Wayback: <https://web.archive.org/web/20240327145200/https://home.treasury.gov/news/press-releases/jy2213>
  - body_hash: `sha256:a0910742ffa37ccb08b4da2af4b2c64626cd390e6bfc4820aa4516b1d3271894`
  - body_path: `sources/http_captures/ofac-hamas-gaza-now-2024-03/primary/web.archive.org__web-20240327145200-https-home.treasury.gov-news-press-releases-jy2213__59d46e3aec.html`
  > v0.3 audit 2026-05-20 (c) Batch C-1: observation row added at
> promotion to admitted state, following lazarus / sim-hyon-sop /
> buy-cash precedent for OFAC SDN of foreign-operated non-CEX
> target. Treasury jy2213 + OFAC RA 20240327 serve as the
> admission-grade denominator anchors substantiating the trigger
> event (SDN designation + 8-address enumeration); absence of
> fresh public CEX policy statement explicitly citing Gaza Now in
> the 14d post-event window is the null finding (industry
> preference for private chain-analytics KYT-flag workflows over
> public per-wallet disclosure, same pattern as Hamas-class SDN
> siblings). Original draft's asset_onchain observation row
> (gaza_now_8_addresses_added_to_sdn_list) REMOVED at promotion:
> validator requires primary_onchain source for asset_onchain
> observations; SDN listing itself is the trigger not a downstream
> cascade response. Per-address Tether/Circle freeze-tx evidence
> deferred to follow-up enrichment.

## 5. Honest coverage gaps

- **l3_rpc** (`not_measured`): No pinned MEV-Blocker / OFAC-compliant RPC filter-list snapshot
- **asset_onchain** (`not_measured`): 8 digital-currency addresses attached to the Gaza Now SDN entry

## 7. Related events

- [`ofac-hamas-buy-cash-msb-2023-10`](./ofac-hamas-buy-cash-msb-2023-10.md)
- `ofac-hamas-irgc-virtual-currency-network-2024-01` (rejected; no rendered admitted-chain link)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `939a17f`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

