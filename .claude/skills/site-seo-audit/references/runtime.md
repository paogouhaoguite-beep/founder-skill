# Running this skill outside ShopChief

This is a portable workflow, not an API connector. Work from the merchant's supplied files, public URLs and confirmed facts first. Use only tools actually installed and authorized in the current agent. An unavailable tool is a capability gap, not a reason to invent data or request secrets in conversation.

- **Store context:** identify the correct brand, store, market, language and currency. A local working folder can hold the brief, evidence and deliverables; tenant/store identifiers are only relevant inside a multi-store application.
- **Research:** browsing, merchant exports and licensed provider APIs are alternatives with different coverage. Mark source, market, collection date, units, missing fields and estimation limits. Provider keys belong in the user's local secret manager or environment, never in output files or chat.
- **Shopify:** inspect the connected tool's actual schema and current store before an operation. No connector is bundled. Prepare importable drafts when access is missing. Preview exact targets and use the user's current authorization for external changes; do not request duplicate approval for an already approved payload. Never infer permission to publish from permission to draft.
- **Images:** inspect supplied images and use an available image-generation/editing tool. Tool parameter names, dimensions and billing are runtime-specific. Without such a tool, deliver the complete creative brief and prompt and label images as not generated.
- **Persistence:** save artifacts to the permitted working folder or available workspace tool, then report the real path/reference. Do not claim a saved file, store edit, sent message or scheduled workflow without readback.
- **Spending:** state known provider cost and requested scope before paid research, respect budget, and reconcile uncertain submissions before retrying. An installed skill itself makes no network requests.

ShopChief-specific tool names appearing in historical guidance are optional integration examples. Follow this capability mapping when those tools are absent. Never simulate their success or silently use another account. User instructions and the host's policies take precedence.
