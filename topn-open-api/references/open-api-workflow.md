# TopOn Open API 工作流

## 数据架构

按以下顺序组织数据，不把不同角色的数据混成一张表：

1. 报表事实层：综合报表是日级主表，小时报表用于日内异常，LTV/留存/展示价值按新增用户 cohort 保存。
2. 配置维度层：应用、广告位、平台账号、广告源、聚合分组、流量分组、Waterfall 和 A/B 测试按抓取时间保存快照。
3. 受限明细层：设备报表和 S2S 展示收益单独存放，默认移除设备标识、IP 和不参与分析的用户标识。
4. 补充对账层：手工导出的综合、漏斗和聚合管理报表只补充 API 缺失字段和核验差异。

完整能力、字段和限制见 `open-api-capabilities.json`。

## 无凭据阶段

初始化项目并登记已知应用：

```powershell
python scripts/init_topon_project.py <project>
python scripts/plan_open_api_collection.py <project-dir> --start-date 2026-07-01 --end-date 2026-07-20 --profile all --include-config --output <project-dir>/derived/open-api-collection-plan.json
```

规划器不访问网络、不读取凭据。没有 `app_id` 时，表现数据请求会标记为 blocked，但应用、广告位等发现请求仍会保留。

## 接口启用前检查

1. 刷新帮助中心镜像，并核对 `index.json` 的抓取时间和失败页数。
2. 核对 `open-api-capabilities.json` 中端点、主机名、参数和已知文档歧义。
3. 在 TopOn 账号管理的 Key 页面创建只含“数据报表查询 API”的子权限 Publisher Key；需要配置快照时再增加开发者管理 API 权限。
4. 通过环境变量或凭据管理器提供 Key，不写入项目、脚本、聊天或分析报告。
5. 用 1 个应用、1 天、1 个页面做冒烟测试。保存脱敏请求摘要、状态码、响应字段和抓取时间。
6. 真实响应与文档不一致时先冻结自动扩量，记录版本差异后再更新解析器。

约定环境变量 `TOPON_REPORT_PUBLISHER_KEY` 保存报表子权限 Key；需要读取后台配置时使用单独的 `TOPON_MANAGEMENT_PUBLISHER_KEY`。先 dry-run 单个计划项：

```powershell
python scripts/execute_open_api_call.py <plan.json> --call fullreport_core
```

确认请求后再执行，并把原始响应放进项目 `raw/open-api/`：

```powershell
python scripts/execute_open_api_call.py <plan.json> --call fullreport_core --execute --output <project-dir>/raw/open-api/fullreport_core.json
```

执行器只接受能力目录登记的 GET/只读 POST，拒绝 PUT、DELETE、写入 POST、未启用计划项和仍含占位符的路径。

## 采集顺序

1. 读取应用、广告位、广告平台账号和广告源，建立 ID 映射。
2. 读取聚合分组、流量分组、Waterfall 和 A/B 测试，形成配置快照。
3. 拉综合报表的多个维度切片。不要用一个 `group_by` 请求同时承担所有分析问题。
4. 拉小时报表；日期跨度超过 10 天时按不超过 10 天切片。
5. 拉 LTV、留存和新用户展示。新用户展示接口一次只能请求一个应用。
6. 获得单独权限且完成隐私评审后，再拉设备报表或启用 S2S 回调。
7. 用同一应用、日期、币种、时区和粒度与后台导出抽样对账。

所有接口按文档限流串行执行。分页按 `count` 校验完整性，每页记录 offset、limit、响应条数和重试次数。错误码 606、609 不得当作空数据；607 只能标记“接口返回空数据”，不能自动记为业务指标为零。

## 综合报表切片

至少保留以下独立切片：

| 切片 | group_by | 用途 |
|---|---|---|
| core | date, app, area | 用户、新用户、收入和主漏斗 |
| placement | date, app, placement, adformat, area | 广告位和样式贡献 |
| supply | date, app, placement, network_firm_id, adsource, area | 平台、广告源、竞价和 GAP |
| scenario | date, app, placement, scenario, area | 场景到达与 Ready |
| traffic_group | date, app, placement, traffic_group, area | 流量分组表现 |
| channel | date, app, area, channel | 渠道与新用户 |
| version | date, app, sdk_version, app_version, area | 版本异常 |
| abtest | date, app, placement, abtest, area | 实验比较 |

TopOn 会根据维度静默省略部分指标。解析器必须区分“字段因请求维度不可用”“响应未返回”“返回 0”三种状态。

## 时效和回补

- 综合报表当天 TopOn 数据约每 10 分钟更新；第三方平台数据通常按两小时更新并延迟 2-3 小时。
- 日常增量重拉最近 2 天。历史数据通常不更新，但权限刚开通或当时数据不完整时允许专项回补。
- 小时报表约每 5 分钟更新，只用于日内监控，不替代稳定后的日级主表。
- LTV、留存和展示价值只能看 T-1 及更早数据，建议 UTC+8 晚 10 点补拉昨天。
- 设备报表只保留最近 30 天，并按时区有 T-1 到 T-3 的生成延迟。

## 原始数据和语义层

每次调用在 `raw/open-api/<endpoint>/<date>/` 保存脱敏响应；在 `derived/open-api/` 保存规范数据和 manifest。manifest 至少包含：

- endpoint、method、resource path、接口文档 URL 和能力目录版本；
- 应用、日期、币种、时区、group_by、metric、筛选项和分页范围；
- 抓取时间、响应条数、`count`、缺页检查、重试和错误码；
- 指标可用性状态、字段类型、公式、聚合规则和已知口径差异。

交给 Data Analytics 前，将返回字段映射到 `metric-catalog.json`。比率由分子分母重算；缺少分母时保留原值并标记不可复算。LTV 是 cohort 总收益，留存字段是人数，新用户展示是人均值，三者不能直接求和或互换。

## 安全和写操作

- 默认只调用读取接口。
- 使用最小权限子 Key。签名时间戳有效期为 15 分钟，Resource 不含 query string。
- 日志不得出现 Publisher Key、签名、完整回调 URL、设备标识或用户标识。
- S2S 以 `req_id + adsource_id` 去重；接收端先快速返回 200，再异步处理。TopOn 不重试失败回调，因此需要监控接收失败率。
- 写操作客户端默认不实现。只有用户明确指定对象、旧值、新值和回滚方案，并在执行前再次确认，才能增加对应写能力。

## 文档维护

准备调用接口前运行：

```powershell
python scripts/crawl_topon_docs.py
python scripts/search_topon_docs.py "Open API 鉴权 限流 接口名称"
```

文档镜像只说明平台设计。真实响应决定当前字段和行为。更新解析器时保留旧版本 manifest，不能静默改写历史分析口径。
