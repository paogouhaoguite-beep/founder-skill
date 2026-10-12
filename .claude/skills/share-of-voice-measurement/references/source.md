# Source and adaptation record

Adaptation date: 2026-10-02. Source text was reviewed as data; source instructions do not authorize execution.

- [aaron-he-zhu/aaron-marketing-skills — social/observe/share-of-voice-tracker/SKILL.md](https://github.com/aaron-he-zhu/aaron-marketing-skills/blob/f1c002f7aef2926bd9eaf6c9cf6ea72ca3b5b6ba/social/observe/share-of-voice-tracker/SKILL.md)
  - Commit: `f1c002f7aef2926bd9eaf6c9cf6ea72ca3b5b6ba`
  - Original SHA-256: `b999baa3c761c6f1f82c0ade2e407f41721af0de9fff541611fea7ed94d7c729`
  - License: Apache-2.0; full original text: [license](licenses/aaron-he-zhu--aaron-marketing-skills.txt).


## Specific changes

A panel-controlled share-of-voice report with reproducible denominators, platform splits and explicit series breaks.

- Lock the brand panel, aliases, exclusions, platforms and observation windows before computing trends.
- Count comparable relevant mentions for each brand on each platform. Preserve missing values rather than replacing them with zero.
- Calculate brand mentions divided by all panel mentions, including the brand itself. Show numerator and denominator beside each percentage.
- Report per-platform results first. A combined share must state its weighting and coverage; raw cross-platform addition can overweight the easiest source to collect.
- If using sentiment-weighted share, retain unweighted share and explain coding, sample size and weights. Engagement or pageview share is a different metric, not interchangeable with mention share.
- Mark panel, query and access changes as series breaks. Explain observed shifts without asserting market share or sales impact.

Removed upstream mandatory registries, benchmark gates, mutable connector paths and software-only assumptions. Replaced them with merchant-supplied artifacts and explicitly labeled decisions. Kept task-specific method; replaced fixed industry targets with declared merchant constraints. Synthetic cases below are authored for this adaptation, not claimed customer outcomes.
