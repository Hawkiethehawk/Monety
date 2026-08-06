---
title: "留存（2-60天数据）"
source: "https://help.toponad.net/cn/docs/liu-cun-260-tian-shu-ju"
captured_at: "2026-07-21T08:07:23Z"
site_modified: "2025-08-15"
category_path: ["Open API接入指南", "数据报表API", "留存价值报表", "留存（2-60天数据）"]
content_sha256: "0275fefe1a73a58881111887a7d0dca16c8bb013544990349bae2d84e4810660"
knowledge_role: "reference_only"
has_article_body: true
---

# 留存（2-60天数据）

### 注意：接入Api前请先熟悉api签名机制（参考[接口鉴权说明](/cn/docs/9NzgWP)）, 即Api请求样例中的一些http请求头的来源

### 使用注意：

1.最新只能查询今天往前推1天的数据

2.报表涉及到三方数据，建议晚上10点左右再拉一次昨天数据（三方数据可能会持续更新），正常情况此时数据是完整的

说明：

对应后台留存价值报表的留存模块

![](https://cdn-customer.helplook.net/_hl/load-img.DSGdRIBO.png)

### 1 请求URL

[https://api.toponad.net/v3/retentionreport](https://openapi.toponad.com/v3/retentionreport)

### 2 请求方式

POST

### 3 请求参数

| 字段 | 类型 | 是否必传 | 备注 | 样例 |
| --- | --- | --- | --- | --- |
| start\_date | Int | Y | 开始日期，格式：YYYYmmdd | 20190501 |
| end\_date | Int | Y | 结束日期，格式：YYYYmmdd | 20190506 |
| appid\_list | Array[String] | N | 开发者后台的应用ID列表，不传默认开发者的全部app | [“a600e6fbeac98c”]， |
| area\_list | Array[String] | N | 国家短码列表，不传默认所有国家 | [“US”,"CN"] |
| channel\_list | Array[String] | N | 渠道列表，不传默认所有渠道 | [“haoyou”] |
| time\_zone | String | N | 时区，枚举值：UTC-8、UTC+8、UTC+0，不传则默认使用开发者账号时区 | “UTC-8” |
| start | Int | Y | 偏移数，代表从第几条数据开始，默认为0 | 0 |
| limit | Int | Y | 每次拉取数据的最大条数，默认是1000，可选[1,1000] | 不传默认1000，最大1000 |
| metric | Array[String] | Y | 请求的指标，其中retention\_day\_xx 代表留存人数，不再是比例：  all（2-60天用户留存）， retention\_day\_2（第2天用户留存），  ... retention\_day\_60（第60天用户留存）， | ["retention\_day\_11","retention\_day\_12","retention\_day\_13"] |
| group\_by | Array[String] | Y | group by 维度，默认date和app维度固定存在，仅iOS应用支持device维度，如果开发者同时传了iOS和安卓应用，那么只返回iOS应用的数据：  date（日期，默认值），  app（应用）， area（地区）， channel（渠道），  device（设备类型）， | ["date","app","area","channel"] |

### 4 返回参数

| 字段 | 类型 | 是否必传 | 备注 |
| --- | --- | --- | --- |
| records | Array[Object] | Y | 记录，对象数组每个record结构见下面records元素结构 |
| count | Int | Y | 总条数 |
| time\_zone | String | Y | 时区，枚举值：UTC-8、UTC+8、UTC+0 |

**records元素结构如下：**

| 字段名 | 类型 | 是否必传 | 备注 |
| --- | --- | --- | --- |
| app | Object | Y | 应用信息 |
| app.id | String | Y | 开发者后台的应用ID |
| app.name | String | Y | 应用名称 |
| app.platform | Int | Y | 应用的系统平台 |
| date | Int | Y | 日期 |
| area | String | N | 国家码。group\_by有选area维度时才有返回 |
| channel | String | N | 渠道。group\_by有选channel才有返回 |
| device | String | N | 设备类型。group\_by有选device才有返回 |
| new\_user | Int | Y | 新增用户 |
| retention\_day\_2 | Float | Y | 第2天用户价值 |
| ... | Float | Y | 第3到第59天用户价值 |
| retention\_day\_60 | Float | Y | 第60天用户价值 |

### 备注只能查询今天往前推1天的数据

### 5 样例

请求样例：

```
curl --location --request POST 'https://api.toponad.net/v3/retentionreport' \
--header 'X-Up-Key: 877f8ae9c6e9ca82c0==5b5fff594c373axxx' \
--header 'X-Up-Signature: CE12B506DBCD868C2C6F09E08C139CBC' \
--header 'X-Up-Timestamp: 1626161553000' \
--header 'Content-Type: application/json' \
--data-raw '{
    "start_date": 20200301,
    "end_date": 20200301,
    "appid_list":["a5c41a9ed1679c"],
    "group_by":["date","area"],
    "start": 0,
    "limit": 30,
    "metric": ["all"]
}'
```

返回样例：

```
{
    "records": [
        {
            "app": {
                "app_id": "a6012251c3dfxx",
                "name": "一群小辣鸡",
                "platform": 1
            },
            "date": 20200424,
            "new_user": 7036,
            "retention_day_10": 32,
            "retention_day_11": 20,
            "retention_day_12": 21,
            "retention_day_13": 19,
            "retention_day_14": 0,
            "retention_day_15": 0,
            "retention_day_16": 0,
            "retention_day_17": 0,
            "retention_day_18": 0,
            "retention_day_19": 0,
            "retention_day_2": 297,
            "retention_day_20": 0,
            "retention_day_21": 0,
            "retention_day_22": 0,
            "retention_day_23": 0,
            "retention_day_24": 0,
            "retention_day_25": 0,
            "retention_day_26": 0,
            "retention_day_27": 0,
            "retention_day_28": 0,
            "retention_day_29": 0,
            "retention_day_3": 169,
            "retention_day_30": 0,
            "retention_day_31": 0,
            "retention_day_32": 0,
            "retention_day_33": 0,
            "retention_day_34": 0,
            "retention_day_35": 0,
            "retention_day_36": 0,
            "retention_day_37": 0,
            "retention_day_38": 0,
            "retention_day_39": 0,
            "retention_day_4": 104,
            "retention_day_40": 0,
            "retention_day_41": 0,
            "retention_day_42": 0,
            "retention_day_43": 0,
            "retention_day_44": 0,
            "retention_day_45": 0,
            "retention_day_46": 0,
            "retention_day_47": 0,
            "retention_day_48": 0,
            "retention_day_49": 0,
            "retention_day_5": 75,
            "retention_day_50": 0,
            "retention_day_51": 0,
            "retention_day_52": 0,
            "retention_day_53": 0,
            "retention_day_54": 0,
            "retention_day_55": 0,
            "retention_day_56": 0,
            "retention_day_57": 0,
            "retention_day_58": 0,
            "retention_day_59": 0,
            "retention_day_6": 50,
            "retention_day_60": 0,
            "retention_day_7": 45,
            "retention_day_8": 35,
            "retention_day_9": 32
        }
    ],
    "time_zone": "",
    "count": 128
}
```

##
