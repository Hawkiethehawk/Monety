---
title: "应用管理（过期）"
source: "https://help.toponad.net/cn/docs/Ndt56S"
captured_at: "2026-07-21T08:07:23Z"
site_modified: "2026-06-02"
category_path: ["Open API接入指南", "开发者后台管理API", "应用管理（过期）"]
content_sha256: "aed99363f5beb576ae8cc7b4d4f762c0179f3b1eb23eff9c7567e3641e393e9a"
knowledge_role: "reference_only"
has_article_body: true
---

# 应用管理（过期）

### 注意：接入Api前请先熟悉api签名机制（参考[接口鉴权说明](/cn/docs/9NzgWP)）, 即Api请求样例中的一些http请求头的来源

## 1 批量创建和修改应用

#### 1.1 请求URL

[https://api.toponad.net/v1/deal\_app](https://openapi.toponad.com/v1/deal_app)

#### 1.2 请求方式

POST

#### 1.3 请求参数

| 字段 | 类型 | 是否必传 | 备注 |
| --- | --- | --- | --- |
| count | Int | Y | 创建或修改的应用的数量 |
| apps | Array[Object] | Y | 创建或修改的应用信息列表，列表长度最大限制为100 |
| apps.app\_id | String | N | 开发者后台的应用ID，注意： 1. 修改操作传入 2. 创建操作不传，此时如果app\_name和platform已存在，则也标识为修改操作，即不允许在同一个平台下创建相同名字的应用 |
| apps.app\_name | String | Y | 应用名称，注意：名称前后不允许空格，长度不允许超过100个字符 |
| apps.platform | Int | Y | 应用平台，创建后不可修改，枚举值说明： 1: 安卓平台 2: iOS平台 |
| apps.market\_url | String | N | 应用商店链接，需符合商店链接规范，未上架应用可不填 |
| apps.screen\_orientation | Int | Y | 屏幕方向，枚举值说明： 1: 竖屏 2: 横屏 3: 所有 |
| apps.package\_name | String | Y | 应用包名，需符合包名规范，示例：com.xxx |
| apps.category | String | N | 一级分类，需符合[附录（应用一级和二级分类列表）](/cn/docs/4hPdxj)规范，创建时未上架的应用必传 |
| apps.sub\_category | String | N | 二级分类，需符合[附录（应用一级和二级分类列表）](/cn/docs/4hPdxj)规范，创建时未上架的应用必传 |
| apps.coppa | Int | N | 是否遵守COPPA协议，默认否，枚举值说明： 1: 否 2: 是 |
| apps.ccpa | Int | N | 是否遵守CCPA协议，默认否，枚举值说明： 1: 否 2: 是 |
| apps.store\_on\_sale | Int | N | 是否在商店上架，默认否，枚举值说明： 1: 否 2: 是 |

#### 1.4 返回参数

| 字段 | 类型 | 是否必传 | 备注 |
| --- | --- | --- | --- |
| - | Array[Object] | Y | 应用信息列表 |
| -.app\_id | String | Y | 开发者后台的应用ID |
| -.app\_name | String | Y | 应用名称 |
| -.errors | String | N | 错误信息（错误时返回）,部分错误描述如下： 1. “Market url of the app is error“: 请求参数market\_url链接无效 2. "xxx is required": 一些必填参数错误 3. "repeat app name error": 修改时传入的app\_name对应的app\_id无效 |
| -.platform | Int | Y | 应用平台，创建后不可修改，枚举值说明： 1: 安卓平台 2: iOS平台 |
| -.screen\_orientation | Int | Y | 屏幕方向，枚举值说明： 1: 竖屏 2: 横屏 3: 所有 |
| \_.package\_name | String | Y | 应用包名，需符合包名规范，示例：com.xxx |
| \_.category | String | N | 一级分类，需符合[附录（应用一级和二级分类列表）](/cn/docs/4hPdxj)规范 |
| \_.sub\_category | String | N | 二级分类，需符合[附录（应用一级和二级分类列表）](/cn/docs/4hPdxj)规范 |
| -.coppa | Int | N | 是否遵守COPPA协议，默认否，枚举值说明： 1: 否 2: 是 |
| -.ccpa | Int | N | 是否遵守CCPA协议，默认否，枚举值说明： 1: 否 2: 是 |
| -.store\_on\_sale | Int | N | 是否在商店上架，默认否，枚举值说明： 1: 否 2: 是 |

#### 1.5 样例

请求样例：

```
curl --location --request POST 'https://api.toponad.net/v1/deal_app' \
--header 'X-Up-Key: 877f8ae9c6e9ca82c0675b5fff594c373axxx' \
--header 'X-Up-Signature: CE12B506DBCD868C2C6F09E08C139CBC' \
--header 'X-Up-Timestamp: 1626161553000' \
--header 'Content-Type: application/json' \
--data-raw '{
    "count": 1,
    "apps": [
        {
            "app_name": "===222555",
            "platform": 1,
            "screen_orientation":2,
            "category":"Game",
            "sub_category":"Action",
            "package_name": "com.hunantv.imgo.activity.inter3"
        }
    ]
}'
```

返回样例：

```
[
    {
        "app_name": "===222555",
        "app_id": "a1d5ke4j7vp123",
        "platform": 1,
        "category": "Game",
        "sub_category": "Action",
        "screen_orientation": 2,
        "package_name": "com.hunantv.imgo.activity.inter3"
    }
]
```

## 2. 获取应用列表

#### 2.1 请求URL

[https://api.toponad.net/v1/apps](https://openapi.toponad.com/v1/apps)

#### 2.2 请求方式

POST

#### 2.3 请求参数

| 字段 | 类型 | 是否必传 | 备注 |
| --- | --- | --- | --- |
| app\_ids | Array[String] | N | 应用ID列表，默认所有应用ID，数量最大限制为100 注意：和start, limit参数一起使用时，以start+limit条件获取到的应用个数为准 |
| start | Int | N | 起始偏移量，默认0 |
| limit | Int | N | 获取个数，默认100，最大一次性获取100 |

#### 2.4 返回参数

| 字段 | 类型 | 是否必传 | 备注 |
| --- | --- | --- | --- |
| - | Array[Object] | Y | 应用信息列表 |
| -.app\_id | String | Y | 开发者后台的应用ID |
| -.app\_name | String | Y | 应用名称 |
| -.app\_key | String | Y | 应用标识key，在集成Taku SDK并初始化Taku SDK时，您需要使用到Taku 的App Key。您可以使用此账号维度的App Key，也可以使用应用维度的App Key |
| -.platform | Int | Y | 应用平台，创建后不可修改，枚举值说明： 1: 安卓平台 2: iOS平台 |
| -.market\_url | String | N | 应用商店链接 |
| -.screen\_orientation | Int | Y | 屏幕方向，枚举值说明： 1: 竖屏 2: 横屏 3: 所有 |
| -.package\_name | String | N | 应用包名 |
| -.category | String | N | 应用一级分类 |
| -.sub-category | String | N | 应用二级分类 |
| -.coppa | String | N | 是否遵守COPPA协议，默认否，枚举值说明： 1: 否 2: 是 |
| -.ccpa | Int | N | 是否遵守CCPA协议，默认否，枚举值说明： 1: 否 2: 是 |
| \_.status | Int | N | 应用开启、关闭等状态，枚举说明 1: 关闭 3: 开启 |
| -.store\_on\_sale | Int | N | 是否在商店上架，默认否，枚举值说明： 1: 否 2: 是 |
| -.errors | Int | N | 错误信息（错误时返回）,部分错误描述如下： 1. “No apps could be matched“: 请求参数app\_ids和start,limit混用错误 |

#### 2.5 样例

请求样例：

```
curl --location --request POST 'https://api.toponad.net/v1/apps' \
--header 'X-Up-Key: 877f8ae9c6e9ca82c0==5b5fff594c373axxx' \
--header 'X-Up-Signature: CE12B506DBCD868C2C6F09E08C139CBC' \
--header 'X-Up-Timestamp: 1626161553000' \
--header 'Content-Type: application/json' \
--data-raw '{
    "limit":1
}'
```

返回样例：

```
[
    {
        "app_name": "uparputest",
        "app_id": "a5bc9921f7fdb4",
        "platform": 2,
        "app_key": "aed37b858b3a7ecc54e1ecf4634399fxx",
        "market_url": "https://itunes.apple.com/cn/app/%E7%A5%9E%E5%9B%9E%E9%81%BF/id1435756371?mt=8",
        "category": "Game",
        "sub_category": "Action",
        "screen_orientation": 3
    }
]
```

## ~~3. 批量删除应用~~

#### 3.1 请求URL

[https://api.toponad.net/v1/del\_apps (该接口已废弃)](https://openapi.toponad.com/v1/del_apps)

#### 3.2 请求方式

POST

#### 3.3 请求参数

| 字段 | 类型 | 是否必传 | 备注 |
| --- | --- | --- | --- |
| app\_ids | Array[String] | Y | 应用ID列表，数量最大限制为100 |

#### 3.4 返回参数

| 字段 | 类型 | 是否必传 | 备注 |
| --- | --- | --- | --- |
| msg | String | Y | 结果描述，比如"suc"代表删除成功 |

#### 3.5 样例

请求样例：

```
curl --location --request POST 'https://api.toponad.net/v1/del_apps' \
--header 'X-Up-Key: 877f8ae9c6e9ca82c0==5b5fff594c373axxx' \
--header 'X-Up-Signature: CE12B506DBCD868C2C6F09E08C139CBC' \
--header 'X-Up-Timestamp: 1626161553000' \
--header 'Content-Type: application/json' \
--data-raw '{
    "app_ids": ["a1bu2thutsq3mn"]
}'
```

返回样例：

```
{
    "msg": "suc"
}
```
