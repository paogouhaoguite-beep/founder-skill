# Synthetic worked example

Synthetic O1 USD 120 has a provider high-risk label because billing/shipping differ. Customer history shows three delivered gift orders to that same address; payment is authorized, parcel not dispatched. Output: **manual review, not proven fraud**; preserve alternative gift explanation, request the approved identity check, no cancellation. Customer C2 has refund events 10+5 on one of two orders: refunded-order rate 1/2=50%, refund value 15, **not 2/2=100%**. Reason “item damaged” plus inspection photos supports a service-quality investigation, not a fraud label.

## Boundary case 1

Provider gives score 91 but no feature explanations. Report score as supplied and explanation unavailable; do not invent SHAP percentages.

## Boundary case 2

A held order already shipped one of two parcels. Mark only remaining fulfillment as a possible hold; request authorized interception separately rather than report entire order stopped.
