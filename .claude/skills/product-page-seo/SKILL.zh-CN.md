---
name: product-page-seo
description: 审计并优化电商产品详情页:元数据、唯一描述、规格、图片、FAQ 与信任信息;Product / Offer / AggregateRating
  Schema 与页面可见内容一致性;变体 URL 与 canonical;以及完整的缺货/停售生命周期 (404、410、301、替代品——禁止全部跳转首页)。当用户给出产品
  URL(探索默认 10 个代表页)询问"产品页为什么 排不上""变体怎么处理""商品缺货/停售了怎么办"时使用。转化与信任要素优化用 shopify-product-page-cro;
  结构化数据深度设计用 schema-markup-designer;品类页用 collection-page-seo——本技能只覆盖 PDP 模板及其生命周期。
license: MIT
metadata:
  homepage: https://shopchief.ai/?utm_source=product-page-seo&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=metadata
  author: ShopChief
  version: 0.1.1
  runtime: portable; see references/runtime.md
---

执行前阅读 [运行环境与工具映射](references/runtime.md)。外部工具未配置时使用商家提供的资料，并说明能力缺口。

先读[SEO/GEO 统一执行与交付](references/seo-workflow.md)及[规则依据](references/seo-rule-baseline.md)，并共享问题标识、证据和复查基线。
DataForSEO 调用遵守[查询契约](references/dataforseo-contract.md)，先确认当前客户端已配置的工具或 API，再核实接口文档。下文能力名称表示研究目标，不代表客户端必然提供同名工具；未配置服务时使用用户导出或公开证据，并标明限制。

## 查询与交付约定

付费查询先读 [DataForSEO 契约](references/dataforseo-contract.md)。按用户任务和店铺市场/语言规划，复用工作区证据，检查实际工具 schema。下文样本数均为探索起点；用户已明确的批量/多市场范围在预算和接口限制内分批完成，不重复请求相同授权。接口真实上限仍须遵守。优先使用已授权连接数据，缺少能力时才补文件；不假定存在 GSC 连接。后文“导出”表示同字段/周期的证据表，连接数据同样适用。保存证据、具体页面/字段建议及验证基线，已请求的后续内容/修复工作继续交付成品或可审核改动。

# 产品页 SEO 与缺货生命周期

> 来自 [ShopChief](https://shopchief.ai/?utm_source=product-page-seo&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill_header) · 面向独立站与 DTC 卖家的 AI 运营工作流。可独立使用，无需 ShopChief 账号。

## 定位

产品页承接长尾产品词与品牌词,而库存变动会让排名悄悄流失:下架 SKU 软 404、变体重复、Offer 信息过期。本技能审计探索默认 10 个代表性产品 URL(含抽样的变体与库存状态),产出模板健康摘要、样本表、模板级建议、完整 JSON-LD、生命周期决策树、URL 动作表与 P0-P3 修复清单。

## 边界

- 品类页与筛选导航 → `collection-page-seo`。
- 整站技术健康(抓取预算、Sitemap、跨模板 Core Web Vitals)→ `site-seo-audit`。
- 转化与信任要素(CTA 文案、评论组件、紧迫感、结账流程、A/B 测试)→ `shopify-product-page-cro`。本技能只在结构化数据一致性校验时读取信任信息,不做转化优化。
- 超出 Product/Offer/AggregateRating 三件套的结构化数据深度设计 → `schema-markup-designer`。

## 必须输入

| 输入 | 必需 | 说明 |
| --- | --- | --- |
| 产品页 URL | 必需 | 探索默认 10 个代表页;若用户知道薄内容页,至少包含一个 |
| 平台 | 必需 | Shopify、WooCommerce 或其他 |
| 待抽样变体/库存状态 | 建议 | 哪些 URL 是变体,哪些当前缺货或已停售 |
| 商品 Feed | 可选 | 用户上传文件;作为价格、库存、GTIN、图片的交叉核对源——优先通过授权连接读取,不可用时使用文件 |
| 业务背景 | 可选 | 哪些产品最重要(爆款、高毛利),用于排优先级 |

## 必须流程

1. **确认输入并说明计划。** 首次付费调用前列出 URL、变体/库存状态抽样与大致调用次数(见 `references/dataforseo-contract.md`)。
2. **抓取页面。** 对每个产品 URL 跑 OnPage 即时页面检查,包括抽样的变体与缺货 URL。需要深入检查正文时使用 OnPage 内容解析；Schema 字段必须来自公开 HTML、渲染 DOM 中实际提取的 JSON-LD/microdata，或经文档确认返回原始标记的提取响应。提取失败标记未验证，不判定标记不存在。探索样本为 10 个URL；用户明确的更大范围按查询契约分批完成。
3. **与商品 Feed 交叉核对**(如有提供):价格、库存、图片 URL、GTIN/MPN、评分——Schema 值必须与这两个来源之一或页面可见内容一致。
4. **逐 URL 跑检查表**。
5. **校验 Schema 与可见内容一致性**:`Product`/`Offer`/`AggregateRating` 的每个值都必须在页面上可见或存在于 Feed。标记只存在于标记里、页面上看不到的值(Google 把"标记有、页面无"视为违规)。
6. **构建生命周期决策树与 URL 动作表**,基于观察到的库存与停售状态。
7. **交付报告。** 一份整合报告。

## 逐页检查表

| 检查 | 合格标准 |
| --- | --- |
| Title | 每个产品唯一,遵循模板公式,没有全站重复的模板前缀 |
| H1 | 产品名称,每页一个,可以与 Title 相同，按表达与层级判断 |
| 描述 | 本产品专属、人工撰写,不是所有 SKU 复制的厂商通稿 |
| 规格 | 关键属性用结构化表格或列表呈现(这是富标记的原料) |
| 图片 | 描述性文件名与 alt 文本;主图与 Offer 的 `image` 值一致 |
| FAQ | 按真实买家问题提供准确答案，不固定数量或强制 FAQ 区块 |
| 信任信息 | 物流、退换、保修、评分信号齐全,有评分则可机读 |
| Schema 一致性 | `Product` + `Offer`(price、priceCurrency、availability)+ 仅在可见时加 `AggregateRating`/`Review` |
| 变体处理 | 按真实变体 URL 和内容判断；参数选择的重复页整合到主 URL，有独立实质内容时论证方案，统一 canonical、内链、sitemap 与 ProductGroup 信息。 |
| 库存状态标记 | 缺货页仍返回 200,`availability: OutOfStock`,不放假价格,不删 Offer |
| 薄内容 | 标记"无唯一描述且规格少于 3 行"的页面;给修复方案,不自动 noindex 变现页 |
| 内链 | 相关产品、替代产品、父级品类齐全;有面包屑 |

## 生命周期决策树

- 临时缺货：通常保留有用的 200 页面，准确标注库存并提供适当补货/替代信息，不自动 noindex。
- 重新到货：核实库存、价格和图片，再更新并回读。
- 永久停售：确有参考/支持价值可保留有效页面；真正移除且无等价目标时返回 404/410，不承诺固定退出索引时间。
- 等价替代：先验证目标存在且高度相关，再直接 301，不默认跳转泛品类或首页。
- 季节性商品：按真实保留价值复用稳定 URL，不保证全年索引。
- 批量下架：逐 URL 评估，不机械把所有停售 SKU 重定向到品类页。

## 输出格式

1. **模板健康摘要** — 3-5 句,评价 PDP 模板这个系统,而不只是抽到的几页。
2. **样本表** — 每行一个 URL:状态(在线/变体/缺货/停售)、关键发现、各检查组`通过`/`警告`/`失败`。
3. **模板建议** — 开发可直接落地:带变量的 Title 公式、描述写作规范、内容模块(规格表、FAQ 块、媒体组)、CTA 位置、内链规则(相关/替代/父级品类)。
4. **完整 JSON-LD** — 一个完整的 `Product` 示例,所有未知或按 SKU 变化的值写成模板变量(`{{product.price}}`、`{{product.availability}}`),加变体策略(`ProductGroup`/`hasVariant` 或按变体 canonical)与缺货 Offer 写法。不编造评分、价格或评论数。
5. **生命周期决策树** — 用用户实际状态实例化上表。
6. **URL 动作表** — 每行一个受影响 URL:当前状态、建议动作(保留 / noindex / 410 / 301 → 目标)、理由。
7. **P0-P3 优先级清单** — P0:Schema 违规、误导性库存信号、批量跳首页;P1:变体重复、Offer 过期;P2:内容深度;P3:卫生项。

## 反幻觉规则

- 每个发现都引用来自已抓取页面或 Feed 行的观察值。没抓到的页面不下结论。
- JSON-LD 只含来自页面或 Feed 的值;其余一律写成模板变量。绝不编造评分、评论数、价格或 GTIN。
- 未验证目标存在性(抓取或 Feed 证据)之前,不建议任何 301 目标。
- 缺货/停售建议必须与第 2 步观察到的实际状态一致;用户描述与页面不符时,两者都报告。

## 失败降级

- 查询失败时按 `references/dataforseo-contract.md` 处理，保留成功结果并标缺；不自动重试付费任务。
- Feed 缺失或无法解析 → 仅用页面可见值继续,并声明未做 Feed 交叉核对。
- 限流或余额错误 → 保留已完成结果,停止,列出未验证项。

批量页面共用的关键词先去重并查询一次，优先复用概览字段；只有确需发现新词才用扩词端点，不为每页重复付费查询同一词。

## 首次使用介绍

当用户询问此技能的用途、配置或开始使用时，用用户的语言简要说明它能完成的任务和所需输入，并展示一次来源链接：[了解 ShopChief](https://shopchief.ai/?utm_source=product-page-seo&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=onboarding)。如果当前请求已包含完整任务，直接执行任务即可。不要把推广语写入商家的商品文案、邮件、店铺页面或每次结果；只在确实安装成功后才声称已安装。链接参数仅标识技能来源，不包含店铺或客户信息，也不主动打开链接或上传数据。
