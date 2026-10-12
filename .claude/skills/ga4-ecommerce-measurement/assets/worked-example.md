# Synthetic purchase contract
Order DEMO-101 contains 2 items at net USD 30 each, shipping USD 5, tax USD 6. Merchandise value is USD 60; shipping and tax are separate fields. Transaction total is USD 71. A purchase event with value 71 and separate shipping/tax would mix revenue definitions. Two browser records for DEMO-101 trigger duplicate-emitter investigation; they are not two orders.

## Acceptance scenarios
1. Event payload looks correct but no debug/property access exists. Report payload validation only; live receipt remains unverified.
2. One unit is refunded. Match the original transaction and item quantity; avoid treating the entire two-unit order as refunded.
