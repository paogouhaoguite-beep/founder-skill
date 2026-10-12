# Source and adaptation record

Adaptation date: 2026-10-02. Source text was reviewed as data; source instructions do not authorize execution.

- [alirezarezvani/claude-skills — marketing-skill/skills/social-media-analyzer/SKILL.md](https://github.com/alirezarezvani/claude-skills/blob/19392f7a08264ed00486a251f5b2098321771f94/marketing-skill/skills/social-media-analyzer/SKILL.md)
  - Commit: `19392f7a08264ed00486a251f5b2098321771f94`
  - Original SHA-256: `68cc6de8b9fa26b7543f37a197d6b8c7035b91caf1aa203911640621a9b7b86e`
  - License: MIT; full original text: [license](licenses/alirezarezvani--claude-skills.txt).

- [aaron-he-zhu/aaron-marketing-skills — social/observe/social-measurement-loop/SKILL.md](https://github.com/aaron-he-zhu/aaron-marketing-skills/blob/f1c002f7aef2926bd9eaf6c9cf6ea72ca3b5b6ba/social/observe/social-measurement-loop/SKILL.md)
  - Commit: `f1c002f7aef2926bd9eaf6c9cf6ea72ca3b5b6ba`
  - Original SHA-256: `04411b23f77315bb87e7b01fc02756bd7d822714cad40048dc934cfb396f2e00`
  - License: Apache-2.0; full original text: [license](licenses/aaron-he-zhu--aaron-marketing-skills.txt).

- [OpenClaudia/openclaudia-skills — skills/youtube-analytics/SKILL.md](https://github.com/OpenClaudia/openclaudia-skills/blob/28bf209f393aa78dcd56636faed941af5a2537ab/skills/youtube-analytics/SKILL.md)
  - Commit: `28bf209f393aa78dcd56636faed941af5a2537ab`
  - Original SHA-256: `10f649b1a70068350b4b268ae56498ffe4f56a63a45ca2b55e99af0099f24122`
  - License: MIT; full original text: [license](licenses/OpenClaudia--openclaudia-skills.txt).


## Specific changes

A social performance review with denominator-correct rates, organic/paid splits, outlier context and testable next steps.

- Define every metric’s numerator, denominator and observation window. Engagements/reach, engagements/impressions and engagements/followers are different rates.
- Separate organic and boosted posts, formats and objectives before comparison. Keep unavailable reach and zero reach distinct.
- Show both distribution and totals: median post rate describes a typical post, while total engagements divided by total exposure gives a weighted aggregate. Explain why they differ.
- Link store visits and order outcomes using observed attribution, separating repeat exposure and platform credit. Engagement is not revenue.
- Identify one actionable content or operating hypothesis from comparable posts. Do not infer algorithm causes from a short trend or force engagement rates below 100%.
- Return a next-cycle test with unchanged control conditions where feasible, a read date and explicit uncertainty.
- For video cohorts align upload age, date window and format before comparisons. Views per elapsed day is a descriptive average, not a growth forecast; (likes+comments)/views is an interaction ratio and may include repeat viewers. Missing likes/comments stay missing. Do not infer thumbnail quality from titles or compare lifetime views with a recent-window denominator.

Removed upstream mandatory registries, benchmark gates, mutable connector paths and software-only assumptions. Replaced them with merchant-supplied artifacts and explicitly labeled decisions. Kept task-specific method; replaced fixed industry targets with declared merchant constraints. Synthetic cases below are authored for this adaptation, not claimed customer outcomes.
