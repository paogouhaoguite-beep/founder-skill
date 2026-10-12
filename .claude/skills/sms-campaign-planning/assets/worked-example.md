# Synthetic worked example

All people, products, account results and amounts below are invented fixtures, not merchant outcomes. Amounts are USD unless noted.

Synthetic eligible 1,000 recipients, quoted USD 0.02 per SMS segment before carrier/tax fees. A confirmed 150-unit GSM-7 message costs one segment: USD 20. A finalized 170-unit message needs ceil(170/153)=2 segments: USD 40. If a non-GSM character converts a 150-unit string to UCS-2, ceil(150/67)=3 segments and the base estimate becomes USD 60. Verify with the chosen provider; placeholders are not the final message.

Draft content: “Field & Fold: the navy pouch you requested is back at USD 39. Current stock and delivery: [verified link]. [required opt-out text].” Bracketed values must be resolved and counted before sending.

## Acceptance scenarios

1. Given checkout phone numbers but no SMS marketing permission, keep them out of the promotional send population and deliver a draft only.
2. Given an emoji or long personalized link changes encoding/length, recalculate cost from finalized text before checking the budget cap.
