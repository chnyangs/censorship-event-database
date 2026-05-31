# Evidence chain — `wikileaks-amazon-aws-eviction-2010-12`

**Status**: `admitted` · **Stratum**: `S5_corporate` · **Shape**: `comparison` (1 changed layer(s): `l4_frontend`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `e405eb6` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-21` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "On 2010-12-01, Amazon Web Services terminated WikiLeaks' EC2 / S3
> cloud-hosting account approximately 2 days after WikiLeaks had
> migrated to AWS to escape DDoS against its self-hosted infrastructure,
> following same-morning public pressure from Senator Joe Lieberman's
> office. AWS publicly grounded the termination in TOS violation and
> denied that the Lieberman contact prompted the decision.
> Observational axis at l4_frontend (cloud-hosting eviction).
> Discovery-only precedent for the corporate-intermediary censorship
> pattern; not eligible for the 2017+ comparable denominator."

## 1. Trigger

- **Type**: `corporate_policy_change`
- **Actor**: `AMAZON_AWS_OPERATOR`
- **Timestamp**: `2010-12-01 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_corporate`**
  - URL: <https://aws.amazon.com/message/65348/>
  - Wayback: <https://web.archive.org/web/2010/https://aws.amazon.com/message/65348/>
  > Amazon Web Services public message "WikiLeaks" (2010-12-02) stating
> WikiLeaks violated AWS terms of service ("you represent and warrant
> that you own or otherwise control all of the rights to the content
> ... that use of the content you supply does not violate this policy
> and will not cause injury to any person or entity"). The same
> statement denies that government inquiry or DDoS prompted the
> decision. Wayback wildcard pointer (web/2010/) in lieu of pinned
> snapshot; evidence_use=contextual_unarchived because no
> body_hash+body_path pair has been captured in this session.
- **`supporting_journalism`**
  - URL: <https://www.cnn.com/2010/US/12/01/wikileaks.amazon/index.html>
  - Wayback: <https://web.archive.org/web/2010/https://www.cnn.com/2010/US/12/01/wikileaks.amazon/index.html>
  > CNN 2010-12-01 reporting that Amazon dropped WikiLeaks after
> Senator Joe Lieberman's office contacted Amazon. Quotes Lieberman:
> "This morning Amazon informed my staff that it has ceased to host
> the WikiLeaks website." Wayback wildcard pointer in lieu of pinned
> snapshot.
- **`supporting_journalism`**
  - URL: <https://www.theregister.com/2010/12/01/wikileaks_disappers_from_amazon_us/>
  - Wayback: <https://web.archive.org/web/2010/https://www.theregister.com/2010/12/01/wikileaks_disappers_from_amazon_us/>
  > The Register 2010-12-01 reporting that WikiLeaks vanished from
> Amazon US EC2 hosting on the afternoon of 2010-12-01 following the
> Lieberman press release. Confirms the 2010-11-30 → 2010-12-01
> AWS-hosting window (WikiLeaks had migrated to AWS on Sunday
> 2010-11-28/29 after DDoS against its Swedish infrastructure).

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: WikiLeaks (Sunshine Press)
- **Canonical domains**: `wikileaks.org`, `cablegate.wikileaks.org`

> Single-target entity: WikiLeaks (wikileaks.org). WikiLeaks had migrated
> to Amazon EC2 / S3 hosting on or about 2010-11-28/29 after DDoS attacks
> against its self-hosted infrastructure (PRQ in Sweden). AWS terminated
> the WikiLeaks account approximately 2 days later on 2010-12-01.
> enumeration=subset because the specific AWS account identifiers and
> affected S3 buckets / EC2 instance IDs are not publicly enumerated.

## 3. Changed-layer observations (supports the scoped claim)

### l4_frontend · attribution: `plausible` · Δt = 0h

**Event label**: `wikileaks_account_terminated_from_amazon_aws_ec2_s3_hosting`

**Timestamp**: `2010-12-01 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_corporate`**
  - URL: <https://aws.amazon.com/message/65348/>
  - Wayback: <https://web.archive.org/web/20101203190043/http://aws.amazon.com/message/65348/>
  - body_hash: `sha256:0d7f1f8f509c9d4dbce3726d25078e49ae1a63ece43bcc269b047ec58abffe0d`
  - body_path: `sources/http_captures/wikileaks-amazon-aws-eviction-2010-12/primary/web.archive.org__web-20101203000000-https-aws.amazon.com-message-65348__517c15f209.html`
  > Amazon Web Services official statement ("WikiLeaks") explaining
> its 2010-12-01 termination of WikiLeaks hosting on AWS for AUP/terms
> violations. Iconic primary-corporate anchor (still live; Wayback
> 20101203190043 pinned).
- **`semi_primary_wayback`**
  - URL: <https://www.theregister.co.uk/2010/12/01/wikileaks_disappers_from_amazon_us/>
  - Wayback: <https://web.archive.org/web/20101203062456/http://www.theregister.co.uk/2010/12/01/wikileaks_disappers_from_amazon_us/>
  - body_hash: `sha256:bdc06e1dff16bd05b9fe94395749977cc01f3297c5b67a94998a6b76a818d2fa`
  - body_path: `sources/http_captures/wikileaks-amazon-aws-eviction-2010-12/primary/web.archive.org__web-20101202000000-http-www.theregister.co.uk-2010-12-01-wikileaks_disappers_from_amazon_us__d735e9558b.html`
  > The Register 2010-12-01 coverage of WikiLeaks' eviction from
> Amazon US hosting. Independent semi-primary anchor.
- **`semi_primary_wayback`**
  - URL: <https://www.cnn.com/2010/US/12/01/wikileaks.amazon/index.html>
  - Wayback: <https://web.archive.org/web/20101202040945/http://www.cnn.com/2010/US/12/01/wikileaks.amazon/index.html>
  - body_hash: `sha256:7fe56f12ed53641ccd916ebee1f6623bf60c6128dcf67dd2ad65e25b5fc3fab6`
  - body_path: `sources/http_captures/wikileaks-amazon-aws-eviction-2010-12/primary/web.archive.org__web-20101202000000-http-www.cnn.com-2010-US-12-01-wikileaks.amazon-index.html__8ba2fd3e9f.html`
  > CNN 2010-12-01 coverage confirming Amazon dropped WikiLeaks from
> its servers. Independent semi-primary anchor.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`wikileaks-everydns-domain-termination-2010-12`](./wikileaks-everydns-domain-termination-2010-12.md)
- [`apple-india-crypto-exchange-removal-2024-01`](./apple-india-crypto-exchange-removal-2024-01.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `e405eb6`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

