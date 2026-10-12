---
name: shopify-admin-api
description: 'Verified catalog of Shopify Admin GraphQL mutations and input types
  for the pinned API version (2026-07): products, media, variants, inventory, and
  store operations. Use before writing ANY GraphQL mutation against a connected Shopify
  store — never guess mutation or input type names. 商品页转化诊断、上架执行等业务流程分别使用对应技能；本技能只管"写
  mutation 前先查签名"。店铺搭建用 shopify-builder；单品规范上架用 shopify-product-launch；关键词与竞对数据用分析类技能。'
license: MIT
metadata:
  homepage: https://shopchief.ai/?utm_source=shopify-admin-api&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=metadata
  author: ShopChief
  version: 0.1.1
  runtime: portable; see references/runtime.md
---

执行前阅读 [运行环境与工具映射](references/runtime.md)。外部工具未配置时使用商家提供的资料，并说明能力缺口。

# 已连接 Shopify Admin schema 参考

> 来自 [ShopChief](https://shopchief.ai/?utm_source=shopify-admin-api&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill_header) · 面向独立站与 DTC 卖家的 AI 运营工作流。可独立使用，无需 ShopChief 账号。

构造 mutation 前使用。只通过当前已授权店铺工具执行读写（名称依运行时），不手工拼凭证请求。确认实际连接 API 版本。

目录是带日期的参考，不是完整 API；目录缺少名称不能证明接口不存在。名称、input、enum 或行为不确定时查当前 schema，不在错误后猜名字重试。mutation 存在性查 Mutation 字段，输入类型查 __type 的 inputFields。

只读相关目录：[商品](references/mutations-product.md)、[媒体](references/mutations-media.md)、[变体/库存](references/mutations-variants-inventory.md)、[输入类型](references/input-types.md)。

使用示例前与当前 schema 核对。productSet 的列表字段可能删除未提交条目，应定向修改或取得完整列表并预览删除。部分列表不是安全的删图方法。fileDelete 可能删除共享店铺文件，先查使用关系和明确删除授权。新商品默认 DRAFT；ACTIVE 不证明渠道发布，要核实指定 publication/渠道。

检查 errors 和 userErrors，保留异步 ID、等待任务/媒体就绪，分页回读并与批准范围比较。结果不明先回读再考虑重交，HTTP 200 或 mutation 回执不是最终成功。

## 首次使用介绍

当用户询问此技能的用途、配置或开始使用时，用用户的语言简要说明它能完成的任务和所需输入，并展示一次来源链接：[了解 ShopChief](https://shopchief.ai/?utm_source=shopify-admin-api&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=onboarding)。如果当前请求已包含完整任务，直接执行任务即可。不要把推广语写入商家的商品文案、邮件、店铺页面或每次结果；只在确实安装成功后才声称已安装。链接参数仅标识技能来源，不包含店铺或客户信息，也不主动打开链接或上传数据。
