---
title: "概述"
source: "https://help.toponad.net/cn/docs/dHqDSB"
captured_at: "2026-07-21T08:07:23Z"
site_modified: "2025-05-30"
category_path: ["Open API接入指南", "概述"]
content_sha256: "3a443b11fb52d8ed1f2539bbedb7ef8fb9116f203054d8d2b85fcb83b859b867"
knowledge_role: "reference_only"
has_article_body: true
---

# 概述

为提高合作伙伴的变现效率，TopOn平台专门提供了对接开发者中台的相关OpenAPI接口：**开发者后台管理API、数据报表查询API、设备层级数据报告API。**欢迎使用OpenAPI接口，谢谢！

# 1. TopOn OpenAPI接口功能介绍

1、TopOn OpenAPI提供以下功能：

| OpenAPI接口 | 功能介绍 | 默认开放 |
| --- | --- | --- |
| 开发者后台管理API | TopOn平台专门提供了对接开发者后台相关操作的API接口，如创建应用和广告位、调整Waterfall优先级等 | 是 |
| 数据报表查询API | TopOn平台专门提供了数据报表查询的API接口，可查询综合报表、LTV&留存报表等数据 | 是 |
| 设备层级数据报告API | TopOn平台专门提供了设备维度数据报告的API接口，可详细了解每个设备的变现情况，实现精细化运营。 | 需要向TopOn申请权限 |

2、为满足开发者对Open API权限授予与管理的需求，TopOn Open API的Publisher Key提供子权限功能。

| 权限类型 | 说明 |
| --- | --- |
| 全局Publisher Key | 全局Publisher Key权限可以访问此赂下全部的OpenAPI接口，包括：**开发者后台管理API、数据报表API** |
| 子权限Publisher Key | 可以针对**开发者后台管理API、数据报表API** 两个不同类型的AP**I**接口单独控制子权限。 |

开发者可以根据不同的使用场景创建不同子权限的Publisher Key，[具体流程参考](/cn/docs/XfibL9)。

# 2. TopOn OpenAPI使用流程

您可以通过表格的**快速接入导航**一栏，按照我们的基础步骤迅速地开始使用TopOn OpenAPI接口。

| 快速接入导航 | 说明 |
| --- | --- |
| 1.申请权限 | **开发者后台管理API、数据报表查询API**默认开放不需要额外申请，如果要使用**设备层级数据报告API**请联系TopOn开通 |
| 2.了解授权和风险 | 您可以了解OpenAPI的授权和风险， [查看详情](/cn/docs/CDrD9t) |
| 3.创建子权限Publisher Key | (可选)您可以根据您实际需求来创建和管理子权限的Publisher Key，[查看详情](/cn/docs/XfibL9) |
| 4.接口鉴权说明 | 您可以查看OpenAPI的接口鉴权说明， [查看详情](/cn/docs/9NzgWP) |
| 5.示例代码 | 您可以查看OpenAPI的示例代码详细说明， [查看详情](/cn/docs/l0ytRw) |
| 6.开发者后台管理API | 您可以查看开发者后台管理API详细说明， [查看详情](/cn/docs/OEAV0i) |
| 7.数据报表查询API | 您可以查看数据报表查询API详细说明， [查看详情](/cn/docs/Rf16i5) |
| 8.设备层级数据报告API | 您可以查看设备层级数据报告API详细说明， [查看详情](/cn/docs/Kam0xX) |
| 9.错误码 | 您可以查看OpenAPI的详细错误码说明， [查看详情](/cn/docs/l0ytRw) |
| 10.常见问题 | 您可以查看OpenAPI的常见问题说明， [查看详情](https://newdocs.toponad.com/docs/I1uS29) |
| 11.附录 | 您可以查看OpenAPI的附录说明，[查看详情](/cn/docs/htFjPU) |
