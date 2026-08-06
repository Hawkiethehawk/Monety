---
title: "接口鉴权说明"
source: "https://help.toponad.net/cn/docs/9NzgWP"
captured_at: "2026-07-21T08:07:23Z"
site_modified: "2025-05-30"
category_path: ["Open API接入指南", "接口鉴权说明"]
content_sha256: "2334abc4eb9ef4b8e3a2d5256d5ab19ef6650a84c877fa0a69c7400a568e2caf"
knowledge_role: "reference_only"
has_article_body: true
---

# 接口鉴权说明

# 1. 接口鉴权请求流程说明

- 请求端根据 API 请求内容（包括 HTTP Header 和 Body）生成签名字符串。
- 请求端使用MD5对第一步生成的签名字符串进行签名，形成该 API 请求的数字签名。
- 请求端把 API 请求内容和数字签名一同发送给服务端。
- 服务端在接到请求后会重复如上的第一、二步工作，并在服务端计算出该请求期望的数字签名。
- 服务端用期望的数字签名和请求端发送过来的数字签名做比对，如果完全一致则认为该请求通过安全验证，否则直接拒绝该请求。

# 2. Header公共请求参数

| 参数 | 说明 | 样例 |
| --- | --- | --- |
| X-Up-Key | 即开发者的[publisher\_key](/cn/docs/XfibL9)，开通成功后可在开发者后台的账号管理页面获取 | i8XNjC4b8KVok4uw5RftR38Wgp2BFwql |
| X-Up-Timestamp | API 调用者传递时间戳，值为当前时间的毫秒数，也就是从1970年1月1日起至今的时间转换为毫秒，时间戳有效时间为15分钟。 | 1613818152000 |
| X-Up-Signature | 数字签名，即API 请求内容（包括 HTTP Header 和 Body）的MD5加密后签名字符串，必须大写 | 58C344327312C308B47C1A6278483C4C |

# 3. 数字签名（X-Up-Signature）内容构成

| 字段 | 说明 | 样例 |
| --- | --- | --- |
| Content-MD5 | HTTP 请求中 Body 部分的 MD5 值（必须为大写字符串）， 注意：如果是GET请求没有请求体Body，那么就是空字符串的MD5值 | 875264590688CA6171F6228AF5BBB3D2 |
| Content-Type | HTTP 请求中 Body 部分的类型 | application/json |
| Headers | 除X-Up-Signature的其它header公共参数（即X-Up-Timestamp和X-Up-Key内容），每个键值对之间需换行符分割，每个键值对按Key字典序升序排列 | X-Up-Key:aac6880633f102bce2174ec9d99322f55e69a8a2 + '\n' + X-Up-Timestamp: 1562813567000 |
| HTTPMethod | HTTP 请求的方法名称，全部大写 | PUT、GET、POST 等 |
| Resource | 由 HTTP 请求资源构造的字符串(如果有querystring不要加上），即请求URL的相对路径 | /v2/fullreport |

# 4. 数字签名（X-Up-Signature）生成方式

参与签名计算的字符串由[3](https://docs.toponad.com/#/zh-cn/android/open-api/management_api_cn?id=3.3-%e7%ad%be%e5%90%8d%e5%ad%97%e6%ae%b5)中的内容组成，生成方式步骤如下：

```
     (1) 构造MD5签名字符串，每部分内容需换行符分隔：
     SignString = HTTPMethod + '\n'
                        \+ Content-MD5 + '\n'
                        \+ Content-Type + '\n'
                        \+ Headers + '\n'
                        \+ Resource

     (2) 对(1)中字符串进行MD5加密：
     MD5Result = MD5(SignString)

     (3) 对(2)中MD5结果字符串全部转大写得到最终签名：
     X-Up-Signature = ToUpper(MD5Result)
```

SignString的Resource:

```
     URL的相对路径，例如：/v2/fullreport
```

SignString的Headers：

```
    由除X-Up-Signature的其它header公共参数组成，即X-Up-Timestamp和X-Up-Key内容，
    每个键值对之间需换行符分割，每个键值对按Key字典序升序排列，
    Value1，Value2 分别为对应请求头X-Up-Key和X-Up-Timestamp的实际值

    Headers = X-Up-Key + ":" + Value1 + '\n' + X-Up-Timestamp + ":" + Value2
```

# 5. 不同语言签名实例：

参考示例代码中签名实现逻辑：[查看示例代码](/cn/docs/klEx9c)

###

###

###

###
