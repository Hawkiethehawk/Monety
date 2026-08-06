---
title: "报表上传"
source: "https://help.toponad.net/cn/docs/RoWhLz"
captured_at: "2026-07-21T08:07:23Z"
site_modified: "2025-08-21"
category_path: ["Open API接入指南", "开发者后台管理API", "报表上传"]
content_sha256: "8f02e5683d8df4c64850a3679f247e08bfcb11fac3e1ecd03b9db6aafc64d34a"
knowledge_role: "reference_only"
has_article_body: true
---

# 报表上传

### 注意：接入Api前请先熟悉api签名机制（参考[接口鉴权说明](/cn/docs/9NzgWP)）, 即Api请求样例中的一些http请求头的来源

## 1. 上传三方收益报表

#### 1.1 请求URL

[https://api.toponad.net/v1/report/upload](https://openapi.toponad.com/v1/report/upload)

#### 1.2 请求方式

POST

#### 1.3 请求参数

| 字段 | 类型 | 是否必传 | 备注 |
| --- | --- | --- | --- |
| network\_id | Int | Y | TopOn三方平台账号ID列表 1. api: 可根据广告平台管理模块获取 2.后台: 获取如下图 |
| report\_currency | String | Y | 报表币种单位，枚举值：USD，CNY |
| area | String | N | 地区短码，穿山甲的账号必传： CN：中国内地 JP：日本 |
| file | String | Y | base64编码的三方的数据文件内容，文件大小不超过5M,仅支持穿山甲、腾讯广告、百度联盟、快手联盟和自定义广告平台，对应文件类型如下： 穿山甲：8、10、11、12列的xlsx文件 腾讯广告：15列的csv文件 百度联盟：12列的csv文件，12列的xlsx文件 快手联盟：12列的csv文件 自定义广告平台：6列的xlsx文件 |
| file\_type | Int | N | 文件扩展名类型，0（默认）代表xlsx文件，1代表csv文件 |

#### 1.4 返回参数

HTTP响应码200表示上传成功，其它响应码表示上传失败

#### 1.5 样例

请求样例：

```
curl --location --request POST 'https://api.toponad.net/v1/report/upload' \
--header 'X-Up-Key: 877f8ae9c6e9ca82c0==5b5fff594c373axxx' \
--header 'X-Up-Signature: CE12B506DBCD868C2C6F09E08C139CBC' \
--header 'X-Up-Timestamp: 1626161553000' \
--header 'Content-Type: application/json' \
--data-raw '{
    "file": "UEsDBBQACAgIAGx6EFcAAAAAAA",
    "file_type": 0,
    "network_id": 3609090882,
    "report_currency": "USD"
}'
```
