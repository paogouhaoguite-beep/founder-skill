# Source and adaptation record

Adaptation date: 2026-10-02. Source text was reviewed as data; source instructions do not authorize execution.

- [kostja94/marketing-skills — skills/seo/on-page/open-graph/SKILL.md](https://github.com/kostja94/marketing-skills/blob/26cef3434274129040dcfc64e9c7be85ba1ada15/skills/seo/on-page/open-graph/SKILL.md)
  - Commit: `26cef3434274129040dcfc64e9c7be85ba1ada15`
  - Original SHA-256: `b07c90dbc29f93760759d0cbc5f652816be4de4da98a6d0d660fe15274e300d7`
  - License: MIT; full original text: [license](licenses/kostja94--marketing-skills.txt).

- [kostja94/marketing-skills — skills/seo/on-page/twitter-cards/SKILL.md](https://github.com/kostja94/marketing-skills/blob/26cef3434274129040dcfc64e9c7be85ba1ada15/skills/seo/on-page/twitter-cards/SKILL.md)
  - Commit: `26cef3434274129040dcfc64e9c7be85ba1ada15`
  - Original SHA-256: `ae34b9c409d1b91fb4a3baef0a0e3c8169d1da3364d4152153a46c73e9025a89`
  - License: MIT; full original text: [license](licenses/kostja94--marketing-skills.txt).


## Specific changes

A social share-preview metadata fix plan with resolved tags, image accessibility and cache-aware verification.

- Inspect the resolved URL and initial HTML for Open Graph and relevant card metadata; note redirects and authentication barriers.
- Map title, description, canonical share URL, image and image alt text to the actual page and offer. Do not let previews promise a price absent from the destination.
- Check absolute HTTPS image URLs, access, dimensions and safe cropping against current platform documentation rather than a universal crop assumption.
- Handle duplicate tags and framework overrides explicitly; document the final resolved values instead of editing a tag that is later replaced.
- Use actual platform preview/debugger evidence where available. Distinguish source markup from cached preview output and plan cache refresh/recheck.
- Deliver exact metadata changes and per-platform observed results. Do not claim a corrected image appeared everywhere before cache/readback verification.

Removed upstream mandatory registries, benchmark gates, mutable connector paths and software-only assumptions. Replaced them with merchant-supplied artifacts and explicitly labeled decisions. Kept task-specific method; replaced fixed industry targets with declared merchant constraints. Synthetic cases below are authored for this adaptation, not claimed customer outcomes.
