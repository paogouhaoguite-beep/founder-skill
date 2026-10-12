# Source and adaptation record

Adaptation date: 2026-10-02. Source text was reviewed as data; source instructions do not authorize execution.

- [coreyhaines31/marketingskills — skills/free-tools/SKILL.md](https://github.com/coreyhaines31/marketingskills/blob/c0e35b78ad294c4ea8dbe7801c79bfeb6f67f3e9/skills/free-tools/SKILL.md)
  - Commit: `c0e35b78ad294c4ea8dbe7801c79bfeb6f67f3e9`
  - Original SHA-256: `609158ee26c6005cf6138635a1a8ac4928322651c82ba13584db19d610d61e6b`
  - License: MIT; full original text: [license](licenses/coreyhaines31--marketingskills.txt).


## Specific changes

A product-selector or calculator specification with traceable decision rules, no-match behavior and maintenance requirements.

- Define one useful decision the tool should support, such as size, quantity or compatible accessory. It must provide value even without a purchase.
- Map each input to a rule and source. Separate hard compatibility constraints from preference-based ranking; unknown attributes cannot pass a hard constraint.
- Create the smallest decision table or calculation and test representative and boundary rows before specifying UI.
- Explain results with the inputs and tradeoffs, including no-match or insufficient-data outcomes; do not always force a product recommendation.
- Estimate build, maintenance and data-refresh costs against plausible value scenarios, explicitly labeling assumptions instead of promising traffic.
- Deliver a tool specification, sample results, validation cases and catalogue update contract. Do not publish or collect user data without implementation scope.

Removed upstream mandatory registries, benchmark gates, mutable connector paths and software-only assumptions. Replaced them with merchant-supplied artifacts and explicitly labeled decisions. Kept task-specific method; replaced fixed industry targets with declared merchant constraints. Synthetic cases below are authored for this adaptation, not claimed customer outcomes.
