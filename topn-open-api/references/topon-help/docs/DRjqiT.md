---
title: "AB测试管理"
source: "https://help.toponad.net/cn/docs/DRjqiT"
captured_at: "2026-07-21T08:07:23Z"
site_modified: "2025-12-16"
category_path: ["Open API接入指南", "开发者后台管理API", "AB测试管理"]
content_sha256: "38997c23712d61c0f7715178bf69539cdaf1841c5989200eac4d305eebbb0d29"
knowledge_role: "reference_only"
has_article_body: true
---

# AB测试管理

### 注意：接入Api前请先熟悉api签名机制（参考[接口鉴权说明](/cn/docs/9NzgWP)）, 即Api请求样例中的一些http请求头的来源

## 1. 获取A/B测试列表

#### 1.1 请求URL

[https://api.toponad.net/v3/abtest](https://openapi.toponad.com/v3/abtest)

#### 1.2 请求方式

GET

#### 1.3 请求参数

| 字段 | 类型 | 是否必传 | 备注 |
| --- | --- | --- | --- |
| app\_ids | Array[String] | N | 应用ID列表，默认所有应用ID，数量最大限制为100 |
| placement\_ids | Array[String] | N | 广告位ID列表，数量最大限制为100 |
| name | String | N | A/B测试名称 |
| status | Int | N | 状态 1=已结束， 3=测试中，6=待生效 |
| start | Int | N | 起始偏移量，默认0 |
| limit | Int | N | 获取个数，默认15,最大一次性获取100 |

#### 1.4 返回参数

| 字段 | 类型 | 是否必传 | 备注 |
| --- | --- | --- | --- |
| data | Array[Object] | Y | 返回结果数据 |
| data.id | Int | Y | A/B测试的ID |
| data.app\_id | String | Y | 应用ID |
| data.name | String | Y | A/B测试的名称 |
| data.status | Int | Y | 状态 1=已结束， 3=测试中，6=待生效 |
| data.start\_time\_type | Int | Y | 开始时间的类型 1=立即生效，2=指定生效时间，3-手动 |
| data.start\_time\_timezone | Int | Y | 时区 -12~12 = 西12区 ~ 东12区。 |
| data.start\_time | Int | Y | 开始时间，时间戳。start\_time\_type=3时传0 |
| data.items | Array[Object] | Y | 实验分组 |
| data.items.id | Int | Y | 实验分组的ID |
| data.items.name | Int | Y | 实验分组的名称 |
| data.items.traffic\_variation | Int | Y | 实验分组的权重 |
| data.items.enable | Bool | Y | 实验分组启用状态 false: 停用， true：启用中 |
| data.placement\_ids | Array[String] | Y | 测试广告位 |
| data.choices | Array[Object] | Y | 从A/B实验中停掉的广告位 |
| data.choices.placement\_id | String | Y | 广告位ID |
| data.choices.item\_id | Int | Y | 停掉的广告位选择的实验分组ID |
| data.choices.item\_name | String | Y | 停掉的广告位选择的实验分组名称 |

#### 1.5 样例

请求样例：

```
curl --location --request GET 'https://api.toponad.net/v3/abtest?name=test' \
--header 'X-Up-Key: 877f8ae9c6e9ca82c0===b5fff594c373axxx' \
--header 'X-Up-Signature: CE12B506DBCD868C2C6F09E08C139CBC' \
--header 'X-Up-Timestamp: 1626056011000' \
--header 'Content-Type: application/json' \
--data-raw ''
```

返回样例：

```
{
    "page_info": {
        "total": 2,
        "start": 0,
        "limit": 15
    },
    "data": [
        {
            "id": 5815,
            "app_id": "a60f54770a583d",
            "name": "adbc",
            "status": 3,
            "start_time_type": 1,
            "start_time_timezone": 8,
            "start_time": 1627639246,
            "items": [
                {
                    "id": 10000080,
                    "name": "A\u7ec4",
                    "traffic_variation": 2,
                    "enable": false
                },
                {
                    "id": 10000081,
                    "name": "B\u7ec4",
                    "traffic_variation": 1,
                    "enable": false
                },
                {
                    "id": 10000082,
                    "name": "C\u7ec4",
                    "traffic_variation": 1,
                    "enable": false
                }
            ],
            "placement_ids": [
                "b60f6e9480e4ba"
            ],
            "choices": [
                {
                    "placement_id": "b60f547a595c75",
                    "item_id": 10000081,
                    "item_name": "B\u7ec4"
                }
            ]
        },
        {
            "id": 5814,
            "app_id": "a60f54770a583d",
            "name": "asbc",
            "status": 1,
            "start_time_type": 1,
            "start_time_timezone": 8,
            "start_time": 1627638003,
            "items": [
                {
                    "id": 10000077,
                    "name": "A\u7ec4",
                    "traffic_variation": 2,
                    "enable": false
                },
                {
                    "id": 10000078,
                    "name": "B\u7ec4",
                    "traffic_variation": 1,
                    "enable": false
                },
                {
                    "id": 10000079,
                    "name": "C\u7ec4",
                    "traffic_variation": 1,
                    "enable": false
                }
            ],
            "placement_ids": [],
            "choices": [
                {
                    "placement_id": "b60f547a595c75",
                    "item_id": 10000077,
                    "item_name": "A\u7ec4"
                },
                {
                    "placement_id": "b60f6e9480e4ba",
                    "item_id": 10000077,
                    "item_name": "A\u7ec4"
                }
            ]
        }
    ]
}
```

## 2. 创建A/B测试

#### 2.1 请求URL

[https://api.toponad.net/v3/abtest](https://openapi.toponad.com/v3/abtest)

#### 2.2 请求方式

POST

#### 2.3 请求参数

| 字段 | 类型 | 是否必传 | 备注 |
| --- | --- | --- | --- |
| name | String | Y | A/B测试名称 |
| app\_id | String | Y | 应用ID |
| start\_time\_type | Int | Y | 开始时间的类型 1=立即生效，2=指定生效时间,3-手动 |
| start\_time\_timezone | Int | Y | 开始时间的时区 -12~12 = 西12区 ~ 东12区 |
| start\_time | Int | Y | 开始时间,时间戳，立即生效、手动时可以不填 |
| placement\_ids | Array[String] | Y | 测试广告位, 至少一个 |
| items | Array[Object] | Y | 实验分组，至少两组 |
| items.name | String | Y | 实验分组的名称 |
| items.traffic\_variation | Int | Y | 实验分组的权重 |

#### 2.4 返回参数

| 字段 | 类型 | 是否必传 | 备注 |
| --- | --- | --- | --- |
| id | Int | Y | 成功时返回创建的ID，失败时无id |

#### 2.5 样例

请求样例：

```
curl --location --request POST 'https://api.toponad.net/v3/abtest' \
--header 'X-Up-Key: 877f8ae9c6e9ca82c0==5b5fff594c373axxx' \
--header 'X-Up-Signature: CE12B506DBCD868C2C6F09E08C139CBC' \
--header 'X-Up-Timestamp: 1626161553000' \
--header 'Content-Type: application/json' \
--data-raw '{
    "name": "test_1",
    "app_id": "a60f54770a583d",
    "start_time_type": "1",
    "start_time_timezone": "8",
    "start_time": "1627639246",
    "items": [
                    {
                        "name": "AAA",
                        "traffic_variation": 10,
                    },
                    {
                       "name": "BBB",
                       "traffic_variation": 10,
                    },
    ],
    "placement_ids": [
                "b60f547a2904f9"
    ]
}'
```

返回样例：

```
{
    "id": 5816
}
```

## 3. 更新A/B测试

#### 3.1 请求URL

[https://api.toponad.net/v3/abtest/:id](https://openapi.toponad.com/v3/abtest/:id)

#### 3.2 请求方式

PUT

#### 3.3 请求参数

| 字段 | 类型 | 是否必传 | 备注 |
| --- | --- | --- | --- |
| id | Int | Y | A/B测试ID |
| name | String | Y | A/B测试名称 |
| start\_time\_type | Int | Y | 开始时间的类型 1=立即生效，2=指定生效时间，3-手动 |
| start\_time\_timezone | Int | Y | 开始时间的时区 -12~12 = 西12区 ~ 东12区 |
| start\_time | Int | Y | 开始时间,时间戳，立即生效、手动时可以不填 |
| items | Array[Object] | Y | 实验分组（所有的实验组都需要上报） |
| items.id | Int | Y | 实验分组的ID |
| items.name | String | Y | 实验分组的名称 |
| items.traffic\_variation | Int | Y | 实验分组的权重 |
| items.enable | Bool | Y | 实验分组启用状态 false: 停用， true：启用中 |
| placement\_ids | Array[String] | Y | 测试广告位 |
| choices | Array[Object] | N | 从A/B实验中停掉的广告位 |
| choices.placement\_id | String | N | 广告位ID |
| choices.item\_id | Int | N | 停掉的广告位选择的实验分组ID |
| choices.item\_name | String | N | 停掉的广告位选择的实验分组名称 |

#### 3.4 返回参数

| 字段 | 类型 | 是否必传 | 备注 |
| --- | --- | --- | --- |
| id | Int | Y |  |

#### 3.5 样例

请求样例：

```
curl --location --request PUT 'https://api.toponad.net/v3/abtest/5810' \
--header 'X-Up-Key: 877f8ae9c6e9ca82c0==5b5fff594c373axxx' \
--header 'X-Up-Signature: CE12B506DBCD868C2C6F09E08C139CBC' \
--header 'X-Up-Timestamp: 1626161553000' \
--header 'Content-Type: application/json' \
--data-raw '{
    "name": "test_45678",
    "start_time_type": "2",
    "start_time_timezone": "8",
    "start_time": "1627639246",
    "items": [
                    {
                        "id" : 10000066,
                        "name": "AAA",
                        "traffic_variation": 10,
                        "enable": true
                    },
                    {
                        "id" : 10000067,
                        "name": "BBB",
                        "traffic_variation": 10,
                        "enable": true
                    },
    ],
    "placement_ids": [
                "b60f547a3d8b5d"
    ]
}'
```

返回样例：

```
{
    "id": 5810
}
```

## 4. 停用A/B测试

#### 4.1 请求URL

[https://api.toponad.net/v3/abtest/:id/stop](https://openapi.toponad.com/v3/abtest/:id/stop)

#### 4.2 请求方式

PUT

#### 4.3 请求参数

| 字段 | 类型 | 是否必传 | 备注 |
| --- | --- | --- | --- |
| placement\_id | String | Y | 广告位ID |
| item\_id | Int | Y | 停掉的广告位选择的实验分组ID |

#### 4.4 返回参数

| 字段 | 类型 | 是否必传 | 备注 |
| --- | --- | --- | --- |
| id | Int | Y |  |

#### 4.5 样例

请求样例：

```
curl --location --request PUT 'https://api.toponad.net/v3/abtest/5810/stop' \
--header 'X-Up-Key: 877f8ae9c6e9ca82c0==5b5fff594c373axxx' \
--header 'X-Up-Signature: CE12B506DBCD868C2C6F09E08C139CBC' \
--header 'X-Up-Timestamp: 1626161553000' \
--header 'Content-Type: application/json' \
--data-raw '{
    "choices" : [
        {
            "placement_id" : "b60f547a3d8b5d",
            "item_id" : 10000066,
        }
    ]
}'
```

返回样例：

```
{
    "id": 5810
}
```

## 5. 获取A/B测试详情

#### 5.1 请求URL

[https://api.toponad.net/v3/abtest/:id](https://openapi.toponad.com/v3/abtest/:id)

#### 5.2 请求方式

GET

#### 5.3 请求参数

无

#### 5.4 返回参数

| 字段 | 类型 | 是否必传 | 备注 |
| --- | --- | --- | --- |
| id | Int | Y | A/B测试的ID |
| name | String | Y | A/B测试名称 |
| app\_id | String | Y | 应用ID |
| status | Int | Y | 状态 1=已结束， 3=测试中，6=待生效 |
| start\_time\_type | Int | Y | 开始时间的类型 1=立即生效，2=指定生效时间， 3-手动 |
| start\_time\_timezone | Int | Y | 开始时间的时区 -12~12 = 西12区 ~ 东12区 |
| start\_time | Int | Y | 开始时间，时间戳 |
| items | Array[Object] | Y | 实验分组 |
| items.id | Int | Y | 实验分组的ID |
| items.name | String | Y | 实验分组的名称 |
| items.traffic\_variation | Int | Y | 实验分组的权重 |
| items.enable | Bool | Y | 实验分组启用状态 false: 停用， true：启用中 |
| placement\_ids | Array[String] | Y | 测试广告位 |
| choices | Array[Object] | Y | 从A/B实验中停掉的广告位 |
| choices.placement\_id | String | Y | 广告位ID |
| choices.item\_id | Int | Y | 停掉的广告位选择的实验分组ID |
| choices.item\_name | String | Y | 停掉的广告位选择的实验分组名称 |

#### 5.5 样例

请求样例：

```
url --location --request GET 'https://api.toponad.net/v3/abtest/5810' \
--header 'X-Up-Key: 877f8ae9c6e9ca82c0===b5fff594c373axxx' \
--header 'X-Up-Signature: CE12B506DBCD868C2C6F09E08C139CBC' \
--header 'X-Up-Timestamp: 1626056011000' \
--header 'Content-Type: application/json' \
--data-raw ''
```

返回样例：

```
{
    "id": 5810,
    "name": "test_45678",
    "publisher_id": 0,
    "app_id": "a60f54770a583d",
    "status": 3,
    "start_time_type": 1,
    "start_time_timezone": 8,
    "start_time": 1627635702,
    "items": [
        {
            "id": 10000066,
            "name": "AAA",
            "traffic_variation": 10,
            "enable": false
        },
        {
            "id": 10000067,
            "name": "BBB",
            "traffic_variation": 10,
            "enable": false
        }
    ],
    "placement_ids": [
        "b60f547a3d8b5d"
    ],
    "choices": [
        {
            "placement_id": "b60f547a2904f9",
            "item_id": 10000066,
            "item_name": "AAA"
        }
    ]
}
```

## 6. 手动开启A/B实验

#### 6.1 请求URL

[https://api.toponad.net/v3/abtest/:id/start\_manual](https://openapi.toponad.com/v3/abtest/:id)

#### 6.2 请求方式

PUT

#### 6.3 请求参数

无

#### 6.4 返回参数

|  |  |  |  |
| --- | --- | --- | --- |
| id | Int | Y | 已开启的测试ID（必须是手动类型） |

#### 6.5 样例

请求样例：

```
url --location --request GET 'https://api.toponad.net/v3/abtest/5810/start_manual' \
--header 'X-Up-Key: 877f8ae9c6e9ca82c0===b5fff594c373axxx' \
--header 'X-Up-Signature: CE12B506DBCD868C2C6F09E08C139CBC' \
--header 'X-Up-Timestamp: 1626056011000' \
--header 'Content-Type: application/json' \
--data-raw ''
```

返回样例：

```
{
    "id": 5810
}
```
