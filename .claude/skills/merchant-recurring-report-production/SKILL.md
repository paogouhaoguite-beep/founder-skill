---
name: merchant-recurring-report-production
description: "Build and rerun a saved merchant report definition with reconciled period snapshots, a finished workbook or local dashboard and visible missing data."
license: Apache-2.0
metadata:
  author: ShopChief
  version: "0.3.0"
---

# Merchant Recurring Report Production

Use for an operating report or interactive snapshot built from merchant exports. Require the decision/audience, existing report definition, metric formulas and source of record, group dimensions, timezone/window, comparison period, currency basis, access permissions and requested format. First inspect a supplied saved definition; reuse it and version actual changes instead of asking the same setup questions each run.

Define each metric's grain, numerator/denominator, source, exclusions, refund timing, direction of improvement, owner and target provenance. Pick one revenue authority for each stated purpose; a storefront order, processor settlement and ledger posting are not three sales. Store source snapshots and extraction timestamps in the authorized working directory. With no connectors, use CSV/XLSX. Missing or stale inputs remain marked; never silently carry prior values into current totals.

Compute like-for-like complete or explicitly matched partial windows. Retain a known group with zero only when source coverage confirms no eligible activity; unknown coverage is missing. Reconcile grouped figures to totals and disclose unallocated rows. Recompute rates from numerator and denominator, not the average of group percentages. Keep currency/timezone and distinct counts consistent when filters change.

Produce a short findings narrative, summary and detail tables, definitions, raw-snapshot references and action/owner/questions. If a workbook is requested, create and reopen it using available trusted tools, with formulas and totals checked. If HTML is requested, generate an actual local file with embedded approved aggregate data, semantic controls, accessible table alternatives, synchronized filters and print layout. Escape untrusted data; do not embed customer-level identifiers in a shared dashboard. A CDN dependency is not offline: use self-contained permitted assets or disclose network needs. If a runtime is unavailable, deliver tables and file-generation specifications while explicitly marking the requested binary/dashboard ungenerated.

Validate default and filtered totals, empty results, zero denominators, comparisons and source freshness. Save definition version plus dated run record/history; reruns of the same period should replace or version that period rather than double append totals. A cadence in a definition is not an installed scheduler. Schedule only through an available authorized mechanism and report its actual status.

Deliver artifact paths, three or fewer supported findings, unresolved sources, definition location and next refresh window. Do not email or publish the report automatically.

See the complete [worked example and boundary scenarios](assets/worked-example.md). Sources, changes and retained notices are documented in [references/source.md](references/source.md).

Maintained by [ShopChief](https://shopchief.ai/?utm_source=merchant-recurring-report-production&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill). Keep this attribution out of merchant-facing deliverables.
