# External Benchmark Crosswalk

Status as of 2026-05-07: reviewer-facing crosscheck plan.

This artifact records how adjacent censorship, sanctions, and transparency
measurement work should be used to sanity-check the corpus. It is not an
additional admission source and it does not change the six-artifact
measurement protocol. Its job is to make external validity checks explicit:
what each benchmark can validate, what it cannot validate, and how its
denominator differs from this event-level database.

Machine-readable source: [`benchmark_crosswalk.yaml`](benchmark_crosswalk.yaml).

## Crosswalk

| Benchmark | What to borrow | Project crosscheck | Denominator boundary |
| --- | --- | --- | --- |
| [OONI Explorer](https://explorer.ooni.org/) / [OONI](https://ooni.org/) | Open network measurements, probe/test metadata, anomaly vs blocking distinction | Backfill L0 query scope, measurement count, country/ASN, and no-data status | No OONI measurements means no L0 denominator, not observed no-change |
| [Censored Planet](https://docs.censoredplanet.org/index.html) | Longitudinal remote reachability baselines and false-positive controls | Compare pre/post reachability windows for public domains before promoting L0/L4 claims | Reachability drift does not prove legal-trigger attribution |
| [Tornado Cash sanctions event-study literature](https://www.snb.ch/en/publications/research/working-papers/2024/working_paper_2024_09) | Event-study windowing, persistence/recovery framing, settlement-layer cooperation checks | Use Tornado-family findings as an external sanity check for anchor cases | Single-case flow metrics cannot become cross-case or cross-layer denominators |
| [MEV Watch](https://www.mevwatch.info/) | OFAC-compliant mev-boost relay/block exposure metrics | Check L1 Tornado-family rows against relay-policy exposure windows | Relay share is not event-specific transaction censorship and does not cover other layers |
| [Chainalysis sanctions reporting](https://www.chainalysis.com/blog/tornado-cash-ofac-designation-sanctions/) + [Lumen-style transparency databases](https://lumendatabase.org/pages/about?ResourceID=31) | Entity normalization, notice provenance, redaction/source-limit discipline | Improve legal actor / target / address / domain / exchange normalization and transparency language | Proprietary or redacted intelligence is supporting context, not a sole replayable admission anchor |

## Integration Rules

Use these benchmarks as external checks, not as substitutes for local evidence:

- A benchmark can strengthen an evidence chain only when the event YAML still
  contains a replayable public source, archive/hash, and scoped claim.
- A benchmark can downgrade a claim when it exposes missing denominator,
  baseline ambiguity, target drift, or attribution overreach.
- A benchmark cannot create a denominator for an unmeasured layer. It can only
  document why that layer is measured, partially measured, or not measured.
- Proprietary intelligence and compliance reports are discovery/supporting
  material unless the relevant claim is public, replayable, and source-class
  admissible under `docs/methodology.md`.

## Concrete Improvements To Apply

1. **L0 and L4 baseline check**: for domain-bearing cases, record whether OONI
   or Censored Planet has a T-14/T+14 measurement window. If not, leave the
   denominator as a measurement gap.
2. **Tornado-family sanity check**: compare our Tornado cases against external
   event-study claims on transaction volume, user diversity, and settlement
   cooperation, but keep stack-layer observations separate from economic-flow
   findings.
3. **L1 relay exposure check**: use MEV Watch / Wahrstätter-style data to
   verify the direction and window of relay-policy exposure before promoting
   L1 claims.
4. **Entity-resolution discipline**: split legal actor, legal entity, service
   name, domain, address, contract, and exchange fields where possible; do not
   let one label stand for all of them.
5. **Transparency language**: copy Lumen-style caveats into audit/release notes
   when a source is redacted, incomplete, self-reported, or proprietary.

## Reviewer Use

For each promoted paper claim, ask:

- Which external benchmark is relevant, if any?
- Does that benchmark validate the layer, only the context, or neither?
- Does the benchmark denominator match the denominator used in our table?
- If the benchmark contradicts or weakens the claim, is the event re-scoped,
  downgraded, or sent to human audit?

If those answers are not explicit, the claim is not ready for A-class
submission framing.
