# Table 5 · Complete-vs-subset target stratification

Dataset snapshot: **v0.2.0-rc-dryrun-11** · cutoff `2026-05-17` · commit `35cd33f` · generated `2026-05-25T00:00:00Z`

Supports `docs/paper_claims.md §4 item 5`. Stratifies events by whether their `target` enumerates the **complete** set of in-scope addresses/entities/domains or only a **subset**. Complete enumeration supports stronger causal statements about the address set; subset enumeration should be cited with that qualifier.

## Summary · enumeration value

| enumeration | count |
| --- | ---: |
| `complete` | 38 |
| `subset` | 67 |
| **total** | **105** |

## enumeration × target.kind

| kind \ enum | complete | subset | total |
| --- | ---: | ---: | ---: |
| `address_set` | 20 | 4 | 24 |
| `asset` | 0 | 2 | 2 |
| `domain` | 1 | 1 | 2 |
| `entity` | 17 | 60 | 77 |

## enumeration × archetype

| enum \ archetype | asset_only | frontend_only | cex_only | multi_layer | other_single_layer | null_event | total |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `complete` | 8 | 5 | 12 | 4 | 0 | 9 | 38 |
| `subset` | 5 | 9 | 31 | 19 | 0 | 3 | 67 |

A `subset` row means OFAC/DOJ named specific addresses or entities rather than an entire protocol; downstream layer-change claims must say `observed on the named subset`, not `on the protocol as a whole`.
