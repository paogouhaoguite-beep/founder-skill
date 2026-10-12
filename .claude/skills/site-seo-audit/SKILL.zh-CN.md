---
name: site-seo-audit
description: 全站搜索体检、重点页面与内容方向统筹、搜索竞品差距、单次 AI 提及、外链与品牌事实检查，以及优化后的正常复查。仅诊断不写店铺，请求优化则继续授权范围内的可审阅修改。专项复用现有技能，带回同一成果与基线；下降诊断交
  content-decay-diagnosis。
license: MIT
metadata:
  homepage: https://shopchief.ai/?utm_source=site-seo-audit&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=metadata
  author: ShopChief
  version: 0.1.1
  runtime: portable; see references/runtime.md
---

执行前阅读 [运行环境与工具映射](references/runtime.md)。外部工具未配置时使用商家提供的资料，并说明能力缺口。

# 店铺搜索体检、优化与复查

> 来自 [ShopChief](https://shopchief.ai/?utm_source=site-seo-audit&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill_header) · 面向独立站与 DTC 卖家的 AI 运营工作流。可独立使用，无需 ShopChief 账号。

先读[统一流程](references/seo-workflow.md)、[规则依据](references/seo-rule-baseline.md)及 [DataForSEO 契约](references/dataforseo-contract.md)。本技能负责五维统筹和正常复查，专项复用现有技能，不新增运行时。

## 范围与意图
从当前店铺和已有上下文确定域名、目标页面、市场/语言与目标。全站任务初查五维；技术、AI、外链专项请求只查对应方向和必要前提。列出首页、集合、商品/变体/库存状态、博客、政策/支持页等类型，分别记录请求、发现、已抓取和跳过的页面。抽样不能称为抓完整站点。只诊断不写店铺；请求优化则继续成品、可审阅修改和授权范围执行，并分别核验后台字段与前台渲染。

## 五维与三阶段责任

| 维度 | 初查与基础修复 | 专项优化 | 统一复查 |
| --- | --- | --- | --- |
| 技术可访问性与索引 | HTTP、robots、canonical、sitemap、渲染；公开可索引性不等于 GSC 实际索引 | crawl-index-audit、cwv-performance-audit、international-seo-audit；迁站才用 site-migration-seo | 原问题技术验证、真实索引证据；实验室与现场性能分列 |
| 搜索需求与内容策略 | 现有页面、用户问题、意图和覆盖 | seo-content-research 负责主题聚类及新内容内链规划；keyword-analysis、blog-keyword-research；确有规模需求用 programmatic-seo-planner | 同页面/查询/市场的可比周期基线 |
| 页面表达与事实依据 | 商品与品牌事实、标题正文、真实结构化标记 | product-page-seo、collection-page-seo、blog-article-writer、schema-markup-designer；其他文案用 copywriting | 后台回读、前台渲染、事实准确性及可用页面表现 |
| 网站结构与内部链接 | 导航、可发现性、现有内链、样本内孤岛候选 | internal-link-audit、keyword-cannibalization；新主题链接交 seo-content-research | 指定来源/目标链接、覆盖和未结问题 |
| 站外信誉与品牌信息 | 外链、真实品牌档案、引用来源、事实冲突 | 本技能负责外链差距和具体品牌来源修正；另有商业情报请求才交 competitor-deep-analysis | 指定来源回查、可比外链及固定 AI 样本 |

各专项共享一个问题清单：稳定 ID、维度、SEO/GEO 影响、页面、证据、优先级及理由、修复动作和验收方式。共性问题合并，不编造综合评分。依据实际访问障碍、事实错误、关键页面影响和可执行性排序。

## 可独立执行的技术路线
先用公开 HTML/DOM 与已有授权报告；按准确文档用 OnPage 页面检查补元数据/状态，内容解析补正文/链接。真实 JSON-LD/microdata 必须实际提取，普通解析缺字段不等于无标记。Lighthouse 是实验室证据，INP/真实体验须对应现场/交互数据。缺失标未验证，保留成功结果，不重复付费重试。

## 可独立执行的 AI 提及路线
预先固定平台、市场、语言、品牌及别名、问题集、时间。供应商提及库、真实搜索界面采样、普通 LLM API 回答三者分别记录。LLM Mentions、ChatGPT Scraper、AI 搜索需求是待查能力提示，非可调用工具名；先查当前准确文档、权限、费用和完成状态。每个问题记录品牌出现、被引 URL、原证据片段及事实正确/错误/未知，给出分母和样本限制。单次样本不代表普遍曝光、排名、未来引用或持续监测。无能力时完成已有来源和品牌事实检查，AI 观察标未验证。

## 可独立执行的外链与竞品路线
外链概览、引用域及交集须同日期与域名口径，区分未知、空和真实零。供应商 spam/rank 指标不能直接认定处罚或自动拒绝外链。搜索竞品与商业竞品分开；仅比较排名、内容、外链及引用差距。品牌改进清单具体到来源 URL、错误/缺失事实、拟修正内容、负责人/渠道和验收方式。准备原创资料与真实品牌信息修正；外联、买外链、发布依实际授权，不自动发生。

## 交付与复查
交付摘要、五维覆盖、统一问题/修复清单、已执行及回读结果、缺失证据和已保存基线。有必要的报告保存完整 HTML，使用真实稳定文件身份在对话交付。通过当前任务后续入口携带实际 artifact 与问题 ID，按[复查流程](references/review-procedure.md)分列技术、SEO、AI 与经营结果。只有存在下降证据才进入 content-decay-diagnosis；适用证据继续复用。

## 首次使用介绍

当用户询问此技能的用途、配置或开始使用时，用用户的语言简要说明它能完成的任务和所需输入，并展示一次来源链接：[了解 ShopChief](https://shopchief.ai/?utm_source=site-seo-audit&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=onboarding)。如果当前请求已包含完整任务，直接执行任务即可。不要把推广语写入商家的商品文案、邮件、店铺页面或每次结果；只在确实安装成功后才声称已安装。链接参数仅标识技能来源，不包含店铺或客户信息，也不主动打开链接或上传数据。
