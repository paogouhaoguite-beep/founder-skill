# Worked example

All names, inputs and results below are synthetic.

Input: A seed test covers 10 Gmail inboxes and 5 Outlook.com inboxes: Gmail 8 inbox/2 spam, Outlook.com 1 inbox/4 spam. Expected per-provider inbox shares are 80% and 20%; overall 9/15 = 60% is supplementary and not the production inbox rate. An ESP reports 99% delivered; preserve that as SMTP acceptance, not a contradiction of the seed findings.

## Acceptance scenarios

1. Given no iCloud Mail seed was included, report iCloud Mail placement unknown; Apple Mail is a client and does not identify the recipient mailbox provider.

2. Given the test used a different sending domain, do not apply its result to the production domain.
