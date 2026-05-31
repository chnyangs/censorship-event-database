# Table 5 · Complete-vs-subset target stratification

Dataset snapshot: **v0.2.0-rc-dryrun-11** · cutoff `2026-06-01` · commit `432aaf5` · generated `2026-06-01T00:00:00Z`

Supports `docs/paper_claims.md §4 item 5`. Stratifies events by whether their `target` enumerates the **complete** set of in-scope addresses/entities/domains or only a **subset**. Complete enumeration supports stronger causal statements about the address set; subset enumeration should be cited with that qualifier.

## Summary · enumeration value

| enumeration | count |
| --- | ---: |
| `complete` | 71 |
| `subset` | 297 |
| **total** | **368** |

## enumeration × target.kind

| kind \ enum | complete | subset | total |
| --- | ---: | ---: | ---: |
| `address_set` | 21 | 6 | 27 |
| `asset` | 10 | 7 | 17 |
| `domain` | 1 | 5 | 6 |
| `entity` | 39 | 279 | 318 |

## enumeration × archetype

| enum \ archetype | asset_only | frontend_only | cex_only | multi_layer | other_single_layer | null_event | total |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `complete` | 8 | 8 | 38 | 4 | 0 | 13 | 71 |
| `subset` | 6 | 38 | 131 | 32 | 7 | 83 | 297 |

A `subset` row means OFAC/DOJ named specific addresses or entities rather than an entire protocol; downstream layer-change claims must say `observed on the named subset`, not `on the protocol as a whole`.
