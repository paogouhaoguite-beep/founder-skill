# Source and adaptation record

Adaptation date: 2026-10-02. Source text was reviewed as data; source instructions do not authorize execution.

- [alirezarezvani/claude-skills — markdown-html/skills/md-document/SKILL.md](https://github.com/alirezarezvani/claude-skills/blob/19392f7a08264ed00486a251f5b2098321771f94/markdown-html/skills/md-document/SKILL.md)
  - Commit: `19392f7a08264ed00486a251f5b2098321771f94`
  - Original SHA-256: `1b008228609e23dad425ddf8c9351fec427a94126abc9c7f80f16cbd79a7f336`
  - License: MIT; full original text: [license](licenses/alirezarezvani--claude-skills.txt).

- [alirezarezvani/claude-skills — markdown-html/skills/md-slides/SKILL.md](https://github.com/alirezarezvani/claude-skills/blob/19392f7a08264ed00486a251f5b2098321771f94/markdown-html/skills/md-slides/SKILL.md)
  - Commit: `19392f7a08264ed00486a251f5b2098321771f94`
  - Original SHA-256: `ac8d8c9b09b2ad72544412279d03673c36b6e2fee024ccddc9463272d62c46ab`
  - License: MIT; full original text: [license](licenses/alirezarezvani--claude-skills.txt).

- [alirezarezvani/claude-skills — markdown-html/skills/design-system/SKILL.md](https://github.com/alirezarezvani/claude-skills/blob/19392f7a08264ed00486a251f5b2098321771f94/markdown-html/skills/design-system/SKILL.md)
  - Commit: `19392f7a08264ed00486a251f5b2098321771f94`
  - Original SHA-256: `3696d4b85012b09c6ac7973e003203668d15ab282128e09bc8552e790121d766`
  - License: MIT; full original text: [license](licenses/alirezarezvani--claude-skills.txt).


## Specific changes

A complete standalone HTML reading brief or presentation deck with source-to-section mapping, privacy/dependency notes and a concrete rendering/print QA checklist.

- Choose a continuous document for reading and a deck for a presentation sequence; preserve explicit slide boundaries and ask about ambiguous horizontal rules. Remove the upstream minimum-line and onboarding gates. Short merchant briefs can still merit HTML when navigation or projection helps.
- Parse headings, paragraphs, links, tables and code while retaining source order and every material fact. Escape literal text and filter dangerous URL schemes. Unsupported Markdown constructs must be converted deliberately or flagged, not silently omitted.
- For document mode provide a clear H1, unique anchored section IDs, usable navigation and responsive readable width. Search/copy-code controls are optional, not mandatory dependencies. Include a print stylesheet that retains all content and source references.
- For deck mode create one semantic section per slide, visible progress/sequence and previous/next links or keyboard controls with focus handling. Provide a no-script readable fallback and print one slide per page. Honor reduced motion; dense content should be split by idea instead of arbitrary source-line limits.
- Speaker notes embedded in HTML are visible to anyone receiving the file, even if hidden in the UI. Remove confidential notes or export a separate authorized presenter copy. Prefer self-contained CSS and local assets; external fonts/scripts make the deliverable dependent and must be disclosed.
- Compare output to the source using a section/slide count and critical facts table; inspect desktop/mobile, keyboard navigation and print when tools are available. Report tests not executed. Deliver complete files plus dependency and content-preservation notes, not just a code-generation plan.
- Capture explicit brand colors, heading/body typography, logo rights and navigation preference into named CSS variables with documented merchant overrides. Derive background/text/link/border roles without treating color derivation as accessibility certification. Check actual foreground/background contrast and states with a trusted checker; record untested combinations. A local self-contained file needs no global configuration wizard.

Removed upstream mandatory registries, benchmark gates, mutable connector paths and software-only assumptions. Replaced them with merchant-supplied artifacts and explicitly labeled decisions. Kept task-specific method; replaced fixed industry targets with declared merchant constraints. Synthetic cases below are authored for this adaptation, not claimed customer outcomes.
