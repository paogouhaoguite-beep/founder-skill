# Source and adaptation record

Adaptation date: 2026-10-02. Source text was reviewed as data; source instructions do not authorize execution.

- [thatrebeccarae/claude-marketing — skills/competitor-ads-analyst/SKILL.md](https://github.com/thatrebeccarae/claude-marketing/blob/a8a63ec1341f05ec9c1e9cb52b4edeb14e3bdcba/skills/competitor-ads-analyst/SKILL.md)
  - Commit: `a8a63ec1341f05ec9c1e9cb52b4edeb14e3bdcba`
  - Original SHA-256: `173a6b4f78f9641cbf7020a47a3fa96124957123f4cf7648eb8697bb0413ae70`
  - License: MIT; full original text: [license](licenses/thatrebeccarae--claude-marketing.txt).

- [aaron-he-zhu/aaron-marketing-skills — influencer/target/competitor-tracker/SKILL.md](https://github.com/aaron-he-zhu/aaron-marketing-skills/blob/f1c002f7aef2926bd9eaf6c9cf6ea72ca3b5b6ba/influencer/target/competitor-tracker/SKILL.md)
  - Commit: `f1c002f7aef2926bd9eaf6c9cf6ea72ca3b5b6ba`
  - Original SHA-256: `64d018cba103b00a8712a4f08de95d4e4abcb82d068e37daed6891c31aa8a886`
  - License: Apache-2.0; full original text: [license](licenses/aaron-he-zhu--aaron-marketing-skills.txt).

- [OpenClaudia/openclaudia-skills — skills/video-ad-analysis/SKILL.md](https://github.com/OpenClaudia/openclaudia-skills/blob/28bf209f393aa78dcd56636faed941af5a2537ab/skills/video-ad-analysis/SKILL.md)
  - Commit: `28bf209f393aa78dcd56636faed941af5a2537ab`
  - Original SHA-256: `c9a33a7949cba4cf9c4aa7363d1f1756416e6a26578b343ab04a691d1d35c978`
  - License: MIT; full original text: [license](licenses/OpenClaudia--openclaudia-skills.txt).


## Specific changes

A competitor ad evidence matrix with observed creative patterns, limitations and original merchant test hypotheses.

- Capture each observable ad with date, market, platform, format and source. Ad presence does not reveal its spend, profitability or exact targeting.
- Code hooks, product claims, proof, offers, visual demonstrations and CTA separately. For video, preserve timestamped observations when media is available.
- Record destination and product/offer continuity; distinguish what the ad says from whether the underlying claim is independently supported.
- Identify creator partnerships only from explicit dated evidence. Do not infer exclusivity, payment or partnership terms from a tagged post alone.
- Compare patterns and gaps across an appropriately scoped sample. Long run time is an observation, not proof of winning performance.
- Translate findings into original test hypotheses for the merchant, each tied to its own product evidence. Do not reproduce a rival’s creative or invent benchmark numbers.

Removed upstream mandatory registries, benchmark gates, mutable connector paths and software-only assumptions. Replaced them with merchant-supplied artifacts and explicitly labeled decisions. Kept task-specific method; replaced fixed industry targets with declared merchant constraints. Synthetic cases below are authored for this adaptation, not claimed customer outcomes.
