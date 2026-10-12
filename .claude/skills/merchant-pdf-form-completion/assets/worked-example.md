# Synthetic worked example

Input: Supplier onboarding form fields company_name, billing_email, tax_id and signature. Merchant provides “Sample Store” and billing@example.com, no tax ID, and authorizes filling business details only.

Mapping: company_name→Sample Store; billing_email→billing@example.com; tax_id→unresolved; signature→not authorized. Deliver a partial-fill proposal with tax ID flagged; do not fabricate an identifier or insert a signature. No actual PDF is asserted in this text fixture.

Boundary scenario 1: Two fields share the same internal name on separate pages. Verify whether one fill intentionally updates both.
Boundary scenario 2: The original is digitally signed. Preserve it and flag signature consequences before any edited copy is used.
