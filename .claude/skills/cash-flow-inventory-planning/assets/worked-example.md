# Synthetic worked example

All quantities, amounts, policies and company circumstances below are invented for arithmetic or decision review. They are not benchmarks.

Synthetic opening cash USD 5,000. Week 1 receipts 2,000, deposit 3,000 and operating outflows 1,000 leave 3,000. Week 2 receipts 1,500, remaining supplier balance 4,000 and operations 1,000 leave -500. A merchant-selected minimum buffer of 1,000 implies a week-2 funding gap of 1,500, even if products have positive contribution.

## Acceptance case 1 — supported inputs

Return balances 3,000 and -500 plus the 1,500 buffer gap, without replacing cash receipts with booked sales.

## Acceptance case 2 — boundary or missing evidence

If a payout is held in reserve until week 3, move its cash date and show the gap; do not count the same funds as available in weeks 1 and 3.

These cases specify expected behavior. Reading them or validating package syntax does not demonstrate live merchant acceptance.

## Rolling forecast: actual versus frozen plan

Frozen week 1: opening 1,000 + expected receipt 600 − expected payments 900 = closing 700. Actual receipts are 400 and payments are 950, so closing cash is 450. The difference is −250: a receipt shortfall of −200 plus payment excess of −50.

Evidence shows that the remaining receipt of 200 moved to week 2, while the additional payment of 50 is a previously omitted bank fee. Set week 2 opening cash to 450, include the delayed receipt of 200 once, and record the bank fee as an amount difference. Without evidence explaining the receipt shortfall, leave it unresolved rather than classifying it as a timing difference.
