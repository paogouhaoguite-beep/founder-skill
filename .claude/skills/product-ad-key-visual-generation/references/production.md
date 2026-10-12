# Production notes

## Inputs and identity lock

Product identity images; approved exact headline, offer, CTA and logo artwork; destination aspect/crop; brand colors; required text-safe region. If an offer or claim lacks confirmation, omit it and list the missing copy instead of inventing a promotion.

Assign a stable local reference ID to every actual input, for example `product_primary`, and record its real file path or provider asset ID, role and permitted changes. A filename in a prompt does not attach an image. Inspect each input and use the tool's actual attachment mechanism. Keep the original input available for revisions rather than relying exclusively on a generated derivative.

## Task-specific decisions

Separate product label text from promotional copy: removing all text from an image could erase the real product label. For exact offers, preserve currency, decimal separators, dates, qualifying text and capitalization as approved. Reserve enough copy space at design time instead of covering the product after generation. If only a flattened final image is possible, state that limitation; JSON layout data is editable source information, not a layered image file.

The [worked example](../assets/worked-example.md) supplies a concrete brief, complete prompt, layout and failure cases. Its synthetic facts demonstrate decisions; substitute verified merchant inputs before execution.

## Capability check before a call

Check the installed tool's schema for reference attachments, targeted editing and output retrieval. Check required transparency or exact text composition separately; success in general image generation does not imply those features. Record the actual tool/provider used and the supported settings chosen. Use credentials already configured through the environment; never put credentials into prompts or this package.

For provider-specific implementation details, consult current official [OpenAI image documentation](https://developers.openai.com/api/docs/guides/image-generation) or [Gemini image documentation](https://ai.google.dev/gemini-api/docs/image-generation). Documentation references checked on 2026-10-05. The runtime's available tool and schema determine the call; this package does not promise a fixed model, price, size or feature set.

## Review and delivery

Review the actual returned pixels beside the identity references. Zoom into this task's locked details and inspect the whole composition. Record observed output dimensions/format and a stable output reference; do not fabricate provider request IDs. Distinguish a requested deliverable from a generated file, and a generated file from a reviewed one. A missing tool produces a ready-to-run prompt and manifest, explicitly marked `not_generated`; a failed detail check produces a repair note and a non-approved asset.
