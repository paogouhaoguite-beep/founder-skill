# Worked example

All names, inputs and results below are synthetic.

Input: A merchant-verified current product export dated 2026-10-02 identifies SKU CUP350 at $18 USD and in stock. The visible 350 ml cup page matches it; JSON-LD says $15 and feed says out of stock. Expected audit marks conflicting product truth and specifies the authoritative current values for repair. It does not certify agent checkout because discovery markup exists. A draft cart with 2 cups at $18 has merchandise subtotal $36, with shipping/tax still unresolved before buyer confirmation.

## Acceptance scenarios

1. Given a crawler is blocked intentionally for training, do not remove that rule without distinguishing the requested search or commerce use.

2. Given no documented order-placement integration exists, stop at comparison/cart preparation rather than inventing an API.
