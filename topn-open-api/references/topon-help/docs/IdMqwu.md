---
title: "广告源管理（过期）"
source: "https://help.toponad.net/cn/docs/IdMqwu"
captured_at: "2026-07-21T08:07:23Z"
site_modified: "2025-08-21"
category_path: ["Open API接入指南", "开发者后台管理API", "广告源管理（过期）"]
content_sha256: "5e8b18ffd575f7bcc8733bdd75b25bfc51126e2ef8ac130599326a0c221c580c"
knowledge_role: "reference_only"
has_article_body: true
---

# 广告源管理（过期）

##### 注意：已过期，使用新版Api: [广告源管理 (新版v3)](/cn/docs/yj3d9s)

## 1. 批量创建和修改广告源

注意：在应用下创建新广告平台的广告源时，需要先调用 【广告平台管理Api1】创建新广告平台的Publisher和App维度参数

#### 1.1 请求URL

[https://api.toponad.net/v1/set\_units](https://openapi.toponad.com/v1/set_units)

#### 1.2 请求方式

POST

#### 1.3 请求参数

| 字段 | 类型 | 是否必传 | 备注 |
| --- | --- | --- | --- |
| count | Int | Y | 创建或修改的广告源总数 |
| ecpm\_currency | String | N | 请求参数units中的default\_ecpm币种单位，默认为开发者账号币种，可选USD，CNY |
| units | Array[Object] | Y | 广告源信息列表，数量最大限制为10，注意：  1. 同一个TopOn平台账号对应的第三方平台的广告源唯一标识（例如腾讯平台的广告源唯一标识为广告位ID，对应请求参数adsource\_token属性中的unit\_id）不能重复创建TopOn不同广告源，各三方平台的广告源唯一标识见【[附录三方广告平台详细参数](/cn/docs/FSwcAe)】规范中adsource\_token列的后面带'(唯一)'的key |
| units.network\_id | Int | Y | 广告平台账号ID，可通过【广告平台管理Api1】创建广告平台后获取 |
| units.adsource\_id | Int | N | 广告源ID，修改时必传 |
| units.adsource\_name | String | Y | 广告源名称 |
| units.adsource\_token | Object | Y | 广告平台Unit维度参数，非自定义广告平台详见【[附录三方广告平台详细参数】](/cn/docs/FSwcAe)规范，自定义广告平台时需满足json object格式 |
| units.placement\_id | String | Y | TopOn的广告位ID，可通过【广告位管理Api1】创建广告位后获取 |
| units.default\_ecpm | String | Y | 广告源默认价格，注意：  1. ecpm是流量分组维度下属性，如果想修改ecpm,请调用7.2接口修改  2. 该接口不可修改ecpm,若要修改其它属性（例如adsource\_name），则和创建时传一样ecpm即可，后期升级接口时会优化体验 |
| units.header\_bidding\_switch | Int | N | Header Bidding 开关，默认为关闭，注意：只有部分广告平台的部分广告位样式支持Header Bidding，详情见【[附录支持开启Header Bidding 的广告平台和广告样式】](/cn/docs/0ZYsjj)，创建后不可修改，即修改操作可不传，枚举值说明：  1：关（默认）  2：开 |
| units.bottom\_type | Int | N | 是否为兜底广告源，注意：只有普通广告源才支持设置是否兜底，并且激励视频、插屏、原生、Banner类型的广告源默认不允许设置兜底类型，需要联系运营人员开通权限，枚举值说明：  0：非兜底（默认）  1：是兜底 |

#### 1.4 返回参数

| 字段 | 类型 | 是否必传 | 备注 |
| --- | --- | --- | --- |
| units | Array[Object] | Y | 广告源信息列表 |
| units.network\_id | Int | Y | 广告平台账号ID，可通过 【广告位管理Api2】 获取该ID |
| units.adsource\_id | Int | N | 广告源ID，修改时必传 |
| units.adsource\_name | String | Y | 广告源名称 |
| units.adsource\_token | Object | Y | 广告平台Unit维度参数，详见【[附录三方广告平台详细参数】](/cn/docs/FSwcAe)规范中adsource\_token列 |
| units.placement\_id | String | Y | TopOn的广告位ID |
| units.default\_ecpm | String | Y | 广告源默认价格 |
| units.header\_bidding\_switch | Int | N | Header Bidding 开关，默认为关闭，注意：只有部分广告平台的部分广告位样式支持Header Bidding，详情见【[附录支持开启Header Bidding 的广告平台和广告样式】](/cn/docs/0ZYsjj)，创建后不可修改，即修改操作可不传，枚举值说明：  1：关（默认）  2：开 |
| units.bottom\_type | Int | N | 是否为兜底广告源，注意：只有普通广告源才支持设置是否兜底，并且激励视频、插屏、原生、Banner类型的广告源默认不允许设置兜底类型，需要联系运营人员开通权限，枚举值说明：  0：非兜底（默认）  1：是兜底 |
| units.ecpm\_currency | String | Y | ecpm币种单位，对应请求时的参数ecpm\_currency |
| units.errors | String | N | 错误信息（错误时返回）,部分错误描述如下： 1. "header\_bidding\_switch error"：请求参数header\_bidding\_switch值错误或某些平台暂时不支持开启HB  2. “network\_id check network error”：请求参数network\_id非法  3. "network\_id auth content decode error"：广告平台publisher维度参数未设置，检查确认后调用【广告平台管理Api1】或者在开发者后台设置重新编辑该平台保存  4. "network\_id error please check": 广告平台publisher维度参数未设置  5. “network app param error, please check”：广告平台的app维度参数未设置，注意：批量创建广告源之前必须确认对应的三方广告平台的app维度参数已经绑定到了TopOn的对应应用，并且每个应用只需绑定一次即可，具体绑定方式有如下两种：  （1）调用8.1接口（若果是自定义平台则调用【广告位管理Api5】）进行绑定：请求参数中的network\_app\_info.app\_id即为要绑定到的TopOn的应用ID，network\_app\_info.app\_auth\_content即为三方平台的app维度参数，具体详情参考【广告位管理Api1】 （2）在开发者后台进行绑定，页面操作流程：选中广告平台（变现平台）-->点击对应账号的广告源管理-->点击关联应用进行绑定即可（左边的应用列表即该平台账号已经绑定app维度参数的TopOn应用）  6. “ad\_souce\_token param empty error“: 请求参数adsource\_token未传  7. "adsource\_id error"：请求参数adsource\_id非法  8. "ad\_souce\_token auth error"：请求参数adsource\_token填写错误或缺失  9. "ad\_souce\_token error:xxx is null"：adsource\_token参数里的对应key缺失  10. "ad\_souce\_token error:xxx is err: example: xxx"：adsource\_token参数里的对应key枚举值非法  11. "ad\_source\_name repeated"：不允许创建重复名字的广告源  12. "repeated unit error": 同一个TopOn平台账号对应的第三方平台的广告源唯一标识（例如腾讯平台的广告源唯一标识为广告位ID，对应请求参数adsource\_token属性中的unit\_id）不能重复创建TopOn不同广告源，各三方平台的广告源唯一标识见【[附录三方广告平台详细参数】](/cn/docs/FSwcAe)规范中adsource\_token列的后面带'(唯一)'的key  13. “the network and placement format does not support header bidding”：广告平台和广告样式不支持开启Header Bidding，详情参考【[附录支持开启Header Bidding 的广告平台和广告样式】](/cn/docs/0ZYsjj) |

#### 1.5 样例

请求样例：

```
{
    "count": 2,
    "units": [
        {
            "network_id": 307,
            "adsource_name": "5234",
            "adsource_token": {
                "unit_id": "fasfasf",
                "is_video": "0",
                "personalized_template": "1",
                "size": "320x50",
                "layout_type": "1"
            },
            "placement_id": "b5bc993ab0966a",
            "default_ecpm": "69"
        },
        {
            "network_id": 225,
            "adsource_name": "5234",
            "adsource_id": 19759,
            "adsource_token": {
                "slot_id": "fasfasf",
                "is_video": "0",
                "personalized_template": "1",
                "size": "640x100",
                "layout_type": "1"
            },
            "placement_id": "b5bc993ab0966a",
            "default_ecpm": "69"
        }
    ]
}
```

返回样例：

```
    [
        {
            "network_id": 307,
            "adsource_id": 19743,
            "adsource_name": "23423423423",
            "adsource_token": {
                "size": "sdsd",
                "unit_id": "xcxc"
            },
            "placement_id": "12312312",
            "default_ecpm": "",
            "errors": "adsource_id error",
            "ecpm_currency": "USD"
        },
        {
            "network_id": 307,
            "adsource_name": "asfdasdasd",
               "adsource_token": {
                "size": "asfasd",
                "unit_id": "asdasdafsdddd"
            },
            "placement_id": "123123123",
            "default_ecpm": "",
            "errors": "ad_source_name repeated",
            "ecpm_currency": "USD"
        }
    ]
```

## 2. 获取广告源列表

#### 2.1 请求URL

[https://api.toponad.net/v1/units](https://openapi.toponad.com/v1/units)

#### 2.2 请求方式

POST

#### 2.3 请求参数

| 字段 | 类型 | 是否必传 | 备注 |
| --- | --- | --- | --- |
| network\_firm\_ids | Array[Int] | N | 广告平台ID列表，默认所有广告平台ID，各广告平台ID可查看文档获取：[聚合平台概况](/cn/docs/2KR6QU) 注意：和start, limit参数一起使用时，以start+limit条件获取到的广告源个数为准 |
| app\_ids | Array[String] | N | 应用ID列表，默认所有应用ID，可通过【应用管理Api2】获取已创建的应用ID 注意：和start, limit参数一起使用时，以start+limit条件获取到的广告源个数为准 |
| placement\_ids | Array[String] | N | 广告位ID列表，默认所有广告位ID，可通过【广告位管理Api2】获取已创建的广告位ID 注意：和start, limit参数一起使用时，以start+limit条件获取到的广告源个数为准 |
| adsource\_ids | Array[Int] | N | 广告源ID列表，默认所有广告源ID 注意：和start, limit参数一起使用时，以start+limit条件获取到的广告源个数为准 |
| start | Int | N | 起始偏移量，默认0 |
| limit | Int | N | 获取个数，默认0，如果network\_firm\_ids，app\_ids，placement\_ids，adsource\_ids都不传时则最大一次性获取100 |
| metrics | Array[String] | N | 指定返回的字段，默认全部返回，可选字段：nw\_firm\_id，network\_id，network\_name，adsource\_id，adsource\_name，adsouce\_token，app\_id，app\_name，platform，placement\_id，placement\_name，placement\_format，waterfall |
| ecpm\_currency | String | N | ecpm币种单位，不传时默认USD，可选CNY，返回参数waterfall\_list中的ecpm价格根据该字段传对应单位值 |

#### 2.4 返回参数

| 字段 | 类型 | 是否必传 | 备注 |
| --- | --- | --- | --- |
| network\_id | Int | N | 广告平台账号ID |
| network\_name | String | N | 广告平台账号名称 |
| nw\_firm\_id | Int | N | 广告平台ID |
| adsource\_id | Int | N | 广告源ID |
| adsource\_name | String | N | 广告源名称 |
| adsource\_token | Object | N | 广告源配置参数 |
| app\_id | String | N | TopOn的应用ID |
| app\_name | String | N | TopOn的应用名称 |
| platform | Int | N | 客户端系统类型，枚举值说明： 1: Android 2: IOS |
| placement\_id | String | N | TopOn的广告位ID |
| placement\_name | Object | N | TopOn的广告位名称 |
| placement\_format | String | N | 广告位广告形式，枚举值：native、banner、rewarded\_video、interstitial、splash |
| ecpm\_currency | String | Y | ecpm币种单位，对应请求时的参数ecpm\_currency |
| waterfall\_list | Array[Object] | N | 当前正在使用该广告源的waterfall信息 |
| bottom\_type | Int | N | 是否为兜底广告源，注意：只有普通广告源才支持设置是否兜底，并且激励视频、插屏、原生、Banner类型的广告源默认不允许设置兜底类型，需要联系运营人员开通权限，枚举值说明：  0：非兜底（默认）  1：是兜底 |
| waterfall\_list.ecpm | String | N | waterfall关联的ecpm |
| waterfall\_list.auto\_ecpm | String | N | waterfall自动优化的ecpm |
| waterfall\_list.header\_bidding\_switch（已废弃无效） | Int | N | 是否支持headerbidding，注意：header\_bidding\_switch非waterfalls属性，已废弃 |
| waterfall\_list.auto\_switch | Int | N | 是否开启了自动优化，枚举值说明：  1: 关闭  2: 开启 |
| waterfall\_list.day\_cap | Int | N | daycap |
| waterfall\_list.hour\_cap | Int | N | hour cap |
| waterfall\_list.pacing | Int | N | pacing |
| waterfall\_list.segment\_name | String | N | segment名称 |
| waterfall\_list.segment\_id | Int | N | 关联的segment\_id |
| waterfall\_list.parallel\_request\_number | Int | N | 关联的segment的并发请求数 |
| waterfall\_list.is\_abtest | Int | N | 是否是测试组，默认为默认组，枚举值说明：  0: 默认组  1: 测试组 |
| waterfall\_list.mediation\_group\_id | Int | N | 聚合分组ID |
| waterfall\_list.remark | String | N | 广告源+流量分组维度的备注信息 |

#### 2.5 样例

请求样例：

```
{
    "adsource_ids":[19683]
}
```

返回样例：

```
[
    {
        "nw_firm_id": 12,
        "network_name": "Default",
        "adsource_id": 19683,
        "adsource_name": "Unity Ads_int_2",
        "adsource_token": {
            "game_id": "234234",
            "placement_id": "23434"
        },
        "app_id": "232323",
        "app_name": "234234",
        "platform": 2,
        "placement_id": "234234234234",
        "placement_name": "234234234",
        "placement_format": "3",
        "ecpm_currency": "USD",
        "waterfall_list": [
            {
                "ecpm": "1",
                "auto_ecpm": "",
                "header_bidding_switch": 1,
                "auto_switch": 1,
                "day_cap": 0,
                "hour_cap": 0,
                "pacing": 0,
                "name": "日韩",
                "segment_id": 123,
                "priority": 3,
                "parallel_request_number": 2,
                "remark": "test"
            },
            {
                "ecpm": "2",
                "auto_ecpm": "",
                "header_bidding_switch": 1,
                "auto_switch": 1,
                "day_cap": -1,
                "hour_cap": -1,
                "pacing": -1,
                "name": "ipad",
                "segment_id": 456,
                "priority": 2,
                "parallel_request_number": 2,
                "remark": "test"
            }
        ]
    }
]
```

## 3. 批量删除广告源

#### 3.1 请求URL

[https://api.toponad.net/v1/del\_units](https://openapi.toponad.com/v1/del_units)

#### 3.2 请求方式

POST

#### 3.3 请求参数

| 字段 | 类型 | 是否必传 | 备注 |
| --- | --- | --- | --- |
| adsource\_ids | Array[Int] | Y | 广告源ID列表，数量最大限制为10，广告源id列表可通过【Api1】创建广告源后获取 |

#### 3.4 返回参数

| 字段 | 类型 | 是否必传 | 备注 |
| --- | --- | --- | --- |
| msg | String | N | 结果描述，比如"suc"代表删除成功 |

#### 3.5 样例

请求样例：

```
{
    "adsource_ids":[19683]
}
```

返回样例：

```
{
    "msg": "suc"
}
```
