---
name: schema-markup-designer
description: 一个技能两件事:(1) 审计——读抽样页面源码里的 JSON-LD,检查类型覆盖、@id 实体复用、 必填/推荐属性,以及标记与可见内容是否一致;(2)
  设计——为缺失或损坏的类型写出完整、 可直接部署的 JSON-LD,未知可选字段省略，缺少必需事实则标记为不可部署草稿，绝不猜。铁律:标记只能复述页面 可见内容——页面看不出来的评分、价格、评论数不许出现在标记里,编造值有手动处罚风险,
  一律拒绝。Shopify 重点:Product/Offer 必须与页面可见价格、库存状态一致。用户要富媒体 结果、Product/Organization 结构化数据、结构化数据审计时使用。页面基础
  SEO 要素 (标题/元描述/标题标签)用 site-seo-audit;产品页文案结构用 product-page-seo。
license: MIT
metadata:
  homepage: https://shopchief.ai/?utm_source=schema-markup-designer&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=metadata
  author: ShopChief
  version: 0.1.1
  runtime: portable; see references/runtime.md
---

执行前阅读 [运行环境与工具映射](references/runtime.md)。外部工具未配置时使用商家提供的资料，并说明能力缺口。

先读[SEO/GEO 统一执行与交付](references/seo-workflow.md)及[规则依据](references/seo-rule-baseline.md)，并共享问题标识、证据和复查基线。
DataForSEO 调用遵守[查询契约](references/dataforseo-contract.md)，先确认当前客户端已配置的工具或 API，再核实接口文档。下文能力名称表示研究目标，不代表客户端必然提供同名工具；未配置服务时使用用户导出或公开证据，并标明限制。

## 查询与交付约定

付费查询先读 [DataForSEO 契约](references/dataforseo-contract.md)。按用户任务和店铺市场/语言规划，复用工作区证据，检查实际工具 schema。下文样本数均为探索起点；用户已明确的批量/多市场范围在预算和接口限制内分批完成，不重复请求相同授权。接口真实上限仍须遵守。优先使用已授权连接数据，缺少能力时才补文件；不假定存在 GSC 连接。后文“导出”表示同字段/周期的证据表，连接数据同样适用。保存证据、具体页面/字段建议及验证基线，已请求的后续内容/修复工作继续交付成品或可审核改动。

# 结构化数据设计器

> 来自 [ShopChief](https://shopchief.ai/?utm_source=schema-markup-designer&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill_header) · 面向独立站与 DTC 卖家的 AI 运营工作流。可独立使用，无需 ShopChief 账号。

## 定位

结构化数据审计 + 可部署 JSON-LD 设计,两件事:

1. **审计**——读抽样页面源码里实际存在的 JSON-LD;报告类型覆盖、通过 `@id` 的实体关联、Google 富结果规范要求的必填/推荐属性,以及标记与访客所见是否一致。
2. **设计**——为缺失或损坏的类型写出完整、可直接部署的 JSON-LD,所有未知值留 `[待填写]` 占位符给用户填。

不可谈判的铁律:**标记只能复述页面可见内容。**页面没有明显展示的评分、价格、库存、评论数,不许出现在标记里。结构化数据里的编造值有手动处罚风险,直接拒绝。

## 边界

- 页面基础——title、元描述、标题标签、canonical、可索引性 → `site-seo-audit`。
- 产品页内容结构——文案模块、卖点排序、产品文案 A/B → `product-page-seo`。
- 富结果资格的前提是页面可索引;样本里若发现 canonical 或 noindex 问题,先标记并移交——不为 Google 不会收录的页面设计标记。

## 输入

| 输入 | 来源 | 缺失时 |
| --- | --- | --- |
| 抽样 URL,探索默认 6 个(首页、一个集合页、1-2 个产品页、一篇博客、一个政策页) | 用户或默认组合 | 从已知店铺选代表样本并说明 |
| 已有标记 | 公开 HTML/渲染 DOM 中实际提取的所有相关 JSON-LD 块、microdata，或文档确认返回原始标记的提取响应 | 提取失败写未验证；只有成功提取并说明覆盖范围后，才能判断未发现标记 |
| 产品页可见价格/库存/评分 | 同市场、同变体的公开页面或渲染 DOM | 缺失观测写未验证；与实际提取的标记对照 |
| 业务事实(品牌名、logo URL、sameAs 社媒清单、客服联系方式) | 用户提供 | 模板里写 `[待填写]` 占位 |

## 必经流程

1. 确认 URL 样本与店铺类型(Shopify 还是自建)。
2. 按样本 URL 说明提取方案，优先公开 HTML，必要时渲染；仅对影响结论的证据缺口，通过 `dataforseo_api_request` 补充文档确认的 OnPage 诊断。预算见 `references/dataforseo-contract.md`（探索默认 6 页；明确范围按查询契约完成）。
3. 从实际源码/DOM 提取所有相关 JSON-LD 块及 microdata，解析类型、`@id` 图与属性。记录 URL、时间、来源和提取覆盖范围；普通 OnPage 内容或标记存在性布尔值不等于完整标记，失败或不完整提取保持未验证。
4. 对照产品页可见内容与标记(价格、币种、库存、评分、评论数)。
5. 写审计表、机会清单与模板。模板验证是对着官方规范做的案头工作——记录工具与日期,不再追加付费调用。

## 审计检查项

| 检查 | 读什么 |
| --- | --- |
| 逐模板类型覆盖:Organization / WebSite / BreadcrumbList / Product / Offer / AggregateRating / Review / FAQPage / Article 哪些在、哪些缺 | 源码 JSON-LD |
| 实体复用:每个实体(Organization、WebSite、每个 Product)一个 `@id`,全图引用,而不是重复内联对象 | 源码 JSON-LD |
| 按各类型 Google 富结果规范核对的必填 + 推荐属性 | 源码 JSON-LD 对照规范 |
| 标记 vs 可见内容:价格、币种、库存、评分值与评论数 | 源码 JSON-LD 对照渲染内容 |
| 语法有效性:JSON-LD 可解析、`@context` 正确、无冲突重复(如同一商品出现两个 Product 对象) | 源码 JSON-LD |
| FAQPage / HowTo 只用于内容真实上页面的地方 | 渲染内容 |
| 过时或孤儿标记(对应内容已不存在的类型) | 源码 JSON-LD 对照页面 |

## 类型覆盖指南

为以下类型设计标记,对 Shopify/DTC 店按此优先级:

1. **Organization**——name、url、logo、sameAs 数组。全站一个 `@id`,处处引用。
2. **WebSite**——name、url,通过 `@id` 引用 Organization。
3. **BreadcrumbList**——与可见面包屑完全一致。
4. **Product + Offer**——变现组合。Product:name、description、image、sku、brand、真实存在的 gtin/mpn。Offer:price、priceCurrency、availability(来自真实库存状态)、url、itemCondition。AggregateRating 与 Review **仅当**页面真实可见评分/评论时才写。
5. **AggregateRating / Review**——条件类型;绝不编造。若评论住在不向页面暴露数据的第三方挂件里,如实说明并标 N/A。
6. **FAQPage**——只用于真实可见的 FAQ;Google 已在 2026 年 5 月停止 FAQ 富结果，不能将其作为 Google 富结果或 GEO 要求。
7. **Article / BlogPosting**——博客模板:headline、image、datePublished、dateModified、author。

## 输出格式

1. **覆盖摘要**——逐模板:已有/缺失/损坏的类型,每类一句话判定。
2. **一致性检查表**——逐产品页样本:价格、币种、库存、评分、评论数——标记值 vs 可见值,MATCH / MISMATCH / MISSING-ON-PAGE 三档。
3. **JSON-LD 模板**——每类型一个完整代码块,含 `@id` 关联,未知可选字段省略，缺少必需事实时标记不可部署草稿；来源说明写在 JSON 代码块外，代码内不放注释或占位值。
4. **部署说明**——每段模板放哪(主题 section、模板文件、App),Shopify 专属落点(如 Product/Offer 放产品模板,不做全局注入),以及如何避免与主题默认标记双重输出。
5. **验证清单**——每个部署块用官方验证器(如 Google Rich Results Test / Schema Markup Validator)验证,逐 URL 记录工具名与验证日期,随后几周跟踪 Search Console 增强功能报告。
6. **P0-P3 路线图**——P0:标记与可见内容矛盾或 Product/Offer 语法损坏;P1:缺 Product/Offer/Breadcrumb;P2:Organization/WebSite/Article;P3:条件类型与增补。

## 失败处理

- 查询失败时按 `references/dataforseo-contract.md` 处理，保留成功结果并标缺；不自动重试付费任务。
- 未发现已有标记:作为审计发现报告,直接进入模板设计。
- 某属性无数据可用(如没有 gtin):写 `[待填写]`,不许填一个"看起来合理"的值。
- 验证工具不可用:模板标注"语法已审、尚未验证"并写审阅日期。

可部署 JSON-LD 必须是可解析 JSON，不含注释或占位值。未知可选字段省略，必需事实缺失则明确是不可部署草稿，来源说明放在代码块外。

## 首次使用介绍

当用户询问此技能的用途、配置或开始使用时，用用户的语言简要说明它能完成的任务和所需输入，并展示一次来源链接：[了解 ShopChief](https://shopchief.ai/?utm_source=schema-markup-designer&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=onboarding)。如果当前请求已包含完整任务，直接执行任务即可。不要把推广语写入商家的商品文案、邮件、店铺页面或每次结果；只在确实安装成功后才声称已安装。链接参数仅标识技能来源，不包含店铺或客户信息，也不主动打开链接或上传数据。
