# Evidence chain — `eba-virtual-currencies-opinion-eba-op-2014-08`

**Status**: `admitted` · **Stratum**: `S6_supranational` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `eabcaae` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-21` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "EBA Opinion EBA/Op/2014/08 of 4 July 2014 ('Opinion on virtual
> currencies') is the first major EU-level supervisory instrument on
> virtual currencies; it advises national supervisory authorities to
> discourage EU credit institutions, payment institutions, and
> e-money institutions from buying, holding, or selling virtual
> currencies pending a longer-term regulatory regime. The
> load-bearing axis is offramp_cex at the dispersed-cascade
> institutional-aggregate layer; downstream banking-rail / payment-
> rail severance against EU crypto businesses across 2014-2018 is
> consistent with the cascade hypothesis but not enumerated in this
> draft."

## 1. Trigger

- **Type**: `supranational_regulation`
- **Actor**: `EU_EBA`
- **Timestamp**: `2014-07-04 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://www.eba.europa.eu/sites/default/files/documents/10180/657547/81409b94-4222-45d7-ba3b-7deb5863ab57/EBA-Op-2014-08%20Opinion%20on%20Virtual%20Currencies.pdf>
  - Wayback: <https://web.archive.org/web/2014/https://www.eba.europa.eu/sites/default/files/documents/10180/657547/81409b94-4222-45d7-ba3b-7deb5863ab57/EBA-Op-2014-08%20Opinion%20on%20Virtual%20Currencies.pdf>
  > EBA Opinion EBA/Op/2014/08 ("Opinion on 'virtual currencies'")
> issued by the European Banking Authority on 4 July 2014. The
> Opinion identifies 70+ risks arising from virtual currencies
> (risks to users, market participants, financial integrity,
> payment systems, and regulatory authorities) and concludes that
> the risks outweigh the benefits in the EU context. While the
> Opinion proposes a longer-term comprehensive regulatory regime,
> as an immediate interim measure it advises national supervisory
> authorities to "discourage credit institutions, payment
> institutions, and e-money institutions from buying, holding, or
> selling virtual currencies" whilst no such regime is in place.
> This is the first major EU-level supervisory guidance on virtual
> currencies and sets the pre-MiCA pan-European regulatory tone
> for the 2014-2018 window.
- **`primary_legal`**
  - URL: <https://eba.europa.eu/eba-proposes-potential-regulatory-regime-for-virtual-currencies-but-also-advises-that-financial-institutions-should-not-buy-hold-or-sell-them-whilst-n>
  - Wayback: <https://web.archive.org/web/20191031205451/https://eba.europa.eu/eba-proposes-potential-regulatory-regime-for-virtual-currencies-but-also-advises-that-financial-institutions-should-not-buy-hold-or-sell-them-whilst-n>
  - body_hash: `sha256:db0c0a0913e085cf73e49b4ce0b26874ea9b4f7f1f0782aa15d5b1d4a0ace781`
  - body_path: `sources/http_captures/eba-virtual-currencies-opinion-eba-op-2014-08/primary/web.archive.org__web-20191031205451-https-eba.europa.eu-eba-proposes-potential-regulatory-regime-for-virtual-currencies-but-also-advises-that-financial-institutions-sho__a1903a26ac.html`
  > EBA press release accompanying the 2014-07-04 publication of
> EBA/Op/2014/08, confirming the discouragement recommendation
> directed at credit institutions, payment institutions, and
> e-money institutions and the parallel proposal of a longer-term
> regulatory regime. Wayback memento 20191031205451 captured
> 2026-05-21 with replayable body_hash. The Opinion PDF itself
> has no Wayback memento across 2014-2024 (CDX prefix-match
> empty); the press release substitutes as the primary_legal
> admission anchor.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: EU credit/payment/e-money institutions handling virtual currencies

> Class-level target: EU credit institutions, payment institutions,
> and e-money institutions (as defined under CRD IV, the Payment
> Services Directive, and the E-Money Directive respectively) that
> might otherwise buy, hold, or sell virtual currencies. The
> discouragement is routed through national competent authorities
> rather than imposed on named institutions; no address-level or
> institution-level enumeration. The 2014 EU credit/payment/e-money
> institutional population numbers in the thousands across the 28
> Member States and EEA participants supervised by the EBA.

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `plausible` · Δt = 0h

**Event label**: `eba_opinion_2014_08_discourages_institutional_vc_handling`

**Timestamp**: `2014-07-04 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_legal`**
  - URL: <https://www.eba.europa.eu/sites/default/files/documents/10180/657547/81409b94-4222-45d7-ba3b-7deb5863ab57/EBA-Op-2014-08%20Opinion%20on%20Virtual%20Currencies.pdf>
  - Wayback: <https://web.archive.org/web/2014/https://www.eba.europa.eu/sites/default/files/documents/10180/657547/81409b94-4222-45d7-ba3b-7deb5863ab57/EBA-Op-2014-08%20Opinion%20on%20Virtual%20Currencies.pdf>
  > EBA/Op/2014/08 directs national supervisory authorities to
> discourage EU credit/payment/e-money institutions from buying,
> holding, or selling virtual currencies pending a longer-term
> regulatory regime. observation_kind=observed_change at the
> supranational supervisory-instruction layer: the Opinion's
> issuance is itself the regulatory change at offramp_cex via
> the class-level discouragement directive routed through
> national competent authorities. attribution=plausible (not
> direct) because the Opinion operates through downstream
> national-supervisor and institution-level risk-appetite
> decisions rather than a discrete enumerable enforcement
> action; downstream banking-rail severance against EU crypto
> businesses across 2014-2018 is consistent with the cascade
> hypothesis but not enumerated here. The PDF carries the
> load-bearing Opinion text; replayable anchor for this row is
> on the trigger-level EBA press release citation (Wayback
> memento 20191031205451 captured 2026-05-21).

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`fatf-r15-vasp-travel-rule-2019`](./fatf-r15-vasp-travel-rule-2019.md)
- [`eu-mica-2023`](./eu-mica-2023.md)
- [`oecd-carf-2022`](./oecd-carf-2022.md)
- [`fatf-virtual-currencies-key-definitions-2014`](./fatf-virtual-currencies-key-definitions-2014.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `eabcaae`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

