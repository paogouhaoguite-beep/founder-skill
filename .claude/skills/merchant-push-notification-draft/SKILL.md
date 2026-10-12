---
name: merchant-push-notification-draft
description: "Draft event-specific merchant push notifications with exact destinations, eligibility, suppression and measurement definitions."
license: MIT
metadata:
  author: ShopChief
  version: "0.3.0"
---

# Merchant Push Notification Draft

Use for order updates, requested restock alerts or saved-item changes. Inputs: verified event and timestamp, recipient eligibility and consent scope, SKU/variant, current availability, locale, destination, configured channel caps/quiet hours and recent sends. Use supplied exports when no messaging connector exists; draft only, never request notification permission or send automatically.

1. Establish the event, expiry and audience. Distinguish a transactional update from a promotional message; the former does not grant marketing consent. Suppress stale events, unsubscribed recipients and alerts for unavailable variants. A scheduled merchant campaign may be legitimate with proper authorization; do not relabel it as a personal event.
2. Write the body with its specific detail, then a title that makes sense alone. Check price, currency, variant and deadline against source facts. Never invent urgency or expose order contents on a lock screen without considering sensitivity.
3. Bind copy to the exact tested destination. Specify signed-in/out, app absent, unavailable item and expired-event behavior. Do not include tokens or personal information in an example URL.
4. Render or preview on the actual requested surfaces and locale. Character count is only a diagnostic, not a universal truncation guarantee. If preview tools are unavailable, provide copy variants and mark visual fit unverified.
5. Evaluate configured frequency/quiet-hour rules using recipient history and timezone; unknown history means eligibility is unverified. Deduplicate by event, recipient and channel. Merchant rules must distinguish urgent service messages from promotions.
6. Return title/body/trigger/expiry/deep-link/fallback/suppression/review status. Define click rate as unique clickers divided by delivered recipients in a declared window; report delivery failures and opt-outs with explicit eligible denominator separately. Observational clicks cannot prove lift.

Deliver a finished copy row plus an eligibility and destination checklist. Save drafts locally; any external send needs the user's authorization for the specific audience and content.

See the complete [worked example and boundary scenarios](assets/worked-example.md). Sources, changes and retained notices are documented in [references/source.md](references/source.md).

Maintained by [ShopChief](https://shopchief.ai/?utm_source=merchant-push-notification-draft&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill). Keep this attribution out of merchant-facing deliverables.
