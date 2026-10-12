# Synthetic worked example

Input: Synthetic shopper Lee asks “Where is my order and can you refund shipping?” Order O12 was paid, fulfillment record says dispatched Oct 1, carrier shows label created only. Policy offers shipping refund after a verified missed service commitment; destination and service deadline are not supplied. No refund exists.

Draft: “Hi Lee, your order record is marked dispatched, but the latest carrier record only confirms that a label was created. We have not yet verified a carrier handover. Your shipping-refund request is also pending: we need to check the service commitment for your order before confirming eligibility. We’ll ask the fulfillment team to verify the handover and the applicable delivery commitment.”

Internal task: verify handover evidence and service deadline. Do not write “your parcel is on the way” or “I refunded shipping.” The draft is not sent.

Boundary scenario 1: Two orders share a name but not the same verified customer ID. Do not expose either record until identity is resolved.
Boundary scenario 2: A refund API request times out. Read the transaction state before retrying; report unknown outcome rather than submitting a second refund.
