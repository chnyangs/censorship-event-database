# Null-Case LLM Expert Pre-Audit

Snapshot date: 2026-05-07.

Scope: 13 admitted `null_case` events listed in [`../../human-audit.md`](../../human-audit.md). This is a multi-expert LLM pre-audit, not a human audit.

Commands checked:

```sh
python3 scripts/validate.py events/iran-ransomware-ofac-2018.yaml events/irgc-ransomware-ofac-2022.yaml events/lazarus-entity-ofac-2019.yaml events/lazarus-laundering-ofac-2020.yaml events/lockbit-leader-ofac-2024.yaml events/matveev-ofac-2023.yaml events/pertsev-nl-arrest-2022.yaml events/russian-cybercrime-infra-ofac-2025.yaml events/sec-v-uniswap-wells-notice-2024.yaml events/sichuan-silence-ofac-2024.yaml events/sinbad-ofac-2023.yaml events/storm-semenov-doj-2023.yaml events/zservers-ofac-2025.yaml
```

Result: all 13 returned `[OK]`.

Evidence/provenance expert additionally ran archive validation over the same set and reported all local `body_hash` + `body_path` pairs hash-match. No `query_hash` or `measurement_ids` were found on the null-case no-change observations.

## Consensus Summary

| Category | Count | Events |
| --- | ---: | --- |
| Stronger LLM pre-audit pass | 2 | `iran-ransomware-ofac-2018`, `sinbad-ofac-2023` |
| Needs human attention | 10 | `irgc-ransomware-ofac-2022`, `lazarus-entity-ofac-2019`, `lazarus-laundering-ofac-2020`, `lockbit-leader-ofac-2024`, `matveev-ofac-2023`, `pertsev-nl-arrest-2022`, `russian-cybercrime-infra-ofac-2025`, `sichuan-silence-ofac-2024`, `storm-semenov-doj-2023`, `zservers-ofac-2025` |
| Methods fail-pre-audit / highest risk | 1 | `sec-v-uniswap-wells-notice-2024` |

The distinction is semantic, not mechanical. The validator can confirm local hashes and schema invariants, but it cannot decide whether a legal page plus a scope descriptor is enough evidence for an absence claim across exchange public statements.

## Per-Event Pre-Audit Table

| Event | Methods verdict | Evidence/provenance verdict | Anchor types | LLM consensus action |
| --- | --- | --- | --- | --- |
| `iran-ransomware-ofac-2018` | `pass_pre_audit` | `pass_pre_audit` | Two local Wayback `body_hash+body_path` artifacts | Safe for aggregate/null table as partial L4 frontend null. Human should compare pre/post Enexchanger redirect-shell snapshots before narrative use. |
| `irgc-ransomware-ofac-2022` | `needs_human_attention` | `needs_human_attention` | OFAC RA `body_hash+body_path`; `scope_descriptor` | Treat only as public-disclosure CEX null. Human must inspect Binance/Kraken/Coinbase/Bybit statements for 2022-09-14 to 2022-09-28. |
| `lazarus-entity-ofac-2019` | `needs_human_attention` | `needs_human_attention` | OFAC RA `body_hash+body_path`; `scope_descriptor` | Entity-level designation has no address cohort; use only as entity-level public-disclosure null pending human review. |
| `lazarus-laundering-ofac-2020` | `needs_human_attention` | `needs_human_attention` | OFAC RA `body_hash+body_path`; `scope_descriptor` | Address cohort exists, but CEX absence search is not replayed. Human must inspect public CEX statements for the 20-BTC-address cohort. |
| `lockbit-leader-ofac-2024` | `needs_human_attention` | `needs_human_attention` | OFAC RA `body_hash+body_path`; `scope_descriptor` | Treat only as public-disclosure CEX null. Human must inspect public exchange statements for KHOROSHEV/1 BTC address. |
| `matveev-ofac-2023` | `needs_human_attention` | `needs_human_attention` | OFAC RA `body_hash+body_path`; `scope_descriptor` | Target enumeration is `subset` and asset layer is not measured; human must decide if the off-ramp null denominator remains defensible. |
| `pertsev-nl-arrest-2022` | `needs_human_attention` | `needs_human_attention` | FIOD `body_hash+body_path`; `scope_descriptor` | Confounded by prior Tornado Cash OFAC cascade; human must confirm a Pertsev-individual no-change scope is defensible. |
| `russian-cybercrime-infra-ofac-2025` | `needs_human_attention` | `needs_human_attention` | OFAC RA `body_hash+body_path`; `scope_descriptor` | Treat only as public-disclosure CEX null. Human must inspect public exchange statements for VOLOSOVIK/Yalishanda. |
| `sec-v-uniswap-wells-notice-2024` | `fail_pre_audit` | `needs_human_attention` | Uniswap blog and SEC index `body_hash+body_path`; `scope_descriptor` | Highest risk. Current anchors do not replay `app.uniswap.org` operational uptime across 2024-04-10 to 2025-02-25. Upgrade direct frontend continuity evidence or re-scope before aggregate/null-rate use. |
| `sichuan-silence-ofac-2024` | `needs_human_attention` | `needs_human_attention` | OFAC RA `body_hash+body_path`; `scope_descriptor` | Entity-level target and public-disclosure-only CEX null; human must inspect major-CEX public statements. |
| `sinbad-ofac-2023` | `pass_pre_audit` | `pass_pre_audit` | Two local Wayback `body_hash+body_path` artifacts | Safe for aggregate/null table as L4 frontend null. Human should compare event-day and +10 day snapshots before narrative use. |
| `storm-semenov-doj-2023` | `needs_human_attention` | `needs_human_attention` | DOJ `body_hash+body_path`; `scope_descriptor` | Entangled with same-day Semenov OFAC/Circle cascade. Human must confirm DOJ-indictment-specific no-change scope. |
| `zservers-ofac-2025` | `needs_human_attention` | `needs_human_attention` | OFAC RA `body_hash+body_path`; `scope_descriptor` | Treat only as public-disclosure CEX null. Human must inspect public exchange statements for Zservers/4 BTC addresses. |

## Cross-Cutting Findings

The frontend null cases are stronger because they have direct Wayback artifacts for the frontend surface. Even there, human review should compare the actual snapshots and confirm that "unchanged" is not overstated.

Most off-ramp CEX null cases should be described as "public-disclosure nulls", not as "no exchange action occurred". Private KYT flags, account freezes, SARs, law-enforcement requests, and paid chain-analytics telemetry are outside the current measurement denominator.

`scope_descriptor` is useful for defining the intended search scope, but it is not an independent evidence anchor. A legal trigger page plus a scope descriptor does not replay the absence search across exchange statements.

`analysis/paper_tables/table6_null_denominator.md` correctly reports `body_hash+body_path` anchors for all rows, but the paper text must explain what those anchors prove. For many off-ramp rows, they prove the trigger and scoped public-evidence basis, not a complete exchange-action denominator.

## Recommended Limitation Text

Null-case rows marked `observed_no_change` should be interpreted as scoped public-evidence nulls, not proof that no private compliance action occurred. For off-ramp CEX cases, the denominator is limited to publicly disclosed exchange or corporate statements in the coded window; private KYT flags, account freezes, SARs, law-enforcement requests, and paid chain-analytics telemetry are outside scope. `scope_descriptor` fields define the intended search scope but are not independent evidence anchors. Until Human-Expert-Audit is complete, these null cases support aggregate descriptive tables only and should not be used as named narrative exemplars or as strong claims of no real-world exchange action.

