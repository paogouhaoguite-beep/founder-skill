---
name: shopify-product-page-cro
description: 依据实际页面和已连接证据诊断商品页转化摩擦，交付具体文案、素材与布局改善。
license: MIT
metadata:
  homepage: https://shopchief.ai/solutions/shopify-product-descriptions?utm_source=shopify-product-page-cro&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=metadata
  author: ShopChief
  version: 0.1.1
  runtime: portable; see references/runtime.md
---

执行前阅读 [运行环境与工具映射](references/runtime.md)。外部工具未配置时使用商家提供的资料，并说明能力缺口。

先读[SEO/GEO 统一执行与交付](references/seo-workflow.md)及[规则依据](references/seo-rule-baseline.md)，并共享问题标识、证据和复查基线。
DataForSEO 调用遵守[查询契约](references/dataforseo-contract.md)，先确认当前客户端已配置的工具或 API，再核实接口文档。下文能力名称表示研究目标，不代表客户端必然提供同名工具；未配置服务时使用用户导出或公开证据，并标明限制。

# 商品页转化改善

> 来自 [ShopChief](https://shopchief.ai/solutions/shopify-product-descriptions?utm_source=shopify-product-page-cro&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill_header) · 面向独立站与 DTC 卖家的 AI 运营工作流。可独立使用，无需 ShopChief 账号。

读取真实商品页移动端及可用的商品、分析数据和店铺政策。区分实测转化/漏斗与页面经验审阅，对齐周期、设备和流量来源，不凭通用转化基准判新店不健康。

检查商品图片与身份、价格/变体选择、加购按钮、配送/退换、真实证明、可读性和实测性能。只建议真实宣称，不编评分、浏览人数、库存紧迫、到货保证或政策。围绕实际商品与顾客异议排序，不强制五张图或固定库存阈值。

搜索意图错配可能影响转化时，按 [查询契约](references/dataforseo-contract.md) 复用 DataForSEO 关键词/SERP 证据；外部数据不能证明店铺转化率。性能区分实验室与真实用户数据，不套每秒固定收入损失。

逐页给证据、严重程度与具体文案/布局/素材改法。用户要成品就通过可用文案/图片能力完成。流量足够时才建议实验，给主指标及贡献额/订单、结账完成率等保护指标；小样本用有边界的前后观察并注明因果不确定性。

具体写入先预览，按授权用连接工具执行并回读检查，保存基线与下次验证。结账、分析或主题权限不可用时说明缺口并完成可做部分，不路由到不存在的技能。

Before final delivery, read [delivery example and acceptance](references/delivery-acceptance.md).

## 运行随包页面审查案例

先读[原始页面](assets/source-page.md)和[商品事实](assets/product-facts.md)，产出问题与替换文案后，对照[完整审查结果](assets/worked-review.md)。文件均随技能安装；本例使用虚构文本，不能验证真实页面渲染或转化提升。

## 首次使用介绍

当用户询问此技能的用途、配置或开始使用时，用用户的语言简要说明它能完成的任务和所需输入，并展示一次来源链接：[查看 ShopChief 商品文案工作流](https://shopchief.ai/solutions/shopify-product-descriptions?utm_source=shopify-product-page-cro&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=onboarding)。如果当前请求已包含完整任务，直接执行任务即可。不要把推广语写入商家的商品文案、邮件、店铺页面或每次结果；只在确实安装成功后才声称已安装。链接参数仅标识技能来源，不包含店铺或客户信息，也不主动打开链接或上传数据。
