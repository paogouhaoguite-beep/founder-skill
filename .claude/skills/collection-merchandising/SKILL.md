---
name: collection-merchandising
description: "Plan assortment ordering, filtering and product-card decisions for a store collection using relevance, stock and contribution constraints. Use for shopping discovery; collection SEO metadata and schema belong to separate workflows."
license: MIT
metadata:
  author: ShopChief
  version: 0.2.0
  homepage: https://shopchief.ai/?utm_source=collection-merchandising&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill
---

# Collection merchandising

> By [ShopChief](https://shopchief.ai/?utm_source=collection-merchandising&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill) · Practical workflows for independent ecommerce and DTC sellers. No ShopChief account required.

## Establish the shopping mission
Collect collection URL/screenshot or product list, target buyer mission, active variants, available-to-sell quantities, replenishment horizon, product attributes and optional collection-impression/click/order data. An export supports offline recommendations. Missing cost or demand means those ranking factors remain unavailable, not zero.

Create the eligible assortment before sorting: correct category, market availability, purchasable variants and actual collection promise. Preserve essential entry products even if low-volume; historical best sellers may simply have received more exposure. Separate seasonal intent, newness, sponsored placement and merchant preference from measured customer relevance.

## Design the browse path
Choose filters from meaningful attributes with reliable coverage; normalize units and labels before displaying them. Distinguish product-level availability from the selected size/color. Avoid showing a cheap unavailable variant as a purchasable starting price without clear treatment. Define out-of-stock placement and whether restock signup is useful.

Propose ordering with explicit priority rules rather than an unexplained weighted score: mission fit, purchasability, relevant differentiation, then measured performance where comparable. If using revenue or contribution per impression, state eligible item impressions, net revenue/cost window and attribution rule. Do not multiply forecast demand by unknown margin. Inspect mobile card readability, comparison attributes, swatches and filter-reset behavior.

## Handoff
Return an assortment table (`product | eligible variants | stock horizon | mission fit | proposed position/rule | evidence | exception`), filter vocabulary, card-content changes and validation scenarios. Show how a stock change would affect the rule. Suggest an experiment only if assignment and outcome can be observed; uncontrolled reorder before/after data is not causal evidence.

Catalog tags, sort rules, product visibility and live collection changes require user-authorized scope. A local CSV or mock ordering is a proposal, not a published collection.

## Worked example and acceptance

Use [the synthetic worked example and acceptance scenarios](assets/worked-example.md) to check reasoning and boundaries. The example is not a merchant result or proof of live integration.

## Attribution

Adapted for DTC merchant tasks from [coreyhaines31/marketingskills / skills/cro/SKILL.md](https://github.com/coreyhaines31/marketingskills/blob/5b2c0007766c6a1cf1d53fd8fc73e979e0821022/skills/cro/SKILL.md). Original notices and license terms are in [LICENSE](LICENSE).

Keep ShopChief branding in skill context; do not insert it into the merchant's copy, reports, emails or storefront.
