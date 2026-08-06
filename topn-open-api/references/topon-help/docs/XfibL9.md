---
title: "Publisher Key说明"
source: "https://help.toponad.net/cn/docs/XfibL9"
captured_at: "2026-07-21T08:07:23Z"
site_modified: "2025-05-30"
category_path: ["Open API接入指南", "Publisher Key说明"]
content_sha256: "07271f7ff49f8860137c1012b80e9f2ff1e59860b5262b5aeaaf4dd23f2c92d3"
knowledge_role: "reference_only"
has_article_body: true
---

# Publisher Key说明

为满足开发者对Open API权限授予与管理的需求，TopOn Open API的Publisher Key提供子权限功能。

| 权限类型 | 说明 |
| --- | --- |
| 全局Publisher Key | 全局Publisher Key权限可以访问此账户下全部的OpenAPI接口，包括：**开发者后台管理API、数据报表API** |
| 子权限Publisher Key | 可以针对**开发者后台管理API、数据报表API** 两个不同类型的AP**I**接口单独控制子权限。 |

开发者可以根据不同的使用场景创建不同子权限的Publisher Key。

# 1. 配置子权限Publisher Key

1、进入“**账号管理**” --> “**Key**” 页面

![文章图片](https://cdn-customer.helplook.net/_hl/load-img.DSGdRIBO.png)

2、点击“**+子权限**”进行添加及设置

![文章图片](https://cdn-customer.helplook.net/_hl/load-img.DSGdRIBO.png)

3、填写“**权限名称**”后，指定授权的应用及所授予的权限。

- **开发者管理API**，包括：**应用管理、广告位管理、广告平台管理、广告位维度的流量分组管理、聚合管理基本操作、广告源管理、A/B测试**等等。详情请参考：[开发者后台管理API](docs/VNUQG4)
- **数据报表查询API**，包括：**综合报表、用户价值1-60天报表、用户留存2-60天报表、用户价值广告位的展示、新增用户1-60天报表、Roi报表、Roi\_Ltv报表、Tk\_Hour报表**等等。数据报表查询API可以指定应用或全部应用生效。详情请参考：[数据报表查询API](docs/Eh9n46)

![文章图片](https://cdn-customer.helplook.net/_hl/load-img.DSGdRIBO.png)

4、确定保存后，生成**子权限Publisher Key**。

# 2. 常见问题答疑

### 1、子权限Publisher Key的接入方法?

答：与全局Publisher Key接入一致，接入方法可参考[OpenAPI对接文档](docs/VNUQG4)

### 2、子权限Publisher Key权限是否可以更改？

答：主账号可以根据实际情况随时更改子权限Publisher Key的授权内容，如修改授权应用及授权权限等。

### 3、子权限Publisher Key个数有限制吗？

答：每个主账号最多可建20个子权限Publisher Key。如开发者需要支持更多，可与TopOn对接人员联系。

### 4、子权限Publisher Key选择开发者后台管理API时可以指定应用吗？

答：开发者后台管理API无法指定应用，目前是全部应用生效
