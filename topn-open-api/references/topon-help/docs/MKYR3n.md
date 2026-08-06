---
title: "广告平台管理"
source: "https://help.toponad.net/cn/docs/MKYR3n"
captured_at: "2026-07-21T08:07:23Z"
site_modified: "2026-04-21"
category_path: ["Open API接入指南", "开发者后台管理API", "广告平台管理"]
content_sha256: "ad8454f3b4e6796f102cba8ec3f9cb43f3eae1c823a44cf6bff4aa47072d959d"
knowledge_role: "reference_only"
has_article_body: true
---

# 广告平台管理

### 注意：接入Api前请先熟悉api签名机制（参考[接口鉴权说明](/cn/docs/9NzgWP)）, 即Api请求样例中的一些http请求头的来源

## 1. 创建和修改广告平台Publisher、App维度参数

#### 1.1 请求URL

[https://api.toponad.net/v1/set\_networks](https://openapi.toponad.com/v1/set_networks)

#### 1.2 请求方式

POST

#### 1.3 请求参数

| ，字段 | 类型 | 是否必传 | 备注 |
| --- | --- | --- | --- |
| network\_name | String | N | 广告平台账号名称，创建或修改操作不传默认名字为“Default”，注意：同一个广告平台（nw\_firm\_id）不允许创建相同名称的平台账号 |
| nw\_firm\_id | Int | Y | 广告平台ID，各广告平台ID可查看文档获取：[聚合平台概况](/cn/docs/2KR6QU) |
| network\_id | Int | N | 广告平台账号ID，修改时传入，创建时不传 |
| is\_open\_report | Int | Y | 是否开通Report API，枚举值说明： 1: 不开通 2: 开通 |
| api\_version | Int | N | 三方平台Publisher维度参数（即下面的auth\_content）版本， 注意： 1.不同的版本有不同的三方参数，枚举具体见附件 2.暂时只有穿山甲平台支持分版本，其他平台可忽略不传，穿山甲不传默认是2 |
| auth\_content | Object | N | 广告平台Publisher维度参数，注意：无论是否开通报表，有些广告平台相关参数都是必传的，详见[附录（三方广告平台详细参数）](/cn/docs/FSwcAe)规范中auth\_content列 注意： 1：百度平台默认支持的是公钥模式（暂不支持私钥模式） 2：分api版本的平台主要不同版本传不同参数 |
| network\_app\_info | Array[Object] | N | 广告平台App维度信息列表 |
| network\_app\_info.app\_id | String | N | TopOn的应用ID |
| network\_app\_info.app\_auth\_content | Object | N | 广告平台App维度参数，有些广告平台App维度参数必填，详见[附录（三方广告平台详细参数）](/cn/docs/FSwcAe)规范中app\_auth\_content列 |

#### 1.4 返回参数

| 字段 | 类型 | 是否必传 | 备注 |
| --- | --- | --- | --- |
| network\_name | String | Y | 广告平台账号名称 |
| nw\_firm\_id | Int | Y | 广告平台ID，各广告平台ID可查看文档获取：[聚合平台概况](/cn/docs/2KR6QU) |
| network\_id | Int | Y | 广告平台账号ID |
| is\_open\_report | Int | Y | 是否开通Report API，枚举值说明： 1: 不开通 2: 开通 |
| auth\_content | Object | N | 广告平台Publisher维度参数，详见[附录（三方广告平台详细参数）](/cn/docs/FSwcAe)规范中auth\_content列 |
| network\_app\_info | Array[Object] | N | 广告平台App维度信息列表 |
| network\_app\_info.app\_id | String | N | TopOn的应用ID |
| network\_app\_info.app\_auth\_content | Object | N | 广告平台App维度参数，详见[附录（三方广告平台详细参数）](/cn/docs/FSwcAe)规范中app\_auth\_content列 |

注意：响应错误时（http响应状态码不是200），部分错误描述如下：

1.“network is report error“：请求参数is\_open\_report数值错误

2.“network name repeated"：同一个广告平台创建相同名字账号错误

3.“network auth\_content xxx error”：请求参数auth\_content缺失或错误，请检查是否开通报表和[附录（三方广告平台详细参数）规范](/cn/docs/FSwcAe)

4.“failed to verify network auth\_content”：开通报表时校验三方network参数错误或者三方校验超时，请检查三方network参数是否正确，或者稍后重试

5.“network app\_auth\_content xxx error”：请求参数network\_app\_info.app\_auth\_content缺失或错误，请参考[附录（三方广告平台详细参数）](/cn/docs/FSwcAe)规范

6."appid error"：参数network\_app\_info.app\_id无效

#### 1.5 样例

请求样例：

```
curl --location --request POST 'https://api.toponad.net/v1/set_networks' \
--header 'X-Up-Key: 877f8ae9c6e9ca82c0===b5fff594c373axxx' \
--header 'X-Up-Signature: CE12B506DBCD868C2C6F09E08C139CBC' \
--header 'X-Up-Timestamp: 1626161553000' \
--header 'Content-Type: application/json' \
--data-raw '{
	"network_name": "Default",
	"nw_firm_id": 2,
	"network_id": 226,
	"is_open_report": 2,
	"auth_content": {
		"account_id": "pub-1310074477383748",
		"oauth_key": "1/CW8VoZRbc5UCscXs3ddTXzwT9LQ71uFUMSE6iEwcRlk"
	},
	"network_app_info": [
		{
			"app_id": "a5bc9921f7fdb4",
			"app_auth_content": {
				"app_id": "ca-app-pub-1310074477383748~6985182465"
			}
		}
	]
}'
```

返回样例：

```
{
    "network_name": "Default",
    "nw_firm_id": 2,
    "network_id": 226,
    "is_open_report": 2,
    "auth_content": {
        "account_id": "pub-1310074477383748",
        "oauth_key": "1/CW8VoZRbc5UCscXs3ddTXzwT9LQ71uFUMSE6iEwcRlk"
    },
    "network_app_info": [
        {
            "app_id": "a5bc9921f7fdb4",
            "app_auth_content": {
                "app_id": "ca-app-pub-1310074477383748~6985182465"
            }
        }
    ]
}
```

## 2. 获取广告平台Publisher、App维度参数

#### 2.1 请求URL

[https://api.toponad.net/v1/networks](https://openapi.toponad.com/v1/networks)

#### 2.2 请求方式

GET

#### 2.3 请求参数

无

#### 2.4 返回参数

| 字段 | 类型 | 是否必传 | 备注 |
| --- | --- | --- | --- |
| - | Array[Object] | Y | 广告平台Publisher、App维度参数信息列表 |
| -.network\_name | String | Y | 广告平台账号名称 |
| -.nw\_firm\_id | Int | Y | 广告平台ID，各广告平台ID可查看文档获取：[聚合平台概况](/cn/docs/2KR6QU) |
| -.nw\_firm\_name\_zh | String | Y | 广告平台中文名 |
| -.nw\_firm\_name\_en | String | Y | 广告平台英文名 |
| -.network\_id | Int | Y | 广告平台账号ID，可通过Api(1)创建广告平台后获取 |
|  |  |  |  |
| -.is\_open\_report | Int | Y | 是否开通Report API，枚举值说明： 1: 不开通 2: 开通 |
| -.api\_version | Int | N | 三方平台Publisher维度参数（即下面的auth\_content）版本， 注意： 1.不同的版本有不同的三方参数，枚举具体见附件 2.暂时只有穿山甲平台支持分版本，其他平台可忽略 |
| -.auth\_content | Object | N | 广告平台Publisher维度参数，详见[附录（三方广告平台详细参数）](/cn/docs/FSwcAe)规范中auth\_content列 |
| -.network\_app\_info | Array[Object] | N | 广告平台App维度信息列表  注意：同一个应用只能绑定到同一个三方平台的一个账号（即一对一关系），某个应用绑定到某个账号后，暂时不支持解绑，也不支持切换绑定到另一个账号（可在后台切换绑定） |
| -.network\_app\_info.app\_id | String | N | TopOn的应用ID |
| -.network\_app\_info.app\_auth\_content | Object | N | 广告平台App维度参数，详见[附录（三方广告平台详细参数）](/cn/docs/FSwcAe)规范中app\_auth\_content列 |
| \_.status | Int | N | 应用开启、关闭等状态，枚举说明 1: 关闭 3: 开启 |

#### 2.5 样例

请求样例：

```
curl --location --request GET 'https://api.toponad.net/v1/networks' \
--header 'X-Up-Key: ee609bfc9112c50ca4936fdecc43713e7eaaxxxx' \
--header 'X-Up-Signature: CE12B506DBCD868C2C6F09E08C139CBC' \
--header 'X-Up-Timestamp: 1626056011000' \
--header 'Content-Type: application/json' \
--data-raw ''
```

返回样例：

```
[
    {
        "network_name": "Default",
        "nw_firm_id": 1,
        "network_id": 307,
        "is_open_report": 2,
        "network_app_info": [
            {
                "app_id": "appid1",
                "app_auth_content": {
                    "app_id": "24234234",
                    "app_token": "1"
                }
            }
        ]
    },
    {
        "network_name": "24523423",
        "nw_firm_id": 1,
        "network_id": 1418,
        "is_open_report": 2,
        "network_app_info": [
            {
                "app_id": "appid2",
                "app_auth_content": {
                    "app_id": "232323",
                    "app_token": "1"
                }
            }
        ]
    }
]
```

## 3. 自定义广告平台的创建和修改

#### 3.1 请求URL

[https://api.toponad.net/v1/set\_custom\_network](https://openapi.toponad.com/v1/set_custom_network)

#### 3.2 请求方式

POST

#### 3.3 请求参数

| 字段 | 类型 | 是否必传 | 备注 |
| --- | --- | --- | --- |
| nw\_firm\_id | Int | N | 广告平台ID，修改操作必传，不传表示创建新的自定义广告平台 |
| nw\_firm\_name | String | N | 广告平台名称，创建或修改操作不传默认名字为“Default” |
| network\_id | Int | N | 广告平台账号ID，修改操作必传  注意1：如果想在同一个自定义平台继续创建账号，nw\_firm\_id传指定值即可  注意2：创建平台账号后，在创建广告源之前必须先调用Api(5)绑定到指定应用 |
| network\_name | String | N | 广告平台账号名称，创建或修改操作不传默认名字为“Default” |
| firm\_adapters | Array[Object] | N | 广告平台adapter信息列表 |
| firm\_adapters.platform | Int | Y | 客户端系统类型，枚举值说明： 1: Android 2: IOS |
| firm\_adapters.format | Int | Y | 广告样式标识，枚举值说明： 0: native 1: rewarded\_video 2: banner 3: interstitial 4: splash |
| firm\_adapters.adapter | String | N | adapter类名，默认为空 |

#### 3.4 返回参数

| 字段 | 类型 | 是否必传 | 备注 |
| --- | --- | --- | --- |
| nw\_firm\_id | Int | Y | 广告平台ID |
| nw\_firm\_name | String | Y | 广告平台名称 |
| network\_id | Int | Y | 广告平台账号ID |
| network\_name | String | Y | 广告平台账号名称 |
| firm\_adapters | Array[Object] | Y | 广告平台adapter信息列表 |
| firm\_adapters.platform | Int | Y | 客户端系统类型，枚举值说明： 1: Android 2: IOS |
| firm\_adapters.format | Int | Y | 广告样式标识，枚举值说明： 0: native 1: rewarded\_video 2: banner 3: interstitial 4: splash |
| firm\_adapters.adapter | String | N | adapter类名 |

注意：响应错误时（http响应状态码不是200），部分错误描述如下：

1.“network id error“：修改操作时没传network\_id或所传network\_id无效

2.“network firm name is repeated”：已创建有相同名字的自定义广告平台，不允许重复

3.“invalid firm id”：修改操作时没传nw\_firm\_id或者nw\_firm\_id和network\_id不匹配

#### 3.5 样例

请求样例：

```
curl --location --request POST 'https://api.toponad.net/v1/set_custom_network' \
--header 'X-Up-Key: 877f8ae9c6e9ca82c0675b5fff594c373axxx' \
--header 'X-Up-Signature: CE12B506DBCD868C2C6F09E08C139CBC' \
--header 'X-Up-Timestamp: 1626161553000' \
--header 'Content-Type: application/json' \
--data-raw '{
	"nw_firm_id": 1000068,
	"nw_firm_name": "第555",
	"network_id": 33,
	"network_name": "默认账号112",
	"firm_adapters": [
	 {
		 "platform": 1,
		 "format": 0,
		 "adapter" : "com.topon"
	 },
	 {
		 "platform": 2,
		 "format": 1,
		 "adapter" : "com.topon"
	 }
	]
}'
```

返回样例：

```
{
    "nw_firm_id": 1000068,
     "nw_firm_name": "第555",
     "network_id": 33,
     "network_name": "默认账号112",
     "firm_adapters": [
         {
             "platform": 1,
             "format": 0,
             "adapter" : "com.topon"
         },
         {
             "platform": 2,
             "format": 1,
             "adapter" : "com.topon"
         }
     ]
 }
```

## 4. 获取自定义广告平台Publisher维度信息

#### 4.1 请求URL

[https://api.toponad.net/v1/custom\_networks](https://openapi.toponad.com/v1/custom_networks)

#### 4.2 请求方式

GET

#### 4.3 请求参数

无

#### 4.4 返回参数

| 字段 | 类型 | 是否必传 | 备注 |
| --- | --- | --- | --- |
| \_ | Array[Object] | Y | 自定义广告平台Publisher维度信息列表 |
| -.nw\_firm\_id | Int | Y | 广告平台ID |
| -.nw\_firm\_name | String | Y | 广告平台名称 |
| -.network\_id | Int | Y | 广告平台账号ID，可通过Api(3)创建自定义广告平台后获取 |
| -.network\_name | String | Y | 广告平台账号名称 |
| -.firm\_adapters | Array[Object] | Y | 广告平台adapter信息列表 |
| -.firm\_adapters.platform | Int | Y | 客户端系统类型，枚举值说明： 1: Android 2: IOS |
| -.firm\_adapters.format | Int | Y | 广告样式标识，枚举值说明： 0: native 1: rewarded\_video 2: banner 3: interstitial 4: splash |
| -.firm\_adapters.adapter | String | N | adapter类名 |
| \_.status | Int | N | 应用开启、关闭等状态，枚举说明 1: 关闭 3: 开启 |

#### 4.5 样例

请求样例：

```
curl --location --request GET 'https://api.toponad.net/v1/custom_networks' \
--header 'X-Up-Key: ee609bfc9112c50ca4936fdecc43713e7eaaxxxx' \
--header 'X-Up-Signature: CE12B506DBCD868C2C6F09E08C139CBC' \
--header 'X-Up-Timestamp: 1626056011000' \
--header 'Content-Type: application/json' \
--data-raw ''
```

返回样例：

```
[
    {
        "nw_firm_id": 1000068,
         "nw_firm_name": "第555",
         "network_id": 33,
         "network_name": "默认账号112",
         "firm_adapters": [
             {
                 "platform": 1,
                 "format": 0,
                "adapter" : "com.topon"
             },
             {
                 "platform": 2,
                 "format": 1,
                 "adapter" : "com.topon"
             }
         ]
     },
     {
        "nw_firm_id": 1000069,
         "nw_firm_name": "第555",
         "network_id": 33,
         "network_name": "默认账号112",
         "firm_adapters": [
             {
                 "platform": 1,
                 "format": 0,
                "adapter" : "com.topon"
             },
             {
                 "platform": 2,
                 "format": 1,
                 "adapter" : "com.topon"
             }
         ]
     }
]
```

## 5. 绑定平台账号的APP维度参数

#### 5.1 请求URL

[https://api.toponad.net/v3/networks/app\_auths](https://openapi.toponad.com/v3/networks/app_auths)

#### 5.2 请求方式

POST

#### 5.3 请求参数

| 字段 | 类型 | 是否必传 | 备注 |
| --- | --- | --- | --- |
| items | Array[Object] | Y | 绑定关系列表 |
| items.network\_id | Int | Y | 广告平台账号ID |
| items.app\_id | String | Y | TopOn应用ID |
| items.app\_auth\_content | Object | Y | 广告平台App维度参数，暂时只支持自定义平台  1.自定义平台：无App维度参数，传{}即可，参考请求样例 |

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
curl --location --request POST 'https://api.toponad.net/v3/networks/app_auths' \
--header 'X-Up-Key: 877f8ae9c6e9ca82c0675b5fff594c373axxx' \
--header 'X-Up-Signature: CE12B506DBCD868C2C6F09E08C139CBC' \
--header 'X-Up-Timestamp: 1626161553000' \
--header 'Content-Type: application/json' \
--data-raw '{
    "items" : [
        {
            "network_id" : 28574,
            "app_id" : "a644751967e00d",
            "app_auth_content": {

            }
        },
        {
            "network_id" : 28574,
            "app_id" : "a644751f9f034c",
            "app_auth_content": {

            }
        },
                {
            "network_id" : 28575,
            "app_id" : "a644751967e00d",
            "app_auth_content": {

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
