# Evidence chain — `taiwan-fsc-bitcoin-bank-atm-ban-2014-01`

**Status**: `admitted` · **Stratum**: `S4_nation_state` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-02` · **Source commit**: `c3a88e8` · **Schema**: `0.2.0` · **Event last_verified**: `2026-06-01` · **Tool version**: `0.1.0` · **Generated**: `2026-06-02T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "Taiwan's FSC on 2014-01-06 barred banks and financial institutions from
> accepting or exchanging Bitcoin and from providing Bitcoin-related services
> through bank ATMs. Effect carried at the offramp_cex (payment-rail) layer at
> institution-class level with direct attribution to the official FSC press
> release."

## 1. Trigger

- **Type**: `nation_state_block`
- **Actor**: `TW_FSC`
- **Timestamp**: `2014-01-06 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_government`**
  - URL: <https://www.fsc.gov.tw/en/home.jsp?aplistdn=ou%3Dnews%2Cou%3Dmultisite%2Cou%3Denglish%2Cou%3Dap_root%2Co%3Dfsc%2Cc%3Dtw&dataserno=202011120011&dtable=News&id=54&mcustomize=multimessage_view.jsp&parentpath=0>
  - body_hash: `sha256:fc7886ec985edc6772079f79dc2fc4a8528b4525ba428f44429ce1b6b1fb8d4c`
  - body_path: `sources/http_captures/taiwan-fsc-bitcoin-bank-atm-ban-2014-01/primary-fsc-press-live/www.fsc.gov.tw__en-home.jsp__dbeef62d88.html`
  > Official FSC English press release dated 2014-01-06, "Financial
> Institutions' ATMs may not Provide Related Services for Bitcoin."
> The FSC states that Bitcoin is not currency but a virtual asset, cannot
> be used as a commonly accepted payment tool, and therefore banks and
> other financial institutions may not accept or exchange Bitcoin or
> provide related services for Bitcoin through bank ATMs. Captured with
> certificate verification disabled because the local TLS validator failed
> on the FSC certificate chain; the body is pinned by hash and path.
- **`primary_government`**
  - URL: <https://www.fsc.gov.tw/ch/home.jsp?dataserno=201401060003&dtable=News&id=96&mcustomize=news_view.jsp&parentpath=0%2C2>
  - body_hash: `sha256:8c780a7d93396ee37ef651978bea26cf7058995996264bc0674084743e11e4c1`
  - body_path: `sources/http_captures/taiwan-fsc-bitcoin-bank-atm-ban-2014-01/primary-fsc-press-live/www.fsc.gov.tw__ch-home.jsp__899be8f835.html`
  > Official FSC Chinese press release dated 2014-01-06, "金融機構ATM不得提供比特幣
> 相關服務." The Chinese text states that Bitcoin is a virtual commodity
> rather than currency and that banks and other financial institutions may
> not accept or exchange Bitcoin or provide Bitcoin-related services
> through bank ATMs.
- **`semi_primary_wayback`**
  - URL: <http://www.taipeitimes.com/News/biz/archives/2014/01/07/2003580688>
  - Wayback: <https://web.archive.org/web/20140109163139/http://www.taipeitimes.com/News/biz/archives/2014/01/07/2003580688>
  - body_hash: `sha256:a5fb9b0d0ff23f4f567c245dfa54e12c0917c75388d5a15412753c81034a801d`
  - body_path: `sources/http_captures/taiwan-fsc-bitcoin-bank-atm-ban-2014-01/primary/web.archive.org__web-20140110000000-http-www.taipeitimes.com-News-biz-archives-2014-01-07-2003580688__46d53f886c.html`
  > Taipei Times report "FSC bans banks using bitcoins" (published
> 2014-01-07, reporting the FSC's 2014-01-06 announcement). The
> Financial Supervisory Commission "barred local banks and financial
> institutions from bitcoin conversion or using the virtual currency as
> a payment tool via automated teller machines (ATMs)" and stated that
> "financial institutions may not accept bitcoins or provide conversion
> in an effort to avoid consumer disputes and related trading risks."
> This was issued jointly with the central bank, which ruled bitcoin "a
> virtual commodity, not a currency." The announcement followed
> Robocoin's plan to install bitcoin ATMs in Taiwan; the FSC stated such
> installation would require FSC approval, which would not be given.
> Wayback snapshot 20140109163139 (contemporaneous, ~3 days post-event)
> captured replayable body_hash. Retained as contemporaneous corroboration
> and context for the proposed bitcoin-ATM entry.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: Taiwan banks / financial institutions and bitcoin ATM services (class)
- **Chains**: `bitcoin`

> Canonical target is the class of Taiwan banks and financial institutions
> barred from accepting or exchanging Bitcoin or providing Bitcoin-related
> services through bank ATMs. Class-level target (no enumerated roster of
> banks); enumeration=subset because the FSC press release addresses the
> financial-institution population class rather than a fixed entity list.

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `direct` · Δt = 0h

**Event label**: `fsc_barred_banks_from_bitcoin_conversion_and_atms`

**Timestamp**: `2014-01-06 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_government`**
  - URL: <https://www.fsc.gov.tw/en/home.jsp?aplistdn=ou%3Dnews%2Cou%3Dmultisite%2Cou%3Denglish%2Cou%3Dap_root%2Co%3Dfsc%2Cc%3Dtw&dataserno=202011120011&dtable=News&id=54&mcustomize=multimessage_view.jsp&parentpath=0>
  - body_hash: `sha256:fc7886ec985edc6772079f79dc2fc4a8528b4525ba428f44429ce1b6b1fb8d4c`
  - body_path: `sources/http_captures/taiwan-fsc-bitcoin-bank-atm-ban-2014-01/primary-fsc-press-live/www.fsc.gov.tw__en-home.jsp__dbeef62d88.html`
  > Official FSC English press release. attribution=direct: the FSC itself
> states that banks and other financial institutions may not accept or
> exchange Bitcoin or provide related services for Bitcoin through bank
> ATMs.
- **`primary_government`**
  - URL: <https://www.fsc.gov.tw/ch/home.jsp?dataserno=201401060003&dtable=News&id=96&mcustomize=news_view.jsp&parentpath=0%2C2>
  - body_hash: `sha256:8c780a7d93396ee37ef651978bea26cf7058995996264bc0674084743e11e4c1`
  - body_path: `sources/http_captures/taiwan-fsc-bitcoin-bank-atm-ban-2014-01/primary-fsc-press-live/www.fsc.gov.tw__ch-home.jsp__899be8f835.html`
  > Official FSC Chinese press release carrying the same restriction in
> the original-language government publication.
- **`semi_primary_wayback`**
  - URL: <http://www.taipeitimes.com/News/biz/archives/2014/01/07/2003580688>
  - Wayback: <https://web.archive.org/web/20140109163139/http://www.taipeitimes.com/News/biz/archives/2014/01/07/2003580688>
  - body_hash: `sha256:a5fb9b0d0ff23f4f567c245dfa54e12c0917c75388d5a15412753c81034a801d`
  - body_path: `sources/http_captures/taiwan-fsc-bitcoin-bank-atm-ban-2014-01/primary/web.archive.org__web-20140110000000-http-www.taipeitimes.com-News-biz-archives-2014-01-07-2003580688__46d53f886c.html`
  > Taipei Times 2014-01-07 "FSC bans banks using bitcoins": the FSC
> barred banks/financial institutions from bitcoin conversion or using
> bitcoin as a payment tool via ATMs, and stated "financial
> institutions may not accept bitcoins or provide conversion."
> Retained as contemporaneous corroboration; no longer the load-bearing
> source after the official FSC pages were pinned.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`russia-cbr-bitcoin-information-letter-2014`](./russia-cbr-bitcoin-information-letter-2014.md)
- `jordan-cbj-crypto-banking-ban-2014` (not found; no rendered admitted-chain link)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `c3a88e8`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

