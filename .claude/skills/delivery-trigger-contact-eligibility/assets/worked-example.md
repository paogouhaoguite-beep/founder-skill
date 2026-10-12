# Synthetic worked example

Synthetic as-of October 10 12:00 UTC; merchant requests email survey 3–7 full days after all items delivered, inclusive, with 30-day cooldown. C1 final parcel delivered October 5 12:00 →5 days and no contact in complete history: eligible if email permission valid. C2 first parcel October 5 but final parcel undelivered: pending. C3 delivered October 6 (4 days) but survey sent October 1: suppressed.

| Recipient | Event result | History/permission | Final result |
|---|---|---|---|
| C1 |5 days|complete history, permitted|eligible, key survey-C1-O1|
| C2 |completion unknown|permitted|pending delivery|
| C3 |4 days|last sent 9 days ago|cooldown exclusion|

## Boundary case 1

Delivery timestamp is October 11, after as-of October 10. Flag invalid future event and exclude from current eligibility; do not use negative elapsed days.

## Boundary case 2

Carrier delivery missing but fulfillment occurred 5 days ago. Do not silently treat as delivered; return unknown or explicitly separate merchant-approved fulfillment-proxy cohort.
