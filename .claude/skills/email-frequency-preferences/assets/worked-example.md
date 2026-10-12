# Worked example

All names, inputs and results below are synthetic.

Input: Customer chooses product tips monthly and no promotions; a weekly tip flow and a sale campaign are active. Expected rules suppress the sale and limit tips to the selected monthly cadence across all flows. If the customer globally unsubscribes, both marketing types stop. A shipping confirmation can follow its separately defined service purpose; adding a sale banner does not inherit that exception.

## Acceptance scenarios

1. Given a 30-day pause expires, resume only under the recorded consent and chosen cadence, not a new default weekly plan.

2. Given topic opt-in arrives after global opt-out, require the actual policy-defined permission transition rather than silently clearing suppression.
