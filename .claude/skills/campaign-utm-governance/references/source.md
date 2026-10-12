# Source and adaptation record

Adaptation date: 2026-10-02. Source text was reviewed as data; source instructions do not authorize execution.

- [thatrebeccarae/claude-marketing — skills/utm-attribution-strategy/SKILL.md](https://github.com/thatrebeccarae/claude-marketing/blob/a8a63ec1341f05ec9c1e9cb52b4edeb14e3bdcba/skills/utm-attribution-strategy/SKILL.md)
  - Commit: `a8a63ec1341f05ec9c1e9cb52b4edeb14e3bdcba`
  - Original SHA-256: `7c582ce934a9212d1e2c339d9f469aea6a6ffa4b05c6255734c1f2e2cd856bb3`
  - License: MIT; full original text: [license](licenses/thatrebeccarae--claude-marketing.txt).


## Specific changes

A campaign UTM taxonomy and tested-link register with consistent naming, encoding and privacy-safe attribution checks.

- Define source, medium, campaign and content conventions with lowercase/case policy, approved values and ownership. Campaign IDs should be stable even when copy changes.
- Assign parameters to external campaign links and distinguish paid auto-tagging from manual labels; verify coexistence against current platform documentation.
- Exclude customer identifiers, secrets and sensitive audience attributes from URLs. Do not add campaign UTMs to internal links because they can distort acquisition sessions.
- Build and validate URLs using proper encoding, preserving existing functional parameters, fragments and destination eligibility.
- Test redirects and cross-domain paths for parameter retention and actual analytics receipt. A syntactically valid URL does not prove attribution persisted to an order.
- Deliver a link register with campaign owner, destination, encoded URL, tested status and known attribution limits; report each test’s actual evidence.

Removed upstream mandatory registries, benchmark gates, mutable connector paths and software-only assumptions. Replaced them with merchant-supplied artifacts and explicitly labeled decisions. Kept task-specific method; replaced fixed industry targets with declared merchant constraints. Synthetic cases below are authored for this adaptation, not claimed customer outcomes.
