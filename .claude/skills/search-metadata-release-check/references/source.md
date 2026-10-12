# Source and adaptation record

Adaptation date: 2026-10-02. Source text was reviewed as data; source instructions do not authorize execution.

- [seoskillsai/seo-skills-ai — skills/seo-drift/SKILL.md](https://github.com/seoskillsai/seo-skills-ai/blob/7daed7f36e2d3a74fe864854014e6a432d23e0f6/skills/seo-drift/SKILL.md)
  - Commit: `7daed7f36e2d3a74fe864854014e6a432d23e0f6`
  - Original SHA-256: `cf3cf1093ecf2ff6c9fe4560cc0a93c87a3b1abc1ce2ae69e9eee45630fa7bf4`
  - License: MIT; full original text: [license](licenses/seoskillsai--seo-skills-ai.txt).


## Specific changes

A release-time SEO metadata comparison with valid snapshot checks, intent-aware regressions and verification steps.

- Capture response status, final URL, timestamp and page variant with each snapshot. Reject login, bot-check and error pages as substitutes for the intended content.
- Compare title, robots directives, canonical, headings, structured data and important links at the same URL and rendering stage.
- Separate intended editorial changes from accidental deletion or conflicting indexability. Severity depends on commercial scope and crawl impact, not a fixed percentage of title text changed.
- Validate structured-data parseability and visible-content consistency; a removed unsupported field can be an improvement rather than a regression.
- Identify template-wide patterns versus one-page defects and propose the smallest reversible fix. Preserve before/after evidence and the release that introduced the difference.
- Report observed regressions, deliberate changes and unverified checks. A monitoring report is not evidence that Google recrawled or changed indexing.

Removed upstream mandatory registries, benchmark gates, mutable connector paths and software-only assumptions. Replaced them with merchant-supplied artifacts and explicitly labeled decisions. Kept task-specific method; replaced fixed industry targets with declared merchant constraints. Synthetic cases below are authored for this adaptation, not claimed customer outcomes.
