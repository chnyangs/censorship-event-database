# Table 5 · Complete-vs-subset target stratification

Dataset snapshot: **v0.2.0-rc-dryrun-11** · cutoff `2026-06-08` · commit `ee7bf1a` · generated `2026-06-25T23:48:26Z`

Supports `docs/paper_claims.md §4 item 5`. Stratifies events by whether their `target` enumerates the **complete** set of in-scope addresses/entities/domains or only a **subset**. Complete enumeration supports stronger causal statements about the address set; subset enumeration should be cited with that qualifier.

## Summary · enumeration value

| enumeration | count |
| --- | ---: |
| `complete` | 79 |
| `subset` | 319 |
| **total** | **398** |

## enumeration × target.kind

| kind \ enum | complete | subset | total |
| --- | ---: | ---: | ---: |
| `address_set` | 27 | 8 | 35 |
| `asset` | 11 | 8 | 19 |
| `domain` | 1 | 6 | 7 |
| `entity` | 40 | 296 | 336 |
| `protocol` | 0 | 1 | 1 |

## enumeration × archetype

| enum \ archetype | asset_only | frontend_only | cex_only | multi_layer | other_single_layer | null_event | total |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `complete` | 12 | 6 | 41 | 4 | 0 | 16 | 79 |
| `subset` | 9 | 40 | 143 | 25 | 11 | 91 | 319 |

A `subset` row means OFAC/DOJ named specific addresses or entities rather than an entire protocol; downstream layer-change claims must say `observed on the named subset`, not `on the protocol as a whole`.
