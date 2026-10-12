---
name: review-request-workflow
description: "Design a neutral post-purchase review request and suppression workflow using delivery status, permission and existing reviews. Use for collection operations; it does not mine existing reviews or generate customer testimonials."
license: MIT
metadata:
  author: ShopChief
  version: 0.2.0
  homepage: https://shopchief.ai/?utm_source=review-request-workflow&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill
---

# Review request workflow

> By [ShopChief](https://shopchief.ai/?utm_source=review-request-workflow&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill) · Practical workflows for independent ecommerce and DTC sellers. No ShopChief account required.

## Anchor requests to a real experience
Read the review destination, store markets, order and delivery event definitions, product use period, message permissions and available email/SMS/review tooling. Ask only for missing decisions that change eligibility. Build from redacted exports offline if no connector exists; do not claim an active automation.

Model states: order paid → fulfilled → delivered/confirmed received → experience window elapsed → eligible → requested → reviewed or expired. Delivery delays should move eligibility rather than trigger a fixed order-date blast. Choose the experience window from the product and merchant policy, not a universal day count.

## Eligibility and neutral treatment
Apply consent/contact permission, unsubscribes, invalid addresses, duplicate requests and already-reviewed suppression before scheduling. Separate service-resolution messages from public review solicitation. Do not route happy customers to a public review site while hiding the same option from unhappy customers. Never ask specifically for five stars, prefill praise or condition a benefit on sentiment. Check the destination's current policies before proposing any incentive.

Use an idempotency key such as order + product + destination + campaign revision. Define behavior for refunded, partially delivered and multi-item orders; do not infer that a refund invalidates the customer's experience. A retry must check the send/request record first. Cap follow-ups according to the merchant's actual policy, with stop conditions for reply, review, unsubscribe or complaint.

## Deliver the operating artifact
Provide an eligibility decision table, event/state diagram in text, field mapping, message drafts, suppression rules and a QA ledger. Draft a neutral request with product context, honest-feedback invitation and the actual review URL; no fabricated personalized use claim.

Report request coverage as eligible customers requested / eligible customers in a fixed cohort, delivery rate as delivered messages / sent messages, and observed review response as attributable new reviews / delivered requests within the stated window. Keep organic reviews and unknown attribution separate. Do not call all reviews incremental. Importing contacts, enabling an automation and sending requests require explicit user scope and account authorization.

## Worked example and acceptance

Use [the synthetic worked example and acceptance scenarios](assets/worked-example.md) to check reasoning and boundaries. The example is not a merchant result or proof of live integration.

## Attribution

Adapted for DTC merchant tasks from [coreyhaines31/marketingskills / skills/customer-research/SKILL.md](https://github.com/coreyhaines31/marketingskills/blob/5b2c0007766c6a1cf1d53fd8fc73e979e0821022/skills/customer-research/SKILL.md); [coreyhaines31/marketingskills / skills/emails/SKILL.md](https://github.com/coreyhaines31/marketingskills/blob/5b2c0007766c6a1cf1d53fd8fc73e979e0821022/skills/emails/SKILL.md). Original notices and license terms are in [LICENSE](LICENSE).

Keep ShopChief branding in skill context; do not insert it into the merchant's copy, reports, emails or storefront.
