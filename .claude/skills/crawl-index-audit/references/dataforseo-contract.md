# Search evidence and DataForSEO integration

## Choose the evidence route
Use the merchant's dated exports or existing research when sufficient. For new search evidence, use a provider connector already installed and authorized in the host, or the provider's documented API through an approved local client. This package does not bundle credentials, a paid account, a connector, or free API credits. Public web research is useful but cannot be presented as provider volume, CPC, KD, backlink or traffic data.

DataForSEO documentation: https://docs.dataforseo.com/v3/ . Verify the exact endpoint, HTTP method, payload, location/language identifiers, task limits, returned fields and current price before execution. Names of API families elsewhere in the skill are research objectives, not valid tool names or guessed URL paths.

In ShopChief, the optional adapter names are `dataforseo_docs_list_sections`, `dataforseo_docs_index`, `dataforseo_docs_search` and `dataforseo_api_request`. In another host, inspect that host's tool schema; do not pass ShopChief arguments into a different connector. The documentation tools and API response envelope are not universal provider interfaces.

## Scope, cost and coverage
Resolve the target country, search language, dates and requested products/URLs. Do not silently use the US market for another country's store. Deduplicate requests and reuse evidence. State the requested scope, intended calls and known cost; an unavailable price is unknown. Stay within the agreed monetary/call limit. User-authorized batches may be split to provider limits without asking again for the same scope.

Inspect provider- and task-level statuses, pagination and truncation. Async task acceptance is not completed research: retain task IDs, retrieve results, and never resubmit to poll. Do not automatically retry paid requests or ambiguous submissions. Record actual returned cost separately from an estimate; retrieval responses containing historical task cost do not establish a new charge.

## Interpret evidence correctly
- Search volume is modeled search demand, not product sales. CPC is an external estimate, not the merchant's realized acquisition cost.
- Paid competition is not organic keyword difficulty. Missing fields stay unknown.
- Domain traffic estimates are not first-party visits, conversion rate or orders.
- Search trends are normalized series unless the provider documents absolute units. A single observation cannot establish growth.
- Public ad presence/duration does not establish spend, profitability or winning creative.
- Merchant exports or authorized first-party connectors establish account performance; never assume GSC, GA4 or Google Ads is connected.
- For schema, links, canonicals and hreflang, inspect actual HTML/rendered output or documented extraction. Missing extraction fields do not prove missing markup.
- Label public research, samples, account data and modeled values separately.

## Deliver an actionable evidence record
Include source URL/provider, observation date/window, market/language, requested and returned coverage, units, task IDs where relevant, cost when known, limitations, finding and recommended merchant action. Preserve supplied input identities. A constrained or missing data route should narrow the conclusion, not generate fabricated numbers.
