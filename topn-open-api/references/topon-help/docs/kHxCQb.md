---
title: "聚合管理的广告源管理"
source: "https://help.toponad.net/cn/docs/kHxCQb"
captured_at: "2026-07-21T08:07:23Z"
site_modified: "2026-04-21"
category_path: ["Open API接入指南", "开发者后台管理API", "聚合管理的广告源管理"]
content_sha256: "eeddf2a8188a571bd81d0572c09ed114093da5cf0c9758c0cdce6f1c0377a21f"
knowledge_role: "reference_only"
has_article_body: true
---

# 聚合管理的广告源管理

### 注意：接入Api前请先熟悉api签名机制（参考[接口鉴权说明](/cn/docs/9NzgWP)）, 即Api请求样例中的一些http请求头的来源

> 2025.10.29更新：升级支持管理在做实验的流量分组下的广告源，见接口6

## 1. 指定流量分组下的所有广告源(不包括adx广告源)

注意：不支持获取有在做实验的流量分组下的广告源，否则报错：{"errors":"code: 4602, msg: the mediation connection not found"}，如果需要，请使用API6

#### 1.1 请求URL

[https://api.toponad.net/v3/waterfall/:mediation\_group\_id/segment\_id/:segment\_id/units](https://openapi.toponad.com/v3/waterfall/:mediation_group_id/segment_id/:segment_id/units)

#### 1.2 请求方式

GET

#### 1.3 请求参数

| 字段 | 类型 | 是否必传 | 备注 |
| --- | --- | --- | --- |
| ecpm\_currency | String | N | ecpm币种单位，不传时默认为开发者账号币种，可选USD，CNY，返回参数ad\_source\_list中的ecpm和auto\_ecpm价格根据该字段传对应单位值 |

#### 1.4 返回参数

| 字段 | 类型 | 是否必传 | 备注 |
| --- | --- | --- | --- |
| offer\_list\_switch | Int | Y |  |
| ecpm\_currency | String | Y | ecpm币种单位，对应请求时的参数ecpm\_currency，返回参数ad\_source\_list中的ecpm和auto\_ecpm价格根据该字段传对应单位值 |
| parallel\_request\_number | Int | Y | 并发请求数 |
| offer\_list | Array[Object] | Y | 正在使用的交叉推广列表 |
| offer\_list.offer\_id | String | Y | 交叉推广ID |
| offer\_list.offer\_name | String | Y | 交叉推广名称 |
| ad\_source\_list | Array[Object] | Y | 启用的广告源信息列表 |
| ad\_source\_list.ad\_source\_id | Int | Y | 广告源ID |
| ad\_source\_list.name | String | Y | 广告源名称 |
| ad\_source\_list.header\_bidding\_switch | Int | Y | 是否支持Header Bidding，广告源创建时已确定  1：表示不支持  2：表示支持 |
| ad\_source\_list.ecpm | String | Y | eCPM价格 |
| ad\_source\_list.auto\_ecpm\_switch | Int | Y | 自动优化ECPM  1：表示不开启自动优化， 2：表示开启自动优化 |
| ad\_source\_list.auto\_ecpm | String | Y | 流量分组ID自动eCPM价格 |
| ad\_source\_list.ecpm\_rank | Int | Y | 同价格广告源展示优先级，值范围：[1,99]，值越大优先级越高 |
| ad\_source\_list.bid\_floor | String | N | 竞价广告源竞价底价 |
| ad\_source\_list.hour\_cap | Int | Y | 展示上限（小时），-1 表示无限制 |
| ad\_source\_list.day\_cap | Int | Y | 展示上限（天），-1 表示无限制 |
| ad\_source\_list.pacing | Int | Y | 展示间隔（秒），-1 表示无限制 |
| free\_ad\_source\_list | Array[Object] | Y | 关闭的广告源信息列表 |
| free\_ad\_source\_list.ad\_source\_id | Int | Y | 广告源ID |
| free\_ad\_source\_list.name | String | Y | 广告源名称 |
| free\_ad\_source\_list.header\_bidding\_switch | Int | Y | 是否支持Header Bidding，广告源创建时已确定  1：表示不支持  2：表示支持 |
| free\_ad\_source\_list.ecpm | String | Y | eCPM价格 |
| free\_ad\_source\_list.auto\_ecpm\_switch | Int | Y | 1：表示不开启自动优化，  2：表示开启自动优化 |
| free\_ad\_source\_list.auto\_ecpm | String | Y | 流量分组ID自动eCPM价格 |
| free\_ad\_source\_list.bid\_floor | String | N | 竞价广告源竞价底价 |

#### 1.5 样例

请求参例：

```
curl --location --request GET 'https://api.toponad.net/v3/waterfall/116112/segment_id/600262/units?ecpm_currency=USD' \
--header 'X-Up-Key: 877f8ae9c6e9ca82c0===b5fff594c373axxx' \
--header 'X-Up-Signature: CE12B506DBCD868C2C6F09E08C139CBC' \
--header 'X-Up-Timestamp: 1626056011000' \
--header 'Content-Type: application/json' \
--data-raw ''
```

返回样例：

```
{
    "offer_list_switch": 2,
    "ecpm_currency": "USD",
    "parallel_request_number": 2,
    "offer_list": [],
    "ad_source_list": [
        {
            "ad_source_id": 681853,
            "name": "Chartboost_int_2",
            "header_bidding_switch": 1,
            "ecpm": "66",
            "auto_ecpm_switch": 1,
            "auto_ecpm": "0",
            "ecpm_rank": 1,
            "hour_cap": -1,
            "day_cap": -1,
            "pacing": -1
        },
        {
            "ad_source_id": 681852,
            "name": "Sigmob_int_2",
            "header_bidding_switch": 1,
            "ecpm": "20",
            "auto_ecpm_switch": 1,
            "auto_ecpm": "0",
            "ecpm_rank": 1,
            "hour_cap": 4,
            "day_cap": 5,
            "pacing": 6
        }
    ],
    "free_ad_source_list": [
        {
            "ad_source_id": 681851,
            "name": "Kuaishou Ads_int_2",
            "header_bidding_switch": 1,
            "ecpm": "50",
            "auto_ecpm_switch": 1,
            "auto_ecpm": "0",
            "ecpm_rank": 1,
        },
        {
            "ad_source_id": 681850,
            "name": "Mintegral_int_1",
            "header_bidding_switch": 1,
            "ecpm": "100",
            "auto_ecpm_switch": 1,
            "auto_ecpm": "0",
            "ecpm_rank": 1,
        },
        {
            "ad_source_id": 681854,
            "name": "Facebook_int_2",
            "header_bidding_switch": 1,
            "ecpm": "22",
            "auto_ecpm_switch": 1,
            "auto_ecpm": "0",
            "ecpm_rank": 1,
        }
    ]
}
```

## 2. 批量修改广告源在waterfall的属性（过期，请使用Api5）

#### 2.1 请求URL

[https://api.toponad.net/v3/waterfall/:mediation\_group\_id/segment\_id/:segment\_id/units](https://openapi.toponad.com/v3/waterfall/:mediation_group_id/segment_id/:segment_id/units)

#### 2.2 请求方式

PUT

#### 2.3 请求参数

| 字段 | 类型 | 是否必传 | 备注 |
| --- | --- | --- | --- |
| parallel\_request\_number | Int | Y | 并发请求数 |
| offer\_switch | Int | N | 交叉推广开关 |
| ad\_source\_list | Array[Object] | Y | 要启用的广告源信息列表，注意：默认广告源如果还未绑定到segment\_id，则修改属性的同时也绑定到流量分组 |
| ad\_source\_list.ad\_source\_id | Int | Y | 广告源ID |
| ad\_source\_list.ecpm | String | Y | eCPM价格 |
| ad\_source\_list.auto\_ecpm\_switch | Int | Y | 是否开启自动优化，注意：广告源关联的平台账号必须是开启报表api【广告位管理Api1的is\_open\_report参数】后才可以开启自动优化  1：表示不开启自动优化，  2：表示开启自动优化 |
| ad\_source\_list.hour\_cap | Int | N | 展示上限（小时），-1 表示无限制， 注意：不传时默认为-1，和传-1是一样的意义 |
| ad\_source\_list.day\_cap | Int | N | 展示上限（天），-1 表示无限制 注意：不传时默认为-1，和传-1是一样的意义 |
| ad\_source\_list.pacing | Int | N | 展示间隔（秒），-1 表示无限制 注意：不传时默认为-1，和传-1是一样的意义 |
| ad\_source\_list.ecpm\_rank | Int | N | 同价格广告源展示优先级，值范围：[1,99]，值越大优先级越高，注意：不传默认为不修改 注意：暂时ad\_source\_list里面每个item要么都设置ecpm\_rank，要么都不设置，某些广告源不关心ecpm\_rank设置1即可 |
| ad\_source\_list.bid\_floor | String | N | 竞价广告源竞价底价 注意：暂时ad\_source\_list里面每个item要么都设置bid\_floor，要么都不设置，非竞价广告源设置"0"即可 |
| unbind\_ad\_source\_list | Array[Int] | N | 要关闭的广告源ID列表 |
| ecpm\_currency | String | N | ecpm币种单位，不传时默认为开发者账号币种，可选USD，CNY，返回参数ad\_source\_list中的ecpm和auto\_ecpm价格根据该字段传对应单位值 |

#### 2.4 返回参数

| 字段 | 类型 | 是否必传 | 备注 |
| --- | --- | --- | --- |
| mediation\_group\_id | Int | Y | 聚合分组ID |
| segment\_id | Int | Y | 流量分组ID |

#### 2.5 样例

请求样例：

```
curl --location --request PUT 'https://api.toponad.net/v3/waterfall/116112/segment_id/600262/units' \
--header 'X-Up-Key: 877f8ae9c6e9ca82c0==5b5fff594c373axxx' \
--header 'X-Up-Signature: CE12B506DBCD868C2C6F09E08C139CBC' \
--header 'X-Up-Timestamp: 1626161553000' \
--header 'Content-Type: application/json' \
--data-raw '{
    "parallel_request_number" : 1,
    "offer_switch" : 1,
    "ad_source_list": [
            {
                "ad_source_id": 681853,
                "header_bidding_switch": 1,
                "ecpm": "66",
                "auto_ecpm_switch": 1,
                "hour_cap": -1,
                "day_cap": -1,
                "pacing": -1,
                "ecpm_rank": 1
            },
            {
                "ad_source_id": 681852,
                "header_bidding_switch": 1,
                "ecpm": "20",
                "auto_ecpm_switch": 1,
                "hour_cap": 4,
                "day_cap": 5,
                "pacing": 6,
                "ecpm_rank": 1
            }
        ],
    "unbind_ad_source_list" : [
        681851,
        681850,
        681854
    ]
}'
```

返回样例：

```
{
    "mediation_group_id": 116112,
    "segment_id": 600262
}
```

## 3. 批量开启/关闭waterfall广告源

#### 3.1 请求URL

[https://api.toponad.net/v3/waterfall/units/status](https://openapi.toponad.com/v3/waterfall/units/status)

#### 3.2 请求方式

PUT

#### 3.3 请求参数

| 字段 | 类型 | 是否必传 | 备注 |
| --- | --- | --- | --- |
| placement\_id | String | Y | 广告位ID |
| mediation\_group\_id | Int | Y | 聚合分组ID |
| segment\_id | Int | Y | 流量分组ID，0代表默认分组 |
| abtest\_group\_item\_id | Int | N | 流量分组A/B测试分组ID，当流量分组没有做实验时，传入0或为空即可 |
| ad\_source\_ids | Array[Int] | Y | 广告源ID列表 |
| status | Int | Y | 操作状态，注意：开启或关闭操作时，传的广告源id必须是已绑定到流量分组segment\_id（即只能开启或关闭已绑定的广告源），枚举说明： 1: 关闭  3: 开启  11: 解绑 |

#### 3.4 返回参数

| 字段 | 类型 | 是否必传 | 备注 |
| --- | --- | --- | --- |
| items | Array[Object] | N | 错误广告源信息列表，注意：  1. 列表为空，则标识操作成功  2. 列表不为空，则列表标识哪些广告源校验不通过，所有广告源（包括校验通过）操作失败 |
| items.id | Int | Y | 广告源ID |
| items.err\_code | Int | Y | 错误码 |
| items.err\_msg | String | Y | 错误信息，部分描述如下 1. "the unit is not yet bind to the segment": 开启或关闭操作时传参存在未绑定的广告源 |

#### 3.5 样例

请求样例：

```
curl --location --request PUT 'https://api.toponad.net/v3/waterfall/units/status' \
--header 'X-Up-Key: 877f8ae9c6e9ca82c0==5b5fff594c373axxx' \
--header 'X-Up-Signature: CE12B506DBCD868C2C6F09E08C139CBC' \
--header 'X-Up-Timestamp: 1626161553000' \
--header 'Content-Type: application/json' \
--data-raw '{
    "placement_id" : "34343943uucce33",
    "mediation_group_id" : 100000,
    "segment_id" : 100000,
    "abtest_group_item_id": 0,
    "ad_source_ids": [232,435],
    "status": 1
}'
```

返回样例：

```
{
    "items": [
        {
            "id": 232,
            "err_code": 4000
            "err_msg": "the unit not found"
        }
    ]
}
```

## 4. 获取广告源所有waterfall属性

注意：流量分组做了实验，同一个segment\_id可能会有多条（对应不同的实验组abtest\_group\_item\_id）

#### 4.1 请求URL

[https://api.toponad.net/v3/waterfall/units](https://openapi.toponad.com/v3/waterfall/units)

#### 4.2 请求方式

GET

#### 4.3 请求参数

| 字段 | 类型 | 是否必传 | 备注 |
| --- | --- | --- | --- |
| ids | Array[Int] | Y | 广告源ID列表，数量最大限制为100，最小限制为1 |
| currency | String | Y | ecpm,bid\_floor等对应的币种单位，可选USD，CNY |

#### 4.4 返回参数

| 字段 | 类型 | 是否必传 | 备注 |
| --- | --- | --- | --- |
| id | Int | Y | 广告源ID |
| items | Array[Object] | Y | 广告源所有waterfall信息列表 |
| items.mediation\_group\_id | Int | Y | 聚合分组ID |
| items.segment\_id | Int | Y | 流量分组ID，0代表默认分组 |
| items.abtest\_group\_item\_id | Int | Y | 流量分组A/B测试分组ID，0代表当前流量分组没有做实验 |
| items.ecpm | Double | Y | eCPM价格, 币种单位为请求参数的currency |
| items.ecpm\_rank | Int | Y | 同价格广告源展示优先级，值范围：[1,99]，值越大优先级越高 |
| items.auto\_ecpm\_switch | Int | Y | 是否开启自动ECPM优化  1：不开启  2：开启 |
| items.auto\_ecpm | Double | Y | 开启自动ECPM优化后的自动ecpm，0代表不生效自动ecpm |
| items.show\_delay | Int | Y | 延迟展示时间，单位毫秒，范围[5000]，注意：一些样式才有，比如插屏，不关注或非插屏是传0即可 |
| items.show\_delay\_rate | Int | Y | 延迟展示概率，范围[1,100]，注意：一些样式才有，比如插屏, 不关注或非插屏是传0即可 |
| items.bid\_floor | Double | Y | 竞价底价，币种单位为请求参数的currency，非竞价或不关注传0即可 |
| items.setup\_sw | Int | Y | 广告源在该流量分组是否是开启状态的，枚举说明：  1：是  2：否 |
| items.cap\_hour | Int | Y | 小时展示上限，-1代表不限制，注意：开启的广告源才有的属性，关闭状态时传-1即可 |
| items.cap\_day | Int | Y | 天展示上限，-1代表不限制，注意：开启的广告源才有的属性，关闭状态时传-1即可 |
| items.pacing | Int | Y | 展示间隔，-1代表不限制，注意：开启的广告源才有的属性，关闭状态时传-1即可 |

#### 4.5 样例

请求样例：

```
curl --location --request GET 'https://api.toponad.net/v3/waterfall/units?ids=417018,2280206¤cy=CNY' \
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
        "id": 2280206,
        "items": [
            {
                "mediation_group_id": 273234,
                "segment_id": 0,
                "abtest_group_item_id": 0,
                "ecpm": 2,
                "ecpm_rank": 1,
                "remark": "",
                "setup_sw": 1,
                "auto_ecpm_switch": 1,
                "auto_ecpm": 0,
                "cap_hour": -1,
                "cap_day": -1,
                "pacing": -1,
                "show_delay": 0,
                "show_delay_rate": 100,
                "bid_floor": 0
            }
        ]
    }
]
```

## 5. 编辑（绑定+开启）广告源所有waterfall属性

#### 5.1 请求URL

[https://api.toponad.net/v3/waterfall/units](https://openapi.toponad.com/v3/waterfall/units)

#### 5.2 请求方式

PUT

#### 5.3 请求参数

| 字段 | 类型 | 是否必传 | 备注 |
| --- | --- | --- | --- |
| placement\_id | String | Y | TopOn的广告位ID |
| currency | String | Y | ecpm,bid\_floor等对应的币种单位，可选USD,，CNY |
| items | Array[Object] | Y | 多个广告源所有waterfall信息列表，注意：默认广告源如果还未绑定到segment\_id，则修改属性的同时也绑定到流量分组 |
| items.id | Int | Y | TopOn广告源ID |
| items.items | Array[Object] | Y | 对应每个广告源ID下的所有waterfall信息列表 注意：相同属性，所以item要么一起修改，要么一起不修改 |
| items.items.mediation\_group\_id | Int | Y | 聚合分组ID |
| items.items.segment\_id | Int | Y | 流量分组ID，0代表默认分组 |
| items.items.abtest\_group\_item\_id | Int | N | 流量分组A/B测试分组ID，当流量分组没有做实验时，传入0或为空即可 |
| items.items.ecpm | Double | Y | eCPM价格, 币种单位为请求参数的currency 注意：竞价类型没有ecpm可传0，非竞价类型最小ecpm为0.01 |
| items.items.ecpm\_rank | Int | Y | 同价格广告源展示优先级，值范围：[1,99]，值越大优先级越高 |
| items.items.auto\_ecpm\_switch | Int | Y | 是否开启自动ECPM优化 （开启广告源关联的平台账号必须是开启报表api）1：不开启 2：开启 注意：只有部分类型广告源广告源（常规非竞价，兜底广告源）才能开启指定价格 |
| items.items.show\_delay | Int | Y | 延迟展示时间，单位毫秒，注意：一些样式才有，比如插屏 |
| items.items.show\_delay\_rate | Int | Y | 延迟展示概率，范围[1,100]，注意：一些样式才有，比如插屏 |
| items.items.bid\_floor | Double | Y | 竞价底价，币种单位为请求参数的currency 注意：非竞价广告源或无竞价底价传0即可， 设置竞价底价范围，美元：[0.01,10000]；人民币：[0.1,10000] |
| items.items.setup\_sw | Int | Y | 广告源在该流量分组是否是开启状态的，枚举说明： 1：是 2：否 |
| items.items.cap\_hour | Int | Y | 小时展示上限，-1代表不限制，注意：开启的广告源才有的属性 |
| items.items.cap\_day | Int | Y | 天展示上限，-1代表不限制，注意：开启的广告源才有的属性 |
| items.items.pacing | Int | Y | 展示间隔，-1代表不限制，注意：开启的广告源才有的属性 |

#### 5.4 返回参数

| 字段 | 类型 | 是否必传 | 备注 |
| --- | --- | --- | --- |
| items | Array[Object] | N | 错误广告源信息列表，注意： 1. 列表为空，则标识操作成功 2. 列表不为空，则列表标识哪些item校验不通过，所有item（包括校验通过）操作失败 |
| items.index | Int | Y | 错误item所在的索引，从0开始 |
| items.err\_code | Int | Y | 错误码 |
| items.err\_msg | String | Y | 错误信息 |

#### 5.5 样例

请求样例：

```
curl --location --request PUT 'https://api.toponad.net/v3/waterfall/units' \
--header 'X-Up-Key: 877f8ae9c6e9ca82c0==5b5fff594c373axxx' \
--header 'X-Up-Signature: CE12B506DBCD868C2C6F09E08C139CBC' \
--header 'X-Up-Timestamp: 1626161553000' \
--header 'Content-Type: application/json' \
--data-raw '{
	"placement_id":"qdfji3434====",
	"currency":"USD",
	"items":[
		{
			"id": 2280206,
			"items": [
				{
					"mediation_group_id": 273234,
					"segment_id": 0,
					"abtest_group_item_id": 0,
					"ecpm": 2,
					"ecpm_rank": 1,
					"remark": "",
					"setup_sw": 1,
					"auto_ecpm_switch": 1,
					"auto_ecpm": 0,
					"cap_hour": -1,
					"cap_day": -1,
					"pacing": -1,
					"show_delay": 0,
					"show_delay_rate": 100,
					"bid_floor": 0
				}
			]
		}
	]
}'
```

返回样例：

```
{

}
```

## 6. 指定流量分组AB测试分组下的所有广告源(不包括adx广告源)

注意：当指定的流量分组没有在做实验时，abtest\_group\_item\_id传入0即可；如果正在做实验，那么则需要传入对应的A/B测试分组ID。如果参数不正确或当前流量分组正在做实验但是传入的测试分组ID为0，会返回错误：{"errors":"code: 4602, msg: the mediation connection not found"}

#### 6.1 请求URL

<https://api.toponad.net/v3/waterfall/:mediation_group_id/segment_id/:segment_id/abtest_group_item_id/:abtest_group_item_id/units>

#### 6.2 请求方式

GET

#### 6.3 请求参数

| 字段 | 类型 | 是否必传 | 备注 |
| --- | --- | --- | --- |
| ecpm\_currency | String | N | ecpm币种单位，不传时默认为开发者账号币种，可选USD，CNY，返回参数ad\_source\_list中的ecpm和auto\_ecpm价格根据该字段传对应单位值 |

#### 6.4 返回参数

| 字段 | 类型 | 是否必传 | 备注 |
| --- | --- | --- | --- |
| offer\_list\_switch | Int | Y |  |
| ecpm\_currency | String | Y | ecpm币种单位，对应请求时的参数ecpm\_currency，返回参数ad\_source\_list中的ecpm和auto\_ecpm价格根据该字段传对应单位值 |
| parallel\_request\_number | Int | Y | 并发请求数 |
| offer\_list | Array[Object] | Y | 正在使用的交叉推广列表 |
| offer\_list.offer\_id | String | Y | 交叉推广ID |
| offer\_list.offer\_name | String | Y | 交叉推广名称 |
| ad\_source\_list | Array[Object] | Y | 启用的广告源信息列表 |
| ad\_source\_list.ad\_source\_id | Int | Y | 广告源ID |
| ad\_source\_list.name | String | Y | 广告源名称 |
| ad\_source\_list.header\_bidding\_switch | Int | Y | 是否支持Header Bidding，广告源创建时已确定 1：表示不支持 2：表示支持 |
| ad\_source\_list.ecpm | String | Y | eCPM价格 |
| ad\_source\_list.auto\_ecpm\_switch | Int | Y | 自动优化ECPM 1：表示不开启自动优化， 2：表示开启自动优化 |
| ad\_source\_list.auto\_ecpm | String | Y | 流量分组ID自动eCPM价格 |
| ad\_source\_list.ecpm\_rank | Int | Y | 同价格广告源展示优先级，值范围：[1,99]，值越大优先级越高 |
| ad\_source\_list.bid\_floor | String | N | 竞价广告源竞价底价 |
| ad\_source\_list.hour\_cap | Int | Y | 展示上限（小时），-1 表示无限制 |
| ad\_source\_list.day\_cap | Int | Y | 展示上限（天），-1 表示无限制 |
| ad\_source\_list.pacing | Int | Y | 展示间隔（秒），-1 表示无限制 |
| free\_ad\_source\_list | Array[Object] | Y | 关闭的广告源信息列表 |
| free\_ad\_source\_list.ad\_source\_id | Int | Y | 广告源ID |
| free\_ad\_source\_list.name | String | Y | 广告源名称 |
| free\_ad\_source\_list.header\_bidding\_switch | Int | Y | 是否支持Header Bidding，广告源创建时已确定 1：表示不支持 2：表示支持 |
| free\_ad\_source\_list.ecpm | String | Y | eCPM价格 |
| free\_ad\_source\_list.auto\_ecpm\_switch | Int | Y | 1：表示不开启自动优化， 2：表示开启自动优化 |
| free\_ad\_source\_list.auto\_ecpm | String | Y | 流量分组ID自动eCPM价格 |
| free\_ad\_source\_list.bid\_floor | String | N | 竞价广告源竞价底价 |

#### 6.5 样例

请求参例：

```
curl --location --request GET 'https://openapi.toponad.com/v3/waterfall/116112/segment_id/600262/abtest_group_item_id/0/units?ecpm_currency=USD' \
--header 'X-Up-Key: 877f8ae9c6e9ca82c0===b5fff594c373axxx' \
--header 'X-Up-Signature: CE12B506DBCD868C2C6F09E08C139CBC' \
--header 'X-Up-Timestamp: 1626056011000' \
--header 'Content-Type: application/json' \
--data-raw ''
```

返回样例：

```
{
    "offer_list_switch": 2,
    "ecpm_currency": "USD",
    "parallel_request_number": 2,
    "offer_list": [],
    "ad_source_list": [
        {
            "ad_source_id": 681853,
            "name": "Chartboost_int_2",
            "header_bidding_switch": 1,
            "ecpm": "66",
            "auto_ecpm_switch": 1,
            "auto_ecpm": "0",
            "ecpm_rank": 1,
            "hour_cap": -1,
            "day_cap": -1,
            "pacing": -1
        },
        {
            "ad_source_id": 681852,
            "name": "Sigmob_int_2",
            "header_bidding_switch": 1,
            "ecpm": "20",
            "auto_ecpm_switch": 1,
            "auto_ecpm": "0",
            "ecpm_rank": 1,
            "hour_cap": 4,
            "day_cap": 5,
            "pacing": 6
        }
    ],
    "free_ad_source_list": [
        {
            "ad_source_id": 681851,
            "name": "Kuaishou Ads_int_2",
            "header_bidding_switch": 1,
            "ecpm": "50",
            "auto_ecpm_switch": 1,
            "auto_ecpm": "0",
            "ecpm_rank": 1,
        },
        {
            "ad_source_id": 681850,
            "name": "Mintegral_int_1",
            "header_bidding_switch": 1,
            "ecpm": "100",
            "auto_ecpm_switch": 1,
            "auto_ecpm": "0",
            "ecpm_rank": 1,
        },
        {
            "ad_source_id": 681854,
            "name": "Facebook_int_2",
            "header_bidding_switch": 1,
            "ecpm": "22",
            "auto_ecpm_switch": 1,
            "auto_ecpm": "0",
            "ecpm_rank": 1,
        }
    ]
}
```

## 7. 修改ADX广告源

#### 7.1 请求URL

[https://api.toponad.net/v3/adx\_units](https://openapi.toponad.com/v3/units)

#### 7.2 请求方式

PUT

#### 7.3 请求参数

| remarkecpm字段 | 类型 | 是否必传 | 备注 |
| --- | --- | --- | --- |
|  |  |  |  |
| items | Array[Object] | Y | 更新信息列表 |
| items.placement\_id | String | Y | 广告位ID |
| items.traffic\_group\_id | Int | Y | 聚合分组id |
| items.segment\_id | Int | Y | 流量分组id |
| items.abtest\_group\_item\_id | Int | Y | 实验id |
| items.unit\_id | Int | Y | ADX广告源id |
| items.remote\_unit | Object | Y | ADX广告源配置参数JSON【[新附录三方广告平台详细参数](/cn/docs/AZUgZD)】该属性只支持adx广告源 |
| items.ecpm | Float | Y | Ecpm底价输入范围0.1 ~ 10000 |
| items.cap\_day | String | Y | 每日展示限制  不限制为空字符串 |
| items.cap\_hour | String | Y | 每小时展示限制 不限制为空字符串 |
| items.pacing | String | Y | 展示间隔（秒）不限制为空字符串 |

#### 7.4 返回参数

| 字段 | 类型 | 是否必传 | 备注 |
| --- | --- | --- | --- |
| items | Array[Object] | N | 错误广告源信息列表，注意： 1. 列表为空，则标识操作成功 2. 列表不为空，则列表标识哪些item校验不通过，所有item（包括校验通过）操作失败 |
| items.index | Int | Y | 错误item所在的索引，从0开始 |
| items.err\_code | Int | Y | 错误码 |
| items.err\_msg | String | Y | 错误信息 |

#### 7.5 样例

请求样例：

```
curl --location --request PUT 'https://api.toponad.net/v3/adx_units' \
--header 'X-Up-Key: 877f8ae9c6e9ca82c0==5b5fff594c373axxx' \
--header 'X-Up-Signature: CE12B506DBCD868C2C6F09E08C139CBC' \
--header 'X-Up-Timestamp: 1626161553000' \
--header 'Content-Type: application/json' \
--data-raw '{
  "items": [
    {
      "placement_id": "b69a11257df772",
      "traffic_group_id": 769382,
      "unit_id": 12138437,
      "segment_id": 0,
      "abtest_group_item_id": 0,
      "remote_unit":{
                "mt_type": "1",
                "s_c_t_sw": "1",
                "s_c_t": "5",
                "v_m": "0",
                "video_autoplay": "2",
                "size": "320x50",
                "close_button": "1",
                "unit_type": "1",
                "orientation": "1",
                "countdown": "5",
                "allows_skip": "0",
                "layout_type": "1",
                "mode_type": "1",
                "custom_ext": "",
                "nv_tmpl_id": [
                    "1",
                    "2",
                    "4",
                    "5"
                ],
                "inter_type": "1"
            },
      "ecpm": 15,
      "cap_day": "5",
      "cap_hour": "3",
      "pacing": ""
    }
  ]
}'
```

返回样例：

```
{

}
```
