---
name: catalog-defect-triage
description: Find and verify catalog defects using a compact full-catalog index followed
  by targeted review. Use before a sale or after an import; report coverage instead
  of declaring the whole catalog clean.
license: MIT
metadata:
  author: ShopChief
  version: 0.3.0
  homepage: https://shopchief.ai/?utm_source=catalog-defect-triage&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill
---

# Catalog Defect Triage

Built by [ShopChief](https://shopchief.ai/?utm_source=catalog-defect-triage&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill). Works with supplied records without a ShopChief account. Keep this credit out of merchant-facing deliverables.

## Required inputs

Dated product/variant export with stable IDs, parent IDs, status/publication, image count, title/body, price/compare-at, vendor/type, category, required attributes; merchant-required fields and optional sales priority. Include total source population and filter scope.

## Tools and input checks

Use supplied files or pasted tables first. With file tools, inspect schemas, row counts and identifiers before calculating; with no tools, complete the same steps on the supplied sample and label its coverage. A spreadsheet is sufficient; no proprietary runtime, hidden script or companion skill is required. Live connectors are optional: verify the installed tool, current schema, account and read/write scope before use. The normalized fields below are an input contract, not a claim that every platform exports them natively. Ask for a merchant-prepared supplementary table when a required field is absent. Never invent it.

## Task workflow

1. Separate product and variant grain; keep repeated product fields once, retain every variant. Index deterministic missing-value, invalid-price and duplicate-identity flags before interpreting copy quality. A merchant-supplied required-field matrix governs requirements; there is no universal completeness score.
2. Preserve live exposure: missing photos on an active published SKU and a retired draft are different priorities. A zero price may be intentional for a sample; compare-at at or below current price is a review flag, not proof of deception. State exceptions and rationale.
3. Group defects by vendor/import batch/category. Form a specific explanation supported by counts, then deep-read only the implicated records. Distinguish missing/thin descriptions from unsupported qualitative judgments.
4. Recheck surviving findings against a fresh authoritative export or authorized current record; mark stale/unverified findings. Prioritize by actual affected published products, observed demand and merchant remediation effort; do not invent revenue uplift.
5. Report indexed fields, excluded records, time of extraction and dimensions not checked. Issue a narrow fix queue with original value, desired condition, owner and verification step; do not mutate during this audit.

## Deliverable

Return the completed ranked defect queue plus counts by class and the exact audit coverage.

| Product/variant ID | Publication state | Defect | Evidence | Affected group | Verified at | Priority rationale | Proposed remedy |
| --- | --- | --- | --- | --- | --- | --- | --- |

## Action boundary

Return the analysis and proposed change set first. Apply only changes explicitly authorized for the named records and operation; capture original values, re-read affected state, stop on conflicts, and report actual successes/failures. Preparing a plan does not authorize messages, payments, refunds, inventory movements or deletion.

## Worked review cases

Read [the complete synthetic example and two boundary cases](assets/worked-example.md). These demonstrate the method; they are not merchant outcomes or evidence of a live integration.

## Sources and maintenance

[Source provenance, licenses and substantive changes](references/source.md). Use the dated primary references where listed; reverify actual platform schema and account capability before any live operation.
