# Audit Resume Note — 2026-05-21

**Clean checkpoint at commit `4adbf6e`.**

## State
- **176 verified / 80 candidate / 6 retracted** (262 events total)
- Audit log: `analysis/audit_log_session_1.jsonl`, last `audit_id` = 382

## Completed batches
| Batch | Stratum | Events | Status |
|-------|---------|--------|--------|
| C-1 | S1 OFAC SDN | 8 | ✓ (7 verified, 1 retracted) |
| C-2 | S3 federal_enforcement | 22 | ✓ (14 verified, 5 retracted) |
| C-3 | S6 supranational | 17 | ✓ (17 verified) |
| C-4 null_event | S4 nation_state | 22 | ✓ (22 verified) |
| C-4 comparison — China cluster | S4 nation_state | 7 | ✓ (7 verified) |

## Remaining work

### C-4 comparison group — 26 events left (per-group review)
**Japan FSA (5):** japan-fsa-binance-warning-2018, japan-fsa-six-exchange-orders-2018-06, japan-fsa-zaif-orders-2018-09, japan-fsa-ftx-japan-suspension-2022-11, japan-fsa-dmm-bitcoin-order-2024-09
**Hong Kong (4):** hongkong-sfc-vatp-licensing-2023-06, hongkong-sfc-jpex-block-2023, hongkong-sfc-bybit-warning-2024, hongkong-hkma-stablecoins-ordinance-2025
**Kazakhstan (2):** kazakhstan-internet-shutdown-mining-2022-01, kazakhstan-digital-assets-law-2023-02
**Iran (2):** iran-cbi-crypto-banking-prohibition-2018, iran-government-mining-electricity-restriction-2021
**Thailand (2):** thailand-bot-bitcoin-prohibition-2013, thailand-sec-binance-bybit-c-and-d-2021
**Others (11):** bitfinex-tether-nyag-2021, korea-fsc-institutional-restriction-2017, singapore-mas-retail-crypto-restriction-2022, uk-fca-crypto-promotion-rule-2023, ukraine-virtual-assets-law-2022-03, india-* , philippines-sec-binance-block-2024, israel-nbctf-hamas-crypto-addresses-2021, russia-mining-regional-ban-2024-12, indonesia-bappebti-illegal-exchange-block-2023, liberty-reserve-costa-rica-license-denial-2011-03, wikileaks-wau-holland-tax-status-challenge-2010-12

### C-5 — S5 corporate (~54 drafts) untouched

## Established audit pipeline (per event)
1. `grep` scan for source URLs + observation structure
2. CDX query Wayback (`curl https://web.archive.org/cdx/search/cdx?url=...` with `id_` suffix for PDFs that return wrapper pages; browser UA for 403 bot-blocks)
3. Capture: `python3 scripts/capture_http_artifact.py --output-dir sources/http_captures/<id>/primary <wayback-url>`
4. Python-script patch: status draft→admitted, origin agent_draft→human_reviewed, version→0.2, last_verified→date, evidence_use contextual_unarchived→replayable + body_hash + body_path, coverage status→measured, prepend PROMOTED note to analysis_notes
5. `python3 scripts/validate.py events/<id>.yaml`
6. Append audit_log row, `bootstrap-legacy` to confirm count

## Key validator rules learned (comparison events)
- `observed_change` + `attribution: direct` requires ≥1 `primary_*` source; semi-primary measurements alone → use `attribution: plausible`
- `asset_onchain` `observed_change`/`observed_no_change` requires a `primary_onchain` source — for policy/framework events with no on-chain tx, **drop the asset_onchain observation + set coverage `not_applicable`**, move the bookkeeping observation to `offramp_cex`
- Admission threshold: 1 primary OR 2 independent semi-primary (`semi_primary_wayback` / `semi_primary_measurement`); `supporting_journalism` alone does not satisfy. Distinct sources need distinct `evidence_group_id` to count as independent.
- `placeholder` is a forbidden release-readiness marker in any note/analysis field (reword); `DRYRUN` is NOT forbidden.
- Wayback memento of a PDF often returns an HTML wrapper page — use the `<timestamp>id_/` raw-resource form to get the actual binary.
- Chinese/foreign gov SPA pages (BCB, BI exibenormativo) capture as empty shells — fall back to legal-DB reproductions (LegisWeb) as `semi_primary_wayback`, or live capture with browser UA.

## To resume
Tell Claude "继续 C-4 comparison" (per-group YES/NO) — start with the Japan FSA cluster.
