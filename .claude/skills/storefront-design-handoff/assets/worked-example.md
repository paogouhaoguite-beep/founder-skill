# Synthetic worked example

Input: Bag PDP permits selecting a size and adding one item to cart. Backend may return out-of-stock; mobile width is narrow. Handoff:

States: no-size→CTA explains selection needed; valid-size→CTA enabled; submitting→prevent duplicate action and show pending; success→cart count updates from confirmed response; stock-conflict→preserve selection, show verified availability and offer another size. Responsive rule: product facts and size choice remain before CTA; long translated labels wrap, not truncate.

Acceptance: two rapid taps produce one intended request; a stock-conflict response does not show “Added”; keyboard focus reaches size choices and the resulting message. These are requirements, not claims that tests ran.

Boundary scenario 1: The design shows delivery dates but no reliable API/data exists. Mark the feature blocked rather than invent estimates.
Boundary scenario 2: Only a scaled screenshot exists. Use relative layout guidance and request source measurements before pixel-exact redlines.


Continuity fixture: an email links to cart C1, but inventory and price must refresh on arrival. When the saved cart has expired, show an explanatory state and a path to rebuild from still-available items; do not say “Your cart is restored” without state confirmation. A support handoff carries only authorized order/context fields, not an unrestricted customer-history dump.
