PYTHON      ?= python3
EVENTS      ?= events/*.yaml
TIMEOUT     ?= 10
REPRO_SOURCE_DATE_EPOCH ?= $(shell $(PYTHON) scripts/repro_source_date_epoch.py 2>/dev/null)

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
TRIGGER_REGISTRY_DIR ?= analysis/trigger_registry
TEMPORAL_LEDGER_DIR ?= analysis/temporal_ledger
SOURCE_MANIFEST_PREFIX ?= sources/source_manifest

# ---- Framework Layer B (case-based retrieval) inputs ----
# Override when querying: make compare LIKE=sinbad-ofac-2023 TOP=5
LIKE        ?=
TOP         ?= 5
COMPARE_OUT ?= -

.DEFAULT_GOAL := help

.PHONY: help \
    validate schema-check validate-citations validate-archives verify-citations freshness \
    draft-gaps status review staleness dataset ofac-recent-action-candidates trigger-registry temporal-ledger source-manifest census-registry-check \
    ingestion-db ingestion-register-sources ingestion-bootstrap ingestion-status ingestion-report \
    ofac-canary ofac-canary-status review-next review-export review-packets review-triage \
    human-audit-worksheet evidence-repair-plan source-discovery-worklist non-human-todo-list \
    er-training-template audit-archive repair-evidence-anchors \
    event-metrics action-registry layer-observability archetypes coverage-matrix l0-coverage-summary l3-provider-census \
    admission-sensitivity jurisdiction derived \
    audit-worksheets paper-tables paper-macros paper-check paper-release-check paper-regenerate-check test \
    render-site render-evidence render-evidence-all compare \
    ooni-scan l0-query-metadata usdt-scan operator-census capture \
    irr-sample irr-packet irr-open irr-kappa evidence-tier-irr-kappa \
    check check-network check-all \
    regenerate clean

help:
	@printf '%s\n' \
	    '### Validation' \
	    'make validate              # schema / field consistency checks for $(EVENTS)' \
	    'make schema-check          # JSON Schema validation for $(EVENTS)' \
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
	    'make ofac-recent-action-candidates # materialize OFAC backfill stubs from cached triage' \
	    'make trigger-registry      # pre-admission trigger registry + sampling-frame gaps' \
	    'make temporal-ledger       # 2008+ monthly source-frame discovery ledger' \
	    'make source-manifest       # hash manifest for local source artifacts under sources/' \
	    'make census-registry-check # fail-closed census-gap registry/docs reconciliation check' \
	    'make ingestion-db          # initialize local v0.3 ingestion SQLite state under .local/' \
	    'make ingestion-register-sources # register v0.3 ingestion source registry without marking fetch success' \
	    'make ingestion-bootstrap   # bootstrap events/*.yaml into local v0.3 SQLite state' \
	    'make ingestion-status      # print local v0.3 ingestion status JSON' \
	    'make ingestion-report      # write v0.3 operating report under analysis/ingestion_reports/' \
	    'make ofac-canary           # run OFAC SDN canary against local/fetched XML into review queue' \
	    'make ofac-canary-status    # print OFAC canary 7-day clean-run gate status' \
	    'make review-next           # print the next v0.3 review queue item as JSON' \
	    'make review-export         # export v0.3 review queue JSON/CSV/MD under analysis/review_queue/' \
	    'make review-packets        # write per-item human review packets under analysis/review_queue/packets/' \
	    'make review-triage         # write pre-human LLM/machine triage summary + worklists' \
	    'make human-audit-worksheet # write blank worksheet + decision templates for pending human audit' \
	    'make evidence-repair-plan  # write repair plan for LLM/machine flagged rows' \
	    'make repair-evidence-anchors # capture missing body_hash/body_path anchors from repair plan' \
	    'make source-discovery-worklist # write source-discovery worklist for remaining machine blockers' \
	    'make non-human-todo-list # write non-human task status list; excludes real human audit' \
	    'make er-training-template  # write blank ER training-set worksheet template' \
	    'make audit-archive         # archive hot audit_log rows older than 90 days' \
	    '' \
	    '### Derived research layer (→ $(DERIVED_DIR)/)' \
	    'make event-metrics         # per-event metrics panel (cascade breadth/speed/source strength)' \
	    'make action-registry       # corpus-level physical-action dedupe registry' \
	    'make layer-observability   # coverage-aware per-layer observability table (denominator-honest)' \
	    'make archetypes            # rule-based archetype classifier + archetype_distribution.md' \
	    'make coverage-matrix       # explicit event×layer denominator eligibility surface' \
	    'make l0-coverage-summary   # denominator-aware OONI query summary for L0 artifacts' \
	    'make l3-provider-census    # L3 provider/event denominator census; no v0.1 rate' \
	    'make admission-sensitivity # strict/current/permissive admission-rubric ablation' \
	    'make jurisdiction          # jurisdictional composition of the admitted corpus (Table 7)' \
	    'make derived               # all derived research artifacts in one shot' \
	    'make audit-worksheets      # per-event audit worksheets (default: anchor cases)' \
	    'make paper-tables          # reproducible paper tables → analysis/paper_tables/' \
	    'make paper-macros          # reproducible LaTeX paper-number macros → paper_numbers.tex' \
	    'make paper-check           # non-mutating paper-facing claim/table/audit-coherence checks' \
	    'make paper-release-check   # strict submission/release paper gate' \
	    'make paper-regenerate-check # rebuild paper dependencies, then run paper-check' \
	    'make test                  # pytest regression suite for classifier + numerator rules' \
	    '' \
	    '### Static site + framework outputs' \
	    'make render-site           # render events/*.yaml → $(SITE_DIR)/' \
	    'make render-evidence-all   # framework A: render admitted evidence chains → $(EVIDENCE_DIR)/' \
	    'make render-evidence SLUG=<slug>   # framework A: render a single event to stdout' \
	    'make compare LIKE=<slug> TOP=5     # framework B: find top-N comparable cases' \
	    '                                   # (or: make compare TRIGGER_TYPE=... ACTOR=...)' \
	    '' \
	    '### Data collection (targeted)' \
	    'make ooni-scan             # OONI Explorer batch query for L0 substrate' \
	    'make l0-query-metadata     # backfill query-cell metadata into legacy OONI artifacts' \
	    'make usdt-scan             # usdtbanlist.com batch scan across all events' \
	    'make operator-census       # multi-repo git-history scan of operator compliance' \
	    'make irr-sample            # stratified blind sample for inter-rater reliability' \
	    'make irr-packet            # blank independent-human IRR packet under site/h1_irr_packet/' \
	    'make irr-open              # build + open the IRR packet HTML page (macOS)' \
	    'make irr-kappa             # compute Cohen'"'"'s κ on filled-in blind worksheets' \
	    'make evidence-tier-irr-kappa # compute codebook-4.0 evidence_tier κ after human coding' \
	    'make capture URL=<url> OUT=<dir>   # capture a single URL with body_hash' \
	    '' \
	    '### Omnibus' \
	    'make check                 # test + validate + reports + paper-readiness gate' \
	    'make check-network         # verify-citations + freshness' \
	    'make check-all             # check + check-network' \
	    'make regenerate            # dataset + derived + paper tables + site/evidence outputs' \
	    'make clean                 # remove untracked generated site artifacts'

# ---- Validation targets ----
validate:
	$(PYTHON) scripts/validate.py $(EVENTS)

schema-check:
	$(PYTHON) scripts/validate_json_schema.py $(EVENTS)

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

ofac-recent-action-candidates:
	$(PYTHON) scripts/materialize_ofac_recent_action_candidates.py

trigger-registry: dataset
	$(PYTHON) scripts/build_trigger_registry.py --out-dir $(TRIGGER_REGISTRY_DIR)

temporal-ledger: dataset
	$(PYTHON) scripts/build_temporal_discovery_ledger.py --out-dir $(TEMPORAL_LEDGER_DIR)

source-manifest: dataset
	$(PYTHON) scripts/build_source_manifest.py --out-prefix $(SOURCE_MANIFEST_PREFIX)

census-registry-check:
	$(PYTHON) scripts/check_census_gap_registry.py

ingestion-db:
	$(PYTHON) scripts/ingestion_v03.py init-db

ingestion-register-sources:
	$(PYTHON) scripts/ingestion_v03.py register-sources

ingestion-bootstrap:
	$(PYTHON) scripts/ingestion_v03.py bootstrap-legacy $(if $(ENQUEUE),--enqueue-reextraction)

ingestion-status:
	$(PYTHON) scripts/ingestion_v03.py status-report

ingestion-report:
	$(PYTHON) scripts/ingestion_v03.py ingestion-report

ofac-canary:
	$(PYTHON) scripts/ingestion_v03.py ofac-canary $(if $(CURRENT_XML),--current-xml $(CURRENT_XML)) $(if $(PREVIOUS_XML),--previous-xml $(PREVIOUS_XML))

ofac-canary-status:
	$(PYTHON) scripts/ingestion_v03.py ofac-canary-status

review-next:
	$(PYTHON) scripts/review_queue.py --next

review-export:
	$(PYTHON) scripts/ingestion_v03.py export-review-queue

review-packets:
	$(PYTHON) scripts/ingestion_v03.py review-packets $(if $(LIMIT),--limit $(LIMIT))

review-triage:
	$(PYTHON) scripts/ingestion_v03.py review-triage-summary

human-audit-worksheet:
	$(PYTHON) scripts/ingestion_v03.py human-audit-worksheet

evidence-repair-plan:
	$(PYTHON) scripts/ingestion_v03.py evidence-repair-plan

repair-evidence-anchors:
	$(PYTHON) scripts/repair_evidence_anchors.py $(if $(PRIORITY_MAX),--priority-max $(PRIORITY_MAX)) $(if $(LIMIT),--limit $(LIMIT)) $(if $(EVENT_ID),--event-id $(EVENT_ID)) $(if $(DRY_RUN),--dry-run)

source-discovery-worklist:
	$(PYTHON) scripts/ingestion_v03.py source-discovery-worklist

non-human-todo-list:
	$(PYTHON) scripts/ingestion_v03.py non-human-todo-list

er-training-template:
	$(PYTHON) scripts/ingestion_v03.py er-training-template

audit-archive:
	$(PYTHON) scripts/ingestion_v03.py archive-audit-log

l3-provider-census:
	$(PYTHON) scripts/build_l3_provider_census.py --out-dir $(DERIVED_DIR)

event-metrics:
	$(PYTHON) scripts/build_event_metrics.py --out-dir $(DERIVED_DIR)

action-registry:
	$(PYTHON) scripts/build_action_registry.py --out-dir $(DERIVED_DIR)

layer-observability:
	$(PYTHON) scripts/build_layer_observability.py --out-dir $(DERIVED_DIR)

archetypes:
	$(PYTHON) scripts/assign_archetypes.py --out-dir $(DERIVED_DIR)

coverage-matrix: dataset
	$(PYTHON) scripts/build_coverage_matrix.py --out-dir $(DERIVED_DIR)

l0-coverage-summary:
	$(PYTHON) scripts/build_l0_coverage_summary.py --out-dir $(DERIVED_DIR)

# Admission-protocol sensitivity ablation: recomputes the per-layer
# change rate under strict/current/permissive admission rubrics and
# labels each as robust/moderate/sensitive (see
# derived/admission_sensitivity.md). Reviewer-facing answer to
# "can partially_measured loosening inflate the rate?".
admission-sensitivity:
	$(PYTHON) scripts/build_admission_sensitivity.py --out-dir $(DERIVED_DIR)

# Jurisdictional composition of the admitted corpus (Table 7). The
# US-trigger share + non-US split is the honest sampling-frame
# statement reviewers asked for; the paper's abstract and §1 must
# cite this table when framing the corpus.
jurisdiction:
	$(PYTHON) scripts/build_jurisdiction_distribution.py --out-dir $(DERIVED_DIR)

# Per-event audit worksheets for human sign-off (default: anchor cases).
# Usage:
#   make audit-worksheets                 # all anchor_case events
#   make audit-worksheets SLUG=<slug>     # single event
#   make audit-worksheets TIERS=anchor_case,null_case
audit-worksheets:
	$(PYTHON) scripts/build_audit_worksheet.py \
	    $(if $(SLUG),--slug $(SLUG)) \
	    $(if $(TIERS),--tiers $(TIERS))

# Reproducible paper-table surface (see docs/paper_claims.md §4).
# Rebuilds the full derived layer first so Tables 1-6 cannot silently
# consume stale metrics/archetypes after an event-YAML edit. Every
# number in the paper must come from this artifact at a given
# source_commit.
ifndef SOURCE_DATE_EPOCH
paper-tables paper-macros paper-check paper-release-check paper-regenerate-check source-manifest temporal-ledger: export SOURCE_DATE_EPOCH := $(REPRO_SOURCE_DATE_EPOCH)
endif
paper-tables: derived
	$(PYTHON) scripts/build_paper_tables.py

paper-macros: derived
	$(PYTHON) scripts/build_paper_macros.py

paper-check: paper-tables paper-macros
	$(PYTHON) scripts/check_paper_readiness.py

paper-release-check: paper-tables paper-macros
	$(PYTHON) scripts/check_paper_readiness.py --strict-audit --strict-null-audit --strict-repro --strict-reliability

paper-regenerate-check: trigger-registry temporal-ledger source-manifest paper-tables paper-macros paper-check

# Pytest suite for classifier / coverage-numerator / recovery-filter /
# paper-table fail-closed invariants (install with `pip install -r
# requirements-dev.txt`). Locks the fixes from the 2026-04-23 and
# 2026-04-24 review findings so a silent regression cannot re-enter.
test:
	$(PYTHON) -m pytest tests/ -v

# Umbrella target: rebuild every derived artifact (dataset.meta.json must
# land first so downstream scripts read the latest version/cutoff).
ifndef SOURCE_DATE_EPOCH
derived coverage-matrix trigger-registry temporal-ledger: export SOURCE_DATE_EPOCH := $(REPRO_SOURCE_DATE_EPOCH)
endif
derived: dataset event-metrics action-registry layer-observability archetypes coverage-matrix l0-coverage-summary l3-provider-census admission-sensitivity jurisdiction
	@echo "[derived] all derived artifacts rebuilt under $(DERIVED_DIR)/"

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

l0-query-metadata:
	$(PYTHON) scripts/backfill_l0_query_metadata.py

usdt-scan:
	$(PYTHON) scripts/batch_usdtbanlist_check.py

# Multi-repo operator-compliance git-history census (see
# analysis/operator_census/README.md). Clones candidate public
# operator repos to sources/operator_census/ (gitignored) and
# extracts commits touching filter-list substrates.
operator-census:
	$(PYTHON) scripts/scan_operator_census.py

# Inter-rater reliability: stratified blind sampler + Cohen's κ.
# Current output lives under analysis/inter_rater/.
irr-sample:
	$(PYTHON) scripts/build_irr_sample.py

irr-packet:
	$(PYTHON) scripts/build_irr_packet.py

# Build the IRR packet HTML page (render-site emits index.html + assets;
# irr-packet writes the blank worksheet CSVs into the same dir) and open
# it in the default browser (macOS `open`).
irr-open: render-site irr-packet
	open $(SITE_DIR)/h1_irr_packet/index.html

irr-kappa:
	$(PYTHON) scripts/compute_irr_kappa.py

evidence-tier-irr-kappa:
	$(PYTHON) scripts/compute_evidence_tier_irr_kappa.py

# Usage: make capture URL=https://example.com OUT=sources/http_captures/foo/primary
capture:
	@if [ -z "$(URL)" ] || [ -z "$(OUT)" ]; then echo 'error: set URL=<url> OUT=<output-dir>' >&2; exit 1; fi
	mkdir -p $(OUT)
	$(PYTHON) scripts/capture_http_artifact.py --output-dir $(OUT) $(URL)

# ---- Omnibus ----
ifndef SOURCE_DATE_EPOCH
check: export SOURCE_DATE_EPOCH := $(REPRO_SOURCE_DATE_EPOCH)
endif
check: test validate schema-check draft-gaps status review staleness trigger-registry temporal-ledger source-manifest census-registry-check paper-check

check-network: verify-citations freshness

check-all: check check-network

# Full rebuild of all derived artifacts (after an event-YAML change).
# Order matters: dataset.meta.json must land first so downstream
# scripts read the latest version/cutoff. Admission-sensitivity and
# jurisdiction emit derived/ + analysis/paper_tables/ artifacts that
# docs/paper_claims.md cites — they belong in the regenerate chain
# so the reproduction path stays consistent with the paper claims.
ifndef SOURCE_DATE_EPOCH
regenerate: export SOURCE_DATE_EPOCH := $(REPRO_SOURCE_DATE_EPOCH)
endif
regenerate: validate schema-check dataset trigger-registry temporal-ledger source-manifest event-metrics action-registry layer-observability archetypes coverage-matrix \
            admission-sensitivity jurisdiction \
            paper-tables paper-macros status review staleness census-registry-check \
            render-site irr-packet render-evidence-all audit-worksheets paper-check
	@echo "[regenerate] all derived artifacts rebuilt and gated"

clean:
	rm -rf $(SITE_DIR)
	@echo "[clean] removed untracked site/ artifacts; tracked research artifacts are preserved"
