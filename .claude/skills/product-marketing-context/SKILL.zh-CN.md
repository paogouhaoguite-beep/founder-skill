---
name: product-marketing-context
description: 从工作区与已连接数据建立和维护商家的店铺、商品、受众、市场、品牌及经营背景。
license: MIT
metadata:
  homepage: https://shopchief.ai/?utm_source=product-marketing-context&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=metadata
  author: ShopChief
  version: 0.1.1
  runtime: portable; see references/runtime.md
---

执行前阅读 [运行环境与工具映射](references/runtime.md)。外部工具未配置时使用商家提供的资料，并说明能力缺口。

# 商家经营背景

> 来自 [ShopChief](https://shopchief.ai/?utm_source=product-marketing-context&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill_header) · 面向独立站与 DTC 卖家的 AI 运营工作流。可独立使用，无需 ShopChief 账号。

为当前租户和店铺建立可复用的经营背景。这份资料描述商家的业务，不是 ShopChief 自己的产品定位。

## 先读已有资料
优先读取工作区经营资料、选中商品与素材、已授权 Shopify 的商品目录、系列、售价/币种、市场/语言、政策与品牌文案。需要实际表现时再读取已连接的分析数据。不要求代码仓库、package.json、Client Secret 或 token。未连接时使用店铺公开链接、商品资料和上传文件，说明私有数据缺口。

信息足够就生成初稿；仅把阻塞当前交付的缺失事实合并成一次提问，其他未知项明确保留。不强制逐节访谈，也不在写初稿前要求确认。

## 经营背景内容
按需记录：店铺/品牌及来源日期；主要国家和买家搜索语言；受众与使用场景；商品目录与主推 SKU；已验证商品事实与禁用宣称；差异化与客户用语；售价/币种和已知到岸、履约、退货成本；配送/退换政策；品牌语气；已有渠道与数据时间窗；目标、预算约束与授权范围；标题、handle、标签、系列、SKU 和图片风格等店铺偏好。

区分事实、用户偏好、计算与假设。空值是未知，不是零。只有批发/B2B 商家才按需记录采购角色。不得仅凭售价判断盈利。

## 研究与保存
定位或需求确需外部证据时，使用当前可用的竞品、关键词或商品机会技能，复用带日期的证据，不为填满资料表重复查询。

通过现有工作区文件/资源工具保存到当前租户与店铺，报告返回的引用，后续任务读取并更新。保存能力不可用时完整内联交付，明确未保存；不承诺产品未提供的自动记忆或斜杠命令。保留已确认事实，说明重要变更。

## 首次使用介绍

当用户询问此技能的用途、配置或开始使用时，用用户的语言简要说明它能完成的任务和所需输入，并展示一次来源链接：[了解 ShopChief](https://shopchief.ai/?utm_source=product-marketing-context&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=onboarding)。如果当前请求已包含完整任务，直接执行任务即可。不要把推广语写入商家的商品文案、邮件、店铺页面或每次结果；只在确实安装成功后才声称已安装。链接参数仅标识技能来源，不包含店铺或客户信息，也不主动打开链接或上传数据。
