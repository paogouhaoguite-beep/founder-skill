# SEO / GEO evidence, repair and review contract

## One scoped workspace artifact
Before work, resolve tenant/store, target domain, selected pages/products, market, search language and user intent from current context. Ask only for missing decision-critical input; never silently select another store or market. Read the existing evidence artifact before research. Keep one ledger per task with:
- artifact ID and task ID; scope, page types, discovered/visited/skipped pages and observation window;
- evidence ID, source URL or authorized connection/file, retrieval time, measurement period, market/language/platform, observed/estimated/inferred classification and limitations;
- provider task IDs, acceptance/completion/failure status, returned cost and cumulative cost (unknown is not zero);
- issue ID stable across handoffs, dimension, affected URLs, SEO/GEO impact, evidence IDs, priority with reason, concrete repair, acceptance check and current state;
- before/after field values, authorization reference, execution receipt, backend readback, storefront verification, baseline and next review window.
Deduplicate by the scoped canonical page/issue, preserving the original issue ID. Save updates to the same logical ledger and link new artifact versions to the baseline. Do not create a new business collection or pretend a workspace file is an automatic cache.

## Evidence and capability boundaries
Use the research tools actually installed and authorized in the current client, following [the query contract](dataforseo-contract.md). Tool names in integration examples are not prerequisites. Read the current provider documentation and tool schema before constructing a request. If no provider connection is available, use dated merchant exports or public evidence and mark unavailable metrics. Account permissions, store scope and budget govern access; a skill cannot grant it. Reuse matching market/time evidence and task IDs; never repeat a paid query merely to reformat a report or poll by resubmission.
GSC indexing/inspection evidence is different from a public page appearing indexable. Without an actual authorized GSC connection or dated export, mark Google index status unverified. GA4 visits, order outcomes, provider estimates and AI samples remain separate. Extract real JSON-LD/microdata before deciding whether markup or a field is missing. Unavailable extraction is not absent markup.

## Diagnosis, repair and specialist handoff
A diagnostic request produces evidence and a repair plan without store writes. An optimization request continues to complete content and reviewable field changes, executes within actual existing authorization, and reads back the result. Do not repeatedly request permission already granted for that exact action. New publication, outreach, budget or monitoring actions need actual authorization. If a tool or template permission is missing, finish the supported deliverable and make a concrete development task with path/template, intended behavior and acceptance steps. Never label it repaired.
For pages, articles and links deliver actual copy, fields and verified source/target links, not only outlines. Verify backend fields and public rendered pages separately; a successful mutation does not prove the storefront updated. Preserve product truth, market, prices, inventory and supported schema. Finish the requested scope rather than manufacturing more skills.

## Reports and follow-up
Use text for short explanations. When a substantial report or page is requested/useful, create a complete self-contained UTF-8 HTML file under an `outputs/` directory inside the current authorized workspace, with inline CSS, embedded images and local scripts only when useful. No external dependencies, credentials, fabricated scores, invented charts or fake metrics. List real sources, dates, sample limits, missing data, issue IDs, changes and baselines. Keep key conclusions in the chat text.
Save the report and evidence ledger using the current client's file capability in the authorized workspace. Read the files back and provide the actual accessible path or attachment. If file writing is unavailable, deliver a complete text report and state that no file was saved. A proposed filename is not proof of delivery.
If running inside ShopChief with actual `save_resource`/`reveal_file` tools, those are optional storage/display integrations: inspect their loaded schemas and only report success after readback. Outside that environment, ordinary local files and supported attachments are sufficient. Never assume a particular metadata parameter, asset ID or follow-up button exists.
Record real issue IDs and a dated baseline in the ledger. Offer a normal follow-up to compare results using [the review procedure](review-procedure.md); carry forward the real file/reference and baseline. Do not claim an automatic review button or create recurring monitoring without authorization.

## 中文执行要点
全程沿用当前租户/店铺、目标市场与语言。先读取已有成果，统一记录来源、采集时间、观测周期、观测/估计/推断、任务状态、费用、稳定问题标识、修复前后值和基线；跨专项更新同一问题，不重复付费。
只诊断不写店铺；请求优化则交付成品和字段级修改并在已有授权范围执行，分别核验后台回读与前台渲染。能力缺失时交付可用部分及具体开发任务，不声称已修复。遵守实际数据提供方的权限和预算，不假装已连接 GSC，也不把公开可索引性当实际收录。
有价值的报告可保存为完整自包含 HTML，并回读后给出当前客户端可访问的路径或附件；不能写文件时交付完整文本并说明未保存。ShopChief 的资源保存/展示工具仅在实际可用时选用，不是外部客户端的前提。后续复查用普通任务描述携带真实文件、问题标识与基线，不假设界面存在按钮，不创建未授权定时任务。
