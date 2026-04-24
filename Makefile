PYTHON      ?= python3
EVENTS      ?= events/*.yaml
TIMEOUT     ?= 10

# ---- Artifact paths ----
DATASET_JSON    ?= dataset.json
DATASET_CSV     ?= dataset.csv
STATUS_OUT      ?= analysis/pilot-status.json
REVIEW_JSON     ?= analysis/review-report.json
REVIEW_MD       ?= analysis/review-report.md
STALENESS_JSON  ?= analysis/staleness.json
STALENESS_MD    ?= analysis/staleness.md
DATASET_META    ?= dataset.meta.json
DERIVED_DIR     ?= derived
SITE_DIR        ?= site
EVIDENCE_DIR    ?= analysis/evidence-chains

# ---- Framework Layer B (case-based retrieval) inputs ----
# Override when querying: make compare LIKE=sinbad-ofac-2023 TOP=5
LIKE        ?=
TOP         ?= 5
COMPARE_OUT ?= -

.DEFAULT_GOAL := help

.PHONY: help \
    validate validate-citations validate-archives verify-citations freshness \
    draft-gaps status review staleness dataset \
    event-metrics layer-observability archetypes derived \
    audit-worksheets paper-tables paper-check \
    render-site render-evidence render-evidence-all compare \
    ooni-scan usdt-scan capture \
    check check-network check-all \
    regenerate clean

help:
	@printf '%s\n' \
	    '### Validation' \
	    'make validate              # schema / field consistency checks for $(EVENTS)' \
	    'make validate-citations    # validate + lightweight citation reachability' \
	    'make validate-archives     # validate + local body-hash / wayback checks' \
	    'make verify-citations      # citation URL reachability sweep for $(EVENTS)' \
	    'make freshness             # link freshness / 404 sweep for $(EVENTS)' \
	    '' \
	    '### Reports (dataset → analysis/)' \
	    'make draft-gaps            # unresolved draft-gap summary' \
	    'make status                # write $(STATUS_OUT)' \
	    'make review                # write $(REVIEW_JSON) + $(REVIEW_MD)' \
	    'make staleness             # write $(STALENESS_JSON) + $(STALENESS_MD)' \
	    'make dataset               # rebuild $(DATASET_JSON) + $(DATASET_CSV) + $(DATASET_META)' \
	    '' \
	    '### Derived research layer (→ $(DERIVED_DIR)/)' \
	    'make event-metrics         # per-event metrics panel (cascade breadth/speed/source strength)' \
	    'make layer-observability   # coverage-aware per-layer observability table (denominator-honest)' \
	    'make archetypes            # rule-based archetype classifier + archetype_distribution.md' \
	    'make derived               # all three derived artifacts in one shot' \
	    'make audit-worksheets      # per-event audit worksheets (default: anchor cases)' \
	    'make paper-tables          # reproducible paper tables → analysis/paper_tables/' \
	    'make paper-check           # paper-facing claim/table/audit-coherence checks' \
	    '' \
	    '### Static site + framework outputs' \
	    'make render-site           # render events/*.yaml → $(SITE_DIR)/' \
	    'make render-evidence-all   # framework A: render 53 evidence chains → $(EVIDENCE_DIR)/' \
	    'make render-evidence SLUG=<slug>   # framework A: render a single event to stdout' \
	    'make compare LIKE=<slug> TOP=5     # framework B: find top-N comparable cases' \
	    '                                   # (or: make compare TRIGGER_TYPE=... ACTOR=...)' \
	    '' \
	    '### Data collection (targeted)' \
	    'make ooni-scan             # OONI Explorer batch query for L0 substrate' \
	    'make usdt-scan             # usdtbanlist.com batch scan across all events' \
	    'make capture URL=<url> OUT=<dir>   # capture a single URL with body_hash' \
	    '' \
	    '### Omnibus' \
	    'make check                 # validate + reports + paper-readiness gate' \
	    'make check-network         # verify-citations + freshness' \
	    'make check-all             # check + check-network' \
	    'make regenerate            # dataset + derived + paper tables + site/evidence outputs' \
	    'make clean                 # remove generated artifacts (site/, dataset.{json,csv}, evidence-chains/)'

# ---- Validation targets ----
validate:
	$(PYTHON) scripts/validate.py $(EVENTS)

validate-citations:
	$(PYTHON) scripts/validate.py --check-citations --timeout $(TIMEOUT) $(EVENTS)

validate-archives:
	$(PYTHON) scripts/validate.py --check-archives --timeout $(TIMEOUT) $(EVENTS)

verify-citations:
	$(PYTHON) scripts/verify_citations.py --timeout $(TIMEOUT) $(EVENTS)

freshness:
	$(PYTHON) scripts/freshness_check.py --timeout $(TIMEOUT) $(EVENTS)

# ---- Reports ----
draft-gaps:
	$(PYTHON) scripts/draft_gap_report.py $(EVENTS)

status:
	$(PYTHON) scripts/status_report.py --out $(STATUS_OUT)

review:
	$(PYTHON) scripts/review_report.py --json-out $(REVIEW_JSON) --md-out $(REVIEW_MD)

staleness:
	$(PYTHON) scripts/staleness_report.py --json-out $(STALENESS_JSON) --md-out $(STALENESS_MD)

dataset:
	$(PYTHON) scripts/build_dataset.py --json-out $(DATASET_JSON) --csv-out $(DATASET_CSV) --meta-out $(DATASET_META)

event-metrics:
	$(PYTHON) scripts/build_event_metrics.py --out-dir $(DERIVED_DIR)

layer-observability:
	$(PYTHON) scripts/build_layer_observability.py --out-dir $(DERIVED_DIR)

archetypes:
	$(PYTHON) scripts/assign_archetypes.py --out-dir $(DERIVED_DIR)

# Per-event audit worksheets for human sign-off (default: anchor cases).
# Usage:
#   make audit-worksheets                 # all anchor_case events
#   make audit-worksheets SLUG=<slug>     # single event
#   make audit-worksheets TIERS=anchor_case,null_case
audit-worksheets:
	$(PYTHON) scripts/build_audit_worksheet.py \
	    $(if $(SLUG),--slug $(SLUG)) \
	    $(if $(TIERS),--tiers $(TIERS))

# Reproducible paper-table generator (see docs/paper_claims.md §4).
# Requires `make derived` to have been run. Emits 6 tables + a meta.json
# under analysis/paper_tables/; every number in the paper must come from
# this artifact at a given source_commit.
paper-tables:
	$(PYTHON) scripts/build_paper_tables.py

paper-check: derived paper-tables
	$(PYTHON) scripts/check_paper_readiness.py

# Umbrella target: rebuild every derived artifact (dataset.meta.json must
# land first so downstream scripts read the latest version/cutoff).
derived: dataset event-metrics layer-observability archetypes
	@echo "[derived] all three derived artifacts rebuilt under $(DERIVED_DIR)/"

# ---- Static site + framework ----
render-site:
	$(PYTHON) scripts/render_site.py --site-dir $(SITE_DIR)

render-evidence-all:
	$(PYTHON) scripts/render_evidence_chain.py --all --output-dir $(EVIDENCE_DIR)

# Usage: make render-evidence SLUG=tornado-cash-ofac-2022
render-evidence:
	@if [ -z "$(SLUG)" ]; then echo 'error: set SLUG=<event-slug>' >&2; exit 1; fi
	$(PYTHON) scripts/render_evidence_chain.py $(SLUG) --stdout

# Framework B: Comparable-case retrieval.
#   make compare LIKE=sinbad-ofac-2023 TOP=5
#   make compare TRIGGER_TYPE=ofac_sdn_designation ACTOR=US_OFAC STRATUM=S1_ofac_sdn CHAINS=bitcoin,ethereum TOP=5
compare:
	@if [ -n "$(LIKE)" ]; then \
	    $(PYTHON) scripts/find_comparable_cases.py --like $(LIKE) --top $(TOP) --output $(COMPARE_OUT); \
	else \
	    $(PYTHON) scripts/find_comparable_cases.py \
	        $(if $(TRIGGER_TYPE),--trigger-type $(TRIGGER_TYPE)) \
	        $(if $(ACTOR),--actor $(ACTOR)) \
	        $(if $(STRATUM),--stratum $(STRATUM)) \
	        $(if $(SHAPE),--shape $(SHAPE)) \
	        $(if $(CHAINS),--chains $(CHAINS)) \
	        $(if $(TARGET_KIND),--target-kind $(TARGET_KIND)) \
	        $(if $(ACTOR_TYPE),--actor-type $(ACTOR_TYPE)) \
	        $(if $(PROTOCOL),--protocol $(PROTOCOL)) \
	        $(if $(JURISDICTION),--jurisdiction $(JURISDICTION)) \
	        --top $(TOP) --output $(COMPARE_OUT); \
	fi

# ---- Data collection (targeted scripts) ----
ooni-scan:
	$(PYTHON) scripts/ooni_batch_query.py --domains-file scripts/ooni_domains.json

usdt-scan:
	$(PYTHON) scripts/batch_usdtbanlist_check.py

# Usage: make capture URL=https://example.com OUT=sources/http_captures/foo/primary
capture:
	@if [ -z "$(URL)" ] || [ -z "$(OUT)" ]; then echo 'error: set URL=<url> OUT=<output-dir>' >&2; exit 1; fi
	mkdir -p $(OUT)
	$(PYTHON) scripts/capture_http_artifact.py --output-dir $(OUT) $(URL)

# ---- Omnibus ----
check: validate draft-gaps status review paper-check

check-network: verify-citations freshness

check-all: check check-network

# Full rebuild of all derived artifacts (after an event-YAML change)
regenerate: dataset event-metrics layer-observability archetypes paper-tables status review staleness render-site render-evidence-all
	@echo "[regenerate] all derived artifacts rebuilt"

clean:
	rm -rf $(SITE_DIR)
	rm -f $(DATASET_JSON) $(DATASET_CSV) $(DATASET_META)
	rm -rf $(EVIDENCE_DIR) $(DERIVED_DIR)
	@echo "[clean] removed site/, dataset.{json,csv,meta.json}, evidence-chains/, derived/"
