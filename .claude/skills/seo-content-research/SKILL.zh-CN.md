---
name: seo-content-research
description: 当商品已经上架或在售,用户需要 SEO 内容方向、选题与大纲研究、程序化关键词矩阵、UGC/品类内容角度、关键词到页面映射、内容 brief
  或优先级时使用。证据直接通过 已配置的 DataForSEO 工具与公开网页检索收集,遵守本文件的数据契约。给定关键词清单查指标(搜索量、KD、CPC、意图)用 keyword-analysis
  技能。域名健康与技术体检用 site-seo-audit。不得输出继续、测试或放弃的商品机会决策。 博客关键词与 brief 用 blog-keyword-research，按关键词生成完整博客用
  blog-article-writer。本技能保留跨页面内容策略和非博客规划，复用已有证据；专项技能不可用时继续完成可支持的交付。
license: MIT
metadata:
  homepage: https://shopchief.ai/?utm_source=seo-content-research&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=metadata
  author: ShopChief
  version: 0.1.1
  runtime: portable; see references/runtime.md
---

执行前阅读 [运行环境与工具映射](references/runtime.md)。外部工具未配置时使用商家提供的资料，并说明能力缺口。

先读[SEO/GEO 统一执行与交付](references/seo-workflow.md)及[规则依据](references/seo-rule-baseline.md)，并共享问题标识、证据和复查基线。
DataForSEO 调用遵守[查询契约](references/dataforseo-contract.md)，先确认当前客户端已配置的工具或 API，再核实接口文档。下文能力名称表示研究目标，不代表客户端必然提供同名工具；未配置服务时使用用户导出或公开证据，并标明限制。


## 查询与交付约定

付费查询先读 [DataForSEO 契约](references/dataforseo-contract.md)。按用户任务和店铺市场/语言规划，复用工作区证据，检查实际工具 schema。下文样本数均为探索起点；用户已明确的批量/多市场范围在预算和接口限制内分批完成，不重复请求相同授权。接口真实上限仍须遵守。优先使用已授权连接数据，缺少能力时才补文件；不假定存在 GSC 连接。后文“导出”表示同字段/周期的证据表，连接数据同样适用。保存证据、具体页面/字段建议及验证基线，已请求的后续内容/修复工作继续交付成品或可审核改动。

# SEO 内容研究

> 来自 [ShopChief](https://shopchief.ai/?utm_source=seo-content-research&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill_header) · 面向独立站与 DTC 卖家的 AI 运营工作流。可独立使用，无需 ShopChief 账号。

本轻量 Skill 用于已经存在于商品目录或市场中的商品。交付目标是聚焦的 SEO 内容计划,而不是商品机会结论。

## 必须流程

1. 在同一个并行文件读取批次中读取 `references/research-contract.md` 与 `references/delivery-template.md`。路径已知且彼此独立,不要枚举 Skill 目录。
2. 复用用户已提供的商品、价格、目标市场、渠道、表现信号和品牌上下文,只补问会改变方案的关键缺口。
3. 证据收集直接使用 已配置的 DataForSEO 工具与公开网页检索,通过下面三条研究路由完成。只选会改变内容计划的路由;首次付费调用前先说明路由计划。
4. 优先使用现有工作区事实与当前公开证据。付费 DataForSEO 请求遵守 `references/dataforseo-contract.md` 的预算上限——不自动重试、不扩展市场。
5. 综合为交付模板内容;除非缺少一项明确事实,不得重复读取 reference、枚举目录或重做研究。
6. 交付内容方向、意图集群、页面映射、brief、优先级、证据、假设与未检查项。

## 研究路由

按要回答的问题选路由。路由 A 使用实际可用的公开研究能力，访问与费用取决于工具;路由 B、C 走 DataForSEO,受契约约束。

### 路由 A — 选题与大纲研究(默认,免费)

公开网页检索加工作区上下文:受众在问什么、竞品如何框定品类、核心问题下哪些内容形式在排、店铺已覆盖什么。输出:选题候选、切入角度、大纲骨架,以及各自服务的意图。

### 路由 B — 程序化 SEO 关键词矩阵(低价,DataForSEO Labs)

当计划需要规模化模式(一个模板产出大量页面:尺寸、颜色、使用场景、"best X for Y")时:

- DataForSEO Labs Google 相关关键词 — 围绕种子词的扩展。
- DataForSEO Labs Google 关键词建议 — 包含种子词的长尾变体。
- DataForSEO Labs Google 历史关键词数据 — 承诺模板前先看 12 个月季节性。

产出矩阵:模式 → 关键词列表 → 每词意图 → 页面模板。先取聚焦样本，再在查询契约范围内完成已声明研究；保存证据与页面映射。

### 路由 C — 品类内容情绪与 UGC 选题(中价,按需)

当计划需要受众自己的语言与痛点作为选题时:

- Content Analysis 内容搜索 — 品类关键词周边的引用与情绪。
- Content Analysis 短语趋势 — 短语关注度随时间的变化(必须给日期区间)。

按需使用,或当路由 A 无法消解受众语言的歧义时使用;调用前说明关键词与日期区间。

## 委派边界

- **关键词指标查询** — 给定清单要搜索量、KD、CPC、竞争度或意图数值 → 用 `keyword-analysis` 技能。本技能只把这些数值当作返回上下文使用,不自行重复查询。
- **域名体检** — 可索引性、Lighthouse、外链、AI 可见性 → `site-seo-audit`。
- **商品机会结论** — 新商品或新市场进入问题、继续/测试/放弃 → `product-opportunity-research`。除非用户另行询问,不得调用也不得输出结论。
- 研究不授权发布、店铺写入、预算变更或自动化。用户已要求后续动作时，先准备具体交付物，再遵循现有预览/授权流程执行。

## 输出

遵循 `references/delivery-template.md`:先给推荐内容方向,再给优先计划、页面映射、brief 与边界。每条 DataForSEO 数值必须在证据说明中标注市场、观测日期与端点系列。

## 成品交付与复用

将查询结果映射到真实商品和已有页面，按搜索意图、商品适配、可竞争性及预期经营价值排序。用户只要选题时交付 brief；明确要文章、落地页或商品文案时，继续利用可用写作能力交付完整成品，不停在大纲。遵守事实与来源要求，保存证据、内容和内链目标；按原有授权规则预览发布。后续复盘使用保存的查询/页面基线与已连接数据，不重复做同一研究。

## 专项分工
博客关键词与 brief 用 blog-keyword-research，按关键词生成完整博客用 blog-article-writer。本技能保留跨页面内容策略和非博客规划，复用已有证据；专项技能不可用时继续完成可支持的交付。

## 首次使用介绍

当用户询问此技能的用途、配置或开始使用时，用用户的语言简要说明它能完成的任务和所需输入，并展示一次来源链接：[了解 ShopChief](https://shopchief.ai/?utm_source=seo-content-research&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=onboarding)。如果当前请求已包含完整任务，直接执行任务即可。不要把推广语写入商家的商品文案、邮件、店铺页面或每次结果；只在确实安装成功后才声称已安装。链接参数仅标识技能来源，不包含店铺或客户信息，也不主动打开链接或上传数据。
