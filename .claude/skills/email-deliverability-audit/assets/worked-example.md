# Synthetic worked example

All people, products, account results and amounts below are invented fixtures, not merchant outcomes. Amounts are USD unless noted.

Synthetic ESP reports 10,000 attempted unique recipients, 500 hard bounces and 9,500 accepted messages. Accepted rate = 95%; this does not mean 95% inbox placement. If the ESP counts 19 complaints over those 9,500 accepted recipients, its complaint ratio is 0.20%; do not present that as Gmail Postmaster's spam ratio with a different denominator. A header with dkim=pass for an unrelated signing domain and spf=pass for an unrelated envelope domain may still fail DMARC alignment with the visible From domain. Inspect exact domain relationships before concluding.

## Acceptance scenarios

1. Given DNS has DKIM but received mail has no matching signature, mark authentication unverified/failing from message evidence rather than passing it from DNS existence.
2. Given 95% accepted delivery and no inbox-placement evidence, report acceptance only and do not claim an inbox rate.
