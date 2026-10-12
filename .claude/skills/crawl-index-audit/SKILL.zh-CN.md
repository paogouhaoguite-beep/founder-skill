---
name: crawl-index-audit
description: 诊断页面"为什么没被发现、没被渲染、没资格被索引、没真的被收录"。四个状态分开判断、 不混为一谈,检查 robots 冲突、Sitemap
  质量、noindex、参数/分页/筛选 URL、 www/HTTPS/尾斜杠变体、软 404、重定向链、孤岛页与 JS 渲染可发现性。抓取与渲染证据 用 DataForSEO
  on_page 系列工具在限定 URL 样本上实测;索引状态只认用户提供的 GSC/日志导出,没有则整节标 N/A。用户问"页面为什么没收录"、报告抓取或 Sitemap
  问题、 怀疑筛选/分页页浪费抓取预算时使用。页面速度与 Core Web Vitals 用 cwv-performance-audit;内容重复与关键词内耗用
  keyword-cannibalization。
license: MIT
metadata:
  homepage: https://shopchief.ai/?utm_source=crawl-index-audit&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=metadata
  author: ShopChief
  version: 0.1.1
  runtime: portable; see references/runtime.md
---

执行前阅读 [运行环境与工具映射](references/runtime.md)。外部工具未配置时使用商家提供的资料，并说明能力缺口。

先读[SEO/GEO 统一执行与交付](references/seo-workflow.md)及[规则依据](references/seo-rule-baseline.md)，并共享问题标识、证据和复查基线。
DataForSEO 调用遵守[查询契约](references/dataforseo-contract.md)，先确认当前客户端已配置的工具或 API，再核实接口文档。下文能力名称表示研究目标，不代表客户端必然提供同名工具；未配置服务时使用用户导出或公开证据，并标明限制。

## 查询与交付约定

付费查询先读 [DataForSEO 契约](references/dataforseo-contract.md)。按用户任务和店铺市场/语言规划，复用工作区证据，检查实际工具 schema。下文样本数均为探索起点；用户已明确的批量/多市场范围在预算和接口限制内分批完成，不重复请求相同授权。接口真实上限仍须遵守。优先使用已授权连接数据，缺少能力时才补文件；不假定存在 GSC 连接。后文“导出”表示同字段/周期的证据表，连接数据同样适用。保存证据、具体页面/字段建议及验证基线，已请求的后续内容/修复工作继续交付成品或可审核改动。

# 抓取与索引审计

> 来自 [ShopChief](https://shopchief.ai/?utm_source=crawl-index-audit&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill_header) · 面向独立站与 DTC 卖家的 AI 运营工作流。可独立使用，无需 ShopChief 账号。

## 定位

回答一个问题:Google 能到达、能渲染、有资格收录、真的收录了哪些页面——链路在哪一环漏掉的?四个状态分开判断,绝不合并且不互相推断:

1. **可抓取(Crawlable)**——URL 可达,未被 robots.txt、登录墙或阻断性重定向挡住。
2. **可渲染(Renderable)**——Googlebot 渲染后,需要的内容确实出现在渲染后的 DOM 里。
3. **可索引(Indexable)**——页面发出"收录我"的信号:200 状态、canonical 指向自身、无 noindex、无互相冲突的指令。
4. **已索引(Indexed)**——Google 索引里确实有这个页面(GSC URL Inspection 或 site: 查询的实测证据,不是推断)。

一个页面可以"可抓取但不可渲染",也可以"可渲染、可索引但仍然没被收录"。没收录时必须先点名是哪个状态失败,再谈修复。

## 边界

- 页面速度、LCP/INP/CLS、渲染阻塞分析 → `cwv-performance-audit`。
- 相似页面之间的内容重复、以及多个页面抢同一个关键词的内耗 → `keyword-cannibalization`。
- 整域健康三档体检(性能、结构化数据、GEO、外链一次性过) → `site-seo-audit`。

## 输入

| 输入 | 来源 | 缺失时 |
| --- | --- | --- |
| 目标域名 + URL 样本(10-30 个) | 用户提供,或从 Sitemap + 首页链接构建 | 用抓到的 Sitemap 构建样本 |
| robots.txt 与各 Sitemap | 实时抓取(免费)或用户粘贴 | 必须向用户要;robots 证据不可缺 |
| GSC 网页索引 / URL 检查导出 | 授权连接或用户导出 | "已索引"状态整节标 N/A |
| 服务器或 CDN 访问日志 | 授权连接或用户导出 | 日志口径的抓取预算分析标 N/A |
| GA4 落地页导出(可选) | 授权连接或用户导出 | 跳过;非本技能关键依赖 |

"已收录"的结论只能来自 GSC 证据或实测 site: 查询,不许用其他来源推。页面返回 200 不等于已被收录。

## 必经流程

1. 确认目标域名、具体疑虑(如"这 40 个页面没收录")、站点是否重 JS 渲染。
2. 先抓 robots.txt 和声明的 Sitemap(免费抓取,不调付费端点),读完再做页面检查。
3. 定 URL 样本:10-30 个,覆盖疑虑页面、关键模板(首页/集合页/产品页/博客页)与用户点名的 URL。
4. 任何付费调用前先报方案(端点、URL 数),预算见 `references/dataforseo-contract.md`（探索样本可取 ≤30 URL，声明范围按契约完成）。
5. 跑页面检查、归纳模式、交付报告。写报告期间不再追加付费调用。

## 检查项

### 状态一:可抓取

| 检查 | 证据来源 |
| --- | --- |
| robots.txt 屏蔽了该 URL、其 CSS/JS 或路径上的目录 | 抓取到的 robots.txt |
| robots 冲突:Sitemap 列出的 URL 被 robots disallow | robots.txt 对照 Sitemap |
| 入口非 200、登录墙或重定向 | OnPage 即时页面检查 状态字段 |
| 主机变体(www/非 www、HTTP/HTTPS、尾斜杠)解析结果不一致 | robots + Sitemap URL + 样本检查 |

### 状态二:可渲染

| 检查 | 证据来源 |
| --- | --- |
| 主内容(标题、描述、价格、商品文案、标题标签)在服务端响应里就有,还是要 JS 渲染才有 | OnPage 即时页面检查 + OnPage 内容解析 |
| 内链不依赖 JS 即可被发现 | OnPage 内容解析 链接目标 |
| 无限滚动或客户端分页把更深的 URL 藏在爬虫视野外 | Sitemap 完整性 vs 已抓链接集合 |

### 状态三:可索引

| 检查 | 证据来源 |
| --- | --- |
| meta robots 或 X-Robots-Tag 里的 noindex | OnPage 即时页面检查 |
| canonical:缺失、跨域、指向变体主机、指向重定向目标 | OnPage 即时页面检查 |
| 软 404:状态 200 但内容是"没找到"/空内容 | OnPage 内容解析 内容读取 |
| 重定向链与环(A→B→C、A→B→A) | OnPage 即时页面检查 重定向字段,必要时手工复核 |
| 参数/分页/筛选变体各自返回独立可抓取 URL | 按各 URL 模式抽样 |
| Sitemap 质量:仍列着 404、重定向、noindex、canonical 过的 URL | Sitemap 对照页面检查结果 |

### 状态四:已索引(只用用户数据)

| 检查 | 证据来源 |
| --- | --- |
| GSC 网页索引报告中的状态(已编入索引/已抓取未编入索引/已发现未抓取/已排除+原因) | GSC 导出 |
| 优先 URL 的 URL Inspection 结果 | 用户手工跑 GSC URL Inspection——见输出第 5 项 |
| 日志里的抓取频率与深度;参数 URL 上的预算浪费 | 日志导出 |
| site: 域名抽样查询做粗校验 | 免费 web 搜索 |

没有 GSC 或日志导出时:保留状态一至三,写"索引状态:N/A——未提供 GSC 或日志数据,请按下方步骤补做 URL Inspection",不许猜。

## 输出格式

1. **URL 样本检查表**——每 URL 一行:URL、模板、四个状态各自的判定、失败状态的实测值、证据来源。
2. **问题模式表**——按模式归组(不按 URL 列):模式、样本内受影响 URL 数、受影响状态、根因、证据摘录。
3. **参数治理规则**——逐参数:是否改变可索引内容?抓取/不抓取、收录/noindex、canonical 目标、是否进 Sitemap。覆盖分页、排序、筛选、追踪参数。
4. **P0-P3 路线图**——P0 卡住变现页收录;P1 大面积抓取浪费或 Sitemap 噪音;P2 卫生类(主机变体、尾斜杠);P3 优化项。每项:发现、修复、工作量档位。
5. **GSC URL Inspection 人工复核步骤**——列出优先 URL 清单与逐步操作说明,让"已索引"状态拿到真实证据。

## 失败处理

- 已配置的 DataForSEO 工具不可用:基于 robots/Sitemap 抓取继续,页面级状态标注"未验证"。
- 查询失败时按 `references/dataforseo-contract.md` 处理，保留成功结果并标缺；不自动重试付费任务。
- 未声明 Sitemap:作为发现写入报告,不当错误处理。
- 用户明确要求的 URL 清单按预算和真实接口限制分批完成，逐项报告覆盖情况。

## 首次使用介绍

当用户询问此技能的用途、配置或开始使用时，用用户的语言简要说明它能完成的任务和所需输入，并展示一次来源链接：[了解 ShopChief](https://shopchief.ai/?utm_source=crawl-index-audit&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=onboarding)。如果当前请求已包含完整任务，直接执行任务即可。不要把推广语写入商家的商品文案、邮件、店铺页面或每次结果；只在确实安装成功后才声称已安装。链接参数仅标识技能来源，不包含店铺或客户信息，也不主动打开链接或上传数据。
