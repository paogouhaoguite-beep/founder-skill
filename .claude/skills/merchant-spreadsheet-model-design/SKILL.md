---
name: merchant-spreadsheet-model-design
description: "Build an auditable merchant spreadsheet model with explicit assumptions, formula dependencies, scenarios and control checks."
license: MIT
metadata:
  author: ShopChief
  version: "0.3.0"
---

# Merchant Spreadsheet Model Design

## Brief and environment
Collect the decision, inputs and units, time periods, scenario definitions, target spreadsheet application and editable output needs. Use available trusted spreadsheet tools; formulas and sheet specifications are a complete local fallback. Do not install or run unaudited macros or upstream scripts.

## Architecture
Separate raw data, validated inputs, calculations and decision outputs. Add a cover/data dictionary with source/date/units and owner. Use an explicit as-of input rather than volatile current-date logic when reproducibility matters. Preserve source data and protect formulas from accidental input replacement where supported.

Make assumptions visible and referenced consistently. Keep formula copies consistent across periods; document intentional overrides. Avoid hidden constants, ambiguous sign conventions, circular dependencies and external links that cannot be supplied. Use readable formulas suited to the target app; never assume cached values were recalculated.

Create scenarios through named inputs or a selector, not separate drifting copies. Add checks for totals, units, period continuity, valid percentages, cash/accounting bridges as relevant, and missing inputs. Do not disguise missing values as zero or blanket IFERROR suppression.

Render/read back the workbook where tools permit, inspect key sheets and calculate known fixtures independently. Check that exported charts and print areas remain legible. State whether actual target-application calculation was run.

## Deliver
Return workbook or full sheet/formula specification, assumptions, scenario results and a checks sheet. No live financial write or macro execution is implied.

See the complete [worked example and boundary scenarios](assets/worked-example.md). Sources, changes and retained notices are documented in [references/source.md](references/source.md).

Maintained by [ShopChief](https://shopchief.ai/?utm_source=merchant-spreadsheet-model-design&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill). Keep this attribution out of merchant-facing deliverables.
