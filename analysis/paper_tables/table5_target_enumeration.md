# Table 5 · Complete-vs-subset target stratification

Dataset snapshot: **v0.2.0-rc-dryrun-2** · cutoff `2026-05-16` · commit `f8dc941` · generated `2026-05-16T12:00:00Z`

Supports `docs/paper_claims.md §4 item 5`. Stratifies events by whether their `target` enumerates the **complete** set of in-scope addresses/entities/domains or only a **subset**. Complete enumeration supports stronger causal statements about the address set; subset enumeration should be cited with that qualifier.

## Summary · enumeration value

| enumeration | count |
| --- | ---: |
| `complete` | 30 |
| `subset` | 32 |
| **total** | **62** |

## enumeration × target.kind

| kind \ enum | complete | subset | total |
| --- | ---: | ---: | ---: |
| `address_set` | 20 | 3 | 23 |
| `domain` | 1 | 1 | 2 |
| `entity` | 9 | 28 | 37 |

## enumeration × archetype

| enum \ archetype | asset_only | frontend_only | cex_only | multi_layer | other_single_layer | null_event | total |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `complete` | 8 | 3 | 6 | 4 | 0 | 9 | 30 |
| `subset` | 5 | 8 | 13 | 3 | 0 | 3 | 32 |

A `subset` row means OFAC/DOJ named specific addresses or entities rather than an entire protocol; downstream layer-change claims must say `observed on the named subset`, not `on the protocol as a whole`.
