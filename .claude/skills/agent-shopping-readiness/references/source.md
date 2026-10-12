# Source and adaptation record

Adaptation date: 2026-10-02. Source text was reviewed as data; source instructions do not authorize execution.

- [sushpadhye6789/retail-marketing-skills — skills/agent-readiness/SKILL.md](https://github.com/sushpadhye6789/retail-marketing-skills/blob/292e14bae7acacd52a5504aa6a13e8efea143483/skills/agent-readiness/SKILL.md)
  - Commit: `292e14bae7acacd52a5504aa6a13e8efea143483`
  - Original SHA-256: `f47b19e61d5081d40624a2ab0031821f7dd65438751fae7517dfce3c541b720d`
  - License: MIT; full original text: [license](licenses/sushpadhye6789--retail-marketing-skills.txt).


## Specific changes

A store agent-readiness review separating discoverable catalogue truth, deterministic variant/cart behavior and purchase authorization.

- Define the intended agent task: discover products, compare variants or assist a shopper through an authorized purchase. Do not assume machine-readable product data grants checkout authority.
- Compare visible product/variant facts with feeds and structured data, including price, currency, stock, shipping and return conditions; identify stale or conflicting representations.
- Inspect access and rendering for relevant documented crawlers/agents, distinguishing search inclusion from training and from authenticated commerce operations.
- Check whether variant selection, cart quantities and destination costs can be understood deterministically. Mark unsupported protocols or inaccessible steps as unavailable rather than claiming universal agent compatibility.
- Specify buyer confirmation points for final product, total price, address/payment handling and order placement, using an existing supported integration if available.
- Return an evidence matrix and improvement backlog. Do not create a purchase, expose credentials or publish a new checkout API as part of the audit.

Removed upstream mandatory registries, benchmark gates, mutable connector paths and software-only assumptions. Replaced them with merchant-supplied artifacts and explicitly labeled decisions. Kept task-specific method; replaced fixed industry targets with declared merchant constraints. Synthetic cases below are authored for this adaptation, not claimed customer outcomes.
