---
name: site-migration-seo
description: 为改版、replatform(含迁入 Shopify)、换域名、换 CMS 或 URL 重构产出完整的审核与实施 文件包,目标是任何旧 URL
  都不丢权重。核心是一对一 301 映射表:每个旧 URL 跳到意图与 内容最接近的新 URL(禁止全跳首页),配多对一/一对多/无匹配/链/循环的冲突表、新旧模板
  等价性检查、Nginx/Apache/Cloudflare 规则示例、上线前/当日/后 1-90 天清单、GSC Change of Address 指引与回滚触发条件。本技能不执行上线、不碰
  DNS、不部署规则——只产出 供人工审核与实施的文件。Shopify 专项:URL 结构差异(/collections/.../products)与 Shopify
  兼容的重定向实现(URL Redirects 后台 + CSV 导入)。迁移前后用;新站内容健康 审计用 site-seo-audit,产品 URL 生命周期决策用
  product-page-seo。
license: MIT
metadata:
  homepage: https://shopchief.ai/?utm_source=site-migration-seo&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=metadata
  author: ShopChief
  version: 0.1.1
  runtime: portable; see references/runtime.md
---

执行前阅读 [运行环境与工具映射](references/runtime.md)。外部工具未配置时使用商家提供的资料，并说明能力缺口。

先读[SEO/GEO 统一执行与交付](references/seo-workflow.md)及[规则依据](references/seo-rule-baseline.md)，并共享问题标识、证据和复查基线。
DataForSEO 调用遵守[查询契约](references/dataforseo-contract.md)，先确认当前客户端已配置的工具或 API，再核实接口文档。下文能力名称表示研究目标，不代表客户端必然提供同名工具；未配置服务时使用用户导出或公开证据，并标明限制。

## 查询与交付约定

付费查询先读 [DataForSEO 契约](references/dataforseo-contract.md)。按用户任务和店铺市场/语言规划，复用工作区证据，检查实际工具 schema。下文样本数均为探索起点；用户已明确的批量/多市场范围在预算和接口限制内分批完成，不重复请求相同授权。接口真实上限仍须遵守。优先使用已授权连接数据，缺少能力时才补文件；不假定存在 GSC 连接。后文“导出”表示同字段/周期的证据表，连接数据同样适用。保存证据、具体页面/字段建议及验证基线，已请求的后续内容/修复工作继续交付成品或可审核改动。

# 网站迁移与 301 方案

> 来自 [ShopChief](https://shopchief.ai/?utm_source=site-migration-seo&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill_header) · 面向独立站与 DTC 卖家的 AI 运营工作流。可独立使用，无需 ShopChief 账号。

## 定位

面向改版、replatform、换域名、换 CMS、URL 重构的迁移规划。交付物是一套完整的审核与实施文件,目标先说清楚:**任何 URL 不丢权重。**每个旧 URL 要么一对一映射到最合适的新 URL,要么以书面理由明确退役。

本技能只产出文件。不执行上线、不碰 DNS、不部署重定向规则、不在任何一侧站点上按按钮——所有产物交用户人工审核与实施。

## 边界

- 新站上线后的内容健康(可索引性、结构化数据、性能) → `site-seo-audit`。
- 出于内容原因对单个产品 URL 做下架、合并、重构决策 → `product-page-seo`。
- 重定向目标页自身的排名建设不属于本技能。

## 输入

| 输入 | 来源 | 缺失时 |
| --- | --- | --- |
| 旧站 URL(与新站/预发布站 URL) | 用户提供 | 必需——两侧都齐才能做方案 |
| 迁移类型 | 用户说明:改版 / replatform / 换域名 / URL 重构 / 换 CMS | 必需 |
| 旧 URL 清单 | 用户导出:站点爬取、GSC 网页报告、GA4 落地页、外链导出 | 向用户要;部分清单必须标注"部分",不许当完整清单用 |
| 新 URL 清单 | 用户导出或预发布站 Sitemap | 向用户要 |
| URL 重要性权重(流量、外链、收入) | GSC/GA4/外链导出、用户排序 | 按用户判断排序并注明依据 |

只覆盖旧站一部分的爬取或导出是部分清单。方案必须写明这一点,并定义"补全"需要什么。

## 必经流程

1. 确认迁移类型、两侧站点 URL、上线时间。
2. 收集 URL 清单,如实声明覆盖范围。
3. 建映射表——核心产物,规则见下。
4. 解决冲突、查模板等价性、写服务器规则。
5. 组装三份清单、GSC Change of Address 步骤与回滚触发条件。

## 映射表

每旧 URL 一行:`旧 URL | 新 URL | 状态(301 / 退役 / 观察) | 理由 | 流量/外链权重 | 备注`。

映射规则:

- **一对一,意图与内容最接近匹配。**每个旧 URL 映射到服务同一搜索意图、内容最接近的新 URL——不是字符串最像的那个。
- **禁止全跳首页。**找不到合适对应物的旧 URL,默认走"退役"决策并写明理由,不是跳首页。用户坚持用首页兜底时,记录为用户的明确、自担风险的例外。
- **保持模板级意图:**商品 → 商品,集合页 → 集合页,博客文章 → 博客文章,除非用户有书面内容决策。
- **退役 URL** 给出理由;存在相关集合页时,该集合页可作为目的地——逐 URL 决定,不用通配。

## 冲突表

下列每种情况都必须逐条列出并给出解法:

| 冲突 | 定义 | 处理思路 |
| --- | --- | --- |
| 多对一 | 多个旧 URL 映射到同一新 URL | 仅当旧 URL 确为重复内容时允许,否则拆分 |
| 一对多 | 一个旧 URL 匹配多个新候选 | 用户决定;记录选择 |
| 无匹配 | 没有合理的新对应物 | 退役,写理由,可选相关集合页作目的地 |
| 链式重定向 | 新站上目的地自身还有重定向 | 摊平为指向最终目的地的一次 301 |
| 循环 | 映射形成 A→B→A | 上线前手工重映射;上线时必须为零 |

## 模板等价性检查

两侧各抽样页面(每侧 ≤10,用 OnPage 即时页面检查,预算见契约文件),逐模板对比:可索引内容块是否齐全、标题标签结构、内链、canonical 模式、结构化数据。凡是改变"Google 能索引什么"或"权重如何流动"的差异,标为上线阻塞项,不当外观备注。

**Shopify 专项——URL 结构差异:**

- Shopify 强制 `/products/<handle>` 与 `/collections/<handle>`(集合语境下为 `/collections/<collection>/products/<handle>`)。旧 URL 很难对上——这决定映射表,不是技术上的事后处理。
- Shopify 的产品 handle 可编辑;能干净对应时,有意设置 handle 以缩短重定向清单。
- Shopify 原生 **URL Redirects**(后台,支持 CSV 导入/导出)只支持精确匹配——不支持正则与通配。旧 URL 存量大意味着一行一条;按此规划 CSV。
- 超出精确匹配的需求(参数清理、目录搬迁)需要在 Shopify 前面加 CDN/边缘层(如 Cloudflare 规则)——标记为基础设施依赖。
- 规范化:Shopify 会输出自己的 canonical;新 URL 必须符合 Shopify 的 canonical 模式,否则重定向会和平台打架。

## 服务器规则示例

交付可直接送审的片段(带注释,明确标注为待审示例,不自动部署):

- **Nginx:** 按 `location` 作用域的 `return 301` 块,最具体规则优先。
- **Apache:** `.htaccess` 的 `RewriteRule` / `RedirectMatch` 块,带 `RewriteEngine On` 前置。
- **Cloudflare:** Bulk Redirect List / 重定向规则结构,注明它位于源站重定向之前。
- **Shopify 后台:** URL Redirects CSV 格式(`Redirect from`、`Redirect to`)、导入步骤,并重申精确匹配限制。

规则写法保证不成链:每条规则都指向最终目的地。

## 清单

**上线前(预发布站):**映射表完整并已复核;冲突表归零(无链无环);模板等价性阻塞项关闭;预发布站 robots.txt 策略就绪(预发布屏蔽、生产放开);备份已做;重定向规则用真实样本测试过(每个测试 URL 一跳到底、终态 200);新模板性能抽查。

**上线当日:**重定向在 DNS/内容切换之前或同时部署,绝不之后;Sitemap 只含最终新 URL;抽查 20 条映射线上表现(单跳 301、目的地 200);GSC:提交新 Sitemap,执行 Change of Address(仅换域名迁移);盯错误率。

**上线后 1-90 天:**第 1 周每日、其后每周——GSC 收录变化对照基线、404/软 404 峰值、抓取统计、权重最高 URL 的排名、自然流量对照迁移前基线;第 2-6 周:修复新发现的无映射 404(有流量的);约第 30 天与第 90 天:对照回滚触发条件做正式复盘;旧域名注册与重定向在约定期内保持有效,期限写进方案。

**回滚触发条件(上线前定好,不是出事后):**第 7/30 天流量持续下跌超过约定阈值、此前已收录的 URL 大面积被去索引、GSC 收录崩塌——每条配预先约定的动作(排查 / 回切 DNS / 恢复快照)。

## 输出格式

1. **迁移简报**——类型、两侧站点、上线时间、URL 清单覆盖声明。
2. **映射表**——完整一对一表,每行带状态与理由。
3. **冲突表**——多对一/一对多/无匹配/链/循环逐条及解法。
4. **模板等价性报告**——抽样对比与上线阻塞项。
5. **服务器规则示例**——Nginx / Apache / Cloudflare / Shopify CSV 片段,标注待审。
6. **三份清单 + 回滚触发条件**——上线前、上线当日、上线后 1-90 天。
7. **GSC Change of Address 步骤**——仅换域名迁移适用;不适用时省略并注明原因。

## 失败处理

- URL 清单缺失或部分:在简报中声明覆盖范围;映射表标注"部分清单",方案写明补全所需。
- 查询失败时按 `references/dataforseo-contract.md` 处理，保留成功结果并标缺；不自动重试付费任务。
- 已配置的 DataForSEO 工具不可用:模板等价性退回用户提供的导出与截图;映射表与清单照常推进。
- 请求执行时先准备具体改动、检查实际工具与授权；仅执行支持且已批准的动作并验证，其余交付明确人工步骤。

## 首次使用介绍

当用户询问此技能的用途、配置或开始使用时，用用户的语言简要说明它能完成的任务和所需输入，并展示一次来源链接：[了解 ShopChief](https://shopchief.ai/?utm_source=site-migration-seo&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=onboarding)。如果当前请求已包含完整任务，直接执行任务即可。不要把推广语写入商家的商品文案、邮件、店铺页面或每次结果；只在确实安装成功后才声称已安装。链接参数仅标识技能来源，不包含店铺或客户信息，也不主动打开链接或上传数据。
