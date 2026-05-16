# Source Artifact Manifest

Dataset snapshot: v0.2.0-rc-dryrun-3 · cutoff `2026-05-16` · commit `bfb1de7` · generated `2026-05-17T00:00:00Z`

This manifest lists local source artifacts included in the release reproduction surface and records their SHA-256 hashes. Re-fetchable operator-census repository clones and large upstream dumps excluded by `.gitignore` are intentionally not listed; their retrieval policy is recorded in `sources/external_retrieval_receipts.yaml`.

- Files: 871
- Total bytes: 52802552

## By Artifact Family

| family | files |
| --- | ---: |
| `README.md` | 1 |
| `archived_htmls` | 2 |
| `asset_layer_scan` | 17 |
| `external_retrieval_receipts.yaml` | 1 |
| `http_captures` | 726 |
| `l0_datasets` | 24 |
| `l1_datasets` | 3 |
| `ofac_sdn_diffs` | 77 |
| `operator_census` | 1 |
| `operator_commits` | 12 |
| `source_frame_triage` | 7 |

## By Extension

| extension | files |
| --- | ---: |
| `bin` | 3 |
| `csv` | 9 |
| `diff` | 3 |
| `go` | 3 |
| `html` | 552 |
| `json` | 293 |
| `md` | 3 |
| `py` | 1 |
| `txt` | 2 |
| `yaml` | 2 |

## Exclusions

- `sources/operator_census/*/` clones are re-fetchable from `sources/operator_census/candidates.yaml` and are not release inputs. `analysis/operator_census/commits.json` is the compact tracked receipt.
- `sources/ofac_sdn_diffs/current/sdn.xml` and `sources/ofac_sdn_diffs/opensanctions/us_ofac_sdn.ftm.json` are large upstream dumps excluded by `.gitignore`.
- `sources/external_retrieval_receipts.yaml` records the retrieval contract for excluded upstream inputs.
- `source_manifest.*` outputs are excluded from their own input set.
