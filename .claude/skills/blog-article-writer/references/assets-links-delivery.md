# Merchant images, internal links and article delivery

## Images: select actual assets first
1. Read related product media from the current store/catalog and merchant uploads. Select the exact product/variant for the point being illustrated; merchant-owned lifestyle photography can be more useful than repeatedly inserting a packshot. Inspect candidate images visually when tools permit. Record asset ID, source URL, product ID, intended section, alt text and verified/unverified status.
2. Prioritize usable merchant product imagery. Use an existing real photo unchanged when it answers the need; don't call image generation to recreate it. Avoid competitor imagery without rights. Missing or unsuitable assets permit a text-complete draft with an explicit image gap, not fake URLs or unrelated stock products. Generated explanatory illustrations are optional supplements within scope and must not masquerade as actual product evidence.
3. Place images near relevant text. Choose a cover only if it suits the article; image count follows content needs, not a quota. Use concise descriptive alt text for informative images, empty alt for purely decorative images, no keyword stuffing. Preserve material, color, proportions and labels when any authorized edit is requested.
4. Verify public fetchability and correct image content when possible; use stable merchant/CDN URLs, not expiring signed links, local paths or private download URLs in the publishing body. Record verified dimensions when known, choose an appropriate existing rendition and preserve aspect ratio. Below-fold lazy loading is appropriate when supported; do not force lazy loading of a visible cover/LCP image. Do not claim image checks passed when access is blocked.

## Internal links: use real destinations in the body
Discover links from the authorized catalog, existing blog index, navigation/sitemap or fetched pages. Verify final destination and language/market alignment; use the actual canonical route, not a guessed /products/ or /blogs/ handle. Prefer the resolved live destination over redirect chains. Exclude broken, archived/private/draft-only, cart/checkout, tracking and irrelevant filtered links. If public availability cannot be checked, mark the link unverified and omit it from a claimed publish-ready body until resolved.

Choose contextually useful product, collection and related-article links. Use descriptive natural anchors that explain the destination and match the surrounding claim. No fixed link density, repeated exact-match anchors or links to every product. HTML output uses real <a href="..."> elements; Markdown links are fine for a Markdown artifact. Internal links need no routine nofollow/new-window flags. A same-store market subdomain can qualify; a merchant CDN image URL is an image source, not an internal content link.

Plan an inbound link from an existing relevant page when useful, with exact source URL, suggested sentence/anchor and destination. If the new article URL is still proposed, keep the inbound edit in the handoff only. Do not edit other pages or insert public links to an unpublished article without authorization and a live destination.

## Deliverable and save receipt
- SEO fields: article title, SEO title, meta description, excerpt, proposed handle, language.
- Complete body with embedded verified images and contextual links; cover source/alt if available. No invented URLs or internal handoff notes in the reader-facing body.
- Compact asset/link register: source IDs/URLs, section/anchor or alt, final URL, verification time/status, missing items.
- Facts/source notes and optional inbound-link proposals outside the article.
- Save result: workspace reference or Shopify blog/article ID, actual unpublished/published state, preview URL if returned, fields verified by readback and fields unsupported by the connected schema. Never claim public verification from an inaccessible draft preview.

Illustrative acceptance: a verified photograph of Product A may illustrate Product A's design, but not a made-up durability test; a care guide links to Product A only when the verified material/care matches. If no suitable image exists, the article remains text-complete with the missing image called out separately. These examples are decision patterns, not live merchant facts.
