# Worked example

All names, inputs and results below are synthetic.

Input: Brand “Harbor” has 30 search hits: 12 unrelated port stories, 8 syndicated copies of one review, 6 unique product mentions and 4 owned posts. Expected third-party distinct relevant count: 1 review + 6 mentions = 7; keep owned posts separately. Query exclusions remove port terminology, with a note that legitimate product posts mentioning ports could be missed.

## Acceptance scenarios

1. Given one platform export is missing, report its coverage unknown rather than zero mentions.

2. Given a query expands mid-series, annotate a break and re-run earlier periods before claiming growth.

## Media-monitor result

This extends the synthetic Harbor example; it is an offline worked result, not an activated monitor.

Inputs: the same seven eligible third-party distinct origin items remain after deduplication. Four matched prior weekday buckets, collected with the same query and coverage, have counts5,7,6,6: baseline mean6. The merchant chose a volume review at twice that mean and a separate manual-review rule for any new product-safety allegation. These are this merchant's hypothetical rules, not recommended universal thresholds.

Current coding of the seven origin items: positive2, neutral1, negative3, mixed0, unclear1. Net sentiment=(2−3)/7×100=−14.3%. The immediately prior comparable bucket had positive2, neutral3, negative1, mixed0, unclear0: net sentiment=(2−1)/6×100=16.7%. The change is−31.0 percentage points after rounding; the unclear item remains in the current denominator. This is observed mention sentiment, not a customer satisfaction estimate.

One negative origin item R1 at09:00 says, “The strap separated while I carried a glass jar.” At11:00 publication N1 quotes R1 without new testing or an additional customer account. N1 is among the previously collapsed copies, so it does not add an eighth independent origin. No injury is established by either text.

| Digest field | Completed result |
| --- | --- |
| Window/coverage | Same hypothetical weekday bucket and source set as baseline; private groups unavailable |
| Volume |7 distinct origins /6 baseline mean=1.17×; merchant2× rule did not trigger |
| Narrative/source chain | New strap-separation allegation: R1 at09:00→N1 quotation at11:00; one underlying allegation, two exposure locations |
| Sentiment |2positive,1neutral,3negative,0mixed,1unclear; net−14.3%, change−31.0points |
| Review condition | New product-safety allegation rule triggers manual review despite the volume rule not triggering |
| Owner/action | Product-safety owner: inspect original account and supplied product/batch evidence; no verified defect or injury conclusion yet |
| Next review | Merchant-selected12:00 check for investigation updates and corrections; this example has not scheduled or sent that check |

Additional boundary: a news connector begins returning twice as many sources today. Mark a coverage break; do not treat the larger feed as a calibrated volume alert until comparable history is reconstructed.

Additional boundary: five copied posts repeat one allegation. Preserve their exposure trail but do not call them five independently confirmed incidents.
