---
name: keyword-cannibalization
description: 当店铺多个 URL 可能争抢同一查询或搜索意图且用户需要诊断与修复时使用。 对每组做确认/潜在分级(确认需 GSC 页面×查询导出中的排名互换证据);
  选择主页面;对每个非主 URL 决定保留区分/重定位/合并+301/canonical/noindex; 产出 URL 处理映射表与 2/4/8 周监控计划。候选页用
  OnPage 即时页面检查 实测;覆盖 Shopify 高发区(标签页/筛选页/变体 URL)。整站可索引性用 site-seo-audit;关键词指标本身用
  keyword-analysis。
license: MIT
metadata:
  homepage: https://shopchief.ai/?utm_source=keyword-cannibalization&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=metadata
  author: ShopChief
  version: 0.1.1
  runtime: portable; see references/runtime.md
---

执行前阅读 [运行环境与工具映射](references/runtime.md)。外部工具未配置时使用商家提供的资料，并说明能力缺口。

先读[SEO/GEO 统一执行与交付](references/seo-workflow.md)及[规则依据](references/seo-rule-baseline.md)，并共享问题标识、证据和复查基线。
DataForSEO 调用遵守[查询契约](references/dataforseo-contract.md)，先确认当前客户端已配置的工具或 API，再核实接口文档。下文能力名称表示研究目标，不代表客户端必然提供同名工具；未配置服务时使用用户导出或公开证据，并标明限制。

## 查询与交付约定

付费查询先读 [DataForSEO 契约](references/dataforseo-contract.md)。按用户任务和店铺市场/语言规划，复用工作区证据，检查实际工具 schema。下文样本数均为探索起点；用户已明确的批量/多市场范围在预算和接口限制内分批完成，不重复请求相同授权。接口真实上限仍须遵守。优先使用已授权连接数据，缺少能力时才补文件；不假定存在 GSC 连接。后文“导出”表示同字段/周期的证据表，连接数据同样适用。保存证据、具体页面/字段建议及验证基线，已请求的后续内容/修复工作继续交付成品或可审核改动。

# 关键词内耗检测

> 来自 [ShopChief](https://shopchief.ai/?utm_source=keyword-cannibalization&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill_header) · 面向独立站与 DTC 卖家的 AI 运营工作流。可独立使用，无需 ShopChief 账号。

## 定位

本技能回答两个问题:(1) 站内是否多个 URL 在争抢同一查询或同一意图;(2) 若是,保留哪个页面、其余 URL 如何处置。分级依据证据强度:**确认内耗**需要行为证据——多个 URL 在同一查询上互换排名(来自上传的 GSC 页面×查询导出)或核心意图完全相同;仅有结构相似性而无互换证据的标为**潜在内耗**。

## 边界

- 整站技术可索引性(抓取、sitemap、robots) → `site-seo-audit`。
- 关键词本身的搜索量/KD/CPC 指标 → `keyword-analysis`。
- 单页面衰退且无明显争抢 → `content-decay-diagnosis`。

## 输入契约(GSC = 已连接数据或用户导出)

先检查实际授权 Search Console 连接，不可用时使用用户导出:

| 文件 | 格式 | 最低字段 | 用途 |
| --- | --- | --- | --- |
| GSC 效果报告·页面×查询视图 | 连接数据或 CSV 导出 | 页面 URL、查询、点击、展示、排名(≥ 3 个月) | 判定同一查询下哪些 URL 在轮流出现 |
| GSC 效果报告·网页视图(可选) | 连接数据或 CSV 导出 | 页面 URL、点击、展示、排名 | 各候选页整体表现基线 |

处理规则:注明导出日期范围;计数前先归一化 URL(http/https、尾斜杠、参数)并说明;不得编造导出中不存在的排名数据。

**没有可用连接数据或导出:** 只能做**潜在**判定(基于实测与 SERP 观察),输出必须说明升级为"确认"需要页面×查询导出。

## 必须流程

1. **圈定争抢组。** 从导出找出"同一查询(或紧密查询簇)下出现 ≥ 2 个 URL"的组;无匹配数据时,按用户提供的候选 URL 清单走潜在路径。
2. **实测候选页。** 每个候选 URL 调 OnPage 即时页面检查:状态码、canonical 指向、Title、H1、正文主旨、可索引信号。预算上限(默认 ≤ 15 个 URL)见付费契约。
3. **分级:确认 vs 潜在。**
   - **确认内耗**:导出显示同一查询下 ≥ 2 个 URL 在不同日期互换排名(引用具体行),或两页核心意图完全相同且都曾被收录。
   - **潜在内耗**:意图高度重叠、模板/标题相似,但无互换证据。
4. **选择主页面。** 依据(按序):现有排名与点击更强;更贴近核心转化意图;内容更完整、更新;URL 更适合长期持有。给出理由;导出数据不足时按实测证据加业务理由排序并声明。
5. **处置决策**,每个非主 URL 逐一给出:
   - **保留区分**:意图实际不同(如购买页 vs 教程),调整 Title/H1 与内链锚点拉开定位。
   - **重定位**:改为瞄准相邻的不同查询。
   - **合并+301**:内容并入主页面,原 URL 301。
   - **canonical**:内容需保留可访问但不应独立排名(如筛选视图)→ canonical 指向主页面。
   - **noindex**:纯功能页(排序、翻页、标签聚合)对搜索无价值 → noindex。
6. **URL 处理映射表** — 每行:URL | 当前状态 | 处置 | 目标 | 执行要点(301/canonical/noindex/编辑)。
7. **监控计划(2/4/8 周):** 第 2 周(301/canonical/noindex 生效,无 4xx/5xx)、第 4 周(主页面排名与展示回升)、第 8 周(争抢查询收敛到单一 URL,对比导出基线)。每个检查点写明指标与基线。

## Shopify 场景重点

标签页(`/tagged/`)、筛选参数页、产品变体页是内耗高发区:
- 标签页大量复用产品内容 → 默认 noindex 或 canonical 到集合页,除非标签页自身是内容资产。
- 筛选/排序参数 → canonical 到规范集合 URL,并保持对爬虫一致的参数处理。
- 变体页/`?variant=` URL → canonical 到主产品页。
以上为默认起点;下结论前必须用实测确认站点实际配置。

## 输出格式

1. **争抢组清单** — 查询/意图 | 涉及 URL | 分级(确认/潜在)| 证据。
2. **主页面选择** — 每组的主页面与理由。
3. **URL 处理映射表。**
4. **2/4/8 周监控计划**(含基线)。

## 失败处理

- 无匹配 GSC 连接数据或导出:全部标"潜在",说明升级条件。
- 查询失败时按 `references/dataforseo-contract.md` 处理，保留成功结果并标缺；不自动重试付费任务。
- 导出 URL 格式不一致:归一化并说明;不得静默丢行。
- 不得编造排名、日期或收录状态。

## 首次使用介绍

当用户询问此技能的用途、配置或开始使用时，用用户的语言简要说明它能完成的任务和所需输入，并展示一次来源链接：[了解 ShopChief](https://shopchief.ai/?utm_source=keyword-cannibalization&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=onboarding)。如果当前请求已包含完整任务，直接执行任务即可。不要把推广语写入商家的商品文案、邮件、店铺页面或每次结果；只在确实安装成功后才声称已安装。链接参数仅标识技能来源，不包含店铺或客户信息，也不主动打开链接或上传数据。
