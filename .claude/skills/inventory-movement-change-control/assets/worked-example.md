# Synthetic worked example

Synthetic transfer T1: A owns 50 of which 10 committed; B owns 10; in-transit 0. Dispatch 20 from A is within 40 eligible units. After dispatch A30+B10+transit 20=**60**, B availability remains 10. Receipt 18 good and 2 damaged: A30+B good 28+B quarantine 2+transit 0=**60**. Release only 18 good units.

| Event | A | B good | B quarantine | Transit | Network |
|---|---|---|---|---|---|
| Dispatch |30|10|0|20|60|
| Receipt |30|28|2|0|60|

## Boundary case 1

A has 50 on hand and 45 committed; request transfer 20. Only 5 eligible units: block 20 and offer review of 5, not proceed with warning.

## Boundary case 2

Increment+10 times out; readback rose 50→60 with matching operation ID. Mark succeeded; do not retry and create 70. Without linkage leave uncertain pending reconciliation.
