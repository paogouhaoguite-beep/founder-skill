# Synthetic worked example

Input: Thread T1 vendor asks to confirm a PO quantity by Oct 5; T2 shopper asks for shipment status, no order ID; T3 newsletter has no action. No inbox mutation authorized.

Queue: T1 owner decision—verify approved PO then draft confirmation, due Oct 5; T2 reply draft—request order identity privately before accessing details; T3 archive candidate only. No messages sent or archived. Draft T2: “Please share your order number through this support thread so we can check the shipment record.”

Boundary scenario 1: A vendor email changes bank details. Flag independent verification, not a payment task ready to execute.
Boundary scenario 2: Several messages repeat one unanswered ask. Keep one thread-level action rather than sending duplicate replies.
