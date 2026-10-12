# Synthetic worked example

All people, products, account results and amounts below are invented fixtures, not merchant outcomes. Amounts are USD unless noted.

Synthetic 100-order cohort: 10 canceled before shipping, 20 still in transit, 70 delivered. Of delivered orders, 5 have unresolved damage cases; 65 are eligible for normal education after the declared delay, subject to message type and policy. Do not start all 100 on a “now it has arrived” email.

Education draft: Subject “Set up the two compartments”; Preview “A simple way to separate small travel essentials.” Body “Open both compartments before packing. Use one for cables and the other for toiletries, keeping caps closed and following each item's travel restrictions. Need help with your pouch or delivery? Reply to this message and we will help.” CTA “View the packing guide.” Do not claim leak-proof performance.

## Acceptance scenarios

1. Given missing delivery confirmation, produce a shipping-aware branch rather than assert delivery from order age.
2. Given a canceled order or unresolved damage case, suppress the standard cross-sell and retain the relevant service path.
