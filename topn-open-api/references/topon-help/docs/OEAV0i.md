---
title: "开发者后台管理API"
source: "https://help.toponad.net/cn/docs/OEAV0i"
captured_at: "2026-07-21T08:07:23Z"
site_modified: "2025-05-30"
category_path: ["Open API接入指南", "开发者后台管理API"]
content_sha256: "57442d73ce70f3ab28e28dc6be4b2b475aa35609ef89dbe1490c30271c6fc298"
knowledge_role: "reference_only"
has_article_body: true
---

# 开发者后台管理API

# 1. 修订历史

| 文档版本 | 发布时间 | 修订说明 |
| --- | --- | --- |
| v 2.5 | 2021年10月10日 | 新增A/B测试 |
| v 2.4 | 2021年3月18日 | 按账号币种返回ecpm价格、支持自定义广告源的创建和上传三方数据 |
| v 2.3 | 2020年8月20日 | 新增华为广告平台、Google Ad Manager |
| v 2.2 | 2020年5月14日 | 流量分组接口功能调整 |
| v 2.1 | 2020年3月16日 | 新增广告平台、广告源管理接口 |
| v 2.0 | 2019年11月4日 | 支持Waterfall、流量分组等相关配置 |
| v 1.0 | 2019年7月17日 | 支持批量创建和查询应用、广告位 |

# 2. 使用流程

为提高合作伙伴的变现效率，TopOn平台专门提供了对接开发者后台相关操作的API接口，如创建应用和广告位、调整Waterfall优先级等。该文档详细描述了API的使用方法，如需要帮助，请及时与我们联系，谢谢！

使用api实现聚合变现简单流程：

1.使用api(应用管理Api1)创建TopOn应用（app\_id）

2.使用api(广告位管理Api1)创建TopOn广告位（placement\_id）

3.使用api(广告平台管理Api1)创建TopOn平台账号（network\_id）并绑定三方network,app参数到TopOn应用

4.使用api(广告源管理（新版v3）Api3)创建TopOn广告源

5.使用api(聚合管理的广告源管理Api2或Api5)绑定广告源到指定流量分组，设置ecpm并开启广告源

各api模块功能逻辑图：

![](https://cdn-customer.helplook.net/_hl/load-img.DSGdRIBO.png)

# 3. 限流说明

请勿使用爬虫抓取开发者后台报表数据，违者将被封号处理！

接口限流说明如下(尽量避免触发限流机制，频繁刷接口有可能被封号处理)：

| 限流方案 | 接口调用调优 |
| --- | --- |
| 单个开发者调用单个接口的并发请求数不超过1次 | 开发者的定时任务需使用串行的方式 |
| 单个开发者每分钟调用单个接口次数不超过30次 | 相同维度数据需要多次分页时，每次分页后间隔一小段时间再获取 |
| 单个开发者每半小时调用单个接口次数不超过400次 | 避免重复获取等 |
