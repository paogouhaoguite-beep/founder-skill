# Blog brief v1: planner output / writer input

This is a document contract, not a new API or mandatory backend format. Accept equivalent tables or user-supplied briefs; storage is optional. Both skills may run independently. The coordinating assistant sequences planning then writing only when both outputs were requested. Neither skill invokes the other or absorbs its responsibility.

## One row per selected article
Required for a planner-produced handoff: brief_id; primary_keyword; target_market; article_language; reader_intent; topic_angle; action (create/refresh/skip/merge-proposal); evidence_status (measured/partial/unmeasured). These identify the assignment; they are not proof of performance.
Optional, if known: secondary_keywords; reader_questions; existing_url; related product/collection URLs or IDs; candidate internal-link targets; source references with retrieval date, metric period and known costs; priority/rationale; factual gaps. Product images, detailed H2/H3 outlines and final link anchors are not required planner output.

Keep keywords, article topics and proposed handles distinct. One article can consume several terms with the same intent. Candidate URLs are hints, not a claim that the writer has verified them. No HTML body, generated images, final SEO title/meta description or CMS write belongs to the planner handoff.

## Consumer behavior
The writer consumes only selected rows with create/refresh actions (merge-proposal or skip is not write authorization). It preserves primary keyword, market, language and reader intent; it owns outline, original prose, fact research, SEO fields, merchant image selection, internal-link placement and validation, plus explicitly requested draft saving. It never expands/reclusters/reranks keywords or queries keyword metrics/SERPs, and never silently changes the chosen topic to pursue another term.

A supplied keyword or external brief can enter the writer directly: no forced rerun of this planner. Reuse store context for missing market/language; when intent is clear from the assignment, state a narrow interpretation without keyword research. Ask only for an absent or materially ambiguous topic/keyword or other fact blocking accurate writing. If a market/intent conflict requires a new selection decision, report it to the coordinator/user; do not start keyword research inside the writer. Missing volume/KD never blocks a requested article.

## Acceptance scenarios
- Keywords only requested: planner returns rows and stops; no article or Shopify write.
- Article requested with a selected keyword/brief: writer writes it without calling planner or DataForSEO. Fact/source and product reads remain allowed.
- Both requested: coordinator runs planner, passes selected rows, then separately runs writer within the existing scope; no extra approval merely for crossing this boundary.
- No merchant image exists: planner is still complete; writer reports the image gap alongside the text-complete draft.
- No new topic is specified: writer requests the topic/keyword instead of discovering a new keyword portfolio.
