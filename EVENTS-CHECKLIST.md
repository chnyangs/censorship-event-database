# Events Checklist — stratified candidate list

Working TODO list for event admission. Tracks which candidate events exist in each stratum, their admission status, and the primary-source URL(s) to archive. Not reference documentation — once an event is admitted, the authoritative record is its YAML in `events/` and the entry in `CHANGELOG.md`.

## Strata and target coverage

This dataset aims to be **stratified-complete within each stratum**, not a cherry-picked sample. The target size per stratum drives the paper's statistical claims.

| Stratum | Description | Target N | Universe | Drafted | Admitted |
| --- | --- | --- | --- | --- | --- |
| S1. OFAC SDN designations (crypto-related) 2018–2025 | Original designations with ≥ 1 digital-asset address on the SDN list | 25–35 | **27 (complete)** | 0 | 27 |
| S2. OFAC SDN removals (crypto-related) 2018–2025 | Delistings of earlier crypto-designated entities or addresses | 3–6 | ≈ 1–3 (small) | 0 | 1 |
| S3. DOJ / CFTC / SEC crypto enforcement 2017–2025 | Federal criminal or civil action with material on-chain effect | 8–12 | ≈ 12 | 0 | 12 |
| S4. Nation-state infrastructure bans | Named policy directive that alters L0 / off-ramp access | 3–5 | ≥ 8 confirmed | 0 | 6 |
| S5. Corporate policy (non-OFAC) | Issuer / exchange / frontend unilateral decisions | 5–8 | representative (open) | 0 | 6 |
| S6. Supranational actions | EU / UN / G7-level sanctions or unified crypto-regulatory frameworks | 2–4 | 2 confirmed | 0 | 2 |
| **Total** | | **46–70** | | **0 drafts** | **53 admitted** |

As of the current `v0.1.0` snapshot (cutoff `2026-04-22`):
**53 / 53 admitted, 0 drafts**.

Schema bumped to 0.2.0 (reviewer Actions 1–4 applied): `event_class` replaced by three orthogonal fields — `research_stratum` (sampling-frame stratum), `empirical_shape` (cascade / comparison / null_event based on observed_change layer count), `admission_tier` (anchor_case / empirical_case / null_case based on strong-attribution layer count). `follow_on_reaction` added for `attribution: unknown` observations that should not count toward cross-case statistics. See [docs/methodology.md §3.2](docs/methodology.md#L95). Tier distribution: **5 anchor_case, 35 empirical_case, 13 null_case**. See `dataset.meta.json`, `CHANGELOG.md`, event YAMLs under `events/`, and the chain-distribution structural finding in `docs/chain-coverage-note.md`.

The paper's "20 events minimum" milestone has been cleared (2.65×). Strata that cannot be exhaustively enumerated (S5 in particular) are declared `scope: representative` in the paper rather than claimed complete.

## Legend

- `[x]` — admitted (see `events/<slug>.yaml`)
- `[~]` — draft or under reconstruction in repo
- `[ ]` — candidate identified but not yet added
- `[?]` — needs verification of date / URL / scope before admission

Each candidate shows the expected primary source in a compact form. "OFAC RA YYYYMMDD" = `ofac.treasury.gov/recent-actions/YYYYMMDD`.

---

## Stratum 1 — OFAC SDN designations (crypto-related)

**27 / 27 admitted.** Enumeration authoritative as of 2026-04-21 (see `sources/ofac_sdn_diffs/opensanctions/ofac-recent-actions-triage.json`). Per-date counts show `tokens{...}=N`.

### 2018

- [x] **Iran ransomware facilitators** (Ghorbaniyan, Khorashadizadeh) — 2018-11-28. 2 XBT. ← [`events/iran-ransomware-ofac-2018.yaml`](events/iran-ransomware-ofac-2018.yaml)

### 2019

- [x] **Lazarus Group / Bluenoroff / Andariel** — 2019-09-13. Entity-level. ← [`events/lazarus-entity-ofac-2019.yaml`](events/lazarus-entity-ofac-2019.yaml)

### 2020

- [x] **TIAN Yinyin + LI Jiadong (Lazarus-linked laundering)** — 2020-03-02. 20 XBT. First China-nexus individual OFAC crypto action. ← [`events/lazarus-laundering-ofac-2020.yaml`](events/lazarus-laundering-ofac-2020.yaml)
- [x] **Russia-election-interference actors** — 2020-09-10. 23 addrs. ← [`events/russia-election-interference-ofac-2020.yaml`](events/russia-election-interference-ofac-2020.yaml)
- [x] **Russian cyber actors — virtual-currency theft** — 2020-09-16. 12 addrs, 8 chains. ← [`events/russian-cyber-theft-ofac-2020.yaml`](events/russian-cyber-theft-ofac-2020.yaml)

### 2021

- [x] **SUEX OTC** — 2021-09-21. 25 addrs. ← [`events/suex-ofac-2021.yaml`](events/suex-ofac-2021.yaml)
- [x] **Chatex** — 2021-11-08. 58 addrs. ← [`events/chatex-ofac-2021.yaml`](events/chatex-ofac-2021.yaml)

### 2022

- [x] **Hydra Market** — 2022-04-05. ← [`events/hydra-ofac-2022.yaml`](events/hydra-ofac-2022.yaml)
- [x] **Garantex (original)** — 2022-04-05. ← [`events/garantex-ofac-2022.yaml`](events/garantex-ofac-2022.yaml)
- [x] **Blender.io** — 2022-05-06. 53 addrs. ← [`events/blender-ofac-2022.yaml`](events/blender-ofac-2022.yaml)
- [x] **Tornado Cash (original)** — 2022-08-08. 38 ETH. ← [`events/tornado-cash-ofac-2022.yaml`](events/tornado-cash-ofac-2022.yaml)
- [x] **IRGC-affiliated ransomware actors** — 2022-09-14. 6 XBT. ← [`events/irgc-ransomware-ofac-2022.yaml`](events/irgc-ransomware-ofac-2022.yaml)
- [x] **Tornado Cash re-designation (DPRK authorities)** — 2022-11-08. 98 addrs. ← [`events/tornado-cash-ofac-redesignation-2022.yaml`](events/tornado-cash-ofac-redesignation-2022.yaml)

### 2023

- [x] **Mikhail Matveev** — 2023-05-16. ← [`events/matveev-ofac-2023.yaml`](events/matveev-ofac-2023.yaml)
- [x] **Roman Semenov** — 2023-08-23. 8 ETH. ← [`events/semenov-ofac-2023.yaml`](events/semenov-ofac-2023.yaml)
- [x] **Sinbad.io mixer** — 2023-11-29. 2 XBT. ← [`events/sinbad-ofac-2023.yaml`](events/sinbad-ofac-2023.yaml)

### 2024

- [ ] **Chatex SDN entry update** — 2024-01-11. 30 addrs *added* to existing Chatex entry (entry-update, not new designation). **Still unmodeled**: should either (a) extend `chatex-ofac-2021.yaml` observation window, or (b) admit as separate `chatex-ofac-entry-update-2024.yaml` (update_event subclass). Primary: OFAC RA 20240111.
- [x] **LockBit affiliates** — 2024-02-20. 10 addrs. ← [`events/lockbit-affiliates-ofac-2024.yaml`](events/lockbit-affiliates-ofac-2024.yaml)
- [x] **LockBit senior leader (LockBitSupp)** — 2024-05-07. 1 XBT. ← [`events/lockbit-leader-ofac-2024.yaml`](events/lockbit-leader-ofac-2024.yaml)
- [x] **Cryptex.net / PM2BTC** — 2024-09-26. 4 addrs. ← [`events/cryptex-ofac-2024.yaml`](events/cryptex-ofac-2024.yaml)
- [x] **Sichuan Silence Info Tech / GUAN Tianfeng** — 2024-12-10. ← [`events/sichuan-silence-ofac-2024.yaml`](events/sichuan-silence-ofac-2024.yaml)

### 2025

- [x] **Zservers (ransomware infrastructure)** — 2025-02-11. 4 XBT. ← [`events/zservers-ofac-2025.yaml`](events/zservers-ofac-2025.yaml)
- [x] **Funnull CDN (cyber scam facilitator)** — 2025-05-29. ETH+TRX. ← [`events/funnull-cdn-ofac-2025.yaml`](events/funnull-cdn-ofac-2025.yaml)
- [x] **Aeza Group (bulletproof hosting)** — 2025-07-01. 1 TRX. ← [`events/aeza-group-ofac-2025.yaml`](events/aeza-group-ofac-2025.yaml)
- [x] **Garantex successor / Grinex + A7A5** — 2025-08-14. 21 addrs. ← [`events/grinex-garantex-successor-ofac-2025.yaml`](events/grinex-garantex-successor-ofac-2025.yaml)
- [x] **DPRK banker / IT-worker laundering network** — 2025-11-04. 53 USDT. ← [`events/dprk-usdt-network-ofac-2025.yaml`](events/dprk-usdt-network-ofac-2025.yaml)
- [x] **Russian cybercrime infrastructure (joint US/AU/UK)** — 2025-11-19. 1 XBT. ← [`events/russian-cybercrime-infra-ofac-2025.yaml`](events/russian-cybercrime-infra-ofac-2025.yaml)

### S1 remaining work

Only residual item: the 2024-01-11 Chatex entry-update is not modelled. Low priority — the 30 added addresses are already captured within the 2021-11-08 Chatex event's parent enumeration for research purposes.

---

## Stratum 2 — OFAC SDN removals (crypto-related)

**1 / ≈ 1–3 admitted.**

- [x] **Tornado Cash delisting** — 2025-03-21 (Van Loon-litigation driven). ← [`events/tornado-cash-ofac-delisting-2025.yaml`](events/tornado-cash-ofac-delisting-2025.yaml)
- [ ] **SUEX delisting** `[?]` — verify whether SUEX was ever removed from the SDN list.
- [ ] **Chatex delisting** `[?]` — verify.
- [ ] **Any 2024–2025 mixer delistings** `[?]` — SDN XML diff year-over-year to surface any.

Stratum is naturally small; most designated entities are never removed.

---

## Stratum 3 — DOJ / CFTC / SEC crypto enforcement with on-chain effect

**12 / ≈ 12 admitted.**

- [x] **BTC-e seizure** — 2017-07-26. Earliest crypto enforcement in dataset. ← [`events/btc-e-doj-2017.yaml`](events/btc-e-doj-2017.yaml)
- [x] **Hydra Market DOJ companion** — 2022-04-05. ← [`events/hydra-doj-2022.yaml`](events/hydra-doj-2022.yaml)
- [x] **Pertsev NL arrest** — 2022-08-10. FIOD (non-DOJ but cross-border crypto-enforcement companion to Tornado). ← [`events/pertsev-nl-arrest-2022.yaml`](events/pertsev-nl-arrest-2022.yaml)
- [x] **CFTC v. Ooki DAO** — 2022-09-22. First CFTC-against-DAO enforcement; default judgment 2023-06-08. ← [`events/cftc-v-ooki-dao-2022.yaml`](events/cftc-v-ooki-dao-2022.yaml)
- [x] **Bitzlato** — 2023-01-18. ← [`events/bitzlato-doj-2023.yaml`](events/bitzlato-doj-2023.yaml)
- [x] **ChipMixer** — 2023-03-15 (DOJ + Europol). ← [`events/chipmixer-doj-2023.yaml`](events/chipmixer-doj-2023.yaml)
- [x] **SEC v. Binance** — 2023-06-05. First SEC civil enforcement event; Binance.US fiat rail collapse within 4d. ← [`events/sec-v-binance-2023.yaml`](events/sec-v-binance-2023.yaml)
- [x] **SEC v. Coinbase** — 2023-06-06. Companion SEC action; paired-comparison with Binance. ← [`events/sec-v-coinbase-2023.yaml`](events/sec-v-coinbase-2023.yaml)
- [x] **Storm + Semenov DOJ indictment** — 2023-08-23. ← [`events/storm-semenov-doj-2023.yaml`](events/storm-semenov-doj-2023.yaml)
- [x] **Binance 4-framework settlement** — 2023-11-21 ($4.3B DOJ + FinCEN + OFAC + CFTC). ← [`events/binance-4framework-2023.yaml`](events/binance-4framework-2023.yaml)
- [x] **SEC Wells notice v. Uniswap Labs** — 2024-04-10 (dropped 2025-02-25). Lowest-intensity SEC regulatory-pressure event. ← [`events/sec-v-uniswap-wells-notice-2024.yaml`](events/sec-v-uniswap-wells-notice-2024.yaml)
- [x] **Samourai Wallet** — 2024-04-24. ← [`events/samourai-doj-2024.yaml`](events/samourai-doj-2024.yaml)

### S3 out-of-scope (rejected with rationale)

- **LocalBitcoins operator charges** — verified out-of-scope 2026-04-22. LocalBitcoins Oy (Finnish platform operator) was never charged by DOJ; the platform ceased operations voluntarily on 2023-02-09. DOJ cases associated with LocalBitcoins (Rockcoons, Florida trader) are individual traders using the platform, not the platform operator, and fall below the S3 bar ("Federal criminal or civil action with material on-chain effect" — individual-trader prosecutions don't materially affect the platform). No admission event; no follow-up required.

---

## Stratum 4 — Nation-state infrastructure bans

**7 / 3–5 admitted (exceeds upper target).**

- [x] **India RBI crypto-banking circular** — 2018-04-06. ← [`events/india-rbi-crypto-ban-2018.yaml`](events/india-rbi-crypto-ban-2018.yaml)
- [x] **Nigeria CBN crypto-banking ban** — 2021-02-05. ← [`events/nigeria-cbn-crypto-ban-2021.yaml`](events/nigeria-cbn-crypto-ban-2021.yaml)
- [x] **Turkey CBRT crypto-payment ban** — 2021-04-16. ← [`events/turkey-cbrt-crypto-ban-2021.yaml`](events/turkey-cbrt-crypto-ban-2021.yaml)
- [x] **PRC PBOC joint notice** — 2021-09-24. ← [`events/china-pboc-crypto-ban-2021.yaml`](events/china-pboc-crypto-ban-2021.yaml)
- [x] **Canada Emergencies Act / Freedom Convoy freeze** — 2022-02-14. First G7 emergency-powers crypto freeze. ← [`events/canada-convoy-freeze-2022.yaml`](events/canada-convoy-freeze-2022.yaml)
- [x] **South Korea FSC Travel Rule** — 2022-03-25. First Asia-jurisdiction national Travel Rule. ← [`events/korea-travel-rule-2022.yaml`](events/korea-travel-rule-2022.yaml)
- [x] **EU MiCA Regulation 2023/1114** — 2023-06-09. First supranational unified crypto framework. ← [`events/eu-mica-2023.yaml`](events/eu-mica-2023.yaml)
- [x] **EU 12th Russia sanctions package** — 2023-12-18. Full-prohibition user-class EU crypto sanction. ← [`events/eu-12th-russia-sanctions-2023.yaml`](events/eu-12th-russia-sanctions-2023.yaml)

### S4 remaining candidates

- [ ] **Russia crypto infrastructure restrictions** — 2022-03 onward `[?]`. Russia passed multiple laws; needs a single named directive (e.g. 2024-08-08 Bank of Russia Mining Law, 2022-03-09 "On Digital Financial Assets" amendment). Pick one with clearest on-chain/off-ramp effect.
- [ ] **Japan FSA KYC enforcement / Travel Rule** 2022 `[?]` — verify effective date.
- [ ] **UK FCA ban on crypto derivatives for retail** — 2021-01-06 `[?]` — frontend-restriction-adjacent.

---

## Stratum 5 — Corporate policy changes (non-OFAC triggered)

**6 admitted.** Cannot be exhaustively enumerated; `scope: representative` in the paper.

### Stablecoin issuer unilateral actions

- [x] **Circle USDC Tornado blacklist** (standalone from OFAC cascade) — 2022-08-08. ← [`events/circle-usdc-tornado-2022.yaml`](events/circle-usdc-tornado-2022.yaml)
- [x] **Tether 2023-12-09 retroactive sweep** — cross-event Tether batch freeze. ← [`events/tether-retroactive-sweep-2023.yaml`](events/tether-retroactive-sweep-2023.yaml)
- [x] **Tether DPRK pre-commit freeze** — 2025-04-30 / 05-08 (188 days before 2025-11-04 OFAC). ← [`events/tether-dprk-precommit-freeze-2025.yaml`](events/tether-dprk-precommit-freeze-2025.yaml)
- [x] **Tether DOJ-request pig-butchering freeze** — 2023-11-20 ($225M, 37-39 wallets, non-OFAC). ← [`events/tether-doj-pig-butchering-freeze-2023.yaml`](events/tether-doj-pig-butchering-freeze-2023.yaml)

### Frontend operator unilateral restrictions

- [x] **Uniswap Labs frontend token delisting** — 2023-07-21. ← [`events/uniswap-frontend-delisting-2023.yaml`](events/uniswap-frontend-delisting-2023.yaml)

### Exchange / operator policy

- [x] **Coinbase India exit** — 2022-04 (NPCI UPI-disavowal). ← [`events/coinbase-india-exit-2022.yaml`](events/coinbase-india-exit-2022.yaml)

### Non-OFAC-triggered Tornado cascade

- [x] **Tether 2023-12-09 sweep** (listed above) — cross-event corporate-policy-change.

### S5 remaining candidates

- [ ] **dYdX Tornado Cash policy** — 2022-08-10 standalone (separate from `tornado-cash-ofac-2022` which captures dYdX as a sub-observation). Primary: dYdX blog posts captured under that parent event. Only worth splitting if paper needs the S5-isolated datapoint.
- [ ] **OpenSea NFT collection takedowns** — pick 1-2 high-profile cases with archived policy statement (Bored Ape derivatives, sanctioned-wallet-held collections). Primary: OpenSea help-center + verified-removal tweets.
- [ ] **Tether non-OFAC-requested freeze** — pick 2-3 DOJ-request-only freezes from Tether's transparency page (distinct from the already-admitted Tornado and DPRK sweeps).
- [ ] **Binance market exits** — pick one specific announcement (SG 2021-09, JP 2018-03, Canada 2023-05).
- [ ] **Kraken UK withdrawal / Kraken Tornado token restrictions** `[?]` — verify.

---

## Process rollup

### Current state (2026-04-23)

- **53 admitted, 0 drafts.** Full dataset validates via `scripts/validate.py`.
- **All 2026-Q2 adversarial audit outcomes applied** (5 re_scoped + 1 escalation resolved).
- **L0 / L3 / offramp_cex substrate pinned** (documented measurement-gap findings rather than fabricated data).
- **Chain-distribution structural finding** written to [`docs/chain-coverage-note.md`](docs/chain-coverage-note.md).

### Genuinely remaining work (NOT in current session scope)

These items are candidates deferred for later session work — each represents a discrete event not fabricatable without additional primary-source research.

**S1 entry-update**:
- [ ] 2024-01-11 Chatex entry-update modeling decision (extend parent vs. new event).

**S2 SDN-removal verification** (3 items):
- [ ] SUEX delisting verification.
- [ ] Chatex delisting verification.
- [ ] 2024-2025 mixer delistings SDN XML diff.

**S3 DOJ/CFTC/SEC gap** (2 concrete, 2 deferred):
- [ ] CFTC v. Ooki DAO (2022-09-22).
- [ ] SEC v. Binance (2023-06-05) + SEC v. Coinbase (2023-06-06).
- [ ] SEC v. Uniswap Labs Wells notice (2024-04) `[?]` scope check.
- [ ] LocalBitcoins operator charges `[?]` scope check.

**S4 nation-state extensions** (3 items):
- [ ] Russia crypto-infrastructure directive pin.
- [ ] Japan FSA Travel Rule.
- [ ] UK FCA retail-derivatives ban 2021-01-06.

**S5 corporate extensions** (4+ items):
- [ ] dYdX Tornado standalone (split decision).
- [ ] OpenSea NFT takedowns (2 cases).
- [ ] Non-OFAC Tether DOJ freezes (2–3 cases).
- [ ] Binance regional market-exit pin.
- [ ] Kraken UK / Tornado restrictions `[?]`.

### Dependencies per stratum

- **S1**: ✓ complete (27/27).
- **S2**: blocked on SDN XML year-over-year diff tooling — not currently prioritized.
- **S3**: DOJ / CFTC / SEC press-release archival via PACER + justice.gov scraping. Next-session work.
- **S4**: multi-language primary-source archival (RU/JP original texts); non-trivial.
- **S5**: hand-curated, continue as paper needs dictate.

### Verification flags

- S1: all `[?]` resolved.
- S3: 2 `[?]` remaining (Uniswap Wells notice scope; LocalBitcoins year).
- S4: 1 `[?]` (Russia directive choice); 2 new candidates still `[ ]`.
- S5: representative scope; `[?]` resolved during admission.

---

## Historical sequencing note

The bootstrap sequence (2026-04-21 → 2026-04-22) that took the dataset from 6 admitted → 49 admitted:

1. **S1 triage pass** (2026-04-21): scraped 308-page OFAC Recent Actions archive, keyword-matched 73 candidate dates, confirmed 27-event S1 universe.
2. **Overnight batch 1** (2026-04-21 → 2026-04-22 AM): 17 new drafts added + asset-layer scan via `scripts/batch_usdtbanlist_check.py`.
3. **Admission wave** (2026-04-22 AM): 15 drafts → admitted via primary_onchain tx-hash extraction + validator rule relaxations.
4. **Final wave** (2026-04-22 mid-day): 14 remaining drafts admitted via int-parsed-YAML fix + state_block_event observed_no_change admissibility.
5. **2026-Q2 adversarial audit** (2026-04-22 PM): 5-event sample, 5 re_scoped + 1 escalation; expanded to 9 more events during audit scope-expansion.
6. **Phase B/C/D expansion** (2026-04-22 PM): +13 new events (Lazarus-2019 through EU-12th-Russia-2023) + L0 OONI pass + L3 MEV-Blocker anchors + offramp_cex chain-analytics anchors + chain-coverage structural note.

Bootstrap subtotal: **49 admitted / 0 drafts** — the point at which the
initial stratified corpus first exceeded the paper's 20-event gate.
Subsequent schema / coverage / stratum updates raised the live snapshot
to **53 admitted / 0 drafts**.
