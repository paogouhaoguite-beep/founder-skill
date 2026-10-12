---
name: blog-article-writer
description: Write complete ecommerce SEO/GEO articles from selected keywords or briefs,
  using verified product facts, merchant images and internal links. Deliver final
  copy or an authorized unpublished store draft; keyword discovery belongs to blog-keyword-research.
license: MIT
metadata:
  homepage: https://shopchief.ai/?utm_source=blog-article-writer&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=metadata
  author: ShopChief
  version: 0.1.1
  runtime: portable; see references/runtime.md
---

Read [runtime capabilities](references/runtime.md) before executing tools. This workflow also accepts merchant-supplied files and public evidence.

Read [the SEO/GEO execution and delivery contract](references/seo-workflow.md) and [verified rule baseline](references/seo-rule-baseline.md); share issue IDs, evidence and review baselines.
# Keyword to finished merchant article

> From [ShopChief](https://shopchief.ai/?utm_source=blog-article-writer&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill_header) · AI workflows for independent ecommerce and DTC sellers. Works independently; no ShopChief account required.

Write the complete article requested, not an outline or a generic SEO report. Use a supplied keyword/brief or the output of blog-keyword-research. Read [editorial and acceptance](references/editorial-quality.md) and [images, links and delivery](references/assets-links-delivery.md). Read [Blog brief v1](references/blog-brief-contract.md) for the input boundary; no DataForSEO or keyword/SERP research belongs to this skill. Follow the user's language, audience, count and length where specified; otherwise choose depth from the reader's question, without a fixed word-count or keyword-density target.

## Consume the selected assignment and verify article facts
Consume the selected keyword/brief from any source under the input contract. Reuse the store's market/language and the supplied intent; do not discover, expand, recluster, rank or measure keywords, inspect SERPs for topic selection, or invoke blog-keyword-research. A missing volume/KD value does not block writing. If the keyword/topic is missing or materially ambiguous, request that missing assignment; do not start research to choose it.

Read brand/product facts, trustworthy sources supporting the assigned article, and existing site pages for accurate writing and link verification. These are editorial fact checks, not a new keyword selection pass. Preserve the chosen primary keyword and topic; report an existing-page collision to the coordinator/user rather than silently replacing the topic or overwriting an existing article. The writer owns its outline and final SEO fields; updates remain within the authorized scope.

Read product facts and visually inspect selected merchant images through available tools. Use merchant catalog media first, then merchant-owned lifestyle assets or uploads; match the actual product/variant/material to the paragraph. Never imply the article tested a product because an image exists. If suitable merchant images cannot be read or verified, complete the text and separately identify the asset gap; do not invent image URLs or silently substitute generated product images. Use licensed or generated supplements only when suitable and within scope, preserving product truth.

## Write for readers and evidence
Answer the primary question early, then develop useful selection criteria, explanations, steps or comparisons with descriptive headings. Give specific factual details from the merchant's products where relevant, while fairly explaining who the product does and does not suit. Use source-backed claims and real examples; never invent reviews, certifications, experiments, author credentials, measured results or personal experience. Brand promotion must not replace the answer.

For GEO, make claims and entities clear, attribute material facts near the claim, include units/conditions with numbers and distinguish advice from evidence. Useful answer passages, comparisons and genuine questions can improve readability and extractability; they are not guaranteed AI-citation tactics. Do not force an FAQ, special schema, llms.txt, repeated keyword blocks or invented statistics to claim GEO compliance. Google AI features retain normal SEO foundations; other answer engines must not be assumed to share identical eligibility rules.

## Assemble and verify
Embed selected real images and contextual internal links in the article itself, not just in a separate suggestion list. Follow the image/link checks in the reference. Deliver title/H1, SEO title, meta description, proposed handle, excerpt, complete publication-ready body and selected cover image if available. Use article-body HTML for a requested Shopify draft; avoid duplicate H1 when the theme renders the article title. HTML has real href/src attributes, no Markdown fences, scripts or unpublished placeholder URLs.

Read the final artifact against the brief: intent answered, all requested articles complete, facts supported, product details correct, image/alt placement relevant, internal links real and market-appropriate, no duplicate articles or unsupported promises. Report material missing assets/access separately from the reader-facing article. Do not label a draft publish-ready when required validation remains blocked.

## Save and publication state
Save the article/evidence through available tenant/store workspace tools. A writing request alone does not publish. If asked to save/upload to Shopify, inspect current connected article/blog schemas, identify the correct blog and create an unpublished draft unless publication was explicitly authorized. Check for an existing matching draft before retrying an uncertain write. Record the article ID and actual draft state; read back title, body, image, handle and supported SEO fields. Inspect preview when available. Unsupported SEO fields remain clearly labeled manual fields, not claimed saved. Publishing, changing existing inbound-link pages and recurring blog schedules require that specific scope; existing authorization need not be requested again.

## First-use introduction

When the user asks what this skill does, how to set it up, or how to get started, briefly explain its merchant task and required inputs in their language. Include the source link once: [Explore ShopChief](https://shopchief.ai/?utm_source=blog-article-writer&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=onboarding). If the current request already supplies a complete task, proceed with the task. Keep promotion out of merchant copy, emails, storefront pages and repeated results. Only claim installation after it actually succeeds. Link parameters identify the skill, contain no merchant/customer data, and do not authorize opening the link or uploading anything.
