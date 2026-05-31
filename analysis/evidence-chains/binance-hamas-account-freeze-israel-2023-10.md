# Evidence chain — `binance-hamas-account-freeze-israel-2023-10`

**Status**: `admitted` · **Stratum**: `S5_corporate` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `71ac901` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-31` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "In the week after the 2023-10-07 Hamas attack, Binance froze/seized a set of
> accounts allegedly linked to Hamas at the request of Israeli law enforcement
> (Lahav 433 / NBCTF), transferring funds to the state treasury — a single-layer
> offramp_cex observed_change with attribution=plausible (trade-press anchored;
> the Hamas-link is the LE allegation)."

## 1. Trigger

- **Type**: `corporate_policy_change`
- **Actor**: `binance`
- **Timestamp**: `2023-10-10 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`semi_primary_wayback`**
  - URL: <https://www.dlnews.com/articles/regulation/israeli-police-seize-binance-account-linked-to-hamas/>
  - Wayback: <https://web.archive.org/web/20260117195331/https://www.dlnews.com/articles/regulation/israeli-police-seize-binance-account-linked-to-hamas/>
  - body_hash: `sha256:088d77dc114cd382054e9d91000977b41621db57a843311a5f516e1ed87d3705`
  - body_path: `sources/http_captures/binance-hamas-account-freeze-israel-2023-10/primary/web.archive.org__web-20260117195331-https-www.dlnews.com-articles-regulation-israeli-police-seize-binance-account-linked-to-hamas__c80d6b79b1.html`
  > DL News 2023-10-10: Israeli police seized Hamas-linked crypto accounts
> on Binance with the exchange's help; an Israeli cybercrime unit (Lahav
> 433) located the accounts on Binance, seized them, and transferred funds
> to the state treasury; action supported by the National Bureau for
> Counter Terror Financing (NBCTF), the Ministry of Defence, and
> intelligence organisations. Grep of captured body confirms "Israeli
> police seize Hamas crypto wallets on Binance", "Lahav 433", "NBCTF",
> "10 October 2023". Wayback 20260117195331 pinned.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: Binance accounts allegedly linked to Hamas (Israeli LE seizure)
- **Canonical domains**: `binance.com`

> Target is a set of Binance accounts that Israeli law enforcement identified
> as allegedly linked to Hamas fundraising and froze/seized with Binance's
> cooperation. Subset enumeration: the captured DL News report describes the
> seized-account set qualitatively (located by Lahav 433, funds moved to the
> state treasury) without an enumerated account list; a related FT report
> (not relied on here) put the figure at 100+ accounts. No on-chain
> address-level set is enumerated in the captured sources.

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `plausible` · Δt = 0h

**Event label**: `binance_freezes_hamas_linked_accounts_at_israeli_le_request`

**Timestamp**: `2023-10-10 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`semi_primary_wayback`**
  - URL: <https://www.dlnews.com/articles/regulation/israeli-police-seize-binance-account-linked-to-hamas/>
  - Wayback: <https://web.archive.org/web/20260117195331/https://www.dlnews.com/articles/regulation/israeli-police-seize-binance-account-linked-to-hamas/>
  - body_hash: `sha256:088d77dc114cd382054e9d91000977b41621db57a843311a5f516e1ed87d3705`
  - body_path: `sources/http_captures/binance-hamas-account-freeze-israel-2023-10/primary/web.archive.org__web-20260117195331-https-www.dlnews.com-articles-regulation-israeli-police-seize-binance-account-linked-to-hamas__c80d6b79b1.html`
  > DL News 2023-10-10: Israeli police (Lahav 433), with Binance's help and
> NBCTF/MoD support, seized Hamas-linked accounts on Binance and moved
> funds to the state treasury. attribution=plausible: the freeze/seizure
> is reported via trade press (not a Binance or Israeli-police primary
> notice) and the "Hamas-linked" characterization is the law
> enforcement's allegation as reported.
- **`semi_primary_wayback`**
  - URL: <https://unchainedcrypto.com/binance-helps-israel-police-freeze-hamas-crypto-accounts-report/>
  - Wayback: <https://web.archive.org/web/20250720194349/https://unchainedcrypto.com/binance-helps-israel-police-freeze-hamas-crypto-accounts-report/>
  - body_hash: `sha256:963f5cdf4e44604bd386c9a5040293397a3824dd90dfc4320da34785b2766ece`
  - body_path: `sources/http_captures/binance-hamas-account-freeze-israel-2023-10/primary/web.archive.org__web-20250720194349-https-unchainedcrypto.com-binance-helps-israel-police-freeze-hamas-crypto-accounts-report__74d7358f26.html`
  > Unchained: "Binance Helps Israel Police Freeze Hamas Crypto Accounts."
> Grep of captured body confirms "The seized funds will go into the state
> treasury" and the freeze-following-the-2023-10-07-attack framing.
> Independent second semi-primary anchor.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`israel-nbctf-hamas-crypto-addresses-2021`](./israel-nbctf-hamas-crypto-addresses-2021.md)
- [`ofac-hamas-buy-cash-msb-2023-10`](./ofac-hamas-buy-cash-msb-2023-10.md)
- [`binance-palestinian-accounts-seizure-israel-2023-11`](./binance-palestinian-accounts-seizure-israel-2023-11.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `71ac901`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

