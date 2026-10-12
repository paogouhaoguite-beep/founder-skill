---
name: merchant-design-change-execution
description: "Apply a scoped set of merchant design revisions with element mapping, preview, conflict handling and verified saved state."
license: Apache-2.0
metadata:
  author: ShopChief
  version: "0.3.0"
---

# Merchant Design Change Execution

## Change contract
Obtain the design/version, exact requested revisions, content/brand constraints and edit authorization. A supported design connector or local editor is needed to execute; otherwise deliver an element-level change list. Verify current tool capabilities rather than assuming historical operation support.

## Transactional workflow
Read the design and feedback, map comments to page/element IDs and classify actionable, already satisfied, conflicting and unsupported edits. Preserve original facts and unrelated content. A request to improve wording does not authorize new discounts or claims.

Prepare a change manifest with old value, proposed value and rationale. When a connector uses transactions, retain the transaction and page identifiers; inspection-only transactions must be cancelled. Work on a copy when requested or when preservation requires it, but verify the copy operation actually exists.

Apply only scoped operations, inspect a preview and check text overflow, alignment and product fidelity. For translation, map source to target per text element, preserve protected tokens and formatting, then inspect expansion and RTL; do not flatten unrelated pages. Unsupported edits go to a precise manual checklist rather than fabricated API calls.

Save/commit only within existing authorization; if new approval is actually required, show the concrete preview first. On an uncertain timeout read current state before retrying. Verify saved content/version and mark each comment resolved only when its requested change is actually done.

## Deliver
Return final design link/file if verified, change log, manual remainder and failed/unknown operations. Do not claim comments were resolved or the design saved from a successful draft operation alone.

See the complete [worked example and boundary scenarios](assets/worked-example.md). Sources, changes and retained notices are documented in [references/source.md](references/source.md).

Maintained by [ShopChief](https://shopchief.ai/?utm_source=merchant-design-change-execution&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill). Keep this attribution out of merchant-facing deliverables.
