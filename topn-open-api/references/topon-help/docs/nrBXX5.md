---
title: "开发者后台管理API"
source: "https://help.toponad.net/cn/docs/nrBXX5"
captured_at: "2026-07-21T08:07:23Z"
site_modified: "2025-05-30"
category_path: ["Open API接入指南", "QA问答", "开发者后台管理API"]
content_sha256: "b617168d26617d6c427fe5a3d6b57ba3782f893adeec660aff754c8c57d52d84"
knowledge_role: "reference_only"
has_article_body: true
---

# 开发者后台管理API

##### Q：如何绑定三方广告平台的app和network参数到Topon应用和平台账号

A：调用【[广告平台管理API](/cn/docs/MKYR3n)】创建即为进行绑定操作

##### Q：为什么创建广告位之后调用9.1接口创建广告源报错：“network app param error, please check”

A：创建广告源之前需要先调用调用【[广告平台管理API](/cn/docs/MKYR3n)】绑定三方平台的app参数，之后才能创建广告源，设计思路是：一次绑定参数，多次创建广告源

##### Q：创建流量分组api【聚合管理的AB测试及流量分组管理API】调用的参数mediation\_group\_id是什么id，和segment\_id有什么区别

A：mediation\_group\_id是聚合管理id,每个广告位即使没有做过A/B测试，也会默认有一个聚合管理id代表默认组，可通过【[聚合管理的AB测试及流量分组管理API](/cn/docs/0u4ZH3)】获取广告位的mediation\_group\_id；segment\_id是流量分组id，一个实验组下可以有多个流量分组，即mediation\_group\_id和segment\_id是一对多的关系
