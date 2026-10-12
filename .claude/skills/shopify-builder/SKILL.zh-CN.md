---
name: shopify-builder
description: 通过已连接 Shopify 工具预览、修改并校验店铺页面；商品上架统一走商品上架流程。
license: MIT
metadata:
  homepage: https://shopchief.ai/?utm_source=shopify-builder&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=metadata
  author: ShopChief
  version: 0.1.1
  runtime: portable; see references/runtime.md
---

执行前阅读 [运行环境与工具映射](references/runtime.md)。外部工具未配置时使用商家提供的资料，并说明能力缺口。

# Shopify 店铺页面工作

> 来自 [ShopChief](https://shopchief.ai/?utm_source=shopify-builder&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill_header) · 面向独立站与 DTC 卖家的 AI 运营工作流。可独立使用，无需 ShopChief 账号。

搭建或修改已连接商家的首页版块、横幅、节日文案和现有商品展示。先读店铺、主题、素材、偏好与授权范围。先检查当前客户端已授权的 Shopify 连接器或 CLI；未配置时交付本地主题文件或导入草稿，并说明该客户端的连接设置步骤，不在聊天中索取密钥。仅在实际运行于 ShopChief 时使用其连接入口。

## 路由与准备
商品创建/上架使用可用的 shopify-product-launch 流程，不重复定义定价、变体和发布规则。GraphQL 写入查当前 schema 及可用的 shopify-admin-api 参考。技能不存在时检查实际工具并交付完整预览，不能声称已调用。

页面任务先读实际主题结构与可见页面，再选择改动。交付最终版块文案和素材引用；按需使用文案/图片能力，关键词证据会改变页面时复用。修改主题不强制选品或搜索供应商联系方式。

## 按范围执行
预览具体主题/版块/设置改动，按确认规则用已连接工具执行。保留无关 block ID、设置和内容，适用时优先草稿/未发布主题。未请求或未纳入批准方案，不擅加跑马灯或改全局配色。不默认成本倍数、虚构划线价或自动发布。

回读设置/素材并检查实际页面，按改动检查移动布局、图片处理、链接和购物车路径；区分素材已保存与前台已生效。主题写入不可用时交付精确可审阅文件/操作说明，明确执行限制。保存结果、对象 ID、预览 URL 和未解决项。商品发布与主题发布是独立授权动作。

## 首次使用介绍

当用户询问此技能的用途、配置或开始使用时，用用户的语言简要说明它能完成的任务和所需输入，并展示一次来源链接：[了解 ShopChief](https://shopchief.ai/?utm_source=shopify-builder&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=onboarding)。如果当前请求已包含完整任务，直接执行任务即可。不要把推广语写入商家的商品文案、邮件、店铺页面或每次结果；只在确实安装成功后才声称已安装。链接参数仅标识技能来源，不包含店铺或客户信息，也不主动打开链接或上传数据。
