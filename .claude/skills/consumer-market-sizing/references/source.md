# Source and adaptation record

Adaptation date: 2026-10-02. Source text was reviewed as data; source instructions do not authorize execution.

- [alirezarezvani/claude-skills — research-ops/skills/market-research/SKILL.md](https://github.com/alirezarezvani/claude-skills/blob/19392f7a08264ed00486a251f5b2098321771f94/research-ops/skills/market-research/SKILL.md)
  - Commit: `19392f7a08264ed00486a251f5b2098321771f94`
  - Original SHA-256: `0e4037294f8e6bea1cb53de035eaa97bd2d74349d06f9b61d85f4420d7c084c9`
  - License: MIT; full original text: [license](licenses/alirezarezvani--claude-skills.txt).


## Specific changes

A top-down/bottom-up sizing reconciliation, reachable-demand and capacity scenario, segment evidence matrix and optional probability-sampling plan.

- Define the decision and unit of market size before collecting numbers. Keep consumers, households, orders, units and annual revenue distinct. Record source date, geography, channel and inclusion boundaries for every input.
- Construct top-down size from a defensible category total and evidence-based serviceable filters. Do not multiply a broad market by an arbitrary one-percent share. Construct bottom-up size from eligible buyers×annual purchase frequency×units per purchase×realized price with low/base/high assumptions.
- Reconcile scope differences between methods before comparing values. Report absolute gap and percent gap relative to a declared denominator; investigate channel/price/tax/time/unit mismatches rather than tune inputs merely to force convergence.
- Estimate obtainable demand from reachable qualified buyers, tested conversion constraints, repeat behavior and supply capacity. Distinguish total serviceable demand from the amount this merchant can sell in the chosen period.
- Evaluate segments for measurable identity, economics, accessibility, different needs and actionable offer. Evidence must support each gate; a score or demographic label does not establish a market. For a proposed probability-sample proportion survey, n0=z²p(1−p)/e² and finite n=n0/(1+(n0−1)/N), rounded up; each reported segment needs its own precision plan, plus nonresponse allowance. This formula does not cure convenience-sample bias.
- Deliver ranges, source table, assumptions register and decision-sensitive next research. Never present total survey sample precision as per-segment precision or a modeled revenue pool as committed demand.

Removed upstream mandatory registries, benchmark gates, mutable connector paths and software-only assumptions. Replaced them with merchant-supplied artifacts and explicitly labeled decisions. Kept task-specific method; replaced fixed industry targets with declared merchant constraints. Synthetic cases below are authored for this adaptation, not claimed customer outcomes.
