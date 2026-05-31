# Next steps — censorship-event-database

Carried forward from the 2026-05-31 session close (corpus at 368 admitted / 398 total; see
`analysis/STATE_OF_CORPUS_2026_05_31.md`). Ordered by priority. Nothing here is pushed — all work is local.

## P1 — Scope / design decisions
- [x] **US-state enforcement stratum.** Resolved by delegated automation on 2026-05-31: do **not**
      add `S7_us_state` and do **not** fold state regulators into S3. US state/subnational
      regulator administrative actions use `trigger.type=regulatory_enforcement` and
      `research_stratum=S4_nation_state`; S3 remains reserved for US federal DOJ/SEC/CFTC/FinCEN
      and court actions. This matches the existing NY OAG / NJ Bureau precedent and avoids
      paper-table churn from a new stratum.
- [x] **iraq-cbi-cryptocurrency-prohibition-2017-12** — §9 ban-vs-warning ruling resolved. The
      captured Arabic CBI page is genuine, but the operative text supports issuing a circular
      against use rather than itself establishing a clearly binding prohibition; conservative
      ruling is `status=rejected` as warning/context-only.
- [x] **goldage-ny-state-indictment-2006-07** — pre-2007 boundary resolved. Recommended strict
      frame applied: the case is real and retained as provenance, but `status=rejected` because
      the declared census starts on 2007-01-01 and no pre-2007 temporal tier exists.

## P2 — Held drafts to finish (mechanical once unblocked)
- [x] **t3-financial-crime-unit-launch-2024-09** — representative on-chain repair completed.
      The launch source only gives an aggregate "over USDT 12M" freeze figure and does not enumerate a
      full frozen-address roster, so the row remains `target.enumeration=subset` and
      `asset_onchain=partially_measured`. Two same-day TronGrid-verified USDT
      `AddedBlackList(address)` tx hashes are now pinned:
      `b08e804e631be03ff779027181d7069be9135d57890fc32856d8b093c07f0c5d`
      for `TYMtkQ1rdvu5XnHFsg5SWizsdr4zk8AgqS`, and
      `0f7c52af61004b54bc9de3ec37695c3a3d61fd135b2db29faee824386f604856`
      for `TDSp29bjTQZjQ6qoMB9VK74NnbbhT4aPB8`. The row remains `status=draft`
      only because admission is human-only (`origin=agent_draft` cannot be promoted by automation).
      **ren-protocol stays a terminal draft**
      (off-chain RenVM darknode signature cessation — no tx can exist; it's the §1.6 precedent, leave as-is).
- [x] **circle-usdc-sealed-civil-case-16-address-freeze-2026-03** — full-list on-chain repair completed.
      AMLBot's 2026-03-26 investigation is captured + Wayback-pinned and enumerates the complete
      16-address set. Ethereum JSON-RPC verification found a matching USDC `Blacklisted(address)` log
      for all 16 addresses on 2026-03-23 (blocks 24722161-24722385, 18:59:11-19:43:59 UTC);
      all 16 blacklist receipts are cached. Coverage is now `measured` and `target.enumeration=complete`.
      The Goated.com `UnBlacklisted(address)` recovery tx remains pinned. The row remains `status=draft`
      only because admission is human-only (`origin=agent_draft` cannot be promoted by automation).
- [x] **tether-ofac-iran-economic-fury-344m-freeze-2026-04** — primary legal + on-chain repair
      completed. OFAC Recent Actions 2026-04-24 is captured locally and enumerates the two Central Bank
      of Iran TRON addresses; two TronGrid-verified USDT AddedBlackList tx hashes in block 82092618 are
      pinned. The row remains `status=draft` only because admission is human-only
      (`origin=agent_draft` cannot be promoted by automation).
- [x] **tether-okx-doj-pig-butchering-225m-freeze-2025-06** — primary legal + on-chain repair
      completed. The row is now modeled as the 2025 D.D.C. forfeiture / Tether burn-reissue stage rather than a
      second new 2025 freeze. DOJ OPA + verified complaint captures are pinned, the seven USDT Token Group
      addresses are enumerated, seven 2023 AddedBlackList txs and seven 2025 DestroyedBlackFunds txs are cached,
      and the sibling 2023 Tether freeze row now carries `asset_onchain=partially_measured` for the seven pinned
      addresses. The 2025 row remains `status=draft` only because admission is human-only
      (`origin=agent_draft` cannot be promoted by automation).
- [x] **circle-usdc-multichain-hack-freeze-2023-07** — tx_hash repair completed. The stale 2023-10
      candidate date was corrected to the actual 2023-07-07 USDC blacklist block; all three
      `Blacklisted(address)` tx hashes and full addresses are pinned. The row remains `status=draft`
      only because admission is human-only (`origin=agent_draft` cannot be promoted by automation).
- [x] **task-force-rusich-ofac-2022-09** — crypto-nexus source pinned. The official OFAC Recent
      Actions page for 2022-09-15 is now captured locally and enumerates the five digital-currency
      addresses (2 XBT / 2 ETH / 1 USDT-on-Tron). The event remains `status=draft` only because
      admission is human-only (`origin=agent_draft` cannot be promoted by automation).
- [x] **bitfinex-us-retail-customer-exit-2017-11** — re-captured. The event now cites the 2017-10-18
      Wayback memento of the Bitcoin.com article, whose rendered body confirms the US-retail service
      termination and November 9 deadline. The event remains `status=draft` only because admission is
      human-only (`origin=agent_draft` cannot be promoted by automation).

## P3 — Methodology debt (codebook process)
- [ ] **`evidence_tier` IRR pass.** Codebook 4.0.0 added a decision-rule (the `attested_secondary` tier). The
      codebook's own "Effective" convention requires a new IRR pass on ≥ 10 events for a decision-rule change.
      Run a 2-coder IRR pass on a 10–15 event sample of the 34 `attested_secondary` rows to confirm inter-rater
      agreement on (a) §9-clarity and (b) the single-source judgment. Record κ. This is outstanding process debt.
      Prep packet created at `analysis/evidence_tier_irr_packet_2026_05_31.md`; it is intentionally blank and
      must not be treated as completed IRR until two independent human coders fill it.

## P4 — Census long-tail (ongoing, low-yield-per-event)
- [ ] **`census_gap_candidates.tsv`** has 264 agent-sourced candidate rows; `census_gap_registry.tsv` has 149
      verified+scope-tagged rows. Registry reconciliation on 2026-05-31 found 101 already covered
      (`in_corpus=true`, including exact, duplicate-covered, and semantic-covered rows). Of the remaining
      48 `in_corpus=false` rows, all 48 are now reviewed-excluded/context-only under codebook §9, leaving
      0 currently actionable registry rows. Exact-id remaining queue: 35 candidate rows not yet in events
      or registry. Continue by promoting new rows from the 264-row candidate pool
      into the verified registry: verify candidate → dedup against corpus → §9 scope → author as verified
      draft → adversarial verify → admit (or `attested_secondary` if single-source). Heaviest gap remains
      the under-collected 2013–2020 era and non-US/non-English actions.
      `bangladesh-bb-crypto-illegality-2017-09` was closed as a date-corrected 2017-12-24 Bangladesh Bank
      cautionary notice: the source record supports a request/warning about possible legal risk, not a
      distinct service denial, platform block, payment-rail prohibition, or binding ban beyond the
      already-admitted `bangladesh-bb-bitcoin-warning-2014`. `vietnam-sbv-bitcoin-prohibition-2014-02`
      was closed as semantic-covered by `vietnam-sbv-payment-prohibition-2017-10`; the inspected source
      is a 2017-10 SBV ban report, not a distinct 2014 event. `cftc-bzerox-founders-settlement-2022-09`
      was closed as covered by `cftc-v-ooki-dao-2022`, because the corpus row already uses the same CFTC
      8590-22 trigger and explicitly enumerates bZeroX LLC, both founders, and successor Ooki DAO.
      Follow-on triage added 8 more registry rows: Liberty Reserve takedown/sentencing, e-Bullion
      indictment, and e-Gold sentencing are covered by existing corpus enforcement arcs; Roman Semenov
      2025 is an OFAC authority-tag change with no independent access restoration; Centra and BitConnect
      are fraud/Ponzi prosecutions; Mt. Gox Chapter 15 is bankruptcy administration after platform failure.
      A second follow-on S4 triage added 25 exact-slug closures: 18 semantic-covered duplicates
      (Kenya, Nepal, Pakistan, Qatar, Egypt, UAE, Thailand, BlockFi, Taiwan, Korea, Sri Lanka, Jordan,
      and Iraq) and 7 reviewed-excluded soft warning / non-recognition rows (France, Norway, Malaysia,
      Belgium, Mexico, Denmark, and Cambodia).
      A third follow-on triage added 20 more closures: 10 covered slug mismatches/date corrections
      (Algeria, Argentina, Canada CSA, Venezuela SUNACRIP, Nigeria Binance, OKX Canada, Huobi privacy
      coins, and Circle/Multichain) plus 10 reviewed exclusions for political pressure, draft legislation,
      fraud/Ponzi/rug-pull prosecutions, non-binding guidance, administrative framework transfer, and a
      malformed placeholder candidate.
      A fourth follow-on triage added 20 closures: 12 covered/date-corrected rows (Korea privacy-coin
      delistings, Liberty Reserve Costa Rica, BTC-e/Vinnik disposition, Sinbad/Blender DOJ, DOJ/Tether
      pig-butchering forfeiture, Circle sealed-civil freeze, OpenSea/MetaMask sanctions blocks, EU TFR
      application, IMF-FSB synthesis paper, Binance Canada, and Iran CBI exchange-payment-gateway block)
      and 8 reviewed exclusions (FinCEN CVC-mixing NPRM, Mango exploit prosecution, India VDA tax/TDS
      duplicates, Kazakhstan mining tax hike, Pakistan ban-intent statement, and G20 roadmap status report).
      `bittrex-global-shutdown-2023-11`
      was narrowed to a primary-corporate-captured `origin=agent_draft` event; it is net-new versus
      `sec-v-bittrex-2023` but still needs human admission / causation review before becoming a paper row.
      `colonial-pipeline-darkside-ransom-clawback-doj-2021` was narrowed to a one-address
      primary-onchain-pinned `origin=agent_draft` event; it clears the mechanical tx_hash gate but still
      needs human attribution/admission review.
      This continuation added two more official-source agent drafts:
      `nydfs-bittrex-bitlicense-denial-2019-04` (NYDFS press release + denial-letter PDF capture) and
      `kuwait-cma-virtual-assets-prohibition-2023-07` (CBK official PDF capture; CMA HTML verified live but
      CLI capture timed out). It also closed Singapore MAS public-advertising and Nexo eight-state
      candidates as covered by existing corpus rows.
      `celsius-multistate-cease-desist-earn-2021-09` was added as a conservative official-source draft
      using the New Jersey and Texas 2021-09-17 PDFs; the short-form duplicate candidate is now covered in
      the registry. It remains non-admitted pending OCR/human confirmation of the scanned New Jersey order.
      A fifth follow-on triage added 5 reviewed exclusions for disposition-only SEC/DOJ rows with no new
      platform-access restriction: ShapeShift's 2024 SEC settlement, the Bitfinex hack laundering case, the
      James Zhong Silk Road forfeiture, the Banmeet Singh dark-web vendor forfeiture, and the DPRK IT-worker
      civil forfeiture action.
      A sixth follow-on triage added 4 exact-id closures: Cheil / First Credit Bank is covered by
      `dprk-usdt-network-ofac-2025`; DataCell / Valitor Supreme Court is covered as downstream trajectory
      of `datacell-v-valitor-iceland-district-court-2012-07`; `bitcoin-maven-tetley-doj-2018` was added
      as an official DOJ / Wayback-captured `origin=agent_draft` individual-MSB off-ramp row; and the
      Sim Hyon Sop DOJ indictment was excluded as a same-day criminal-indictment disposition with the
      sanctions/access-denial component already modeled by `ofac-dprk-it-worker-sim-hyon-sop-2023-04`.
      A seventh follow-on triage added 3 OFAC closures: `fayzimatov-alqaeda-syria-ofac-2021-07` was added
      as an official OFAC/Treasury-captured `origin=agent_draft` individual-BTC null_case row; Kimsuky 2023
      and Nordic Resistance Movement 2024 were reviewed-excluded because their official OFAC artifacts do
      not enumerate cryptocurrency addresses or a crypto-platform/payment-rail access restriction.
      An eighth follow-on triage added `crypto-capital-fowler-doj-2019` as an official DOJ / Wayback-captured
      `origin=agent_draft` off-ramp shadow-banking row. It is scoped narrowly to Fowler / GTS / Crypto Capital's
      fiat-rail service for cryptocurrency exchanges, with no claim of an exchange shutdown, frontend seizure,
      or on-chain asset freeze.
      A ninth follow-on triage added `terror-financing-crypto-seizure-doj-2020` as an official DOJ /
      Wayback-captured `origin=agent_draft` l4_frontend seizure row. The draft narrowly codes seized
      websites/Facebook pages; reported cryptocurrency-account seizures remain `asset_onchain=not_measured`
      until a public tx_hash is pinned.
      A tenth follow-on triage added `revil-vasinskyi-polyanin-doj-2021` as an official DOJ /
      Wayback-captured `origin=agent_draft` ransomware forfeiture row. The draft records DOJ's USD 6.1M
      seizure and later 39.89138522 BTC final-forfeiture statement, but keeps `asset_onchain=not_measured`
      until a public tx_hash, address-history capture, or body-hashed court complaint enumerating the wallet
      is pinned.
      An eleventh follow-on triage added `netwalker-vachon-desjardins-doj-2022` as an official DOJ + RCMP /
      Wayback-captured `origin=agent_draft` NetWalker ransomware forfeiture row. The draft records the
      official 719 BTC search-seizure and 680 BTC Canadian forfeiture facts, but keeps
      `asset_onchain=not_measured` until a public tx_hash, address-history capture, or body-hashed court
      document enumerating the wallet is pinned.
      A twelfth follow-on triage added `bitcoin-fog-sterlingov-doj-2024` as an official DOJ /
      Wayback-captured `origin=agent_draft` Bitcoin-mixer operator-state row. The draft records the
      2024 conviction/sentencing criminal-finality endpoint, but keeps the DOJ-reported 1,354/1,345 BTC
      forfeiture facts at `asset_onchain=not_measured` until a public tx_hash, address-history capture,
      or wallet-enumerating court artifact is pinned.
      A thirteenth follow-on triage reviewed `fincen-paxful-bsa-penalty-2025-08` against official FinCEN
      and DOJ sources and closed it as reviewed-excluded: the 2025-12-09 Consent Order / guilty-plea
      resolution imposes monetary, cooperation, record-retention, and successor-assignment terms for past
      AML/BSA failures, but no platform shutdown, user offboarding, geoblock, industry bar, asset freeze,
      or other new service-denial action.
      A fourteenth follow-on triage added `lebanon-bdl-bitcoin-warning-2013-12` as an official BDL-PDF
      captured `origin=agent_draft` historical-baseline row. The draft narrowly models BDL Announcement
      No. 900 as a class-level warning / electronic-money restriction signal addressed to banks,
      financial institutions, exchange institutions, brokerage institutions, and the public; it does not
      claim a specific exchange shutdown, user offboarding, domain block, or on-chain action.
      A fifteenth follow-on triage closed `russia-prosecutor-general-monetary-surrogate-2014-02`
      as semantic-covered by admitted `russia-cbr-bitcoin-information-letter-2014`: the official
      Prosecutor General Wayback page confirms the 2014 monetary-surrogate / no-use posture and
      interagency coordination with CBR, FSB, and MVD, but does not add a distinct exchange shutdown,
      banking-rail cutoff, domain block, asset freeze, or measured off-ramp observation.
- [ ] **Task-2 capture route**: opportunistic official-PDF wins as found (central-bank circulars, law texts on
      standard URLs). Skip JS-gated exchange pages + bot-protected gov HTML.

## P5 — Release prep (when ready — maintainer-gated, NEVER auto-push)
- [ ] **`CITATION.cff` `version`** is currently `0.2.0-rc-dryrun-11` (date-released 2026-05-25), now far behind
      the corpus. When the maintainer wants to mint a release: bump `version` (single source of truth for
      `dataset_version`) + `date-released`, then a git tag mints the Zenodo DOI. Do NOT tag/push autonomously.
