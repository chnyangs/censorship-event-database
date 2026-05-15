# Null-case cross-audit · agent A · INDEX

Audit subject: 13 paper-critical `null_case` events listed in `human-audit.md` H2.
Dataset snapshot: v0.1.0 · cutoff 2026-05-06 · source_commit `5b59b99`.
Reference rubric: `scripts/build_audit_worksheet.py`, `analysis/audit_worksheets/{tornado-cash-ofac-2022,cryptex-ofac-2024}.md`.
Cross-reference: `analysis/llm_expert_audit/null_case_pre_audit.md` (independent LLM pre-audit).

This is agent A's independent verdict surface. It does NOT stamp `last_human_audit`. Diff against agent B's INDEX after both are written.

## Verdict counts

| Verdict | Count | Events |
| --- | ---: | --- |
| `pass` | 1 | `sinbad-ofac-2023` |
| `pass_with_concerns` | 9 | `iran-ransomware-ofac-2018`, `irgc-ransomware-ofac-2022`, `lazarus-entity-ofac-2019`, `lazarus-laundering-ofac-2020`, `lockbit-leader-ofac-2024`, `matveev-ofac-2023`, `russian-cybercrime-infra-ofac-2025`, `sichuan-silence-ofac-2024`, `zservers-ofac-2025` |
| `needs_human_review` | 3 | `pertsev-nl-arrest-2022`, `sec-v-uniswap-wells-notice-2024`, `storm-semenov-doj-2023` |
| `fail` | 0 | — |

## Per-event verdict table

| Event ID | agent_verdict | confidence | one-line justification |
| --- | --- | --- | --- |
| `iran-ransomware-ofac-2018` | pass_with_concerns | high | Wayback bracket pair anchors the L4 null; differing digests (host-header variation) want a human eye. |
| `irgc-ransomware-ofac-2022` | pass_with_concerns | medium | `offramp_cex: measured` rests on OFAC RA + scope_descriptor only; concrete 6-BTC cohort exists. |
| `lazarus-entity-ofac-2019` | pass_with_concerns | medium | Entity-only designation with zero on-chain addresses; cohort label is the entity name. |
| `lazarus-laundering-ofac-2020` | pass_with_concerns | medium | Concrete 20-BTC cohort, but absence search not artifact-pinned; stale "null_event rather than null_event" line in `analysis_notes`. |
| `lockbit-leader-ofac-2024` | pass_with_concerns | medium | 1 concrete address; Operation Cronos follow-on context complicates "independent" CEX-cascade reading. |
| `matveev-ofac-2023` | pass_with_concerns | medium | Target enumeration is `subset`; asset_onchain `not_measured`; cohort label is an individual name. |
| `pertsev-nl-arrest-2022` | needs_human_review | medium | Structurally confounded by the 2-days-prior OFAC Tornado Cash cascade; null is hard to separate. |
| `russian-cybercrime-infra-ofac-2025` | pass_with_concerns | medium | 1 concrete BTC address; same OFAC RA + scope_descriptor pattern; recent enough for delayed signals. |
| `sec-v-uniswap-wells-notice-2024` | needs_human_review | high | Wells notice is pre-enforcement; no `app.uniswap.org` uptime artifact across 10½-month window; `scoped_claim` over-attributes. |
| `sichuan-silence-ofac-2024` | pass_with_concerns | medium | Entity-only designation; no enumerated addresses; same systemic pattern. |
| `sinbad-ofac-2023` | pass | high | Two Wayback captures anchor sinbad.io persistence; honest L0 OONI-negative documentation; paper-worthy contrast to Tornado 2022. |
| `storm-semenov-doj-2023` | needs_human_review | medium | Structurally entangled with same-day OFAC Semenov SDN (24h Circle batch-freeze); DOJ-attributable null is conceptually thin. |
| `zservers-ofac-2025` | pass_with_concerns | medium | 4 concrete BTC addresses; same OFAC RA + scope_descriptor pattern; joint US/UK/AU scope. |

## Cross-cutting agent A observations

1. **Systemic off-ramp CEX `measured`-without-search-artifact pattern**: 8 of the 13 events code `offramp_cex: measured` while the only observation anchor is the OFAC trigger page + `scope_descriptor`. Per `null_case_pre_audit.md`, `scope_descriptor` is not an independent evidence anchor for absence claims. Either an aggregator/news-search artifact is pinned per event, or a corpus-wide downgrade to `partially_measured` is applied, or the limitation text in the paper explicitly recasts these as "public-disclosure nulls". Agent A's pass_with_concerns verdicts on these 8 cases would individually become pass if a consistent corpus convention is applied.
2. **Cohort-as-name vs cohort-as-address-set**: 4 events (`lazarus-entity-ofac-2019`, `matveev-ofac-2023`, `sichuan-silence-ofac-2024`, and arguably the entity-side of `storm-semenov-doj-2023`) carry `addresses_cohort` labels that are entity/individual names rather than enumerated addresses. The absence search reduces to entity-name-mention, which is conceptually thinner than address-cohort search.
3. **Frontend null anchors are the gold standard**: `iran-ransomware-ofac-2018` and `sinbad-ofac-2023` both use Wayback bracket pairs. These are the strongest nulls in the set. Any event whose null claim can be re-anchored to direct frontend captures (the obvious candidate: `sec-v-uniswap-wells-notice-2024` for `app.uniswap.org`) should be upgraded that way before paper use.
4. **Trigger-window confounding**: 2 events (`pertsev-nl-arrest-2022`, `storm-semenov-doj-2023`) have null windows that overlap with same-day or 2-day-prior major OFAC cascades; the "no incremental cascade attributable to *this* trigger" framing is honest but hard to falsify.
5. **`sec-v-uniswap-wells-notice-2024` is the standout**: pre-enforcement procedural trigger + missing uptime evidence + causal-overclaim in `scoped_claim`. This case is the only one where agent A would specifically recommend either downgrade out of `null_case` or substantive evidence upgrade *before* sign-off.

## Methodology notes

- Each per-event report was produced from the YAML alone plus the LLM pre-audit triage in `analysis/llm_expert_audit/null_case_pre_audit.md`. Agent A did not re-open the local body_path artifacts beyond verifying their existence; that read-the-passage step is part of human sign-off.
- Verdict mapping: `pass` = ready for human sign-off as-is; `pass_with_concerns` = the case can pass after the human resolves the flagged issue (often a corpus-wide convention question); `needs_human_review` = structural or evidence problem that the human must actively adjudicate before sign-off; `fail` = the case should not be admitted as currently written. No event in the 13 lands at `fail` because no event is dishonest about its own evidence — the concerns are about whether the evidence is sufficient for the claimed coverage status.
