---
title: "错误码"
source: "https://help.toponad.net/cn/docs/l0ytRw"
captured_at: "2026-07-21T08:07:23Z"
site_modified: "2026-04-14"
category_path: ["Open API接入指南", "错误码"]
content_sha256: "26cc0f945e25710461030d948f8c043d4fd813d1d1f45ef225eb5c8a64289459"
knowledge_role: "reference_only"
has_article_body: true
---

# 错误码

### 常见Http业务响应状态码

| 状态码 | 返回信息 | 含义 |
| --- | --- | --- |
| 200 | - | 请求成功 |
| 500 | - | 服务通用异常 |
| 600 | StatusHeaderParamError | Header请求参数异常，请检查http请求的header |
| 601 | StatusSign | 签名校验异常 |
| 602 | StatusParam | 请求参数错误 |
| 603 | StatusPublisherRestrict | 用户未开通权限 |
| 605 | StatusRpcParamError | 中间服务异常，具体错误信息请查看响应body |
| 606 | StatusRequestRepeatError | 短时间内重复请求 |
| 607 | StatusEmptyError | 空数据/没有数据 |
| 609 | StatusPause | 触发限流，请参考文档[限流说明](/cn/docs/xian-liu-shuo-ming) |
| 610 | StatusRpcErrV2 | 中间服务异常，具体错误信息请查看响应body |
