# Review C — Pipeline State (Stub → Event Triage Health)

Snapshot: cutoff `2026-05-16`, dataset `v0.2.0-rc-dryrun`. Sources: `analysis/temporal_ledger/yearly_collection_plan.csv`, `analysis/temporal_ledger/monthly_discovery_ledger.csv`, `candidate_triggers/`, `events/`, `scripts/validate.py`, `scripts/build_audit_worksheet.py`, `docs/process-checklist.md` §1, §4.

## Headline numbers

- Admitted events: 52 · `observation_closed`: 4. (Other `status:` lines in events are `coverage[].status`, not event-level.)
- 57 files in `candidate_triggers/` (excluding `rejected/`): **28 with `registry_status: candidate`** + 29 post-promotion audit shells (`registry_status: promoted_to_event`: 4 `candidate-*` shells matching the 4 `observation_closed` events, plus 25 `ofac-recent-action-*` shells whose ledger rows say "represented by promoted event YAML"). The 28 match the `yearly_collection_plan.csv::candidate_stubs` total: 2013(2)+2014(4)+2015(3)+2016(2)+2020(2)+2021(4)+2022(2)+2023(6)+2024(3).
- 47 `screened_rows` = `candidate_triggers/rejected/*.yaml`, all `registry_status: screened_no_extractor_target` with a `rejection_reason` (OFAC sweep rows with no crypto target).

## 1. Stub aging (Q1)

Git age is unusable: `git status` shows all 28 candidate stubs and the 4 `candidate-*` shells are **untracked working-tree files**; only the 25 OFAC audit shells were committed `2026-05-07` (commit `312d297`). File mtimes are uniformly today.

The only objective age signal is `trigger.timestamp` vs cutoff. 22 of 28 stubs anchor events that occurred ≥ 12 months ago — past the 12-month observation hard cap (`methodology.md` §3.3). So promotion is no longer "waiting for stabilization"; every non-2024 stub is **evidence-collection blocked**.

No stub-retirement policy: `candidate_triggers/README.md` lists accept/reject/defer with no time-out; `process-checklist.md` defines only the `admitted` gate. Recommendation: add `defer_review_after` + quarterly stub sweep mirroring the §6 adversarial audit.

## 2. Stub → event conversion rate (Q2)

From `monthly_discovery_ledger.csv` aggregates: 104 distinct `candidate_ids`, 30 distinct `promoted_event_ids`. After excluding OFAC audit shells that were minted as `promoted_to_event` from the start, the cleaner read is: **30 promoted vs 28 still pending = 51.7 % closed**. That is a 1.07-to-1 ratio of open-to-closed — weak for a frame open-ended since 2008.

## 3. Per-year backlog priority (Q3)

The 14 historical-baseline stubs (2013-2016) are **lower priority** — `temporal_tier: historical_baseline` is excluded from 2017+ comparable denominators (`monthly_discovery_ledger.md` "Contract"). The 14 comparable-tier stubs are the binding constraint on paper claims.

- **2023 (6, all comparable_main)** — paxos-busd, binance-russia-exit, okx-privacy-token-delist, canada-csa-binance, belgium-fsma-binance, india-fiu-offshore. **Highest priority.**
- **2024 (3)** — philippines-sec-binance, kucoin-doj, ofac-recent-action-20240111.
- **2021 (4)** — uk-fca, malaysia-sc, netherlands-dnb, singapore-mas (all S4 vs Binance).
- **2022 (2)** — eu-russia wallet cap + full ban (S6 supranational).
- **2020 (2)** — helix-doj-mixer, bitmex-cftc-doj.

Drain order: 2023 → 2024 → 2021 Binance S4 cluster → 2020 → 2022 S6. Park 2013-2016 unless paper claims explicitly need historical baseline stratification.

## 4. `observation_closed` events (Q4)

Per `process-checklist.md` §1, `observation_closed` is the post-stabilization, pre-admission state (all touched layers stable 14 days, or 12-month hard cap reached). The 4 events — alphabay-hansa-doj-2017, blockfi-sec-lending-2022, kraken-sec-staking-2023, sec-beaxy-platform-shutdown-2023 — are all `origin: agent_draft`, `created_at: 2026-05-16`, with HTTP capture bundles in `sources/http_captures/<slug>/` and full coverage entries. `validate.py` blocks `status: admitted` for `origin: agent_draft`, so the next gate is **human review** against the 10-item checklist in `process-checklist.md` §4, not more evidence collection.

## 5. Screened rows (Q5)

All 47 `candidate_triggers/rejected/*.yaml` are OFAC sweep rows with `registry_status: screened_no_extractor_target`, a `rejection_reason` field, and an `extraction` block recording `triage_status: no_crypto_content`, `total_crypto_addresses: 0`, `entity_keyword_hits: []`, and the cached page title. These are auditable rejections, not tombstones. Leave as-is; they prove selection-frame completeness for the OFAC sweep.

## 6. Top 5 promotion candidates (Q6)

Ranked by **(a)** primary citation quality in stub, **(b)** v0.2 paper-claim leverage (Binance-cluster S4 enforcement comparability; under-represented S5/S6 strata), **(c)** distance from §4 admission gate.

| # | candidate_id | yr | frame | next action |
| --- | --- | --- | --- | --- |
| 1 | `kucoin-doj-2024` | 2024 | S3 fed | Capture KuCoin US off-boarding notice + DOJ indictment PDF; emit `l4_frontend` + `offramp_cex` coverage rows; matches BitMEX/Beaxy template. |
| 2 | `paxos-busd-nydfs-minting-stop-2023` | 2023 | S5 corporate | Pull on-chain BUSD mint-cessation (Etherscan) + Paxos newsroom capture; biggest lift for the structurally thin S5 stratum. |
| 3 | `uk-fca-binance-markets-2021` | 2021 | S4 non-US | Capture FCA consumer warning + Binance UK notice; promote alongside netherlands-dnb and singapore-mas as a coordinated Binance-S4 batch. |
| 4 | `eu-russia-crypto-wallet-cap-2022` | 2022 | S6 supra | Capture EU 5th sanctions package + 1-2 platform implementation notices; S6 currently has only 2 admitted (eu-mica, eu-12th-russia). |
| 5 | `philippines-sec-binance-block-2024` | 2024 | S4 non-US | Capture NTC block order + app-store/web accessibility probe; mirrors india-rbi-crypto-ban-2018. |

All five have replayable primary URLs in stub citations; none has captured artifacts. Est. 1-2 hr per stub for capture + observations + coverage block + `validate.py` pass.

## All 28 stubs — triage table

| candidate_id | year | source_frame | age_days (file/git) | evidence_state | priority | blocking_gate |
| --- | --- | --- | --- | --- | --- | --- |
| sec-shavers-btcst-2013 | 2013 | us_federal_enforcement | 0 / untracked | trigger-only | skip | historical_baseline |
| silk-road-doj-seizure-2013 | 2013 | us_federal_enforcement | 0 / untracked | trigger-only | P2 | historical_baseline |
| sec-voorhees-satoshidice-2014 | 2014 | us_federal_enforcement | 0 / untracked | trigger-only | skip | historical_baseline |
| shrem-faiella-bitcoin-exchange-2014 | 2014 | us_federal_enforcement | 0 / untracked | trigger-only | skip | historical_baseline |
| powell-unlicensed-bitcoin-exchange-2014 | 2014 | us_federal_enforcement | 0 / untracked | trigger-only | skip | historical_baseline |
| sec-burnside-bitcoin-stock-exchange-2014 | 2014 | us_federal_enforcement | 0 / untracked | trigger-only | skip | historical_baseline |
| ripple-fincen-xrp-2015 | 2015 | us_federal_enforcement | 0 / untracked | trigger-only | P2 | historical_baseline |
| coinflip-cftc-derivabit-2015 | 2015 | us_federal_enforcement | 0 / untracked | trigger-only | skip | historical_baseline |
| teraexchange-cftc-bitcoin-swap-2015 | 2015 | us_federal_enforcement | 0 / untracked | trigger-only | skip | historical_baseline |
| bitfinex-cftc-retail-commodity-2016 | 2016 | us_federal_enforcement | 0 / untracked | trigger-only | P2 | historical_baseline |
| coinbase-irs-john-doe-summons-2016 | 2016 | us_federal_enforcement | 0 / untracked | trigger-only | skip | weak legal-order target |
| helix-doj-mixer-2020 | 2020 | us_federal_enforcement | 0 / untracked | trigger-only | P1 | no Wayback capture yet |
| bitmex-cftc-doj-2020 | 2020 | us_federal_enforcement | 0 / untracked | trigger-only | P1 | no user-region restriction evidence |
| uk-fca-binance-markets-2021 | 2021 | non_us_state | 0 / untracked | trigger-only | **P0** | no FCA + Binance UK captures |
| malaysia-sc-binance-disable-2021 | 2021 | non_us_state | 0 / untracked | trigger-only | P1 | no implementation notice |
| netherlands-dnb-binance-warning-2021 | 2021 | non_us_state | 0 / untracked | trigger-only | P1 | event-scoping decision needed |
| singapore-mas-binance-services-2021 | 2021 | non_us_state | 0 / untracked | trigger-only | P1 | MAS source not archived |
| eu-russia-crypto-wallet-cap-2022 | 2022 | supranational | 0 / untracked | trigger-only | **P0** | no platform implementation evidence |
| eu-russia-full-crypto-wallet-ban-2022 | 2022 | supranational | 0 / untracked | trigger-only | P1 | platform-side restrictions not captured |
| paxos-busd-nydfs-minting-stop-2023 | 2023 | corporate_policy | 0 / untracked | trigger-only | **P0** | on-chain mint-cessation evidence |
| binance-russia-exit-commex-2023 | 2023 | corporate_policy | 0 / untracked | trigger-only | P1 | migration/shutdown evidence |
| okx-privacy-token-delist-2024 | 2023 | corporate_policy | 0 / untracked | trigger-only | P1 | pair-removal state + withdrawal evidence |
| canada-csa-binance-withdrawal-2023 | 2023 | non_us_state | 0 / untracked | trigger-only | P1 | Binance Canada withdrawal notice |
| belgium-fsma-binance-cease-2023 | 2023 | non_us_state | 0 / untracked | trigger-only | P1 | FSMA + Binance Belgium captures |
| india-fiu-offshore-vda-block-2023 | 2023 | non_us_state | 0 / untracked | trigger-only | P1 | multi-platform target split |
| philippines-sec-binance-block-2024 | 2024 | non_us_state | 0 / untracked | trigger-only | **P0** | NTC order + web/app accessibility |
| kucoin-doj-2024 | 2024 | us_federal_enforcement | 0 / untracked | trigger-only | **P0** | US off-boarding evidence |
| ofac-recent-action-20240111 | 2024 | ofac_recent_actions | ~9 / committed 2026-05-07 | trigger-only | P1 | per-layer evidence collection |

Legend: P0 = ship in next batch · P1 = follow-on · P2 = baseline-stratum optional · skip = leave unless paper demands.

## Verdict

**Pipeline is backlogging, not flowing.**

- 28 open vs 30 historically closed: half the lifetime triage decisions are unresolved.
- 2023 holds 6 stubs against 14 admitted that year — 43 % open ratio, highest of any comparable year.
- All 28 candidate stubs are **trigger-citation only**, no captured artifacts — stuck at the same mechanical gate (HTTP capture + coverage block + `validate.py`). Tractable, not methodological.
- The 4 `observation_closed` events show the agent-draft workflow works end-to-end; they queue behind one human-review pass.
- Healthy: 47/47 screened rows justified, promoted-shell audit trail intact, `validate.py` blocks agent-draft self-promotion to admitted.
- Unhealthy: no stub-age policy, no quarterly sweep, 28 stubs are **untracked working-tree files** so age is invisible to any reproducibility audit, no retirement rule for historical-baseline stubs the paper won't consume.

Highest-leverage action: commit the 28 stubs (make age measurable), then run a 1-day capture sprint on the five P0s. That would lift admitted from 52 → 57 and clear all 4 `observation_closed` simultaneously.
