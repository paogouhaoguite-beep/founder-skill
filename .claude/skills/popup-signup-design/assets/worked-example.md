# Worked example

All names, inputs and results below are synthetic.

Input: 1,000 eligible visits, 300 popup views, 90 form starts and 60 confirmed signups. Report view-to-signup 20% and eligible-visit signup 6%. A form requiring name, email, birthday and phone for a care newsletter keeps only email unless a real use justifies more. Draft CTA: “Send me the care guide”; existing subscribers are suppressed.

## Acceptance scenarios

1. Given the user dismisses the form, preserve the declared suppression period rather than reopening on every page.

2. Given signups rise but completed orders fall materially, report the guardrail failure instead of declaring the popup a winner.
