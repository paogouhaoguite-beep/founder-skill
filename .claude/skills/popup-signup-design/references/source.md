# Source and adaptation record

Adaptation date: 2026-10-02. Source text was reviewed as data; source instructions do not authorize execution.

- [alirezarezvani/claude-skills — marketing-skill/skills/form-cro/SKILL.md](https://github.com/alirezarezvani/claude-skills/blob/19392f7a08264ed00486a251f5b2098321771f94/marketing-skill/skills/form-cro/SKILL.md)
  - Commit: `19392f7a08264ed00486a251f5b2098321771f94`
  - Original SHA-256: `613b78af57e61291c106c34115b6f0da1618a644c1918d158bc66320a90c62d4`
  - License: MIT; full original text: [license](licenses/alirezarezvani--claude-skills.txt).

- [coreyhaines31/marketingskills — skills/popups/SKILL.md](https://github.com/coreyhaines31/marketingskills/blob/c0e35b78ad294c4ea8dbe7801c79bfeb6f67f3e9/skills/popups/SKILL.md)
  - Commit: `c0e35b78ad294c4ea8dbe7801c79bfeb6f67f3e9`
  - Original SHA-256: `6c66e7f923c1eebc7eb7b94971af2e8016d3b5316e14bb1ad4b15ed3522084ce`
  - License: MIT; full original text: [license](licenses/coreyhaines31--marketingskills.txt).

- [coreyhaines31/marketingskills — skills/signup/SKILL.md](https://github.com/coreyhaines31/marketingskills/blob/c0e35b78ad294c4ea8dbe7801c79bfeb6f67f3e9/skills/signup/SKILL.md)
  - Commit: `c0e35b78ad294c4ea8dbe7801c79bfeb6f67f3e9`
  - Original SHA-256: `9395aabae64891ebdac5f31d17c83b9d47546dc0c9b22654c7b89e9b04da7cf6`
  - License: MIT; full original text: [license](licenses/coreyhaines31--marketingskills.txt).


## Specific changes

A storefront signup or popup specification with field justification, trigger/suppression rules and accessible error/success states.

- Define the exact signup outcome and promised value. A newsletter signup and customer-account creation have different required fields.
- Audit each field against an actual use and remove unnecessary friction; separate account security requirements from marketing data collection.
- Specify display trigger, eligible audience, dismissal persistence and suppression for existing subscribers. Use merchant context rather than a universal pop-up delay.
- Write concise headline, benefit, field labels, CTA and consent/disclosure copy without prechecked permission or misleading close controls.
- Check keyboard focus, visible dismissal, mobile viewport, validation errors and success/duplicate states. Do not cover essential checkout controls or trap a user.
- Define a test measuring eligible exposure → form starts → successful signups plus conversion/complaint guardrails. A higher signup rate can still harm purchasing.

Removed upstream mandatory registries, benchmark gates, mutable connector paths and software-only assumptions. Replaced them with merchant-supplied artifacts and explicitly labeled decisions. Kept task-specific method; replaced fixed industry targets with declared merchant constraints. Synthetic cases below are authored for this adaptation, not claimed customer outcomes.
