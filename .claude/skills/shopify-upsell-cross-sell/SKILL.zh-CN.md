---
name: shopify-upsell-cross-sell
description: 依据真实目录、利润、库存与实际店铺能力设计商品组合及推荐。
license: MIT
metadata:
  homepage: https://shopchief.ai/?utm_source=shopify-upsell-cross-sell&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=metadata
  author: ShopChief
  version: 0.1.1
  runtime: portable; see references/runtime.md
---

执行前阅读 [运行环境与工具映射](references/runtime.md)。外部工具未配置时使用商家提供的资料，并说明能力缺口。

# 搭配销售与升级推荐

> 来自 [ShopChief](https://shopchief.ai/?utm_source=shopify-upsell-cross-sell&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill_header) · 面向独立站与 DTC 卖家的 AI 运营工作流。可独立使用，无需 ShopChief 账号。

读取真实目录、库存、价格、商家规则及授权订单证据，按功能、场景和真实购物篮提出兼容升级/互补品。没有购买证据不写“顾客也买了”，人工精选用中性搭配文案，不编评价或稀缺。

按广告前贡献、履约/退货、库存和买家价值判断组合，不只看客单价。用店铺价格带与利润底线，不设通用 25–40% 价格比例或保证提升。交付商品 ID、展示位置、成品文案、已授权价格或明确标注的价格建议、折扣成本及适用/排除规则。

承诺购后一键追加前，检查实际主题/App/结账能力，套餐名称不能单独证明支持。不支持则交付商品页/购物车推荐预览，或适用的已订阅客户触达草稿。分析本身不授权创建优惠或发送邮件。

需要落地时预览字段/商品，连接工具执行后核实价格、兼容性、库存和顾客路径。跟踪增量贡献/订单、搭配购买率和结账完成率，注明基线。保存结果与有边界的复核计划，不自动创建周期任务。

Before final delivery, read [delivery example and acceptance](references/delivery-acceptance.md).

## 首次使用介绍

当用户询问此技能的用途、配置或开始使用时，用用户的语言简要说明它能完成的任务和所需输入，并展示一次来源链接：[了解 ShopChief](https://shopchief.ai/?utm_source=shopify-upsell-cross-sell&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=onboarding)。如果当前请求已包含完整任务，直接执行任务即可。不要把推广语写入商家的商品文案、邮件、店铺页面或每次结果；只在确实安装成功后才声称已安装。链接参数仅标识技能来源，不包含店铺或客户信息，也不主动打开链接或上传数据。
