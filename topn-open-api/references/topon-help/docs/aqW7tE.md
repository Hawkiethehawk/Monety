---
title: "广告位管理"
source: "https://help.toponad.net/cn/docs/aqW7tE"
captured_at: "2026-07-21T08:07:23Z"
site_modified: "2026-06-02"
category_path: ["Open API接入指南", "开发者后台管理API", "广告位管理"]
content_sha256: "a05f384e9a6ced1155d9aeb226815873fc33ab12cfcaa066e2a48d541d32f458"
knowledge_role: "reference_only"
has_article_body: true
---

# 广告位管理

### 注意：接入Api前请先熟悉api签名机制（参考[接口鉴权说明](/cn/docs/9NzgWP)）, 即Api请求样例中的一些http请求头的来源

## 1. 批量创建和修改广告位

#### 1.1 请求URL

[https://api.toponad.net/v1/deal\_placement](https://openapi.toponad.com/v1/deal_placement)

#### 1.2 请求方式

POST

#### 1.3 请求参数

| 字段 | 类型 | 是否必传 | 备注 |
| --- | --- | --- | --- |
| count | Int | Y | 创建或修改的广告位数量 |
| app\_id | String | Y | 创建或修改的广告位的应用ID |
| placements | Array[Object] | Y | 创建或修改的广告位信息列表，列表长度最大限制为100 |
| placements.placement\_name | String | Y | 广告位名称，注意：名称前后不允许空格，长度不允许超过100个字符 |
| placements.placement\_id | String | N | 广告位id，注意： 1.修改操作传入 2.创建操作不传，此时如果placement\_name已存在，则也标识为修改操作，即不允许在同一个应用下创建相同名字的广告位 |
| placements.adformat | String | Y | 广告样式，创建后不可修改，枚举值：native、banner、rewarded\_video、interstitial、splash |
| placements.reward\_s2s\_sw | Int | N | 服务端激励回调开关， 注意：只有激励视频样式才有的属性，非激励视频不传即可， 激励视频创建时默认是关闭，编辑时不不传代表不修改 枚举说明： 1：开启 2：关闭 |
| placements.reward\_rule\_id | Int | N | 激励回调规则ID，服务端激励回调开启时必传，非激励视频或激励回调关闭时不传即可, 0代表自定义规则，大于0代表已有的回调规则 规则ID具体看：[服务端回调规则管理](/cn/docs/fu-wu-duan-hui-diao-gui-ze) |
| placements.reward\_s2s | Object | N | 服务端激励回调开启时（reward\_s2s\_sw=1）并且选择了自定义规则（reward\_rule\_id=0）时必传属性，非激励视频或激励回调关闭时不传即可， 结构如下 |
| placements.reward\_s2s.number | Int | Y | 激励数量，有效范围[1:10000000] |
| placements.reward\_s2s.name | String | Y | 激励名称 |
| placements.reward\_s2s.url | String | Y | 激励回调地址，注意：请输入有效地址，TopOn会在操作时回调该地址（增加参数is\_test=1）测试是否正常 |
| placements.template（已废弃无效） | Int | N | 针对native广告才有的配置，默认为标准，创建后不可修改，枚举值说明： 0: 标准 1: 原生Banner 2: 原生开屏 |
| placements.template\_extra（已废弃无效） | Object | N | 针对native广告必传的模板额外信息 |
| placements.template\_extra.cdt（已废弃无效） | Int | N | template为原生开屏时：倒计时时间，单位为秒，默认5秒 |
| placements.template\_extra.ski\_swt（已废弃无效） | Int | N | template为原生开屏时：是否可跳过，默认不可跳过，枚举值说明： 0: 表示No 1: 表示Yes |
| placements.template\_extra.aut\_swt（已废弃无效） | Int | N | template为原生开屏时：是否自动关闭，默认不自动关闭，枚举值说明： 0: 表示No 1: 表示Yes |
| placements.template\_extra.auto\_refresh\_time（已废弃无效） | Int | N | template为原生Banner时：是否开启自动刷新+自动刷新的时间，秒为单位，建议至少间隔10秒，注意：小于等于0标识不开启自动更新 |
| placements.remark | String | N | 备注 |
| placements.status （已废弃，勿传） | Int | N | 广告位状态（后期不再维护，请使用5.4接口），默认正常，注意：设置1,2会影响广告位使用，枚举值说明： 1: 锁定 2: 等待审核 3: 正常 |

#### 1.4 返回参数

| 字段 | 类型 | 是否必传 | 备注 |
| --- | --- | --- | --- |
| - | Array[Object] | Y | 广告位信息列表 |
| -.app\_id | String | Y | 开发者后台的应用ID |
| -.app\_name | String | Y | 应用名称 |
| -.placement\_name | String | Y | 广告位名称 |
| -.placement\_id | String | Y | 开发者后台的广告位ID |
| -.adformat | String | Y | 广告样式，枚举值：native、banner、rewarded\_video、interstitial、splash |
| -.reward\_s2s\_sec\_key | String | N | 激励是否服务端回调的安全密钥，  注意：只有开启服务端激励（reward\_s2s\_sw=1）并且选择了自定义规则（reward\_rule\_id=0）时才回传 |
| -.template | Int | N | 针对native广告才有的配置，默认为标准，创建后不可修改，枚举值说明： 0: 标准 1: 原生Banner 2: 原生开屏 |
| \_.template\_extra | Object | N | 针对native广告的模板额外信息 |
| -.template\_extra.cdt | Int | N | template为原生开屏时：倒计时时间，单位为秒，默认5秒 |
| -.template\_extra.ski\_swt | Int | N | template为原生开屏时：是否可跳过，默认不可跳过，枚举值说明： 0: 表示No 1: 表示Yes |
| -.template\_extra.aut\_swt | Int | N | template为原生开屏时：是否自动关闭，默认不自动关闭，枚举值说明： 0: 表示No 1: 表示Yes |
| -.template\_extra.auto\_refresh\_time | Int | N | template为原生Banner时：自动刷新的时间，秒为单位 |
| \_.template\_extra.auto\_refresh | Int | N | template为原生Banner时：是否自动刷新, 枚举值说明: 0: 关闭自动刷新 1: 开启自动刷新 |
| -.remark | String | N | 备注 |
| -.status | Int | N | 广告位状态 |
| -.errors | String | N | 错误信息（错误时返回）,部分错误描述如下： 1. “xxx of the placement is error“: 请求参数数值错误 |

#### 1.5 样例

请求样例：

```
curl --location --request POST 'https://api.toponad.net/v1/deal_placement' \
--header 'X-Up-Key: 877f8ae9c6e9ca82c0675b5fff594c373axxx' \
--header 'X-Up-Signature: CE12B506DBCD868C2C6F09E08C139CBC' \
--header 'X-Up-Timestamp: 1626161553000' \
--header 'Content-Type: application/json' \
--data-raw '{
    "count": 1,
    "app_id": "a5c41a9ed1679c",
    "placements": [
        {
            "placement_name": "6",
            "adformat": "native",
            "remark": "remark",
            "template":2,
            "template_extra":{
                "cdt":55,
                "ski_swt":1,
                "aut_swt":1
            }

        }

    ]
}'
```

返回样例：

```
[
    {
        "app_name": "我要翘课",
        "app_id": "a5c41a9ed1679c",
        "platform": 2,
        "placement_id": "b1bv57tielnlts",
        "placement_name": "6",
        "adformat": "native",
        "remark": "remark",
        "template": 2,
        "template_extra": {
            "cdt": 55,
            "ski_swt": 1,
            "aut_swt": 1
        }
    }
]
```

## 2. 获取广告位列表

#### 2.1 请求URL

[https://api.toponad.net/v1/placements](https://openapi.toponad.com/v1/placements)

#### 2.2 请求方式

POST

#### 2.3 请求参数

| 字段 | 类型 | 是否必传 | 备注 |
| --- | --- | --- | --- |
| app\_ids | Array[String] | N | 应用ID列表，默认所有应用ID，数量最大限制为100 |
| placement\_ids | Array[String] | N | 广告位ID列表，默认所有广告位ID，数量最大限制为100 注意：和start, limit参数一起使用时，以start+limit条件获取到的广告位个数为准 |
| start | Int | N | 起始偏移量，默认0 |
| limit | Int | N | 起始偏移量，默认100, 最大一次性获取100 |

#### 2.4 返回参数

| 字段 | 类型 | 是否必传 | 备注 |
| --- | --- | --- | --- |
| - | Array[Object] | Y | 广告位信息列表 |
| \_.app\_id | String | Y | 开发者后台的应用ID |
| \_.app\_name | String | Y | 应用名称 |
| \_.platform | Int | Y | 应用平台，枚举值说明： 1: 安卓平台 2: iOS平台 |
| \_.placement\_name | String | Y | 广告位名称 |
| \_.placement\_id | String | Y | 开发者后台的广告位ID |
| \_.adformat | String | Y | 广告样式，枚举值：native、banner、rewarded\_video、interstitial、splash |
| \_.reward\_s2s\_sw | Int | N | 激励视频样式服务端回调开关，枚举说明： 1：开  2：关 |
| \_.reward\_rule\_id | Int | N | 激励回调规则ID, 0（不返回）表自定义规则，大于0代表已有的回调规则 |
| \_.reward\_s2s | Object | N | 激励视频样式服务端回调开启并选择了自定义规则时，才返回的一些配置属性 |
| \_.reward\_s2s.number | Int | N | 激励数量 |
| \_.reward\_s2s.name | String | N | 激励名称 |
| \_.reward\_s2s.url | String | N | 激励回调地址 |
| \_.reward\_s2s.sec\_key | String | N | 激励安全密钥 |
| \_.template | Int | N | 针对native广告才有的配置，默认为标准，创建后不可修改，枚举值说明： 0: 标准 1: 原生Banner 2: 原生开屏 |
| \_.template\_extra | Object | N | 针对native广告的模板额外信息 |
| \_.template\_extra.cdt | Int | N | template为原生开屏时：倒计时时间，单位为秒，默认5秒 |
| \_.template\_extra.ski\_swt | Int | N | template为原生开屏时：是否可跳过，默认不可跳过，枚举值说明： 0: 表示No 1: 表示Yes |
| \_.template\_extra.aut\_swt | Int | N | template为原生开屏时：是否自动关闭，默认不自动关闭，枚举值说明： 0: 表示No 1: 表示Yes |
| \_.template\_extra.auto\_refresh\_time | Int | N | template为原生Banner时：自动刷新时间，秒为单位 |
| \_.template\_extra.auto\_refresh | Int | N | template为原生Banner时：是否自动刷新, 枚举值说明: 0: 关闭自动刷新 1: 开启自动刷新 |
| \_.remark | String | N | 备注 |
| \_.status | Int | N | 广告位状态（后期不再维护，使用status\_v2） |
| \_.status\_v2 |  |  | 广告位开启、关闭等状态，枚举说明 1: 关闭 3: 开启 |
| -.errors | String | N | 错误信息（错误时返回）,部分错误描述如下： 1. “No placements could be matched“: 请求参数app\_ids，placement\_ids和start，limit混用错误 |

#### 2.5 样例

请求样例：

```
curl --location --request POST 'https://api.toponad.net/v1/placements' \
--header 'X-Up-Key: 877f8ae9c6e9ca82c0675b5fff594c373axxx' \
--header 'X-Up-Signature: CE12B506DBCD868C2C6F09E08C139CBC' \
--header 'X-Up-Timestamp: 1626161553000' \
--header 'Content-Type: application/json' \
--data-raw '{
    "placement_ids":["b5bc9bc2951216"]
}'
```

返回样例：

```
[
    {
        "app_name": "topontest",
        "app_id": "a5bc9921f7fdb4",
        "platform": 2,
        "placement_id": "b5bc9bc2951216",
        "placement_name": "topontest_rewardvideo",
        "adformat": "rewarded_video"
    }
]
```

## ~~3. 批量删除广告位~~

#### 3.1 请求URL

[https://api.toponad.net/v1/del\_placements (该接口已废弃)](https://openapi.toponad.com/v1/del_placements)

#### 3.2 请求方式

POST

#### 3.3 请求参数

| 字段 | 类型 | 是否必传 | 备注 |
| --- | --- | --- | --- |
| placement\_ids | Array[String] | Y | 广告位id列表，数量最大限制为100 |

#### 3.4 返回参数

| 字段 | 类型 | 是否必传 | 备注 |
| --- | --- | --- | --- |
| msg | String | N | 结果描述，比如"suc"代表删除成功 |

#### 3.5 样例

请求样例：

```
curl --location --request POST 'https://api.toponad.net/v1/del_placements' \
--header 'X-Up-Key: 877f8ae9c6e9ca82c0675b5fff594c373axxx' \
--header 'X-Up-Signature: CE12B506DBCD868C2C6F09E08C139CBC' \
--header 'X-Up-Timestamp: 1626161553000' \
--header 'Content-Type: application/json' \
--data-raw '{
    "placement_ids":["b5bc9bc2951216"]
}'
```

返回样例：

```
{
    "msg": "suc"
}
```

## 4. 批量开启/关闭广告位

#### 4.1 请求URL

[https://api.toponad.net/v3/placements/status](https://openapi.toponad.com/v3/placements/status)

#### 4.2 请求方式

PUT

#### 4.3 请求参数

| 字段 | 类型 | 是否必传 | 备注 |
| --- | --- | --- | --- |
| ids | Array[String] | Y | 广告位ID列表，最大批量100个， 例如：["34343943uucce33"] |
| status | Int | Y | 操作状态，枚举说明： 1: 关闭 3: 开启 |

#### 4.4 返回参数

| 字段 | 类型 | 是否必传 | 备注 |
| --- | --- | --- | --- |
| items | Array[Object] | N | 错误广告源信息列表，注意： 1. 列表为空，则标识操作成功 2. 列表不为空，则列表标识哪些广告位校验不通过，所有广告位（包括校验通过）操作失败 |
| items.id | String | Y | 广告位ID |
| items.err\_code | Int | Y | 错误码 |
| items.err\_msg | String | Y | 错误信息，部分描述如下 1. "the unit is not yet bind to the segment": 开启或关闭操作时传参存在未绑定的广告源 |

#### 4.5 样例

请求样例：

```
curl --location --request PUT 'https://api.toponad.net/v3/placements/status' \
--header 'X-Up-Key: 877f8ae9c6e9ca82c0675b5fff594c373axxx' \
--header 'X-Up-Signature: CE12B506DBCD868C2C6F09E08C139CBC' \
--header 'X-Up-Timestamp: 1626161553000' \
--header 'Content-Type: application/json' \
--data-raw '{
    "ids": ["34343943uucce33"],
    "status": 1
}'
```

返回样例：

```
{

}
```
