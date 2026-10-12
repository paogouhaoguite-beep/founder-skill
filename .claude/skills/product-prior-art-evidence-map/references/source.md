# Source and adaptation record

Adaptation date: 2026-10-02. Source text was reviewed as data; source instructions do not authorize execution.

- [alirezarezvani/claude-skills — research/patent/skills/patent/SKILL.md](https://github.com/alirezarezvani/claude-skills/blob/19392f7a08264ed00486a251f5b2098321771f94/research/patent/skills/patent/SKILL.md)
  - Commit: `19392f7a08264ed00486a251f5b2098321771f94`
  - Original SHA-256: `7cf68646b2572da081b0769e001f1379665c4f33de43c9651317112c147e84ba`
  - License: MIT; full original text: [license](licenses/alirezarezvani--claude-skills.txt).


## Specific changes

A patent-family and feature-to-claim evidence map with identifiers, dates, jurisdictions, source passages, status verification and questions for qualified counsel.

- Break the physical product into technical features and mechanisms. Define the search purpose: landscape/prior-art discovery versus collecting documents for freedom-to-operate counsel. Do not convert a search result into a legal clearance verdict.
- Build keyword/synonym and classification queries using verified CPC/IPC entries. Search relevant patent registers and non-patent technical literature, recording query, date and database; supplied documents support an offline partial map.
- Resolve publication numbers, applicants/inventors and patent families. Keep priority, filing, publication and grant dates distinct; deduplicate family variants while preserving jurisdiction-specific claim sets and legal status evidence.
- Read the relevant claims and supporting description/drawings. Map each product feature to exact claim passage or no identified match. Independent claims are not always limited to claim1, and a dependent claim adds limitations rather than automatically proving an inventive step.
- Record jurisdiction, verified status and status-as-of date from authoritative records when available. Application, granted, expired or abandoned labels may differ within a family; unknown status stays unknown. Do not infer enforceability or a date-specific novelty conclusion from title similarity.
- Deliver a ranked document/feature evidence map and search gaps for qualified review. Explain priority by technical relevance and evidence completeness, not an invented infringement probability. The output supports investigation; it does not establish novelty, validity, patentability or freedom to operate.

Removed upstream mandatory registries, benchmark gates, mutable connector paths and software-only assumptions. Replaced them with merchant-supplied artifacts and explicitly labeled decisions. Kept task-specific method; replaced fixed industry targets with declared merchant constraints. Synthetic cases below are authored for this adaptation, not claimed customer outcomes.
