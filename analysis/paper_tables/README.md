# Paper-tables index

Dataset snapshot: **v0.1.0** · cutoff `2026-04-22` · commit `229adc4` · generated `2026-04-24T03:16:25Z`

These tables are the reproducible surface for every number in the paper. Each table links to the specific `docs/paper_claims.md` claim(s) it supports and to the `derived/` artifact it reads from. Re-run with `make paper-tables` from a clean checkout; the output under this directory should match the paper's figures byte-for-byte at a given `source_commit`.

Events in snapshot: **53**

| # | table | supports | inputs |
| --- | --- | --- | --- |
| 1 | [table1_case_roles.md](table1_case_roles.md) | `§0 case roles` | `events/*.yaml` + `derived/event_metrics` + `derived/event_archetypes` |
| 2 | [table2_layer_observability.md](table2_layer_observability.md) | `C1` | `derived/layer_observability` |
| 3 | [table3_archetype_stratum.md](table3_archetype_stratum.md) | `C2`, `C5` | `derived/event_archetypes` |
| 4 | [table4_latency_by_precision.md](table4_latency_by_precision.md) | `C3`, `C4` | `events/*.yaml` + `derived/event_metrics` + `derived/event_archetypes` |
| 5 | [table5_target_enumeration.md](table5_target_enumeration.md) | `§4 item 5` | `events/*.yaml` + `derived/event_archetypes` |
| 6 | [table6_null_denominator.md](table6_null_denominator.md) | `C6`, null-event interpretation | `events/*.yaml` + `derived/event_archetypes` |

Claims that are NOT yet backed by a table (because the underlying data is absent or the analysis is out of scope for v0.1) are enumerated in `docs/paper_claims.md §2`.
