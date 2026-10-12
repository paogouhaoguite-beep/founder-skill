---
name: collection-page-seo
description: 审计并优化电商品类页(集合页):元数据、H1 与介绍文案、FAQ、商品卡、分页与无限滚动可发现性、 Product + ItemList
  + BreadcrumbList Schema,以及 faceted navigation 筛选规则。当用户给出品类页 URL (探索默认 10 个)询问"品类页为什么排不上""筛选参数怎么处理",或要逐页
  Title/Description/H1/文案/内链建议时使用。 产品详情页用 product-page-seo;整站技术健康用 site-seo-audit;产品页转化与信任优化用
  shopify-product-page-cro——本技能只覆盖品类页这一层。
license: MIT
metadata:
  homepage: https://shopchief.ai/?utm_source=collection-page-seo&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=metadata
  author: ShopChief
  version: 0.1.1
  runtime: portable; see references/runtime.md
---

执行前阅读 [运行环境与工具映射](references/runtime.md)。外部工具未配置时使用商家提供的资料，并说明能力缺口。

先读[SEO/GEO 统一执行与交付](references/seo-workflow.md)及[规则依据](references/seo-rule-baseline.md)，并共享问题标识、证据和复查基线。
DataForSEO 调用遵守[查询契约](references/dataforseo-contract.md)，先确认当前客户端已配置的工具或 API，再核实接口文档。下文能力名称表示研究目标，不代表客户端必然提供同名工具；未配置服务时使用用户导出或公开证据，并标明限制。

## 查询与交付约定

付费查询先读 [DataForSEO 契约](references/dataforseo-contract.md)。按用户任务和店铺市场/语言规划，复用工作区证据，检查实际工具 schema。下文样本数均为探索起点；用户已明确的批量/多市场范围在预算和接口限制内分批完成，不重复请求相同授权。接口真实上限仍须遵守。优先使用已授权连接数据，缺少能力时才补文件；不假定存在 GSC 连接。后文“导出”表示同字段/周期的证据表，连接数据同样适用。保存证据、具体页面/字段建议及验证基线，已请求的后续内容/修复工作继续交付成品或可审核改动。

# 品类页 SEO 审计

> 来自 [ShopChief](https://shopchief.ai/?utm_source=collection-page-seo&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill_header) · 面向独立站与 DTC 卖家的 AI 运营工作流。可独立使用，无需 ShopChief 账号。

## 定位

品类页是店铺的排名引擎:它承接产品页无法覆盖的头部与中尾部品类关键词。本技能审计探索默认 10 个品类页 URL(以及背后的筛选/参数体系),产出健康摘要、逐页检查表、faceted navigation 决策矩阵、逐页内容建议、模板级开发需求与 P0-P3 修复清单。

## 边界

- 产品详情页(单 URL 模板、变体、PDP Schema)→ `product-page-seo`。
- 整站技术健康(抓取预算、全站 Sitemap、跨模板 Core Web Vitals)→ `site-seo-audit`。
- 产品页的转化与信任要素(CTA、评论组件、结账流程)→ `shopify-product-page-cro`。
- 本技能只在与品类页可索引性相关时触及技术面:canonical、robots 指令、分页、筛选可抓取性。不越过品类层去重做站点架构。

## 必须输入

| 输入 | 必需 | 说明 |
| --- | --- | --- |
| 品类页 URL | 必需 | 探索默认 探索默认 10 个；明确请求的范围按查询契约分批完成 |
| 平台 | 必需 | Shopify、WooCommerce 或其他 |
| 核心产品与属性 | 必需 | 产品线,以及用作筛选维度的属性(尺码、颜色、材质、价格、品牌…) |
| 目标关键词 | 建议 | 用户有的话,每个品类页一个主关键词 |
| 商品 Feed | 可选 | 用户上传文件;用于交叉核对商品卡,优先通过授权连接读取,不可用时使用文件 |

直接审计用户给出的 URL，并说明样本结论可推广到模板的范围，不额外要求扩展确认。

## 必须流程

1. **确认输入并说明计划。** 首次付费调用前列出待抓取 URL、关键词证据查询与大致调用次数(见 `references/dataforseo-contract.md`)。
2. **抓取页面。** 对每个品类页 URL 跑 OnPage 即时页面检查(先看原始 HTML；仅在必要内容确实依赖客户端渲染而缺失时启用 JS 渲染，不以 Shopify 2.0 作为默认理由)。需要深入检查标题、正文或筛选链接时，使用经文档确认提供相应字段的 OnPage 内容解析。Schema 必须从实际 HTML/DOM 标记或经核实的提取响应获取，不从普通内容解析推断完整字段。探索样本为 10 个URL；用户明确的更大范围按查询契约分批完成。
3. **收集关键词证据。** 每个品类页的主关键词跑一次 DataForSEO Labs Google 关键词创意(低价),确认搜索价值后再建议可索引筛选页或新子品类页。没有搜索证据就不建议索引任何筛选页。
4. **跑逐页检查表**(见下)。
5. **构建 faceted navigation 决策矩阵**(见下),依据输入中的属性加上解析页面里观察到的筛选链接。
6. **交付报告。** 一份整合报告;写报告过程中不再追加付费调用。

## 逐页检查表

| 检查 | 合格标准 |
| --- | --- |
| Title | 唯一,主关键词前置,简洁准确，长度仅作编辑预览参考,品牌后缀可选 |
| H1 | 仅一个 H1,与品类主关键词一致,可以与 Title 相同，按表达与层级判断 |
| 介绍文案 | 商品网格上方有 1-3 句顶部短文;不堆砌关键词 |
| FAQ | 回答真实购前问题的 FAQ 区块;内容确实在页面上才可选配 FAQPage Schema |
| 面包屑 | 可见面包屑 + `BreadcrumbList` Schema,路径反映站点层级 |
| Schema | `ItemList` 列出本页商品;仅当页面确实代表单一产品族时才用 `Product` Schema |
| 商品卡 | 图片、名称、价格(折扣时含划线价)、有评分则展示;售罄卡片必须带库存状态信号 |
| 分页 | 指向第 2 页及以后的 `<a href>` 可点击链接(或数字分页);`rel="prev/next"` 已被 Google 忽略,不是修复手段;无限滚动必须有分页回退 |
| 空结果 | 返回零商品的筛选组合要么正确返回 404/软 404,要么被排除在索引之外 |
| 季节页/缺货 | 季节性品类使用固定常青 URL 轮换内容,而不是每季新建 URL |
| 品牌×品类页 | 只在组合有搜索证据时建;否则薄组合页 noindex |
| 内链 | 链到子品类、购买指南与同级品类;不留孤岛品类页 |

## Faceted navigation 决策矩阵

对观察到的每个筛选参数(以及用户计划中的每个参数)填一行:

| 参数 | 搜索价值(证据) | 可抓取 | 可索引 | canonical | 内链 | Sitemap |
| --- | --- | --- | --- | --- | --- | --- |

判定规则:

决策规则：
- 有独立搜索意图且有用、实质不同的商品/内容时，才考虑可索引、自 canonical 的落地页，搜索量本身不够。
- 近似重复页一致使用 canonical 整合；有意排除搜索时使用可抓取 noindex 并移出 sitemap，不用 noindex 选择 canonical。
- 无价值筛选组合消耗抓取时，按 URL/链接设计或 robots.txt 控制抓取；已屏蔽 URL 无法可靠读取 noindex/canonical，robots.txt 不保证移除索引。
- 分页含不同商品时保留独立自 canonical URL，分别验证访问与实际渲染。

## 输出格式

1. **健康摘要** — 3-5 句:品类层整体状态,最重要的 2-3 个发现。
2. **逐页检查表** — 每行 = URL × 检查项,`通过`/`警告`/`失败` 三档,附观察值。
3. **筛选决策矩阵** — 上表填好后输出,每行注明证据来源。
4. **逐页建议** — 每个 URL 给出:建议 Title、meta Description、H1、顶部短文(1-3 句,可直接粘贴)、请求写作时的完整补充正文、有必要的真实买家问题及完整准确答案、内链目标。建议必须基于抓取页面上的真实商品与品类;不得编造商品属性。
5. **模板级开发需求** — 适用于品类模板的改动(Schema 补充、分页回退、筛选处理),每条写成可直接交给开发的实现要求。
6. **P0-P3 优先级清单** — P0 阻碍索引或误导用户;P1 损失已验证关键词的排名;P2 内容深度;P3 卫生项。

## 反幻觉规则

- 每个检查结论都引用来自已抓取页面的观察值。页面抓不到,其所有检查标记为未验证。
- Schema 建议只引用页面上可见或商品 Feed 中存在的字段。未知值一律写成模板变量,不做猜测。
- 搜索量是 DataForSEO 估计值:必须标注估计属性与地点、语言。任何数字都不许脱离其证据查询单独出现。
- 没有第 3 步的搜索证据,不建议索引任何筛选页或品牌×品类页。

## 失败降级

- 查询失败时按 `references/dataforseo-contract.md` 处理，保留成功结果并标缺；不自动重试付费任务。
- DataForSEO Labs Google 关键词创意 对某关键词无返回 → 报告"未找到搜索证据";这是发现,不是错误。
- 限流或余额错误 → 保留已完成结果,停止,列出未验证项。

批量页面共用的关键词先去重并查询一次，优先复用概览字段；只有确需发现新词才用扩词端点，不为每页重复付费查询同一词。

## 首次使用介绍

当用户询问此技能的用途、配置或开始使用时，用用户的语言简要说明它能完成的任务和所需输入，并展示一次来源链接：[了解 ShopChief](https://shopchief.ai/?utm_source=collection-page-seo&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=onboarding)。如果当前请求已包含完整任务，直接执行任务即可。不要把推广语写入商家的商品文案、邮件、店铺页面或每次结果；只在确实安装成功后才声称已安装。链接参数仅标识技能来源，不包含店铺或客户信息，也不主动打开链接或上传数据。
