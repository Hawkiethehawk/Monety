---
title: "服务端回调规则管理"
source: "https://help.toponad.net/cn/docs/fu-wu-duan-hui-diao-gui-ze"
captured_at: "2026-07-21T08:07:23Z"
site_modified: "2025-08-21"
category_path: ["Open API接入指南", "开发者后台管理API", "服务端回调规则管理"]
content_sha256: "44ab9f2640d07fcc9c86b81449181911189330294f86c6cdd37afb01130c2e43"
knowledge_role: "reference_only"
has_article_body: true
---

# 服务端回调规则管理

## 1. 获取激励规则

#### 1.1 请求URL

[https://api.toponad.net/v3/advanced/reward\_rule](https://openapi.toponad.com/v3/units/list)

#### 1.2 请求方式

GET

#### 1.3 请求参数

| 字段 | 类型 | 是否必传 | 备注 |
| --- | --- | --- | --- |
| ids | Array[Int32] | N | 激励规则ID列表，数量最大限制为100，  不传时代表获取所有 |

#### 1.4 响应参数

| 字段 | 类型 | 是否必传 | 备注 |
| --- | --- | --- | --- |
| items | Array[Object] | Y | 激励规则信息列表 |
| items.id | Int | Y | 规则ID |
| items.rule\_name | String | Y | 规则名称，最大长度30 |
| items.reward\_name | String | Y | 激励名称，最大长度30 |
| items.reward\_number | Int | Y | 激励数量，有效范围[1,100000000] |
| items.reward\_url | String | Y | 回调地址 |
| items.reward\_sec\_key | String | Y | 公共密钥 |
| items.remark | String | Y | 备注 |
| items.status | Int | Y | 状态，枚举说明：  1：停用  3：开启 |

#### 1.5 样例

请求样例：

```
curl --location --request GET 'https://api.toponad.net/v3/advanced/reward_rule?ids=417018,374133' \
--header 'X-Up-Key: 877f8ae9c6e9ca82c0===b5fff594c373axxx' \
--header 'X-Up-Signature: CE12B506DBCD868C2C6F09E08C139CBC' \
--header 'X-Up-Timestamp: 1626056011000' \
--header 'Content-Type: application/json' \
--data-raw ''
```

返回样例：

```
{
    "items": [
        {
            "id": 1,
            "rule_name": "新增加的测试规则零零一",
            "remark": "备注一下",
            "reward_number": 10000,
            "reward_name": "测试规则01",
            "reward_url": "https://topon-billing-sys.oss-accelerate.aliyuncs.com/1613/20231226/1703578680_r0u5ZR1c.pdf?OSSAccessKeyId=LTAI5tKdnC9J6sdUn1SB1ju3&中文=测试&_!@#$%^&*4353*(233223)_+-={]}[]\\|:;\"'23424.?/Expires=1703592649&32`~4355&Signature=05yq2Zb9%2FdCeDnehO277KuV17mk%3D",
            "reward_sec_key": "llyh0dzbrudgakp06baipujcotrhwo1k",
            "status": 3
        }
    ]
}
```

## 2. 创建激励规则

##

#### 2.1 请求URL

[https://api.toponad.net/v3/advanced/reward\_rule](https://openapi.toponad.com/v3/units/list)

#### 2.2 请求方式

POST

#### 2.3 请求参数

| 字段 | 类型 | 是否必传 | 备注 |
| --- | --- | --- | --- |
| items | Array[Object] | Y | 激励规则信息列表 |
| items.rule\_name | String | Y | 规则名称，最大长度30 |
| items.reward\_name | String | Y | 激励名称，最大长度30 |
| items.reward\_number | Int | Y | 激励数量，有效范围[1,100000000] |
| items.reward\_url | String | Y | 回调地址,  注意：请输入有效地址，Taku会在操作时回调该地址（增加参数is\_test=1）测试是否正常 |
| items.remark | String | Y | 备注 |

#### 2.4 响应参数

| 字段 | 类型 | 是否必传 | 备注 |
| --- | --- | --- | --- |
| items | Array[Object] | N | 成功的激励规则信息列表，索引位置和请求参数items索引位置一一对应 |
| items.id | Int | Y | 添加成功后的激励规则ID |
| items.reward\_sec\_key | String | Y | 添加成功后的激励规则公共密钥 |
| errs | Array[Object] | N | 错误激励规则信息列表，注意： 1. 列表为空，则标识操作成功 2. 列表不为空，则列表标识哪些激励规则校验不通过，所有激励规则（包括校验通过）操作失败 |
| errs.index | Int | Y | 错误item在请求参数items中的索引位置，从0开始 |
| errs.code | Int | Y | 错误码 |
| errs.msg | String | Y | 错误信息 |

#### 2.5 样例

请求样例：

```
curl --location --request POST 'https://api.toponad.net/v3/advanced/reward_rule' \
--header 'X-Up-Key: 877f8ae9c6e9ca82c0==5b5fff594c373axxx' \
--header 'X-Up-Signature: CE12B506DBCD868C2C6F09E08C139CBC' \
--header 'X-Up-Timestamp: 1626161553000' \
--header 'Content-Type: application/json' \
--data-raw '{
    "items": [
        {

            "reward_number": 4778,
            "rule_name": "xcj2",
            "reward_name":"激励1",
            "remark":"===",
            "reward_url": "https://www.baidu.com/"
        }
    ]
}'
```

返回样例：

```
{
    "items": [
        {
            "id": 318,
            "reward_sec_key": "0b9df85fb9d552ef7====b805e6b004"
        }
    ]
}
```

## 3. 修改激励规则

##

#### 3.1 请求URL

[https://api.toponad.net/v3/advanced/reward\_rule](https://openapi.toponad.com/v3/units/list)

#### 3.2 请求方式

PUT

#### 3.3 请求参数

| 字段 | 类型 | 是否必传 | 备注 |
| --- | --- | --- | --- |
| items | Array[Object] | Y | 激励规则信息列表 |
| items.id | Int | Y | 规则ID |
| items.rule\_name | String | Y | 规则名称，最大长度30 |
| items.reward\_name | String | Y | 激励名称，最大长度30 |
| items.reward\_number | String | Y | 激励数量，有效范围[1,100000000] |
| items.reward\_url | String | Y | 回调地址,  注意：请输入有效地址，Taku会在操作时回调该地址（增加参数is\_test=1）测试是否正常 |
| items.remark | Int | Y | 备注 |
| items.status | Int | Y | 状态，枚举说明：  1：停用  3：开启 |

#### 3.4 响应参数

| 字段 | 类型 | 是否必传 | 备注 |
| --- | --- | --- | --- |
| errs | Array[Object] | N | 错误激励规则信息列表，注意： 1. 列表为空，则标识操作成功 2. 列表不为空，则列表标识哪些激励规则校验不通过，所有激励规则（包括校验通过）操作失败 |
| errs.index | Int | Y | 错误item在请求参数items中的索引位置，从0开始 |
| errs.code | Int | Y | 错误码 |
| errs.msg | String | Y | 错误信息 |

#### 3.5 样例

请求样例：

```
curl --location --request POST 'https://api.toponad.net/v3/advanced/reward_rule' \
--header 'X-Up-Key: 877f8ae9c6e9ca82c0==5b5fff594c373axxx' \
--header 'X-Up-Signature: CE12B506DBCD868C2C6F09E08C139CBC' \
--header 'X-Up-Timestamp: 1626161553000' \
--header 'Content-Type: application/json' \
--data-raw {
    "items": [
        {
            "id":313,
            "reward_number": 4778999,
            "rule_name": "xcj1",
            "reward_name":"激励1_1",
            "reward_url": "https://www.baidu.com/",
            "remark": "222",
            "status": 3
        }
    ]
}'
```

返回样例：

```
{}
```

## 4. 删除激励规则

#### 4.1 请求URL

[https://api.toponad.net/v3/advanced/reward\_rule](https://openapi.toponad.com/v3/units/list)

#### 4.2 请求方式

DELETE

#### 4.3 请求参数

| 字段 | 类型 | 是否必传 | 备注 |
| --- | --- | --- | --- |
| ids | Array[Int32] | Y | 激励规则ID列表，数量最大限制为100，最小1 |

#### 4.4 响应参数

暂无

#### 4.5 样例

请求样例：

```
curl --location --request DELETE 'https://api.toponad.net/v3/advanced/reward_rule' \
--header 'X-Up-Key: 877f8ae9c6e9ca82c0===b5fff594c373axxx' \
--header 'X-Up-Signature: CE12B506DBCD868C2C6F09E08C139CBC' \
--header 'X-Up-Timestamp: 1626056011000' \
--header 'Content-Type: application/json' \
--data-raw '
{
    "ids":[313]
}'
```

返回样例：

暂无

####
