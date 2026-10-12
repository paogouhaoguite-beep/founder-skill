---
name: retail-location-discovery
description: "Prepare accurate location pages and listing corrections for genuine customer-facing retail locations, with eligibility and measurement checks."
license: Apache-2.0
metadata:
  author: ShopChief
  version: 0.3.0
---

# Retail Location Discovery

Use this when a DTC merchant needs a canonical location record, listing discrepancy/action table, useful location-page draft and a bounded measurement plan.

## Merchant inputs

Real merchant locations and customer-access arrangements, verified name/address/contact/hours, location-page URLs, available listing exports, and market/language. Online-only stores must identify whether any eligible customer-facing location exists.

Separate supplied facts, observed evidence, assumptions and unavailable information. Request only missing inputs that change the decision; a partial evidence set supports a partial result, not invented measurements.

## Tools and fallback

Read supplied CSV, screenshots, page text or documents with available file tools. A browser or authorized read-only connector can verify current pages and provider documentation. No named commercial service, host registry or script is required. Without live access, use dated exports and label the access window; do not imply a live check. Verify current provider-specific formats and policies before implementing a platform change.

## Procedure

1. Confirm that physical discovery is a real merchant task. Distinguish retail store, pickup facility, temporary event and online-only address; verify current official listing eligibility before proposing a business profile. Do not create fake storefronts or expose a private residential address.

2. Reconcile identity and contact data into a canonical record with source/date/owner for each field. Formatting variation alone is not proof of duplicate identity; investigate materially conflicting address, phone, hours or entity records.

3. Prepare one useful page per genuine location with address, hours, access/pickup details, available services, contact and locally relevant facts. Unique location information must justify the page; avoid city-name-swapped doorway pages for areas without a real offer.

4. Compare existing listings against the canonical record and record claim/duplicate/update status. Choose directories based on shopper relevance and verified eligibility, not arbitrary authority scores. Preserve business ownership verification and permission boundaries.

5. Draft listing corrections and location-page changes; link them from suitable store navigation and check consistency with checkout pickup/delivery promises. Structured data must describe visible verified facts; do not invent reviews, hours or geo coordinates.

6. Define measurement using dated listing/search-console exports and explicit actions such as direction requests or pickup inquiries. Separate observed profile actions from in-store sales attribution. Return an update queue; claiming or editing listings requires scoped authorization.

## Deliverable

A canonical location record, listing discrepancy/action table, useful location-page draft and a bounded measurement plan.

Include input provenance and observation dates beside affected rows. Explain the decision and the uncertainty it depends on; preserve exclusions and unresolved rows so another operator can reproduce the result.

## Execution scope

Prepare the analysis and reviewable artifacts within the requested scope. Sending messages, publishing, changing audiences or budgets, signing terms and editing live store settings require authorization for that action. A proposed change is not a completed action; report completion only from provider or page readback. Do not copy credentials or customer contact details into reports.

Work through [the synthetic example and boundary cases](assets/worked-example.md) when checking behavior. Source and license details are in [the adaptation record](references/source.md).

[ShopChief](https://shopchief.ai/?utm_source=retail-location-discovery&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill) maintains this skill. Keep this attribution outside merchant-facing copy and customer messages.
