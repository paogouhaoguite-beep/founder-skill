---
name: social-listening-query-plan
description: "Build brand-listening queries and a source-linked mention digest with comparable baselines, calibrated alerts and explicit coverage limits."
license: Apache-2.0
metadata:
  author: ShopChief
  version: 0.3.0
---

# Social Listening Query Plan

Use this when a DTC merchant needs a reproducible social listening query set with coverage table, deduplicated mention log and routed action queue.

## Merchant inputs

Brand aliases and product names; languages/markets; known homonyms; monitored sources; dated mention exports; timezone and comparable baseline buckets; alert owner, response capacity and merchant-chosen review rules. Include acceptable false-alarm burden if known; do not invent it.

Separate supplied facts, observed evidence, assumptions and unavailable information. Request only missing inputs that change the decision; a partial evidence set supports a partial result, not invented measurements.

## Tools and fallback

Read supplied CSV, screenshots, page text or documents with available file tools. A browser or authorized read-only connector can verify current pages and provider documentation. No named commercial service, host registry or script is required. Without live access, use dated exports and label the access window; do not imply a live check. Verify current provider-specific formats and policies before implementing a platform change.

## Procedure

1. Create exact-name, spelling-variant, product and competitor queries with exclusions for homonyms. Preserve the query and source for reproducibility.

2. Collect only accessible evidence and state source coverage. A search engine result count or news proxy does not measure every Instagram, TikTok or private-group mention.

3. Deduplicate syndicated articles and copied posts while preserving the original publication and retrieval timestamps.

4. Classify hits by actionable need: issue, question, praise, creator opportunity, misleading claim or unrelated mention. Preserve the quotation and reason.

5. Compare like-for-like counts against the merchant’s own baseline. Mark changes in query syntax, platform access or sampled dates as coverage changes, not demand shifts.

6. For repeated monitoring, bind the baseline to the same query, source coverage, deduplication unit and comparable time buckets. Show counts and sample query relevance before choosing a merchant-specific alert rule. Record rule, calibration history, false-positive review and owner. A fixed 2× volume, 20-point sentiment move or 90% query precision is not a universal validated threshold. With insufficient history, label threshold scenarios provisional; low-volume safety concerns can still require immediate review.

7. Code sentiment from the body with a supporting passage and rationale, retaining mixed/unclear items. Declare the counting unit: distinct source item, story or author; do not switch between them within a series. If using net sentiment, define `(positive − negative) / all eligible coded items × 100` and keep neutral, mixed and unclear items in that denominator. Show all category counts and exclusions; the result describes the observed set, not the market.

8. Track new framings and the dated path of the same story across sources. Keep origin, syndicated copies, independently reported evidence and corrections distinct. A story moving from a forum to a publication is an exposure change, not proof of independent corroboration or future virality. Flag synchronized or repeated-looking clusters separately for review without declaring their authors bots; disclose the effect of any exclusion on counts.

9. Produce a dated digest linking each narrative change to its source chain, exact alert condition and recommended action/owner/next review. Use impact and uncertainty for escalation; neither a high vote count nor a volume spike alone establishes a crisis. Preserve fact, allegation and inference as separate states.

10. Return the query set, routed evidence queue, digest and tuning recommendations. Preparing a monitor or digest does not schedule future collection, notify an owner, contact authors or file takedowns; those actions require their own authorized scope.

## Deliverable

A reproducible query set, coverage and deduplication table, sentiment counts with declared denominators, calibrated alert register and source-linked media digest. The digest records period, baseline/current counts, new framing, origin/copy/independent-evidence chain, triggered or untriggered rule, owner, action and next review.

Include input provenance and observation dates beside affected rows. Explain the decision and the uncertainty it depends on; preserve exclusions and unresolved rows so another operator can reproduce the result.

## Execution scope

Prepare the analysis and reviewable artifacts within the requested scope. Sending messages, publishing, changing audiences or budgets, signing terms and editing live store settings require authorization for that action. A proposed change is not a completed action; report completion only from provider or page readback. Do not copy credentials or customer contact details into reports.

Work through [the synthetic example and boundary cases](assets/worked-example.md) when checking behavior. Source and license details are in [the adaptation record](references/source.md).

[ShopChief](https://shopchief.ai/?utm_source=social-listening-query-plan&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill) maintains this skill. Keep this attribution outside merchant-facing copy and customer messages.
