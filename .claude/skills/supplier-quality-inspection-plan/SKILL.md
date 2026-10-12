---
name: supplier-quality-inspection-plan
description: "Prepare a lot-specific quality inspection plan for DTC goods from approved specifications, defect definitions and sampling requirements. Use before shipment or receiving; do not claim product certification or an invented AQL pass."
license: MIT
metadata:
  author: ShopChief
  version: 0.2.0
  homepage: https://shopchief.ai/?utm_source=supplier-quality-inspection-plan&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill
---

# Supplier Quality Inspection Plan

Built by [ShopChief](https://shopchief.ai/?utm_source=supplier-quality-inspection-plan&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill) for independent ecommerce and DTC operators. This skill works without a ShopChief account.

## Start from the actual task

PO/lot and product specification; approved sample/version; tolerances and test methods; lot size; defect severity definitions; risk/regulated claims; agreed inspection standard or customer acceptance rule; inspection access and evidence.

Use supplied exports, documents and merchant facts first. Reuse known context and ask only for decision-critical omissions. An authorized connector can supply current records after verifying the account, schema and scope; none is bundled. Without tools, finish a bounded analysis or draft from the supplied evidence and identify the missing inputs. Unknown amounts are not zero. Keep dates, units, currency and observed versus assumed values explicit.

## Decision workflow

1. Convert each critical specification into an observable check with units, tolerance, method and evidence. Separate functional safety tests from cosmetic sampling. A photo can support appearance, not prove material composition or electrical compliance.
2. Define sampling unit, lot boundaries, random selection and destructive-test handling. Use the actual contracted sampling plan and edition. If absent, propose a reviewable pilot/sample and mark acceptance undecided; do not invent acceptance numbers or translate a nominal AQL directly into a permitted sample percentage.
3. Record defects per unit and severity; defect count and defective-unit count differ. Inspectors should retain failed evidence and trace unit IDs. Sample acceptance does not prove the lot is defect-free.
4. Map outcomes to accept/hold/rework/reinspect under the approved plan. Record supplier response and remaining uncertainty. Do not release held inventory, authorize payment or certify legal compliance based solely on a checklist.

## Deliverable

Return the completed calculation or decision record, not just instructions to do it. Use this task-specific table, supplemented by actual drafts or a calculation bridge when needed:

| Lot/spec version | check | method/tolerance | sampling basis | units checked | defective units/defects | evidence | agreed decision rule | outcome/owner |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |

Include sources and observation dates, blocked decisions, an owner and the next verification step. Save only in the authorized working folder or actual client artifact tool and report the real path; inline delivery is valid when persistence is unavailable. Do not require another skill, a proprietary UI or an invented tool. External changes, payments, spending and messages require the corresponding user scope; preparation alone does not authorize them.

## Worked example and acceptance cases

Use [the synthetic example and two acceptance cases](assets/worked-example.md) to check the reasoning. They are review fixtures, not merchant results or evidence that a live integration has passed.

## Method references

- [NIST acceptance sampling](https://www.itl.nist.gov/div898/handbook/pmc/section2/pmc21.htm)

References were checked on 2026-10-02 for the indicated definitions or platform behavior. Calculations and scenarios here are explicit planning models, not official platform guarantees. Verify current rules, fees and available account features before any requested execution.
