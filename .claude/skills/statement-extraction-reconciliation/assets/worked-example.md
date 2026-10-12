# Synthetic worked example

Input: Printed opening 100.00; deposit +30.00 → printed running balance 130.00; payment −20.00 → printed closing 110.00. OCR mistakenly extracts the payment as +20.00.

First extraction gives 100 + 30 + 20 = 150, difference +40 versus closing 110. The difference equals twice the suspicious 20 amount, suggesting a sign error. Visual/source-column check confirms it is a debit; record correction +20 → −20, page 1 row 2. Recheck: 100 + 30 − 20 = 110; both running balances match.

Boundary scenario 1: All values parse 100× too large but still tie. Reject the extraction until number-format verification resolves the scale.
Boundary scenario 2: Opening cash was derived from the first transaction instead of printed independently. Mark the first-row check unverified even if later balances tie.
