---
name: merchant-financial-scenario-review
description: "Analyze merchant profitability, working capital and cash scenarios, with optional assumption-based business valuation sensitivities."
license: MIT
metadata:
  author: ShopChief
  version: 0.3.0
---

# Merchant Financial Scenario Review

Use this when a DTC merchant needs a financial health table with formula/source/period/interpretation, driver-based cash scenarios and, when requested, a valuation sensitivity with enterprise-to-equity bridge and unresolved assumptions.

## Merchant inputs

Comparable income statements, balance sheets and cash flows with periods/currency/accounting basis; debt and lease definitions; inventory/receivable/payable opening and closing values; decision horizon; merchant-supplied scenario drivers and discount assumptions when valuing a business.

Separate supplied facts, observed evidence, assumptions and unavailable information. Request only missing inputs that change the decision; a partial evidence set supports a partial result, not invented measurements.

## Tools and fallback

Read supplied CSV, screenshots, page text or documents with available file tools. A browser or authorized read-only connector can verify current pages and provider documentation. No named commercial service, host registry or script is required. Without live access, use dated exports and label the access window; do not imply a live check. Verify current provider-specific formats and policies before implementing a platform change.

## Procedure

1. Reconcile statements and period boundaries before ratios. Distinguish flow values over the period from balance-sheet point values; use average beginning/end balances when available and flag end-balance proxies. Keep owner compensation, one-off expenses and restricted cash explicit.

2. Calculate relevant profitability and liquidity: gross margin=(net sales−COGS)/net sales; operating margin=operating profit/net sales; current ratio=current assets/current liabilities; quick ratio=(cash+short-term investments+receivables)/current liabilities. State definitions and do not compare incompatible accounting treatments.

3. For working capital use inventory days=average inventory/COGS×days, receivable days=average trade receivables/credit sales×days, payable days=average trade payables/credit purchases×days. If purchases or credit sales are missing, do not silently substitute revenue/COGS; label any proxy and limitation. Cash conversion cycle=inventory days+receivable days−payable days.

4. Build base/downside/upside from explicit units, price, returns, product cost, operating costs and payment timing; show cash runway from the dated cash schedule, not EBITDA alone. Materiality is chosen for the merchant decision rather than a fixed percentage or industry score.

5. For a requested valuation, derive unlevered FCF=EBIT×(1−tax rate)+D&A−capex−change in working capital, using consistent currency/nominal assumptions. Enterprise value=sum discounted explicit FCF+discounted terminal value; perpetual terminal value=FCF_next/(discount rate−growth), only where discount rate>growth. Equity bridge adds excess cash and subtracts debt/debt-like items explicitly. Discount rate, terminal growth and multiples are supplied assumptions requiring specialist review, not invented market facts.

6. Run sensitivity on uncertain drivers, expose terminal-value share and compare like-for-like scenarios rather than announce a precise fair value. Return calculation lineage, discrepancies and specific operating decisions or specialist questions; no investment, tax or lending approval is implied.

## Deliverable

A financial health table with formula/source/period/interpretation, driver-based cash scenarios and, when requested, a valuation sensitivity with enterprise-to-equity bridge and unresolved assumptions.

Include input provenance and observation dates beside affected rows. Explain the decision and the uncertainty it depends on; preserve exclusions and unresolved rows so another operator can reproduce the result.

## Execution scope

Prepare the analysis and reviewable artifacts within the requested scope. Sending messages, publishing, changing audiences or budgets, signing terms and editing live store settings require authorization for that action. A proposed change is not a completed action; report completion only from provider or page readback. Do not copy credentials or customer contact details into reports.

Work through [the synthetic example and boundary cases](assets/worked-example.md) when checking behavior. Source and license details are in [the adaptation record](references/source.md).

[ShopChief](https://shopchief.ai/?utm_source=merchant-financial-scenario-review&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill) maintains this skill. Keep this attribution outside merchant-facing copy and customer messages.
