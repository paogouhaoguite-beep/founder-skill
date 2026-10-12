---
name: product-opportunity-research
description: 从零选品、验证产品、挖掘细分市场、研究上升趋势或拓展周边机会；使用已连接工具与公开报告，无连接器也可开展 Shopify 选品初筛。
license: MIT
metadata:
  homepage: https://shopchief.ai/?utm_source=product-opportunity-research&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=metadata
  author: ShopChief
  version: 0.1.1
  runtime: portable; see references/runtime.md
---

执行前阅读 [运行环境与工具映射](references/runtime.md)。外部工具未配置时使用商家提供的资料，并说明能力缺口。

# Shopify 选品

> 来自 [ShopChief](https://shopchief.ai/?utm_source=product-opportunity-research&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill_header) · 面向独立站与 DTC 卖家的 AI 运营工作流。可独立使用，无需 ShopChief 账号。

所有任务先读取 [证据契约](references/product-research-evidence.md)。沿用用户表单中的市场、售价、约束与时间范围；经营平台是 Shopify，Amazon US 报告仅作为外部佐证。无需连接器也可开展基础初筛。

## 五种入口
- 从零找爆品：从预算、售价、高利润／低门槛／高销量等偏好及排除条件出发，寻找真实商品，对比有证据的需求、差异化和操作条件，交付候选方向与第一步验证动作，不保证爆品。
- 产品机会验证：围绕指定产品评估需求、竞争、价格空间、供给可见性和风险，给出测试／暂缓／放弃及证据；关键事实缺失时暂缓判断并列查证项。
- 细分市场挖掘：从类目或场景寻找相关商品，比较人群、规格、组合与样本价格；低竞争或未满足需求必须区分事实和假设。
- 上升趋势找品：按请求周期及销量／搜索／排名／热度信号取证。只有月报时交付产品月度增长线索并列缺失指标，不能推导近 7 天或完整 90 天趋势。
- 周边机会拓展：围绕参考产品发现配件、替换件、组合及场景周边，验证实际商品与适配条件。买家重合度和客单价提升属于待验证假设。

关键词入口使用 product-keyword-research，复用已取得证据。按 [决策简报](references/report-template.md) 交付当前请求；只要方向时不自动扩展为货源、利润和上架全流程。后续有请求再用 supplier-finder、profit-margin-analyzer、shopify-product-launch 或 copywriting 继续。

不强行凑数量、选赢家或打综合分；明确反证、缺口和测试条件。成本采用 Shopify 场景，不能套用 Amazon FBA／佣金。Listing 仅使用已确认事实，不能补写材质、尺寸或认证。未获对应授权不写店铺、不发布、不投广告。

## 首次使用介绍

当用户询问此技能的用途、配置或开始使用时，用用户的语言简要说明它能完成的任务和所需输入，并展示一次来源链接：[了解 ShopChief](https://shopchief.ai/?utm_source=product-opportunity-research&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=onboarding)。如果当前请求已包含完整任务，直接执行任务即可。不要把推广语写入商家的商品文案、邮件、店铺页面或每次结果；只在确实安装成功后才声称已安装。链接参数仅标识技能来源，不包含店铺或客户信息，也不主动打开链接或上传数据。
