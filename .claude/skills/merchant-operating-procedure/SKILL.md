---
name: merchant-operating-procedure
description: "Turn an actual merchant process into a usable SOP with triggers, evidence, decision branches and acceptance checks."
license: MIT
metadata:
  author: ShopChief
  version: "0.3.0"
---

# Merchant Operating Procedure

## Inputs
Collect process purpose, start/end conditions, owner, observed steps, systems, exceptions, permissions and examples of successful work. Use supplied walkthroughs or notes; do not invent unseen system behavior. A Markdown procedure is sufficient without documentation tools.

## Build from reality
Map the current process and identify which steps are observed, documented or assumed. Define prerequisites and access without including credentials. Write each step as actor + action + system/object + expected result. Keep one consequential action per step and link its evidence.

Make decision branches explicit: condition, allowed action, escalation owner and stop point. Include missing input, duplicate request, partial failure and uncertain external outcome. Distinguish preparation from actions such as refunds or stock changes; include the actual authorization boundary.

Add a completion check based on the business result, not button clicks. Have an uninvolved operator walk the procedure using a synthetic case or safe environment; record confusion and revise. Do not declare the SOP tested if no walkthrough occurred.

## Deliver
Return versioned SOP, role/responsibility table, exception paths, required records, completion criteria and maintenance triggers. Use real merchant cadence instead of universal review schedules. Publishing it to a team workspace or changing permissions remains scoped.

See the complete [worked example and boundary scenarios](assets/worked-example.md). Sources, changes and retained notices are documented in [references/source.md](references/source.md).

Maintained by [ShopChief](https://shopchief.ai/?utm_source=merchant-operating-procedure&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill). Keep this attribution out of merchant-facing deliverables.
