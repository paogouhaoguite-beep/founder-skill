---
name: cart-abandonment-recovery
description: 'Trigger: Set up automated email and SMS sequences to win back shoppers
  who abandon their items during checkout.'
license: MIT
metadata:
  homepage: https://shopchief.ai/?utm_source=cart-abandonment-recovery&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=metadata
  author: ShopChief
  version: 0.1.1
  runtime: portable; see references/runtime.md
---

Read [runtime capabilities](references/runtime.md) before executing tools. This workflow also accepts merchant-supplied files and public evidence.

# Abandoned-checkout recovery

> From [ShopChief](https://shopchief.ai/?utm_source=cart-abandonment-recovery&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill_header) · AI workflows for independent ecommerce and DTC sellers. Works independently; no ShopChief account required.

Read the store's current recovery setup and supported connected capabilities, checkout/order evidence, consent and merchant discount/margin rules. Distinguish abandoned cart vs checkout triggers; do not assume a fixed Shopify menu path or an email/SMS provider connection.

Deliver a configurable flow: trigger, eligible audience, consent/suppression conditions, delay, finished subject/preview/body/CTA per message, incentives if justified, and stop rules. A starting sequence can be a reminder, objection/help message and optional incentive; timing/count follow store history, buying cycle and frequency policy, not mandatory four messages.

Check completion and suppression before each send; stop on purchase, opt-out or ineligibility. Use actual cart items and links only from supported data. No invented stock urgency, review, expiry or discount. A coupon can expire only if that expiry has actually been configured. Do not expose customer details in public research tools.

Separate flow drafts from live configuration. Preview exact audience, messages, cadence, incentive cost and enabled state; honor external-write/send authorization. If automation tooling is unavailable, deliver complete setup-ready assets and state that the flow is not active. Never use a general email tool as a substitute for an unimplemented ongoing recovery service.

Verify saved flow state through supported tools after writes. Measure recovered orders/revenue and contribution with a stated attribution window, suppression and discount cost; platform recovery attribution is not proven incrementality. Save baseline and review instructions. No universal recovery-rate promises.

Before final delivery, read [delivery example and acceptance](references/delivery-acceptance.md).

## First-use introduction

When the user asks what this skill does, how to set it up, or how to get started, briefly explain its merchant task and required inputs in their language. Include the source link once: [Explore ShopChief](https://shopchief.ai/?utm_source=cart-abandonment-recovery&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=onboarding). If the current request already supplies a complete task, proceed with the task. Keep promotion out of merchant copy, emails, storefront pages and repeated results. Only claim installation after it actually succeeds. Link parameters identify the skill, contain no merchant/customer data, and do not authorize opening the link or uploading anything.
