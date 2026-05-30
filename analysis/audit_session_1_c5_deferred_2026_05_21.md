# C-5 Deferred Events — need human decision (2026-05-21)

State at handoff: **249 admitted / 7 draft / 6 rejected** (262 total). Audit log `analysis/audit_log_session_1.jsonl` through `audit_id` 455.

C-4 comparison COMPLETE (33/33). C-5 S5 corporate: 47/54 promoted; the 7 below were deferred rather than forced through, because each needs a judgment call (per the standing per-item YES/NO rule). Grouped by issue:

## A. Date conflation (re-date / retract decision — same shape as the indonesia re-date)
1. **huobi-htx-privacy-coin-delisting-2024** — event claims a 2024 HTX privacy-coin delisting, but the only verifiable source is an *aggregate* Kaiko/CryptoSlate 2024 tally; the discrete, well-documented Huobi privacy-coin delisting (Dash/Monero/Zcash/…) was **Sept 2022** (Decrypt/Cointelegraph). "HTX" is the post-2023-09 rebrand, anachronistic for 2022. Options: re-date+rescope to 2022 Huobi, find an HTX-specific 2024 announcement, or retract.
2. **tether-pig-butchering-second-wave-2024** — claims a June 2024 ~$47M USDT freeze, but the captured Chainalysis + Infosecurity sources describe an **Aug 2025** $47M freeze. Re-date to 2025 or find 2024 sources.
3. **tether-tron-philippines-pdea-freeze-2024** — asset_onchain freeze; only source is newsbytes.ph dated **2025-01-29** (vs 2024 claim). Also hits issue B.

## B. asset_onchain null / observed_change needs a `primary_onchain` tx_hash (validator rule holds even for nulls)
4. **circle-usdc-svb-policy-statement-2023** — observed_no_change at asset_onchain (Circle said SVB reserves safe; no freeze). Has circle pressroom body_hash but asset_onchain requires a `primary_onchain` source. Needs a representative USDC tx as anchor, or a layer reclassification.
5. **makerdao-emergency-shutdown-contingency-2022-08** — observed_no_change at asset_onchain (ESM stayed in standby; no global settlement). Same primary_onchain blocker. l1_consensus here means *Ethereum validator* consensus (not Maker's), so that layer is wrong. Needs a representative PSM/DAI tx anchor.
6. **ren-protocol-shutdown-alameda-ftx-2022-12** — observed_change at asset_onchain (RenVM bridge wind-down, renBTC unredeemable). Anchors ready (medium renprotocol primary_corporate `a036aa37`, The Block `87ee31e8`) but asset_onchain needs a `primary_onchain` tx. Either pin a real renBTC redemption-disable/transfer tx, or reclassify the bridge layer (asset_onchain → offramp_cex).

## C. Source-finding (real action, agent URL wrong)
7. **okx-monero-global-delisting-2024** — real OKX privacy-coin delisting (timestamp 2023-12-29). The okx.com/help URL 404s. Find the real OKX announcement or a journalism source, then reclassify coverage_gap → observed_change/plausible (offramp_cex).

## Established C-5 patterns used this session
- Agent-draft source URLs were **partly fabricated** (see [[project_c5_audit_approach]]); real sources found via WebSearch + captured via the Wayback date-prefix form (auto-resolves to closest memento).
- Twitter/X primaries are unarchivable → replaced with 2 semi_primary_wayback journalism; attribution direct→plausible.
- asset_onchain observed_change without a pinnable `primary_onchain` tx → drop asset_onchain → coverage not_applicable, carry the effect at offramp_cex/l4_frontend (binance-busd, paxos-busd).
- Helper `/tmp/c5patch.py` (patch/hp) rewrites observation sources + header + PROMOTED note.
- Forbidden release markers reworded: `placeholder`/`PLACEHOLDER`, `before admission` (DRYRUN is allowed).
