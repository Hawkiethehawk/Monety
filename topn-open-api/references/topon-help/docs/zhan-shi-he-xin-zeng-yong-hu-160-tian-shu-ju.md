---
title: "展示和新增用户（1-60天数据）"
source: "https://help.toponad.net/cn/docs/zhan-shi-he-xin-zeng-yong-hu-160-tian-shu-ju"
captured_at: "2026-07-21T08:07:23Z"
site_modified: "2025-05-30"
category_path: ["Open API接入指南", "数据报表API", "留存价值报表", "展示和新增用户（1-60天数据）"]
content_sha256: "185eb59a49a8ca2530f12b7cf4ebef4dd82e88e737fa6f274b189221c4b95e1b"
knowledge_role: "reference_only"
has_article_body: true
---

# 展示和新增用户（1-60天数据）

### 注意：接入Api前请先熟悉api签名机制（参考[接口鉴权说明](/cn/docs/9NzgWP)）, 即Api请求样例中的一些http请求头的来源

### 使用注意：

1.报表延迟一天，建议当天晚上10点左右再拉一次昨天数据（数据可能会持续更新），正常情况此时数据是完整的

说明：

对应后台留存价值报表的展示模块，同时支持查询新增用户数

![](https://cdn-customer.helplook.net/_hl/load-img.DSGdRIBO.png)

### 1 请求URL

[https://api.toponad.net/v3/impnewuserreport](https://openapi.toponad.com/v3/impnewuserreport)

### 2 请求方式

POST

### 3 请求参数

| 字段 | 类型 | 是否必传 | 备注 | 样例 |
| --- | --- | --- | --- | --- |
| start\_date | Int | Y | 开始日期，格式：YYYYmmdd，支持时间必须大于20180101 | 20190501 |
| end\_date | Int | Y | 结束日期，格式：YYYYmmdd，支持时间必须大于20180101 | 20190506 |
| app\_id\_list | Array[String] | Y | 开发者后台的应用ID列表，暂时必须且只能传一个 | [“a600e6fbeac98c”]， |
| placement\_id\_list | Array[String] | N | 开发者后台的广告位ID列表，不传默认开发者的全部广告位 | [“b600e6fbeac98c”]， |
| geo\_short\_list | Array[String] | N | 国家短码列表，不传默认所有国家 | [“US”,"CN"] |
| channel\_list | Array[String] | N | 渠道列表，不传默认所有渠道 | [“haoyou”] |
| time\_zone | String | Y | 时区，枚举值：UTC-8、UTC+8、UTC+0 | “UTC-8” |
| start | Int | N | 偏移数，代表从第几条数据开始，默认为0 | 0 |
| limit | Int | N | 每次拉取数据的最大条数，默认是1000，可选[1,1000] | 不传默认1000，最大1000 |
| group\_by | Array[String] | N | group by 维度，不传时默认date\_time，支持的维度说明  date\_time（日期，默认值），  app\_id（应用），  placement\_id（广告位），  geo\_short（地区短码），  channel（渠道）， | ["date\_time"] |

### 4 返回参数

| 字段 | 类型 | 是否必传 | 备注 |
| --- | --- | --- | --- |
| records | Array[Object] | N | 记录，对象数组每个record结构见下面records元素结构，无数据时为空 |
| count | Int | N | 总条数，无数据时为空 |

**records元素结构如下：**

| 字段名 | 类型 | 是否必传 | 备注 |
| --- | --- | --- | --- |
| date\_time | Int | N | 日期，格式：YYYYmmdd。group\_by有选date\_time才有返回 |
| app\_id | String | N | 开发者后台的应用ID，group\_by有选app\_id维度时才返回 |
| app\_name | String | N | 应用名称，group\_by有选app\_id维度时才返回 |
| placement\_id | String | N | 开发者后台的广告位ID，group\_by有选placement\_id维度时才返回 |
| placement\_name | String | N | 广告位名称，group\_by有选placement\_id维度时才返回 |
| geo\_short | String | N | 国家码，group\_by有选geo\_short维度时才有返回 |
| channel | String | N | 渠道，group\_by有选channel才有返回 |
| new\_user | Int | Y | 新增用户数 |
| impression\_1 | String | Y | 第1天用户价值广告位的展示/新增用户 注意：开发者后台的是当天总展示数并且每天累加前一天，api返回的是新用户平均展示数，例如：  impression\_1\*new\_user=后台的imp0, impression\_2\*new\_user=后台的(imp1-imp0), |
| ... | String | Y | 第2到第59天用户价值广告位的展示/新增用户 |
| impression\_60 | String | Y | 第60天用户价值广告位的展示/新增用户 |

### 5 样例

请求样例：

```
curl --location --request POST 'https://api.toponad.net/v3/impnewuserreport' \
--header 'X-Up-Key: 877f8ae9c6e9ca82c0==5b5fff594c373axxx' \
--header 'X-Up-Signature: CE12B506DBCD868C2C6F09E08C139CBC' \
--header 'X-Up-Timestamp: 1626161553000' \
--header 'Content-Type: application/json' \
--data-raw '{
    "start_date":20211203,
    "end_date":20211216,
    "timezone_api":"UTC-8",
    "offset":0,
    "app_id_list": ["a5df88b5140222"],
    "placement_id_list": ["b5df88bc03222c"],
    "limit":1,
    "group_by": ["date_time"]
}'
```

返回样例：

```
{
    "count": 14,
    "records": [
        {
            "date_time": 20211203,
            "new_user": 12000,
            "impression_1": "2.612",
            "impression_2": "1.5897",
            "impression_3": "0.7926",
            "impression_4": "0.3768",
            "impression_5": "0.276",
            "impression_6": "0.227",
            "impression_7": "0.1569",
            "impression_8": "0.159",
            "impression_9": "0.1974",
            "impression_10": "0.1485",
            "impression_11": "0.086",
            "impression_12": "0.073",
            "impression_13": "0.0813",
            "impression_14": "0.0541",
            "impression_15": "0.0749",
            "impression_16": "0",
            "impression_17": "0",
            "impression_18": "0",
            "impression_19": "0",
            "impression_20": "0",
            "impression_21": "0",
            "impression_22": "0",
            "impression_23": "0",
            "impression_24": "0",
            "impression_25": "0",
            "impression_26": "0",
            "impression_27": "0",
            "impression_28": "0",
            "impression_29": "0",
            "impression_30": "0",
            "impression_31": "0",
            "impression_32": "0",
            "impression_33": "0",
            "impression_34": "0",
            "impression_35": "0",
            "impression_36": "0",
            "impression_37": "0",
            "impression_38": "0",
            "impression_39": "0",
            "impression_40": "0",
            "impression_41": "0",
            "impression_42": "0",
            "impression_43": "0",
            "impression_44": "0",
            "impression_45": "0",
            "impression_46": "0",
            "impression_47": "0",
            "impression_48": "0",
            "impression_49": "0",
            "impression_50": "0",
            "impression_51": "0",
            "impression_52": "0",
            "impression_53": "0",
            "impression_54": "0",
            "impression_55": "0",
            "impression_56": "0",
            "impression_57": "0",
            "impression_58": "0",
            "impression_59": "0",
            "impression_60": "0"
        }
    ]
}
```

##
