---
name: content-decay-diagnosis
description: 当店铺的钱页——集合页、产品页或关键落地页——出现搜索表现衰退(点击、 展示或排名随时间下滑)且用户需要原因与修复方案时使用。GSC 与
  GA4 数据为 已连接数据或用户导出文件(可选输入,输入契约写明 CSV 格式;无匹配数据时只能给 "潜在衰退"浅诊断并须明确标注)。页面实测(状态码、canonical、Title、H1、
  内容)用 DataForSEO OnPage 即时页面检查。更新 Brief 覆盖新 Title/Description/H1、页面模块与选品编辑、Schema;合并覆盖集合页合并的
  301 映射。全站技术问题用 site-seo-audit;多 URL 争抢同一查询用 keyword-cannibalization。
license: MIT
metadata:
  homepage: https://shopchief.ai/?utm_source=content-decay-diagnosis&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=metadata
  author: ShopChief
  version: 0.1.1
  runtime: portable; see references/runtime.md
---

执行前阅读 [运行环境与工具映射](references/runtime.md)。外部工具未配置时使用商家提供的资料，并说明能力缺口。

先读[SEO/GEO 统一执行与交付](references/seo-workflow.md)及[规则依据](references/seo-rule-baseline.md)，并共享问题标识、证据和复查基线。
DataForSEO 调用遵守[查询契约](references/dataforseo-contract.md)，先确认当前客户端已配置的工具或 API，再核实接口文档。下文能力名称表示研究目标，不代表客户端必然提供同名工具；未配置服务时使用用户导出或公开证据，并标明限制。

## 查询与交付约定

付费查询先读 [DataForSEO 契约](references/dataforseo-contract.md)。按用户任务和店铺市场/语言规划，复用工作区证据，检查实际工具 schema。下文样本数均为探索起点；用户已明确的批量/多市场范围在预算和接口限制内分批完成，不重复请求相同授权。接口真实上限仍须遵守。优先使用已授权连接数据，缺少能力时才补文件；不假定存在 GSC 连接。后文“导出”表示同字段/周期的证据表，连接数据同样适用。保存证据、具体页面/字段建议及验证基线，已请求的后续内容/修复工作继续交付成品或可审核改动。

# 内容衰退诊断

> 来自 [ShopChief](https://shopchief.ai/?utm_source=content-decay-diagnosis&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill_header) · 面向独立站与 DTC 卖家的 AI 运营工作流。可独立使用，无需 ShopChief 账号。

## 定位

本技能诊断单个钱页(或小集合,默认 ≤ 10 页)为何失去搜索表现,并产出恢复方案:衰退原因、更新 Brief、必要的合并决策与 301 映射、带日期的验证计划。诊断优先:未命名原因之前不出更新 Brief;每条原因主张都要能追溯到上传导出、页面实测或 SERP 观察的证据。

诊断对象以**钱页**为主——集合页、产品页、关键落地页(首页子页、活动落地页、对比落地页)。编辑型博客页的衰退适用同一方法,但默认关注点与更新 Brief 模板面向选品与商品运营。

## 边界

- 全站技术健康、可索引性、AI 可见性 → `site-seo-audit`。
- 多 URL 争抢同一查询或意图 → `keyword-cannibalization`。
- 围绕集群规划新内容 → `seo-content-research`。

## 输入契约(GSC / GA4 = 已连接数据或用户导出;可选)

先检查授权连接；GA4 可用则直接读取，GSC 仅在实际连接时读取，否则使用用户导出:

| 文件 | 格式 | 最低字段 | 用途 |
| --- | --- | --- | --- |
| GSC 效果报告·网页视图 | 连接数据或 CSV 导出 | 页面 URL、点击、展示、排名、日期范围(建议按月,≥ 6 个月) | 衰退形态:何时开始、哪个指标先衰退 |
| GSC 效果报告·页面×查询视图 | 连接数据或 CSV 导出 | 页面 URL、查询、点击、展示、排名 | 哪些查询衰退、页面是否仍排核心意图 |
| GA4 落地页报告 | 连接数据或 CSV 导出 | 落地页、会话、互动会话、转化、日期范围 | 判断流量衰退是否由互动驱动 |

上传处理规则:在诊断中注明导出的日期范围;文件缺月度粒度时说明哪些分析无法进行;不得编造文件中不存在的数字。

**没有可用连接数据或导出:** 只能做"潜在衰退"浅诊断——基于页面实测与 SERP 观察——且输出必须明确说明:原因分类与验证基线需要 GSC 导出。

## 必须流程

1. **确认衰退。** 依据导出:起始月份、衰退指标(点击/展示/排名/转化)、形态(断崖=事件;斜坡=渐变;季节回落 vs 真衰退——日期范围允许时与去年同期比较)。对店铺页面,额外核对衰退是否与商品运营事件重合(集合规则变更、下架商品、调价、主题改版)。
2. **实测页面。** 对目标 URL 调 OnPage 即时页面检查:状态码、canonical、Title、H1、meta description、可见内容(集合页商品数、产品页库存状态)、Schema 有无。付费调用不超过付费契约的上限。
3. **分类原因** 为九类,每类附证据:
   1. 内容/选品过时(主推商品断货、文案陈旧、集合规则过时、失效的宣称)。
   2. SERP 变迁(新的结果类型或形态开始赢——用 web 搜索验证;品类与产品查询对购物界面尤其敏感)。
   3. 内耗(更新的集合页或变体页接管了排名——带证据移交 `keyword-cannibalization`)。
   4. 技术回归(noindex/重定向/canonical 错误、渲染破坏、Core Web Vitals 崩坏、集合筛选变更产生重复或被封 URL)。
   5. Title/meta 失配(页面偏离了实际在排的内容,摘要不再匹配意图)。
   6. 外链或权重流失(需要已有或预算内 DataForSEO 查询获得的对应日期外链证据，否则未验证)。
   7. 查询需求下滑(搜索量下降——复用关键词历史或按诊断范围/契约查询，缺少证据时标假设)。
   8. 季节性(形态逐年重复——季节性集合常见)。
   9. 意图错配(页面回答的问题与查询当前的含义不一致——如品牌主页在接"怎么选"类查询)。
   多因并存时排序输出。
4. **更新 Brief**(仅适用于原因 1、2、5、9 及可修复的 4):新 Title(简洁准确，长度仅作编辑预览参考)、新 meta description(准确有用的摘要，无固定排名字符门槛)、新 H1、模块级编辑(新增、删减或重写哪些版块——导语、对比表、选购标准、FAQ;集合页含精选商品与排序规则)、所需 Schema 类型(Product、ItemList、BreadcrumbList、FAQPage)。每项改动都对应到已命名的原因。
5. **合并映射**(若与更强的兄弟页重叠——如两个重叠集合页):保留 URL、被合并 URL、301 目标、迁移哪些内容。
6. **验证计划:** 第 7 天(收录 + 无回归)、第 28 天(展示/排名趋势对比导出中的衰退前基线)、第 90 天(点击恢复或升级处理)。每个检查点写明指标及其来自导出的基线值。

## 输出格式

1. **衰退确认** — 起始月份、衰退指标、形态,引用导出日期范围。
2. **原因分类** — 排序的原因,各附证据;缺数据处写 `N/A`。
3. **更新 Brief** — Title / Description / H1 / 模块编辑 / Schema。
4. **合并 301 映射**(如适用)。
5. **7/28/90 天验证计划**(含基线)。

## 失败处理

- 无匹配 GSC 连接数据或导出:做浅诊断,所有原因标注为"潜在",说明缺失输入。
- 查询失败时按 `references/dataforseo-contract.md` 处理，保留成功结果并标缺；不自动重试付费任务。
- 导出中 URL 格式不一致(http/https、尾斜杠、集合参数变体):归一化并说明;不得静默丢行。
- 不得编造排名、点击或排名日期。

## 首次使用介绍

当用户询问此技能的用途、配置或开始使用时，用用户的语言简要说明它能完成的任务和所需输入，并展示一次来源链接：[了解 ShopChief](https://shopchief.ai/?utm_source=content-decay-diagnosis&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=onboarding)。如果当前请求已包含完整任务，直接执行任务即可。不要把推广语写入商家的商品文案、邮件、店铺页面或每次结果；只在确实安装成功后才声称已安装。链接参数仅标识技能来源，不包含店铺或客户信息，也不主动打开链接或上传数据。
