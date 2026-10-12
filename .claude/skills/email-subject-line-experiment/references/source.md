# Source and adaptation record

Adaptation date: 2026-10-02. Source text was reviewed as data; source instructions do not authorize execution.

- [OpenClaudia/openclaudia-skills — skills/email-subject-lines/SKILL.md](https://github.com/OpenClaudia/openclaudia-skills/blob/28bf209f393aa78dcd56636faed941af5a2537ab/skills/email-subject-lines/SKILL.md)
  - Commit: `28bf209f393aa78dcd56636faed941af5a2537ab`
  - Original SHA-256: `314bf56aba260d7b414899da61dea5b62650d4ad0cd566276fd6d1e9c1f3e203`
  - License: MIT; full original text: [license](licenses/OpenClaudia--openclaudia-skills.txt).

- [aaron-he-zhu/aaron-marketing-skills — email/deliver/send-experiment-designer/SKILL.md](https://github.com/aaron-he-zhu/aaron-marketing-skills/blob/f1c002f7aef2926bd9eaf6c9cf6ea72ca3b5b6ba/email/deliver/send-experiment-designer/SKILL.md)
  - Commit: `f1c002f7aef2926bd9eaf6c9cf6ea72ca3b5b6ba`
  - Original SHA-256: `7d0f3e2825a408a20ac5ac4a6514ab093c34bebb9450ebf6e481e21f84d918ce`
  - License: Apache-2.0; full original text: [license](licenses/aaron-he-zhu--aaron-marketing-skills.txt).

- [aaron-he-zhu/aaron-marketing-skills — email/engage/subject-line-lab/SKILL.md](https://github.com/aaron-he-zhu/aaron-marketing-skills/blob/f1c002f7aef2926bd9eaf6c9cf6ea72ca3b5b6ba/email/engage/subject-line-lab/SKILL.md)
  - Commit: `f1c002f7aef2926bd9eaf6c9cf6ea72ca3b5b6ba`
  - Original SHA-256: `6b7431ad52a51543abc5d67bb1c822495243cf17d255a036d729b9a1a2af3a5d`
  - License: Apache-2.0; full original text: [license](licenses/aaron-he-zhu--aaron-marketing-skills.txt).


## Specific changes

A subject/preheader test plan with truthful variants, fixed experimental conditions and uncertainty-aware readout.

- Generate subjects from the actual content and offer, preserving conditions. Count characters as an observable property; screen for misleading urgency and fake reply prefixes.
- Pair each subject with a preheader that adds useful context rather than repeating it. Treat possible truncation as a render check, not a universal character cutoff.
- Define one changed variable, randomization unit, audience eligibility and allocation. Keep content, sender and timing comparable unless timing is the variable being tested.
- Predeclare the primary outcome, observation window and decision rule. Opens may be distorted by privacy features; prefer meaningful click/order outcomes when the goal and sample support them.
- Record creative versions and actual delivered counts per cell. Check allocation imbalance, suppression changes, bot clicks and overlapping sends before interpreting results.
- Report absolute and relative differences with uncertainty; do not choose a statistical winner from a tiny early sample or automatically mail the rest of the list.

Removed upstream mandatory registries, benchmark gates, mutable connector paths and software-only assumptions. Replaced them with merchant-supplied artifacts and explicitly labeled decisions. Kept task-specific method; replaced fixed industry targets with declared merchant constraints. Synthetic cases below are authored for this adaptation, not claimed customer outcomes.
