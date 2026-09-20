# Official public-disclosure collection

Executed 20 September 2026. This is deterministic, source-defined collection with **human adjudication pending**. It measures lexical target naming in public material, not private account restrictions, exchange access, actual enforcement, or causal reactions.

The frozen issuer bundle supplied 18 action URLs and 35 candidate address/action units. All were retained across Coinbase, Kraken and Binance: 54 operator/action windows and 105 target/operator units. Every alias, address and UTC `[d-7,d+31)` window was frozen before the corresponding collection run. The target frame and alias identity remain machine proposals, not human gold.

| Official surface | Retrieved scope | Current result |
| --- | --- | --- |
| [Kraken blog](https://blog.kraken.com/) and its advertised [WordPress REST archive](https://blog.kraken.com/wp-json/) | All 18 date-filtered windows; each fits one page and passes total-item/page reconciliation. 426 buffered article appearances (388 distinct IDs); 399 appearances within the exact windows (370 distinct IDs). | 35 `no_disclosure_found_under_enumerated_archive` target units; no exact frozen alias/address matches. |
| [Coinbase blog](https://www.coinbase.com/blog) and robots-declared sitemap | Blog sitemap has 1,773 entries; 1,772 distinct article URLs pass the frozen path scope. No target alias/address appears in the screened URLs/anchors, so no article bodies were selected. | 35 `gap` target units. Full-text archive coverage is unestablished. |
| [Binance English blog](https://www.binance.com/en/blog), [announcements](https://www.binance.com/en/support/announcement), and robots-declared sitemaps | Separate locale-corrected run reached the English blog sitemap and three English support/announcement sitemaps; 11,105 distinct URLs pass the frozen paths. No URLs/anchors matched the frozen queries; no article bodies were selected. | 35 `gap` target units. Sitemap enumeration is not full-text archive coverage. |

The Kraken result means only that the **currently enumerable public WordPress post HTML**, filtered by its reported `date_gmt` and searched with the frozen lexical dictionary, contains no matches in these windows. It does not establish that no historical disclosure ever existed. Deleted posts, attachments, other official surfaces/languages, rewritten publication metadata, and names not represented by the frozen aliases remain outside this conclusion. Multiple address units and overlapping windows are not independent observations.

The final combined result is zero lexical `disclosure_found`, 35 narrowly scoped archive negatives, and 70 gaps. **Do not recode the 70 gaps as negatives, or any public-disclosure result as a private-account action.** These outcomes remain separate from independent human reference labels.

## Frozen procedure and captures

`protocol_v1/manifest.json` was frozen at **12:59:09 UTC**, before v1 requests. It binds the issuer candidate bundle, collector source, operator panel, exact lexical queries and windows. Matching uses NFKC/case folding and exact word sequences after punctuation normalization; it does not use stemming or inferred synonyms. Person surnames alone are not automatically added. Source website labels can be machine aliases and need identity review.

Kraken's official index capture advertises `/wp-json/`; the retrieved API index documents the public posts route and its date/pagination arguments. Each requested interval adds a one-day retrieval buffer at each side. The collector then applies the exact UTC window using `date_gmt`. `X-WP-Total`, `X-WP-TotalPages`, expected page sizes, unique post IDs, readable public content, and valid publication timestamps must all agree before an archive negative is permitted. Protected/malformed/missing content, request failures, duplicates or unresolved pagination remain gaps/partial coverage. All returned posts, including unmatched posts, remain in the captured responses.

Coinbase/Binance use only official indices and robots-declared sitemap links. `lastmod` is never treated as publication time. Lexical URL screening has low recall for mentions that occur only in article bodies, and opaque article URLs are especially limiting. This procedure intentionally cannot produce a negative from sitemap-only coverage.

The v1 Binance sitemap budget was consumed by locale ordering before reaching the declared `/en/` surfaces. **v1 remains unchanged.** `protocol_v2_binance_locale/` was separately frozen at **13:02:11 UTC**, with the same source targets/windows and a source-structure-only ordering correction: relevant root indices, exact English locale, then other sitemaps. Only Binance was queried again. The combined analysis uses Coinbase/Kraken v1 and Binance v2, without double counting.

Raw requests and responses are in:

- `sources/disclosure_collection/official_archive_v1/`
- `sources/disclosure_collection/binance_locale_v2/`

Across both preserved runs there were **56 direct HTTP attempts: 46 HTTP 200, eight HTTP 202 and two HTTP 429**. HTTP 202 responses were not accepted as complete article/index bodies, and the rate-limited Coinbase request remained a gap. Exact URLs, times, status, response headers and body hashes are retained. All body hashes and frozen protocol hashes were verified; capture times follow their respective freezes.

The predeclared caps are 40 endpoint queries per operator, at most two attempts per endpoint, 12-second timeout, 8 MB response cap, eight sitemap documents and 16 selected article documents per operator, and at most three WordPress pages per window. At most three operators run concurrently. There is **no explicit request-spacing interval** in this version; request starts are bounded by concurrency and query caps. Both versions are intentionally **non-resumable**: preserve an interrupted directory and create a new frozen version and output directory. Existing captures/protocols are never overwritten.

## Outputs and reproduction

`summary.json` and `target_results.json`/`.csv` combine the selected runs. `kraken_window_counts.json` separates buffered retrieval counts from exact-window counts and identifies every in-window post ID. Operator-specific raw result files contain query ledgers, archive/pagination status and capture locations. `artifact_hashes.json` binds all retained disclosure artifacts and final script/tests; hashes establish byte integrity, not source truth or human review.

The final collector includes the v2 ordering change. To reproduce the original protocol exactly, use its immutable source snapshot and a **new** output directory:

```sh
python analysis/disclosure_collection/protocol_v1/collector_source.py run --protocol analysis/disclosure_collection/protocol_v1 --out-dir /tmp/disclosure-v1-rerun
python scripts/collect_public_disclosures.py run --protocol analysis/disclosure_collection/protocol_v2_binance_locale --out-dir /tmp/disclosure-binance-v2-rerun
pytest -q tests/test_collect_public_disclosures.py
```

Re-execution queries today's current public archives; identical historical archive contents are not guaranteed. The 14 synthetic tests cover negative gating, pagination inconsistencies, unreadable/protected posts, publication-window boundaries, undated matches, exact lexical matching, capture hashes, frozen-input integrity, safe output refusal and source-locale ordering. Fixtures are not disclosure evidence.
