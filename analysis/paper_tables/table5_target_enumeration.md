# Table 5 · Complete-vs-subset target stratification

Dataset snapshot: **v0.1.0** · cutoff `2026-04-22` · commit `b99dfaf` · generated `2026-04-27T11:03:02Z`

Supports `docs/paper_claims.md §4 item 5`. Stratifies events by whether their `target` enumerates the **complete** set of in-scope addresses/entities/domains or only a **subset**. Complete enumeration supports stronger causal statements about the address set; subset enumeration should be cited with that qualifier.

## Summary · enumeration value

| enumeration | count |
| --- | ---: |
| `complete` | 29 |
| `subset` | 22 |
| **total** | **51** |

## enumeration × target.kind

| kind \ enum | complete | subset | total |
| --- | ---: | ---: | ---: |
| `address_set` | 20 | 3 | 23 |
| `domain` | 1 | 0 | 1 |
| `entity` | 8 | 19 | 27 |

## enumeration × archetype

| enum \ archetype | asset_only | frontend_only | cex_only | multi_layer | other_single_layer | null_event | total |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `complete` | 8 | 3 | 4 | 4 | 0 | 10 | 29 |
| `subset` | 5 | 5 | 9 | 0 | 0 | 3 | 22 |

A `subset` row means OFAC/DOJ named specific addresses or entities rather than an entire protocol; downstream layer-change claims must say `observed on the named subset`, not `on the protocol as a whole`.
