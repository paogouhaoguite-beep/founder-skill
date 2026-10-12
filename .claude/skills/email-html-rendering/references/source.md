# Source and adaptation record

Adaptation date: 2026-10-02. Source text was reviewed as data; source instructions do not authorize execution.

- [aaron-he-zhu/aaron-marketing-skills — email/engage/email-render-builder/SKILL.md](https://github.com/aaron-he-zhu/aaron-marketing-skills/blob/f1c002f7aef2926bd9eaf6c9cf6ea72ca3b5b6ba/email/engage/email-render-builder/SKILL.md)
  - Commit: `f1c002f7aef2926bd9eaf6c9cf6ea72ca3b5b6ba`
  - Original SHA-256: `9943c2dada33831431d071c71f0839c0463b3f03836e5b1c346c6280dc5a7592`
  - License: Apache-2.0; full original text: [license](licenses/aaron-he-zhu--aaron-marketing-skills.txt).

- [alirezarezvani/claude-skills — engineering-team/skills/email-template-builder/SKILL.md](https://github.com/alirezarezvani/claude-skills/blob/19392f7a08264ed00486a251f5b2098321771f94/engineering-team/skills/email-template-builder/SKILL.md)
  - Commit: `19392f7a08264ed00486a251f5b2098321771f94`
  - Original SHA-256: `e01efa4b96637071fede0bfbf3c3d178e5da7a1ee6ee35ab33cf1cfcb4589e69`
  - License: MIT; full original text: [license](licenses/alirezarezvani--claude-skills.txt).


## Specific changes

A portable marketing email HTML and plain-text build with profile fallbacks and an observed-versus-pending render QA matrix.

- Preserve approved copy and offer conditions while building a robust single-column structure using email-compatible tables and inline styling where required.
- Make image dimensions, fluid widths and text sizes deliberate; do not put essential offer terms only inside images. Include meaningful alt text and a plain-text alternative.
- Build buttons as live text links with appropriate padding; verify destination, tracking and unsubscribe links. Template tags must use the actual ESP syntax with fallback behavior.
- Check narrow screens, long text, blocked images, dark-mode color pairs and Outlook-specific rendering risks. A browser preview is not proof of inbox-client compatibility.
- Create a client/condition QA matrix and record observed versus predicted behavior. Use available inbox previews or seed tests; otherwise mark checks pending with a reproducible inspection plan.
- Deliver HTML, plain text, asset requirements and open rendering issues. Do not ship unreviewed source scripts or claim the email was sent.

Removed upstream mandatory registries, benchmark gates, mutable connector paths and software-only assumptions. Replaced them with merchant-supplied artifacts and explicitly labeled decisions. Kept task-specific method; replaced fixed industry targets with declared merchant constraints. Synthetic cases below are authored for this adaptation, not claimed customer outcomes.
