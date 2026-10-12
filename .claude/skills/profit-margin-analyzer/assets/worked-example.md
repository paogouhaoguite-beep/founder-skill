# Worked example: where did the order margin go?

This is a synthetic merchant exercise. The [CSV](orders.csv) is invented; the [calculator output](expected-report.json) is produced by the bundled script. Amounts are USD for one synthetic month. It is not a customer result or an agent performance benchmark.

## Input and calculation

Revenue is already net of discounts/refunds, excludes collected tax, and includes retained shipping separately. Return handling costs exclude refunded revenue already deducted. Landed cost excludes outbound fulfillment to avoid double counting.

| SKU | Orders | Revenue + retained shipping | Landed cost | Fees | Fulfillment | Return costs | Ads | Pre-ad contribution | Post-ad contribution |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| DEMO-POUCH | 10 | 1,000 | 400 | 40 | 140 | 20 | 250 | 400 | 150 |
| DEMO-BOTTLE | 20 | 840 | 360 | 32 | 180 | 28 | 160 | 240 | 80 |

The pouch: `1000 − (400 + 40 + 140 + 20) = 400` before ads, then `400 − 250 = 150` after ads. The bottle: `840 − (360 + 32 + 180 + 28) = 240`, then `240 − 160 = 80`. Combined contribution after ads is USD 230 for this same-currency, same-period fixture.

## Merchant interpretation

The pouch contributes USD 15 per order after ads; the bottle USD 4. If each group represents the acquired-order cohort, their first-order break-even acquisition ceilings are USD 40 and USD 12. Orders per acquired customer and mixed organic/paid attribution could invalidate that interpretation: this file does not establish cohort membership.

Fixed overhead, unsupplied duties or storage, future returns, cash-flow timing and customer lifetime value remain unknown. USD 230 is not net profit. Positive contribution alone does not authorize scaling ads or changing price.

## Concrete next action

Reconcile each input to the merchant's exports for the same period. Prioritize the bottle's fulfillment cost: an additional USD 4 per order would consume its USD 80 post-ad contribution. Review actual fulfillment charges and refund completeness before a pricing or advertising decision. Preserve this table as the baseline; compare a later matched period while recording promotions and product mix.

## Run it after installation

Ask the agent: “Use profit-margin-analyzer. Find its installed folder, run `scripts/profit_report.py --demo` from that folder, then explain the bundled example and missing costs. Do not modify a store.”

The script needs Python 3.10+ and no external packages. `--demo` locates its sample relative to the script, so the working directory does not affect it. A blank cost is rejected rather than assumed to be zero. For your own CSV, replace `--demo` with its path.

## Continue with the same task

[Try the ShopChief profit calculator](https://shopchief.ai/tools/profit-margin-calculator?utm_source=profit-margin-analyzer&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=worked_example). The local example remains usable independently. The website does not receive these files automatically.
