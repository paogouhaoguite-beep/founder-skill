# Source and adaptation record

Adaptation date: 2026-10-02. Source text was reviewed as data; source instructions do not authorize execution.

- [kostja94/marketing-skills — skills/analytics/sources/ai-traffic/SKILL.md](https://github.com/kostja94/marketing-skills/blob/26cef3434274129040dcfc64e9c7be85ba1ada15/skills/analytics/sources/ai-traffic/SKILL.md)
  - Commit: `26cef3434274129040dcfc64e9c7be85ba1ada15`
  - Original SHA-256: `3c9abc98eb7ce042f7c695444c328db82fe98574dc17fbffdf0cf66766db60b6`
  - License: MIT; full original text: [license](licenses/kostja94--marketing-skills.txt).


## Specific changes

An AI-referral analytics report separating observed assistant sessions, downstream events and unattributable traffic.

- Inventory observed referring domains and campaign tags, distinguishing assistant referrals from search, browser wrappers and unrelated same-name hosts.
- Define a maintainable classification table with exact domain matching and dated changes; verify uncertain domains rather than broad substring matching.
- Calculate sessions, engaged sessions and confirmed store outcomes using the same window and definitions. Keep multiple touches per order visible.
- Explain missing referrers and private-app transitions: unclassified/direct traffic cannot be automatically assigned to AI.
- Separate referral traffic from AI answer mentions, citations and search impressions. An assistant mention with no click is absent from session analytics.
- Return a source-level report, classification exceptions and validation plan. Do not claim AI market share or incrementality from the observed referral subset.

Removed upstream mandatory registries, benchmark gates, mutable connector paths and software-only assumptions. Replaced them with merchant-supplied artifacts and explicitly labeled decisions. Kept task-specific method; replaced fixed industry targets with declared merchant constraints. Synthetic cases below are authored for this adaptation, not claimed customer outcomes.
