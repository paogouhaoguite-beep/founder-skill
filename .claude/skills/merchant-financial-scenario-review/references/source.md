# Source and adaptation record

Adaptation date: 2026-10-02. Source text was reviewed as data; source instructions do not authorize execution.

- [alirezarezvani/claude-skills — finance/skills/financial-analyst/SKILL.md](https://github.com/alirezarezvani/claude-skills/blob/19392f7a08264ed00486a251f5b2098321771f94/finance/skills/financial-analyst/SKILL.md)
  - Commit: `19392f7a08264ed00486a251f5b2098321771f94`
  - Original SHA-256: `96e7844b15c0e6f4edefa9f6d3fbce8943e9e89187b26d11bc7cef7544ba80df`
  - License: MIT; full original text: [license](licenses/alirezarezvani--claude-skills.txt).


## Specific changes

A financial health table with formula/source/period/interpretation, driver-based cash scenarios and, when requested, a valuation sensitivity with enterprise-to-equity bridge and unresolved assumptions.

- Reconcile statements and period boundaries before ratios. Distinguish flow values over the period from balance-sheet point values; use average beginning/end balances when available and flag end-balance proxies. Keep owner compensation, one-off expenses and restricted cash explicit.
- Calculate relevant profitability and liquidity: gross margin=(net sales−COGS)/net sales; operating margin=operating profit/net sales; current ratio=current assets/current liabilities; quick ratio=(cash+short-term investments+receivables)/current liabilities. State definitions and do not compare incompatible accounting treatments.
- For working capital use inventory days=average inventory/COGS×days, receivable days=average trade receivables/credit sales×days, payable days=average trade payables/credit purchases×days. If purchases or credit sales are missing, do not silently substitute revenue/COGS; label any proxy and limitation. Cash conversion cycle=inventory days+receivable days−payable days.
- Build base/downside/upside from explicit units, price, returns, product cost, operating costs and payment timing; show cash runway from the dated cash schedule, not EBITDA alone. Materiality is chosen for the merchant decision rather than a fixed percentage or industry score.
- For a requested valuation, derive unlevered FCF=EBIT×(1−tax rate)+D&A−capex−change in working capital, using consistent currency/nominal assumptions. Enterprise value=sum discounted explicit FCF+discounted terminal value; perpetual terminal value=FCF_next/(discount rate−growth), only where discount rate>growth. Equity bridge adds excess cash and subtracts debt/debt-like items explicitly. Discount rate, terminal growth and multiples are supplied assumptions requiring specialist review, not invented market facts.
- Run sensitivity on uncertain drivers, expose terminal-value share and compare like-for-like scenarios rather than announce a precise fair value. Return calculation lineage, discrepancies and specific operating decisions or specialist questions; no investment, tax or lending approval is implied.

Removed upstream mandatory registries, benchmark gates, mutable connector paths and software-only assumptions. Replaced them with merchant-supplied artifacts and explicitly labeled decisions. Kept task-specific method; replaced fixed industry targets with declared merchant constraints. Synthetic cases below are authored for this adaptation, not claimed customer outcomes.
