# Source and adaptation record

Adaptation date: 2026-10-02. Source text was reviewed as data; source instructions do not authorize execution.

- [aaron-he-zhu/aaron-marketing-skills — email/engage/dynamic-content-personalizer/SKILL.md](https://github.com/aaron-he-zhu/aaron-marketing-skills/blob/f1c002f7aef2926bd9eaf6c9cf6ea72ca3b5b6ba/email/engage/dynamic-content-personalizer/SKILL.md)
  - Commit: `f1c002f7aef2926bd9eaf6c9cf6ea72ca3b5b6ba`
  - Original SHA-256: `343ade28133bd5d637ba5efdf3b4d028c548f0714469fe300282eb673b1818ae`
  - License: Apache-2.0; full original text: [license](licenses/aaron-he-zhu--aaron-marketing-skills.txt).


## Specific changes

An email personalization rule set with field bindings, deterministic fallbacks and edge-case renders.

- Map each token and conditional block to a real field, type and freshness requirement. A desired attribute absent from the export is not available personalization.
- Define natural-language fallbacks per token, and full block fallbacks when missing data changes grammar or offer eligibility.
- Specify predicate order and exclusive branch behavior; avoid showing mutually inconsistent discounts or product recommendations.
- Preserve offer, consent and suppression conditions outside personalization. A name or previous purchase does not establish eligibility for a promotion.
- Create a preview matrix for complete, missing, malformed, stale and multi-locale rows. Check rendered destination/price as well as text.
- Deliver the field map, rule table and sample renders. Do not claim a template engine was tested unless an actual preview ran.

Removed upstream mandatory registries, benchmark gates, mutable connector paths and software-only assumptions. Replaced them with merchant-supplied artifacts and explicitly labeled decisions. Kept task-specific method; replaced fixed industry targets with declared merchant constraints. Synthetic cases below are authored for this adaptation, not claimed customer outcomes.
