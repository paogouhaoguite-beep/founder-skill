# Synthetic worked example

Input: A merchant wants to know why recent bottle purchasers chose a size. Survey email draft for orders delivered in the last 30 days; no deployment permission.

Finished questionnaire:
1. “Have you used the bottle from your recent order?” Yes / No. No skips Q3.
2. “Which influenced the size you selected? Select all that apply.” Bag space / Amount I expect to drink / Bottle weight / Price / Other [optional text] / Do not remember. “Do not remember” is exclusive.
3. “Thinking about the last seven days, on how many days did you use it?” 0 through 7 / Do not remember.
4. “What, if anything, would you change about the size?” Optional text.

Synthetic counts: 100 eligible invitations, 30 starts, 24 completions, 20 of the 24 completed surveys contain an answer to Q2; 8 of those 20 select bag space. Report 8/20 Q2 respondents (40%), with 4 completed surveys missing Q2. Do not report 40% of all customers. Pilot must verify Q1 branching and exclusive Q2 option before sending.

Boundary scenario 1: A tracking satisfaction question has old wording. Keep it unchanged or start a clearly labeled new series.
Boundary scenario 2: Only five responses arrive. Return exact counts and comments; do not infer no demand or statistical equivalence.
