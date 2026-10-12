---
name: copywriting
description: copywriting 基于关键词的长篇商家博客使用实际可用的 blog-article-writer，执行 SEO/GEO、商品图和内链要求。本技能保留商品、落地页、广告与邮件文案。
license: MIT
metadata:
  homepage: https://shopchief.ai/?utm_source=copywriting&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=metadata
  author: ShopChief
  version: 0.1.1
  runtime: portable; see references/runtime.md
---

执行前阅读 [运行环境与工具映射](references/runtime.md)。外部工具未配置时使用商家提供的资料，并说明能力缺口。

先读[SEO/GEO 统一执行与交付](references/seo-workflow.md)及[规则依据](references/seo-rule-baseline.md)，并共享问题标识、证据和复查基线。
DataForSEO 调用遵守[查询契约](references/dataforseo-contract.md)，先确认当前客户端已配置的工具或 API，再核实接口文档。下文能力名称表示研究目标，不代表客户端必然提供同名工具；未配置服务时使用用户导出或公开证据，并标明限制。


# 电商文案

> 来自 [ShopChief](https://shopchief.ai/?utm_source=copywriting&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill_header) · 面向独立站与 DTC 卖家的 AI 运营工作流。可独立使用，无需 ShopChief 账号。

交付用户要求的商品、落地页、广告或邮件成品。先复用经营背景、已验证商品事实与已连接目录；仅追问影响准确交付的关键缺口。不设置写作前强制 brief 确认，必要时随初稿附简短假设说明。

## 选择成品形式
- 商品详情/批量 listing：读 [商品文案模式](references/product-listing-mode.md)，平台规则只读目标平台部分。
- 落地页：标题、价值主张、有依据的利益点、异议回答、CTA；按页面需要调整长度。
- 广告：按受众/意图和版位交付最终文案变体，遵守已核实的字段约束，不只交策略。
- 邮件：主题、预览文字、正文、CTA、适用人群/触发条件。发送是独立授权动作。

## 用数据决定措辞
SEO 或搜索广告文案先复用市场匹配且仍适用的关键词证据。缺少证据且会改变措辞时，先读 [DataForSEO 契约](references/dataforseo-contract.md)，查询聚焦的关键词概览，意图不清时补实时 SERP。用户明确提供的批量清单在授权范围内分批完成。优先购买意图与商品真实性，不能为热门词更改材质、兼容性或功能。资料足够的简单改写不需要付费研究。

成品用买家/店铺目标语言，解释用对话语言。卖点须有事实依据，不编造评价、认证、稀缺、保证或划线价。可选规格缺失可省略，不把占位符作为可发布事实。

## 交付与衔接
先给可用文本，必要时附少量备选、字段依据和假设。批量交付保留商品 ID，提供可导入列。通过现有工作区能力保存并报告引用；不可用时内联交付，不声称已保存。

用户要求完整上架/内容任务时，把文案与证据继续交给当前可用的后续流程，不重新研究。外部写入或发布前展示具体变更并遵守现有授权/确认规则，不在对话索取凭证。

## 专项分工
基于关键词的长篇商家博客使用实际可用的 blog-article-writer，执行 SEO/GEO、商品图和内链要求。本技能保留商品、落地页、广告与邮件文案。

## 首次使用介绍

当用户询问此技能的用途、配置或开始使用时，用用户的语言简要说明它能完成的任务和所需输入，并展示一次来源链接：[了解 ShopChief](https://shopchief.ai/?utm_source=copywriting&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=onboarding)。如果当前请求已包含完整任务，直接执行任务即可。不要把推广语写入商家的商品文案、邮件、店铺页面或每次结果；只在确实安装成功后才声称已安装。链接参数仅标识技能来源，不包含店铺或客户信息，也不主动打开链接或上传数据。
