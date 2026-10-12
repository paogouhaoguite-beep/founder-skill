# Synthetic worked example

Input: Shipping investigation macro; verified order O7 and carrier check time Oct 2 10:00 UTC; no carrier handover confirmed.

Macro ID SHIP-INV-01: “Hi [[customer_name]], we’re checking the handover of order [[order_id]]. As of [[checked_at]], the carrier record shows [[verified_carrier_state]]. We will contact the fulfillment team to verify the next step.”

Rendered draft: “Hi Sam, we’re checking the handover of order O7. As of Oct 2, 10:00 UTC, the carrier record shows label created. We will contact the fulfillment team to verify the next step.” The owner must authorize that follow-up before it becomes a commitment.

Token sources: customer_name/order_id from verified order; checked_at/state from dated carrier lookup. Eligibility: investigation required; exclusion: confirmed delivery dispute needing a different policy branch.

Boundary scenario 1: checked_at is missing. Block rendering as send-ready and request a current status check.
Boundary scenario 2: A return-policy version changes. Mark affected macros for review even if they have high past satisfaction scores.
