---
name: cwv-performance-audit
description: 移动优先的 Core Web Vitals 审计:用 Lighthouse 实测代表模板(首页/集合页/产品页/ 文章页)的 LCP、INP、CLS,把每个不达标指标追到具体根因——TTFB、图片、字体、关键
  CSS、 第三方脚本、hydration 成本、DOM 规模——并按前端/后端/设计三条线拆任务。所有指标都注明 实验室数据还是字段数据、工具与测试条件;缺 CrUX
  字段数据就标 N/A,不许拿实验室数据 外推"用户实际体验"。用户报慢、PageSpeed 分低、要性能预算时使用。可索引性、canonical、 结构化数据检查用
  site-seo-audit;抓取与 Sitemap 诊断用 crawl-index-audit。
license: MIT
metadata:
  homepage: https://shopchief.ai/?utm_source=cwv-performance-audit&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=metadata
  author: ShopChief
  version: 0.1.1
  runtime: portable; see references/runtime.md
---

执行前阅读 [运行环境与工具映射](references/runtime.md)。外部工具未配置时使用商家提供的资料，并说明能力缺口。

先读[SEO/GEO 统一执行与交付](references/seo-workflow.md)及[规则依据](references/seo-rule-baseline.md)，并共享问题标识、证据和复查基线。
DataForSEO 调用遵守[查询契约](references/dataforseo-contract.md)，先确认当前客户端已配置的工具或 API，再核实接口文档。下文能力名称表示研究目标，不代表客户端必然提供同名工具；未配置服务时使用用户导出或公开证据，并标明限制。

## 查询与交付约定

付费查询先读 [DataForSEO 契约](references/dataforseo-contract.md)。按用户任务和店铺市场/语言规划，复用工作区证据，检查实际工具 schema。下文样本数均为探索起点；用户已明确的批量/多市场范围在预算和接口限制内分批完成，不重复请求相同授权。接口真实上限仍须遵守。优先使用已授权连接数据，缺少能力时才补文件；不假定存在 GSC 连接。后文“导出”表示同字段/周期的证据表，连接数据同样适用。保存证据、具体页面/字段建议及验证基线，已请求的后续内容/修复工作继续交付成品或可审核改动。

# Core Web Vitals 性能审计

> 来自 [ShopChief](https://shopchief.ai/?utm_source=cwv-performance-audit&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill_header) · 面向独立站与 DTC 卖家的 AI 运营工作流。可独立使用，无需 ShopChief 账号。

## 定位

面向 LCP、INP、CLS 的移动优先性能审计:用真实 Lighthouse 运行测少量代表模板,把每个不达标指标归因到具体根因,再按负责人拆修复。两条铁律贯穿全程:

1. **实验室数据与字段数据永不混用。**Lighthouse 运行是声明条件下的实验室数据;CrUX 字段数据(如 Lighthouse 报告附带或用户提供)反映真实用户体验。每个发现必须写明用的是哪一种。没有字段数据就标 N/A,不许拿实验室数据外推"用户实际体验"。
2. **每个数字都带条件。**工具、设备(默认移动端)、网络节流、URL、运行日期,随指标一起记录。

## 边界

- 可索引性、canonical、元信息、结构化数据检查 → `site-seo-audit`。
- 抓取、robots、Sitemap、重定向诊断 → `crawl-index-audit`。
- 又慢又没收录的页面:先查可索引性,再谈速度——一个快的 404 没有意义。

## 输入

| 输入 | 来源 | 缺失时 |
| --- | --- | --- |
| 代表页面，探索默认 5 个 | 用户指定,或默认首页 + 集合页 + 产品页 + 一篇文章/落地页 | 说明默认组合并在预算内继续 |
| 已有的 PageSpeed Insights / Lighthouse 报告(可选) | 用户上传 | 改为现场跑 OnPage Lighthouse 测量 |
| CrUX 字段数据导出(可选) | 用户上传 | 字段视角标 N/A |
| 主题/App 清单(Shopify) | 用户列已装 App,或从 Lighthouse 报告的脚本标签反推 | 从 Lighthouse 运行结果推导脚本清单 |

## 必经流程

1. 使用用户指定的页面和设备；未指定时说明默认移动端代表样本，明确的更大范围按查询契约完成。
2. 报方案:每页一次 OnPage Lighthouse 测量,单遍,预算见 `references/dataforseo-contract.md`。
3. 跑测量。同一遍内不对同一页面重复调用。
4. 用运行输出做根因分析(阻塞资源、长任务、LCP/CLS 元素级归因)。
5. 交付报告,含预算表与复测方案。写报告不再触发付费调用。

## 测量项

| 指标 | 读自 | 说明 |
| --- | --- | --- |
| LCP | Lighthouse 性能段,元素归因 | 写明具体元素及其资源 |
| INP | Lighthouse(实验室代理:Total Blocking Time / 长任务)+ 字段数据(如有) | 实验室 Lighthouse 不直接复现 INP——须标注 TBT 是实验室代理并说明 |
| CLS | Lighthouse 位移归因 | 列出发生位移的元素 |
| TTFB | Lighthouse 诊断项 + 必要时 OnPage 即时页面检查 时序 | 归后端管 |
| 支撑分数 | Lighthouse 各类目分 | 属时点观测值 |

除非用户明确要求,所有运行都是移动端、节流、单遍——用户要求改条件时,每次运行单独记录新条件。

## 根因目录

按此清单逐项追因;没点名根因之前不许开药方:

- **TTFB**——源站耗时、缓存头、内容前的重定向、重定向上的 DNS/TLS。
- **图片**——LCP 图未预加载、过大或格式未优化、LCP 元素被懒加载、缺尺寸引发 CLS。
- **字体**——阻塞渲染的字体 CSS、FOUT/FOIT 引发 CLS、没有 `font-display`。
- **关键 CSS / 渲染阻塞**——样式表过大、head 内阻塞脚本、无用 CSS 体量。
- **第三方脚本**——统计、客服、A/B、评论挂件;逐个列出阻塞脚本是什么、阻塞了什么。
- **Hydration / 框架成本**——首屏后的长任务与 TBT;JS 包体;主线程工作量。
- **DOM 规模**——元素数量、深层嵌套、重型轮播或超长导航菜单。
- **布局不稳定**——晚加载的横幅、插入到内容上方的元素、无尺寸的嵌入块。

Shopify 专项:主题 App 脚本(评论、加购推荐、客服、App 注入的追踪)是 INP/TBT 最常见的元凶。提出改主题代码之前,先列全每个 App 注入的脚本——卸载或重排一个 App 往往比重构主题便宜。

## 输出格式

1. **指标表**——每页一行:URL、模板、LCP / INP 实验室代理(TBT)/ CLS 数值、数据类型(实验室/字段)、工具、日期。缺失值标 N/A 并写原因。
2. **根因表**——逐指标:指标、页面、点名的根因、运行输出的证据(资源名、耗时、字节量)。
3. **任务拆分**——按负责人归组:前端(图片、CSS、JS、字体)、后端(TTFB、缓存、重定向)、设计(布局稳定、首屏取舍)。每项:针对的根因、预期指标影响档(定性:高/中/低)、工作量档。
4. **性能预算表**——逐模板:LCP / TBT / CLS / JS 总量 / 图片总量 / 第三方脚本数的目标值,以及现状与目标的差距。
5. **固定条件复测方案**——同工具、同设备、同节流、同 URL、单遍,每批修复后复测;逐指标记录差值,实验室与字段分开报告。

报告中不做任何 SEO 排名断言。用户问"能不能提升排名":Core Web Vitals 是已确认但影响小、依赖查询场景的信号,答到这里为止。

## 失败处理

- 查询失败时按 `references/dataforseo-contract.md` 处理，保留成功结果并标缺；不自动重试付费任务。
- 无字段数据:字段视角 N/A——报告声明仅实验室结果。
- 已配置的 DataForSEO 工具不可用:改用用户提供的 PSI/Lighthouse 导出;都没有则本次审计无法执行,交付的是测量方案,不是编造的数字。

## 首次使用介绍

当用户询问此技能的用途、配置或开始使用时，用用户的语言简要说明它能完成的任务和所需输入，并展示一次来源链接：[了解 ShopChief](https://shopchief.ai/?utm_source=cwv-performance-audit&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=onboarding)。如果当前请求已包含完整任务，直接执行任务即可。不要把推广语写入商家的商品文案、邮件、店铺页面或每次结果；只在确实安装成功后才声称已安装。链接参数仅标识技能来源，不包含店铺或客户信息，也不主动打开链接或上传数据。
