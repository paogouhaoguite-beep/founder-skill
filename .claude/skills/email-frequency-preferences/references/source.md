# Source and adaptation record

Adaptation date: 2026-10-02. Source text was reviewed as data; source instructions do not authorize execution.

- [aaron-he-zhu/aaron-marketing-skills — email/nurture/preference-frequency-manager/SKILL.md](https://github.com/aaron-he-zhu/aaron-marketing-skills/blob/f1c002f7aef2926bd9eaf6c9cf6ea72ca3b5b6ba/email/nurture/preference-frequency-manager/SKILL.md)
  - Commit: `f1c002f7aef2926bd9eaf6c9cf6ea72ca3b5b6ba`
  - Original SHA-256: `d34da47c22e2488ece9483a881d78bf00fce70191fab5cbc1f6f316dba1dacb4`
  - License: Apache-2.0; full original text: [license](licenses/aaron-he-zhu--aaron-marketing-skills.txt).


## Specific changes

An email preference and frequency design with state precedence, cross-flow caps and testable pause/unsubscribe behavior.

- Inventory what customers were promised and what they actually receive, including overlapping automations and campaigns.
- Define understandable topic choices and cadence options the ESP can implement. Avoid choices that imply a frequency guarantee the system cannot enforce.
- Specify global unsubscribe, topic opt-out, temporary pause and reduced frequency as distinct states, with clear precedence. Marketing opt-out should not be silently undone by a new preference choice.
- Map each state to segment filters and a frequency cap evaluated across all marketing sends, not separately per workflow.
- Test pause expiry, conflicting preferences and recent events; explicitly classify necessary order/service messages instead of using “transactional” as a loophole for promotions.
- Deliver UI wording, state-transition rules and enforcement checks. Preference edits and live flow changes require explicit implementation scope.

Removed upstream mandatory registries, benchmark gates, mutable connector paths and software-only assumptions. Replaced them with merchant-supplied artifacts and explicitly labeled decisions. Kept task-specific method; replaced fixed industry targets with declared merchant constraints. Synthetic cases below are authored for this adaptation, not claimed customer outcomes.
