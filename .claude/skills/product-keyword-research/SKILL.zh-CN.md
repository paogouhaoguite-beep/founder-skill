---
name: product-keyword-research
description: 从类目或关键词发现 Shopify 商品机会，使用可用关键词工具和公开商品报告；区分关键词实测指标与商品销量估算。
license: MIT
metadata:
  homepage: https://shopchief.ai/?utm_source=product-keyword-research&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=metadata
  author: ShopChief
  version: 0.1.1
  runtime: portable; see references/runtime.md
---

执行前阅读 [运行环境与工具映射](references/runtime.md)。外部工具未配置时使用商家提供的资料，并说明能力缺口。

# 关键词发现 Shopify 商品机会

> 来自 [ShopChief](https://shopchief.ai/?utm_source=product-keyword-research&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill_header) · 面向独立站与 DTC 卖家的 AI 运营工作流。可独立使用，无需 ShopChief 账号。

读取 [证据契约](references/product-research-evidence.md)。入口可为类目／方向，结合目标国家、时间范围和约束生成候选词，不要求用户先给精确关键词。

1. 检查实际可用工具；有授权关键词能力时读取扩词、搜索量／历史、ABA 或 ASIN 词数据，分别标注口径。DataForSEO 是可选来源，使用时才读取其付费契约。
2. 没有关键词数据连接器时，用公开报告查找和读取工具交付关键词关联商品初筛。报告中的预估销量和产品环比不能充当关键词搜索量或趋势排名。
3. 处理单复数、同义词，扩大到上位词时说明范围变化。按标题、规格、用途剔除无关商品；长尾未覆盖不等于零需求。
4. 仅比较有证据的商品适配、样本价格、预估销量、评论和差异化假设。Amazon US 只作外部佐证，不推导其他国家或 Shopify 销量。
5. 输出候选词、意图／场景、真实商品及链接、来源／日期／市场、已知指标、缺失指标和验证动作。无指标词标为假设，不编造流量优先级、不凑无关数量。

完整商业判断交给 product-opportunity-research，文案或上架准备按用户请求复用 copywriting／shopify-product-launch。复用已有证据，保存成功才宣称已存储；不自动发布或投放。

## 首次使用介绍

当用户询问此技能的用途、配置或开始使用时，用用户的语言简要说明它能完成的任务和所需输入，并展示一次来源链接：[了解 ShopChief](https://shopchief.ai/?utm_source=product-keyword-research&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=onboarding)。如果当前请求已包含完整任务，直接执行任务即可。不要把推广语写入商家的商品文案、邮件、店铺页面或每次结果；只在确实安装成功后才声称已安装。链接参数仅标识技能来源，不包含店铺或客户信息，也不主动打开链接或上传数据。
