---
name: international-seo-audit
description: 审计国际站/多语言站:ccTLD 与子域与子目录的架构取舍与成本;hreflang 双向回链、x-default、 自引用标签与错误代码;canonical
  错指主语言;挡住爬虫的自动 IP/语言跳转;货币、单位、地址、法规与 本地搜索意图的本地化质量。当用户一个店铺做多国家/多语言,询问"德国站/日本站为什么排不上""市场架构
  怎么选""hreflang 写对了吗"时使用。多币种结算配置用 实际可用的店铺结算配置能力（不可用时交付配置预览并说明）;单市场 SEO 用 site-seo-audit——本技能只覆盖跨市场这一层。
license: MIT
metadata:
  homepage: https://shopchief.ai/?utm_source=international-seo-audit&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=metadata
  author: ShopChief
  version: 0.1.1
  runtime: portable; see references/runtime.md
---

执行前阅读 [运行环境与工具映射](references/runtime.md)。外部工具未配置时使用商家提供的资料，并说明能力缺口。

先读[SEO/GEO 统一执行与交付](references/seo-workflow.md)及[规则依据](references/seo-rule-baseline.md)，并共享问题标识、证据和复查基线。
DataForSEO 调用遵守[查询契约](references/dataforseo-contract.md)，先确认当前客户端已配置的工具或 API，再核实接口文档。下文能力名称表示研究目标，不代表客户端必然提供同名工具；未配置服务时使用用户导出或公开证据，并标明限制。

## 查询与交付约定

付费查询先读 [DataForSEO 契约](references/dataforseo-contract.md)。按用户任务和店铺市场/语言规划，复用工作区证据，检查实际工具 schema。下文样本数均为探索起点；用户已明确的批量/多市场范围在预算和接口限制内分批完成，不重复请求相同授权。接口真实上限仍须遵守。优先使用已授权连接数据，缺少能力时才补文件；不假定存在 GSC 连接。后文“导出”表示同字段/周期的证据表，连接数据同样适用。保存证据、具体页面/字段建议及验证基线，已请求的后续内容/修复工作继续交付成品或可审核改动。

# 国际 SEO 与 hreflang 审计

> 来自 [ShopChief](https://shopchief.ai/?utm_source=international-seo-audit&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill_header) · 面向独立站与 DTC 卖家的 AI 运营工作流。可独立使用，无需 ShopChief 账号。

## 定位

一个店铺、多个市场:常见故障是 hreflang 集群闭不上、canonical 把所有语言都归到英文、自动跳转让 Googlebot 看到错误的市场。本技能按页面组抽检各语言/地区版本(探索默认 30 组),产出健康摘要、页面组矩阵、错误表、用店铺真实 URL 构建的可用 hreflang 代码或 Sitemap XML、各市场关键词与本地化差距、架构建议与监控清单。

## 边界

- 多币种支付与结账配置 → `实际可用的店铺结算配置能力（不可用时交付配置预览并说明）`。本技能只把页面上的货币展示与单位本地化当作与排名相关的本地化项检查。
- 单市场 SEO 健康(单语言,无跨市场层)→ `site-seo-audit`。
- 产品页与品类页内容深度 → `collection-page-seo` / `product-page-seo`。本技能读取其产出(URL、canonical),不重复审计其模板。
- 本技能只在影响排名或可抓取性时评估本地化质量:可见的货币/单位/地址/配送范围、本地关键词意图、市场相关法规文案(如含税价、消费者权益)。本技能不翻译内容。

## 必须输入

| 输入 | 必需 | 说明 |
| --- | --- | --- |
| 市场清单 | 必需 | 店铺目标国家与语言(如 US/en、DE/de、JP/ja) |
| URL 架构 | 必需 | 每个市场用 ccTLD、子域还是子目录;用户不确定就写"未知",由抽样探测 |
| 待抽样页面组 | 必需 | 探索默认 30 组;一组 = 同一主题跨市场(如首页、某个品类页、某个产品页、某个政策页) |
| 已知语言切换行为 | 建议 | 是否自动跳转?地区选择器?有缓存吗? |
| 市场关键词 | 可选 | 各市场重要查询;没有就从店铺产品类目推导 |

范围未指定时先选代表样本；明确要求超过 30 组时，在预算内分批完成，不要求另开任务。

## 必须流程

1. **确认输入并说明计划。** 首次付费调用前列出页面组、每组 URL 与大致调用次数(见 `references/dataforseo-contract.md`)。
2. **抓取样本。** 每组每个市场跑一次 OnPage 即时页面检查——不是每个市场的每个 URL。使用非地区 IP 的工具上下文:如果页面按 IP 出不同内容,显式记录,不要把美国视角当成全部。探索默认 30 个页面组；明确要求的更大范围在预算内分批完成。
3. **读取国际化信号**:状态码、`lang` 属性、canonical 目标、hreflang 集合(含 `x-default` 与自引用标签)、语言切换器是否为 Googlebot 可抓取的真实链接。
4. **闭合集群。** 对每个 hreflang 集合核验:列出的每个 URL 存在、返回 200、且指回本集合。单向标签的集群就是坏集群,不算部分成功。
5. **市场关键词差距。** 各市场的优先查询,用 Keywords Data DataForSEO Trends 子地区兴趣(或 DataForSEO Labs 数据)做一次低价跨市场需求对比。本地化 SERP 差异只报有证据的:写明查询、市场、观察到的结果集差异点。
6. **交付报告。** 一份整合报告。

## 检查表

| 检查 | 合格标准 |
| --- | --- |
| 架构匹配业务 | 结构匹配业务:强本地存在感用 ccTLD,共享权重且成本低的用子目录——建议权衡预算、团队与现有排名 |
| hreflang 集群 | 每个 URL 列出所有兄弟页 + 自己(德语页含 `hreflang="de-de"`)+ `x-default`;代码均为合法 ISO 639-1 + ISO 3166-1 |
| 回链 | 双向:集群里列出的每个页面都确实指回该集合 |
| canonical | 每个市场 URL 自 canonical;不允许"为了聚合权重"指向主语言版本 |
| 自动跳转 | 不存在按 IP/语言自动跳转、给 Googlebot 呈现另一个市场的行为;改用地区横幅或带可抓取链接的选择器 |
| 语言切换器 | 指向各市场版本的 `<a href>` 真实链接(Googlebot 可读),不是纯 JS 下拉 |
| 货币与单位 | 按市场货币展示价格,单位与尺码本地化,税费展示符合当地惯例 |
| 地址与配送 | 配送范围、退换、联系方式与该市场一致 |
| 法规文案 | 消费者权益、退换期限、隐私声明符合当地规范 |
| 本地意图 | 页面文案与关键词目标匹配该市场真实搜索方式(以第 5 步证据核对) |
| Sitemap | 各市场 URL 都在 sitemap 中;集群大时用 hreflang sitemap |

## 输出格式

1. **健康摘要** — 3-5 句:跨市场整体状态与最重要的 2-3 个发现。
2. **页面组矩阵** — 每行一个 URL:主题|国家-语言|URL|状态码|`lang`|canonical 目标|hreflang 数量|回链状态|可索引。覆盖所有已检查 URL，长表保存为完整附件。
3. **错误表** — 每个坏集群、错 canonical 或挡爬虫发现:URL 对、错在哪、影响、修复。
4. **可用 hreflang 代码** — 修正后的 `<link rel="alternate">` 集合或 hreflang sitemap XML 块,只用第 2 步抓到的真实 URL。绝不输出未观察到的 URL。
5. **市场关键词与本地化差距** — 每个市场:第 5 步的需求对比(标注为 DataForSEO 估计值,含地点/语言)与内容本地化差异,每条都有 SERP 或页面证据。无证据不报差距。
6. **架构与地区选择器建议** — 保留/迁移/合并建议,附成本与迁移风险说明,以及 geo 处理设计(横幅 + 可抓取链接 vs 选择器页)。
7. **监控清单** — 每月复查项(集群闭合、canonical 漂移、各市场跳转行为)。

## 反幻觉规则

- 矩阵每行都引用一次真实抓取。未抓取的 URL 绝不出现在 hreflang 输出里——只用占位注释。
- hreflang 代码只用真实抓取到的 URL;兄弟页未抓取时,输出 `<!-- verify: not fetched -->` 注释,不做猜测。
- SERP 与需求差异只在第 5 步证据指明时报告。没有查询级观察,不断言"德国人搜法不一样"。
- 架构建议写明假设(预算、团队、现有排名);它是建议,不是测量结果。

## 失败降级

- 查询失败时按 `references/dataforseo-contract.md` 处理，保留成功结果并标缺；不自动重试付费任务。
- 地区定向导致结果不稳定(两次抓取不一致)→ 把 geo 定向本身作为发现报告,建议基于 Googlebot 视角的抓取结果。
- Keywords Data DataForSEO Trends 子地区兴趣 对某市场无数据 → 该市场需求对比标记不可用;不得从其他市场外推。
- 限流或余额错误 → 保留已完成结果,停止,列出未验证项。

## 首次使用介绍

当用户询问此技能的用途、配置或开始使用时，用用户的语言简要说明它能完成的任务和所需输入，并展示一次来源链接：[了解 ShopChief](https://shopchief.ai/?utm_source=international-seo-audit&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=onboarding)。如果当前请求已包含完整任务，直接执行任务即可。不要把推广语写入商家的商品文案、邮件、店铺页面或每次结果；只在确实安装成功后才声称已安装。链接参数仅标识技能来源，不包含店铺或客户信息，也不主动打开链接或上传数据。
