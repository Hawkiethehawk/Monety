---
title: "分小时报表"
source: "https://help.toponad.net/cn/docs/1frPcq"
captured_at: "2026-07-21T08:07:23Z"
site_modified: "2025-10-30"
category_path: ["Open API接入指南", "数据报表API", "分小时报表"]
content_sha256: "302df926b7c372547300f006ce50efd73eb48a94e9729fe61ceb8010c3e85c4f"
knowledge_role: "reference_only"
has_article_body: true
---

# 分小时报表

### 注意：接入Api前请先熟悉api签名机制（参考[接口鉴权说明](/cn/docs/9NzgWP)）, 即Api请求样例中的一些http请求头的来源

### 使用前说明：数据更新时间正常为5分钟更新一次

### 1 请求URL

[https://api.toponad.net/v3/report/tk\_hour](https://openapi.toponad.com/v3/report/tk_hour)

### 2 请求方式

POST

### 3 请求参数

| 字段 | 类型 | 是否必传 | 备注 | 样例 |
| --- | --- | --- | --- | --- |
| start\_date | Int | Y | 开始日期，格式：YYYYmmdd | 20190501 |
| end\_date | Int | Y | 结束日期，格式：YYYYmmdd，注意：暂时只允许查询日期跨度10天内的数据 | 20190506 |
| currency | String | Y | 币种，可选：USD，CNY |  |
| time\_zone | String | Y | 时区，枚举值：UTC-8、UTC+8、UTC+0 | “UTC-8” |
| app\_id\_list | Array[String] | N | 应用ID列表，最大查询100个 | [“a600e6fbeac98c”]， |
| placement\_id\_list | Array[String] | N | 广告位ID列表，最大查询100个 |  |
| scenario\_list | Array[String] | N | 广告场景列表，最大查询100个 |  |
| adformat\_list | Array[Int] | N | 广告样式列表，有效枚举值：  0：原生（Native）  1：激励视频（Rewarded Video）  2：横幅（Banner）  3：插屏（Interstitial）  4：开屏（Splash） |  |
| segment\_id\_list | Array[Int] | N | 流量分组ID列表，最大查询100个 |  |
| network\_id\_list | Array[Int] | N | 广告平台账号ID列表，最大查询100个 |  |
| adsource\_id\_list | Array[Int] | N | 广告源ID列表，最大查询100个 |  |
| geo\_short\_list | Array[String] | N | 国家短码列表，最大查询100个 | [“US”,"CN"] |
| sdk\_version\_list | Array[String] | N | sdk版本列表，最大查询100个 | ["5.0.0"] |
| app\_version\_list | Array[String] | N | app版本列表，最大查询100个 | ["5.0.0"] |
| platform\_list | Array[Int] | N | 系统平台列表，有效枚举值：  1：Android  2：Ios |  |
| device\_type\_list | Array[Int] | N | 设备类型列表，有效枚举值：  1：Phone  2：Pad |  |
| channel\_list | Array[String] | N | 渠道列表，最大查询100个 |  |
| start | Int | N | 偏移数，代表从第几条数据开始，默认为0 | 0 |
| limit | Int | N | 每次拉取数据的最大条数，默认是1000，最大1000，可选[1,1000] |  |

### 4 返回参数

| 字段 | 类型 | 是否必传 | 备注 |
| --- | --- | --- | --- |
| records | Array[Object] | N | 记录，对象数组每个record结构见下面records元素结构，无数据时为空 |
| count | Int | N | 总条数，无数据时为空 |

**records元素结构如下：**

| 字段名 | 类型 | 是否必传 | 备注 |
| --- | --- | --- | --- |
| date | Int | Y | 日期，格式：YYYYmmdd |
| hour | Int | Y | 小时，例如0代表：00:00~00:59 |
| loads | Int | Y | 流量请求 |
| load\_fill\_rate | Float | Y | 流量填充率 |
| request | Int | Y | 广告请求 |
| request\_fill\_rate | Float | Y | 广告填充率 |
| impression | Int | Y | 展示 |
| impression\_rate | Float | Y | 展示率 |
| click | Int | Y | 点击 |
| click\_rate | Float | Y | 点击率 |
| estimated\_revenue | Float | Y | 预估收益 |
| estimated\_revenue\_ecpm | Float | Y | 预估ecpm |
| launch | Int | Y | 启动次数 |

### 5 样例

请求样例：

```
curl --location --request POST 'https://api.toponad.net/v3/report/tk_hour' \
--header 'X-Up-Key: 877f8ae9c6e9ca82c0==5b5fff594c373axxx' \
--header 'X-Up-Signature: CE12B506DBCD868C2C6F09E08C139CBC' \
--header 'X-Up-Timestamp: 1626161553000' \
--header 'Content-Type: application/json' \
--data-raw '{
  "start_date": 20220710,
  "end_date": 20220710,
  "currency": "USD",
  "time_zone": "UTC+8",
  "limit": 100,
  "start": 0
}'
```

返回样例：

```
{
    "count": 24,
    "data": [
        {
            "date": 20220710,
            "hour": 23,
            "loads": 981116,
            "load_fill_rate": 0.5182,
            "request": 6847793,
            "request_fill_rate": 0.0781,
            "impression": 397190,
            "impression_rate": 0.7811,
            "click": 30304,
            "click_rate": 0.0762,
            "estimated_revenue": 305.84,
            "estimated_revenue_ecpm": 0.77
        },
        {
            "date": 20220710,
            "hour": 22,
            "loads": 1741902,
            "load_fill_rate": 0.5352,
            "request": 12897069,
            "request_fill_rate": 0.0756,
            "impression": 749196,
            "impression_rate": 0.8035,
            "click": 59080,
            "click_rate": 0.0788,
            "estimated_revenue": 438.3,
            "estimated_revenue_ecpm": 0.59
        },
        {
            "date": 20220710,
            "hour": 21,
            "loads": 2474725,
            "load_fill_rate": 0.5272,
            "request": 19590764,
            "request_fill_rate": 0.0718,
            "impression": 1083043,
            "impression_rate": 0.83,
            "click": 85858,
            "click_rate": 0.0792,
            "estimated_revenue": 546.69,
            "estimated_revenue_ecpm": 0.5
        },
        {
            "date": 20220710,
            "hour": 20,
            "loads": 2690416,
            "load_fill_rate": 0.5464,
            "request": 21094012,
            "request_fill_rate": 0.0727,
            "impression": 1191905,
            "impression_rate": 0.8107,
            "click": 92364,
            "click_rate": 0.0774,
            "estimated_revenue": 538.16,
            "estimated_revenue_ecpm": 0.45
        },
        {
            "date": 20220710,
            "hour": 19,
            "loads": 2437277,
            "load_fill_rate": 0.5802,
            "request": 19497452,
            "request_fill_rate": 0.0757,
            "impression": 1140467,
            "impression_rate": 0.8064,
            "click": 89656,
            "click_rate": 0.0786,
            "estimated_revenue": 495.78,
            "estimated_revenue_ecpm": 0.43
        },
        {
            "date": 20220710,
            "hour": 18,
            "loads": 2361918,
            "load_fill_rate": 0.5784,
            "request": 19140320,
            "request_fill_rate": 0.0765,
            "impression": 1123189,
            "impression_rate": 0.822,
            "click": 86457,
            "click_rate": 0.0769,
            "estimated_revenue": 511.97,
            "estimated_revenue_ecpm": 0.46
        },
        {
            "date": 20220710,
            "hour": 17,
            "loads": 2639547,
            "load_fill_rate": 0.5458,
            "request": 21465595,
            "request_fill_rate": 0.0706,
            "impression": 1169908,
            "impression_rate": 0.812,
            "click": 88987,
            "click_rate": 0.076,
            "estimated_revenue": 503,
            "estimated_revenue_ecpm": 0.43
        },
        {
            "date": 20220710,
            "hour": 16,
            "loads": 2737871,
            "load_fill_rate": 0.5582,
            "request": 22997528,
            "request_fill_rate": 0.0692,
            "impression": 1244705,
            "impression_rate": 0.8143,
            "click": 96585,
            "click_rate": 0.0775,
            "estimated_revenue": 499.22,
            "estimated_revenue_ecpm": 0.4
        },
        {
            "date": 20220710,
            "hour": 15,
            "loads": 2650874,
            "load_fill_rate": 0.5725,
            "request": 22474747,
            "request_fill_rate": 0.0704,
            "impression": 1233668,
            "impression_rate": 0.8128,
            "click": 94638,
            "click_rate": 0.0767,
            "estimated_revenue": 484.51,
            "estimated_revenue_ecpm": 0.39
        },
        {
            "date": 20220710,
            "hour": 14,
            "loads": 2677292,
            "load_fill_rate": 0.5844,
            "request": 23224731,
            "request_fill_rate": 0.0712,
            "impression": 1286505,
            "impression_rate": 0.8222,
            "click": 97836,
            "click_rate": 0.076,
            "estimated_revenue": 524.47,
            "estimated_revenue_ecpm": 0.41
        },
        {
            "date": 20220710,
            "hour": 13,
            "loads": 2836857,
            "load_fill_rate": 0.593,
            "request": 24683988,
            "request_fill_rate": 0.071,
            "impression": 1360077,
            "impression_rate": 0.8084,
            "click": 107215,
            "click_rate": 0.0788,
            "estimated_revenue": 576.13,
            "estimated_revenue_ecpm": 0.42
        },
        {
            "date": 20220710,
            "hour": 12,
            "loads": 2651097,
            "load_fill_rate": 0.587,
            "request": 23764112,
            "request_fill_rate": 0.0684,
            "impression": 1250358,
            "impression_rate": 0.8033,
            "click": 101759,
            "click_rate": 0.0813,
            "estimated_revenue": 518.37,
            "estimated_revenue_ecpm": 0.41
        },
        {
            "date": 20220710,
            "hour": 11,
            "loads": 2559570,
            "load_fill_rate": 0.5809,
            "request": 22496423,
            "request_fill_rate": 0.0692,
            "impression": 1188343,
            "impression_rate": 0.7991,
            "click": 94346,
            "click_rate": 0.0793,
            "estimated_revenue": 522.18,
            "estimated_revenue_ecpm": 0.44
        },
        {
            "date": 20220710,
            "hour": 10,
            "loads": 2296997,
            "load_fill_rate": 0.6302,
            "request": 20346177,
            "request_fill_rate": 0.0747,
            "impression": 1162600,
            "impression_rate": 0.8031,
            "click": 94472,
            "click_rate": 0.0812,
            "estimated_revenue": 499.22,
            "estimated_revenue_ecpm": 0.43
        },
        {
            "date": 20220710,
            "hour": 9,
            "loads": 1929212,
            "load_fill_rate": 0.6453,
            "request": 16688356,
            "request_fill_rate": 0.0784,
            "impression": 986177,
            "impression_rate": 0.7921,
            "click": 82161,
            "click_rate": 0.0833,
            "estimated_revenue": 432.39,
            "estimated_revenue_ecpm": 0.44
        },
        {
            "date": 20220710,
            "hour": 8,
            "loads": 1497775,
            "load_fill_rate": 0.6681,
            "request": 12605883,
            "request_fill_rate": 0.0834,
            "impression": 791331,
            "impression_rate": 0.7907,
            "click": 69715,
            "click_rate": 0.088,
            "estimated_revenue": 337.15,
            "estimated_revenue_ecpm": 0.43
        },
        {
            "date": 20220710,
            "hour": 7,
            "loads": 1019578,
            "load_fill_rate": 0.6389,
            "request": 8402268,
            "request_fill_rate": 0.0813,
            "impression": 507326,
            "impression_rate": 0.7786,
            "click": 41443,
            "click_rate": 0.0816,
            "estimated_revenue": 208.83,
            "estimated_revenue_ecpm": 0.41
        },
        {
            "date": 20220710,
            "hour": 6,
            "loads": 574317,
            "load_fill_rate": 0.5898,
            "request": 4512475,
            "request_fill_rate": 0.0788,
            "impression": 254969,
            "impression_rate": 0.7526,
            "click": 19256,
            "click_rate": 0.0755,
            "estimated_revenue": 120.18,
            "estimated_revenue_ecpm": 0.47
        },
        {
            "date": 20220710,
            "hour": 5,
            "loads": 373667,
            "load_fill_rate": 0.5228,
            "request": 2680886,
            "request_fill_rate": 0.0767,
            "impression": 141238,
            "impression_rate": 0.7228,
            "click": 10326,
            "click_rate": 0.0731,
            "estimated_revenue": 75.1,
            "estimated_revenue_ecpm": 0.53
        },
        {
            "date": 20220710,
            "hour": 4,
            "loads": 338138,
            "load_fill_rate": 0.5042,
            "request": 2281807,
            "request_fill_rate": 0.0785,
            "impression": 122038,
            "impression_rate": 0.7156,
            "click": 9068,
            "click_rate": 0.0743,
            "estimated_revenue": 67.61,
            "estimated_revenue_ecpm": 0.55
        },
        {
            "date": 20220710,
            "hour": 3,
            "loads": 372307,
            "load_fill_rate": 0.511,
            "request": 2461194,
            "request_fill_rate": 0.0815,
            "impression": 139745,
            "impression_rate": 0.7344,
            "click": 10349,
            "click_rate": 0.074,
            "estimated_revenue": 87.46,
            "estimated_revenue_ecpm": 0.63
        },
        {
            "date": 20220710,
            "hour": 2,
            "loads": 383925,
            "load_fill_rate": 0.5383,
            "request": 2461606,
            "request_fill_rate": 0.0886,
            "impression": 150527,
            "impression_rate": 0.7283,
            "click": 10960,
            "click_rate": 0.0728,
            "estimated_revenue": 118.81,
            "estimated_revenue_ecpm": 0.79
        },
        {
            "date": 20220710,
            "hour": 1,
            "loads": 395344,
            "load_fill_rate": 0.6011,
            "request": 2449041,
            "request_fill_rate": 0.1036,
            "impression": 175508,
            "impression_rate": 0.7385,
            "click": 12568,
            "click_rate": 0.0716,
            "estimated_revenue": 165.09,
            "estimated_revenue_ecpm": 0.94
        },
        {
            "date": 20220710,
            "hour": 0,
            "loads": 547474,
            "load_fill_rate": 0.6434,
            "request": 3484201,
            "request_fill_rate": 0.1075,
            "impression": 227910,
            "impression_rate": 0.6469,
            "click": 20151,
            "click_rate": 0.0884,
            "estimated_revenue": 180.42,
            "estimated_revenue_ecpm": 0.79
        }
    ]
}
```
