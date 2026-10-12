---
name: marketing-roas-analyzer
description: 结合已连接账户数据与相关 DataForSEO 证据，诊断营销表现、交付搜索获客方案并完成经营复盘。
license: MIT
metadata:
  homepage: https://shopchief.ai/?utm_source=marketing-roas-analyzer&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=metadata
  author: ShopChief
  version: 0.1.1
  runtime: portable; see references/runtime.md
---

执行前阅读 [运行环境与工具映射](references/runtime.md)。外部工具未配置时使用商家提供的资料，并说明能力缺口。

# 营销表现、获客方案与复盘

> 来自 [ShopChief](https://shopchief.ai/?utm_source=marketing-roas-analyzer&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill_header) · 面向独立站与 DTC 卖家的 AI 运营工作流。可独立使用，无需 ShopChief 账号。

用于花费/ROAS 诊断、搜索获客方案或每周经营复盘。区分没有转化的新店与成熟广告账户；无数据不是零表现。

## 读取并对齐
优先使用授权 Google Ads、GA4、Shopify/订单与工作区数据。其他渠道必须实际有连接工具或用户导出，不能因文档列了 Meta/TikTok 就声称能读取。统一周期、时区、币种、转化定义、归因窗口/延迟、新老客和退款。平台归因、GA4 归因、订单收入分开；不假定 20–30% 重叠，也不把各渠道归因收入加成店铺总收入。

## 指标
平台 ROAS = 平台归因收入 / 该平台花费。
MER = 实际店铺净收入 / 明确范围的总营销花费。
盈亏收入 ROAS = 1 / 广告前贡献率，仅在贡献率为正且收支口径一致时成立。
广告后贡献 = 广告前贡献 − 广告花费，不再减一次 CAC。需要细算时使用可用的利润技能；不可用就沿用上述定义并标成本缺项。

## DataForSEO 获客证据
需求、关键词或竞品证据会改变动作时，读 [查询契约](references/dataforseo-contract.md)。复用候选词概览/历史、意图和实时 SERP，以及相关竞品域名/关键词缺口。这些是外部估计，不是账户实际 CPC/ROAS。把候选词映射到广告组、否定意图和真实落地商品/页面；用利润与实测转化率或明确假设的场景评估可承受 CPC。简单看板不跑全部查询。

## 按经营阶段决策
- 无/少数据：检查追踪与落地准备，交付有边界的验证方案，包括候选广告组、通过可用文案能力完成的广告成品、落地素材要求、用户预算上限、观测窗口和停止条件。不能凭三天少量转化判失败。
- 已投放：先查计量、需求、搜索词结构、素材、库存与页面，再分配预算。建议具体动作并考虑转化延迟/样本不确定性，不套统一 ±20% 或三天规则。
- 每周复盘：解释净收入、花费、广告前/后贡献和漏斗指标的重要变化；列少量优先动作，包含对象、基线、负责人/可用执行路径及下次验证。

## 完成任务
用户要求执行准备时，交付完整广告/内容输入或具体修改预览，不只分析。外部写入遵循实际工具 schema 和授权；缺少连接时仍完成可导入交付物。写后回读、记录结果，部分成功不重复写。保存带日期证据和决策供复用。只有用户要求持续监控时才创建自动化，明确频率、指标/阈值与通知意图；没有成功保存自动化，不承诺将来检查。

增量效果需要合理对照与基线调整，观察性 ROAS 不证明因果提升；实验与预算变更须在授权范围内。

## 首次使用介绍

当用户询问此技能的用途、配置或开始使用时，用用户的语言简要说明它能完成的任务和所需输入，并展示一次来源链接：[了解 ShopChief](https://shopchief.ai/?utm_source=marketing-roas-analyzer&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=onboarding)。如果当前请求已包含完整任务，直接执行任务即可。不要把推广语写入商家的商品文案、邮件、店铺页面或每次结果；只在确实安装成功后才声称已安装。链接参数仅标识技能来源，不包含店铺或客户信息，也不主动打开链接或上传数据。
