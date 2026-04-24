# Evidence chain — `bitzlato-doj-2023`

**Status**: `admitted` · **Stratum**: `S3_doj_sec_cftc_fiod` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.1.0` · **Dataset cutoff**: `2026-04-22` · **Source commit**: `930f3d6` · **Schema**: `0.2.0` · **Event last_verified**: `2026-04-21` · **Tool version**: `0.1.0` · **Generated**: `2026-04-24T03:27:37Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "DOJ indictment of Bitzlato and its founder on 2023-01-18 — paired with
> FinCEN's Section 9714 special measure designation of Bitzlato as a
> 'primary money laundering concern' — produced a same-day L4 seizure of
> bitzlato.com. First application of FinCEN Section 9714 to a crypto
> exchange; structurally distinct from pure-OFAC or pure-DOJ paths."

## 1. Trigger

- **Type**: `doj_indictment`
- **Actor**: `US_DOJ`
- **Timestamp**: `2023-01-18 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://www.justice.gov/opa/pr/founder-and-majority-owner-cryptocurrency-exchange-charged-processing-over-700-million>
  - body_hash: `sha256:f329a65084549262222dbcdba541f48123bff56247cbe0f932e3e025f70f1318`
  - body_path: `sources/http_captures/bitzlato-doj-2023/backfill-1.3/www.justice.gov__opa-pr-founder-and-majority-owner-cryptocurrency-exchange-charged-processing-over-700-million__a42e944c97.html`
  > DOJ Office of Public Affairs press release announcing the Bitzlato action on 2023-01-18
- **`primary_legal`**
  - URL: <https://www.justice.gov/usao-edny/pr/founder-and-majority-owner-bitzlato-cryptocurrency-exchange-charged-unlicensed-money>
  > EDNY press release for the same enforcement action
- **`primary_legal`**
  - URL: <https://www.fincen.gov/news/news-releases/fincen-identifies-virtual-currency-exchange-bitzlato-primary-money-laundering>
  - Wayback: <https://web.archive.org/web/20260421105235/https://www.fincen.gov/news/news-releases/fincen-identifies-virtual-currency-exchange-bitzlato-primary-money-laundering>
  - body_hash: `sha256:bf2c40b29895e11a97510321b0a33003b56802ad3349fac1357f4b927cf143e6`
  - body_path: `sources/http_captures/bitzlato-doj-2023/backfill-1.3/www.fincen.gov__news-news-releases-fincen-identifies-virtual-currency-exchange-bitzlato-primary-money-laundering__c4a9bf0d08.html`
  > Concurrent FinCEN order describing Bitzlato as a primary money laundering concern

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `complete`
- **Chains**: `bitcoin`, `ethereum`

> Single named entity (Bitzlato) fully specified; no address-level enumeration claim is made at this event level.

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `direct` · Δt = Noneh

**Event label**: `exchange_operations_disrupted_by_enforcement`

**Timestamp**: `2023-01-18 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_legal`**
  - URL: <https://www.justice.gov/opa/pr/founder-and-majority-owner-cryptocurrency-exchange-charged-processing-over-700-million>
  - body_hash: `sha256:f329a65084549262222dbcdba541f48123bff56247cbe0f932e3e025f70f1318`
  - body_path: `sources/http_captures/bitzlato-doj-2023/backfill-1.3/www.justice.gov__opa-pr-founder-and-majority-owner-cryptocurrency-exchange-charged-processing-over-700-million__a42e944c97.html`
  > DOJ describes the Bitzlato disruption and arrest
- **`primary_legal`**
  - URL: <https://www.fincen.gov/news/news-releases/fincen-identifies-virtual-currency-exchange-bitzlato-primary-money-laundering>
  - Wayback: <https://web.archive.org/web/20260421105235/https://www.fincen.gov/news/news-releases/fincen-identifies-virtual-currency-exchange-bitzlato-primary-money-laundering>
  - body_hash: `sha256:bf2c40b29895e11a97510321b0a33003b56802ad3349fac1357f4b927cf143e6`
  - body_path: `sources/http_captures/bitzlato-doj-2023/backfill-1.3/www.fincen.gov__news-news-releases-fincen-identifies-virtual-currency-exchange-bitzlato-primary-money-laundering__c4a9bf0d08.html`
  > FinCEN order prohibits certain transmittals involving Bitzlato

## 4. No-change observations (where applicable)

### l3_rpc — `flashbots_protect_in_effect_no_step_change_attributable_to_this_event`

**Window**: `2023-01-18 00:00:00+00:00` → `2023-01-18 23:59:59+00:00`

**Sources**:

- **`primary_corporate`**
  - URL: <https://web.archive.org/web/20221222111307/https://protect.flashbots.net/>
  - Wayback: <https://web.archive.org/web/20221222111307/https://protect.flashbots.net/>
  - body_hash: `sha256:9d1177026d363b7599bdbfa4f66c2b33b5da7944283071b4d31ed8f31194257b`
  - body_path: `sources/http_captures/_shared/l3-rpc-filter-list/web.archive.org__web-20230101000000-https-protect.flashbots.net__a49e4f491d.html`
  > Flashbots Protect landing-page Wayback snapshot (2022-12-22)
> bracketing the event date 2023-01-18. Flashbots Protect (launched 2022-11)
> is the earliest major OFAC-compliance-adjacent public Ethereum RPC substrate.
> MEV-Blocker did not exist yet (launched 2023-03-27), so Flashbots Protect
> is the sole L3 anchor in this pre-MEV-Blocker window. Snapshot documents the
> provider + OFAC-aware routing was in effect; no per-transaction filter-list
> receipt is published.
- **`primary_corporate`**
  - URL: <https://web.archive.org/web/20230326063621/https://docs.flashbots.net/flashbots-protect/overview>
  - Wayback: <https://web.archive.org/web/20230326063621/https://docs.flashbots.net/flashbots-protect/overview>
  - body_hash: `sha256:38c0a61cb1a6c766ef72565562b37b3ccb65d581ed6915e9c74d70ee2fe511df`
  - body_path: `sources/http_captures/_shared/l3-rpc-filter-list/web.archive.org__web-20230215000000-https-docs.flashbots.net-flashbots-protect-overview__12a715a422.html`
  > Second Flashbots Protect Wayback anchor (2023-03-26)
> — post-event docs snapshot, independent archival anchor. The docs.flashbots.net
> overview page describes OFAC-compliance behavior of the Protect RPC endpoint.

## 5. Honest coverage gaps

- **l0_network** (`not_measured`): No network-layer measurement plan attached yet for this event
- **l4_frontend** (`not_measured`): Frontend/operator availability is not asserted in this release
- **asset_onchain** (`not_measured`): This trigger is not primarily an issuer blacklist event

## 8. How to audit this chain

1. Clone the repository at tag `v0.1.0` (commit `930f3d6`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

