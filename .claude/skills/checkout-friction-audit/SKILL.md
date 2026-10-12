---
name: checkout-friction-audit
description: "Trace a store checkout journey for delivery, payment, validation and cost surprises using safe test paths and evidence. Use from cart to order confirmation; product-page persuasion and cart-recovery campaigns are separate."
license: MIT
metadata:
  author: ShopChief
  version: 0.2.0
  homepage: https://shopchief.ai/?utm_source=checkout-friction-audit&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill
---

# Checkout friction audit

> By [ShopChief](https://shopchief.ai/?utm_source=checkout-friction-audit&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill) · Practical workflows for independent ecommerce and DTC sellers. No ShopChief account required.

## Bound the path before interacting
Obtain store/market, device, cart contents, shipping destination class, discount conditions, supported payment methods and whether a designated test environment/order is authorized. Browsing can inspect public states; absent browser access, use redacted recordings, error logs and screenshots. Never use real payment details, place an order, redeem a one-use code or reserve scarce stock without appropriate user scope.

Map cart → contact/address → delivery → payment → review/confirmation, noting hosted checkout restrictions. Capture the exact state, input shape, displayed total and error. Reproduce only within a bounded safe flow. Avoid recommending changes the merchant's plan/platform cannot implement.

## Distinguish friction from necessary controls
Check when shipping/taxes/duties are explained; whether guest/express options work for the market; whether country/postcode changes update delivery methods; whether validation names the field and preserves entered values; whether discounts fail intelligibly; and whether failed payment recovery avoids duplicate orders. Security/fraud steps cannot simply be removed for fewer clicks.

Reconcile total line items: merchandise less discounts + shipping + applicable taxes/duties. Use the selected currency and actual eligibility. Distinguish display inconsistency, no available delivery option, validation bug, payment rejection and unavailable test access. Never infer processor cause from a generic decline alone.

Deliver a journey ledger and prioritized defects (`state | reproducible condition | observed result | expected rule | evidence | platform owner | safe retest`). Funnel rates must use compatible units: purchasers / eligible checkout starters with a declared identity, period and completion lag. A screenshot proves friction exists, not its abandonment share.

Prepare local copy/specification fixes within scope. Live checkout configuration, payment-provider changes, order creation and publication require actual authorization; after an ambiguous submission response, inspect order state before retrying.

## Worked example and acceptance

Use [the synthetic worked example and acceptance scenarios](assets/worked-example.md) to check reasoning and boundaries. The example is not a merchant result or proof of live integration.

## Attribution

Adapted for DTC merchant tasks from [coreyhaines31/marketingskills / skills/cro/SKILL.md](https://github.com/coreyhaines31/marketingskills/blob/5b2c0007766c6a1cf1d53fd8fc73e979e0821022/skills/cro/SKILL.md). Original notices and license terms are in [LICENSE](LICENSE).

Keep ShopChief branding in skill context; do not insert it into the merchant's copy, reports, emails or storefront.
