---
title: "广告源管理（新版v3）"
source: "https://help.toponad.net/cn/docs/yj3d9s"
captured_at: "2026-07-21T08:07:23Z"
site_modified: "2025-08-21"
category_path: ["Open API接入指南", "开发者后台管理API", "广告源管理（新版v3）"]
content_sha256: "96db80ff2f94e02ec9aea7141cd952e26c3ff5d9efc3d06c745a6d5da3c71149"
knowledge_role: "reference_only"
has_article_body: true
---

# 广告源管理（新版v3）

### 注意：接入Api前请先熟悉api签名机制（参考[接口鉴权说明](/cn/docs/9NzgWP)）, 即Api请求样例中的一些http请求头的来源

## 1. 获取广告源列表

#### 1.1 请求URL

[https://api.toponad.net/v3/units/list](https://openapi.toponad.com/v3/units/list)

#### 1.2 请求方式

GET

#### 1.3 请求参数

| 字段 | 类型 | 是否必传 | 备注 |
| --- | --- | --- | --- |
| app\_ids | Array[String] | N | TopOn应用ID列表，数量最大限制为100 |
| placement\_ids | Array[String] | N | TopOn广告位ID列表，数量最大限制为100 |
| network\_ids | Array[Int] | N | TopOn三方平台账号ID列表，数量最大限制为100 |
| start | Int | N | 起始偏移量，默认0 |
| limit | Int | N | 获取个数，，最大限制为1000，默认1000, |

#### 1.4 响应参数

| 字段 | 类型 | 是否必传 | 备注 |
| --- | --- | --- | --- |
| total | Int | Y | 搜索条件下的总数 |
| items | Array[Object] | Y | 广告源信息列表 |
| items.id | Int | Y | 广告源ID |
| items.name | String | Y | 广告源名称 |
| items.app\_id | String | Y | TopOn的应用ID |
| items.placement\_id | String | Y | TopOn的广告位ID |
| items.network\_id | Int | Y | TopOn广告平台账号ID |

#### 1.5 样例

请求样例：

```
curl --location --request GET 'https://api.toponad.net/v3/units/list?app_ids=a63f5cced466da&placement_ids=b1ehgn65hup6v0,b640ae1464e7e9&network_ids=4779,4780&start=0&limit=200 ' \
--header 'X-Up-Key: 877f8ae9c6e9ca82c0===b5fff594c373axxx' \
--header 'X-Up-Signature: CE12B506DBCD868C2C6F09E08C139CBC' \
--header 'X-Up-Timestamp: 1626056011000' \
--header 'Content-Type: application/json' \
--data-raw ''
```

返回样例：

```
{
    "total": 10,
    "items": [
        {
            "app_id": "a6392a1c24510e",
            "placement_id": "b6392a1d36f73f",
            "network_id": 5117,
            "id": 2279787,
            "name": "ADX"
        },
        {
            "app_id": "a6392a1c24510e",
            "placement_id": "b6392a1d59c06f",
            "network_id": 5117,
            "id": 2279797,
            "name": "ADX"
        }
    ]
}
```

## 2. 获取广告源详情

#### 2.1 请求URL

[https://api.toponad.net/v3/units](https://openapi.toponad.com/v3/units)

#### 2.2 请求方式

GET

#### 2.3 请求参数

| 字段 | 类型 | 是否必传 | 备注 |
| --- | --- | --- | --- |
| ids | Array[Int] | Y | 广告源ID列表，数量最大限制为100，最小限制为1 |

#### 2.4 响应参数

| 字段 | 类型 | 是否必传 | 备注 |
| --- | --- | --- | --- |
| - | Array[Object] | Y | 广告源信息列表 |
| \_.id | Int | Y | 广告源ID |
| \_.name | String |  | 广告源名称 |
| \_.network\_id | Int | Y | TopOn广告平台账号ID |
| \_.placement\_id | String | Y | TopOn的广告位ID |
| \_.type | Int | Y | 广告源类型，枚举值说明如下：  2：普通广告源  4：adx广告源  10：兜底广告源  12：客户端竞价广告源  13：服务端竞价广告源 |
| \_.mix\_format | Int | N | 混合样式，注意：只有某些平台才有该属性，枚举说明：  -1或和广告位format值一样：非混合类型  0：混合native类型  1：混合rewarded\_video类型  2：混合banner类型  3：混合interstitial类型  4：混合splash类型 |
| \_.adsource\_token | Object | Y | 广告源配置参数，非自定义广告平台详见【[附录三方广告平台详细参数】](/cn/docs/FSwcAe)规范的adsource\_token列，自定义广告平台时需满足json object格式，该属性暂不支持adx广告源（流量分组相关） |
| \_.auto\_unit\_sw | Int | Y | 自动广告源开关，某些平台才有：1开，2关 |

#### 2.5 样例

请求样例：

```
curl --location --request GET 'https://api.toponad.net/v3/units?ids=417018,374133' \
--header 'X-Up-Key: 877f8ae9c6e9ca82c0===b5fff594c373axxx' \
--header 'X-Up-Signature: CE12B506DBCD868C2C6F09E08C139CBC' \
--header 'X-Up-Timestamp: 1626056011000' \
--header 'Content-Type: application/json' \
--data-raw ''
```

返回样例：

```
[
    {
        "id": 374133,
        "placement_id": "b6049c640e6ad1",
        "network_id": 4779,
        "name": "穿山甲_rv_3",
        "type": 2,
        "mix_format": -1,
        "adsource_token": {
            "app_id": "5343323",
            "personalized_template": "1",
            "slot_id": "4566363563"
        },
        "auto_unit_sw": 2
    },
    {
        "id": 417018,
        "placement_id": "b6049c640e6ad1",
        "network_id": 4779,
        "name": "穿山甲_rv_6",
        "type": 2,
        "mix_format": -1,
        "adsource_token": {
            "app_id": "5343323",
            "personalized_template": "0",
            "slot_id": "324ewrwe"
        },
        "auto_unit_sw": 2
    }
]
```

## 3. 创建广告源

注意：创建广告源成功后默认是解绑+关闭状态（因为这些属性是流量分组相关的，即在不同流量分组会不一样），需要再次调用聚合管理的广告源管理Api2或Api5来根据需要在指定流量分组绑定和开启

#### 3.1 请求URL

[https://api.toponad.net/v3/units](https://openapi.toponad.com/v3/units)

#### 3.2 请求方式

POST

#### 3.3 请求参数

| 字段 | 类型 | 是否必传 | 备注 |
| --- | --- | --- | --- |
| placement\_id | String | Y | TopOn的广告位ID |
| items | Array[Object] | Y | 广告源信息列表 |
| items.name | String | Y | 广告源名称 |
| items.network\_id | Int | Y | TopOn广告平台账号ID |
| items.type | Int | Y | 广告源类型，注意：某些平台才支持竞价广告源，并且同一个平台可能有些广告位样式支持竞价，有些样式又不支持，具体请参考[【](/cn/docs/AZUgZD)[新附录三方广告平台详细参数](/cn/docs/AZUgZD)】的属性列支持的竞价类型>， 枚举值说明如下：  2：常规广告源 10：兜底广告源  12：客户端竞价广告源  13：服务端竞价广告源 |
| items.mix\_format | Int | Y | 混合样式，非混合类型传-1即可，注意：只有某些平台才支持该属性，-1或者和广告位format值一样都代表非混合类型 ，混合类型需要申请权限（联系运营同学），不同三方平台参数文档请联系运营同学获取权限文档  枚举说明：  -1: 非混合类型  0：混合native类型  1：混合rewarded\_video类型  2：混合banner类型  3：混合interstitial类型  4：混合splash类型 |
| items.adsource\_token | Object | Y | 广告源配置参数，非自定义广告平台详见[【](/cn/docs/AZUgZD)[新附录三方广告平台详细参数](/cn/docs/AZUgZD)】规范的属性列adsource\_token>，自定义广告平台时需满足json object格式，该属性暂不支持adx广告源（流量分组相关） |

#### 3.4 返回参数

| 字段 | 类型 | 是否必传 | 备注 |
| --- | --- | --- | --- |
| items | Array[Object] | N | 成功的广告源信息列表，索引位置和请求参数items索引位置一一对应 |
| items.id | Int | Y | 添加成功后的广告源ID |
| errs | Array[Object] | N | 错误广告源信息列表，注意：  1. 列表为空，则标识操作成功  2. 列表不为空，则列表标识哪些广告源校验不通过，所有广告源（包括校验通过）操作失败 |
| errs.index | Int | N | 错误item在请求参数items中的索引位置，从0开始，0的时候可能不返回字段 |
| errs.code | Int | N | 错误码 |
| errs.msg | String | N | 错误信息 |

#### 3.5 样例

请求样例：

```
curl --location --request POST 'https://api.toponad.net/v3/units' \
--header 'X-Up-Key: 877f8ae9c6e9ca82c0==5b5fff594c373axxx' \
--header 'X-Up-Signature: CE12B506DBCD868C2C6F09E08C139CBC' \
--header 'X-Up-Timestamp: 1626161553000' \
--header 'Content-Type: application/json' \
--data-raw '{
    "placement_id": "b64993cxxxx",
    "items": [
        {
            "network_id": 4778,
            "name": "xcj_admob_openapi1",
            "adsource_token": {
                "unit_id":"123456790000",
                "orientation":"1"
            },
            "mix_format":-1,
            "type": 2
        }
    ]
}'
```

返回样例：

```
{
    "errs": [
        {
            "index": 0,
            "code": 4000,
            "msg": "the unit type is invalid"
        }
    ]
}
```

## 4. 修改广告源

#### 4.1 请求URL

[https://api.toponad.net/v3/units](https://openapi.toponad.com/v3/units)

#### 4.2 请求方式

PUT

#### 4.3 请求参数

| 字段 | 类型 | 是否必传 | 备注 |
| --- | --- | --- | --- |
| placement\_id | String | Y | TopOn的广告位ID |
| items | Array[Object] | Y | 广告源信息列表 |
| items.id | Int | Y | 广告源ID |
| items.name | String | Y | 广告源名称 |
| items.adsource\_token | Object | Y | 广告源配置参数，非自定义广告平台详见【[新附录三方广告平台详细参数](/cn/docs/AZUgZD)】规范的属性列adsource\_token>，自定义广告平台时需满足json object格式，该属性暂不支持adx广告源（流量分组相关 |

#### 4.4 返回参数

| 字段 | 类型 | 是否必传 | 备注 |
| --- | --- | --- | --- |
| items | Array[Object] | N | 错误广告源信息列表，注意：  1. 列表为空，则标识操作成功  2. 列表不为空，则列表标识哪些item校验不通过，所有item（包括校验通过）操作失败 |
| items.index | Int | Y | 错误item所在的索引，从0开始 |
| items.err\_code | Int | Y | 错误码 |
| items.err\_msg | String | Y | 错误信息 |

#### 4.5 样例

请求样例：

```
curl --location --request PUT 'https://api.toponad.net/v3/units' \
--header 'X-Up-Key: 877f8ae9c6e9ca82c0==5b5fff594c373axxx' \
--header 'X-Up-Signature: CE12B506DBCD868C2C6F09E08C139CBC' \
--header 'X-Up-Timestamp: 1626161553000' \
--header 'Content-Type: application/json' \
--data-raw '{
    "placement_id": "b64993cxxxx",
    "items": [
        {
            "id": 4778,
            "name": "xcj_admob_openapi1",
            "adsource_token": {
                "unit_id":"123456790000",
                "orientation":"1"
            }
        }
    ]
}'
```

返回样例：

```
{

}
```

## 5. 批量删除广告源

注意：暂时还是v1, 待后续升级v3

#### 51 请求URL

[https://api.toponad.net/v1/del\_units](https://openapi.toponad.com/v1/del_units)

#### 5.2 请求方式

POST

#### 5.3 请求参数

| 段 | 类型 | 是否必传 | 备注 |
| --- | --- | --- | --- |
| adsource\_ids | Array[Int] | Y | 广告源ID列表，数量最大限制为10，广告源id列表可通过【Api3】创建广告源后获取 |

#### 5.3 返回参数

| 字段 | 类型 | 是否必传 | 备注 |
| --- | --- | --- | --- |
| msg | String | N | 结果描述，比如"suc"代表删除成功 |

#### 5.5 样例

请求样例：

```
curl --location --request PUT 'https://api.toponad.net/v1/del_units' \
--header 'X-Up-Key: 877f8ae9c6e9ca82c0==5b5fff594c373axxx' \
--header 'X-Up-Signature: CE12B506DBCD868C2C6F09E08C139CBC' \
--header 'X-Up-Timestamp: 1626161553000' \
--header 'Content-Type: application/json' \
--data-raw '{
    "adsource_ids":[19683]
}'
复制
```

返回样例：

```
{
    "msg": "suc"
}
```
