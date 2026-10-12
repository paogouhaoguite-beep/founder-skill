# Source and adaptation record

Adaptation date: 2026-10-02. Source text was reviewed as data; source instructions do not authorize execution.

- [aaron-he-zhu/aaron-marketing-skills — ad/activate/placement-exclusion-manager/SKILL.md](https://github.com/aaron-he-zhu/aaron-marketing-skills/blob/f1c002f7aef2926bd9eaf6c9cf6ea72ca3b5b6ba/ad/activate/placement-exclusion-manager/SKILL.md)
  - Commit: `f1c002f7aef2926bd9eaf6c9cf6ea72ca3b5b6ba`
  - Original SHA-256: `a008d7eeba7774dfde99f37df0d1991f938a1fa32b67e0b51354ac2dc05ae2ea`
  - License: Apache-2.0; full original text: [license](licenses/aaron-he-zhu--aaron-marketing-skills.txt).

- [thatrebeccarae/claude-marketing — skills/wasted-spend-finder/SKILL.md](https://github.com/thatrebeccarae/claude-marketing/blob/a8a63ec1341f05ec9c1e9cb52b4edeb14e3bdcba/skills/wasted-spend-finder/SKILL.md)
  - Commit: `a8a63ec1341f05ec9c1e9cb52b4edeb14e3bdcba`
  - Original SHA-256: `8e8248bd7bd695457c46b437df192891a5362947bd0de96ac72116783f1d88b1`
  - License: MIT; full original text: [license](licenses/thatrebeccarae--claude-marketing.txt).


## Specific changes

An evidence-based placement exclusion queue separating suitability violations, uncertain efficiency and observed spend loss.

- Normalize placements, network, date and spend so aliases do not split one inventory source. Preserve unavailable placement coverage.
- Separate suitability concerns from efficiency concerns. A harmful placement may need action even with conversions; zero short-window conversions do not alone prove waste.
- Inspect representative placements and record the actual relevance or safety evidence. Avoid blacklisting from a vague domain name or a third-party toxicity score alone.
- Evaluate performance only after the declared attribution lag and minimum evidence needed for the decision. State the merchant-selected loss cap rather than a universal zero-conversion rule.
- Propose exact exclusions with scope, reason, expected reach tradeoff and reversible test or review date. Do not expand one bad placement into an unsupported network-wide conclusion.
- Return an exclusion review queue and unresolved rows; actual account edits require scoped authorization and readback.

Removed upstream mandatory registries, benchmark gates, mutable connector paths and software-only assumptions. Replaced them with merchant-supplied artifacts and explicitly labeled decisions. Kept task-specific method; replaced fixed industry targets with declared merchant constraints. Synthetic cases below are authored for this adaptation, not claimed customer outcomes.
