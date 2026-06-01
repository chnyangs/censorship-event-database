# Source Artifact Manifest

Dataset snapshot: v0.2.0-rc-dryrun-11 · cutoff `2026-06-02` · commit `038e378` · generated `2026-06-02T00:00:00Z`

This manifest lists local source artifacts included in the release reproduction surface and records their SHA-256 hashes. Re-fetchable operator-census repository clones and large upstream dumps excluded by `.gitignore` are intentionally not listed; their retrieval policy is recorded in `sources/external_retrieval_receipts.yaml`.

- Files: 2996
- Total bytes: 355985214

## By Artifact Family

| family | files |
| --- | ---: |
| `README.md` | 1 |
| `archived_htmls` | 2 |
| `asset_layer_scan` | 17 |
| `china_russia_cis_frames` | 2 |
| `corporate_policy` | 2 |
| `defi_wallet_appstore_l3l4` | 2 |
| `external_retrieval_receipts.yaml` | 1 |
| `federal_enforcement` | 2 |
| `historical_baseline_2013_2016` | 2 |
| `http_captures` | 2755 |
| `ingestion_sources.yaml` | 1 |
| `japan_ofac_density_2014_2025` | 2 |
| `l0_datasets` | 24 |
| `l1_datasets` | 3 |
| `non_us_state` | 2 |
| `ofac_sdn_diffs` | 77 |
| `onchain_receipts` | 77 |
| `operator_census` | 1 |
| `operator_commits` | 12 |
| `pre_bitcoin_baseline_2008_2012` | 2 |
| `source_frame_triage` | 7 |
| `supranational` | 2 |

## By Extension

| extension | files |
| --- | ---: |
| `bin` | 88 |
| `csv` | 9 |
| `diff` | 3 |
| `go` | 3 |
| `html` | 1252 |
| `json` | 1621 |
| `md` | 12 |
| `pdf` | 2 |
| `py` | 1 |
| `txt` | 2 |
| `yaml` | 3 |

## Exclusions

- `sources/operator_census/*/` clones are re-fetchable from `sources/operator_census/candidates.yaml` and are not release inputs. `analysis/operator_census/commits.json` is the compact tracked receipt.
- `sources/ofac_sdn_diffs/current/sdn.xml` and `sources/ofac_sdn_diffs/opensanctions/us_ofac_sdn.ftm.json` are large upstream dumps excluded by `.gitignore`.
- `sources/external_retrieval_receipts.yaml` records the retrieval contract for excluded upstream inputs.
- `source_manifest.*` outputs are excluded from their own input set.
