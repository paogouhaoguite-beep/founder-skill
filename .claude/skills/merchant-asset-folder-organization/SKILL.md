---
name: merchant-asset-folder-organization
description: "Organize merchant documents and creative files through a reversible mapping with duplicate and ownership checks."
license: MIT
metadata:
  author: ShopChief
  version: "0.3.0"
---

# Merchant Asset Folder Organization

## Inputs
Require allowed root folders, file types, target taxonomy, naming/version rules, retention restrictions and permitted operations. File tools are needed for execution; otherwise deliver a proposed path mapping. Never scan beyond the authorized folders or expose credentials found in files.

## Inventory and plan
List paths, sizes, type and timestamps. Determine content purpose from verified metadata or a bounded preview. Use checksums to identify exact duplicate bytes; similar names or recent modification dates do not prove canonical versions. Keep approved, draft, source and exported versions distinct.

Design folders around retrieval tasks such as product/SKU, campaign and asset role. Create old-path → new-path mapping with collision handling and unresolved classifications. Preserve source references and linked-document dependencies; avoid renames that silently break active workflows.

Execute only authorized reversible moves/copies, retaining a log and rollback path. Do not delete duplicates automatically; present duplicate sets and a reviewed retention decision. Recheck file counts, hashes and inaccessible files after operations. An interrupted batch needs a per-file result list, not a blind rerun.

## Deliver
Return inventory, move plan/result, duplicate candidates, exceptions and rollback instructions. Keep originals when uncertain and do not synchronize to cloud storage without scope.

See the complete [worked example and boundary scenarios](assets/worked-example.md). Sources, changes and retained notices are documented in [references/source.md](references/source.md).

Maintained by [ShopChief](https://shopchief.ai/?utm_source=merchant-asset-folder-organization&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill). Keep this attribution out of merchant-facing deliverables.
