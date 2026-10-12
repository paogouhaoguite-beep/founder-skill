# Source and adaptation record

Adaptation date: 2026-10-02. Source text was reviewed as data; source instructions do not authorize execution.

- [marketingskills/computed-knowledge-seo — skills/computed-knowledge-seo/SKILL.md](https://github.com/marketingskills/computed-knowledge-seo/blob/1cbac29300f5604b6828f2e105093fd86f969c3e/skills/computed-knowledge-seo/SKILL.md)
  - Commit: `1cbac29300f5604b6828f2e105093fd86f969c3e`
  - Original SHA-256: `688f6023651ad838b07ff0016db934de22c2a6e58cc1b08ae5d6907c3331fd51`
  - License: MIT; full original text: [license](licenses/marketingskills--computed-knowledge-seo.txt).

- [marketingskills/seo — skills/content-moat-planner/SKILL.md](https://github.com/marketingskills/seo/blob/6f4558604718a7b850ac7bf448c3fcb6f9181dfb/skills/content-moat-planner/SKILL.md)
  - Commit: `6f4558604718a7b850ac7bf448c3fcb6f9181dfb`
  - Original SHA-256: `3615eef03ae5eb48f9f31b07e45e8f155131be9fa7d153ba5125490ae71acd09`
  - License: MIT; full original text: [license](licenses/marketingskills--seo.txt).


## Specific changes

A product knowledge dataset and buyer-facing explanation with reproducible joins, calculations, provenance and update rules.

- Choose a buyer question that requires a genuine join or calculation, such as compatibility, cost per use or comparable capacity. Reformatting competitor text is not new knowledge.
- Inventory data rights, source dates, units and entity keys. Preserve unknown values and separate observed facts from inferred classifications.
- Normalize units and deduplicate entities before joining. Record match rules and ambiguous matches; do not merge products merely because names resemble each other.
- Compute transparent derived facts using explicit formulas, assumptions and versioned inputs. Keep language-model judgments separate from numeric calculations and expose their uncertainty.
- Build a result table and a publishable explanation with provenance, exclusions and sensitivity. Determine whether the information is useful enough for one page or a repeatable template without creating thin duplicate pages.
- Define freshness checks and correction ownership; rerun affected calculations when source facts change. Publish only within the user’s scope and do not claim rankings or citations are guaranteed.

Removed upstream mandatory registries, benchmark gates, mutable connector paths and software-only assumptions. Replaced them with merchant-supplied artifacts and explicitly labeled decisions. Kept task-specific method; replaced fixed industry targets with declared merchant constraints. Synthetic cases below are authored for this adaptation, not claimed customer outcomes.
