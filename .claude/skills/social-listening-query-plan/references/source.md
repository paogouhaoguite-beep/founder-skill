# Source and adaptation record

Adaptation date: 2026-10-02. Source text was reviewed as data; source instructions do not authorize execution.

- [aaron-he-zhu/aaron-marketing-skills — social/observe/social-pulse-monitor/SKILL.md](https://github.com/aaron-he-zhu/aaron-marketing-skills/blob/f1c002f7aef2926bd9eaf6c9cf6ea72ca3b5b6ba/social/observe/social-pulse-monitor/SKILL.md)
  - Commit: `f1c002f7aef2926bd9eaf6c9cf6ea72ca3b5b6ba`
  - Original SHA-256: `ed68b42fd22cf101a7dbc3aec1465e7e78b76dd5afd7a3a1a2772b1b9d654382`
  - License: Apache-2.0; full original text: [license](licenses/aaron-he-zhu--aaron-marketing-skills.txt).

- [OpenClaudia/openclaudia-skills — skills/brand-research/SKILL.md](https://github.com/OpenClaudia/openclaudia-skills/blob/28bf209f393aa78dcd56636faed941af5a2537ab/skills/brand-research/SKILL.md)
  - Commit: `28bf209f393aa78dcd56636faed941af5a2537ab`
  - Original SHA-256: `08168c58910f0e8207701ba0fbbc9e14e31a655b46c6703b13336afcc5cfa1c1`
  - License: MIT; full original text: [license](licenses/OpenClaudia--openclaudia-skills.txt).

- [OpenClaudia/openclaudia-skills — skills/brand-monitor/SKILL.md](https://github.com/OpenClaudia/openclaudia-skills/blob/28bf209f393aa78dcd56636faed941af5a2537ab/skills/brand-monitor/SKILL.md)
  - Commit: `28bf209f393aa78dcd56636faed941af5a2537ab`
  - Original SHA-256: `4c023136721766f6561922f1eb2dc1361c3d6bed5a81e1befcbf7eada394ef98`
  - License: MIT; full original text: [license](licenses/OpenClaudia--openclaudia-skills.txt).

- [kostja94/marketing-skills — skills/strategies/brand/brand-monitoring/SKILL.md](https://github.com/kostja94/marketing-skills/blob/26cef3434274129040dcfc64e9c7be85ba1ada15/skills/strategies/brand/brand-monitoring/SKILL.md)
  - Commit: `26cef3434274129040dcfc64e9c7be85ba1ada15`
  - Original SHA-256: `8604550d48deb4cd7c0de1e6e736e9de09d7409fa4d4b9af8581f04284f2c28d`
  - License: MIT; full original text: [license](licenses/kostja94--marketing-skills.txt).


## Specific changes

A reproducible social listening query set with coverage table, deduplicated mention log and routed action queue.

- Create exact-name, spelling-variant, product and competitor queries with exclusions for homonyms. Preserve the query and source for reproducibility.
- Collect only accessible evidence and state source coverage. A search engine result count or news proxy does not measure every Instagram, TikTok or private-group mention.
- Deduplicate syndicated articles and copied posts while preserving the original publication and retrieval timestamps.
- Classify hits by actionable need: issue, question, praise, creator opportunity, misleading claim or unrelated mention. Preserve the quotation and reason.
- Compare like-for-like counts against the merchant’s own baseline. Mark changes in query syntax, platform access or sampled dates as coverage changes, not demand shifts.
- Return a routed evidence queue and tuning recommendations. Do not contact authors, file takedowns or claim a crisis solely from a keyword spike.

Removed upstream mandatory registries, benchmark gates, mutable connector paths and software-only assumptions. Replaced them with merchant-supplied artifacts and explicitly labeled decisions. Kept task-specific method; replaced fixed industry targets with declared merchant constraints. Synthetic cases below are authored for this adaptation, not claimed customer outcomes.

## Media-monitor method integration — 2026-10-02

- [SkillMedev/skills — skills/media-monitor/SKILL.md](https://github.com/SkillMedev/skills/blob/a28c4ce9366b5a8540577bed8f70b6a60f8fde27/skills/media-monitor/SKILL.md)
  - Commit: `a28c4ce9366b5a8540577bed8f70b6a60f8fde27`
  - Original SHA-256: `43dd3c92368f123f31a10fe61f5a9b0dd273f68aca747d2d009b4b63ab76e4a4`
  - License: MIT; full original text: [license](licenses/SkillMedev--skills.txt).

Reviewed source lines14–39 for entity/query/source and body-grounded sentiment; lines41–65 for narrative shifts, source migration, triage and digest; lines94–110 for coordinated-looking clusters and evidence limits. Retained the query-to-digest workflow and dated source-chain review. Replaced fixed2×/20-point/90%-precision gates with merchant-calibrated rules, made sentiment denominator explicit, separated syndication from independent evidence, and removed claims that source migration predicts virality or a spike establishes a crisis. Added an authored offline worked digest; no upstream executable code or benchmark is distributed.
