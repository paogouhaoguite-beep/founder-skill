# Synthetic worked example

Input: shopper requested a restock alert for blue bottle B1; event 09:00 UTC, stock verified 12 at 09:05, alert expires 18:00, opted in, no prior push today; merchant promotional cap one/day. Destination /products/bottle?variant=B1, stockout fallback product page showing unavailable.

Title: “Your blue bottle is back”
Body: “Blue, 500 ml is available again. View current stock and delivery options.”
Decision: draft eligible at 09:05 subject to send-time stock and consent refresh; no claim that stock will last. Deep link points to B1. Lock-screen fit remains unverified until platform preview.
If 80 recipients receive and 8 unique recipients click within 24 hours, click rate is 8/80 = 10%; this is descriptive, not incremental sales.

Boundary 1: stock falls to zero before send → suppress; do not send the stale claim.
Boundary 2: send history missing or permission limited to order notices → promotional eligibility unknown/not established; retain draft, no send.
