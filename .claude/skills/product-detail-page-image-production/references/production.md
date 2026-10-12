# Production notes

## Inputs and identity lock

SKU/variant and identity images; approved product facts and supporting close-ups; module order or buying questions; exact copy and brand artwork; desktop/mobile placement dimensions when known. Map each module to a reference and a supported claim. Identify any module needing a diagram, photograph, exact typography or source evidence not yet supplied.

Assign a stable local reference ID to every actual input, for example `product_primary`, and record its real file path or provider asset ID, role and permitted changes. A filename in a prompt does not attach an image. Inspect each input and use the tool's actual attachment mechanism. Keep the original input available for revisions rather than relying exclusively on a generated derivative.

## Task-specific decisions

A detail module must answer a buying question using visible evidence. A decorative lifestyle image does not prove durability, capacity or material composition. Dimension lines are graphic annotations derived from supplied measurements, not measurements of generated pixels. Keep exact numerical copy outside stochastic image generation when a deterministic layout option exists. The requested mobile aspect is a design brief, not proof that the runtime can render it natively; supported generation followed by a verified crop/recomposition is acceptable.

The [worked example](../assets/worked-example.md) supplies a concrete brief, complete prompt, layout and failure cases. Its synthetic facts demonstrate decisions; substitute verified merchant inputs before execution.

## Capability check before a call

Check the installed tool's schema for reference attachments, targeted editing and output retrieval. Check required transparency or exact text composition separately; success in general image generation does not imply those features. Record the actual tool/provider used and the supported settings chosen. Use credentials already configured through the environment; never put credentials into prompts or this package.

For provider-specific implementation details, consult current official [OpenAI image documentation](https://developers.openai.com/api/docs/guides/image-generation) or [Gemini image documentation](https://ai.google.dev/gemini-api/docs/image-generation). Documentation references checked on 2026-10-05. The runtime's available tool and schema determine the call; this package does not promise a fixed model, price, size or feature set.

## Review and delivery

Review the actual returned pixels beside the identity references. Zoom into this task's locked details and inspect the whole composition. Record observed output dimensions/format and a stable output reference; do not fabricate provider request IDs. Distinguish a requested deliverable from a generated file, and a generated file from a reviewed one. A missing tool produces a ready-to-run prompt and manifest, explicitly marked `not_generated`; a failed detail check produces a repair note and a non-approved asset.
