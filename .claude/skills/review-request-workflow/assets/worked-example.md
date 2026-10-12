# Synthetic eligibility
Orders A and B delivered October 1; merchant-defined experience window is 7 days. A already has a review; B has no review and valid email permission. On October 8 only B is eligible. C ordered October 1 but delivery is unknown: hold C; do not infer October 8 eligibility from purchase date.

Neutral draft: "How has your travel pouch worked for you? Share your honest experience with other shoppers: [merchant review URL]."

## Acceptance scenarios
1. Merchant asks to request reviews only from customers rated happy by support. Propose neutral eligibility and separate service follow-up instead of sentiment gating.
2. A connector times out after sending. Read the request/send ledger before retrying; never blindly duplicate the request.
