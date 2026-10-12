---
name: merchant-customer-record-merge-plan
description: "Prepare a reversible review of customer-record duplicates, field conflicts and associations without merging live identities."
license: MIT
metadata:
  author: ShopChief
  version: "0.3.0"
---

# Merchant Customer Record Merge Plan

Use for DTC customer or wholesale-contact exports before migration or cleanup. Require full source exports, record IDs, field definitions, consent provenance, associations, as-of date and allowed use. Keep originals read-only. Use local CSV tools or manual pair tables; no upstream scripts are bundled or required.

Separate original values, normalized comparison keys and proposed stored values. Trim obvious whitespace for matching, preserve original identifiers, and use region-aware phone parsing only when country context is known. Do not silently strip email dots/plus tags, guess country codes, rewrite cultural names or correct domains. Similarity is a candidate-generation signal, never identity proof.

Block candidate pairs using suitable identifiers; record skipped large blocks and missing coverage. Inspect non-shared email/phone plus compatible names and source evidence. Shared household email, office number, role address, recycled contact details and equal names require review. Recheck every pair inside a proposed cluster: A≈B and B≈C do not establish A=C.

For each owner-approved candidate, nominate the survivor and every field's winner/source/reason. Preserve nonempty conflicting values in the review register instead of overwriting with blanks. Keep historical orders and associations linked to their original evidence; identify orphan relationships and re-pointing proposals. Do not promote consent or lifecycle state merely by taking the furthest or most permissive value. Conflict in consent requires provenance review, not inferred permission.

Deliver pair review queue, cluster-level consistency checks, field conflict ledger, association plan and counts in/out. Produce a proposed cleaned export only for approved decisions, keyed by source ID and explicitly marked unapplied. Distinguish potential matches from reviewed matches; when labeled truth exists report pairwise precision/recall on that sample, not universal accuracy. Live merge, deletion, import and messaging need explicit authorization and a verified native rollback/recovery plan.

See the complete [worked example and boundary scenarios](assets/worked-example.md). Sources, changes and retained notices are documented in [references/source.md](references/source.md).

Maintained by [ShopChief](https://shopchief.ai/?utm_source=merchant-customer-record-merge-plan&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill). Keep this attribution out of merchant-facing deliverables.
