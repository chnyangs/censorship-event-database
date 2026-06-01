# Evidence chain — `switzerland-finma-tezos-zg-2018`

**Status**: `admitted` · **Stratum**: `S4_nation_state` · **Shape**: `null_event` (0 changed layer(s): none) · **Tier**: `null_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-02` · **Source commit**: `c3a88e8` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-21` · **Tool version**: `0.1.0` · **Generated**: `2026-06-02T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> FINMA's 2018-02-16 "Guidelines for enquiries regarding the
> regulatory framework for initial coin offerings (ICOs)"
> established the Swiss-jurisdiction tripartite payment /
> utility / asset token taxonomy that classifies token
> issuances under Swiss financial market law (GwG / Code of
> Obligations / FinSA-precursor frame) and that Swiss-nexus
> 2017-cohort ICO sponsors — most prominently the
> Tezos Foundation (Zug, CH) — must apply retroactively. The
> guidelines are framework predicate guidance, not a per-entity
> enforcement order; observation_kind=observed_no_change with
> attribution=none at the token-classification axis honestly
> represents the dispersed framework predicate role. The
> concurrent Tezos Foundation governance dispute (Gevers vs
> Breitman) is documented in analysis_notes as contextual
> background but is not coded as a censorship-layer
> observation. Comparable-analysis tier; null_case admission
> candidate pending human audit and archival pinning.

## 1. Trigger

- **Type**: `regulatory_enforcement`
- **Actor**: `CH_FINMA`
- **Timestamp**: `2018-02-16 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://www.finma.ch/en/news/2018/02/20180216-mm-ico-wegleitung/>
  - Wayback: <https://web.archive.org/web/20180216152357/https://www.finma.ch/en/news/2018/02/20180216-mm-ico-wegleitung/>
  - body_hash: `sha256:51986c8c7aaa21bd2e1dfd744dc5300bb1768a124bdb4f7b7881cead0ebbc7d6`
  - body_path: `sources/http_captures/switzerland-finma-tezos-zg-2018/primary/web.archive.org__web-20180216152357-https-www.finma.ch-en-news-2018-02-20180216-mm-ico-wegleitung__e8aeea4358.html`
  > Swiss Financial Market Supervisory Authority (FINMA /
> Eidgenössische Finanzmarktaufsicht) press release and accompanying
> "Guidelines for enquiries regarding the regulatory framework for
> initial coin offerings (ICOs)" (FINMA ICO-Wegleitung) published
> 2018-02-16. The guidelines establish FINMA's tripartite token
> taxonomy for the purpose of assessing ICO regulatory treatment
> under Swiss financial market law:
>   (1) Payment tokens (Zahlungs-Token) — synonymous with
>       cryptocurrencies, no further functions or links to
>       development projects; treated as means of payment and
>       subject to Swiss Anti-Money Laundering Act (GwG) obligations
>       once tradeable / transferable.
>   (2) Utility tokens (Nutzungs-Token) — confer digital access
>       rights to an application or service; not treated as
>       securities under Swiss law if their sole purpose is access
>       and they are usable at issuance.
>   (3) Asset tokens (Anlage-Token) — represent assets such as
>       participations in real underlyings, companies, earnings
>       streams, or entitlements to dividends/interest; treated as
>       securities, with attendant prospectus / civil-law
>       requirements under the Swiss Code of Obligations.
> The framework explicitly contemplates hybrid forms (e.g. utility
> tokens with payment-token characteristics simultaneously falling
> under GwG). The guidelines apply retroactively as the framework
> FINMA uses when ICO sponsors request a no-action enquiry; this
> affects Zug-based ICO sponsors from the 2017 cohort, including
> Tezos Foundation (Zug), whose 2017-07 ICO raised ~USD 232M and
> whose post-ICO governance dispute between the Foundation
> (Johann Gevers) and the Breitman family (Dynamic Ledger
> Solutions) escalated concurrent with FINMA's broader Swiss-ICO
> scrutiny. The guidelines themselves are framework guidance, not
> a per-entity enforcement order — they do not name Tezos or any
> other 2017-cohort issuer. evidence_use=contextual_unarchived
> because body_hash + body_path archival capture was not pinned in
> this agent-authoring pass; Wayback anchor is a year-prefix
> bracket pending re-pin by the human auditor.
- **`supporting_journalism`**
  - URL: <https://www.reuters.com/article/us-swiss-finma-ico-idUSKCN1G01YE>
  - Wayback: <https://web.archive.org/web/2018/https://www.reuters.com/article/us-swiss-finma-ico-idUSKCN1G01YE>
  > Reuters coverage of the 2018-02-16 FINMA ICO guidelines release,
> retained as a corroborating secondary anchor for the publication
> date and the tripartite token taxonomy. Useful for cross-checking
> the FINMA press-release language against international press
> reporting on the same day. evidence_use=contextual_unarchived;
> Wayback anchor is a year-prefix bracket pending re-pin.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: Swiss-nexus ICO sponsors (2017 cohort; Tezos Foundation, Zug, CH, as load-bearing illustrative target)

> Canonical target of the 2018-02-16 FINMA ICO guidelines is the
> open-ended regulatory class of Swiss-jurisdiction or Swiss-
> nexus ICO sponsors (token issuers, foundation vehicles, and
> asset-issuing entities) seeking regulatory clarity on Swiss
> financial market law treatment of their token issuances. The
> document is framework guidance applied via FINMA's enquiry
> process; it does not enumerate specific addressee entities. The
> Tezos Foundation (Zug, CH) is the most prominent 2017-cohort
> Swiss ICO sponsor affected by the retroactive framework — its
> 2017-07 ICO (~USD 232M raised) sits squarely in the Swiss
> Zug-foundation issuance pattern the guidelines clarify — but
> other 2017-cohort Swiss ICOs (Cardano Foundation, DFINITY,
> Bancor via BProtocol Foundation, Status, etc.) face the same
> framework retroactively. Marked enumeration=subset rather than
> complete because the affected class is open-ended and
> framework-defined rather than per-entity enumerated; the
> Tezos Foundation is named as the load-bearing illustrative
> target in title and analysis_notes but does not exhaust the
> affected class. No on-chain addresses or canonical_domains are
> enumerated because the framework guidance does not designate
> specific entities or hosts. Schema enum target.kind has no
> regulatory_class value; entity is the closest schema match and
> mirrors the precedent set by
> fatf-virtual-currencies-key-definitions-2014 and
> fincen-virtual-currency-msb-guidance-2013.

## 3. Changed-layer observations (supports the scoped claim)

*No observed_change entries. This is a `null_event`; see §4 for observed_no_change evidence supporting the null claim.*

## 4. No-change observations (where applicable)

### offramp_cex — `tripartite_payment_utility_asset_token_taxonomy_established_swiss_predicate_guidance`

**Window**: `2018-02-16 00:00:00+00:00` → `2020-01-01 00:00:00+00:00`

**Sources**:

- **`primary_legal`**
  - URL: <https://www.finma.ch/en/news/2018/02/20180216-mm-ico-wegleitung/>
  - Wayback: <https://web.archive.org/web/20180216152357/https://www.finma.ch/en/news/2018/02/20180216-mm-ico-wegleitung/>
  - body_hash: `sha256:51986c8c7aaa21bd2e1dfd744dc5300bb1768a124bdb4f7b7881cead0ebbc7d6`
  - body_path: `sources/http_captures/switzerland-finma-tezos-zg-2018/primary/web.archive.org__web-20180216152357-https-www.finma.ch-en-news-2018-02-20180216-mm-ico-wegleitung__e8aeea4358.html`
  > FINMA 2018-02-16 ICO Guidelines is the framework-level
> regulatory predicate that establishes the tripartite
> payment / utility / asset token taxonomy under Swiss
> financial market law (FINMASA / GwG / FinSA-precursor
> frame). observation_kind=observed_no_change honestly
> represents the load-bearing role of the document: it
> introduces the classification rule that subsequent
> Swiss-nexus ICO sponsors (including Tezos Foundation,
> Zug, CH; Cardano Foundation; DFINITY; Bancor; Status)
> must apply retroactively to their 2017-cohort
> issuances, but does not itself impose a per-issuance
> enforcement order or on-chain admin-key freeze.
> attribution=none per the schema constraint that
> observed_no_change rows take attribution=none; the
> dispersed framework predicate role is documented in
> analysis_notes. The Tezos Foundation governance
> dispute (Gevers vs Breitman family) escalated
> concurrent with this Swiss-ICO scrutiny window but is
> a corporate-governance dispute internal to the
> Foundation, not an observable censorship-layer change
> attributable to FINMA. Provisional year-prefix Wayback
> anchor pending re-pin in a follow-up human-audit pass.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`eu-mica-2023`](./eu-mica-2023.md)
- [`japan-fsa-coincheck-orders-2018`](./japan-fsa-coincheck-orders-2018.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `c3a88e8`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

