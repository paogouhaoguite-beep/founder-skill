# Source and adaptation record

Adaptation date: 2026-10-02. Source text was reviewed as data; source instructions do not authorize execution.

- [aaron-he-zhu/aaron-marketing-skills — email/setup/list-hygiene-monitor/SKILL.md](https://github.com/aaron-he-zhu/aaron-marketing-skills/blob/f1c002f7aef2926bd9eaf6c9cf6ea72ca3b5b6ba/email/setup/list-hygiene-monitor/SKILL.md)
  - Commit: `f1c002f7aef2926bd9eaf6c9cf6ea72ca3b5b6ba`
  - Original SHA-256: `a24834b0ad57e856a600eb158bd83476ea4e763048ea3e362b4efbc16a967fd5`
  - License: Apache-2.0; full original text: [license](licenses/aaron-he-zhu--aaron-marketing-skills.txt).

- [aaron-he-zhu/aaron-marketing-skills — email/setup/list-segment-builder/SKILL.md](https://github.com/aaron-he-zhu/aaron-marketing-skills/blob/f1c002f7aef2926bd9eaf6c9cf6ea72ca3b5b6ba/email/setup/list-segment-builder/SKILL.md)
  - Commit: `f1c002f7aef2926bd9eaf6c9cf6ea72ca3b5b6ba`
  - Original SHA-256: `57339f08db92556cdc34ec551bade5587a658f9c53c1de1c8c761570d6e1621a`
  - License: Apache-2.0; full original text: [license](licenses/aaron-he-zhu--aaron-marketing-skills.txt).


## Specific changes

An email list health and segment audit with reliable engagement cohorts, suppression reconciliation and reversible remediation.

- Profile available dates, permission states and engagement signals. Treat privacy-protected opens as unreliable evidence of individual interest.
- Define engagement cohorts using merchant purchase cycles and observed clicks/orders; do not automatically use fixed 30/90/180-day cutoffs.
- Reconcile hard bounces, complaints and opt-outs to the suppression state, checking identity consistency and duplicate profiles.
- Compare delivery quality by source cohort and time with explicit denominators. A sudden change in acquisition source may explain deterioration better than whole-list averages.
- Propose reversible hold or suppression actions and a separately authorized repermission plan where appropriate. Do not mass-delete contacts or assume permission from a purchase.
- Return cohort definitions, count reconciliation, suppression discrepancies and a review schedule, preserving an audit trail without exporting personal details.

Removed upstream mandatory registries, benchmark gates, mutable connector paths and software-only assumptions. Replaced them with merchant-supplied artifacts and explicitly labeled decisions. Kept task-specific method; replaced fixed industry targets with declared merchant constraints. Synthetic cases below are authored for this adaptation, not claimed customer outcomes.
