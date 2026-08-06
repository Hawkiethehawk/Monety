---
title: "应用管理（新版v3）"
source: "https://help.toponad.net/cn/docs/ying-yong-guan-li-xin-ban-v3"
captured_at: "2026-07-21T08:07:23Z"
site_modified: "2026-04-21"
category_path: ["Open API接入指南", "开发者后台管理API", "应用管理（新版v3）"]
content_sha256: "6185b0a7845987578a2f1c66231328525dea9fa2983468aee40fe3763509f68b"
knowledge_role: "reference_only"
has_article_body: true
---

# 应用管理（新版v3）

## 注意：接入Api前请先熟悉api签名机制（参考[接口鉴权说明](https://help.takuad.com/docs/9NzgWP)）, 即Api请求样例中的一些http请求头的来源

## 1. 创建应用

##

#### 1.1 请求URL

[https://api.toponad.net/v3/apps](https://openapi.toponad.com/v3/units/list)

#### 1.2 请求方式

POST

#### 1.3 请求参数

| 字段 | 类型 | 是否必传 | 备注 |
| --- | --- | --- | --- |
| items | Array[Object] | Y | 应用信息列表 |
| items.platform | Int | Y | 系统平台，枚举值说明：  1: 安卓平台  2: iOS平台 |
| items.name | String | Y | 应用名称，注意：最大长度100个字符 |
| items.store\_on\_sale | Int | Y | 是否在商店上架，枚举值说明：  1: 否  2: 是 |
| items.store\_type | Int | N | 商店类型，未上架应用可不填，枚举说明：  1：iOS App Store（系统平台是ios） 2：Google Play 3：华为商店 4：小米应用商店 5：OPPO商店 6：vivo商店 7：应用宝 8：TapTap 9：Amazon应用商店 10：三星应用商店 11：小米海外应用商店 12：华为海外应用市场 13：Roku 14：Samsung Smart TV 15：Microsoft 16：LG Smart TV 17：Vizio 99：其他 |
| items.store\_url | String | N | 应用商店链接，需符合商店链接规范，未上架应用可不填 |
| items.package\_name | String | Y | 应用包名，需符合包名规范，示例：com.xxx |
| items.category | String | Y | 一级分类，需符合[附录（应用一级和二级分类列表）](/cn/docs/4hPdxj)规范 |
| items.sub\_category | String | Y | 二级分类，需符合[附录（应用一级和二级分类列表）](/cn/docs/4hPdxj)规范 |
| items.screen\_orientation | Int | Y | 屏幕方向，枚举值说明：  1: 竖屏  2: 横屏  3: 所有 |
| items.coppa | Int | Y | 是否遵守COPPA协议，枚举值说明：  1: 否  2: 是 |
| items.ccpa | Int | Y | 是否遵守CCPA协议，枚举值说明：  1: 否  2: 是 |
| items.wx\_open\_universal\_link | String | N | 微信开放平台 Universal Link |
| items.wx\_app\_openid | String | N | 微信应用 OpenID |
| items.icon\_url | String | N | app图标地址 |

#### 1.4 响应参数

| 字段 | 类型 | 是否必传 | 备注 |
| --- | --- | --- | --- |
| items | Array[Object] | N | 成功的应用信息列表，索引位置和请求参数items索引位置一一对应 |
| items.uuid | String | Y | 添加成功后的应用ID |
| items.app\_key | String | Y | 添加成功后的应用Key（应用维度）  在集成TopOn SDK并初始化TopOn SDK时，您需要使用到TopOn的App Key。您可以使用此账号维度的App Key，也可以使用应用维度的App Key |
| errs | Array[Object] | N | 错误服应用信息列表，注意： 1. 列表为空，则标识操作成功 2. 列表不为空，则列表标识哪些应用校验不通过，所有应用（包括校验通过）操作失败 |
| errs.index | Int | Y | 错误item在请求参数items中的索引位置，从0开始 |
| errs.code | Int | Y | 错误码 |
| errs.msg | String | Y | 错误信息 |

#### 1.5 样例

请求样例：

```
curl --location --request POST 'https://api.toponad.net/v3/apps' \
--header 'X-Up-Key: 877f8ae9c6e9ca82c0==5b5fff594c373axxx' \
--header 'X-Up-Signature: CE12B506DBCD868C2C6F09E08C139CBC' \
--header 'X-Up-Timestamp: 1626161553000' \
--header 'Content-Type: application/json' \
--data-raw '{
    "items": [
        {
            "platform": 2,
            "name": "xcj_openapi_v1",
            "category": "Game",
            "sub_category": "Casual",
            "store_url": "https://www.taptap.cn/app/dsdsd",
            "package_name": "xcj.vip.test1",
            "screen_orientation": 1,
            "store_on_sale":1,
            "store_type": 8,
            "coppa": 1,
            "ccpa": 2，
           "wx_open_universal_link":"99999",
            "wx_app_openid":"ccccc",
            "icon_url":"https://www.taptap.cn/app/dsdsd"
        }
    ]
}'
```

返回样例：

```
{
    "items": [
        {
            "uuid": "a66cccsxxxx",
            "app_key": "0b9df85fb9d552ef7====b805e6b004"
        }
    ]
}
```

## 2. 修改应用

##

#### 2.1 请求URL

[https://api.toponad.net/v3/apps](https://openapi.toponad.com/v3/units/list)

#### 2.2 请求方式

PUT

#### 2.3 请求参数

| 字段 | 类型 | 是否必传 | 备注 |
| --- | --- | --- | --- |
| items | Array[Object] | Y | 应用信息列表 |
| items.uuid | String | Y | 应用ID |
| items.name | String | Y | 应用名称，注意：最大长度100个字符 |
| items.store\_on\_sale | Int | Y | 是否在商店上架，枚举值说明：  1: 否  2: 是 |
| items.store\_type | Int | N | 商店类型，未上架应用可不填，枚举说明：  1：iOS App Store（系统平台是ios） 2：Google Play 3：华为商店 4：小米应用商店 5：OPPO商店 6：vivo商店 7：应用宝 8：TapTap 9：Amazon应用商店 10：三星应用商店 11：小米海外应用商店 12：华为海外应用市场 13：Roku 14：Samsung Smart TV 15：Microsoft 16：LG Smart TV 17：Vizio 99：其他 |
| items.store\_url | String | N | 应用商店链接，需符合商店链接规范，未上架应用可不填 |
| items.package\_name | String | Y | 应用包名，需符合包名规范，示例：com.xxx |
| items.category | String | Y | 一级分类，需符合[附录（应用一级和二级分类列表）](/cn/docs/4hPdxj)规范 |
| items.sub\_category | String | Y | 二级分类，需符合[附录（应用一级和二级分类列表）](/cn/docs/4hPdxj)规范 |
| items.screen\_orientation | Int | Y | 屏幕方向，枚举值说明：  1: 竖屏  2: 横屏  3: 所有 |
| items.coppa | Int | Y | 是否遵守COPPA协议，枚举值说明：  1: 否  2: 是 |
| items.ccpa | Int | Y | 是否遵守CCPA协议，枚举值说明：  1: 否  2: 是 |
| items.wx\_open\_universal\_link | String | N | 微信开放平台 Universal Link |
| items.wx\_app\_openid | String | N | 微信应用 OpenID |
| items.icon\_url | String | N | app图标地址 |

#### 2.4 响应参数

| 字段 | 类型 | 是否必传 | 备注 |
| --- | --- | --- | --- |
| errs | Array[Object] | N | 错误应用信息列表，注意： 1. 列表为空，则标识操作成功 2. 列表不为空，则列表标识哪些应用校验不通过，所有应用（包括校验通过）操作失败 |
| errs.index | Int | Y | 错误item在请求参数items中的索引位置，从0开始 |
| errs.code | Int | Y | 错误码 |
| errs.msg | String | Y | 错误信息 |

#### 2.5 样例

请求样例：

```
curl --location --request PUT 'https://api.toponad.net/v3/apps' \
--header 'X-Up-Key: 877f8ae9c6e9ca82c0==5b5fff594c373axxx' \
--header 'X-Up-Signature: CE12B506DBCD868C2C6F09E08C139CBC' \
--header 'X-Up-Timestamp: 1626161553000' \
--header 'Content-Type: application/json' \
--data-raw '{
    "items": [
        {
            "uuid": "a1ftn3doaefj15",
            "name": "xcj_openapi_v122",
            "category": "Game",
            "sub_category": "Casual",
            "package_name": "aieku.vip.test122",
            "screen_orientation": 2,
            "store_on_sale": 1,
            "store_type": 8,
            "store_url": "https://www.viziozzz22==.com/smart-tv-apps?appName=topon&appId=vizio.topon",
            "coppa": 1,
            "ccpa": 1

        }
    ]
}'
```

返回样例：

```
{}
```

## 3. 获取应用

注意：暂时还是v1，待后续可能升级到v3

##

#### 3.1 请求URL

https://api.toponad.net/v1/apps

#### 3.2 请求方式

POST

#### 3.3 请求参数

| 字段 | 类型 | 是否必传 | 备注 |
| --- | --- | --- | --- |
| app\_ids | Array[String] | N | 应用ID列表，默认所有应用ID，数量最大限制为100 注意：和start, limit参数一起使用时，以start+limit条件获取到的应用个数为准 |
| start | Int | N | 起始偏移量，默认0 |
| limit | Int | N | 获取个数，默认100，最大一次性获取100 |

#### 3.4 响应参数

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
| -.wx\_open\_universal\_link | String | N | 微信开放平台 Universal Link |
| -.wx\_app\_openid | String | N | 微信应用 OpenID |
| -.icon\_url | String | N | app图标地址 |
| -.errors | Int | N | 错误信息（错误时返回）,部分错误描述如下： 1. “No apps could be matched“: 请求参数app\_ids和start,limit混用错误 |

#### 3.5 样例

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
        "app_key": "aed37b858b3a7ecc54e1ecf4634399fxx",
        "platform": 2,
        "market_url": "https://itunes.apple.com/cn/app/%E7%A5%9E%E5%9B%9E%E9%81%BF/id1435756371?mt=8",
        "category": "Game",
        "sub_category": "Action",
        "screen_orientation": 3，
        "wx_open_universal_link":"99999",
         "wx_app_openid":"ccccc",
         "icon_url":"https://www.taptap.cn/app/dsdsd"
    }
]
```
