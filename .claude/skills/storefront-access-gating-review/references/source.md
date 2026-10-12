# Source and adaptation record

Adaptation date: 2026-10-02. Source text was reviewed as data; source instructions do not authorize execution.

- [sushpadhye6789/retail-marketing-skills — skills/paywalls/SKILL.md](https://github.com/sushpadhye6789/retail-marketing-skills/blob/292e14bae7acacd52a5504aa6a13e8efea143483/skills/paywalls/SKILL.md)
  - Commit: `292e14bae7acacd52a5504aa6a13e8efea143483`
  - Original SHA-256: `fc03cdc2017e700568ebb14d181385eb90f98459cacecefb3bec586b8fc5ac24`
  - License: MIT; full original text: [license](licenses/sushpadhye6789--retail-marketing-skills.txt).


## Specific changes

A storefront access-gate review with entitlement logic, customer recovery paths and inventory-versus-permission distinctions.

- Identify whether the gate controls legal access, wholesale pricing, member access or a limited product drop. A growth tactic is not automatically a legitimate access requirement.
- Map exact entitlements and the minimum verification needed; preserve public product facts and terms necessary for an informed decision where appropriate.
- Design clear pre-gate explanation, eligibility steps, failure/help path and return to the intended product after authentication.
- Separate inventory reservation from permission to view or purchase. A verified member is not guaranteed stock unless the system reserves it.
- Review friction and exclusion on mobile and assistive technology, with special attention to existing eligible customers whose session expires.
- Return a gate decision matrix and event plan. Do not remove mandatory legal controls or add deceptive scarcity to force registration.

Removed upstream mandatory registries, benchmark gates, mutable connector paths and software-only assumptions. Replaced them with merchant-supplied artifacts and explicitly labeled decisions. Kept task-specific method; replaced fixed industry targets with declared merchant constraints. Synthetic cases below are authored for this adaptation, not claimed customer outcomes.
