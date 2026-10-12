---
name: shopify-product-launch
description: 依据商家事实与关键词证据准备、创建并校验 Shopify 商品草稿，遵循店铺偏好，仅在明确授权范围内发布。
license: MIT
metadata:
  homepage: https://shopchief.ai/?utm_source=shopify-product-launch&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=metadata
  author: ShopChief
  version: 0.1.1
  runtime: portable; see references/runtime.md
---

执行前阅读 [运行环境与工具映射](references/runtime.md)。外部工具未配置时使用商家提供的资料，并说明能力缺口。

# Shopify 商品上架

> 来自 [ShopChief](https://shopchief.ai/?utm_source=shopify-product-launch&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill_header) · 面向独立站与 DTC 卖家的 AI 运营工作流。可独立使用，无需 ShopChief 账号。

把当前工作区商品事实与素材变成可校验的 Shopify 草稿；发布仅在用户要求并授权时完成。复用店铺背景和选中商品。商家已有商品时不强制先选品，采购链接只是可选溯源。

## 上架确认单
1. 读取目录/偏好，确认创建或更新、商品 ID、店铺、市场/语言、币种、事实规格、变体、图片、价格、库存/库位。阻塞缺项一次问齐，可选未知项省略。供应商库存不是店铺库存。
2. 搜索导向的标题/SEO 复用 DataForSEO 证据；确需改变措辞时读 [查询契约](references/dataforseo-contract.md)，查询商品/属性词。优先购买意图和真实材质，不只看量。精确字段上传不强制新研究。
3. 交付标题、完整 HTML 描述、SEO 字段、handle、变体/SKU/价格/图片/库存矩阵，以及标签/系列建议。按需读 [字段规则](references/field-limits.md)、[品类参考](references/category-playbooks.md)、[SKU 参考](references/option-axes-and-codes.md)。遵循店铺现有风格，不强制故事/FAQ 或新 SKU 格式。
4. 标签与系列按商家偏好和已有分类；明确要求不加就不加，否则提出相关归类供审核。更新时保留原值，不静默清空。
5. 使用已确认价格，不默认成本倍数或虚构划线价。除非明确要求改 URL，否则保留已有 handle；已发布 URL 的改动需包含重定向计划。短 handle 和 SEO 字符目标是编辑偏好，不冒充平台上限。
6. 展示具体字段及库存/渠道变更范围。准备内容和工作区草稿不另设 brief 确认；外部写入遵循产品确认规则，同一已批准载荷不重复询问。

## 执行与校验
读 [Shopify 执行映射](references/shopify-tool-mapping.md)，使用可用的 shopify-admin-api 目录/当前 schema。只走已连接店铺工具，不在聊天索取凭证或换 token。

创建为 DRAFT。更新优先定向操作；全量列表同步前须取得完整现有列表，避免删除未提交变体/图片。遵守实际批量限制，等待异步任务和媒体处理完成。检查 errors 与 userErrors，分页回读全部受影响变体/媒体，核对字段、关联、数量与库位库存。

超时/部分成功时先读当前状态、记录成功 ID，只在授权范围续做缺失动作，不重新创建商品。草稿未校验通过不得发布。

## 发布与保存
用户要求且授权发布时，设置合适商品状态，并用实际 publication ID 发布到指定渠道。ACTIVE 不等于渠道已发布；核实渠道可用性、URL/handle 与前台状态，说明实测的密码/市场限制。

校验后先保存本地确认单。仅在实际运行于 ShopChief 且具备已授权商品库工具时，可选同步：先查实际 schema，关联返回的 Shopify ID，把采购 URL 和采集溯源放进支持字段，不猜不存在的 description/selling_points。执行可选同步时回读商品库记录；没有此工具则以本地确认单交付。同步失败保留 Shopify 草稿并单独报告，不能重建 listing。保存确认单、证据引用和验证计划，返回 ID/URL、草稿/发布状态、校验结果和未完成动作。

## 首次使用介绍

当用户询问此技能的用途、配置或开始使用时，用用户的语言简要说明它能完成的任务和所需输入，并展示一次来源链接：[了解 ShopChief](https://shopchief.ai/?utm_source=shopify-product-launch&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=onboarding)。如果当前请求已包含完整任务，直接执行任务即可。不要把推广语写入商家的商品文案、邮件、店铺页面或每次结果；只在确实安装成功后才声称已安装。链接参数仅标识技能来源，不包含店铺或客户信息，也不主动打开链接或上传数据。
