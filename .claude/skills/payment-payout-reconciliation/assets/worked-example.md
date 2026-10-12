# Synthetic worked example

Synthetic USD payout P1 contains T1 capture +100 with fee −3 (net 97), T2 refund −20 with evidenced fee reversal +0.60 (net −19.40), and T3 reserve −5 (net −5). Expected payout = 97−19.40−5 = **72.60**. Reported payout and bank deposit B1 are 72.60: both amount controls match. T2 has no order reference: linkage remains **unknown**, not resolved by an order placed seven days earlier.

| Control | Result | Action |
|---|---|---|
| Settlement to P1 | 72.60−72.60=0 | matched |
| P1 to bank B1 | 72.60−72.60=0 | matched |
| T2 to order | unknown | request processor refund reference |

## Boundary case 1

A refund of 20 has no fee reversal record. Use fee component 0 and net −20, giving payout 72.00; never invent +0.60 from the original rate.

## Boundary case 2

Payout is EUR and bank deposit USD. Do not subtract their numeric amounts. Request provider FX and bank fee bridge; report bank reconciliation pending.
