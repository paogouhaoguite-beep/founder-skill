---
name: merchant-ordered-funnel-analysis
description: "Compute ordered merchant funnels from event-level data with explicit entry cohorts, windows, sequence checks and bounded interpretation."
license: MIT
metadata:
  author: ShopChief
  version: "0.3.0"
---

# Merchant Ordered Funnel Analysis

Use to find where an observed purchase journey changes, before deciding what to redesign. Inputs: event extract with stable entity/event IDs and timestamps, ordered stage definitions, entry dates, conversion window, extraction cutoff, timezone, identity rules, segment assignment and known tracking changes. CSV processing is sufficient; without raw sequence data, report limitations and do not reconstruct an ordered funnel from aggregate counts.

Freeze a counting unit (person, session or checkout) and first eligible entry per defined episode. Choose a window from the business question, not from successful converters alone. Exclude or separately label entries without a fully observable window. Deduplicate event IDs; resolve late-arriving events and same-time ordering using reliable sequence metadata or mark ambiguous.

For each eligible entry, search sequentially: select the first qualifying stage-2 event after entry, then stage 3 after that selected event, and so on, all within the original entry window. Do not take independent global minima for each stage: an earlier unrelated cart can conceal a valid later sequence. Every later stage must retain the full qualifying prefix.

Output counts, adjacent-stage rate n_next/n_prior, cumulative rate n_stage/n_entry, losses and elapsed-time summaries among the stated qualified population. Zero denominators yield undefined rates. Freeze device/channel at the selected entry unless another rule is explicit. Compare complete equivalent periods and segments; check instrumentation, consent coverage and identity changes first.

Rank investigation opportunities using observed volume, business stakes, historical evidence and uncertainty, not universal industry bands. Segment differences are associations; report counts, rate differences and appropriate uncertainty. Small samples, clustered events and repeated exploratory comparisons constrain inference. Use statistical tooling only when assumptions are supported; no fixed minimum sample guarantees significance. A hypothetical gap-closure estimate is a scenario, not recoverable revenue.

Deliver a reproducible definition, sequence exception log, funnel table, one evidence-backed investigation priority and next validation action. No store changes or analytics uploads are implied.

See the complete [worked example and boundary scenarios](assets/worked-example.md). Sources, changes and retained notices are documented in [references/source.md](references/source.md).

Maintained by [ShopChief](https://shopchief.ai/?utm_source=merchant-ordered-funnel-analysis&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill). Keep this attribution out of merchant-facing deliverables.
