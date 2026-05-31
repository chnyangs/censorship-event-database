# Evidence chain — `binance-palestinian-accounts-seizure-israel-2023-11`

**Status**: `admitted` · **Stratum**: `S5_corporate` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `00764cd` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-31` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "Binance blocked a contested set of Palestinian user accounts from
> transacting under a November 2023 Israeli NBCTF (Paul Landes) seizure
> order invoking anti-terrorism law; single-layer offramp_cex
> observed_change, attribution=plausible (Binance confirms blocking
> accounts but the order's scope/count is contested and unreproduced;
> enumeration=subset). No verified on-chain freeze tx, so the effect is
> carried at offramp_cex, not asset_onchain."

## 1. Trigger

- **Type**: `corporate_policy_change`
- **Actor**: `binance`
- **Timestamp**: `2023-11-01 00:00:00+00:00` (precision: `week`)

### Trigger citations

- **`semi_primary_wayback`**
  - URL: <https://cointelegraph.com/news/binance-seize-funds-palestine-israel>
  - Wayback: <https://web.archive.org/web/20240827142258/https://cointelegraph.com/news/binance-seize-funds-palestine-israel>
  - body_hash: `sha256:c33a10e717954b66726ad2befd49f1a22dc05de6a43543866c85adc9d8be7102`
  - body_path: `sources/http_captures/binance-palestinian-accounts-seizure-israel-2023-11/primary/web.archive.org__web-20240827142258-https-cointelegraph.com-news-binance-seize-funds-palestine-israel__51e5185689.html`
  > Cointelegraph (capture 2024-08-27): Binance blocked Palestinian
> user accounts pursuant to a November 2023 letter signed by Israel's
> National Bureau for Counter Terror Financing (NBCTF), Paul Landes,
> which rejected appeals by Palestinian users to restore the blocked
> funds. The Hebrew letter invoked Israeli anti-terrorism law
> permitting the Minister of Defense to issue a "temporary seizure of
> property of a declared terrorist organization," including
> cryptocurrency funds. Binance disputed any mass freeze, stating
> "Only a small number of user accounts, linked to illicit funds,
> were blocked from transacting." Wayback 20240827142258.
- **`supporting_community`**
  - URL: <https://skylineforhuman.org/en/news/details/801/binances-response-to-skylines-letter-on-seizure-of-palestinian-cryptocurrency-wallets>
  - Wayback: <https://web.archive.org/web/20241008190737/https://skylineforhuman.org/en/news/details/801/binances-response-to-skylines-letter-on-seizure-of-palestinian-cryptocurrency-wallets>
  - body_hash: `sha256:ea7ab115856d2c3bb7ac0435bb6068fa7cfdd1e7c0fc1748431c483a77373afe`
  - body_path: `sources/http_captures/binance-palestinian-accounts-seizure-israel-2023-11/primary/web.archive.org__web-20241008190737-https-skylineforhuman.org-en-news-details-801-binances-response-to-skylines-letter-on-seizure-of-palestinian-cryptocurrency-wallets__c6a6fa0209.html`
  > Skyline International for Human Rights (capture 2024-10-08):
> rights-org account of Binance's response to its letter on the
> seizure of Palestinian cryptocurrency wallets, corroborating the
> Binance blocking action tied to the NBCTF seizure correspondence.
> Advocacy source — supporting_community, used as corroboration not
> as the primary action attestation.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: Binance (Palestinian user accounts under Israeli NBCTF order)

> Palestinian-user Binance accounts blocked under the November 2023
> NBCTF seizure order. The exact set is contested: Binance states only
> "a small number of user accounts, linked to illicit funds," were
> blocked, while Palestinian advocates allege a broader sweep; the
> captured sources do not enumerate a verified account list or count, so
> enumeration=subset.

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `plausible` · Δt = 0h

**Event label**: `binance_blocks_palestinian_user_accounts_under_israeli_nbctf_order`

**Timestamp**: `2023-11-01 00:00:00+00:00` (precision: `week`)

**Sources**:

- **`semi_primary_wayback`**
  - URL: <https://cointelegraph.com/news/binance-seize-funds-palestine-israel>
  - Wayback: <https://web.archive.org/web/20240827142258/https://cointelegraph.com/news/binance-seize-funds-palestine-israel>
  - body_hash: `sha256:c33a10e717954b66726ad2befd49f1a22dc05de6a43543866c85adc9d8be7102`
  - body_path: `sources/http_captures/binance-palestinian-accounts-seizure-israel-2023-11/primary/web.archive.org__web-20240827142258-https-cointelegraph.com-news-binance-seize-funds-palestine-israel__51e5185689.html`
  > Cointelegraph: Binance blocked Palestinian user accounts under a
> November 2023 NBCTF (Paul Landes) seizure letter invoking Israeli
> anti-terrorism law; Binance states only "a small number of user
> accounts, linked to illicit funds," were blocked.
> attribution=plausible: the account-blocking action is directly
> reported and Binance confirms blocking accounts, but the order's
> target scope/count is contested and the captured page does not
> reproduce the primary seizure order or an enumerated list, so a
> conservative attribution is retained.
- **`supporting_community`**
  - URL: <https://skylineforhuman.org/en/news/details/801/binances-response-to-skylines-letter-on-seizure-of-palestinian-cryptocurrency-wallets>
  - Wayback: <https://web.archive.org/web/20241008190737/https://skylineforhuman.org/en/news/details/801/binances-response-to-skylines-letter-on-seizure-of-palestinian-cryptocurrency-wallets>
  - body_hash: `sha256:ea7ab115856d2c3bb7ac0435bb6068fa7cfdd1e7c0fc1748431c483a77373afe`
  - body_path: `sources/http_captures/binance-palestinian-accounts-seizure-israel-2023-11/primary/web.archive.org__web-20241008190737-https-skylineforhuman.org-en-news-details-801-binances-response-to-skylines-letter-on-seizure-of-palestinian-cryptocurrency-wallets__c6a6fa0209.html`
  > Skyline International for Human Rights corroboration of the
> Binance Palestinian-wallet blocking tied to the NBCTF seizure
> correspondence. Advocacy source (supporting_community);
> corroboration only.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`israel-nbctf-hamas-crypto-addresses-2021`](./israel-nbctf-hamas-crypto-addresses-2021.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `00764cd`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

