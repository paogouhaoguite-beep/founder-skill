---
name: demand-forecasting
description: "Build and back-check short-horizon DTC unit-demand forecasts from sales, availability and events. Use for forecast ranges and uncertainty, not a purchase quantity or guaranteed revenue prediction."
license: MIT
metadata:
  author: ShopChief
  version: 0.2.0
  homepage: https://shopchief.ai/?utm_source=demand-forecasting&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill
---

# Demand Forecasting

Built by [ShopChief](https://shopchief.ai/?utm_source=demand-forecasting&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill) for independent ecommerce and DTC operators. This skill works without a ShopChief account.

## Start from the actual task

Daily/weekly SKU units with dates; time zone and complete periods; cancellations/returns definition; stock availability; promotions, price changes and launches; forecast horizon and error costs.

Use supplied exports, documents and merchant facts first. Reuse known context and ask only for decision-critical omissions. An authorized connector can supply current records after verifying the account, schema and scope; none is bundled. Without tools, finish a bounded analysis or draft from the supplied evidence and identify the missing inputs. Unknown amounts are not zero. Keep dates, units, currency and observed versus assumed values explicit.

## Decision workflow

1. Build a regular time index. Separate missing records, genuine zero demand and stockout-censored sales. Keep booked demand separate from net units after returns; returns are not automatically negative future demand.
2. Start with last-period, moving-average or seasonal-naive baselines appropriate to observed history. Sparse launch data supports scenarios; it does not establish annual seasonality. Do not fit on future periods or use a promotion result known only after the prediction date.
3. Compare candidates with rolling-origin holdouts at the intended horizon. Report MAE in units and bias with an explicit sign (actual minus forecast). MAPE is undefined at zero actuals. WAPE = sum absolute errors / sum actuals is usable only with a nonzero, nonnegative denominator and is not a per-SKU fairness measure.
4. Keep event lifts as explicit assumptions until supported. Show forecast uncertainty separately from inventory buffers and procurement decisions. Report historical interval coverage if measured; do not label a handmade low/base/high range a calibrated prediction interval.

## Deliverable

Return the completed calculation or decision record, not just instructions to do it. Use this task-specific table, supplemented by actual drafts or a calculation bridge when needed:

| SKU | origin | horizon | baseline/method | point units | interval/scenario | holdout count | MAE/bias | stockout treatment | limitations |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Include sources and observation dates, blocked decisions, an owner and the next verification step. Save only in the authorized working folder or actual client artifact tool and report the real path; inline delivery is valid when persistence is unavailable. Do not require another skill, a proprietary UI or an invented tool. External changes, payments, spending and messages require the corresponding user scope; preparation alone does not authorize them.

## Worked example and acceptance cases

Use [the synthetic example and two acceptance cases](assets/worked-example.md) to check the reasoning. They are review fixtures, not merchant results or evidence that a live integration has passed.

## Method references

- [Forecast evaluation, Forecasting: Principles and Practice](https://otexts.com/fpp3/accuracy.html)
- [Shopify inventory states](https://help.shopify.com/en/manual/products/inventory/fundamentals/inventory-states)

References were checked on 2026-10-02 for the indicated definitions or platform behavior. Calculations and scenarios here are explicit planning models, not official platform guarantees. Verify current rules, fees and available account features before any requested execution.
