# Evidence chain — `ukraine-virtual-assets-law-2022-03`

**Status**: `admitted` · **Stratum**: `S4_nation_state` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `ea43eeb` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-21` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T03:45:56Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "On 2022-03-16, two and a half weeks after the start of the Russian
> invasion, Ukrainian President Volodymyr Zelensky signed the Law of
> Ukraine 'On Virtual Assets' (Bill 3637), establishing the legal
> status of virtual assets in Ukraine and designating the National
> Securities and Stock Market Commission (NSSMC) as the primary
> regulator of a Virtual Asset Service Provider (VASP) licensing
> regime. The law is dual-character — permissive in framing
> (legalizing the asset class amid the wartime crypto-donation surge)
> while simultaneously compliance-mandating at the offramp_cex layer
> (NSSMC licensing chokepoint for any VASP servicing UA users,
> including offshore centralized exchanges). The downstream UA-VASP
> licensing cascade is recorded as coverage_gap with
> attribution=unknown because it is not yet measurable at issuance
> date and unfolds dispersedly across 2022-2024 NSSMC secondary
> rulemaking and exigent wartime administrative practice."

## 1. Trigger

- **Type**: `nation_state_block`
- **Actor**: `UA_PRESIDENT_UA_NSSMC`
- **Timestamp**: `2022-03-16 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://www.president.gov.ua/news/prezident-pidpisav-zakon-pro-virtualni-aktivi-73575>
  - Wayback: <https://web.archive.org/web/2022/https://www.president.gov.ua/news/prezident-pidpisav-zakon-pro-virtualni-aktivi-73575>
  > Office of the President of Ukraine press release 2022-03-16
> announcing President Volodymyr Zelensky's signature of the Law of
> Ukraine "On Virtual Assets" (Закон України "Про віртуальні
> активи", Bill No. 3637). The law establishes the legal status,
> classification, and ownership rules for virtual assets in Ukraine
> and designates the National Securities and Stock Market Commission
> (NSSMC, Національна комісія з цінних паперів та фондового ринку)
> as primary regulator of the virtual asset market, alongside the
> National Bank of Ukraine for asset-backed-virtual-asset issuance.
> The law mandates registration / licensing of Virtual Asset Service
> Providers (VASPs) operating in Ukraine. Bill 3637 was adopted by
> the Verkhovna Rada (Parliament) on 2022-02-17, replacing an
> earlier September 2021 draft that Zelensky had returned to
> Parliament in October 2021 for revision on grounds of
> insufficient NSSMC budget/authority. Signed two and a half weeks
> after the start of the Russian invasion (2022-02-24) and amid
> a surge of crypto-denominated donations to the Ukrainian
> government. evidence_use=contextual_unarchived: wayback wildcard
> (web/2022/) pointer in lieu of a pinned-timestamp snapshot; no
> body_hash+body_path pair captured into sources/http_captures/
> ukraine-virtual-assets-law-2022-03/ in this DRYRUN authoring
> pass. Pinned archive deferred to follow-up human-audit pass.
- **`semi_primary_wayback`**
  - URL: <https://www.coindesk.com/policy/2022/03/16/ukraines-zelensky-signs-virtual-assets-bill-into-law-legalizing-crypto>
  - Wayback: <https://web.archive.org/web/20220316162154/https://www.coindesk.com/policy/2022/03/16/ukraines-zelensky-signs-virtual-assets-bill-into-law-legalizing-crypto>
  - body_hash: `sha256:664c1193796b533f6632b84305c97d464c220273da1f6a69323c07c7cc6d1585`
  - body_path: `sources/http_captures/ukraine-virtual-assets-law-2022-03/primary/web.archive.org__web-20220316162154-https-www.coindesk.com-policy-2022-03-16-ukraines-zelensky-signs-virtual-assets-bill-into-law-legalizing-crypto__3dbc77c05f.html`
  > CoinDesk 2022-03-16 coverage: "Ukraine's Zelenskyy Signs Virtual
> Assets Bill Into Law, Legalizing Crypto." Independent confirmation
> of the signing date, NSSMC + NBU dual-regulator design, and
> VASP-registration framework. Notes the law's enabling function
> (legalization of crypto sector during wartime crypto-donation
> surge) and its compliance-mandating function (licensing
> chokepoint for VASPs serving Ukrainian users).
- **`semi_primary_wayback`**
  - URL: <https://www.elliptic.co/blog/crypto-regulatory-affairs-ukrainian-president-signs-virtual-currency-bill-into-law>
  - Wayback: <https://web.archive.org/web/20220325085252/https://www.elliptic.co/blog/crypto-regulatory-affairs-ukrainian-president-signs-virtual-currency-bill-into-law>
  - body_hash: `sha256:67b1b820012c975c0f168ec6c888295520264f7d4fe9b1f97247cc2c8c0169b8`
  - body_path: `sources/http_captures/ukraine-virtual-assets-law-2022-03/primary/web.archive.org__web-20220325085252-https-www.elliptic.co-blog-crypto-regulatory-affairs-ukrainian-president-signs-virtual-currency-bill-into-law__23f7c97c35.html`
  > Elliptic regulatory-affairs commentary 2022-03 on the Law "On
> Virtual Assets." Documents the dual-character framing: permissive
> on its face (creating legal status for the asset class and
> permitting crypto businesses to open Ukrainian bank accounts) and
> compliance-mandating in operation (NSSMC licensing of VASPs
> servicing UA users, with implications for offshore exchanges
> seeking to retain UA customer relationships under PMLA-style
> registration). Notes that the law's full application depended on
> adoption of secondary regulations and NSSMC enabling resources
> through 2022-2023.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: Virtual Asset Service Providers servicing Ukrainian users (NSSMC-licensable class)

> Virtual Asset Service Providers (VASPs) operating in or servicing
> Ukrainian users — including UA-domiciled exchanges, custodial wallet
> providers, virtual-asset-for-fiat exchange operators, and offshore
> centralized exchanges (e.g. Binance, Kraken, KuCoin, Bitfinex) that
> accept Ukrainian users or maintain UA banking-rail relationships.
> Enumeration=subset because the licensing regime targets the VASP
> class rather than enumerable addresses; the operative population is
> open-ended and evolves with NSSMC secondary regulation, VASP
> registration filings, and downstream compliance enforcement. No
> specific addresses or canonical domains are designated by the law
> itself. Dual-character target posture: permissive (legalizing the
> asset class and the on-chain layer for UA persons) while compliance-
> mandating at the offramp_cex layer (licensing chokepoint restricting
> unlicensed VASPs from servicing UA users).

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `plausible` · Δt = 0h

**Event label**: `ua_law_on_virtual_assets_signed_vasp_licensing_framework_established`

**Timestamp**: `2022-03-16 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`semi_primary_wayback`**
  - URL: <https://www.coindesk.com/policy/2022/03/16/ukraines-zelensky-signs-virtual-assets-bill-into-law-legalizing-crypto>
  - Wayback: <https://web.archive.org/web/20220316162154/https://www.coindesk.com/policy/2022/03/16/ukraines-zelensky-signs-virtual-assets-bill-into-law-legalizing-crypto>
  - body_hash: `sha256:664c1193796b533f6632b84305c97d464c220273da1f6a69323c07c7cc6d1585`
  - body_path: `sources/http_captures/ukraine-virtual-assets-law-2022-03/primary/web.archive.org__web-20220316162154-https-www.coindesk.com-policy-2022-03-16-ukraines-zelensky-signs-virtual-assets-bill-into-law-legalizing-crypto__3dbc77c05f.html`
  > CoinDesk 2022-03-16 confirms Zelensky signed the Law On Virtual
> Assets. Semi-primary anchor 1 of 2.
- **`semi_primary_wayback`**
  - URL: <https://www.elliptic.co/blog/crypto-regulatory-affairs-ukrainian-president-signs-virtual-currency-bill-into-law>
  - Wayback: <https://web.archive.org/web/20220325085252/https://www.elliptic.co/blog/crypto-regulatory-affairs-ukrainian-president-signs-virtual-currency-bill-into-law>
  - body_hash: `sha256:67b1b820012c975c0f168ec6c888295520264f7d4fe9b1f97247cc2c8c0169b8`
  - body_path: `sources/http_captures/ukraine-virtual-assets-law-2022-03/primary/web.archive.org__web-20220325085252-https-www.elliptic.co-blog-crypto-regulatory-affairs-ukrainian-president-signs-virtual-currency-bill-into-law__23f7c97c35.html`
  > Elliptic analysis of the Ukraine Law On Virtual Assets +
> NSSMC VASP framework. Semi-primary anchor 2 of 2.
- **`primary_legal`**
  - URL: <https://www.president.gov.ua/news/prezident-pidpisav-zakon-pro-virtualni-aktivi-73575>
  - Wayback: <https://web.archive.org/web/2022/https://www.president.gov.ua/news/prezident-pidpisav-zakon-pro-virtualni-aktivi-73575>
  > Office of the President of Ukraine press release anchoring
> Zelensky's 2022-03-16 signature of the Law "On Virtual Assets"
> (Bill 3637). The law establishes the NSSMC-led VASP licensing
> framework that brings UA-domiciled and UA-servicing virtual
> asset service providers into a registration / compliance
> regime. attribution=plausible (not direct) because the law is
> dual-character: permissive in framing (legalizing the asset
> class, enabling UA-domiciled crypto businesses to bank
> domestically and receive wartime crypto donations) while
> simultaneously compliance-mandating at the offramp_cex layer
> (any VASP servicing UA users becomes subject to NSSMC
> licensing). The immediate signing-date legal effect is
> unambiguous, but the cascade on offshore-exchange UA-user
> relationships unfolds dispersedly over 2022-2024 secondary
> regulation and exigent wartime administrative practice; direct
> attribution would overstate the immediate observable cascade.
> evidence_use=contextual_unarchived: wayback wildcard pointer
> in lieu of a pinned-timestamp snapshot; replace with a
> verified capture + body_hash / body_path during real human
> audit.
- **`supporting_journalism`**
  - URL: <https://www.coindesk.com/policy/2022/03/16/ukraines-zelensky-signs-virtual-assets-bill-into-law-legalizing-crypto>
  - Wayback: <https://web.archive.org/web/2022/https://www.coindesk.com/policy/2022/03/16/ukraines-zelensky-signs-virtual-assets-bill-into-law-legalizing-crypto>
  > CoinDesk 2022-03-16 coverage corroborating the signing date
> and the NSSMC + NBU dual-regulator architecture of the VASP
> licensing framework. Independent secondary anchor pending
> pinned primary capture.

## 4. No-change observations (where applicable)

### offramp_cex — `ua_vasp_licensing_cascade_not_yet_measurable_at_issuance`

**Window**: `2022-03-16 00:00:00+00:00` → `2022-12-31 23:59:59+00:00`

**Sources**:

- **`semi_primary_wayback`**
  - URL: <https://www.coindesk.com/policy/2022/03/16/ukraines-zelensky-signs-virtual-assets-bill-into-law-legalizing-crypto>
  - Wayback: <https://web.archive.org/web/20220316162154/https://www.coindesk.com/policy/2022/03/16/ukraines-zelensky-signs-virtual-assets-bill-into-law-legalizing-crypto>
  - body_hash: `sha256:664c1193796b533f6632b84305c97d464c220273da1f6a69323c07c7cc6d1585`
  - body_path: `sources/http_captures/ukraine-virtual-assets-law-2022-03/primary/web.archive.org__web-20220316162154-https-www.coindesk.com-policy-2022-03-16-ukraines-zelensky-signs-virtual-assets-bill-into-law-legalizing-crypto__3dbc77c05f.html`
  > CoinDesk confirms the law signing; no measurable downstream
> VASP-licensing cascade at issuance date. Semi-primary anchor 1 of 2.
- **`semi_primary_wayback`**
  - URL: <https://www.elliptic.co/blog/crypto-regulatory-affairs-ukrainian-president-signs-virtual-currency-bill-into-law>
  - Wayback: <https://web.archive.org/web/20220325085252/https://www.elliptic.co/blog/crypto-regulatory-affairs-ukrainian-president-signs-virtual-currency-bill-into-law>
  - body_hash: `sha256:67b1b820012c975c0f168ec6c888295520264f7d4fe9b1f97247cc2c8c0169b8`
  - body_path: `sources/http_captures/ukraine-virtual-assets-law-2022-03/primary/web.archive.org__web-20220325085252-https-www.elliptic.co-blog-crypto-regulatory-affairs-ukrainian-president-signs-virtual-currency-bill-into-law__23f7c97c35.html`
  > Elliptic analysis; cascade forward-looking/dispersed.
> Semi-primary anchor 2 of 2.
- **`primary_legal`**
  - URL: <https://www.president.gov.ua/news/prezident-pidpisav-zakon-pro-virtualni-aktivi-73575>
  - Wayback: <https://web.archive.org/web/2022/https://www.president.gov.ua/news/prezident-pidpisav-zakon-pro-virtualni-aktivi-73575>
  > Honest-note coverage_gap row honoring the brief's
> dual-character observation: the downstream UA-VASP licensing
> cascade — VASP registration filings, offshore-exchange
> compliance posture adjustments, NSSMC secondary regulation
> adoption, and any unlicensed-VASP enforcement actions — is
> not yet measurable at the 2022-03-16 issuance date.
> attribution=unknown because the cascade is forward-looking
> and dispersed across 2022-2024 NSSMC secondary rulemaking
> and exigent wartime administrative practice rather than
> localized to a single point-in-time CEX cessation directly
> attributable to the law alone. A pinned VASP-registration
> roster and downstream enforcement archive (NSSMC-licensed
> VASP count, offshore-exchange UA-user-restriction notices,
> any unlicensed-VASP enforcement filings) is deferred to a
> follow-up authoring pass and would be the load-bearing
> replayable artifact for upgrading this row to a falsifiable
> observed_no_change or a second observed_change layer.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`eu-tfr-recast-2023`](./eu-tfr-recast-2023.md)
- [`fatf-r15-vasp-travel-rule-2019`](./fatf-r15-vasp-travel-rule-2019.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `ea43eeb`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

