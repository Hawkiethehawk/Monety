---
title: "通用"
source: "https://help.toponad.net/cn/docs/l1PgZx"
captured_at: "2026-07-21T08:07:23Z"
site_modified: "2025-11-27"
category_path: ["Open API接入指南", "QA问答", "通用"]
content_sha256: "d8784719655e90e207cbf8ce8381ad75a6e8bf047961ca26d3ecd6cff9e900ec"
knowledge_role: "reference_only"
has_article_body: true
---

# 通用

##### Q：请求api报错，错误码600，错误信息：“timestamp is out”

A：这个是请求头X-Up-Timestamp的值过期，时间戳有效值是15分钟，可以检查是不是写死了时间戳或者开发者服务器时钟快了一分钟以上

##### Q：请求api报错，错误码601，错误信息：“signature failed”

A：这个是鉴权错误，请参考实例代码：[查看示例代码](/docs/klEx9c)

##### Q：请求api报错，错误码609，错误信息：“requests too frequent, please try again later”

A：请求太频繁，触发限流，请参考文档顶部限流说明

##### Q：请求api报错，错误码606，错误信息：“It has requested too many times in a short time”

A：单个开发者调用单个接口的并发请求数不允许超过1次，改为串行方式获取即可
