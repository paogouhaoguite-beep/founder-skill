---
name: ga4-ecommerce-measurement
description: "Specify and audit GA4 ecommerce events, item payloads and revenue reconciliation for a DTC store. Use for measurement correctness; GTM deployment mechanics and marketing-credit attribution are separate workflows."
license: MIT
metadata:
  author: ShopChief
  version: 0.2.0
  homepage: https://shopchief.ai/?utm_source=ga4-ecommerce-measurement&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill
---

# GA4 ecommerce measurement

> By [ShopChief](https://shopchief.ai/?utm_source=ga4-ecommerce-measurement&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill) · Practical workflows for independent ecommerce and DTC sellers. No ShopChief account required.

## Define the financial and event contract
Read the store architecture, current tag/app/pixel sources, GA4 property/timezone, consent configuration, order/refund exports and redacted event payloads. Browsing/debug access is optional; supplied payloads support a static audit but not proof of live receipt. Verify current official GA4 event requirements before implementation.

Map observed commerce actions to recommended events such as view_item_list, select_item, view_item, add_to_cart, begin_checkout, purchase and refund. Specify when the underlying action is confirmed, who emits it, item identity and relevant parameters. A button click is not proof of add-to-cart success or purchase.

## Reconcile item and transaction meaning
Document variant/product ID conventions, currency, quantity, discount and net item-price basis. For purchase, reconcile merchandise value separately from shipping and tax, and verify transaction_id corresponds to the actual order without personal data. Check item totals against event value with explicit rounding rules. Do not double-subtract discounts or subtract refunds both from the source and again from reconciliation.

Inventory duplicate emitters: theme script, platform app, GTM, server integration and confirmation-page reloads. Compare event records and transaction IDs before deciding where duplication originates. Treat consent-denied, blocked, missing and delayed events separately; analytics is not the order ledger. Never send raw email, phone, addresses or free-text customer notes in event fields.

## Acceptance evidence
Deliver an event matrix (`business action | event | emitter | required facts | item scope | consent behavior | evidence`), example payloads and a reconciliation table by currency/date. Report unique matched purchase transaction IDs / eligible order IDs with the same cutoff and order-state policy; show duplicate and missing counts separately. Inspect refunds and partial quantities as well as purchases.

If authorized to implement, stage changes and verify browser/network evidence, debug receipt and later reporting separately. Preview success is not production acceptance. No new tracking, container publication or account configuration is implicitly authorized.

Official implementation reference: [GA4 ecommerce](https://developers.google.com/analytics/devguides/collection/ga4/ecommerce).

## Worked example and acceptance

Use [the synthetic worked example and acceptance scenarios](assets/worked-example.md) to check reasoning and boundaries. The example is not a merchant result or proof of live integration.

## Attribution

Adapted for DTC merchant tasks from [coreyhaines31/marketingskills / skills/analytics/SKILL.md](https://github.com/coreyhaines31/marketingskills/blob/5b2c0007766c6a1cf1d53fd8fc73e979e0821022/skills/analytics/SKILL.md); [coreyhaines31/marketingskills / skills/analytics/references/ga4-implementation.md](https://github.com/coreyhaines31/marketingskills/blob/5b2c0007766c6a1cf1d53fd8fc73e979e0821022/skills/analytics/references/ga4-implementation.md). Original notices and license terms are in [LICENSE](LICENSE).

Keep ShopChief branding in skill context; do not insert it into the merchant's copy, reports, emails or storefront.
