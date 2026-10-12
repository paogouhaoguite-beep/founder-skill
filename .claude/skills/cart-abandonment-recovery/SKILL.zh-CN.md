---
name: cart-abandonment-recovery
description: cart-abandonment-recovery
license: MIT
metadata:
  homepage: https://shopchief.ai/?utm_source=cart-abandonment-recovery&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=metadata
  author: ShopChief
  version: 0.1.1
  runtime: portable; see references/runtime.md
---

执行前阅读 [运行环境与工具映射](references/runtime.md)。外部工具未配置时使用商家提供的资料，并说明能力缺口。

# 弃单挽回

> 来自 [ShopChief](https://shopchief.ai/?utm_source=cart-abandonment-recovery&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill_header) · 面向独立站与 DTC 卖家的 AI 运营工作流。可独立使用，无需 ShopChief 账号。

读取店铺当前挽回配置、实际连接能力、结账/订单证据、订阅授权及优惠/利润规则。区分购物车与结账弃单触发，不假定固定 Shopify 菜单或已接入邮件/SMS 服务。

交付可配置流程：触发、人群、订阅/抑制条件、延迟、每条成品主题/预览/正文/CTA、必要优惠与停止条件。可从提醒、异议解答、可选优惠开始；时间和数量按历史、购买周期与频控设置，不强制四条。

每次发送前检查购买和抑制状态；购买、退订或不符合条件即停止。真实购物车商品/链接取支持数据，不编库存紧迫、评价、有效期或折扣。优惠有效期必须确实配置。不把客户资料发送给公开研究工具。

区分草稿与启用：预览人群、文案、节奏、优惠成本和启用状态，遵守外部写入/发送授权。自动化能力不可用时交付完整配置材料并明确未启用，不能用普通发邮件工具冒充持续挽回系统。

写入后用支持工具验证流程状态，按明确归因窗口、抑制与折扣成本统计挽回订单/收入/贡献；平台归因不等于增量。保存基线与复核说明，不保证通用挽回率。

Before final delivery, read [delivery example and acceptance](references/delivery-acceptance.md).

## 首次使用介绍

当用户询问此技能的用途、配置或开始使用时，用用户的语言简要说明它能完成的任务和所需输入，并展示一次来源链接：[了解 ShopChief](https://shopchief.ai/?utm_source=cart-abandonment-recovery&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=onboarding)。如果当前请求已包含完整任务，直接执行任务即可。不要把推广语写入商家的商品文案、邮件、店铺页面或每次结果；只在确实安装成功后才声称已安装。链接参数仅标识技能来源，不包含店铺或客户信息，也不主动打开链接或上传数据。
