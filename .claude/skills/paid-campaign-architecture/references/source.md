# Source and adaptation record

Adaptation date: 2026-10-02. Source text was reviewed as data; source instructions do not authorize execution.

- [thatrebeccarae/claude-marketing — skills/account-structure-review/SKILL.md](https://github.com/thatrebeccarae/claude-marketing/blob/a8a63ec1341f05ec9c1e9cb52b4edeb14e3bdcba/skills/account-structure-review/SKILL.md)
  - Commit: `a8a63ec1341f05ec9c1e9cb52b4edeb14e3bdcba`
  - Original SHA-256: `da43e792e037cf502b1a0b4f37e4baf1cf953a3305db062b0b1a20ddfff00e68`
  - License: MIT; full original text: [license](licenses/thatrebeccarae--claude-marketing.txt).

- [aaron-he-zhu/aaron-marketing-skills — ad/research/campaign-architect/SKILL.md](https://github.com/aaron-he-zhu/aaron-marketing-skills/blob/f1c002f7aef2926bd9eaf6c9cf6ea72ca3b5b6ba/ad/research/campaign-architect/SKILL.md)
  - Commit: `f1c002f7aef2926bd9eaf6c9cf6ea72ca3b5b6ba`
  - Original SHA-256: `00701af99252c60aa8af082ebb4000e0d08d3f3e0d14847efc037bdbf4d78469`
  - License: Apache-2.0; full original text: [license](licenses/aaron-he-zhu--aaron-marketing-skills.txt).

- [kostja94/marketing-skills — skills/paid-ads/platforms/google-ads/SKILL.md](https://github.com/kostja94/marketing-skills/blob/26cef3434274129040dcfc64e9c7be85ba1ada15/skills/paid-ads/platforms/google-ads/SKILL.md)
  - Commit: `26cef3434274129040dcfc64e9c7be85ba1ada15`
  - Original SHA-256: `6d729ce6381c04b4034ad3342c77badf79451e4e65e0a798a45113fdf04502c9`
  - License: MIT; full original text: [license](licenses/kostja94--marketing-skills.txt).

- [thatrebeccarae/claude-marketing — skills/microsoft-ads/SKILL.md](https://github.com/thatrebeccarae/claude-marketing/blob/a8a63ec1341f05ec9c1e9cb52b4edeb14e3bdcba/skills/microsoft-ads/SKILL.md)
  - Commit: `a8a63ec1341f05ec9c1e9cb52b4edeb14e3bdcba`
  - Original SHA-256: `2e2a955b794f16701bcc6caf8dcfcaebd6dd06e1a8c9cf848c24b45ab0fedf73`
  - License: MIT; full original text: [license](licenses/thatrebeccarae--claude-marketing.txt).

- [thatrebeccarae/claude-marketing — skills/tiktok-ads/SKILL.md](https://github.com/thatrebeccarae/claude-marketing/blob/a8a63ec1341f05ec9c1e9cb52b4edeb14e3bdcba/skills/tiktok-ads/SKILL.md)
  - Commit: `a8a63ec1341f05ec9c1e9cb52b4edeb14e3bdcba`
  - Original SHA-256: `3346258a16f2a781415ee511f8c554c92b43f662b8a9cb97d8a1208c03a0db7d`
  - License: MIT; full original text: [license](licenses/thatrebeccarae--claude-marketing.txt).

- [thatrebeccarae/claude-marketing — skills/cross-platform-audit/SKILL.md](https://github.com/thatrebeccarae/claude-marketing/blob/a8a63ec1341f05ec9c1e9cb52b4edeb14e3bdcba/skills/cross-platform-audit/SKILL.md)
  - Commit: `a8a63ec1341f05ec9c1e9cb52b4edeb14e3bdcba`
  - Original SHA-256: `d8de92530075056f2824c64fe2e671356711b46e45c406b1d6411db3be598c02`
  - License: MIT; full original text: [license](licenses/thatrebeccarae--claude-marketing.txt).


## Specific changes

A paid-media account architecture and migration plan aligning campaign roles, signal ownership, exclusions and platform-specific checks.

- Map campaigns to distinct objectives, markets, products and economic constraints. Consolidate only when those settings are compatible; smaller campaign count is not inherently better.
- Separate acquisition, retention, brand demand and testing roles where control or economics require it. Avoid blanket claims that broad and exact keywords automatically bid against themselves.
- Choose search, shopping/feed, social or automated formats according to intent, signal and asset readiness; show the tradeoff between control and automation.
- Create an account map of campaign/group, goal, audience/feed, exclusions, conversion/value basis and budget owner. Diagnose overlap from actual eligibility/auction evidence, not names alone.
- For platform-specific adaptations inspect native data: Microsoft imported settings/UET, TikTok creative permissions and event matching, Google feed and search settings. Verify current provider requirements before implementation.
- Deliver a reversible migration plan with baseline, staged changes and duplicate-conversion safeguards. Do not move spend, delete campaigns or assume learning is complete from a fixed day count.

Removed upstream mandatory registries, benchmark gates, mutable connector paths and software-only assumptions. Replaced them with merchant-supplied artifacts and explicitly labeled decisions. Kept task-specific method; replaced fixed industry targets with declared merchant constraints. Synthetic cases below are authored for this adaptation, not claimed customer outcomes.
