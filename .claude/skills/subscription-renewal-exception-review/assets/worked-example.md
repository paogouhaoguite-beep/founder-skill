# Synthetic worked example

Synthetic S1 renewal USD 30 due October 1 at 09:00UTC: attempt A1 at 09:01 has unknown outcome; warehouse has no shipment. Expected output: **payment status unknown; do not retry or call it unpaid**, request provider lookup by A1; shipment remains pending payment decision. S2 cancellation request September 30 at 18:00UTC was effective immediately under the supplied policy, but charge A2 succeeded October 1. Output: **USD 30 post-cancellation charge requiring billing review**; no automatic refund or shipment.

Separate service add-on priced 30 for a supplied 30-day period has 10 unused days and no fulfilled goods: preview credit 30×10/30=10 only if the supplied policy authorizes that basis.

## Boundary case 1

A1 later reads succeeded with the same provider reference. Mark paid once; do not create a duplicate renewal charge.

## Boundary case 2

Physical box shipped before a plan change. Do not credit its contents as unused subscription days; request the actual returns/policy decision.
