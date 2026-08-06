---
title: "展示、点击设备维度报表"
source: "https://help.toponad.net/cn/docs/OJPZH2"
captured_at: "2026-07-21T08:07:23Z"
site_modified: "2026-03-17"
category_path: ["Open API接入指南", "设备层级报表API", "展示、点击设备维度报表"]
content_sha256: "e262c647f3f6e1f32f9797a5f9869516d3205242052bbdcce75b355f40aa65e4"
knowledge_role: "reference_only"
has_article_body: true
---

# 展示、点击设备维度报表

### 注意：接入Api前请先熟悉api签名机制（参考[接口鉴权说明](/cn/docs/9NzgWP)）, 即Api请求样例中的一些http请求头的来源

### 使用注意：

- 数据支持的时间从TopOn运营开通权限后开始支持生成(例如1号开通权限，最早2号才能拉取到某些时区数据，具体时间参考下面的提前任务各时区数据更新时间点)，并且只保留最近30天数据。返回的内容以文件形式提供，如果当时未获取到数据请隔天再重试。注意：TopOn每天生成各个时区数据任务会执行两次，一次为提前任务，一次为兜底任务，提前任务的收益数据可能不完整（决定因素是不同广告平台出报表数据时间不一样，某些广告平台提前任务时可能还没有出报表数据），开发者可根据需要再拉一次兜底任务后数据
- 提前任务各时区数据更新时间点：

1、utc+8：延迟1天，下午1:00点（utc+8）更新

2、utc+0：延迟1天，下午2:30点（utc+8）更新

3、utc-8：延迟2天，上午1:30点（utc+8）更新

- 兜底任务各时区数据更新时间点：

1、utc+8：延迟2天，上午4点（utc+8）更新

2、utc+0：延迟2天，上午12点（utc+8）更新

3、utc-8：延迟3天，上午4点（utc+8）更新

### 1 请求URL

https://api.toponad.net/v3/devicereport

### 2 请求方式

GET

### 3 请求参数

| 字段 | 类型 | 是否必传 | 备注 | 样例 |
| --- | --- | --- | --- | --- |
| day | Int | Y | 开始日期，格式：YYYYmmdd | 20190501，仅支持1天前的日期 |
| app\_id | String | Y | 开发者后台的应用ID，单选 | xxxxx |
| timezone | Int | N | 时区支持 | -8,8,0三个时区 |

请求样例：

```
curl --location --request GET 'https://api.toponad.net/v3/devicereport? app_id=a606c22b789bc3&day=20210823&timezone=8' \
--header 'X-Up-Key: 877f8ae9c6e9ca82c0===b5fff594c373axxx' \
--header 'X-Up-Signature: CE12B506DBCD868C2C6F09E08C139CBC' \
--header 'X-Up-Timestamp: 1626056011000' \
--header 'Content-Type: application/json'
```

### 4 返回参数

此接口返回报表数据的下载链接，开发者获取此链接后，可直接在浏览器中下载报表数据。链接格式如下：

[https://topon-openapi.s3.amazonaws.com/topon\_report\_device/dt%3D2019-07-10/publisher\_id%3D22/app\_id%3Da5d147334b3685/000000\_0?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA35FGARBHLHHS7TWB%2F20190828%2Fus-east-1%2Fs3%2Faws4\_request&X-Amz-Date=20190828T095315Z&X-Amz-Expires=900&X-Amz-SignedHeaders=host&X-Amz-Signature=6aaf947f9b2cf02f3acb49d64a3daf719cb0b57a3d5221b0121a006e58b04b10](https://topon-openapi.s3.amazonaws.com/topon_report_device/dt%3D2019-07-10/publisher_id%3D22/app_id%3Da5d147334b3685/000000_0?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA35FGARBHLHHS7TWB%2F20190828%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20190828T095315Z&X-Amz-Expires=900&X-Amz-SignedHeaders=host&X-Amz-Signature=6aaf947f9b2cf02f3acb49d64a3daf719cb0b57a3d5221b0121a006e58b04b10%20)

文件以csv形式提供，用","作为分隔符，具体参数内容如下：

| 字段 | 类型 | 备注 |
| --- | --- | --- |
| placement\_id | String | 广告位ID |
| placement\_name | String | 广告位名称 |
| placement\_format | String | 0: native,1: rewarded\_video,2: banner,3: interstitial,4: splash |
| android\_id | String | 设备ID，androidid |
| gaid | String | Google的广告设备ID |
| idfa | String | iOS的设备ID |
| area | String | 国家 |
| impression | String | 展示数 |
| click | String | 点击数 |
| revenue | decimal(18,6) | 收益，根据三方广告平台的收益对设备层级进行拆分，货币单位同开发者后台配置一致 |
| ecpm | decimal(18,6) | TopOn基于收益API按设备展示拆分后的收益和TopOn统计的设备展示计算出eCPM，计算公式：（设备收益/TopOn统计的设备展示）\*1000。注：eCPM延迟2天提供 |
| is\_abtest | String | 对照组或测试组 0 表示对照组或未开通A/B测试 1 表示测试组 |
| traffic\_group\_id | String | 对照组或测试组id |
| segment\_id | String | 流量分组ID |
| segment\_name | String | 流量分组名称 |
| idfv | String | iOS的设备ID |
| oaid | String | 安卓的设备ID |
| user\_id | String | 开发者的自定义用户ID |
| network\_firm\_id | String | 广告平台ID |
| network\_firm | String | 广告平台名称 |
| currency | String | 开发者账号币种，USD表示美元，CNY表示人民币 |
| os\_version | String | 设备的操作系统版本 |
| att\_status | String | 设备的ATT授权状态：  0：Not determined(未决定是否授权)  1：Restricted (受限制) 2：Denied(已拒绝) 3：Authorize(已授权) |
| imei | String | 安卓的设备识别码 |
| device\_type | String | 设备类型，枚举值说明：  0: 非IOS设备  1: iphone  2: ipad |
| brand | String | 设备品牌名 |
| model | String | 设备型号 |
| app\_vn | String | 应用版本名 |
| app\_vc | String | 应用版本号 |
| new\_user\_type | String | 新用户类型，枚举值说明：  1: 是新用户  2: 不是新用户 |
| channel | String | 渠道，由开发者通过TopOn SDK传入的渠道 |
| estimate\_revenue | decimal(18,6) | 预估收益，竞价广告源以实时的广告展示价格汇总得出预估收益，非竞价广告源以人工填写的eCPM价格 \* TopOn统计的展示汇总得出预估收益, 单位美元 |
| cny\_estimate\_revenue | decimal(18,6) | 预估收益，竞价广告源以实时的广告展示价格汇总得出预估收益，非竞价广告源以人工填写的eCPM价格 \* TopOn统计的展示汇总得出预估收益, 单位人民币 |
| set\_gaid | String | 用户自定义上传的Google的广告设备ID |
| set\_imei | String | 用户自定义上传的安卓的设备识别码 |
| set\_oaid | String | 用户自定义上传的安卓的设备ID |
| set\_idfa | String | 用户自定义上传的iOS的设备ID |
| amazon\_id | String | amazon设备ID（sdk6.2.50及以上版本支持），android系统独有 |
| sub\_channel | String | 子渠道，由开发者通过SDK传入的子渠道 |
| scenario\_custom\_uuid | string | 自定义广告场景ID |
| scenario\_name | string | 广告场景名称 |
