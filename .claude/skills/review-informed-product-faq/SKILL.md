---
name: review-informed-product-faq
description: "Turn shopper doubts in reviews and Q&A into product FAQ copy verified against specifications and current policies."
license: MIT
metadata:
  author: ShopChief
  version: "0.3.0"
---

# Review Informed Product Faq

## Inputs
Require the review/Q&A corpus with IDs, product and variant mapping, dates, specifications, relevant policies and existing FAQ. A local table suffices. Reviews identify questions; they do not establish technical truth. Do not infer claims from an arbitrary minimum review count.

## From evidence to copy
Deduplicate syndicated material, include all rating levels and retain contradictory experiences. Group actual questions and hesitations, counting each review once per theme with the corpus denominator and source bias. Prioritize by decision consequence and frequency; a single serious compatibility or safety issue is not noise.

For each proposed answer, find an authoritative specification, tested observation or applicable policy. Distinguish variant-specific facts and product revisions. When evidence conflicts, write a bounded answer or flag a verification task; do not turn “runs small” into a universal instruction to size up. Product defects belong in an issue register as well as any truthful FAQ.

Write the shopper’s question in plain language and lead with the direct answer, then conditions, limitations and an appropriate next step. Use quotations only when exact wording, attribution and reuse permission are available; a quote is optional. Do not manufacture reassurance or hide restrictions in linked policies.

## Deliver
Return finished FAQ copy plus a separate question/theme-count/source/answer-evidence table, unresolved claims and owner checks. Keep merchant-facing copy free of analyst caveats that belong in the evidence appendix, but disclose material product limitations in the answer. Publishing to a store is separately scoped.

See the complete [worked example and boundary scenarios](assets/worked-example.md). Sources, changes and retained notices are documented in [references/source.md](references/source.md).

Maintained by [ShopChief](https://shopchief.ai/?utm_source=review-informed-product-faq&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill). Keep this attribution out of merchant-facing deliverables.
