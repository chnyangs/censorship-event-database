# Next steps — censorship-event-database

Carried forward from the 2026-05-31 session close (corpus at 368 admitted / 385 total; see
`analysis/STATE_OF_CORPUS_2026_05_31.md`). Ordered by priority. Nothing here is pushed — all work is local.

## P1 — Scope / design decisions (block further authoring; need maintainer's call)
- [ ] **US-state enforcement stratum.** Celsius / BlockFi / Coinbase-state cease-and-desist actions fit
      neither S3 (US *federal*) nor S4 (nation-state). Decide: new `S7_us_state` stratum vs fold into S3.
      Surfaced repeatedly during waves 2–3. Once decided, ~several US-state enforcement events can be authored.
- [ ] **iraq-cbi-cryptocurrency-prohibition-2017-12** — §9 ban-vs-warning ruling. Captured source is the
      genuine Arabic CBI page titled "تحذير / WARNING". If a binding prohibition → admit; if only an advisory →
      §9 context-only (cf. the §9-excluded India-2013 RBI caution). Flag is in the event's analysis_notes.
- [ ] **goldage-ny-state-indictment-2006-07** — pre-2007 boundary. The census starts 2007; decide whether the
      2006 GoldAge NY indictment is in scope (REVIEW-FLAG in the event).

## P2 — Held drafts to finish (mechanical once unblocked)
- [ ] **6 asset_onchain freezes need a `primary_onchain` tx_hash** (§1.6): circle-usdc-multichain-hack,
      circle-usdc-sealed-civil, t3-financial-crime-unit, tether-iran-fury, tether-okx-doj. Pin the on-chain
      `addBlackList`/freeze tx via cloudflare-eth.com RPC, then admit. **ren-protocol stays a terminal draft**
      (off-chain RenVM darknode signature cessation — no tx can exist; it's the §1.6 precedent, leave as-is).
- [ ] **task-force-rusich-ofac-2022-09** — pin a crypto-nexus source. The designation is genuinely crypto
      (OFAC sanctioned 5 addresses: 2 BTC / 2 ETH / 1 USDT-TRON) but captured press release jy0954 has zero
      crypto terms. Capture the OFAC Recent-Actions 20220915 page or a reliable secondary (Chainalysis/TRM),
      then admit. NOT a fabrication.
- [ ] **bitfinex-us-retail-customer-exit-2017-11** — re-capture. Current source is a JS-gated React shell
      (body_hash matches but no article text). Capture a static-HTML mirror or a different outlet's Wayback copy.

## P3 — Methodology debt (codebook process)
- [ ] **`evidence_tier` IRR pass.** Codebook 4.0.0 added a decision-rule (the `attested_secondary` tier). The
      codebook's own "Effective" convention requires a new IRR pass on ≥ 10 events for a decision-rule change.
      Run a 2-coder IRR pass on a 10–15 event sample of the 34 `attested_secondary` rows to confirm inter-rater
      agreement on (a) §9-clarity and (b) the single-source judgment. Record κ. This is outstanding process debt.

## P4 — Census long-tail (ongoing, low-yield-per-event)
- [ ] **`census_gap_candidates.tsv`** has 264 agent-sourced candidate rows; `census_gap_registry.tsv` has 47
      verified+scope-tagged. Continue: verify candidate → dedup against corpus → §9 scope → author as verified
      draft → adversarial verify → admit (or `attested_secondary` if single-source). Heaviest gap remains the
      under-collected 2013–2020 era and non-US/non-English actions.
- [ ] **Task-2 capture route**: opportunistic official-PDF wins as found (central-bank circulars, law texts on
      standard URLs). Skip JS-gated exchange pages + bot-protected gov HTML.

## P5 — Release prep (when ready — maintainer-gated, NEVER auto-push)
- [ ] **`CITATION.cff` `version`** is currently `0.2.0-rc-dryrun-11` (date-released 2026-05-25), now far behind
      the corpus. When the maintainer wants to mint a release: bump `version` (single source of truth for
      `dataset_version`) + `date-released`, then a git tag mints the Zenodo DOI. Do NOT tag/push autonomously.
