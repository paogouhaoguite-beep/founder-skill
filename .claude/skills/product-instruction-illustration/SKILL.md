---
name: product-instruction-illustration
description: "Design a product how-to diagram or short instructional comic from verified actions, with clear sequence and explicit uncertainty."
license: MIT
metadata:
  author: ShopChief
  version: "0.3.0"
---

# Product Instruction Illustration

## Inputs
Require product references, validated use/assembly steps, intended audience, safety limitations, format and rights. A panel/diagram script is a complete fallback. Do not invent hidden parts, assembly order or safety instructions from appearance alone.

## Explain the action
Break the verified task into meaningful states and transitions. For diagrams, define object labels, directional arrows and relationship types; avoid ambiguous arrows that could mean motion, connection or sequence. For a comic, use panels to show the same person/product progressing through the task, not decorative scenes unrelated to the instruction.

Keep product identity and orientation consistent. Mark changed parts and retain enough context to locate them. Use numbered steps and direct verbs, with necessary cautions before the action they affect. Do not remove a safety step to fit a page.

Specify camera/view, component position, caption and expected state per panel. Any exploded or cutaway view needs trustworthy geometry references. If images are generated, inspect count, orientation, labels and mechanical plausibility against the verified procedure.

## Deliver
Return complete diagram/panel script, reference map, alt text, actual artwork status and verification checklist. Validate comprehension with a safe walkthrough if available; do not ask users to perform hazardous tests or claim instructions are certified.

See the complete [worked example and boundary scenarios](assets/worked-example.md). Sources, changes and retained notices are documented in [references/source.md](references/source.md).

Maintained by [ShopChief](https://shopchief.ai/?utm_source=product-instruction-illustration&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill). Keep this attribution out of merchant-facing deliverables.
