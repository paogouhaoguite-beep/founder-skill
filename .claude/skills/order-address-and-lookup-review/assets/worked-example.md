# Synthetic worked example

Synthetic email search yields O10 (delivered) and O11 (unfulfilled). Customer confirms O11 through merchant verification. Requested unit number changes from blank to Apt 4; street/city/postcode unchanged. Warehouse has not released O11 and no label exists.

| Field | Old | Proposed | Result |
|---|---|---|---|
| shipping.unit | blank | Apt 4 | eligible scoped correction |
| billing.unit | blank | unchanged | outside request |

Support summary: O11 paid 50, itemX×1 unfulfilled, no refund; address correction proposal awaiting authorized execution.

## Boundary case 1

Customer identifies neither candidate order. Stop with candidate references and request disambiguation; do not expose both full addresses.

## Boundary case 2

Order is unfulfilled in platform but 3PL already printed and dispatched label. Block assumption of reroute; request warehouse/carrier confirmation before promising correction.
