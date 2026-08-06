---
title: "三方广告平台详细参数"
source: "https://help.toponad.net/cn/docs/FSwcAe"
captured_at: "2026-07-21T08:07:23Z"
site_modified: "2026-04-21"
category_path: ["Open API接入指南", "附录", "三方广告平台详细参数"]
content_sha256: "2fca0ecb59520f177f8419789bb1c2e068b54645763497455d21610e33e23acc"
knowledge_role: "reference_only"
has_article_body: true
---

# 三方广告平台详细参数

所有的Key和Value数据类型均为String

| 广告平台ID | 广告平台名称 | auth\_content （所有的key对应的value的值都是string类型） key名称后面带(必填)表示8.1接口创建/修改广告平台无论是否开通报表，都需要传该属性 | app\_auth\_content (所有的key对应的value的值都是string类型） |
| --- | --- | --- | --- |
| 1 | Facebook | - | app\_id  app\_token property\_id |
| 2 | Admob | account\_id oauth\_key | app\_id |
| 3 | Inmobi | username  password apikey app\_id(必填) | - |
| 4 | Flurry | token | sdk\_key |
| 5 | Applovin | sdkkey(必填) apikey | - |
| 6 | Mintegral | skey secret  appkey(必填) | appid |
| 7 | Mopub | repkey apikey | - |
| 8 | 腾讯广告 | ~~当api\_version=1时 agid publisher\_id app\_key qq 当api\_version=2时~~ account\_id secret\_key | app\_id |
| 9 | Chartboost | user\_id  user\_signature | app\_id app\_signature |
| 10 | Tapjoy | apikey | sdk\_key |
| 11 | Ironsource | ~~username~~ secret\_key refresh\_token | app\_key |
| 12 | UnityAds | apikey organization\_core\_id | game\_id |
| 13 | Vungle | apikey account\_id(必填) | app\_id |
| 14 | AdColony | user\_credentials | app\_id |
| 15 | 穿山甲 | （api\_version=1已下线，请使用api\_version=2） ~~当api\_version=1:  user\_id secure\_key~~  当api\_version=2:  user\_id role\_id secure\_key | app\_id |
| 21 | AppNext | email password key | - |
| 22 | Baidu | access\_key | app\_id |
| 23 | Nend | api\_key | - |
| 25 | Start.io | partner\_id token | app\_id |
| 26 | SuperAwesome | - | property\_id |
| 28 | 快手 | access\_key security\_key account\_id(必填) | app\_id app\_name |
| 29 | Sigmob | public\_key secret\_key | app\_id app\_key |
| 32 | MyTarget | access\_token | app\_id |
| 33 | Google Ad Manager | - | - |
| 34 | Yandex | - | - |
| 36 | Ogury | api\_key api\_secret | key |
| 37 | Fyber | publisher\_id consumer\_key consumer\_secret | app\_id |
| 39 | Huawei Ads | client\_id client\_secret | - |
| 40 | Helium | user\_id user\_signature | app\_id app\_signature |
| 49 | Mimo(米盟) | dev\_id app\_secret | app\_id app\_name |
| 50 | Pangle | user\_id secure\_key | app\_id |
| 59 | Bigo | developer\_id token | app\_id |
| 65 | BidMachine | account password | source\_id |
| 74 | Qumeng(趣盟) | secret\_key | app\_id |
| 77 | Kwai | publisher\_id apikey | app\_id app\_token |
| 79 | VIVO 广告联盟 | account\_name secret\_key | media\_id |
| 81 | XiaoMi(小米) | token | app\_key app\_secret |
| 83 | Taurusx | token | app\_id |
| 84 | Smaato | client\_id client\_secret | pub\_id |
| 93 | AdMateX(美数) | agent\_id token | app\_id secure |
| 95 | Beizi(倍孜) | app\_key secret | app\_id |
| 96 | Octopus(章鱼广告) | auth\_code user\_name | app\_id |
