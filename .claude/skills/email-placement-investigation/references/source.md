# Source and adaptation record

Adaptation date: 2026-10-02. Source text was reviewed as data; source instructions do not authorize execution.

- [aaron-he-zhu/aaron-marketing-skills — email/deliver/inbox-placement-monitor/SKILL.md](https://github.com/aaron-he-zhu/aaron-marketing-skills/blob/f1c002f7aef2926bd9eaf6c9cf6ea72ca3b5b6ba/email/deliver/inbox-placement-monitor/SKILL.md)
  - Commit: `f1c002f7aef2926bd9eaf6c9cf6ea72ca3b5b6ba`
  - Original SHA-256: `b800ed91bee0575f7d7870e0dd8bede37fb86c87b093393bb46859a45113cab9`
  - License: Apache-2.0; full original text: [license](licenses/aaron-he-zhu--aaron-marketing-skills.txt).


## Specific changes

A provider-specific email placement investigation separating seed observations, delivery acceptance and unverified causal explanations.

- Bind placement evidence to the tested message, domain, time and provider. Distinguish a seed test from the whole production audience.
- Report inbox, spam and category placement per provider, preserving missing or inconclusive cells. SMTP accepted/delivered does not prove inbox placement.
- Compare reputation and failure patterns with prior compatible periods; identify changes in domain, volume, acquisition source or message before proposing a cause.
- Reconcile placement with authentication and complaint evidence. A subject keyword or a seed score alone cannot establish why a provider filtered the message.
- Prioritize evidence-backed remediation and a small retest with one changed condition where feasible. Keep provider-specific observations separate rather than hiding them in an overall average.
- Return a diagnosis table with observed facts, causal hypotheses, proposed checks and untested providers. Do not change DNS, warm sending volume or launch a seed send without scope.

Removed upstream mandatory registries, benchmark gates, mutable connector paths and software-only assumptions. Replaced them with merchant-supplied artifacts and explicitly labeled decisions. Kept task-specific method; replaced fixed industry targets with declared merchant constraints. Synthetic cases below are authored for this adaptation, not claimed customer outcomes.
