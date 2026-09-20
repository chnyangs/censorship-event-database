# Reproducing manuscript artifacts

Install the runtime, test, and analysis dependencies before a full rebuild:

```sh
python3 -m pip install -r requirements-dev.txt -r requirements-analysis.txt
make paper-artifacts
```

`PAPER_DIR` defaults to the existing sibling manuscript checkout
`../6a1d66df502cdc827ad0999d` when it contains `main.tex`. In a standalone
dataset clone, it defaults to `analysis/manuscript`. Override the directory
explicitly for another checkout layout:

```sh
make paper-artifacts PAPER_DIR=/path/to/manuscript
```

`paper-artifacts` generates all three TeX inputs consumed by `main.tex`:
`paper_numbers.tex`, `measurement_audit_numbers.tex`, and
`measurement_progress_numbers.tex`. Validation progress is rebuilt offline
from existing frozen collection artifacts; network collection is not a dependency.
Its JSON and README go to `VALIDATION_PROGRESS_DIR` (default
`analysis/validation_progress`). The macro output defaults to
`$(PAPER_DIR)/measurement_progress_numbers.tex`; override
`VALIDATION_PROGRESS_TEX` to write it elsewhere, including in a standalone clone:

```sh
make validation-progress VALIDATION_PROGRESS_TEX=analysis/validation_progress/measurement_progress_numbers.tex
```

Additional research targets (not automatic dependencies of paper generation):

- `make validation-frame`: fetch official annual OFAC listings, action pages,
  and SDN histories, retaining retrieval failures and machine proposal status.
- `make validation-frame-offline`: recompute the frame from hash-checked captures.
- `make joint-validation`: execute legacy missing-label sensitivity and prepare
  an empty input for later independent-reference comparisons.
- `python scripts/prepare_measurement_panel.py --out-dir NEW_SOURCE_DIR` and
  `python scripts/measurement_pilot.py --panel-manifest NEW_SOURCE_DIR/verified_panel.json
  --out-dir NEW_RUN_DIR`: create an immutable source-verification bundle and run
  an explicitly excluded read-only feasibility pilot. Existing bundles are preserved.

The frozen issuer bundle is checked with `make issuer-candidate-verify`.
A new partial source-defined endpoint snapshot run can be created with
`python scripts/collect_issuer_snapshots.py --out-dir NEW_RUN_DIR`; it verifies
the frozen candidate batch, binds its hashes before requests, and caps query
count. Its output is not a full-window log scan or an independent reference.

Individual manuscript targets:

- `make paper-tables`: rebuild derived inputs and paper tables.
- `make paper-macros`: rebuild derived inputs, run the measurement-semantic
  audit, and write `paper_numbers.tex` and `measurement_audit_numbers.tex` to
  `PAPER_DIR`.
- `make validation-progress`: cross-check source-frame, candidate, endpoint,
  interface, disclosure, and available indexed-log/OONI/cross-transport artifacts;
  write progress JSON/README and `measurement_progress_numbers.tex` in `PAPER_DIR`.
  Its summary schema is `1.1.0`. Missing optional stages remain pending;
  API, JSONL and POST-archive retrieval of the same OONI records are distinct,
  non-additive stages. Collection and human validation remain separate.
  This target performs no network requests.
- `make paper-figures`: rebuild derived inputs and write five PDF figures
  plus their plotted inputs in `PAPER_DIR/figs/figure_inputs.json`.
- `make benchmark`: write `analysis/benchmark/coverage_prediction.txt` from
  current admitted YAML. Override `BENCHMARK_OUT` to choose another file.
- `make validation-cohort-preflight`: inventory cached OFAC frame sources and
  prepare blank cohort work logs; this does not collect outcomes.
- `make measurement-audit`: write the audit under
  `analysis/measurement_audit` and copy its macros into `PAPER_DIR`.

For generators alone, after rebuilding their inputs, output paths can also
be supplied directly:

```sh
python3 scripts/build_paper_macros.py --out /tmp/manuscript/paper_numbers.tex
python3 scripts/build_paper_figures.py --out /tmp/manuscript/figs
```

`make paper-regenerate-check` includes figures and the exploratory benchmark
before the existing readiness checks. `make regenerate` also includes these
artifacts. A successful render or label-prediction run does not establish that
the evidence supports the labels, complete independent human validation, or
satisfy the strict submission gate. Existing semantic check failures remain
failures until the underlying evidence or coding is repaired.

Figure 3 reads strict/current/permissive values from the generated sensitivity
CSV. The blue point and its fraction both use the permissive rubric (measured
plus partially measured); current uses measured rows with direct or plausible
attribution, and strict uses measured rows with direct attribution. L0 and
asset rates remain suppressed. Figures describe provisional corpus coding,
not independently validated enforcement rates. Jurisdiction shares use the
current admitted-event count, with a multi-jurisdiction event counted once
per jurisdiction.

The benchmark predicts existing coverage labels using temporal splits. Its
scores characterize those labels and the collection process; it is not the
independent method-validity experiment for the paper's measurement arm.
