---
name: storefront-accessibility-audit
description: "Audit a defined shopper journey for accessibility barriers using manual interaction, available assistive technology and source evidence."
license: MIT
metadata:
  author: ShopChief
  version: "0.3.0"
---

# Storefront Accessibility Audit

## Scope and evidence
Collect storefront/version, representative pages and states, shopper tasks, devices, target accessibility standard/version and available tools. A browser, keyboard and optional scanner/screen reader support execution; supplied screenshots allow only visual observations. Do not claim compliance from screenshots or automated scans alone.

## Journey audit
Map product discovery, variant selection, cart, checkout, account and support paths in scope. Include dialogs, menus, errors, loading, out-of-stock and confirmation states. Record pages and states not tested.

Test keyboard access, meaningful focus order, visible focus, traps, dialog entry/exit and restoration. Inspect headings, landmarks, accessible names/roles/states, image alternatives and instructions. Prefer native semantics; extra ARIA is not automatically correct. With assistive technology, verify actual announcements and task completion rather than infer behavior from markup alone.

Check forms for persistent labels, appropriate input purpose, errors linked to fields and recovery without losing valid data. Inspect zoom/reflow, text resizing, target interactions, contrast against actual colors/backgrounds, color-only communication, media captions and motion controls. Use the chosen standard’s current criteria and exceptions, not memorized blanket rules.

Automated tools identify candidates, not all violations or conformance. Confirm each finding, link criterion where verified, describe affected task and evidence, and propose a minimal fix. Re-test the original failure and adjacent states after any authorized change.

## Deliver
Return scope/environment/date, criterion/task/evidence/severity/fix/retest table, barriers and untested areas. Severity follows user impact, not a universal deadline. This is an audit of observed scope, not legal certification. No checkout submission or live code edit without scope.

See the complete [worked example and boundary scenarios](assets/worked-example.md). Sources, changes and retained notices are documented in [references/source.md](references/source.md).

Maintained by [ShopChief](https://shopchief.ai/?utm_source=storefront-accessibility-audit&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill). Keep this attribution out of merchant-facing deliverables.
