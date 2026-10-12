# Source and adaptation record

Adaptation date: 2026-10-02. Source text was reviewed as data; source instructions do not authorize execution.

- [alirezarezvani/claude-skills — research/litreview/skills/litreview/SKILL.md](https://github.com/alirezarezvani/claude-skills/blob/19392f7a08264ed00486a251f5b2098321771f94/research/litreview/skills/litreview/SKILL.md)
  - Commit: `19392f7a08264ed00486a251f5b2098321771f94`
  - Original SHA-256: `f2f14318547dd689dd617219d115cfc12a4c3a36f4118a9dae0bd717f17b0f09`
  - License: MIT; full original text: [license](licenses/alirezarezvani--claude-skills.txt).


## Specific changes

A source-linked literature evidence map with study extraction rows, exact claim applicability, conflicting findings, search log and a bounded internal recommendation.

- Translate the proposed claim into population, intervention/exposure, comparator, outcome and conditions. Separate efficacy, mechanism, durability and safety questions; do not imply evidence for an ingredient automatically validates the finished product.
- Build a query ledger using synonyms and subquestions; search relevant primary literature and reviews, including conflicting and null findings. Use supplied full texts offline; distinguish abstract-only evidence and inaccessible papers. Record search date, database and inclusion criteria.
- Deduplicate by DOI or title/authors/year, link preprints to later versions and label corrections/retractions when verified. Citation count and journal prestige are discovery aids, not automatic quality weights.
- Extract study design, sample, comparator, dose/material specification, use conditions, endpoint/timepoint, effect size and uncertainty, funding and limitations. Preserve denominators and distinguish statistical evidence from practical importance; do not pool incompatible endpoints.
- Compare evidence by applicability to the exact commercial product and customer. Mechanistic, animal, laboratory and human outcomes must remain separate. Explain contradictions by methods/population before calling them a consensus.
- Return a claim-to-evidence matrix, reading order, search coverage and unresolved gaps. Draft only a bounded internal conclusion; regulated claims need applicable current authoritative requirements and qualified review before use. Do not fabricate citations or declare a systematic review unless the actual protocol and coverage support it.

Removed upstream mandatory registries, benchmark gates, mutable connector paths and software-only assumptions. Replaced them with merchant-supplied artifacts and explicitly labeled decisions. Kept task-specific method; replaced fixed industry targets with declared merchant constraints. Synthetic cases below are authored for this adaptation, not claimed customer outcomes.
