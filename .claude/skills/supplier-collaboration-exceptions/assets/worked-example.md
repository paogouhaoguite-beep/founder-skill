# Synthetic worked example

Synthetic PO7 orders 100 mugs, supplier acknowledges 100 due day 10, ships 90. Receipt:85 good+5 damaged. Accepted 85; physical received 90; undelivered 10 and damaged 5 require distinct resolution. Open acceptable obligation 15 unless merchant accepts another settlement.

Draft: “PO7 line 1: received 90,85 accepted and 5 quarantined with photos Q1. Please confirm delivery of remaining 10 and replacement/credit proposal for 5 damaged by the agreed review date.” Not sent.

## Boundary case 1

Supplier promises day 20 after original day 10. Keep both dates and acceptance state; do not rewrite original due date and report on time.

## Boundary case 2

Duplicate receiving event R1 is imported twice. Deduplicate event ID before stock/PO updates; do not mark 180 received.
