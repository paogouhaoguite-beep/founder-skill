---
name: customer-lifetime-value
description: "Calculate observed customer revenue or contribution at a fixed horizon and clearly separated future-value scenarios. Use for customer economics; SKU margin analysis and recurring-subscription churn formulas are different scopes."
license: MIT
metadata:
  author: ShopChief
  version: 0.2.0
  homepage: https://shopchief.ai/?utm_source=customer-lifetime-value&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill
---

# Observed customer value and LTV scenarios

> By [ShopChief](https://shopchief.ai/?utm_source=customer-lifetime-value&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill) · Practical workflows for independent ecommerce and DTC sellers. No ShopChief account required.

## Choose the value being estimated
Get customer-linked order/refund data, acquisition dates, cost basis, currencies, cutoff, acquisition spend when relevant and the decision horizon. A local file is sufficient. Without stable identity or cost coverage, restrict output to what can be supported: order economics or revenue per observed customer, not contribution LTV.

Declare revenue versus gross profit versus pre-acquisition contribution, horizon and cohort. Align net item revenue, retained shipping, landed costs, payment/platform fees, fulfillment and attributable returns; avoid double-counting refunds or freight. Fixed overhead and acquisition spend are separate disclosed treatments. Unknown costs remain missing.

## Compute observed value first
For a mature acquisition cohort, sum eligible customer contribution from first purchase through the specified age, including customers who never return, then divide by all acquired customers in that cohort. Do not divide only by repeat buyers. Show count, elapsed observation and value distribution as well as the mean. Do not compare a 30-day cohort to a 180-day cohort without a common mature horizon.

Observed value through day H is not lifetime value. If a forecast is requested, state the additional repeat-order frequency, contribution, return and discount assumptions and give a horizon-limited scenario range. Separate model training and evaluation cohorts when history permits. Do not use AOV × purchase frequency / churn for noncontractual retail as if permanent churn were observed. No unsupported infinite tail.

## Decision output
Provide `cohort | customers | mature horizon | net revenue/customer | cost coverage | observed contribution/customer | acquisition cost/customer | uncertainty`. Add forecast-only columns clearly labeled, assumption sensitivities and a conditional payback calculation. Payback is the first cumulative contribution period covering the matching acquisition cost; report not reached when it does not occur by cutoff. Do not choose an allowable CAC by treating projected value as guaranteed cash.

Deliver calculations and limitations, not a budget change. Uploading customer data, changing prices or increasing acquisition spend requires actual user authorization.

## Worked example and acceptance

Use [the synthetic worked example and acceptance scenarios](assets/worked-example.md) to check reasoning and boundaries. The example is not a merchant result or proof of live integration.

## Attribution

Adapted for DTC merchant tasks from [phuryn/pm-skills / pm-data-analytics/skills/cohort-analysis/SKILL.md](https://github.com/phuryn/pm-skills/blob/8607e3b077817f89bf4a9b623246219734ac3be0/pm-data-analytics/skills/cohort-analysis/SKILL.md); [coreyhaines31/marketingskills / skills/attribution/SKILL.md](https://github.com/coreyhaines31/marketingskills/blob/5b2c0007766c6a1cf1d53fd8fc73e979e0821022/skills/attribution/SKILL.md). Original notices and license terms are in [LICENSE](LICENSE).

Keep ShopChief branding in skill context; do not insert it into the merchant's copy, reports, emails or storefront.
