---
title: "LTV（1-60天数据）"
source: "https://help.toponad.net/cn/docs/LTV-160-tian-shu-ju"
captured_at: "2026-07-21T08:07:23Z"
site_modified: "2025-08-15"
category_path: ["Open API接入指南", "数据报表API", "留存价值报表", "LTV（1-60天数据）"]
content_sha256: "a7220be535210785095c522f9f6bced36d21f2702b892149b681e3a8ba8dca5f"
knowledge_role: "reference_only"
has_article_body: true
---

# LTV（1-60天数据）

说明：

对应后台留存价值报表的LTV模块，仅支持API统计数据回传

![](https://cdn-customer.helplook.net/_hl/load-img.DSGdRIBO.png)

### 注意：接入Api前请先熟悉api签名机制（参考[接口鉴权说明](/cn/docs/9NzgWP)）, 即Api请求样例中的一些http请求头的来源

### 使用注意：

1.最新只能查询今天往前推1天的数据

2.报表涉及到三方数据，建议晚上10点左右再拉一次昨天数据（三方数据可能会持续更新），正常情况此时数据是完整的

### 1 请求URL

[https://api.toponad.net/v3/ltvreport](https://openapi.toponad.com/v3/ltvreport)

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
| metric | Array[String] | Y | 请求的指标，其中ltv\_day\_xx 代表第N天所有新增用户的收益（区别后台：后台的是新增用户的平均收益，例如： ltv\_day\_1/new\_user=后台的ltv0）：  all（1-60天用户价值）， ltv\_day\_1（第1天用户价值），  ...  ltv\_day\_60（第60天用户价值）， | ["ltv\_day\_11","ltv\_day\_12","ltv\_day\_13"] |
| group\_by | Array[String] | Y | group by 维度，默认date和app维度固定存在，仅iOS应用支持device维度，如果开发者同时传了iOS和安卓应用，那么只返回iOS应用的数据：  date（日期，默认值），  app（应用），  area（地区），  channel（渠道），  device（设备类型）， | ["date","app","area","channel"] |

### 4 返回参数

| 字段 | 类型 | 是否必传 | 备注 |
| --- | --- | --- | --- |
| records | Array[Object] | Y | 记录，对象数组每个record结构见下面records元素结构 |
| count | Int | Y | 总条数 |
| time\_zone | String | Y | 时区，枚举值：UTC-8、UTC+8、UTC+0 |
| currency | String | Y | 开发者账号币种 |

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
| ltv\_day\_1 | Float | Y | 第1天用户价值 |
| ... | Float | Y | 第2到第59天用户价值 |
| ltv\_day\_60 | Float | Y | 第60天用户价值 |

> 备注只能查询今天往前推1天的数据

### 5 样例

请求样例：

```
curl --location --request POST 'https://api.toponad.net/v3/ltvreport' \
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
                "name": "分手回避",
                "platform": 2
            },
            "date": 20200424,
            "new_user": 7036,
            "ltv_day_1": 19.563598,
            "ltv_day_10": 0,
            "ltv_day_11": 0,
            "ltv_day_12": 0,
            "ltv_day_13": 0,
            "ltv_day_14": 0,
            "ltv_day_15": 0,
            "ltv_day_16": 0,
            "ltv_day_17": 0,
            "ltv_day_18": 0,
            "ltv_day_19": 0,
            "ltv_day_2": 0,
            "ltv_day_20": 0,
            "ltv_day_21": 0,
            "ltv_day_22": 0,
            "ltv_day_23": 0,
            "ltv_day_24": 0,
            "ltv_day_25": 0,
            "ltv_day_26": 0,
            "ltv_day_27": 0,
            "ltv_day_28": 0,
            "ltv_day_29": 0,
            "ltv_day_3": 0,
            "ltv_day_30": 0,
            "ltv_day_31": 0,
            "ltv_day_32": 0,
            "ltv_day_33": 0,
            "ltv_day_34": 0,
            "ltv_day_35": 0,
            "ltv_day_36": 0,
            "ltv_day_37": 0,
            "ltv_day_38": 0,
            "ltv_day_39": 0,
            "ltv_day_4": 0,
            "ltv_day_40": 0,
            "ltv_day_41": 0,
            "ltv_day_42": 0,
            "ltv_day_43": 0,
            "ltv_day_44": 0,
            "ltv_day_45": 0,
            "ltv_day_46": 0,
            "ltv_day_47": 0,
            "ltv_day_48": 0,
            "ltv_day_49": 0,
            "ltv_day_5": 0,
            "ltv_day_50": 0,
            "ltv_day_51": 0,
            "ltv_day_52": 0,
            "ltv_day_53": 0,
            "ltv_day_54": 0,
            "ltv_day_55": 0,
            "ltv_day_56": 0,
            "ltv_day_57": 0,
            "ltv_day_58": 0,
            "ltv_day_59": 0,
            "ltv_day_6": 0,
            "ltv_day_60": 0,
            "ltv_day_7": 0,
            "ltv_day_8": 0,
            "ltv_day_9": 0
        }
    ],
    "time_zone": "",
    "count": 128
}
```

##
