# Census gap list (gap-discovery workflow wf_7fa15316, 2026-05-30)

Raw candidates: 238 across 11 mandates. Per-mandate: S1-ofac=24, S2-ofac-removal=1, S3-doj=26, S3-sec-cftc-fincen=17, S4-asia=31, S4-row=29, S6-supra=23, S5-cex=31, S5-defi=20, proto-2007-2012=13, early-bitcoin-2013-2016=23.

I now have everything needed to produce the synthesis. Let me compile the full analysis.

# GAP-LIST SYNTHESIS — Crypto-Censorship Census (2007+)

## Method note

Cross-referenced all complete candidates against the 262-event corpus (`corpus_inventory_2026_05_30.tsv`). The candidate JSON was **truncated mid-entry** at the end (last `tether-apac-pig-butcherin…` S5-defi entry is cut off), so the S5-defi block is the only one I could not fully audit — likely 1-2 entries lost past the cutoff. Everything else is complete.

---

## 1. DEDUPLICATIONS & CORPUS COLLISIONS (drop these)

### A. Already in corpus (DROP)

| Candidate | Reason |
|---|---|
| `chinyong-kim-sang-man-dprk-it-worker-ofac-2023-05` | Corpus already has the DPRK-IT-worker / Sim Hyon Sop OFAC action (`ofac-dprk-it-worker-sim-hyon-sop-2023-04`) **and** the S1 candidate `dprk-it-worker-sim-hyon-sop-doj-indictment-2023` is the *DOJ* twin — Chinyong (May 23) is a **distinct designation**, so KEEP Chinyong but flag near-corpus. Net: KEEP (different date/target). |
| `huobi-seven-privacy-coin-delisting-2022-09` | Corpus `huobi-htx-privacy-coin-delisting-2024` is **mis-dated 2022** in inventory but is the same Huobi privacy-coin delisting event. **DROP** (candidate's own note flags the date discrepancy; this is the corpus entry). |
| `binance-monero-global-delisting-2024-02` | Corpus has `okx-monero-global-delisting-2024` (rejected) and `binance-privacy-coin-delisting-2023`. Binance **global** XMR delisting (Feb 2024) is genuinely distinct from the 2023 EU-only one. **KEEP**, but adjacent to a rejected sibling — maintainer should confirm not out-of-scope. |
| `tether-okx-doj-pig-butchering-225m-freeze-2025-06` | Pairs with S3 `pig-butchering-225m-civil-forfeiture-doj-2025` (same event, different stratum). Corpus has `tether-pig-butchering-second-wave-2024` and `tether-doj-pig-butchering-freeze-2023` — those are **different** seizures. **KEEP** (new $225M event) but **MERGE the S5-defi + S3-doj rows into one cross-stratum event**. |
| `s2 roman-semenov-removal-2025-03` | Same OFAC Recent Action bundle as corpus `tornado-cash-ofac-delisting-2025`. Candidate's own note: borderline sub-action. **DROP** (collapses into existing delisting event per "one designation-action" rule). |
| `india-finance-act-vda-tax-tds-2022` **(S4-row)** | Exact duplicate of `india-vda-30pct-tax-1pct-tds-finance-act-2022` **(S4-asia)**. **MERGE → keep the asia entry (richer).** |
| `vietnam-sbv-payment-prohibition-2017-10` **(S4-row)** | Exact duplicate of `vietnam-sbv-payment-prohibition-2017-10` **(S4-asia)**, same ID. **MERGE → keep asia (richer 2-source).** |
| `pakistan-sbp-crypto-prohibition-2018-04` **(S4-row)** | Duplicate of `pakistan-sbp-crypto-banking-prohibition-2018-04` **(S4-asia)**. **MERGE → keep asia.** |
| `nepal-nrb-crypto-ban-expansion-2021-09` **(S4-row)** | Duplicate of `nepal-nrb-comprehensive-crypto-ban-2021-09` **(S4-asia)** (and the 2017 `nepal-nrb-bitcoin-ban-2017-08`). **MERGE → keep asia pair.** |
| `thailand-sec-meme-nft-token-ban-2021-06` **(S4-row)** | Not a corpus collision but overlaps thematically with the asia Thailand entries; **KEEP** (distinct 2021 meme/NFT delisting order). |
| `genesis-market-ofac-2023-04` | Be careful: corpus has no Genesis Market OFAC row, but S3-doj note lists Genesis Market takedown. **KEEP** (S1 designation is new). |

### B. Cross-agent / cross-stratum duplicates (MERGE, keep richest)

| Real-world event | Candidates | Action |
|---|---|---|
| **DPRK IT-worker Sim Hyon Sop** | S3 `dprk-it-worker-sim-hyon-sop-doj-indictment-2023` ↔ corpus S1 `ofac-dprk-it-worker-sim-hyon-sop-2023-04` | KEEP S3 (criminal twin, explicitly distinct per agent), cross-link to corpus S1. |
| **$225M pig-butchering forfeiture** | S3 `pig-butchering-225m-civil-forfeiture-doj-2025` ↔ S5 `tether-okx-doj-pig-butchering-225m-freeze-2025-06` ↔ S5 `dprk-it-worker-laundering-civil-forfeiture-doj-2025` (different — $7.74M) | MERGE 225M pair into one event w/ DOJ as primary actor + Tether/OKX as executor; keep $7.74M separate. |
| **Garantex takedown** | S3 `garantex-besciokov-mira-serda-doj-2025` ↔ S5 `tether-garantex-usdt-freeze-2025-03` ↔ corpus S1 `grinex-garantex-successor-ofac-2025` | KEEP all three (DOJ indictment, Tether freeze, OFAC successor are genuinely distinct nodes); cross-link as one campaign. |
| **Cryptex/UAPS/PM2BTC** | S3 `cryptex-uaps-pm2btc-ivanov-shakhmametov-doj-2024` ↔ corpus S1 `cryptex-ofac-2024` + S5 `circle-usdc-cryptex-freeze-2024` | KEEP S3 (new DOJ twin), cross-link to existing S1/S5. |
| **911 S5 botnet** | S1 `botnet-911-s5-ofac-2024-05` (DOJ arrest mentioned in source) | KEEP S1; no S3 candidate proposed. |
| **HyperFund** | S3 `hyperfund-doj-charges-2024` (parallel SEC noted) | KEEP as single (DOJ+SEC same day, one event). |
| **ShapeShift** | S3 `sec-shapeshift-unregistered-dealer-2024-03` ↔ S5 `shapeshift-mandatory-kyc-anonymity-end-2018-09` | KEEP both — totally different events (2024 SEC dealer charge vs. 2018 voluntary KYC). |
| **Prince Group / DKBA / pig-butchering Nov 2025** | S1 `prince-group-chen-zhi-ofac-2025-10`, `dkba-burma-scam-compound-ofac-2025-11` | KEEP both (distinct designations). |

### C. Internal S4-asia ↔ S4-row residual dupes already counted above

Net S4-row duplicates removed: **4** (India tax, Vietnam, Pakistan, Nepal). S4-row's effective new count drops from 29 → **~25**.

**Total dropped/merged:** ~7 (Semenov S2, Huobi corpus dup, 4 S4-row dups, 1 S5/S3 pig-butchering merge). **Net deduped gap list ≈ 230 candidates.**

---

## 2. DEDUPED GAP LIST — BY STRATUM × ERA

Counts are post-dedup new candidates.

### S1 — OFAC SDN (24 → 24 new)
- **2017-2020:** `zheng-yan-fentanyl-ofac-2019-08`, `terror-financing-crypto-seizure` (that's S3), `fayzimatov-alqaeda-2021-07` *(2021)*
- **2021-2025:** all remaining 23 — BitRiver (first mining co.), Task Force Rusich, Genesis Market, Wang Hongfei fentanyl, Hanafin/Huriya, Chinyong/Kim Sang Man, China-fentanyl-network 2023-10, Kimsuky, Netex24/Bitpapa, al-Law Hezbollah, OKO/KB-Vostok drones, 911-S5 botnet, Nordic Resistance, Evil Corp 2024, Nemesis/Parsarad, Prince Group/Chen Zhi, Cheil Credit Bank, DKBA, Media Land/Volosovik, Tengyue fentanyl, Derakhshan/Alivand IRGC.
- **Era split:** 2019 ×1, 2021 ×1, **2022-2025 ×22.**

### S2 — OFAC Removal (1 → 0 new after dedup)
- Semenov dropped. **Stratum is census-complete.**

### S3 — DOJ/SEC/CFTC/FinCEN (26 DOJ + 17 SEC/CFTC/FinCEN = 43 new)
- **2007-2012:** none (back-fill is in proto/early-bitcoin agents, see below).
- **2013-2016:** `sec-dao-report-21a-2017-07` is 2017; `bitcoin-maven-tetley-doj-2018` is 2018. **None genuinely 2013-16 here** — gap.
- **2017-2020:** Centra Tech 2018, Bitcoin Maven 2018, OneCoin 2019, Crypto Capital/Fowler 2019, terror-financing seizure 2020, Colonial/DarkSide 2021*(boundary)*, SEC DAO Report 2017, EtherDelta/Coburn 2018, TokenLot 2018, Kik 2020, FinCEN Powers 2019.
- **2021-2025:** the bulk — Bitcoin Fog/Sterlingov, Bitfinex/Lichtenstein-Morgan, Silk Road/Zhong, BitConnect, Sim DOJ, DPRK $7.74M forfeiture, NetWalker, REvil, Blender/Sinbad operators, Mango/Eisenberg, OKX plea, $225M pig-butchering, Garantex DOJ, HyperFund, IcomTech/Forcount, Banmeet Singh, BTC-e/Vinnik plea, SafeMoon, HashFlare, Cryptex DOJ, plus SEC LBRY/Poloniex/Nexo/TradeStation/ShapeShift/Consensys/Abra/eToro, CFTC Opyn/bZeroX, FinCEN CVC-mixing NPRM/Paxful.

### S4 — Nation-state (asia 31 + row 25 = 56 new)
- **2007-2012:** none new (early-bitcoin agent covers).
- **2013-2016:** Kenya 2015 ×1.
- **2017-2020:** Vietnam 2017, Nepal 2017, Bangladesh 2017, Morocco 2017, Algeria 2017, Iraq 2017, Korea real-name 2018, Indonesia BI 2018, Cambodia 2018, Saudi 2018, Pakistan 2018, China-PBOC-2019, Korea privacy 2019/OKEx, Myanmar 2020, Egypt 2020, Qatar 2020, UAE-SCA 2020, Japan 2x leverage 2020, India SC reversal 2020. *(~19)*
- **2021-2025:** China mining-NDRC/payment-channel/search-block 2021, Tencent NFT 2022, Korea FIU/privacy/VAUPA, Indonesia MUI/Kominfo/OJK, Philippines BSP/NTC, Thailand payment/staking bans, Taiwan AML, Pakistan Senate, Nepal 2021, Sri Lanka, Singapore ad-ban, Nigeria-Binance 2024, Bolivia lift, Venezuela SUNACRIP, Kuwait, Iran CBI freeze, Kazakhstan mining tax, plus US state-level (BlockFi/Celsius/Nexo multistate, NYDFS-Bittrex, NYDFS not here) and Canada CSA-PRU. *(~35)*

### S5 — Corporate (cex 31 + defi ~20 = ~51 new; long tail unbounded)
- **2013-2016:** none.
- **2017-2020:** Bitfinex-US-exit 2017, ShapeShift-KYC 2018, Binance.com-US-geofence 2019, Poloniex-US 2019, Upbit/OKEx privacy 2019, GitHub sanctioned-country 2019, Binance-DEX-geoblock 2019. *(~7)*
- **2021-2025:** everything else — Bittrex privacy 2021, Binance global XMR 2024, Upbit/Bithumb purge 2021, eToro ADA/TRX, the entire **2023 Canada exit wave** (OKX/Paxos/Bybit/Binance), **2023 EU/UK Binance retreat** (Netherlands/Cyprus/Austria/Belgium/Germany/UK), Gemini-NL, OKX-India/Nigeria, Binance-Nigeria-naira, Bybit-France, the **MiCA stablecoin-delisting wave** (Coinbase/Crypto.com/Binance/Gate.io 2024-25), Bittrex Global shutdown; plus the **Tether/Circle freeze cluster** (Garantex, Bybit-Lazarus, Multichain, sealed-16-addr, WazirX, Iran-Economic-Fury 2026, T3 FCU), frontend/RPC/app-store blocks (Orca, dYdX-Canada, OpenSea/MetaMask, Infura-Venezuela, MetaMask/Uniswap App Store, PancakeSwap, Magic Eden).

### S6 — Supranational (24 → 23 new)
- **All 2021-2026.** FATF targeted updates 2022/2024/2025 + R.16 overhaul + 2021 RBA guidance + 2026 stablecoin/oVASP reports; BCBS SCO60 2022 + disclosure 2024; IOSCO crypto-2023/DeFi-2023/investor-ed-2024/thematic-2025; FSB GSC-2023/EMDE-2024/thematic-2025, IMF-FSB synthesis 2023, G20 status 2024; EU sanctions 16th-20th, EU-TFR application 2024-12.

### Proto (2007-2012) & Early-Bitcoin (2013-2016) — NOT in the 238 JSON
These two agents reported **13 + 23 = 36** candidates in their coverage notes but their candidate rows were **not included in the JSON payload** (the JSON starts at S1-ofac). This is the single largest blind spot in this synthesis — see §4/§5.

---

## 3. PER-STRATUM COVERAGE ESTIMATES

| Stratum | Corpus has (N) | New gap-fill (M_filled) | Residual long-tail (M_tail) | Coverage after fill | Census-complete? |
|---|---|---|---|---|---|
| **S1 OFAC** | ~33 | 24 | ~6-12 (update/re-listings, minor terror refreshes) | 57/(57+~9) ≈ **86%** | **Near-complete.** Closeable via line-by-line treasury.gov Recent Actions crawl for "digital currency address." |
| **S2 Removal** | 1 | 0 | ~0 | **~100%** | **Census-complete** (universe is genuinely 1 event). |
| **S3 DOJ** | ~22 | 26 | **100-200+** (darknet-vendor forfeitures, small P2P-MSB, ransomware seizures, Ponzi civil forfeitures, NFT cases) | 48/(48+~150) ≈ **24-32%** of *full* universe; but ≈ **70%+** of *significant/canonical* tier | **Long tail (significant tier near-complete; full tail irreducible).** |
| **S3 SEC/CFTC/FinCEN** | ~25 | 17 | ~10-20 (issuer-fraud→delisting cases, CFTC Ponzi, state actions) | 42/(42+~15) ≈ **74%** of censorship-effect subset | **Near-complete for censorship-effect subset**; pure-fraud tail excluded by design. |
| **S4 Nation-state** | ~80 | 52 (post-dedup) | ~30-50 (EU pre-MiCA members, soft 2014 warnings, smaller jurisdictions, 2024-25 refreshes) | 132/(132+~40) ≈ **77%** | **Moderate-high.** Closeable but with a real tail of minor/soft warnings. |
| **S5 Corporate** | ~50 | ~51 | **30-50+ structurally unbounded** (per-exchange MiCA/privacy delistings run dozens/yr; per-address freezes in the thousands) | 101/(101+~40 enumerable) ≈ **70%** of *notable* tier only | **Irreducible long tail.** Census-complete is impossible at address/per-jurisdiction granularity; only "one notable incident/policy = one event" is tractable. |
| **S6 Supranational** | 24 | 23 | ~5-10 (EU 17th pkg, MiCA L2 2025 tranche, BIS/CPMI analytical, EBA RTS, UNSC DPRK refreshes) | 47/(47+~8) ≈ **85%** | **Near-complete** for binding/quasi-binding instruments. |
| **Proto 2007-2012** | ~15 (in corpus) | **13 (NOT in JSON)** | ~5-10 | ~28/(28+~8) ≈ **78%** *if back-filled* | Near-complete **only if the 13 are recovered.** |
| **Early-Bitcoin 2013-2016** | ~25 (in corpus) | **23 (NOT in JSON)** | ~10-15 | ~48/(48+~12) ≈ **80%** *if back-filled* | Near-complete **only if the 23 are recovered.** |

**Bottom line on census-completeness after gap-fill:**
- **Census-complete / near-complete:** S2 (done), S1 (~86%), S6 (~85%), S3-SEC/CFTC/FinCEN (~74% of in-scope), proto & early-bitcoin (~78-80% *if recovered*).
- **Tractable but with a real moderate tail:** S4 (~77%).
- **Irreducible long tail — census impossible:** **S5** (per-exchange delisting + per-address freeze universe is effectively unbounded; cap at "notable incident/policy"). **S3-DOJ** full universe also has a heavy tail, though its canonical tier is well-covered.

---

## 4. KEY GAPS THE AGENTS THEMSELVES FLAGGED (not in the 238)

1. **PROTO + EARLY-BITCOIN candidate rows are missing from the JSON entirely.** 36 dated, primary-sourced candidates (e-gold 2007 indictment, full Liberty Reserve timeline, 2013-14 national warnings, Bitstamp-2015/Bitfinex-2016/Cryptsy-2016 access-restriction events, Dec-2013 joint-ESA warning, CFPB-2014, Mt.Gox Ch.15) exist per the coverage notes but were not transmitted. **This is the highest-priority recovery action** — it is exactly the under-collected 2007-2016 era the task prioritizes.
2. **S5-defi JSON truncated** — last entry cut off; 1-2 entries (incl. a `tether-apac-pig-butchering…` row) lost.

---

## 5. PRIORITIZED TOP-TIER GAP LIST (highest-value missing cases)

Ranked by canonical/seminal status × evidential tractability. **2007-2016 back-fill called out first** per task.

### TIER 0 — 2007-2016 BACK-FILL (most under-collected era; recover + admit first)
1. **e-gold DOJ indictment/guilty plea 2007** *(proto; not in JSON — recover)* — the seminal proto-DGC enforcement action; corpus has e-Bullion/e-gold 2008 but the 2007 indictment is the anchor.
2. **Liberty Reserve takedown 2013** + GoldAge precursor *(proto; not in JSON — recover)* — landmark §311 / largest pre-Bitcoin money-laundering prosecution.
3. **Bitstamp 2015 hack trading-halt; Bitfinex Aug-2016 hack withdrawal-haircut; Cryptsy 2016 collapse** *(early-bitcoin; not in JSON — recover)* — canonical exchange access-restriction events.
4. **Dec-2013 joint EBA/ESMA/EIOPA warning; CFPB Aug-2014 advisory; Mt.Gox US Chapter-15 recognition 2014** *(early-bitcoin; not in JSON — recover)* — seminal supranational/US-consumer nodes.

### TIER 1 — Canonical "firsts" and landmark events (in the JSON, admit)
5. **`bitriver-russia-mining-ofac-2022-04`** — *first-ever OFAC sanction of a crypto mining company.*
6. **`zheng-yan-fentanyl-ofac-2019-08`** — *first narcotics-related crypto SDN action.*
7. **`sec-dao-report-21a-2017-07`** — the DAO Report; foundational "tokens = securities" mandate driving all subsequent US geofencing/delisting.
8. **`sec-etherdelta-coburn-unregistered-exchange-2018-11`** — first SEC action treating a DEX as an illegal unregistered exchange.
9. **`bitfinex-hack-lichtenstein-morgan-doj-2022`** — then-largest financial seizure in DOJ history (~94k BTC).
10. **`silk-road-zhong-50000-btc-seizure-doj-2022`** — second-largest DOJ seizure; distinct from 2013 takedown.
11. **`colonial-pipeline-darkside-ransom-clawback-doj-2021`** — landmark ransomware crypto clawback.
12. **`fincen-cvc-mixing-special-measure-nprm-2023-10`** — first activity-based §311 special measure (the "mixer NPRM").
13. **`bcbs-cryptoasset-prudential-standard-sco60-2022`** — entire Basel/BIS crypto-capital track absent from corpus; this is its anchor.
14. **`eu-19th-russia-sanctions-a7a5-crypto-ban-2025`** — first EU prohibition on transacting a *specific* crypto-asset (A7A5 stablecoin).

### TIER 2 — High-value structural / wave events (admit)
15. **MiCA stablecoin-delisting wave**: `coinbase-eu-usdt-stablecoin-delisting-2024-12`, `crypto-com-eu-usdt-2025-01`, `binance-eea-usdt-2025-03`, `gate-io-privacy-coin-perpetuals-2024-12` — captures the MiCA enforcement cascade (corpus only has Kraken-EU).
16. **2023 Canada CSA exit wave**: `okx-canada-2023-03`, `paxos-canada-2023-04`, `bybit-canada-2023-05`, `binance-canada-2023-05` + `canada-csa-pre-registration-undertaking-2023-02` (the S4 trigger).
17. **2023 Binance Europe retreat**: `binance-netherlands`, `binance-europe-retreat-cyprus-austria-belgium`, `binance-uk-new-user-halt`.
18. **`okx-aux-cayes-doj-guilty-plea-2025`**, **`btc-e-vinnik-guilty-plea-doj-2024`**, **`garantex-besciokov-doj-2025`** — major exchange/launderer dispositions (note Vinnik/Garantex cross-link to existing corpus nodes).
19. **FATF/FSB/IOSCO governance track**: `fatf-targeted-update-2022/2024/2025`, `fatf-recommendation-16-overhaul-2025`, `iosco-crypto-recommendations-2023`, `iosco-defi-2023`, `fsb-global-stablecoin-recommendations-2023` — fills the S6 standard-setter gaps.
20. **First-mover national bans** (S4 back-fill, well-documented): `vietnam-2017`, `nepal-2017`, `myanmar-cbm-2020`, `egypt-banking-law-194-2020`, `cambodia-nbc-2018`, `india-sc-iamai-rbi-reversal-2020` (the judicial reversal of a corpus event).

### TIER 3 — Solid but lower-priority / tail
- Privacy-coin delistings (`bittrex-2021`, `upbit-2019`, `upbit-bithumb-2021`, `binance-global-xmr-2024`); frontend/app-store geoblocks (Orca, dYdX-Canada, PancakeSwap, Magic Eden, MetaMask/Uniswap App Store); US-state lending-product C&Ds (BlockFi/Celsius/Nexo multistate); the Tether/Circle freeze incidents not already in corpus.

---

## 6. RESIDUAL CLOSURE ACTIONS (to reach census)
- **Recover the proto-2007-2012 (13) and early-bitcoin-2013-2016 (23) candidate rows** — missing from JSON; highest leverage for the prioritized era.
- **S1:** line-by-line `home.treasury.gov` Recent Actions crawl filtering "digital currency address" to catch ~6-12 update/refresh designations.
- **S3-SEC:** enumerate the SEC "Crypto Assets and Cyber Enforcement Actions" spreadsheet for the ~10-20 issuer-fraud→delisting cases (Tron/Sun, Hex/Heart) the agent excluded.
- **S4:** EU pre-MiCA member registrations (Italy OAM, Spain CNMV, Portugal, Ireland, Estonia) + soft 2014 national warnings.
- **S5:** accept this stratum will never census-close; freeze the inclusion rule at "one notable incident/policy = one event."

**Net deduped new gap list: ~230 candidates** (from 238), **plus ~36 un-transmitted proto/early-bitcoin candidates to recover.** Strata reaching near-census after fill: **S1, S2, S6, S3-SEC subset, S4** (with a modest tail), and **proto/early-bitcoin if recovered.** Irreducible long tail: **S5** (and the full-universe tail of **S3-DOJ**).
