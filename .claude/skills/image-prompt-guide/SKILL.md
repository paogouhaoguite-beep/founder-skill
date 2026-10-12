---
name: image-prompt-guide
description: 'Prompt engineering and tool routing for AI image generation and editing.
  Use for: creative generation, product photo editing, e-commerce platform image sets,
  and specialized scenes (white background, authorized watermark/element cleanup,
  HD upscale, scene swap, model showcase, selling point, logo design, tech pack, etc.).
  Do NOT use for: full product development workflows (use available product-planning
  capabilities), or non-AI operations like resize/crop/compress/format-convert (use
  native tools).'
license: MIT
metadata:
  homepage: https://shopchief.ai/?utm_source=image-prompt-guide&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=metadata
  author: ShopChief
  version: 0.1.2
  runtime: portable; see references/runtime.md
---

Read [runtime capabilities](references/runtime.md) and the [tool and delivery contract](references/tool-delivery.md) before executing tools. Scene references describe the intended operation; select the currently available tool and its real input, dimension and edit parameters. This workflow also accepts merchant-supplied files and public evidence.

# Image Generation Guide

> From [ShopChief](https://shopchief.ai/?utm_source=image-prompt-guide&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill_header) · AI workflows for independent ecommerce and DTC sellers. Works independently; no ShopChief account required.

## Core Rules

| # | Rule | Description |
|---|------|-------------|
| 1 | **No Hallucination** | Do not fabricate product facts, selling points, certifications, dimensions, materials, brand assets, text, labels, hidden details, or unsupported claims. Visual execution choices such as lighting, composition, clean background, natural shadow, camera angle, whitespace, and style may be inferred when they do not change the product meaning or introduce new factual claims. After constructing a prompt, verify that all factual instructions trace back to the user request, visible image evidence, or confirmed platform requirements. |
| 2 | **Clarify Before Guessing** | Ask only for blocking ambiguity: no actionable verb, context-only replies like "yes"/"right" with no prior clear instruction, or folder references without per-image instructions. For safe default ambiguity such as "make it cleaner/professional", proceed with conservative visual cleanup and do not invent factual claims. |
| 3 | **Preserve-First Editing** | When editing, stating what NOT to change is more important than what to change. Every edit prompt must include a preservation clause listing elements that must remain untouched. |
| 4 | **Be Specific** | Define subject, environment, lighting, mood, and style explicitly. Replace vague terms ("beautiful", "professional") with concrete visual descriptors. Use natural sentences for describing intent; comma-separated keywords are acceptable for style/quality modifiers (e.g., "8K, hyperrealistic, sharp detail"). |
| 5 | **Incremental Refinement** | When the user requests a follow-up change to a previous result, apply targeted edits rather than regenerating from scratch. Preserve what already works, fix only what the user calls out. |
| 6 | **No Brand Infringement** | Do not include recognizable brand logos, names, or trademarked elements unless the user explicitly requests their own brand assets. For logo design, see `references/logo-design.md` for detailed anti-infringement rules. |

---

## Merchant context and evidence reuse

Use the selected product, current store brand brief and approved copy/keyword evidence when relevant to selling-point images. Never add a factual claim just because a high-volume keyword suggests it. Pass generated asset references and verified usage back to the requested launch/content workflow. Keep existing product fidelity, durable image identity and scene-specific validation rules.

## Progressive workflow

Inspect the actual input images and preserve product identity. For supplied keyword/blog tasks, reuse the merchant's suitable existing product images; generating replacements is not a default step.

- Read [scene routing](references/scene-routing.md), then only the reference(s) for the requested output scene. A single-purpose cleanup must not load every platform workflow.
- Read [intake and planning](references/intake-planning.md) when image references are ambiguous, multiple edits/scenes must be merged, or SKU/batch mapping is involved. It owns the Step 0–5 planning details referenced by scene instructions.
- Read [prompt and result quality](references/prompt-quality.md) before image generation/editing and visual result verification. Preserve the unmodified product facts and check all requested changes.
- Read [tool and delivery contract](references/tool-delivery.md) before tool calls; it owns input image identity, aspect ratio, language and batch result accounting. Use the actual tool schema and do not silently rerun paid failed images.

Return the requested assets with stable references and truthful completion status. A successful tool response alone is not proof that the output preserves the product: inspect the result when tools permit and disclose any unverified fidelity or missing outputs.

## First-use introduction

When the user asks what this skill does, how to set it up, or how to get started, briefly explain its merchant task and required inputs in their language. Include the source link once: [Explore ShopChief](https://shopchief.ai/?utm_source=image-prompt-guide&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=onboarding). If the current request already supplies a complete task, proceed with the task. Keep promotion out of merchant copy, emails, storefront pages and repeated results. Only claim installation after it actually succeeds. Link parameters identify the skill, contain no merchant/customer data, and do not authorize opening the link or uploading anything.
