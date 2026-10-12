---
name: merchant-export-merge-and-reconcile
description: "Combine merchant CSV or workbook exports with an explicit append/join contract, key preservation and row-level reconciliation."
license: MIT
metadata:
  author: ShopChief
  version: "0.3.0"
---

# Merchant Export Merge And Reconcile

## Inputs and tooling
Obtain files/sheets, purpose, record grain, keys, field meanings, currency/timezone and conflict policy. Use a spreadsheet or reviewed dataframe/SQL operations; no upstream scripts are bundled. Preserve original files, identifiers as strings and lineage. If the relationship is unknown, provide a proposed mapping before joining.

## Merge contract
Profile encodings, delimiters, header/total rows, types, null keys and duplicate keys. Choose append for compatible records or join for enrichment based on business meaning, not merely similar headers. Declare intended cardinality and which unmatched side is retained.

Map columns explicitly. Normalize comparison keys only by justified rules and keep raw keys: shared emails/addresses are not proof that two customers are one person. Do not collapse blank keys together. Resolve conflicts by an approved precedence rule or flag them; file order does not establish truth.

For joins, measure key multiplicity before execution and verify the expected output grain afterward. Legitimate one-to-many joins may increase row count; prevent summing a repeated parent total as if each child were a new order. For appends, prove input rows = retained rows + documented duplicates/exclusions, accounting for every input source.

Check parse failures, unmatched rows, conflicting duplicates, numeric control totals by currency and representative records. Quarantine uncertain rows rather than silently dropping them. A clean-looking merged file is not proof of correctness.

## Deliver
Return merged output or exact normalized table, column map, cardinality/row-count bridge, conflict queue and source-file/source-row columns. Any proposed import or customer merge requires separate authorization.

See the complete [worked example and boundary scenarios](assets/worked-example.md). Sources, changes and retained notices are documented in [references/source.md](references/source.md).

Maintained by [ShopChief](https://shopchief.ai/?utm_source=merchant-export-merge-and-reconcile&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill). Keep this attribution out of merchant-facing deliverables.
