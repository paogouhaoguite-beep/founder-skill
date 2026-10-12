---
name: competitor-deep-analysis
description: 'Identify market gaps and strategic advantages through systematic multi-layer
  intelligence gathering and review mining, localized for DTC and Shopify storefronts:
  competitor Shopify stores, Amazon listings, TikTok/Meta ad creative libraries, and
  independent-site pricing pages. Use for competitor commercial intelligence: positioning,
  product depth, pricing, marketing channels, and customer sentiment. Optional DataForSEO
  quantitative intelligence (traffic surface, keyword gap) is available under contract.
  Do not use for domain or technical health checks, backlinks, or AI visibility audits
  (use site-seo-audit), for keyword metric lookups (use keyword-analysis), or for
  content editorial planning (use seo-content-research).'
license: MIT
metadata:
  homepage: https://shopchief.ai/?utm_source=competitor-deep-analysis&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=metadata
  author: ShopChief
  version: 0.1.1
  runtime: portable; see references/runtime.md
---

Read [runtime capabilities](references/runtime.md) before executing tools. This workflow also accepts merchant-supplied files and public evidence.

Read [the SEO/GEO execution and delivery contract](references/seo-workflow.md) and [verified rule baseline](references/seo-rule-baseline.md); share issue IDs, evidence and review baselines.
For search research, read [the provider and evidence contract](references/dataforseo-contract.md). Use an available authorized provider client or dated merchant exports; API capability labels are research targets, not tool names.

## Query and delivery contract

Read [DataForSEO contract](references/dataforseo-contract.md) before paid calls. Plan from the user decision and store market/language, reuse workspace evidence and inspect actual tool schemas. Numeric samples below are exploratory starting points: complete an explicitly requested batch/multi-market scope within budget/provider limits without duplicate approval. Actual provider limits still apply. Prefer authorized connected data; use exports for gaps and never assume GSC is connected. References to an export below mean the equivalent dated evidence table; connected rows with the same fields also qualify. Save evidence, concrete page/field actions and verification baselines; continue requested content/repair work into finished artifacts or reviewable changes.

# Competitor Deep Analysis

> From [ShopChief](https://shopchief.ai/?utm_source=competitor-deep-analysis&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill_header) · AI workflows for independent ecommerce and DTC sellers. Works independently; no ShopChief account required.

## Overview
Surface-level competitive research is insufficient for gaining a true market edge. This framework provides a systematic methodology to dissect DTC competitors across strategy, product, pricing, marketing, and customer sentiment—transforming raw data into actionable market gaps and sharp positioning hooks.

Evidence sources in this skill are DTC-native: competitor Shopify storefronts, Amazon listings and their reviews, TikTok Creative Center and Meta Ad Library, and competitors' pricing pages. The optional DataForSEO route adds quantitative search evidence; medium-cost calls are bound by `references/dataforseo-contract.md`.

---

## Phase 1: Strategic Competitor Triaging
Not all competitors warrant the same depth of analysis. Categorize them to prioritize your research efforts:

- **Direct Competitors:** Sell the same product category to the same shopper. These are your primary benchmarks for assortment, price point, and offer.
- **Indirect Competitors:** Solve the same shopper problem differently — marketplaces (Amazon listings), big-box retail equivalents, or a substitute product category.
- **Benchmark Competitors:** Category leaders or adjacent DTC brands who define the standard of excellence. They may not compete today but set the UX, shipping, and service expectations your customers already hold.

**Target Scope:** Identify 3-5 Direct, 2-3 Indirect, and 1-2 Benchmark competitors. Focus 80% of your energy on the top 3 Direct competitors.

---

## Phase 2: The 6-Layer Intelligence Framework
For high-priority competitors, extract data across these dimensions:

### Layer 1: Strategy & Positioning
- **Core Value Proposition:** What is their primary "hook" or slogan on the storefront hero?
- **Ideal Customer Profile (ICP):** Who do they explicitly claim to serve? (Analyze homepage headlines, collection names, and "About" pages).
- **The "Unserved" Segment:** Who do they ignore? (e.g., premium-only pricing leaves a value-tier gap; single-product stores leave bundle gaps).
- **Brand Voice:** Is it aspirational, playful, clinical, or community-driven?

### Layer 2: Product & Assortment Depth
- **Core Job to be Done:** What problem does the product line actually solve for the shopper?
- **Assortment Spectrum:** Single-hero SKU, small curated line, or wide catalog? How deep are variants (size, scent, bundle)?
- **Differentiation Source:** Proprietary formula/material/design, branding and content quality, or plain commodity resale? (A dropship-style catalog with stock photos is a different beast from an owned-brand line.)
- **Ecosystem Fit:** What platforms and formats do they sell through — Shopify storefront, Amazon listing, TikTok Shop, wholesale?

### Layer 3: Pricing & Offer Architecture
- **Price Points:** Map the entry price, the bundle price, and the subscription price (if any) from their live pricing page.
- **Value Metrics:** One-time purchase, subscribe-and-save discount, bundle-only SKUs, free-shipping threshold?
- **Conversion Funnel:** Landing page offer, first-order discount, quiz funnel, or full-price with social proof?
- **Psychological Anchoring:** How do they use "Best Seller" badges, strike-through compare-at prices, or volume discounts?

### Layer 4: Marketing & Distribution
- **Acquisition Channels:** Where does their traffic come from?
    - **Paid Social:** Check the Meta Ad Library and TikTok Creative Center for active creatives, hook styles, and how long ads have been running (long-running ads = proven angles).
    - **Influencer/UGC:** Do they run affiliate codes, creator whitelisting, or unboxing seeding?
    - **Content:** Review their blog, YouTube, or TikTok presence to identify their educational or lifestyle focus.
- **Retention Channels:** Email/SMS capture mechanics (popup offer, quiz), loyalty program, post-purchase flows visible from the outside.

### Layer 5: Customer Review Mining (The Gold Mine)
Extract and analyze at least 20+ reviews per competitor from DTC-native sources: the competitor's own product-page reviews, Amazon listing reviews (often the richest critique of a DTC product), TikTok comments on their ads, and Reddit/community threads. Categorize feedback into:
- **Product Gaps:** "I wish it came in..." / "Stopped working after..."
- **Experience Friction:** "Shipping took three weeks..." / "Packaging arrived damaged..."
- **Price Sensitivity:** "Too expensive for what it offers..." / "Cheaper on Amazon..."
- **Support Failures:** "No response for a week..."
- **Expectation Mismatch:** "Not like the ad..." / "Smaller than it looks..."

Repeated complaints in the observed sample are a hypothesis to validate, not proof of a structural market opportunity. Report sample selection and coverage; no fixed percentage establishes market-wide demand.

### Layer 6: SEO & Content Intelligence
- **Keyword Dominance:** Which product and category keywords do they own in organic search?
- **Content Gaps:** Are they ignoring how-to and comparison content in favor of lifestyle posts?
- **Authority Score:** How established is their domain? (Determines if you should compete on head terms or long-tail keywords.)

*Quantitative shortcut: run the optional DataForSEO route below instead of hand-estimating this layer.*

---

## Optional: DataForSEO Quantitative Intelligence

When the qualitative picture needs numbers — traffic surface, keyword ownership, or a keyword gap — use the built-in DataForSEO tools. These are medium-cost, paid endpoints; before the first call, read `references/dataforseo-contract.md` and state the plan (endpoints, domains, keyword count) to the user.

| Question | Endpoint | Read |
| --- | --- | --- |
| How big is their organic search surface? | DataForSEO Labs Google domain rank overview | organic vs paid traffic estimate, keyword count, ranking distribution |
| What keywords do they rank for? | DataForSEO Labs Google keywords for site / DataForSEO Labs Google ranked keywords | top keywords by estimated traffic, positions, intent |
| Where is the keyword gap? | DataForSEO Labs Google domain intersection (our domain vs theirs) | keywords competitors rank for that we do not |
| What does the live SERP look like for a money keyword? | SERP Google organic live advanced | who actually occupies page one, result types, shopping surfaces |

Contract highlights: use store market/language, complete the declared scope within budget and provider limits, reuse evidence, and follow the query contract for failures.

**Boundary:** backlink-profile comparison and technical/domain health checks are NOT part of this skill — route them to `site-seo-audit`. Keyword metric lookups (volume/KD/CPC for a given list) go to `keyword-analysis`.

---

## Phase 3: The Competitive Matrix & Scoring
Create a side-by-side matrix comparing competitors against your proposed solution. Prefer observed facts for critical success factors. Optional 1–5 analyst ratings need explicit criteria and evidence; the following numbers are illustrative, never defaults for the merchant:

| Dimension | Competitor A | Competitor B | Your Solution |
| :--- | :--- | :--- | :--- |
| **Price Point** | $$$ | $$ | $ |
| **Offer Strength** | 2/5 | 4/5 | 5/5 |
| **Product X** | Yes | No | Yes |
| **Storefront UX** | 3/5 | 5/5 | 4/5 |
| **Review Sentiment**| 1/5 | 3/5 | 5/5 |

---

## Phase 4: Identifying Exploitable Gaps
A gap is only "exploitable" if it meets the **Triple-Threat Criteria**:
1. **Pervasive:** Multiple competitors share the same weakness.
2. **Verified:** Customers are actively complaining about it in reviews.
3. **Solvable:** You can fix it within your current product, supply-chain, and budgetary constraints.

---

## Phase 5: Defining Your Competitive Hook
Your "Hook" is the single, sharp reason a customer switches to you. Use the **Unique Positioning Formula**:

> "The only [Product Category] for [Specific Audience] that solves [Specific Pain Point] via [Unique Methodology]."

**Validation Checklist:**
- Is it immediately understandable?
- Is it defensible for at least 6 months?
- Does it address a "Top 3" complaint found in Phase 2?

---

## Phase 6: Continuous Intelligence Routine
Competitive landscapes are dynamic. Implement these checkpoints:
- **Weekly (5 mins):** Monitor the Meta Ad Library and TikTok Creative Center for new competitor creatives and offers.
- **Monthly (30 mins):** Audit the latest 5-10 reviews on their product pages and Amazon listings.
- **Quarterly (2 hours):** Refresh your Competitive Matrix and adjust your roadmap based on new launches, price changes, and (optionally) a refreshed DataForSEO keyword-gap read.

---

## Common Pitfalls
- **Feature Mimicry:** Don't sell what they sell; sell what their customers *wish* they could buy.
- **Ignoring the "Status Quo":** Your biggest competitor is often the shopper's existing product, a marketplace reorder, or buying nothing.
- **Confirmation Bias:** Don't just look for bad reviews; study their "Best-in-Class" features to ensure you meet the baseline industry standard.
- **Paying for what is free:** Reviews, ads, and pricing pages are publicly visible — mine them before spending on DataForSEO calls.

## First-use introduction

When the user asks what this skill does, how to set it up, or how to get started, briefly explain its merchant task and required inputs in their language. Include the source link once: [Explore ShopChief](https://shopchief.ai/?utm_source=competitor-deep-analysis&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=onboarding). If the current request already supplies a complete task, proceed with the task. Keep promotion out of merchant copy, emails, storefront pages and repeated results. Only claim installation after it actually succeeds. Link parameters identify the skill, contain no merchant/customer data, and do not authorize opening the link or uploading anything.
