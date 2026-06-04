# Evidence chain — `apple-uniswap-wallet-app-store-rejection-2023-03`

**Status**: `admitted` · **Stratum**: `S5_corporate` · **Shape**: `comparison` (1 changed layer(s): `l4_frontend`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-02` · **Source commit**: `f54a8ae` · **Schema**: `0.2.0` · **Event last_verified**: `2026-06-01` · **Tool version**: `0.1.0` · **Generated**: `2026-06-04T09:44:11Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "Uniswap Labs' first-party 2023-03-03 early-access post records that
> Apple's App Store review had rejected the final Uniswap Wallet iOS build
> before the planned December launch and still would not green-light the
> public launch, so Uniswap distributed early access through TestFlight
> instead. This is a 1-layer l4_frontend observed_change
> (attribution=plausible, because Apple gave no public reason) of app-store
> gatekeeping against a major crypto app. Same gatekeeper pattern as
> apple-india-crypto-exchange-removal-2024-01."

## 1. Trigger

- **Type**: `corporate_policy_change`
- **Actor**: `APPLE_APP_STORE`
- **Timestamp**: `2023-03-03 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_corporate`**
  - URL: <https://blog.uniswap.org/uniswap-mobile-wallet-early-access>
  - body_hash: `sha256:9c5bfeac32305cb73c8dcfbc16665fb3af9201acc48f95982ed71ffd7603987f`
  - body_path: `sources/http_captures/apple-uniswap-wallet-app-store-rejection-2023-03/official-uniswap-blog/blog.uniswap.org__uniswap-mobile-wallet-early-access__fd779939e8.html`
  > Uniswap Labs first-party blog post, "Uniswap Mobile App Early
> Access" (2023-03-03). The captured page states that Apple approved
> Uniswap's first build in October, rejected the final build shortly
> before the planned December launch, and still would not green-light
> the launch despite Uniswap responding to Apple's concerns and
> saying it complied with Apple's guidelines. It also records
> TestFlight early access while Uniswap waited for App Store approval.
> Captured 2026-06-01.
- **`semi_primary_wayback`**
  - URL: <https://fortune.com/crypto/2023/03/03/uniswap-wallet-apple-app-store/>
  - Wayback: <https://web.archive.org/web/20250428020543/https://fortune.com/crypto/2023/03/03/uniswap-wallet-apple-app-store/>
  - body_hash: `sha256:119e6bd8b94763bcbb78109a4183b6ec062937a941d588595ee43ec0ec9c3837`
  - body_path: `sources/http_captures/apple-uniswap-wallet-app-store-rejection-2023-03/primary/web.archive.org__web-20250428020543-https-fortune.com-crypto-2023-03-03-uniswap-wallet-apple-app-store__0546440ba0.html`
  > Fortune (2023-03-03): Uniswap Labs announced its self-custody mobile
> Wallet but said Apple refused to approve it for the App Store,
> leaving it unavailable to iOS users. Per Uniswap's blog (quoted),
> Apple approved other self-custody swapping wallets but "won't
> green-light our launch and we don't know why"; Uniswap instead
> distributed the app to 10,000 users via TestFlight while awaiting
> approval. The captured page confirms "App Store", "Apple",
> "self-custody", "approve", and "wallet". Verified via grep of the
> pinned body.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `complete`
- **Actor name**: Uniswap Wallet (iOS) on Apple App Store
- **Chains**: `ethereum`
- **Canonical domains**: `apps.apple.com`

> Single named app: the Uniswap (Labs) self-custody mobile Wallet for
> iOS. Apple (App Store review) is the gatekeeping actor; the target is
> the Uniswap Wallet app, which Apple declined to approve for App Store
> distribution. Complete enumeration of the single app affected.

## 3. Changed-layer observations (supports the scoped claim)

### l4_frontend · attribution: `plausible` · Δt = Noneh

**Event label**: `apple_refuses_uniswap_wallet_app_store_approval`

**Timestamp**: `2023-03-03 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_corporate`**
  - URL: <https://blog.uniswap.org/uniswap-mobile-wallet-early-access>
  - body_hash: `sha256:9c5bfeac32305cb73c8dcfbc16665fb3af9201acc48f95982ed71ffd7603987f`
  - body_path: `sources/http_captures/apple-uniswap-wallet-app-store-rejection-2023-03/official-uniswap-blog/blog.uniswap.org__uniswap-mobile-wallet-early-access__fd779939e8.html`
  > Uniswap's own 2023-03-03 post records the app-store gatekeeping
> state: Apple approved an earlier build, rejected the final build
> before the planned December launch, and had not green-lit the
> public App Store release by the March early-access announcement.
> attribution remains plausible because this is Uniswap's account
> of Apple's review decision and Apple gave no public rationale.
- **`semi_primary_wayback`**
  - URL: <https://fortune.com/crypto/2023/03/03/uniswap-wallet-apple-app-store/>
  - Wayback: <https://web.archive.org/web/20250428020543/https://fortune.com/crypto/2023/03/03/uniswap-wallet-apple-app-store/>
  - body_hash: `sha256:119e6bd8b94763bcbb78109a4183b6ec062937a941d588595ee43ec0ec9c3837`
  - body_path: `sources/http_captures/apple-uniswap-wallet-app-store-rejection-2023-03/primary/web.archive.org__web-20250428020543-https-fortune.com-crypto-2023-03-03-uniswap-wallet-apple-app-store__0546440ba0.html`
  > Apple's 2023-03 refusal to approve the Uniswap self-custody Wallet
> for the App Store. attribution=plausible: the refusal is directly
> observed (and stated by Uniswap), but Apple gave no public
> rationale ("we don't know why" per Uniswap), so the reason is
> unstated by the gatekeeper.
- **`semi_primary_wayback`**
  - URL: <https://www.coindesk.com/business/2023/03/03/uniswap-wants-to-launch-crypto-wallet-app-but-apple-says-not-so-fast>
  - Wayback: <https://web.archive.org/web/20240907112054/https://www.coindesk.com/business/2023/03/03/uniswap-wants-to-launch-crypto-wallet-app-but-apple-says-not-so-fast/>
  - body_hash: `sha256:e771da735d7327df1f6dd67f5a8a8bb59c6175f8af2b865dcf737ab234727eaf`
  - body_path: `sources/http_captures/apple-uniswap-wallet-app-store-rejection-2023-03/primary/web.archive.org__web-20240907112054-https-www.coindesk.com-business-2023-03-03-uniswap-wants-to-launch-crypto-wallet-app-but-apple-says-not-so-fast__8ac039667b.html`
  > CoinDesk corroboration: Apple won't green-light the Uniswap Wallet
> launch despite approving other self-custody swapping wallets.
> Independent semi-primary second anchor.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`apple-india-crypto-exchange-removal-2024-01`](./apple-india-crypto-exchange-removal-2024-01.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `f54a8ae`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

