# Evidence chain — `blender-ofac-2022`

**Status**: `admitted` · **Stratum**: `S1_ofac_sdn` · **Shape**: `comparison` (1 changed layer(s): `l4_frontend`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-05-31` · **Source commit**: `b71c00e` · **Schema**: `0.2.0` · **Event last_verified**: `2026-04-21` · **Tool version**: `0.1.0` · **Generated**: `2026-05-31T13:15:30Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "The first-ever OFAC mixer designation (Blender.io,
> 2022-05-06) produced a measurable L4 frontend change within 10 days in the form of
> operator-driven application teardown (blender.io reduced to default nginx), structurally
> distinct from the US-compliance-driven collapse of Tornado Cash 2022 and the law-
> enforcement seizure of Cryptex 2024."

## 1. Trigger

- **Type**: `ofac_sdn_designation`
- **Actor**: `US_OFAC`
- **Timestamp**: `2022-05-06 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://ofac.treasury.gov/recent-actions/20220506>
  - Wayback: <https://web.archive.org/web/20260421135013/https://ofac.treasury.gov/recent-actions/20220506>
  - body_hash: `sha256:088245cfd0563f12865e84bf51db27dffdd2de2eadb742d278b3f901ca55f3ee`
  - body_path: `sources/http_captures/blender-ofac-2022/ofac-recent-actions/ofac.treasury.gov__recent-actions-20220506__7887ae4d27.html`
  > OFAC Recent Actions page for 2022-05-06. First crypto mixer ever sanctioned by OFAC
> (predates Tornado Cash 2022-08-08 by 94 days). Entity BLENDER.IO (aka BLENDERIO /
> @BLENDERIO_ENGLISH / @BLENDERIO_RUSSIAN / @MADEAMAZE_BOT) with 45 unique Bitcoin
> addresses attached. Same-day action updated DPRK/Lazarus designations on the same
> page but those are separate entity entries (8 ETH addresses on the page belong to
> Lazarus-adjacent entities, not Blender). Tags for Blender: [DPRK3] [CYBER2].
- **`primary_legal`**
  - URL: <https://home.treasury.gov/news/press-releases/jy0768>
  > Treasury press release "U.S. Treasury Issues First-Ever Sanctions on a Virtual Currency Mixer, Targets DPRK Cyber Threats" (2022-05-06).

## 2. Target

- **Kind**: `address_set`
- **Enumeration**: `complete`
- **Protocol**: `blender_io`
- **Actor name**: Blender.io
- **Chains**: `bitcoin`
- **Addresses**: 45 total (enumerated in event YAML)
- **Canonical domains**: `blender.io`, `blender.to`

> Full set of 45 unique Bitcoin addresses attached to the BLENDER.IO SDN entity entry,
> extracted verbatim from the OFAC Recent Actions page for 2022-05-06. Bitcoin-only target;
> no ETH or stablecoin addresses were designated for Blender. (The 8 ETH addresses also on
> the 2022-05-06 page belong to Lazarus-adjacent DPRK individual entries and are out of
> scope for this event.) All 45 addresses are Bitcoin P2SH format (3...).

## 3. Changed-layer observations (supports the scoped claim)

### l4_frontend · attribution: `plausible` · Δt = 251.6h

**Event label**: `canonical_frontend_stripped_to_default_nginx_by_operators`

**Timestamp**: `2022-05-16 11:37:13+00:00` (precision: `minute`)

**Sources**:

- **`semi_primary_wayback`**
  - URL: <https://web.archive.org/web/20220516113713/http://blender.io/>
  - body_hash: `sha256:e5e5eaae392f6c13af512e1000be2270a5b983fe5ca84457a3a0507a2cb31ad0`
  - body_path: `sources/http_captures/blender-ofac-2022/frontend-wayback/web.archive.org__web-20220516113713-http-blender.io__240e6c7838.html`
  > Wayback snapshot 10 days post-designation. 200 OK, 705-byte body carrying the default
> nginx welcome page verbatim ("Welcome to nginx! ... For online documentation and
> support please refer to nginx.org . Commercial support is available at nginx.com .
> Thank you for using nginx."). No Blender.io application content remains. Interpreted
> as operator-driven teardown: the Blender operators removed the mixer application
> from their own web server. attribution=plausible rather than direct because the OFAC
> designation did not itself require operators to take this action — this was a
> voluntary response by the service operator to US sanctions exposure (or to concurrent
> law-enforcement attention).
- **`primary_legal`**
  - URL: <https://home.treasury.gov/news/press-releases/jy0768>
  - Wayback: <https://web.archive.org/web/20260421234013/https://home.treasury.gov/news/press-releases/jy0768>
  - body_hash: `sha256:52cf5226e2f155aff279a140d5fc7555f1c0faddec59f77ecba48df5a70c35b4`
  - body_path: `sources/http_captures/blender-ofac-2022/press-release/home.treasury.gov__news-press-releases-jy0768__25ddcdc9ec.html`
  > Treasury press release "U.S. Treasury Issues First-Ever Sanctions on a Virtual
> Currency Mixer, Targets DPRK Cyber Threats" — primary_legal, anchors the
> US-government-attested disruption of Blender. The release explicitly names
> Blender.io as the target and describes the designation's intent to disrupt the
> service. Used as the second admission-grade source for the L4 observed_change
> claim (the Wayback nginx-default capture is the measurement; this is the legal
> attribution that the designation targeted Blender specifically).

## 5. Honest coverage gaps

- **l0_network** (`not_measured`): L0 network-layer OONI API query performed 2026-04-22. Searched the
- **offramp_cex** (`not_measured`): Chain-analytics anchors pinned 2026-04-22 as primary_corporate

## 7. Related events

- [`tornado-cash-ofac-2022`](./tornado-cash-ofac-2022.md)
- [`sinbad-ofac-2023`](./sinbad-ofac-2023.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `b71c00e`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

