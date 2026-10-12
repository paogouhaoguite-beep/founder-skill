# Source and adaptation record

Adaptation date: 2026-10-02. Source text was reviewed as data; source instructions do not authorize execution.

- [aaron-he-zhu/aaron-marketing-skills — ad/activate/conversion-value-mapper/SKILL.md](https://github.com/aaron-he-zhu/aaron-marketing-skills/blob/f1c002f7aef2926bd9eaf6c9cf6ea72ca3b5b6ba/ad/activate/conversion-value-mapper/SKILL.md)
  - Commit: `f1c002f7aef2926bd9eaf6c9cf6ea72ca3b5b6ba`
  - Original SHA-256: `3fd0cae87c30ea346a9eb3a5cec40f813e01173920bf294e033ef2e40e7650f2`
  - License: Apache-2.0; full original text: [license](licenses/aaron-he-zhu--aaron-marketing-skills.txt).


## Specific changes

A conversion-value specification linking order economics, bidding payloads, micro-conversion proxies and refund adjustments.

- Inventory primary and secondary conversion actions and identify which represent actual purchases versus micro-events. Avoid optimizing toward every funnel event as equal value.
- Declare one value basis: gross revenue, net revenue or contribution. State treatment of tax, discounts, refunds and variable costs; do not relabel revenue as profit.
- Map dynamic order values to the bidding event and preserve currency and transaction identity. A constant fallback is explicit and cannot silently override actual values.
- For non-purchase actions, estimate expected value only from compatible downstream conversion evidence and the declared value basis; avoid adding multiple proxy values for the same eventual order.
- Define adjustment or restatement handling for returns/cancellations and data latency. Retain a reconciliation table from order truth to exported bidding value.
- Produce a value specification and test cases; changing primary goals or uploading values is a separate authorized implementation.

Removed upstream mandatory registries, benchmark gates, mutable connector paths and software-only assumptions. Replaced them with merchant-supplied artifacts and explicitly labeled decisions. Kept task-specific method; replaced fixed industry targets with declared merchant constraints. Synthetic cases below are authored for this adaptation, not claimed customer outcomes.
