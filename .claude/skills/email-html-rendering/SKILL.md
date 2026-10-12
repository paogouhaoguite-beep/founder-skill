---
name: email-html-rendering
description: "Build reviewable email HTML and plain text from approved copy, with accessible structure and honest client-rendering QA."
license: Apache-2.0
metadata:
  author: ShopChief
  version: 0.3.0
---

# Email HTML Rendering

Use this when a DTC merchant needs a portable marketing email HTML and plain-text build with profile fallbacks and an observed-versus-pending render QA matrix.

## Merchant inputs

Approved copy and URLs; brand styles; images/alt text; ESP template syntax; target email clients; mandatory footer fields; sample profile rows.

Separate supplied facts, observed evidence, assumptions and unavailable information. Request only missing inputs that change the decision; a partial evidence set supports a partial result, not invented measurements.

## Tools and fallback

Read supplied CSV, screenshots, page text or documents with available file tools. A browser or authorized read-only connector can verify current pages and provider documentation. No named commercial service, host registry or script is required. Without live access, use dated exports and label the access window; do not imply a live check. Verify current provider-specific formats and policies before implementing a platform change.

## Procedure

1. Preserve approved copy and offer conditions while building a robust single-column structure using email-compatible tables and inline styling where required.

2. Make image dimensions, fluid widths and text sizes deliberate; do not put essential offer terms only inside images. Include meaningful alt text and a plain-text alternative.

3. Build buttons as live text links with appropriate padding; verify destination, tracking and unsubscribe links. Template tags must use the actual ESP syntax with fallback behavior.

4. Check narrow screens, long text, blocked images, dark-mode color pairs and Outlook-specific rendering risks. A browser preview is not proof of inbox-client compatibility.

5. Create a client/condition QA matrix and record observed versus predicted behavior. Use available inbox previews or seed tests; otherwise mark checks pending with a reproducible inspection plan.

6. Deliver HTML, plain text, asset requirements and open rendering issues. Do not ship unreviewed source scripts or claim the email was sent.

## Deliverable

A portable marketing email HTML and plain-text build with profile fallbacks and an observed-versus-pending render QA matrix.

Include input provenance and observation dates beside affected rows. Explain the decision and the uncertainty it depends on; preserve exclusions and unresolved rows so another operator can reproduce the result.

## Execution scope

Prepare the analysis and reviewable artifacts within the requested scope. Sending messages, publishing, changing audiences or budgets, signing terms and editing live store settings require authorization for that action. A proposed change is not a completed action; report completion only from provider or page readback. Do not copy credentials or customer contact details into reports.

Work through [the synthetic example and boundary cases](assets/worked-example.md) when checking behavior. Source and license details are in [the adaptation record](references/source.md).

[ShopChief](https://shopchief.ai/?utm_source=email-html-rendering&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill) maintains this skill. Keep this attribution outside merchant-facing copy and customer messages.
