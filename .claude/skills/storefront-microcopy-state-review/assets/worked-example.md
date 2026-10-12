# Synthetic worked example

Input: Checkout request times out; backend outcome unknown. Current message: “Payment failed. Try again.”

Replacement: “We couldn’t confirm the result yet. Check your order status before trying another payment.” Required behavior: a working order-status route or support path; if absent, use a verified support instruction instead. Internal finding: do not claim failure until transaction state is read back.

Boundary scenario 1: Email field contains an invalid format. Name the field and a useful correction; do not clear the cart.
Boundary scenario 2: A success banner appears before persistence completes. Distinguish “Submitting…” from “Order confirmed” and flag the behavior mismatch.
