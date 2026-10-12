# Worked example

All names, inputs and results below are synthetic.

Input: source newsletter, medium email, campaign autumn_refill, content care_tip, destination https://store.example/refills?size=500. Expected URL: https://store.example/refills?size=500&utm_source=newsletter&utm_medium=email&utm_campaign=autumn_refill&utm_content=care_tip. Preserve size=500 and exclude recipient email. If a redirect removes parameters, mark propagation failed even though the link opens.

## Acceptance scenarios

1. Given a product-page internal CTA is requested, keep campaign tags off it and use an internal event instead.

2. Given the campaign name changes display wording, preserve the stable ID or document a deliberate taxonomy migration.
