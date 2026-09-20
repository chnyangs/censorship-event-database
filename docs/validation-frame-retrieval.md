# Source-first OFAC validation frame

Run `python scripts/build_validation_frame.py` to enumerate every action URL in
the official OFAC Recent Actions year filters for 2022–2025. The script does not
filter discovery by crypto terms, addresses, category, or known outcomes. It
retains multiple actions on one day, including URLs with suffixes such as `_33`.
It checks every page's displayed result range and total, then checks unique URLs
and all result positions against the year's official count. A year is labeled
`official_listing_pagination_exhausted` only if those checks agree.

All enumerated pages are fetched to `sources/validation_frame/actions/`. Requests
use three workers by default and globally spaced starts (0.4 seconds), at most two
attempts per URL, timeouts, raw hashes, response metadata and an append-only
retrieval-attempt log. Successful hash-verified caches are resumed without another
request. `--max-action-pages N` permits a deterministic bounded run; unattempted
URLs remain explicitly in the analysis. `--offline` rebuilds only from verified
caches. The script uses Python's standard library and the `pdftotext` executable
for annual-history reconciliation.

The official archive index supplies the four annual SDN-history PDF links. Raw
files and `pdftotext -raw` extracts are retained with hashes. Dated headings are
compared with Recent Actions dates by month. A date missing from the listing is
an unresolved discrepancy, not an inferred absence of a legal action. Annual
history extraction can also miss a heading; these are complementary source
checks, not a proof of world completeness.

`analysis/validation_frame/` contains the listing manifest, year/month checks,
all action pages (including failed or unparsed pages), explicit action-section
headers, and ETH entry proposals. The address extractor requires the explicit
`Digital Currency Address - ETH` marker. It records the nearest parsed explicit
addition/removal/update heading, entry prefix and source line as a **machine
proposal**. Mixed headings remain unclassified. Unmarked address-shaped strings
have a separate queue. Updates may include old and new versions of an entry;
the extractor does not resolve their target identity or determine which address
was newly designated. A page without an ETH marker is not adjudicated out of scope.

These artifacts advance source discovery and preparation for collection. They
are not independent human gold, evidence of operator enforcement, or executed
outcome measurements. Pagination exhaustion means that the retrieved official
listing surface is fully enumerated at its captured version; it does not rule
out unlisted or historically removed pages. All semantic eligibility and target
associations await independent adjudication. Existing event files and earlier
blank/filled review or query templates are never touched.
