---
title: "美元转人民币汇率"
source: "https://help.toponad.net/cn/docs/mei-yuan-zhuan-ren-min-bi-hui-lyu"
captured_at: "2026-07-21T08:07:23Z"
site_modified: "2025-08-21"
category_path: ["Open API接入指南", "附录", "美元转人民币汇率"]
content_sha256: "6c38dd89d38b8924ce0740cdb92ccbad27d25e6db1ebb5eb4c24d9f33405ed3a"
knowledge_role: "reference_only"
has_article_body: true
---

# 美元转人民币汇率

##

## 注意：接入Api前请先熟悉api签名机制（参考[接口鉴权说明](/docs/9NzgWP)）, 即Api请求样例中的一些http请求头的来源

## 1. 获取美元转人民币汇率列表

##

#### 1.1 请求URL

<https://api.toponad.net/v1/exchange_rate/list>

#### 1.2 请求方式

GET

#### 1.3 请求参数

| 字段 | 类型 | 是否必传 | 备注 |
| --- | --- | --- | --- |
| date | Int | N | 1.传递必须是int类型，而且范围是最近30天内，格式(YMD)：20250731  2.如果不传递，则一次性返回近30天的汇率数据 |
| conversionType | Int | N | 枚举值：  1：美元转人民币（默认值）  2：人民币转美元 |

####

#### 1.4 样例

请求样例：

```
curl --location --request GET 'https://api.toponad.net/v1/exchange_rate/list?date=20250730' \
--header 'X-Up-Key: 877f8ae9c6e9ca82c0===b5fff594c373axxx' \
--header 'X-Up-Signature: CE12B506DBCD868C2C6F09E08C139CBC' \
--header 'X-Up-Timestamp: 1626056011000' \
--header 'Content-Type: application/json'
```

返回样例：

```
{
    "20250730": "6.3757"
}
```
