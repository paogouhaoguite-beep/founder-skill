---
name: merchant-chart-and-data-story
description: "Turn verified merchant data into an honest chart or table with a clear decision message, accessible encoding and source notes."
license: Apache-2.0
metadata:
  author: ShopChief
  version: "0.3.0"
---

# Merchant Chart And Data Story

## Inputs
Collect the decision, verified table, grain, period, units, uncertainty and output medium. Use plotting tools if available; a chart specification and completed accessible data table are valid fallback artifacts. Do not invent numbers to make a chart look balanced.

## Choose and encode
Use bars for category comparisons, lines for ordered time, scatter for relationships and distributions when spread matters. Choose a table when exact lookup is the task. Avoid a chart type that implies continuity, part-of-whole or causality absent from the data.

Keep units, date intervals and scales explicit. Bars need an honest baseline; any transformed or truncated axis must be justified and clearly shown. Avoid dual-axis implications and decorative 3D. Use labels, shapes or patterns alongside color, adequate contrast for the target medium and a text description of the finding. Show missing periods as missing rather than zeros or connected certainty.

Write a headline describing the observed result, not a causal story the data cannot support. Explain denominator and comparison basis. For tables, align numeric precision and units, distinguish subtotal/total rows, preserve sorting intent and handle small-screen overflow without dropping columns.

Check plotted values against the source, labels against categories, uncertainty against its actual method, and the exported artifact at intended size. Separate evidence, interpretation and proposed action; do not claim a visual change improves sales.

## Deliver
Return chart/table, concise takeaway, source/window/metric note, accessible description and verification status.

See the complete [worked example and boundary scenarios](assets/worked-example.md). Sources, changes and retained notices are documented in [references/source.md](references/source.md).

Maintained by [ShopChief](https://shopchief.ai/?utm_source=merchant-chart-and-data-story&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill). Keep this attribution out of merchant-facing deliverables.
