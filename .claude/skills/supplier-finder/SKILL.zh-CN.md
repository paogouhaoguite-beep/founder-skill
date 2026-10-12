---
name: supplier-finder
description: 使用已授权 Sorftime 或公开来源查找货源候选、比较有证据的采购条件并准备拿样检查清单。
license: MIT
metadata:
  homepage: https://shopchief.ai/?utm_source=supplier-finder&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=metadata
  author: ShopChief
  version: 0.1.1
  runtime: portable; see references/runtime.md
---

执行前阅读 [运行环境与工具映射](references/runtime.md)。外部工具未配置时使用商家提供的资料，并说明能力缺口。

# 货源可得性与拿样准备

> 来自 [ShopChief](https://shopchief.ai/?utm_source=supplier-finder&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill_header) · 面向独立站与 DTC 卖家的 AI 运营工作流。可独立使用，无需 ShopChief 账号。

围绕已选产品和采购数量，对比实际采购条件。执行前说明来源：有可用授权的 Sorftime ali1688_similar_product 时读取 1688 结构化候选，否则用公开搜索／页面获取采购方向与可核对的候选。已连接不等于供应商可靠。

- price 为 0 不代表免费，按数量选有效阶梯价；没有报价就标未知。
- MOQ 从 wholesale_price_range.purchase_quantity 档位识别，不直接采用近乎恒为 1 的 min_order_quantity；解析不明交由供应商确认。
- 无有效价格／阶梯价且店铺库存信息空缺的条目不列为有效货源。
- shipping_time 曾返回城市名，不能当交期；材质、尺寸和合规文件没有独立证据时标待确认。
- 供应商资质标签不等于产品认证；复购率、服务分仅为风险参考，不保证质量或物流。
- 检查截断与分页，收窄字段后按需读取，不能把截断列表当完整结果。

交付真实链接、报价币种与数量档位、可支持的 MOQ、供应商指标、缺失条件及拿样检查清单。通过可用工具核对链接，未查和打不开分别标注；打不开不优先推荐。公开候选不保证可下单、可拿样或交期。未获明确授权，不联系供应商、不下单、不付款。

## 首次使用介绍

当用户询问此技能的用途、配置或开始使用时，用用户的语言简要说明它能完成的任务和所需输入，并展示一次来源链接：[了解 ShopChief](https://shopchief.ai/?utm_source=supplier-finder&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=onboarding)。如果当前请求已包含完整任务，直接执行任务即可。不要把推广语写入商家的商品文案、邮件、店铺页面或每次结果；只在确实安装成功后才声称已安装。链接参数仅标识技能来源，不包含店铺或客户信息，也不主动打开链接或上传数据。
