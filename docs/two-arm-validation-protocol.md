# Two-arm validation protocol

**Status: independent human validation and the main bounded-cohort evaluation
remain pending. Automated frame construction, panel verification and explicitly
excluded feasibility pilots can proceed in parallel.** This is a proposed design,
not a preregistration made before the existing corpus was collected. Freezing a
future execution manifest will record its prospective commitments. The existing
398-event snapshot is not declared a complete frame or human gold.

The two research arms share a database and validation cohort:

- **Arm 1 — domain empirical research:** Which restrictions were mandated,
  announced, implemented, observed, and later reversed, by which actors and on
  which surfaces? What differences in implementation and recovery are supported
  within a specified trigger and operator frame?
- **Arm 2 — measurement-validity research:** Which collection, applicability,
  source-entailment and missingness errors affect those observations, and how
  accurately can an auditable protocol distinguish them?

The coupling question (RQ3) is how correcting measurement errors changes the
domain conclusions: apparent reaction frequencies, cross-layer patterns and
recovery timing. The broad retrospective database supports discovery; the bounded
cohort supports more controlled validation. Neither dataset constitutes an arm on
its own. E1 and E2 below are evidence-production stages that serve both arms.
Neither a passing schema check nor high inter-rater agreement establishes that a
source entails a claim. The released automated screen is only a queue for review.

## E1: retrospective source-entailment and coding audit

### Input, scope and separation

Run `python scripts/audit_measurement_semantics.py`. The script reads raw
`events/*.yaml`, reports all registry statuses separately, and generates a
review item for every admitted event and each of the six layers. It never edits
an event or assigns a human-review stamp. Raw input bytes and procedure version
identify the audit snapshot. This census of records is complete only relative to
that finite input directory, not to crypto restriction events in the world.

Two independent human reviewers receive separate blank worksheets and the same
raw evidence bundles. A coordinator retains `sealed_key.csv`, the original
records and screening queues. The key is plain text: seal it through distribution
and access control, not by assuming its filename hides the answers. Do not share
the key, old annotations, author notes, automated flags, or the other reviewer's
answers until both sheets are locked. Reviewers may identify entities from source
material; blinding hides prior answers, not identities or the corpus's prior
source-selection process. This limitation must accompany any reliability claim.

The worksheets contain trigger date, actor, target identifiers and source retrieval
identifiers. They omit prior coverage, observation, attribution, claim text and
event-YAML links. Each reviewer independently writes the strongest supported
claim; the coordinator compares it with the legacy claim only after blinding ends.
Do not ask an LLM to fill a worksheet labeled as independent-human review. Do not
write an author name or human timestamp on behalf of a reviewer.

### Independent coding rubric

Every response field starts empty. Reviewers supply their own identifier and UTC
completion time. Use these labels and write evidence locators and reasoning:

| Field | Allowed interpretation |
| --- | --- |
| `applicability` | `applicable`, `not_applicable`, `undetermined`. Decide from the target and the layer's capability at the trigger date, without requiring an observed response. |
| `source_entailment` | `supports_restriction`, `supports_reversal`, `supports_scoped_negative`, `context_only`, `inconclusive`, `source_unavailable`. Derive this from the bundle, not the old annotation. |
| `supported_claim` | A bounded factual statement in the reviewer's words; state the actor, surface, window and what is actually established. |
| `supporting_source_and_locator` | URL/body path/hash plus page, paragraph, log, commit or query-result locator. A hash without claim-relevant content is insufficient. |
| `furthest_supported_stage` | `legal_mandate`, `operator_announcement`, `source_code`, `deployment`, `observed_effect`, `no_stage_established`. Choose the furthest stage actually demonstrated; note multiple branches or incomparable stages in uncertainty notes. |
| `measurement_coverage` | `documented_measurement`, `partial_measurement`, `gap`, `not_applicable`. Distinguish a queried empty result from no query and a legal statement from a behavior measurement. |
| `negative_scope` | Named addresses/providers/endpoints, geography and interval; blank when no negative claim is warranted. |
| `negative_query_or_probe_artifact` | Retrievable result bundle and complete query/probe specification supporting a scoped negative. A trigger announcement alone does not establish a later absence. |
| `negative_detection_limits` | What the measurement could miss, query completeness, archive coverage, private screening and interval censoring. |
| `attribution_basis` | Explicit operator statement or other evidence linking action to trigger; otherwise write temporal association or no established link. |

N/A means there is no relevant control surface by construction. Lack of a freeze
transaction, inaccessible website, failed archive retrieval or missing query is
not a reason for N/A. A supported policy mandate is a genuine finding, but cannot
be upgraded to deployed enforcement without further evidence. Removing an unused
blocklist file proves a source-code change; it does not by itself prove restored
access. An absent public announcement does not prove absence of private action.

### Adjudication and reporting

1. Pilot on a separate training set drawn before selecting the evaluated sample;
   discuss the rubric, revise it, then freeze its version. Exclude training items
   from reliability estimates. Record the exact selected IDs and sampling seed.
2. The prepared packet covers every admitted cell. If resources require a sample,
   the coordinator must first publish a sampling manifest with inclusion
   probabilities: stratify by layer, trigger family, evidence stage and negative/
   gap/N/A boundary, with a uniform random component. Do not estimate population
   error rates from only the flagged queue; use design weights for an unequal
   probability sample. No sample size or completed sample is claimed here.
3. Reviewers code independently. Lock both originals before discussion. Preserve
   disagreements and missing answers. A third human adjudicates using source
   evidence; never replace original ratings with adjudicated labels for IRR.
4. Report category counts, confusion matrices, raw agreement and an appropriate
   agreement coefficient per field. Bootstrap by event (all six layers together),
   and by legal episode where multiple targets share an action. Report intervals;
   do not use a single kappa threshold as a proxy for evidence validity.
5. Independently report source-support error categories and scope errors with
   their audited denominators. Compare legacy labels with adjudicated results.
   Export proposed corrections for author review; do not silently rewrite events.
6. Only after the corrections and independent review are complete can a new
   version's descriptive tables or evaluation gold be asserted. Blank sheets,
   automated overlap flags and model agreement do not meet this condition.

## E2: bounded, response-independent validation cohort

### Local preflight now available

Run `python scripts/prepare_validation_cohort.py` to inventory only cached
`sources/ofac_sdn_diffs/recent_actions_cache/YYYYMMDD.html` pages in the proposed
2022–2025 window. Outputs are in `analysis/validation_cohort/`: raw-source page
hashes and dates, candidate address strings, daily/monthly reconciliation ledgers,
a proposed named panel, a blank action/target adjudication worksheet and a
header-only query log. No network or outcome queries run. Changed human worksheets
or logs are preserved; use a new `--out-dir` for another snapshot.

Address-shaped strings are not yet adjudicated Ethereum targets, and regex does
not distinguish designation, removal or repeated contextual mentions. Retain the
`pending_action_target_adjudication` status until a human resolves chain, target
and action. Cached pages are a convenience input, not an exhaustive archive:
uncached days are unassessed; every month's completeness is still unassessed.
Use the ledger to reconcile the full primary-source frame before freezing an
execution manifest. This preparation does not change E2's NOT EXECUTED status.

### Execution dependencies: human review is not a collection barrier

Primary-source retrieval, full listing traversal, source hashing, explicit ETH
field extraction, contract/interface verification, and read-only collection
engineering can proceed without human ratings. Keep machine proposals separate
from adjudicated facts. Technical feasibility pilots are declared and excluded
from the held-out evaluation before their outcomes are inspected.

Main collection may also proceed before human adjudication **once an automated
candidate execution manifest is frozen**: include candidate IDs, raw source hashes,
parser/protocol version, eligibility rules, unresolved candidates, operator panel,
queries, windows and pilot exclusions. Capture responses for that declared frame
without selecting cases by observed response. Record unavailable/unresolved units.
Later frame adjudicators must see trigger evidence without measurement outcomes;
retain both original machine decisions and human revisions. This can produce
unvalidated measurements, not independent reference labels or final error rates.
A complete-frame claim still needs source reconciliation and eligibility review.

Report these statuses separately: source-frame enumeration, collection execution,
independent-reference validation, and publication readiness. A failed endpoint is
a technical gap; pending human review is a validation dependency. Neither should
be used to claim that the other work cannot advance.

### Frozen cohort definition (proposed; not populated)

The validation frame is **all OFAC SDN additions and removals published from
2022-01-01 through 2025-12-31 that explicitly enumerate at least one Ethereum
address**. The frame unit is legal action ID × named target/entity ID × address;
analyses cluster addresses by legal action and also report target-level results.
Re-designations and removals retain distinct action IDs and linked episodes.
Use a manifest of every daily action page and SDN change record in that interval,
including screened-out records and unavailable pages. Two independent extractors
reconcile address and target enumeration against the archived primary records.

Eligibility must not depend on a freeze, provider reaction, press coverage or
whether the address appears in an operator's filter. Retain zero-balance addresses,
events with no reaction, failed queries and operators with no public substrate.
Before collecting outcomes, lock action IDs, target addresses and the panel below
in a versioned execution manifest. Corpus event YAML is a cross-reference, not the
frame enumerator. A missing source period prevents any claim of complete frame
coverage; record it as an unresolved interval rather than silently excluding it.

### Predeclared panel and measurement surfaces

| Surface | Fixed panel | Measured object and applicability |
| --- | --- | --- |
| Issuer control on Ethereum | USDC and USDT canonical Ethereum contracts | Every enumerated Ethereum address is eligible for an issuer-address screening query independently of token balance. Record pre-trigger balance strata separately; identify and verify exact contract/proxy versions and event ABIs in the execution manifest. |
| Public RPC behavior and policy | Flashbots Protect, Infura, Alchemy, QuickNode | Each address × provider. Historical active behavior requires actual event-window probe captures; current probes cannot establish historical behavior. Public documents/code can support only their corresponding stage. Provider not yet operating is structural N/A with dated evidence; inaccessible account or missing archives is a gap. |
| Off-ramp public disclosure | Coinbase, Kraken, Binance | Each target × operator. Search official announcement and policy archives under the fixed procedure below. Outcome is target-naming public disclosure, not whether a private account was frozen. Private account response remains unmeasured absent direct evidence. |
| L0, L1 and frontend | No complete panel in this validation phase | Explicitly outside this bounded cohort's measurement claims. Do not fill these surfaces with zero or infer a six-layer population comparison. An exploratory linked case does not expand the denominator. |

The fixed panel is a designed validation panel, not a representative sample of
providers or issuers. The exact endpoints, domains, contract identities, API
versions, repository refs and operator-existence intervals require verification
before outcome collection. That verification and the execution manifest are
**pending**. It must preserve the named panel: adding/removing an operator after
seeing responses requires a separately labeled protocol amendment and analysis.

### Uniform windows, queries and effort

Use UTC and preserve trigger precision. For a day-precision trigger, the trigger
is an interval covering that day; do not invent an exact hour. Extract the full
window from seven days before the earliest possible trigger time through 30 days
after its latest possible time. Predeclare endpoints at 1, 7, 14 and 30 days, and
report interval-censored latency where dates cannot identify ordering.

For issuer logs, query every declared contract and address across the complete
window, paginate to exhaustion and store block bounds, chain ID, endpoint,
request/response bytes, hashes and completeness checks. Use a second archival
node or independent log index for reconciliation. Record RPC errors and gaps;
empty logs are negative only when the relevant event signatures, proxy history
and full block range were successfully covered. Store blacklist state immediately
before and after the window when historical state is accessible. No transfer or
evasion transaction is required.

For every provider and exchange, enumerate official archive/sitemap entries in
the window, preserving pagination and retrieval failures. Run the same fixed
lexical query set: exact target name, each declared alias from the trigger record,
each designated address, and `OFAC` plus the action date. Store the full query
set/results, search/index version, retrieval date and actual time spent. Use a
fixed maximum of 30 minutes of manual follow-up per action × operator after the
automated queries; unused time is logged. Use at most two retrieval attempts for
each failing endpoint, separated and logged, then mark it unavailable. Do not
spend extra search effort only on promising positive cases. Searches outside this
budget may appear in a separately labeled exploratory appendix, never silently
change the registered primary outcome.

A searched archive supports `no_disclosure_found_under_this_protocol` only over
its enumerated pages, queries and retrieval dates. It does not establish no
historical disclosure anywhere. An incomplete index or snapshot is partial
coverage. A capture of the designation establishes the designation, not a
negative operator response in the following month.

### Outcomes, missingness and estimands

Maintain separate fields for pre-outcome eligibility, execution/completeness of
the measurement, the observed outcome, evidentiary stage, and attribution. Count
an unavailable history as a gap without changing eligibility. Never change the
denominator because an issuer has no matching freeze event. Do not combine
policy announcements, public code, deployment and observed effects into a single
binary enforcement response.

Primary estimands are panel- and window-specific: issuer address-state change
among completely queried eligible address-contract pairs, and target-naming
disclosure found under the fixed search protocol among eligible operator-target
pairs. Report coverage fractions alongside these conditional quantities. All
denominators, failed-query counts, address/target/action weighting choices and
shared legal-action clusters must be visible. Keep additions and removals separate;
allow unchanged preexisting blacklist state. These estimands are neither global
censorship prevalence nor the probability an individual loses platform access.

For Arm 1, report restriction and recovery observations separately for legal
mandates, announcements, source code, deployment and effects; retain unknown
stages. Interpret a deletion in public code only as a code-history observation
unless deployment or effect evidence warrants more. Estimate response and
recovery latency only where both endpoints are measured, using intervals rather
than invented timestamps. Make claims about this panel and cohort, not global
crypto censorship.

For Arm 2, compare legacy coding with this independent cohort only for overlapping units
and matched outcomes; unmatched units are not failures. Evaluate false-negative
and unsupported-positive claims against human adjudicated, directly measured
evidence where available. Compare naive missing-as-zero, legacy coding, and the
separated eligibility/coverage/stage protocol on the same units. Report bounds or
missingness scenarios for unobserved eligible cells rather than assuming missing
at random. Use event/episode-clustered uncertainty and paired comparisons.

For the coupling question RQ3, publish the before/after domain estimates on the
same units, identifying which applicability, negative-evidence and stage
corrections changed each conclusion. Report robust conclusions as well as
conclusions that disappear; the error analysis must not presuppose the domain
answer. Do not present results from E1 flags as if E2 had validated them.

### Completion conditions

The integrated E2 evaluation is complete only when the frozen frame manifest,
panel identity checks, query logs/results, independent ratings and adjudication
are present. Actual collection and feasibility runs must be reported even while
reference validation is pending; they are not yet validated results. A complete
frame claim additionally requires all source periods to be reconciled and all
inclusions/exclusions accounted for. Publication must name any unmet condition.
The automated screen, historical corpus size, or source hashes alone cannot
satisfy the independent-validation requirements.
