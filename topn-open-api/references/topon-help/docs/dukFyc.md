---
title: "综合报表"
source: "https://help.toponad.net/cn/docs/dukFyc"
captured_at: "2026-07-21T08:07:23Z"
site_modified: "2026-06-30"
category_path: ["Open API接入指南", "数据报表API", "综合报表"]
content_sha256: "33f1146aa9ec7e5cf616356954bf997d918b200a670fff5a99e8b8a950d59b0a"
knowledge_role: "reference_only"
has_article_body: true
---

# 综合报表

**注意：接入Api前请先熟悉api签名机制（参考[接口鉴权说明](/cn/docs/9NzgWP)）, 即Api请求样例中的一些http请求头的来源**

**使用前说明：**

● 申请开通报表API权限后：需要等大概等2到3小时左右才能获取到数据（否则数据列表是空，请耐心等待）

（如何确认是否有权限：登录TopOn后台，右上角下拉列表--账户管理--key页面，若有全局Publisher Key相应参数，则为已开通权限；若无，请联系TopOn运营开通权限。）

● 正常能获取到数据后，只能获取到申请开通权限那天向前推10天之后的数据，比如2月24号开通权限，只能获取到2月14号及之后日期的数据

● 历史数据不会更新（除非当时数据不完整，重拉过数据）

● 当天TopOn统计的数据（展示，点击等）每10分钟更新一次，更新频率基本和后台一致（时机不同可能会稍微延迟于后台）

● 昨天的三方数据（或者昨天的三方数据，三方收益，三方展示等）每两小时更新一次，会比开发者后台延迟2到3小时左右，比如开发者后台9点看到完整三方收益，openapi可能需要到12点左右

**使用注意:**

● 当请求参数group\_by中存在维度scenario/traffic\_group/channel/sdk\_version/app\_version中任意一个时，响应不返回api相关指标（request\_api，fillrate\_api，impression\_api，click\_api，ctr\_api，ecpm\_api，unit\_ecpc，unit\_ecpr）以及ecpm，ecpc，ecpr，revenue，black\_revenue，black\_ecpm，revenue\_gap，ecpm\_gap，impression\_gap，click\_gap

● 注意：所有带有API的相关指标为TopOn从三方平台广告后台拉取的数据。因此无法划分到场景、流量分组、渠道、SDK版本、应用版本等维度。不能划分的原因是三方平台后台实际上无法获得TopOn SDK统计到的场景、流量分组、渠道、SDK版本、应用版本等维度。

● 显示启动DAU指标（dau\_launch）的条件：

1. grouby条件不包含有以下任意维度：placement、traffic\_group、network、adformat、adsource、scenario

2. adsource\_id\_list、placement\_id\_list为空

● 显示DAU指标（dau、estimated\_revenue\_arpu、engaged\_rate、imp\_dau）的条件：

1. grouby条件不包含有以下任意维度：network、adsource、scenario

2. adsource\_id\_list为空

● 显示新用户指标（new\_users、new\_user\_rate）的条件：

1. grouby条件必须为以下范围内的维度：date、app、area、channel

2. adsource\_id\_list、placement\_id\_list、network\_firm\_id\_list为空

● 显示流量请求指标（load、loads\_filled、load\_fillrate）的条件：

1. grouby条件不包含有以下任意维度：network、adsource、scenario

2. adsource\_id\_list为空

● 显示广告请求指标（request、request\_filled、fillrate、ecpr）的条件：

1. grouby条件不包含有以下任意维度：scenario

● 显示竞价指标（bid\_request、bid\_filled\_request\_rate、bid\_filled\_request\_ecpm）的条件：

1. grouby条件不包含有以下任意维度：scenario

● 显示广告场景指标（scenario\_entry、scenario\_entry\_ready\_rate、ready\_request、ready\_rate）的条件：

1. grouby条件不包含有以下任意维度：traffic\_group、network、adsource

2. adsource\_id\_list为空

**使用技巧:**

● 获取多个App数据：批量传入多个app\_id，group by app即可

● 获取多天数据：startdate和enddate传入一个时间段，group by date\_time即可，由于数据更新不会很频繁，而且历史数据基本不会更新，建议每天更新最近2天数据就可以了

● 数据汇总：group by到最细维度，可以拿到结果后再作sum计算

## 1. 请求URL

[https://api.toponad.net/v2/fullreport](https://openapi.toponad.com/v2/fullreport)

## 2. 请求方式

POST

## 3. 请求参数

| **字段** | **类型** | **是否必传** | **备注** | **样例** |
| --- | --- | --- | --- | --- |
| startdate | Int | Y | 开始日期，格式：YYYYmmdd | 20190501 |
| enddate | Int | Y | 结束日期，格式：YYYYmmdd | 20190506 |
| app\_id\_list | Array[String] | N | 开发者后台的应用ID列表 | [“a600e6fbeac98c”] |
| placement\_id\_list | Array[String] | N | 开发者后台的广告位ID列表 | [“b601ce4ca8de81”] |
| time\_zone | String | N | 时区，枚举值：UTC-8、UTC+8、UTC+0，不传则默认使用开发者账号时区 | “UTC-8” |
| network\_firm\_id\_list | Array[int32] | N | 广告平台ID列表，一些特殊平台ID:  TopOn Adx: 66  TopOn 交叉推广: 35 | [1,2] |
| adsource\_id\_list | Array[int32] | N | 广告源ID列表 | [121] |
| area\_list | Array[String] | N | 国家列表 | [“US”,"CN"] |
| group\_by | Array[String] | N | 筛选维度列表，注意：最多只允许6个维度，支持的维度如下：  date（日期，默认值）， app（应用）， placement（广告位）， adformat（广告样式）， area（地区）， network（广告平台账号）， adsource（广告源）， network\_firm\_id（广告平台）， scenario（广告场景）， traffic\_group（流量分组）， channel（渠道）， sdk\_version（sdk版本）， app\_version（应用版本），abtest（ab测试） | ["app","placement","area"] |
| metric | Array[String] | N | 当同时选了all和其他指标时即返回全部指标： default（默认的一些指标：dau，arpu，request，fillrate，impression，click，ecpm，revenue，impression\_api，click\_api，ecpm\_api）， all（全部指标），  dau（DAU）, arpu（人均收益，单位美元）， cy\_arpu（人均收益，单位按开发者币种）， request（广告请求数）， fillrate（广告填充率）， impression（展示数）， click（点击数），  ctr（点击率），  ecpm（ECPM）， revenue（收益），  request\_api（三方广告平台的广告请求数），  fillrate\_api（三方广告平台的广告填充率），  impression\_api（三方广告平台的展示数），  click\_api（三方广告平台的点击数），  ctr\_api（三方广告平台的点击率），  ecpm\_api（三方广告平台的ECPM），  estimate\_revenue（预估收益，美元单位）， estimate\_revenue\_ecpm（预估ECMP，美元单位）， ready\_request（isReady调用次数）， ready\_rate（isReady成功率）， cy\_estimate\_revenue（按开发者账号币种返回的预估收益）， cy\_estimate\_revenue\_ecpm（按开发者账号币种返回的预估ECMP） bid\_request（竞价，仅竞价广告源会返回此数据。） bid\_filled\_request\_rate(竞价响应率，仅竞价广告源会返回此数据） bid\_filled\_request\_ecpm(竞价响应eCPM，仅竞价广告源会返回此数据，按开发者账号币种返回)  full\_app\_revenue(对应Meta App的整体收益，只有当前账号有Meta数据时才会返回。不支持维度拆分，所有维度均仅返回对应Meta App的数据) | ["dau","arpu","request","click","ctr\_api"] |
| start | Int | N | 偏移数，代表从第几条数据开始，默认为0 | 0 |
| limit | Int | N | 每次拉取数据的最大条数，默认是1000，可选[1,1000] | 1000 |

## 4. 返回参数

|  |  |  |  |
| --- | --- | --- | --- |
| 字段 | 类型 | 是否必传 | 备注 |
| records | Array[Object] | N | 记录，对象数组每个record结构见下面records元素结构，无数据时为空 |
| count | Int | N | 总条数，无数据时为空 |
| currency | String | N | 开发者账号币种，该字段与revenue字段组成的收益需与开发者后台报表的收益一致 |
| time\_zone | String | N | 时区，枚举值：UTC+8、UTC+0、UTC-8 |

**records数据字段：**

| **字段** | **类型** | **是否必传** | **备注** |
| --- | --- | --- | --- |
| date | String | Y | 日期，格式：YYYYmmdd。group\_by有选才有返回 |
| app | Object | N | 应用信息，group\_by有选app维度时才返回 |
| app.id | String | N | 开发者后台的应用ID |
| app.name | String | N | 应用名称 |
| app.platform | String | N | 应用的系统平台 |
| app.pkg\_name | String | N | 应用的包名 |
| placement | Object | N | 广告位信息，group\_by有选placement维度时才返回 |
| placement.id | String | N | 开发者后台的广告位ID |
| placement.name | String | N | 广告位名称 |
| adformat | String | N | 广告样式，group\_by有选adformat维度时才有返回，枚举值：Rewarded Video、Interstitial、Banner、Native、Splash |
| area | String | N | 国家码。group\_by有选area维度时才有返回 |
| network\_firm\_id | String | N | 广告平台ID，group\_by有选network\_firm\_id维度才有返回 |
| network\_firm | String | N | 广告平台名称，group\_by有选network\_firm\_id维度才有返回 |
| network | String | N | 广告平台账号ID，group\_by有选network维度才有返回 |
| network\_name | String | N | 广告平台账号名称，group\_by有选network维度才有返回 |
| adsource | Object | N | 广告源信息，group\_by有选adsource维度时才返回 |
| adsource.network | String | N | 广告源所属的广告平台名称 |
| adsource.token | String | N | 广告源的三方ID信息，请求广告的appid，slotid等 |
| adsource.slot\_id | String | N | 第三方广告平台ID |
| adsource.adsource\_id | String | N | 广告源id |
| adsource.adsource\_name | String | N | 广告源名称 |
| scenario | Object | N | 广告场景信息，group\_by有选scenario维度时才返回 |
| scenario.id | String | N | TopOn内部广告场景id（"1"代表默认场景），仅用于TopOn内部标记广告场景，开发者请使用custom\_uuid字段进行广告场景匹配 |
| scenario.name | String | N | 广告场景名称 |
| scenario.custom\_uuid | String | N | 自定义广告场景ID（"1"代表默认场景），对应后台广告场景管理页面显示的广告场景ID，即SDK上传的广告场景ID |
| traffic\_group | Object | N | 流量分组信息，group\_by有选traffic\_group维度时才返回 |
| traffic\_group.id | String | N | 流量分组id |
| traffic\_group.name | String | N | 流量分组名称 |
| traffic\_group.segment\_id | Int | N | 流量分组数字id，注意：默认流量分组时segment\_id=0,不会返回 |
| channel | String | N | 渠道名称，group\_by有选channel维度才有返回 |
| sdk\_version | String | N | SDK版本，group\_by有选sdk\_version维度才有返回 |
| app\_version | String | N | 应用版本，group\_by有选app\_version维度才有返回 |
| abtest | Object | N | ab测试，group\_by有选abtest维度才有返回 |
| abtest.t\_g\_id | Int | N | ab切量id, 注意：不存在ab测试也有值，存在ab则表示分组id |
| abtest.id | Int | N | ab测试id |
| abtest.name | Stirng | N | ab测试名称 |
| abtest.group\_item\_id | Int | N | ab测试分组id |
| abtest.group\_item\_name | String | N | ab测试分组名称 |

**指标：**

| **字段** | **类型** | **是否必传** | **指标类型** | **指标分类** | **备注** |
| --- | --- | --- | --- | --- | --- |
| dau | String | N | TopOn数据 | 用户行为 | DAU，根据group\_by条件才有返回 |
| deu | String | N | DEU |
| engaged\_rate | String | N | 渗透率 |
| imp\_dau | String | N | 展示 / DAU |
| imp\_deu | String | N | 展示 / DEU |
| dau\_launch | int | N | 启动DAU，注意：该值为0时，响应不返回该指标 |
| new\_users | String | N | 新用户 |
| new\_user\_rate | String | N | 新用户占比 |
| launch | String | N | 应用启动次数(2026.04.01后支持) |
| per\_dau\_launch | String | N | 人均启动次数(2026.04.01后支持) |
| cy\_estimate\_revenue | String | N | 收益数据 | 预估收益，按开发者账号币种返回的预估收益 |
| cy\_estimate\_revenue\_ecpm | String | N | 预估收益，按开发者账号币种返回的预估eCPM，计算方式和estimate\_revenue\_ecpm一样 |
| estimate\_revenue | String | N | （后续会下线，不推荐使用）预估收益，币种：美元 |
| estimate\_revenue\_ecpm | String | N | 预估eCPM，根据预估收益和TopOn统计的展示计算出预估eCPM，计算公式：（预估收益/TopOn统计的展示）\*1000。注： 1、预估 eCPM当天提供； 2、常规广告源基于手动填写的eCPM价格计算，竞价广告源基于实时竞价价格计算 |
| ecpm | String | N | eCPM，TopOn通过报表API向广告平台拉取到的实际收益和TopOn统计的展示计算出eCPM，计算公式：（收益/TopOn统计的展示）\*1000。注：eCPM延迟1天提供 |
| ecpc | String | N | eCPC，TopOn通过报表API向广告平台拉取到的实际收益和TopOn统计的点击量计算出eCPC，计算公式：（收益/TopOn统计的点击量）\*1000。注：eCPC 数据延迟1天提供 |
| ecpr | String | N | eCPR，TopOn根据计算的预估收益和统计的请求数计算出eCPR，计算公式：（预估收益/TopOn统计的请求数）\*1000。 |
| estimated\_revenue\_arpdeu | String | N | 预估ARPDEU(2026.04.01后支持) |
| per\_launch\_estimated\_revenue | String | N | 单次启动预估收益(2026.04.01后支持) |
| bid\_request | int | N | 竞价数据 | 竞价，仅竞价广告源会返回此数据 |
| bid\_filled\_request\_rate | String | N | 竞价响应率，仅竞价广告源会返回此数据 |
| bid\_filled\_request\_ecpm | String | N | 竞价响应eCPM，仅竞价广告源会返回此数据，按开发者账号币种返回 |
| waterfall\_win | String | N | 竞价胜出次数(2026.04.01后支持) |
| waterfall\_win\_rate | String | N | 广告竞胜率(2026.04.01后支持) |
| load | String | N | 广告请求展示 | 流量请求，注意：当选了某些group\_by维度(例如：network\_firm\_id)，响应为“0” |
| loads\_filled | int | N | 流量填充数，注意：当选了某些group\_by维度(例如：network\_firm\_id)，或者该值为0时，响应不返回该指标 |
| load\_fillrate | String | N | 流量填充率，注意：当选了某些group\_by维度(例如：network\_firm\_id)，响应不返回该指标 |
| request | String | N | 广告源请求 |
| request\_filled | int | N | 广告源填充数，注意：该值为0时，响应不返回该指标 |
| fillrate | String | N | 广告源填充率 |
| impression | String | N | 展示 |
| impression\_rate | String | N | 展示率 |
| click | String | N | 点击 |
| ctr | String | N | 点击率 |
| ready\_request | String | N | 广告Ready数据 | 查询isReady |
| ready\_rate | String | N | isReady成功率 |
| scenario\_entry | int | N | 到达广告场景，注意：该值为0时，响应不返回该指标 |
| scenario\_entry\_ready\_rate | String | N | 广告Ready率 |
| day2\_retention | String | N | 其他数据 | 次日留存（后台无此指标） |
| revenue\_gap | String | N | 收益GAP |
| ecpm\_gap | String | N | eCPM GAP |
| impression\_gap | String | N | 展示Gap |
| click\_gap | String | N | 点击Gap |
| load\_cost\_time | Int | N |  | 流量填充总耗时(2026.04.01后支持)  单位：毫秒  备注：当天无数据，至少T-1天才有数据  平均耗时=load\_cost\_time/1000/loads\_filled |
| request\_cost\_time | Int | N |  | 广告源填充总耗时(2026.04.01后支持)  单位：毫秒  备注：当天无数据，至少T-1天才有数据  平均耗时=request\_cost\_time/1000/request\_filled |
| request\_api | String | N | API数据 | 广告请求展示 | 请求API |
| fillrate\_api | String | N | 填充率API |
| impression\_api | String | N | 展示API |
| click\_api | String | N | 点击API |
| ctr\_api | String | N | 点击率API |
| per\_launch\_impression | String | N | 单次启动广告展示数(2026.04.01后支持) |
| per\_launch\_click | String | N | 单次启动广告点击数(2026.04.01后支持) |
| cy\_arpu | String | N | 收益数据 | ARPDAU，有dau才有该项返回，单位：按开发者账号币种 |
| arpu | String | N | （后续会下线，不推荐使用）ARPDAU，有dau才有该项返回，单位：美元 |
| estimated\_revenue\_arpu | String | N | 预估ARPDAU，有dau才有该项返回，单位：按开发者账号币种 |
| revenue | String | N | 收益API，币种为开发者账号币种 |
| ecpm\_api | String | N | eCPM API，TopOn通过报表API向广告平台拉取到的实际收益和展示API计算出eCPM API，计算公式：（收益/展示API）\*1000。注：eCPM API延迟1天提供 |
| unit\_ecpc | String | N | eCPC API，计算公式：媒体收益/媒体侧点击次数\*1000。注：eCPC API延迟1天提供 |
| unit\_ecpr | String | N | eCPR API，计算公式：收益API/请求API \*1000。部分广告平台不支持请求API数据，请区分广告平台查看此指标。注：eCPR API延迟1天提供 |

## 5. 样例

请求样例：

```
curl --location --request POST 'https://api.toponad.com/v2/fullreport' \
--header 'X-Up-Key: 877f8ae9c6e9ca82c0==5b5fff594c373axxx' \
--header 'X-Up-Signature: CE12B506DBCD868C2C6F09E08C139CBC' \
--header 'X-Up-Timestamp: 1626161553000' \
--header 'Content-Type: application/json' \
--data-raw '{
    "startdate": 20210201,
    "enddate": 20210223,
    "group_by": ["adsource"],
    "metric": ["all"],
    "limit": 1000,
    "start": 0,
    "app_id_list": ["a6012251c3df52"],
    "placement_id_list": ["b601226022d218"]
}'
```

返回样例：

```
{
    "records": [
        {
            "date": "20251021",
            "dau": "28528",
            "arpu": "0",
            "cy_arpu": "0",
            "request": "4184347",
            "fillrate": "0.2345",
            "impression": "67760",
            "click": "18594",
            "ctr": "0.2744",
            "ecpm": "0.00",
            "revenue": "0",
            "request_api": "0",
            "impression_api": "0",
            "click_api": "0",
            "new_users": "6936",
            "day2_retention": "0.4145",
            "deu": "7117",
            "engaged_rate": "0.2494",
            "imp_dau": "2.3752",
            "imp_deu": "9.5208",
            "impression_rate": "0.1409",
            "new_user_rate": "0.2431",
            "estimate_revenue": "4032.975963",
            "estimate_revenue_ecpm": "59.52",
            "ready_request": "5320553",
            "ready_rate": "0.3941",
            "cy_estimate_revenue": "4032.975963",
            "cy_estimate_revenue_ecpm": "59.52",
            "load": "612540",
            "load_fillrate": "0.7849",
            "bid_request": 3627547,
            "bid_filled_request_rate": "0.4785",
            "bid_filled_request_ecpm": "38.65",
            "loads_filled": 480796,
            "request_filled": 981626,
            "dau_launch": 14416,
            "ecpc": "0.00",
            "ecpr": "0.5888",
            "estimated_revenue_arpu": "0.1413",
            "full_app_revenue": "0"
        }
    ],
    "time_zone": "UTC+8",
    "count": 1,
    "currency": "USD"
}
```
