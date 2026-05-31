# Evidence chain — `karpeles-arrest-tokyo-mtgox-2015`

**Status**: `admitted` · **Stratum**: `S3_doj_sec_cftc_fiod` · **Shape**: `null_event` (0 changed layer(s): none) · **Tier**: `null_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `af3a9ed` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-20` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "Tokyo MPD arrested Mark Karpelès (former Mt. Gox CEO) on 2015-08-01
> on suspicion of data manipulation (and was later indicted for
> embezzlement and aggravated breach of trust) related to the 2014
> collapse. Cascade impact is observation_kind=observed_no_change +
> attribution=none because Mt. Gox was already in bankruptcy from
> 2014-02-28 — the arrest does not produce observable change at any
> layer beyond the pre-existing freeze. Historical-baseline tier; not
> used in main statistical denominators."

## 1. Trigger

- **Type**: `doj_indictment`
- **Actor**: `JP_TMPD`
- **Timestamp**: `2015-08-01 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`supporting_journalism`**
  - URL: <https://www.reuters.com/article/us-bitcoin-mtgox-arrest-idUSKCN0Q608B20150801>
  - Wayback: <https://web.archive.org/web/20150801120000/https://www.reuters.com/article/us-bitcoin-mtgox-arrest-idUSKCN0Q608B20150801>
  > Reuters 2015-08-01 wire coverage of the Tokyo Metropolitan Police
> Department arrest of Mark Karpelès, former CEO of Mt. Gox K.K., on
> suspicion of accessing the Mt. Gox computer system to manipulate
> account balances (~$1M inflation of his own USD account in
> February 2013). Tokyo MPD press releases are Japanese-language only;
> Reuters used as English-language contemporaneous anchor.
> evidence_use=contextual_unarchived: no body_hash captured into
> sources/http_captures/ in this session.
- **`supporting_journalism`**
  - URL: <https://www.cnn.com/2015/08/01/asia/bitcoin-mt-gox-karpeles-arrested/index.html>
  - Wayback: <https://web.archive.org/web/20150802165843/https://www.cnn.com/2015/08/01/asia/bitcoin-mt-gox-karpeles-arrested/index.html>
  - body_hash: `sha256:da6bce7b2993bb3a9a5ef4dc7494aba67fc67f6c0ee2c902b11b412c2c7f6991`
  - body_path: `sources/http_captures/karpeles-arrest-tokyo-mtgox-2015/primary/web.archive.org__web-20150802165843-https-www.cnn.com-2015-08-01-asia-bitcoin-mt-gox-karpeles-arrested-index.html__aa80abe173.html`
  > CNN 2015-08-01 coverage confirming the arrest date, the Tokyo MPD as
> the arresting authority, and the data-manipulation predicate. Used
> as cross-source corroboration of the Reuters anchor.
> evidence_use=contextual_unarchived: no body_hash captured this
> session.
- **`supporting_journalism`**
  - URL: <https://www.nbcnews.com/news/world/head-failed-japan-based-bitcoin-exchange-mt-gox-arrested-n402391>
  - Wayback: <https://web.archive.org/web/20150802000000/https://www.nbcnews.com/news/world/head-failed-japan-based-bitcoin-exchange-mt-gox-arrested-n402391>
  > NBC News 2015-08-01 coverage. Third-source corroboration of the
> arrest date and Tokyo MPD attribution.
> evidence_use=contextual_unarchived: no body_hash captured this
> session.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: Mark Karpelès (Mt. Gox K.K. former CEO)
- **Chains**: `bitcoin`
- **Canonical domains**: `mtgox.com`

> Mark Karpelès as former CEO of Mt. Gox K.K., charged with data
> manipulation and (in subsequent September 2015 indictment) embezzlement
> and aggravated breach of trust. Mt. Gox itself was already in
> bankruptcy at arrest date — no further on/off-ramp cascade triggered
> by the arrest. Target is a key person, not the exchange itself.

## 3. Changed-layer observations (supports the scoped claim)

*No observed_change entries. This is a `null_event`; see §4 for observed_no_change evidence supporting the null claim.*

## 4. No-change observations (where applicable)

### offramp_cex — `criminal_arrest_of_former_ceo`

**Window**: `2015-08-01 00:00:00+00:00` → `2015-09-30 23:59:59+00:00`

**Sources**:

- **`primary_legal`**
  - URL: <https://www.mtgox.com/img/pdf/20150422_report.pdf>
  - body_hash: `sha256:34043ed3cb1fa7c386366ba4dca8de746d0976dc3f40b1370941e33c0d6ace22`
  - body_path: `sources/http_captures/karpeles-arrest-tokyo-mtgox-2015/v0_3_primary_repair/www.mtgox.com__img-pdf-20150422_report.pdf__35064f7525.bin`
  > Mt. Gox official trustee / bankruptcy-estate PDF, fetched
> from mtgox.com, with PDF metadata indicating April 2015
> creation/modification before the 2015-08-01 Karpelès arrest.
> It provides primary legal-administrative evidence that the
> Mt. Gox estate was already in post-collapse bankruptcy /
> investigation administration before the arrest window. This
> supports the observed_no_change null posture but does not
> independently evidence the Tokyo MPD arrest.
- **`primary_legal`**
  - URL: <https://www.mtgox.com/img/pdf/201504_faq_en.pdf>
  - body_hash: `sha256:670fa6c954b6d3d6bd4d5e9d0d922dbeeeb93c08c896361de056cee13f1814a5`
  - body_path: `sources/http_captures/karpeles-arrest-tokyo-mtgox-2015/v0_3_primary_repair/www.mtgox.com__img-pdf-201504_faq_en.pdf__f1bf78286c.bin`
  > Mt. Gox official English FAQ PDF for the bankruptcy /
> creditor-claims process, fetched from mtgox.com. It anchors
> the pre-existing bankruptcy-administration state that makes
> the 2015 arrest a downstream criminal-enforcement event
> rather than a new exchange-closure cascade. Human audit
> should run OCR / manual review before treating this as
> release-grade primary evidence.
- **`supporting_journalism`**
  - URL: <https://www.reuters.com/article/us-bitcoin-mtgox-arrest-idUSKCN0Q608B20150801>
  - Wayback: <https://web.archive.org/web/20150801120000/https://www.reuters.com/article/us-bitcoin-mtgox-arrest-idUSKCN0Q608B20150801>
  > observation_kind=observed_no_change + attribution=none
> because Mt. Gox is already in bankruptcy (frozen) from
> 2014-02-28; the arrest does not produce a cascading change at
> any layer beyond what mtgox-dhs-dwolla-wells-fargo-seizure-2013
> and the (not-yet-authored) Mt. Gox bankruptcy event already
> cover. evidence_use=contextual_unarchived: no body_hash
> captured this session.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`mtgox-dhs-dwolla-wells-fargo-seizure-2013`](./mtgox-dhs-dwolla-wells-fargo-seizure-2013.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `af3a9ed`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

