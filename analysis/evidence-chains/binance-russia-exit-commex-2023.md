# Evidence chain — `binance-russia-exit-commex-2023`

**Status**: `admitted` · **Stratum**: `S5_corporate` · **Shape**: `comparison` (2 changed layer(s): `l4_frontend`, `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-4` · **Dataset cutoff**: `2026-05-16` · **Source commit**: `a0d61e2` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-16` · **Tool version**: `0.1.0` · **Generated**: `2026-05-20T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "The 2023-09-27 Binance Holdings Limited divestiture of its Russia-market
> business to the newly-created CommEX exchange, executed under US Treasury
> OFAC pressure and contemporaneous EU sanctions-enforcement concerns about
> ruble-denominated crypto trading, produced a two-layer cascade in the
> dataset: an L4 frontend transition notice on binance.com (Russian-locale)
> plus a destination landing on commex.com, and an offramp_cex restructuring
> in which Binance RUB on/off-ramp rails were wound down and the Russian
> user book was administratively migrated to CommEX over an announced
> one-year window. The row asserts only these two observational axes and
> does not claim L0 network, L1 consensus, L3 RPC, or asset_onchain
> effects; the downstream 2024-09 CommEX shutdown is a separate event row
> outside the scope of this admission."

## 1. Trigger

- **Type**: `corporate_policy_change`
- **Actor**: `binance_holdings_limited`
- **Timestamp**: `2023-09-27 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_corporate`**
  - URL: <https://www.binance.com/en/blog/ecosystem/binance-fully-exits-russia-with-sale-to-commex-3550293696068383963>
  - Wayback: <https://web.archive.org/web/2023/https://www.binance.com/en/blog/ecosystem/binance-fully-exits-russia-with-sale-to-commex-3550293696068383963>
  > Binance corporate blog post (2023-09-27): "Binance Fully Exits Russia
> With Sale to CommEX." Announces complete divestiture of Binance's
> Russia business to CommEX, a newly-launched exchange. Binance stated
> the transition would take "off-boarding existing Russian users" via
> an orderly migration of accounts to CommEX over up to one year, with
> Binance retaining no ongoing revenue share or option to repurchase.
> Marked evidence_use=contextual_unarchived because in this DRYRUN the
> authoring LLM agent did not personally pin a Wayback snapshot
> timestamp or compute a body_hash; the Binance blog URL slug is stable
> and routinely captured by Wayback in 2023 and remains the canonical
> corporate anchor. Pinned snapshot timestamp + body_hash to be
> re-anchored during human audit before this citation may serve as an
> admission anchor in its own right.
- **`primary_corporate`**
  - URL: <https://www.prnewswire.com/news-releases/binance-fully-exits-russia-with-sale-to-commex-301940042.html>
  - Wayback: <https://web.archive.org/web/2023/https://www.prnewswire.com/news-releases/binance-fully-exits-russia-with-sale-to-commex-301940042.html>
  > PRNewswire mirror of the 2023-09-27 Binance corporate announcement
> ("Binance fully exits Russia with sale to CommEX"). Confirms the
> same-day sale terms: full divestiture, up-to-one-year transition
> window for existing Russian users to migrate to CommEX, no ongoing
> ownership stake or revenue share retained by Binance. Wayback
> wildcard pointer (web/2023/) in lieu of a pinned-timestamp snapshot;
> evidence_use=contextual_unarchived pending human-audit re-pin.
- **`primary_corporate`**
  - URL: <https://commex.com/en/blog/post-detail/commex-announcement>
  - Wayback: <https://web.archive.org/web/2023/https://commex.com/en/blog/post-detail/commex-announcement>
  > CommEX launch announcement (late 2023-09): newly-created exchange
> positioned as the destination for migrating Russian Binance users.
> CommEX described itself as an independent operator with no formal
> ownership ties to Binance; subsequent reporting and the eventual
> 2024-09 CommEX shutdown rendered the independence claim contentious.
> Pinned here as primary-corporate context for the counterparty side
> of the Russia-business sale. Wayback wildcard pointer in lieu of
> pinned snapshot; evidence_use=contextual_unarchived pending human
> audit.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: Binance Holdings Limited (Russia market) / CommEX
- **Canonical domains**: `binance.com`, `commex.com`

> Binance Holdings Limited (corporate entity) Russia-market business line,
> consisting of (a) the Russian-user account base on binance.com,
> (b) Russian-ruble (RUB) on/off-ramp peer-to-peer (P2P) merchant rails,
> and (c) Russian-localized frontend surfaces (binance.com Russian-locale
> pages, Russian-language regional notices). The 2023-09-27 sale to CommEX
> is the corporate divestiture instrument; the target on the Binance side
> is the Russia-business book of users + RUB rails, not the global
> binance.com domain (which remained globally operational). On the CommEX
> side the target is the newly-launched commex.com exchange platform
> receiving migrating Russian Binance accounts.

## 3. Changed-layer observations (supports the scoped claim)

### l4_frontend · attribution: `direct` · Δt = 0h

**Event label**: `binance_russia_exit_announcement_and_commex_migration_notices`

**Timestamp**: `2023-09-27 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_corporate`**
  - URL: <https://www.binance.com/en/blog/ecosystem/binance-fully-exits-russia-with-sale-to-commex-3550293696068383963>
  - Wayback: <https://web.archive.org/web/2023/https://www.binance.com/en/blog/ecosystem/binance-fully-exits-russia-with-sale-to-commex-3550293696068383963>
  > Binance corporate blog hosted the 2023-09-27 transition
> announcement and acted as the canonical anchor for subsequent
> Russian-user migration notices. attribution=direct because the
> Binance frontend itself is the conduit through which the
> market-exit notice was delivered to Russian users; the corporate
> decision and the frontend-layer announcement are co-located in
> the same corporate actor. Wayback wildcard pointer in lieu of a
> pinned-timestamp snapshot; evidence_use=contextual_unarchived
> pending human-audit re-pin.
- **`primary_corporate`**
  - URL: <https://commex.com/en/blog/post-detail/commex-announcement>
  - Wayback: <https://web.archive.org/web/2023/https://commex.com/en/blog/post-detail/commex-announcement>
  > CommEX corporate frontend hosted the migration-destination
> landing page for Russian Binance users. Acts as the
> counterparty-side L4 anchor for the migration corridor.
> Wayback wildcard pointer; evidence_use=contextual_unarchived
> pending human-audit re-pin.

### offramp_cex · attribution: `direct` · Δt = 0h

**Event label**: `binance_rub_rails_wound_down_and_migrated_to_commex`

**Timestamp**: `2023-09-27 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_corporate`**
  - URL: <https://www.binance.com/en/blog/ecosystem/binance-fully-exits-russia-with-sale-to-commex-3550293696068383963>
  - Wayback: <https://web.archive.org/web/2023/https://www.binance.com/en/blog/ecosystem/binance-fully-exits-russia-with-sale-to-commex-3550293696068383963>
  > Binance corporate announcement is the legal-economic instrument
> executing the full divestiture of Russia-business RUB rails to
> CommEX. attribution=direct because Binance (the operator of the
> divested rails) made and announced the unilateral corporate
> decision; the OFAC + EU sanctions enforcement context is the
> plausible upstream pressure but the proximate cause of the
> off-ramp restructuring is the Binance corporate sale instrument
> itself. Wayback wildcard pointer; evidence_use=contextual_unarchived
> pending human-audit re-pin.
- **`primary_corporate`**
  - URL: <https://www.prnewswire.com/news-releases/binance-fully-exits-russia-with-sale-to-commex-301940042.html>
  - Wayback: <https://web.archive.org/web/2023/https://www.prnewswire.com/news-releases/binance-fully-exits-russia-with-sale-to-commex-301940042.html>
  > PRNewswire mirror corroborates the divestiture terms (no ongoing
> revenue share, no option to repurchase, one-year user-migration
> window). Provides redundant corporate anchor for the RUB-rail
> restructuring. Wayback wildcard pointer pending human-audit
> re-pin.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`binance-4framework-2023`](./binance-4framework-2023.md)
- [`eu-russia-crypto-wallet-cap-2022`](./eu-russia-crypto-wallet-cap-2022.md)
- [`eu-russia-full-crypto-wallet-ban-2022`](./eu-russia-full-crypto-wallet-ban-2022.md)
- [`eu-12th-russia-sanctions-2023`](./eu-12th-russia-sanctions-2023.md)
- [`coinbase-india-exit-2022`](./coinbase-india-exit-2022.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-4` (commit `a0d61e2`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

