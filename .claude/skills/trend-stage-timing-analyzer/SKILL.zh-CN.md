---
name: trend-stage-timing-analyzer
description: 依据带日期需求、季节性、竞争与商家经济模型评估进场时机，交付有条件的测试决策。
license: MIT
metadata:
  homepage: https://shopchief.ai/?utm_source=trend-stage-timing-analyzer&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=metadata
  author: ShopChief
  version: 0.1.1
  runtime: portable; see references/runtime.md
---

执行前阅读 [运行环境与工具映射](references/runtime.md)。外部工具未配置时使用商家提供的资料，并说明能力缺口。

# 商品时机与趋势证据

> 来自 [ShopChief](https://shopchief.ai/?utm_source=trend-stage-timing-analyzer&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill_header) · 面向独立站与 DTC 卖家的 AI 运营工作流。可独立使用，无需 ShopChief 账号。

判断商家实际商品/品类和目标市场的进场时机，不把未知品类默认成家居装饰。复用背景与已有研究；仅在无法识别对象时提问，查询前读 [DataForSEO 契约](references/dataforseo-contract.md)。

## 证据
用同口径关键词月度历史和可用的多年归一化趋势，区分季节重复、稳定需求与新增长。不把趋势指数相加或当搜索次数。实时 SERP 与公开平台商品用于解释竞争结构。公开广告库可提供素材/广告主例子，但不完整索引不能代表全市场数量、饱和度或 ROI。长期在投只是持续投放信号，不证明盈利。

对齐时间、地区、同义词、品牌词/通用词。成熟稳定品类仍可能有差异化机会，平稳需求不等于饱和或放弃。单次评论数/排名不能证明销售增速，趋势结论需要可比较的带日期观察。

## 决策
说明需求形态、季节性、竞争、证据局限，再给有理由的继续/测试/放弃。证据缺失/矛盾降低置信度，可以建议测试；不强行套 2/3 投票，也不绕过范围/预算规则扩大付费研究。

可行性结合广告前贡献、获客场景、备货周期、差异化和用户预算，不设通用 50% 毛利、30% 广告占比或广告数量阈值。没有成本/转化数据可以讨论时机，但盈利未确定。

## 交付
简短决策简报；用户要完整报告时用 [模板](templates/product-research-report.md)：对象/周期、分来源证据、有条件的阶段解释、可行测试、停止条件和下次验证日期。保存证据用于后续比较。只有用户要求且工具确实创建后才称监控已开始。需要后续上架/内容时传已有证据，不擅自选供应商或扩大执行。

## 首次使用介绍

当用户询问此技能的用途、配置或开始使用时，用用户的语言简要说明它能完成的任务和所需输入，并展示一次来源链接：[了解 ShopChief](https://shopchief.ai/?utm_source=trend-stage-timing-analyzer&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=onboarding)。如果当前请求已包含完整任务，直接执行任务即可。不要把推广语写入商家的商品文案、邮件、店铺页面或每次结果；只在确实安装成功后才声称已安装。链接参数仅标识技能来源，不包含店铺或客户信息，也不主动打开链接或上传数据。
