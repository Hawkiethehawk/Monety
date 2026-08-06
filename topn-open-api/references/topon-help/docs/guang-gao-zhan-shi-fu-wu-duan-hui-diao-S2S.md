---
title: "广告展示收益服务端回调API（S2S）"
source: "https://help.toponad.net/cn/docs/guang-gao-zhan-shi-fu-wu-duan-hui-diao-S2S"
captured_at: "2026-07-21T08:07:23Z"
site_modified: "2026-05-20"
category_path: ["Open API接入指南", "广告展示收益服务端回调API（S2S）"]
content_sha256: "21329e56355464158a654e4263fb2ff8cba4b02f1ec4aa965ead4b1968f602fe"
knowledge_role: "reference_only"
has_article_body: true
---

# 广告展示收益服务端回调API（S2S）

提前注意：

1. 开发者需要保证自己服务器接收数据能力（建议开发者服务器只接收数据，之后另起服务或其它异步处理数据逻辑），TopOn回调失败时（比如2秒超时，或者开发者服务器响应失败状态码）不会重新回调
2. 开发者需要自己作去重处理，req\_id和adsource\_id做过滤标识
3. 回调成功后开发者服务器需要响应http状态码200，其它状态码为失败标识
4. 请与您的AM沟通开通此功能权限并提供接收回调的地址。

1. 请求方式： GET

2. 回调参数：

|  |  |  |
| --- | --- | --- |
| **参数** | **类型** | **说明** |
| user\_id | string | 用户ID，由开发者设置，由SDK上报的开发者自定义信息，在tk的custom参数中的user\_id字段 |
| req\_id | string | TopOn提供，需要开发者使用req\_id和adsource\_id结合进行去重 |
| geo\_short | string | 国家短码， 例如："CN" |
| package\_name | string | 当前应用包名，例如：com.happy.xx |
| adformat | int | 广告类型，枚举说明如下：  0："Native”  1："RewardedVideo"  2："Banner"  3："Interstitial"  4："Splash" |
| placement\_id | string | Taku广告位ID，由SDK上报，例如：“bxxxx2323232677” |
| nw\_firm\_id | int | 三方广告平台对应的ID，例如：1：meta，具体映射关系参考：<https://help.takuad.com/docs/2KR6QU> |
| adsource\_id | int | 广告源ID，由SDK上报，例如：5003245 |
| adsource\_price | double | ECPM，即单次广告展示ecpm：例如：3.24 |
| currency | string | 货币单位（暂时一定是美元），例如："USD" |
| timestamp | int64 | SDK端广告展示时间戳，单位毫秒 |
| client\_ip | string | 用户IP |
| gaid | string | Google的广告设备ID，仅安卓平台显示 |
| oaid | string | 安卓的设备ID |
| imei | string | 安卓的设备ID |
| idfa | string | iOS的设备ID |
| idfv | string | iOS的设备ID |
| amazon\_id | string | amazon设备ID（sdk6.2.50及以上版本支持），android系统独有 |
| show\_custom\_ext | string | 展示自定义扩展参数（sdk6.3.10及以上版本支持），  注意：是字符串，例如："{\"tag\":11}" |
