# Synthetic worked example

Synthetic store O7 maps to ERP E88. EventEV 7 timed out, but ERP export shows E88 with external O7 and amount 100. Result: **order exists; do not replay create**. Stock snapshot 10 at 10:00 followed by a2-unit POS sale at 10:05 reconciles to 8 at 10:10. A destination 8 is matched; applying sale−2 again would wrongly produce 6. Webhook W1 is enabled but has no delivery/processing logs: operational health **unknown**.

## Boundary case 1

Two store IDs both use order number 1001. Include store identity in mapping; do not merge them into one ERP order.

## Boundary case 2

A newer stock version 8 has applied before older version 10 arrives. Quarantine stale overwrite; do not “repair”8 back to 10.
