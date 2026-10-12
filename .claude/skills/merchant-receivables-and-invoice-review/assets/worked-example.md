# Synthetic worked example

Synthetic as-of October 31: invoice I1 USD 1000 due October 20, credit note 100 and settled allocated payment 400. Open =1000−100−400=**500**, 11 days overdue. Another USD 50 payment has no invoice reference: hold it as unapplied cash, not silently reduce I1. Committed uninvoiced order 200 makes current exposure 700. With limit 1000 a proposed 400 order would reach 1100, exceeding by 100.

Draft: “Our records show USD 500 open on I1, due October 20, after credit CN1 and payment P1. We also received USD 50 without an invoice reference. Please confirm its intended allocation so we can update the statement.”

Separate offer: 2% off an eligible 1000 for 20-day acceleration costs 20/980=2.0408% over 20 days; simple annualized cost=**37.2449%**. It is a scenario, not an APR disclosure or recommendation.

Consolidation case as of October 2: customer A owes I1 USD 600 due September 20 (12 days) and I2 USD 200 due September 25 (7 days), last contacted September 28. One draft: “Following our September 28 note, our statement shows I1 USD 600 and I2 USD 200, total USD 800. Could you confirm the expected payment date or any payment reference we should reconcile?” If unmatched cash 800 exists, hold this reminder pending allocation. No two simultaneous messages or invented late fees.

## Boundary case 1

Invoice is disputed for 200: show disputed 200 and undisputed 300 separately. Do not issue an unqualified USD 500 collection demand.

## Boundary case 2

Payment webhook repeats the same payment ID. Allocate once; a second invoice using that payment needs an explicit split whose total does not exceed settled cash.
