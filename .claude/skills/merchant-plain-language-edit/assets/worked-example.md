# Worked example

All names, inputs and results below are synthetic.

Input: a shipping banner says “Fulfillment workflow processing is finalized; transit SLA will be provisioned subsequently.” Merchant facts: order has been packed, carrier has not collected it, customer will get an email when it ships.

Revised banner: “Your order is packed. We’ll email you when it ships.”
Change ledger: fulfillment workflow → packed (supplied fact); SLA phrase → notification next step (supplied fact). No arrival date is added. “Your order has shipped” is rejected because collection is unconfirmed.

## Acceptance scenarios

1. A return-policy draft contains a necessary exclusion. Shortening must retain it and its scope rather than optimize for word count.

2. No proof supports “clinically proven.” Mark the claim unresolved; do not replace it with another unsupported assurance.

## Protected-token rewrite

Synthetic input: “Our B-12 bag is 20 L. Visit https://example.test/B-12. ‘Fits my commute,’ says Lee.” The requested change is simpler prose, with product facts, link and customer quotation unchanged.

Complete output: “The B-12 bag holds 20 L. Visit https://example.test/B-12. ‘Fits my commute,’ says Lee.”

| Source span | Output span | Reason |
| --- | --- | --- |
| Our B-12 bag is 20 L | The B-12 bag holds 20 L | Makes the capacity relationship explicit; no capacity change |
| Visit https://example.test/B-12 | Unchanged | Protected URL |
| ‘Fits my commute,’ says Lee. | Unchanged | Verbatim quotation and attribution |

Exact token audit: `B-12`, `20 L`, `https://example.test/B-12`, `‘Fits my commute,’` and `Lee` remain unchanged. The URL's capitalization and hyphen are preserved. Meaning audit: capacity remains 20 L; the customer's quote remains attributed to Lee; no performance promise or claimed personal experience was added.

Boundary: a requested character limit cannot accommodate a required disclaimer. Keep the disclaimer and flag the length conflict rather than delete or silently paraphrase it.

Boundary: a draft changes `20 L` to `20 oz` or drops “up to” from a protected qualified claim. Mark the mismatch, repair only that span and compare again. If the intended value or qualification is unresolved, leave the passage blocked for factual review.
