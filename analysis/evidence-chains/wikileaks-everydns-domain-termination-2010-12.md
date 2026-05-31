# Evidence chain — `wikileaks-everydns-domain-termination-2010-12`

**Status**: `admitted` · **Stratum**: `S5_corporate` · **Shape**: `comparison` (1 changed layer(s): `l4_frontend`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `e2fc5d2` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-21` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> EveryDNS terminated authoritative DNS service for wikileaks.org at
> ~22:00 EST 2010-12-02 under its TOS clause prohibiting service use
> that interferes with other members', citing DDoS traffic against
> the wikileaks.org records; the termination produced worldwide DNS
> unreachability of wikileaks.org until the relocation to
> wikileaks.ch the following day. The L4-frontend layer carries the
> load-bearing direct-attribution observation; this is the
> foundational pre-crypto DNS-layer corporate-intermediary censorship
> precedent in the corpus.

## 1. Trigger

- **Type**: `corporate_policy_change`
- **Actor**: `EVERYDNS_OPERATOR`
- **Timestamp**: `2010-12-02 22:00:00+00:00` (precision: `hour`)

### Trigger citations

- **`primary_corporate`**
  - URL: <http://everydns.com/>
  - Wayback: <https://web.archive.org/web/2010/http://everydns.com/>
  > EveryDNS public statement of 2010-12-02 terminating free DNS
> service for wikileaks.org within 24 hours of notice, citing the
> EveryDNS Terms of Service clause that "Member shall not
> interfere with another Member's use and enjoyment of the
> Service or another entity's use and enjoyment of similar
> services." EveryDNS cited DDoS attacks against the wikileaks.org
> DNS records that "threatened the stability of EveryDNS.net's
> infrastructure" supporting ~500,000 other domains. The
> termination took effect at 2010-12-02 ~22:00 EST (per the
> EveryDNS statement specifying a 24-hour notice ending 22:00 EST
> on 2010-12-02). DRYRUN: pinned Wayback snapshot and body_hash
> for the EveryDNS statement page are deferred to the human-audit
> pass; marked evidence_use=contextual_unarchived per validator
> policy for unarchived sources.
- **`supporting_journalism`**
  - URL: <https://www.theregister.com/2010/12/03/wikileaks_loses_dns/>
  - Wayback: <https://web.archive.org/web/2010/https://www.theregister.com/2010/12/03/wikileaks_loses_dns/>
  > The Register contemporaneous coverage (2010-12-03) "Wikileaks'
> DNS pulls plug, citing collateral DDoS damage" naming EveryDNS
> as the terminating DNS provider, the TOS clause invoked, and
> the ~22:00 EST 2010-12-02 cutoff. Triangulation source for
> actor (EveryDNS), mechanism (DNS service termination at the
> authoritative free-DNS provider for wikileaks.org), and
> hour-level timing. DRYRUN: pinned Wayback snapshot deferred to
> human audit.
- **`supporting_journalism`**
  - URL: <https://thenextweb.com/news/wikileaks-is-reportedly-down-worldwide-as-dns-services-pulled>
  - Wayback: <https://web.archive.org/web/2010/https://thenextweb.com/news/wikileaks-is-reportedly-down-worldwide-as-dns-services-pulled>
  > The Next Web contemporaneous coverage (2010-12-02/03) reporting
> the worldwide unreachability of wikileaks.org following the
> EveryDNS termination, and WikiLeaks' own Twitter
> acknowledgment that the domain had been "killed by U.S.
> EveryDNS.net after claimed mass attacks." Independent
> confirmation of the public visibility and effect of the DNS
> termination. DRYRUN: pinned Wayback snapshot deferred to
> human audit.
- **`supporting_journalism`**
  - URL: <https://thenextweb.com/media/2010/12/03/wikileaks-resolves-dns-moves-to-switzerland/>
  - Wayback: <https://web.archive.org/web/2010/https://thenextweb.com/media/2010/12/03/wikileaks-resolves-dns-moves-to-switzerland/>
  > The Next Web follow-up (2010-12-03) documenting that wikileaks.org
> was relocated to wikileaks.ch (Swiss Pirate Party-hosted) and
> other mirrors within ~24 hours of the EveryDNS termination.
> Establishes the L4-frontend / domain-takedown effect and the
> immediate mirror-network response. DRYRUN: pinned Wayback
> snapshot deferred to human audit.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: WikiLeaks (wikileaks.org domain)
- **Canonical domains**: `wikileaks.org`

> Canonical target is the wikileaks.org domain (DNS authoritative-
> service relationship at EveryDNS), terminated 2010-12-02. Subset
> enumeration because the EveryDNS action removed authoritative DNS
> for the wikileaks.org domain only (the WikiLeaks organizational
> entity hosted content across multiple infrastructure providers in
> 2010-11/12; this row captures the DNS-provider termination
> specifically, sibling to the Amazon AWS eviction recorded under
> wikileaks-amazon-aws-eviction-2010-12).

## 3. Changed-layer observations (supports the scoped claim)

### l4_frontend · attribution: `plausible` · Δt = 0h

**Event label**: `everydns_terminated_authoritative_dns_for_wikileaks_org_under_tos`

**Timestamp**: `2010-12-02 22:00:00+00:00` (precision: `hour`)

**Sources**:

- **`semi_primary_wayback`**
  - URL: <https://www.theregister.co.uk/2010/12/03/wikileaks_loses_dns/>
  - Wayback: <https://web.archive.org/web/20101204054939/http://www.theregister.co.uk/2010/12/03/wikileaks_loses_dns/>
  - body_hash: `sha256:65efe345e934bf4d05e9e9b6f96332c23b67865960fbf8e783817da00416b083`
  - body_path: `sources/http_captures/wikileaks-everydns-domain-termination-2010-12/primary/web.archive.org__web-20101204000000-http-www.theregister.co.uk-2010-12-03-wikileaks_loses_dns__3de29cd81a.html`
  > The Register 2010-12-03 coverage of EveryDNS terminating
> wikileaks.org authoritative DNS (effective 2010-12-02 23:00 EST),
> citing DDoS-driven ToS violation. Independent semi-primary anchor.
> The agent-drafted everydns.com homepage primary URL was non-archivable;
> attribution downgraded direct->plausible (no archived EveryDNS
> statement pinned).
- **`semi_primary_wayback`**
  - URL: <https://thenextweb.com/media/2010/12/03/wikileaks-resolves-dns-moves-to-switzerland/>
  - Wayback: <https://web.archive.org/web/20101204140314/http://thenextweb.com/media/2010/12/03/wikileaks-resolves-dns-moves-to-switzerland/>
  - body_hash: `sha256:718e6dcbb245bccfccf694780b3a66c2a02df596b529d3c57e0c9afc367113df`
  - body_path: `sources/http_captures/wikileaks-everydns-domain-termination-2010-12/primary/web.archive.org__web-20101204000000-http-thenextweb.com-media-2010-12-03-wikileaks-resolves-dns-moves-to-switzerland__7adb278f4a.html`
  > The Next Web 2010-12-03 coverage confirming the EveryDNS
> termination and WikiLeaks' relocation to the Swiss wikileaks.ch domain.
> Independent second semi-primary anchor.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`wikileaks-amazon-aws-eviction-2010-12`](./wikileaks-amazon-aws-eviction-2010-12.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `e2fc5d2`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

