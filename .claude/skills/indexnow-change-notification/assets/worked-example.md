# Worked example

All names, inputs and results below are synthetic.

Input: the hypothetical verified host is www.example.com. Five rows contain https://www.example.com/p/mug twice, https://www.example.com/p/bottle once, https://other.example/p/cup and https://staging.example.com/p/mug. Expected eligible list contains 2 unique owned production URLs, subject to page-state checks. If a provider accepts the request, report “notification accepted for 2 URLs”; indexed count remains unknown until separate evidence exists. See [the complete hypothetical unsent request](request-example.json): the demonstration host/key/URLs do not claim ownership or an actual submission. The verification file would need to contain the matching key; keyLocation and URL prefix must satisfy the documented scope. No request was sent.

## Acceptance scenarios

1. Given a temporary 503 affects a changed product page, resolve the outage before treating it as a deliberate deletion.

2. Given host/key validation fails, report the error and do not retry by submitting unrelated domains or removing verification controls.
