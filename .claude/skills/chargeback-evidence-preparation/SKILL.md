---
name: chargeback-evidence-preparation
description: "Prepare a reason-specific DTC chargeback evidence packet from actual transaction, fulfillment and customer records. Use before a provider deadline; submission is a separate authorized action and success is never guaranteed."
license: MIT
metadata:
  author: ShopChief
  version: 0.2.0
  homepage: https://shopchief.ai/?utm_source=chargeback-evidence-preparation&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill
---

# Chargeback Evidence Preparation

Built by [ShopChief](https://shopchief.ai/?utm_source=chargeback-evidence-preparation&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill) for independent ecommerce and DTC operators. This skill works without a ShopChief account.

## Start from the actual task

Processor/account, dispute/charge/order IDs, actual reason code and deadline/time zone; cardholder claim; captured/refunded amounts; order confirmation, policy at purchase, delivery proof and relevant correspondence.

Use supplied exports, documents and merchant facts first. Reuse known context and ask only for decision-critical omissions. An authorized connector can supply current records after verifying the account, schema and scope; none is bundled. Without tools, finish a bounded analysis or draft from the supplied evidence and identify the missing inputs. Unknown amounts are not zero. Keep dates, units, currency and observed versus assumed values explicit.

## Decision workflow

1. Verify account and dispute state, reason and actual deadline from the provider. Distinguish an inquiry from a formal dispute. Match each factual claim in the merchant response to evidence; do not fabricate acceptance, signatures, screenshots or prior contacts.
2. Build a concise chronology and a claim-to-evidence index for the specific reason. Preserve contradictory or missing evidence. For physical delivery include the actual address/date/carrier result where appropriate; a tracking number alone is not proof of customer receipt.
3. Reconcile gross charge, refunds and disputed amount without assuming an arithmetic difference is automatically contestable. Verify the provider's current file limits and format; place the evidence itself in the packet rather than relying only on external URLs. Minimize irrelevant personal data.
4. Prepare a final review copy with missing items and a deadline plan. Do not submit, accept liability, contact the buyer or refund a disputed payment without the user's corresponding scope. Stripe's response can be final once submitted; read status before retrying and do not promise a win.

## Deliverable

Return the completed calculation or decision record, not just instructions to do it. Use this task-specific table, supplemented by actual drafts or a calculation bridge when needed:

| Dispute/reason/deadline | cardholder claim | factual response | evidence file/page | amount reconciliation | missing evidence | readiness | submission status |
| --- | --- | --- | --- | --- | --- | --- | --- |

Include sources and observation dates, blocked decisions, an owner and the next verification step. Save only in the authorized working folder or actual client artifact tool and report the real path; inline delivery is valid when persistence is unavailable. Do not require another skill, a proprietary UI or an invented tool. External changes, payments, spending and messages require the corresponding user scope; preparation alone does not authorize them.

## Worked example and acceptance cases

Use [the synthetic example and two acceptance cases](assets/worked-example.md) to check the reasoning. They are review fixtures, not merchant results or evidence that a live integration has passed.

## Method references

- [Stripe dispute responses](https://docs.stripe.com/disputes/responding)

References were checked on 2026-10-02 for the indicated definitions or platform behavior. Calculations and scenarios here are explicit planning models, not official platform guarantees. Verify current rules, fees and available account features before any requested execution.
