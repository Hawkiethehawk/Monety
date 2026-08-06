---
title: "三方平台广告位创建"
source: "https://help.toponad.net/cn/docs/san-fang-ping-tai-guang-gao-wei-chuang-jian"
captured_at: "2026-07-21T08:07:23Z"
site_modified: "2026-07-02"
category_path: ["Open API接入指南", "附录", "三方平台广告位创建"]
content_sha256: "1c4b328e775b531c71425a4158317b907f3594b98585316b7939b908ae8a6da3"
knowledge_role: "reference_only"
has_article_body: true
---

# 三方平台广告位创建

## 注意：接入Api前请先熟悉api签名机制（参考[接口鉴权说明](/docs/9NzgWP)）, 即Api请求样例中的一些http请求头的来源

## 1. 三方平台广告位创建

**采用透传方式协助开发者快捷创建三方平台广告位，需要开发者预先在开发者后台的广告平台创建广告平台账号。三方平台的请求签名由TAKU平台实现，开发者只要专注三方平台的参数组装**。

技术实现流程：

![](https://cdn-customer.helplook.net/_hl/load-img.DSGdRIBO.png)

 支持平台：

|  |  |
| --- | --- |
| 平台名称 | 三方文档地址 |
| Meta | 联系平台获取或查看附件 |
| Unity | [官方文档](https://services.docs.unity.com/monetize/v1/#tag/Ad-Units/operation/createAdUnits) |
| Fyber | [官方文档](https://developer.digitalturbine.com/hc/en-us/articles/4409541086993-DT-FairBid-Management-API) |
| Pangle | [官方文档](https://www.pangleglobal.com/zh/integration/management-api) |
| Bigo | [官方文档](https://www.bigossp.com/guide/sdk/reportingApi/doc?type=2) |
| Taurusx | [官方文档](https://publisher.taurusx.com/knowledge/zh/platform/api/management.html#_3-1-%E5%B9%BF%E5%91%8A%E4%BD%8D%E5%88%9B%E5%BB%BA) |
| Yandex | [官方文档](https://yandex.ru/dev/partner-statistics/doc/en/reference/mobile-adunit/) |
| Vungle | [官方文档](https://support.vungle.com/hc/en-us/articles/360041251552-Publisher-Management-API-1-3) |
| Inmobi | [官方文档](https://support.inmobi.com/monetize/inmobi-apis/ad-management-api/api-details#manage-placements) |
| Mintegral | [官方文档](https://cdn-adn-https.rayjump.com/cdn-adn/open_api/MintegralAPI.html)  备注：Mintegral的三方创建会创建placement和unit,三方参数要传递两个维度参数，如third\_unit\_params：{"placement":{},"unit":{}} |
| Admob | [官方文档](https://developers.google.cn/admob/api/reference/rest?hl=zh-cn) |

##

#### 1.1 请求URL

[https://api.toponad.com/v3/third\_unit](https://openapi.toponad.com/v3/third_unit)

#### 1.2 请求方式

POST

#### 1.3 请求参数

| 字段 | 类型 | 是否必传 | 备注 |
| --- | --- | --- | --- |
| network\_id | Int | Y | 开发者后台的广告平台账号id |
| third\_unit\_params | Object | Y | 三方广告位创建透传参数 |

####

#### 1.4 样例

请求样例：

```
curl --location --request POST 'https://api.toponad.com/v3/third_unit' \
--header 'X-Up-Key: 877f8ae9c6e9ca82c0==5b5fff594c373axxx' \
--header 'X-Up-Signature: CE12B506DBCD868C2C6F09E08C139CBC' \
--header 'X-Up-Timestamp: 1626161553000' \
--header 'Content-Type: application/json' \
--data-raw '{
    "network_id": 4779,
    "third_unit_params": {
        "app_id": 5299426,
        "ad_slot_name": "穿山甲_splash_1-b1grl9cfl7ciqp-1797",
        "ad_slot_type": 3,
        "currency": "cny",
        "use_mediation": "0",
        "bidding_type": 0,
        "cpm": "1",
        "render_type": 3,
        "use_icon": 2,
        "orientation": 1,
        "splash_shake": 1
    }
}'
```

返回样例：

```
{
    "third_unit_id": "5299426"
}
```

#### 1.5 附件

附件：

meta：[AN-Onboarding-Management-API.pdf](https://resource-wangsu.helplook.net/docker_production/5expvy/article/QWh7z3Lc/attachments/AN-Onboarding-Management-API.pdf "AN-Onboarding-Management-API.pdf")
