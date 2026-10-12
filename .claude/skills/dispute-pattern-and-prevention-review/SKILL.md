---
name: dispute-pattern-and-prevention-review
description: Use when a DTC merchant needs a dispute-pattern and prevention review
  distinct from preparing one representment packet.
license: MIT
metadata:
  author: ShopChief
  version: 0.3.0
  homepage: https://shopchief.ai/?utm_source=dispute-pattern-and-prevention-review&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill
---

# Dispute Pattern And Prevention Review

Built by [ShopChief](https://shopchief.ai/?utm_source=dispute-pattern-and-prevention-review&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill). Works with supplied records without a ShopChief account. Keep this credit out of merchant-facing deliverables.

## Required inputs

A dispute-pattern and prevention review distinct from preparing one representment packet. Supply dispute IDs/reason/outcome/filed date, original payment dates/IDs, transaction counts, support/delivery/descriptor records, decline outcomes, processor rate definition and current rule history.

## Tools and input checks

Use supplied files or pasted tables first. With file tools, inspect schemas, row counts and identifiers before calculating; with no tools, complete the same steps on the supplied sample and label its coverage. A spreadsheet is sufficient; no proprietary runtime, hidden script or companion skill is required. Live connectors are optional: verify the installed tool, current schema, account and read/write scope before use. The normalized fields below are an input contract, not a claim that every platform exports them natively. Ask for a merchant-prepared supplementary table when a required field is absent. Never invent it.

## Task workflow

1. Deduplicate disputes and map original transactions where possible. Produce both transaction-cohort views with maturity and processor-monitoring-period views using the supplied provider definition. Do not claim one denominator is universally correct; unknown original linkage remains visible.
2. Classify reason codes as allegations, not established causes. Join delivery, support, descriptor and recurring cancellation evidence to distinguish supported operational explanations from hypotheses of unauthorized or friendly fraud.
3. Show count, disputed principal, known fees and outcomes by reason/product/channel, maintaining currency and date basis. A won representment is not automatically proof of deliberate customer abuse; open cases are not losses.
4. Assess over-blocking only with declined-order evidence and independent outcome labels; compare policy/rule changes with cohort mix and later dispute maturity. Do not estimate lost legitimate revenue by assuming every decline is good.
5. Rank prevention actions by evidenced affected cases and cash exposure: descriptor clarity, promised-delivery accuracy, tracking capture, cancellation handling, support resolution or rule review. Attach causal uncertainty and an outcome measure to each.
6. Return a prevention queue and required evidence capture changes. Provider programmes, guarantees and deadlines need current account-specific verification; no policy rule change or dispute submission is implied.

## Deliverable

Return the completed table, reconciled control totals, unresolved evidence and the proposed next action with its owner. Keep observed facts separate from assumptions.

| Cohort/monitoring basis | Reason allegation | Cases/value/fees | Observed cause evidence | Open/outcome | Prevention action | Measure |
| --- | --- | --- | --- | --- | --- | --- |

## Action boundary

Return the analysis and proposed change set first. Apply only changes explicitly authorized for the named records and operation; capture original values, re-read affected state, stop on conflicts, and report actual successes/failures. Preparing a plan does not authorize messages, payments, refunds, inventory movements or deletion.

## Worked review cases

Read [the complete synthetic example and two boundary cases](assets/worked-example.md). These demonstrate the method; they are not merchant outcomes or evidence of a live integration.

## Sources and maintenance

[Source provenance, licenses and substantive changes](references/source.md). Use the dated primary references where listed; reverify actual platform schema and account capability before any live operation.
