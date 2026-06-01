# Evidence chain — `kucoin-netherlands-exit-2023`

**Status**: `admitted` · **Stratum**: `S5_corporate` · **Shape**: `null_event` (0 changed layer(s): none) · **Tier**: `null_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `ad910b8` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-21` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T00:40:01Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "As of the 2026-05-17 authoring pass, no specific 2023 KuCoin
> Netherlands market-exit action attributable to DNB registration
> requirements could be pinned by the authoring agent. The publicly
> available record brackets the 2023 window with a 2022-12-15 DNB
> warning before and a 2024-09-30 KuCoin NL-user restriction
> announcement (extended to a full 2025-08 NL exit) after, which is
> positive evidence against a clean 2023 NL exit. Slug is retained
> as a documented null_event record for future evidence
> surfacing."

## 1. Trigger

- **Type**: `corporate_policy_change`
- **Actor**: `KUCOIN_EXCHANGE`
- **Timestamp**: `2023-01-01 00:00:00+00:00` (precision: `week`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://www.dnb.nl/en/general-news/news-2022/warning-against-mek-global-limited-doing-business-as-kucoin/>
  - Wayback: <https://web.archive.org/web/2023/https://www.dnb.nl/en/general-news/news-2022/warning-against-mek-global-limited-doing-business-as-kucoin/>
  > De Nederlandsche Bank (DNB) public warning against MEK Global
> Limited d/b/a 'KuCoin' for offering crypto services in the
> Netherlands without the legally required DNB registration.
> Published 2022-12-15 (i.e. PRECEDES the slug's claimed 2023
> exit window). Contextual reference for the regulatory pressure
> backdrop; does NOT by itself document a KuCoin 2023 Netherlands
> market-exit corporate action. evidence_use=contextual_unarchived
> because the authoring agent did not personally pin a Wayback
> snapshot nor compute body_hash.
- **`primary_corporate`**
  - URL: <https://www.kucoin.com/announcement/announcement_for_kucoin_users_in_the_netherlands_240930>
  - Wayback: <https://web.archive.org/web/2023/https://www.kucoin.com/announcement/announcement_for_kucoin_users_in_the_netherlands_240930>
  - body_hash: `sha256:77ccff1f413b36342171d9c1afbf4bb04ef104ece9f7b3545a784affa588bcb8`
  - body_path: `sources/http_captures/kucoin-netherlands-exit-2023/primary/www.kucoin.com__announcement-announcement_for_kucoin_users_in_the_netherlands_240930__a1d0e633e2.html`
  > KuCoin's official announcement for Netherlands users. The
> announcement slug `_240930` indicates an effective date of
> 2024-09-30 (new NL user registrations halted; existing NL users
> without KYC frozen). Subsequent reporting (e.g. KuCoin's
> 2025-07-28 follow-up announcement) extends the wind-down with
> full NL exit effective 2025-08-04 / 2025-08-25. This is
> CONTRARY to the slug's premise of a 2023 exit and is recorded
> here as load-bearing evidence for the null_event disposition.
> Evidence repair 2026-06-01: the KuCoin announcement is locally
> captured with body_hash/body_path, so it is claim-usable for
> the post-window null bracketing claim. It does not establish a
> 2023 KuCoin Netherlands exit.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: KuCoin (MEK Global Limited / Peken Global Limited — NL user cohort, hypothesized)
- **Canonical domains**: `kucoin.com`

> Hypothesized KuCoin Netherlands-resident user cohort. Subset-
> enumerated because the slug postulates the NL retail cohort as the
> target of a 2023 KuCoin corporate-policy exit ostensibly driven by
> DNB registration requirements. The authoring agent could not pin a
> specific 2023 exit-announcement; the closest documented KuCoin NL
> actions are the 2022-12-15 DNB warning (pre-window) and the
> 2024-09-30 NL new-user / KYC freeze announcement followed by the
> 2025-07-28 full NL exit announcement (post-window). Coded as
> null_event per the authoring instruction's null fallback clause.

## 3. Changed-layer observations (supports the scoped claim)

*No observed_change entries. This is a `null_event`; see §4 for observed_no_change evidence supporting the null claim.*

## 4. No-change observations (where applicable)

### offramp_cex — `kucoin_netherlands_exit_2023_unpinned`

**Window**: `2023-01-01 00:00:00+00:00` → `2023-12-31 23:59:59+00:00`

**Sources**:

- **`primary_legal`**
  - URL: <https://www.dnb.nl/en/general-news/news-2022/warning-against-mek-global-limited-doing-business-as-kucoin/>
  - Wayback: <https://web.archive.org/web/2023/https://www.dnb.nl/en/general-news/news-2022/warning-against-mek-global-limited-doing-business-as-kucoin/>
  > De Nederlandsche Bank's 2022-12-15 public warning against
> MEK Global Limited d/b/a 'KuCoin'. Documents the regulatory
> pressure backdrop but predates the slug's 2023 window.
- **`primary_corporate`**
  - URL: <https://www.kucoin.com/announcement/announcement_for_kucoin_users_in_the_netherlands_240930>
  - Wayback: <https://web.archive.org/web/2023/https://www.kucoin.com/announcement/announcement_for_kucoin_users_in_the_netherlands_240930>
  - body_hash: `sha256:77ccff1f413b36342171d9c1afbf4bb04ef104ece9f7b3545a784affa588bcb8`
  - body_path: `sources/http_captures/kucoin-netherlands-exit-2023/primary/www.kucoin.com__announcement-announcement_for_kucoin_users_in_the_netherlands_240930__a1d0e633e2.html`
  > KuCoin's NL-user announcement page (effective 2024-09-30).
> Documents the first published KuCoin NL-restrictive action;
> postdates the slug's 2023 window. Locally captured with
> body_hash/body_path; claim-usable only for the post-window
> observed_no_change/null bracketing claim.

## 5. Honest coverage gaps

- **l4_frontend** (`not_measured`): No geo-gated kucoin.com frontend state diff was captured for the

## 7. Related events

- [`kucoin-canada-exit-2023`](./kucoin-canada-exit-2023.md)
- [`kucoin-doj-2024`](./kucoin-doj-2024.md)
- [`netherlands-dnb-binance-warning-2021`](./netherlands-dnb-binance-warning-2021.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `ad910b8`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

