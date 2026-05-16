# Table 5 · Complete-vs-subset target stratification

Dataset snapshot: **v0.2.0-rc-dryrun-2** · cutoff `2026-05-16` · commit `c6bc9d9` · generated `2026-05-18T10:40:00Z`

Supports `docs/paper_claims.md §4 item 5`. Stratifies events by whether their `target` enumerates the **complete** set of in-scope addresses/entities/domains or only a **subset**. Complete enumeration supports stronger causal statements about the address set; subset enumeration should be cited with that qualifier.

## Summary · enumeration value

| enumeration | count |
| --- | ---: |
| `complete` | 34 |
| `subset` | 49 |
| **total** | **83** |

## enumeration × target.kind

| kind \ enum | complete | subset | total |
| --- | ---: | ---: | ---: |
| `address_set` | 20 | 3 | 23 |
| `asset` | 0 | 1 | 1 |
| `domain` | 1 | 1 | 2 |
| `entity` | 13 | 44 | 57 |

## enumeration × archetype

| enum \ archetype | asset_only | frontend_only | cex_only | multi_layer | other_single_layer | null_event | total |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `complete` | 8 | 4 | 9 | 4 | 0 | 9 | 34 |
| `subset` | 5 | 8 | 19 | 14 | 0 | 3 | 49 |

A `subset` row means OFAC/DOJ named specific addresses or entities rather than an entire protocol; downstream layer-change claims must say `observed on the named subset`, not `on the protocol as a whole`.
