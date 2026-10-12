# Source and adaptation record

Adaptation date: 2026-10-02. Source text was reviewed as data; source instructions do not authorize execution.

- [aaron-he-zhu/aaron-marketing-skills — ad/research/audience-segment-builder/SKILL.md](https://github.com/aaron-he-zhu/aaron-marketing-skills/blob/f1c002f7aef2926bd9eaf6c9cf6ea72ca3b5b6ba/ad/research/audience-segment-builder/SKILL.md)
  - Commit: `f1c002f7aef2926bd9eaf6c9cf6ea72ca3b5b6ba`
  - Original SHA-256: `2aa454645d5053e4b54b7c6c5a4c3fb54301629db8712c555673f49794bb22ac`
  - License: Apache-2.0; full original text: [license](licenses/aaron-he-zhu--aaron-marketing-skills.txt).


## Specific changes

A paid-audience seed and exclusion specification with reproducible predicates, overlap counts and upload prerequisites.

- Inventory available fields and distinguish a usable source field from an inferred characteristic. Exclude unnecessary personal or sensitive information.
- Define seed membership with explicit predicates tied to supplied columns and dates, such as repeat purchasers with positive net order contribution.
- Build exclusions for opt-outs, recent purchasers where inappropriate, returns and conflicting campaigns according to the merchant’s objective.
- Separate a seed list definition from a platform-generated lookalike audience; the latter cannot be reconstructed from customer rows alone.
- Evaluate each predicate on edge cases, including missing dates/value and overlapping memberships. State whether unknown values are excluded or require review.
- Return counts, definitions, overlap and data-minimization requirements. Hashing identifiers does not by itself establish consent or permission to upload.

Removed upstream mandatory registries, benchmark gates, mutable connector paths and software-only assumptions. Replaced them with merchant-supplied artifacts and explicitly labeled decisions. Kept task-specific method; replaced fixed industry targets with declared merchant constraints. Synthetic cases below are authored for this adaptation, not claimed customer outcomes.
