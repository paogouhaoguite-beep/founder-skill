# Source and adaptation record

Adaptation date: 2026-10-02. Source text was reviewed as data; source instructions do not authorize execution.

- [aaron-he-zhu/aaron-marketing-skills — social/observe/dark-social-attributor/SKILL.md](https://github.com/aaron-he-zhu/aaron-marketing-skills/blob/f1c002f7aef2926bd9eaf6c9cf6ea72ca3b5b6ba/social/observe/dark-social-attributor/SKILL.md)
  - Commit: `f1c002f7aef2926bd9eaf6c9cf6ea72ca3b5b6ba`
  - Original SHA-256: `4d9f03dafaa06f95ac85cd8b631940916456a755b1a433e36e86fe2fde7fc2fc`
  - License: Apache-2.0; full original text: [license](licenses/aaron-he-zhu--aaron-marketing-skills.txt).

- [kostja94/marketing-skills — skills/analytics/sources/traffic/SKILL.md](https://github.com/kostja94/marketing-skills/blob/26cef3434274129040dcfc64e9c7be85ba1ada15/skills/analytics/sources/traffic/SKILL.md)
  - Commit: `26cef3434274129040dcfc64e9c7be85ba1ada15`
  - Original SHA-256: `7a3be7d3b923fdab7f5ee48586b1ce6ade8d32f302ea0f097eaa8747a3c83e4d`
  - License: MIT; full original text: [license](licenses/kostja94--marketing-skills.txt).


## Specific changes

A dark-social evidence brief combining direct-traffic segments, self-reports and share-link hygiene without fabricating attribution.

- Inventory measurable share links and private sharing paths. Direct traffic includes typed URLs, missing referrers and other causes; it is not synonymous with dark social.
- Specify a stable UTM taxonomy for owned share buttons and campaign links. Do not add campaign UTMs to internal navigation or assume copied address-bar URLs retain attribution.
- Design an optional, low-friction “how did you hear about us” question and keep free text plus normalized categories; discuss form friction instead of mandating an extra field.
- Segment direct sessions by deep landing URLs, device and time, comparing like windows. Label plausible private-sharing exposure as a hypothesis rather than assigning every session to social.
- Compare self-reports and branded search around activity dates. Describe association, sampling bias and alternate drivers; never add self-reports to orders already counted.
- Deliver ranges or evidence tiers where attribution is incomplete. Recommend a controlled test when a causal budget decision is needed.

Removed upstream mandatory registries, benchmark gates, mutable connector paths and software-only assumptions. Replaced them with merchant-supplied artifacts and explicitly labeled decisions. Kept task-specific method; replaced fixed industry targets with declared merchant constraints. Synthetic cases below are authored for this adaptation, not claimed customer outcomes.
