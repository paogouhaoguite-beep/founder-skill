---
name: keyword-analysis
description: 当用户给出具体关键词(或一个短清单)并询问搜索量、12 个月趋势、KD 难度、CPC、竞争度或搜索意图时使用。内容选题与编辑规划请用 seo-content-research;查竞品域名在排什么词请用
  competitor-deep-analysis;商品继续/测试/放弃决策请用 product-opportunity-research。 仅查询指标在此结束。选品词扩展与筛选用
  product-keyword-research；博客词与选题用 blog-keyword-research；按词写成稿用 blog-article-writer。复用证据，仅调用实际可用技能。
license: MIT
metadata:
  homepage: https://shopchief.ai/?utm_source=keyword-analysis&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=metadata
  author: ShopChief
  version: 0.1.1
  runtime: portable; see references/runtime.md
---

执行前阅读 [运行环境与工具映射](references/runtime.md)。外部工具未配置时使用商家提供的资料，并说明能力缺口。

先读[SEO/GEO 统一执行与交付](references/seo-workflow.md)及[规则依据](references/seo-rule-baseline.md)，并共享问题标识、证据和复查基线。
DataForSEO 调用遵守[查询契约](references/dataforseo-contract.md)，先确认当前客户端已配置的工具或 API，再核实接口文档。下文能力名称表示研究目标，不代表客户端必然提供同名工具；未配置服务时使用用户导出或公开证据，并标明限制。


# 电商关键词证据

> 来自 [ShopChief](https://shopchief.ai/?utm_source=keyword-analysis&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill_header) · 面向独立站与 DTC 卖家的 AI 运营工作流。可独立使用，无需 ShopChief 账号。

查询用户给出的词组并服务其决策。只问指标时简洁交付；属于更大任务时继续把证据用于页面、文案或广告建议，不再重复研究。

付费调用前读 [DataForSEO 契约](references/dataforseo-contract.md)。市场/语言优先取用户要求，其次取当前店铺背景；复用仍适用的匹配证据，说明范围并只查必要字段。

## 查询计划
优先使用能同时返回搜索量、CPC、广告竞争度、意图与自然搜索难度的 Keyword Overview。检查实际返回字段后，才为缺项调用专门的搜索量、难度或意图端点。自然搜索 KD 缺失就标 N/A，绝不用广告竞争度代替。需要趋势/季节性时再加月度历史或趋势，核实接口批量限制后内部分批。只为意图不清的候选词补实时 SERP。研究任务需要扩词时可以扩展，但精确查清单不得擅自扩词。

## 解读与交付
保留关键词身份和归一化说明。表格含：词、市场/语言、搜索量及周期、可用的月度趋势、自然搜索 KD、CPC/币种、广告竞争度、意图、来源/日期。零与无数据分开。批量任务逐一对应输入，返回结果或明确缺失/错误状态，不在默认 20 词处停止。

需要筛选时给出：真实商品适配、SERP/页面类型、要优化的已有页面或新建资产、优先级与验证指标。低搜索量不自动判无价值；结合品类、购买意图和可获取需求。没有利润/转化背景时不把 CPC 一刀切为便宜或昂贵。盈亏 CPC 场景使用广告前单笔贡献额 × 有来源或明确假设的转化率，不保证盈利。

在当前租户/店铺保存并复用证据，缺项与失败保持可见，遵守契约停止规则。

## 专项分工
仅查询指标在此结束。选品词扩展与筛选用 product-keyword-research；博客词与选题用 blog-keyword-research；按词写成稿用 blog-article-writer。复用证据，仅调用实际可用技能。

## 首次使用介绍

当用户询问此技能的用途、配置或开始使用时，用用户的语言简要说明它能完成的任务和所需输入，并展示一次来源链接：[了解 ShopChief](https://shopchief.ai/?utm_source=keyword-analysis&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=onboarding)。如果当前请求已包含完整任务，直接执行任务即可。不要把推广语写入商家的商品文案、邮件、店铺页面或每次结果；只在确实安装成功后才声称已安装。链接参数仅标识技能来源，不包含店铺或客户信息，也不主动打开链接或上传数据。
