# Synthetic worked example

Input: C1 and C2 share normalized email; C1 opted in on Sep 1 and C2 opted out on Sep 20. C3 shares their shipping address but has another email.

Expected: C1/C2 are identity candidates with a consent conflict; marketing export suppresses them pending authoritative reconciliation, not an automatic opt-in merge. C3 is not merged from address alone. Proposed survivor remains undecided until ownership/history is verified.

## Boundary case 1

A WooCommerce field named accepts_marketing is plugin-defined and undocumented: report unknown semantics rather than interpreting true as legally valid consent.

## Boundary case 2

A merge partially completes or returns a job ID: record pending status and verify final state; never rerun a destructive merge blindly.
