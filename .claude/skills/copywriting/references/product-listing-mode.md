# Product Listing Mode

Use this reference when the user asks for product titles, product descriptions, bullets, SEO meta, marketplace listing copy, PDP copy, or bulk product copy.

This mode belongs to `copywriting`. Do not use it for image composition, image generation, or platform posting schedules.

## Inputs

Collect only the fields that materially affect copy:

- Product name, category, target buyer, and platform.
- Confirmed features, specifications, materials, dimensions, package contents, and usage cases.
- Primary buyer problem, desired outcome, differentiator, and proof.
- Brand voice, price tier, region, language, and prohibited claims.
- SEO keywords if supplied by the user or discovered from trusted context.

If specs, certifications, reviews, numbers, or guarantees are missing, do not invent them. Mark them as missing or use a neutral placeholder.

## Workflow

1. Identify the platform: Shopify/DTC, Amazon, eBay, Etsy, TikTok Shop, or generic ecommerce.
2. Read `references/platform-listing-rules.md` when platform-specific fields or limits matter.
3. Separate facts from persuasion:
   - Facts: materials, dimensions, compatibility, included items, certifications.
   - Benefits: outcomes, use cases, emotional value, convenience.
   - Proof: reviews, test data, awards, certifications, guarantees.
4. Build a feature-to-benefit map before writing.
5. Write the listing in the user's requested language.
6. Keep claims compliant: no unverifiable medical, financial, safety, certification, or performance claims.
7. If the user also needs product images, hand off image requirements to `image-prompt-guide`.

## Output Structure

Default output:

1. Product title
2. Short description
3. 5 bullet points
4. Long description
5. SEO title
6. SEO meta description
7. Search keywords or tags
8. Compliance notes and missing facts

For bulk product work, output a table with one row per product and keep each field short enough for import into ecommerce systems.

## Copy Rules

- Lead with the buyer outcome, not a generic adjective.
- Translate features into concrete use cases.
- Keep title keywords natural; do not keyword-stuff.
- Prefer specific nouns and verbs over hype words.
- Use simple, scannable bullets for marketplace listings.
- Preserve brand voice, but never sacrifice clarity.
- Do not include review quotes, star ratings, certifications, awards, or test numbers unless provided.
