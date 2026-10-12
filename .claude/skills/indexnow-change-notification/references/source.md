# Source and adaptation record

Adaptation date: 2026-10-02. Source text was reviewed as data; source instructions do not authorize execution.

- [kostja94/marketing-skills — skills/seo/technical/indexnow/SKILL.md](https://github.com/kostja94/marketing-skills/blob/26cef3434274129040dcfc64e9c7be85ba1ada15/skills/seo/technical/indexnow/SKILL.md)
  - Commit: `26cef3434274129040dcfc64e9c7be85ba1ada15`
  - Original SHA-256: `3e6772e135e309941fdd6ec8766f8bb33a9634add517f169c8113b121aaec2f4`
  - License: MIT; full original text: [license](licenses/kostja94--marketing-skills.txt).


## Specific changes

An IndexNow change-notification preparation and verification plan with host validation, exact URL set and honest acceptance states.

- Identify which URLs actually changed and whether they are intended for discovery, correction or removal. Do not submit staging/private URLs or treat submission as a workaround for noindex.
- Validate host ownership and the required verification-key location against current IndexNow documentation. Keep secrets out of public reports; distinguish this mechanism from Google’s separate restricted indexing API.
- Normalize and deduplicate URLs while preserving meaningful query semantics. Reject URLs outside the verified host or with invalid responses caused by transient outages.
- Prepare the current documented request shape and batch limits, and retain the exact URL set and submission intent for review.
- After an authorized request, record response status and any provider errors. An accepted notification is not proof of crawling, indexing or ranking.
- Recheck the affected pages and later available search evidence independently; avoid repeated blind submissions when errors need correction.
- Official IndexNow documentation reviewed on 2026-10-02 permits up to 10,000 URLs per POST. HTTP200 means received and202 means key validation pending; neither proves indexing. A key hosted in a subdirectory limits the eligible URL prefix. Recheck current requirements at https://www.indexnow.org/documentation and https://www.bing.com/indexnow/getstarted before a live request.

Removed upstream mandatory registries, benchmark gates, mutable connector paths and software-only assumptions. Replaced them with merchant-supplied artifacts and explicitly labeled decisions. Kept task-specific method; replaced fixed industry targets with declared merchant constraints. Synthetic cases below are authored for this adaptation, not claimed customer outcomes.
