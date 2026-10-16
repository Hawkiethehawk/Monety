# 社区与平台网页文本快照

> 快照日期：2026-10-15（Asia/Shanghai）。本文件保存公开页面的可读文本摘录、页面元数据和抓取状态，供 Monety 离线分析参考。它不是完整 HTML 归档；社区页面可能动态加载、被编辑、删除或发生链接漂移，使用时仍需保留来源编号和原始 URL。

## 快照状态

- `readable`：搜索提取内容与页面标题一致；个人案例可按 B+/B/B- 评估，官方页面可作 A 级机制摘录。
- `indexed-excerpt`：页面正文当前不可稳定读取，但搜索索引保留了历史摘录；只能作为待复核线索。
- `mismatch`：URL 当前返回的页面与原案例标题不一致；不把当前返回内容用于结论。

## PDF 网页快照

本目录对应的 PDF 文件和递归附属链接清单保存在 [PDF manifest](../../output/pdf/community-web-snapshots/manifest.md)。清单区分 `rendered`、`text-fallback`、`blocked` 和 `mismatch`：

- Reddit 主帖及其引用帖已保存为文本回退 PDF，因为直连、JSON 和 old.reddit 均返回 403；PDF 内同时保留索引正文和正文/评论中识别出的附属链接。
- 可访问的 AdMob、TopOn、Meta、Google Play、Pangle、Stack Overflow、GameZop 等页面已用浏览器打印 PDF。
- Meta 测试页、AdMob 账号页和 Cloudflare 拦截页保存为访问状态 PDF，不把空白页或登录页当作正文。

优先入口：

- Reddit 主帖：[admob-network-experience.pdf](../../output/pdf/community-web-snapshots/reddit/admob-network-experience.pdf)
- Reddit 引用帖：[admob-revenue-tips.pdf](../../output/pdf/community-web-snapshots/reddit/admob-revenue-tips.pdf)
- 附属链接清单：[manifest.md](../../output/pdf/community-web-snapshots/manifest.md)

## Reddit

### reddit-max

- 状态：`readable`
- 标题：`Applovin Max VS Admob Mediation! Which is better, MY RESULTS >>>`
- 页面日期：2023-10-03
- 来源：**[IAA-COMM-REDDIT-01-AdMob 与 MAX 对照]**
- URL：https://www.reddit.com/r/admob/comments/16vubir/applovin_max_vs_admob_mediation_which_is_better/
- 摘录：作者将新版本用户 50/50 分到 MAX 和 AdMob，使用 AdMob、AppLovin、Pangle、Mintegral、Meta、Unity，按 US、巴西、墨西哥、阿根廷分别投放测试。作者及评论称 MAX eCPM 略高，但展示量约少一半，AdMob mediation 的 fill/impressions 更高，最终更适合比较总收入而非单价。
- 快照判断：个人对照实验，保留地区、版本和分流信息；未保存完整报表，证据 B。

### reddit-requests

- 状态：`mismatch`
- 预期标题：`How I quadrupled my AdMob revenue by REDUCING my ad requests (From $1 to $4/day with 400 DAU)`
- URL：https://www.reddit.com/r/admob/comments/1s7pqxp/case_study_how_i_quadrupled_my_admob_revenue_by/
- 当前抓取结果：该 URL 当前被 Brave 索引为另一篇“15 apps/games to make $1/day”帖子，不能确认是原案例页面。
- 历史检索摘录：原案例被索引为 DAU 约 200–400，收入由约 0.5–1 美元/天升至 3–4 美元/天；作者减少无展示价值的 native/rewarded 预加载，评论提到 native eCPM 约由 3.95 美元升至 6.90 美元。
- 快照判断：只保留为待复核线索，不作为已核验事实；分析时应优先用用户自己的 request、show rate 和 eCPM 数据。

### reddit-floor

- 状态：`readable`
- 标题：`Absurd difference in revenue between eCPM Floor VS Disabled`
- 页面日期：2024-01-07
- 来源：**[IAA-COMM-REDDIT-03-Floor 对照]**
- URL：https://www.reddit.com/r/admob/comments/190r3e9/absurd_difference_in_revenue_between_ecpm_floor/
- 摘录：作者称约 30k 用户的应用测试两个 banner 数月；开启 Google eCPM floor 的单元收入反而较低，关闭 floor 的 banner 只用了约三分之一的 impressions/clicks，却有 2–3 倍收入。评论也提到 floor 变化可能需要约一周或更长时间学习，不能只看短期结果。
- 快照判断：有对照方向，但两个广告位可能存在 CTR、位置和用户构成差异，证据 B。

### reddit-networks

- 状态：`readable`
- 标题：`My experience with the various ad-networks for Admob mediation`
- 页面日期：2026-09-24
- 来源：**[IAA-COMM-REDDIT-04-广告网络长期经验]**
- URL：https://www.reddit.com/r/admob/comments/1oy8gjd/my_experience_with_the_various_adnetworks_for/
- 摘录：作者按广告形式列出多个网络的个人 eCPM 排名，明确强调 eCPM 不是全部，fill rate 也很重要；其多个应用中 AdMob 约占广告总收入 90%，Meta 和 Liftoff/Vungle 是主要补充。作者还记录了 app-ads.txt、支持、支付、崩溃和账号限制等运维差异。
- 快照判断：长期多应用经验，能用于提出需求源与运维成本假设；排名不能外推到其他 GEO，证据 B。

### reddit-game

- 状态：`readable`
- 标题：`I made my first 1500$ from my free mobile game: here is what worked, and what didn't`
- 页面日期：2026-03-12
- 来源：**[IAA-COMM-REDDIT-05-免费游戏复盘]**
- URL：https://www.reddit.com/r/gamedev/comments/1rrswso/i_made_my_first_1500_from_my_free_mobile_game/
- 摘录：作者称一年累计收入超过 1,500 美元，游戏只使用 rewarded，不使用 banner 或强制插屏；通常每天 100–500 impressions、广告收入约 2–10 美元。每次完整观看约 0.001–0.03 美元。早期单用户一天观看 500 次，超过约 20 次后几乎不再赚钱，作者因此为奖励广告设置上限。
- 快照判断：有时间范围、收入、展示量和频控复盘，仍是单一游戏自报数据，证据 B。

### reddit-meta

- 状态：`readable`
- 标题：`Facebook mediation extremely low Match Rate`
- 页面日期：2025-11-27
- 来源：**[IAA-COMM-REDDIT-06-Meta 低填充]**
- URL：https://www.reddit.com/r/admob/comments/1p87jqo/facebook_mediation_extremely_low_match_rate/
- 摘录：作者称 AdMob match 约 60%，接入 Meta 后 Meta match 约 2%，日活约 4,000，主要用户来自印度、巴基斯坦。评论将低填充归因于用户未登录 Facebook、未安装 Facebook 或无法被 Meta 识别；该归因需要按实际 consent、设备和 GEO 验证。
- 快照判断：适合提出“Meta 按 GEO 做增量测试”的假设，不能当作 Meta 的通用填充率，证据 B。

## V2EX

### v2ex-topon

- 状态：`readable`
- 标题：`关于广告优化问题，同一个 iOS 应用，穿山甲和优量汇的收益差别`
- 页面日期：2021-03-18
- 来源：**[IAA-COMM-V2EX-01-TopOn 国内流量测试]**
- URL：https://v2ex.com/t/762911
- 摘录：帖子称同一 iOS 应用平均约 1,000 UV，只接开屏和激励视频，日收益约 200 元；开发者使用 TopOn 聚合。穿山甲展示量约为优量汇 2 倍，开屏 eCPM 接近，激励视频穿山甲高数倍。作者建议按广告位调比例，并提醒小流量很难测出最佳比例。
- 快照判断：原文数据由广告联盟经营者发布，存在业务利益，证据 B-，且年份较旧。

### v2ex-ban

- 状态：`readable`
- 标题：`独立开发者往事#8`
- 页面日期：2023-05-08
- 来源：**[IAA-COMM-V2EX-02-AdMob 封号复盘]**
- URL：https://v2ex.com/t/938170
- 摘录：作者称 2021-04-13 收到 AdMob 封禁邮件；随后接入 MoPub、AppLovin 和 Unity3D，2021 年 5 月广告总收入为 4,674，约为原来的三分之一。作者反思账号被封与未遵守官方规范有关，并记录了通过每日小实验逐步恢复产品状态的过程。
- 快照判断：收入断崖和平台风险是个人复盘，不足以判断封禁原因，证据 B。

### v2ex-year

- 状态：`readable`
- 标题：`独立开发者的 2025 年终总结`
- 页面日期：2026-01-07
- 来源：**[IAA-COMM-V2EX-03-长期独立开发周报]**
- URL：https://v2ex.com/t/1183856
- 摘录：作者公开下载和收入变化：App Store 下载约 363,330、Google Play 约 182,655、国内安卓约 185,007；App Store 收入提高 40%，Google Play 下降 45.71%，AdMob 下降 59%，国内安卓提高 45.63%。首次 Onboarding 后立即展示 paywall 曾短期提升收入，之后回落；一个只有激励广告但没有用户的游戏收入为零。
- 快照判断：长期独立开发公开记录，绝对 AdMob 金额不完整，证据 B。

## 知乎

### zhihu-reward

- 状态：`readable`
- 标题：`想接视频，想请教一下几家平台中如何选择？ - 路人 的回答`
- 来源：**[IAA-COMM-ZHIHU-01-激励视频场景]**
- URL：https://www.zhihu.com/question/53112584/answer/272598400
- 摘录：自称游戏开发者，使用过多家平台；以游戏中的双倍金币、额外任务、死亡复活为例，说明 rewarded 需要给用户明确且即时的价值，并尽量与页面自然融合，降低打扰。
- 快照判断：场景设计有参考价值，但回答较早、没有后台对照数据，证据 B-。

### zhihu-floor

- 状态：`indexed-excerpt`
- 标题：`Admob“由Google优化“设置底价功能，需谨慎使用`
- 来源：**[IAA-COMM-ZHIHU-02-Floor 个人复盘]**
- URL：https://zhuanlan.zhihu.com/p/593934108
- 当前页面状态：直接抓取时返回了与 AdMob 无关的页面，原页面内容发生链接漂移或被替换。
- 历史索引摘录：作者称 T3 流量使用 AdMob 自动优化“适中的底价”后经历约三周明显波动，后来回退配置；作者建议人工 floor 也必须结合自身流量测试。
- 快照判断：只作待复核线索，不作为已核验事实。

## 平台官方文档

### AdMob bidding

- 状态：`readable`
- 标题：`Overview of bidding - Google AdMob Help`
- 来源：**[IAA-ADMOB-01-Mediation 与 bidding]**
- URL：https://support.google.com/admob/answer/9234488?hl=en
- 摘录：bidding 让广告源在实时竞价中竞争填充请求；与依赖历史 eCPM、逐一调用网络的 waterfall 不同，参与 bidding 的广告源同时竞价，最高 eCPM 的广告源进入 mediation waterfall。

### AdMob A/B

- 状态：`readable`
- 标题：`A/B testing in mediation - Google AdMob Help`
- 来源：**[IAA-ADMOB-02-Mediation A/B 测试]**
- URL：https://support.google.com/admob/answer/9572326
- 摘录：可以比较两个 mediation group variant，测试增加/删除广告源、改变 waterfall 顺序、打开或关闭优化，以及改变调用次数；页面明确写出至少需要 10,000 次广告请求才能判断结果。

### AdMob eCPM floor

- 状态：`readable`
- 标题：`About AdMob eCPM floors - Google AdMob Help`
- 来源：**[IAA-ADMOB-03-eCPM floor]**
- URL：https://support.google.com/admob/answer/3418058?hl=en
- 摘录：floor 会阻止低于设定值的 AdMob Network 和 bidding 广告填充，未达到 floor 时请求继续进入 waterfall；floor 不适用于第三方 waterfall 广告源。

### AdMob UMP

- 状态：`readable`
- 标题：`Add the Google User Messaging Platform SDK to your app`
- 来源：**[IAA-ADMOB-05-UMP 与用户同意]**
- URL：https://support.google.com/admob/answer/10113005?hl=en
- 摘录：Google 建议通过 UMP SDK 收集用户同意，并提供隐私政策 URL、同意撤回入口和相关 engagement metrics。

### TopOn waterfall

- 状态：`readable`
- 标题：`Waterfall and optimization tips - TopOn Help center`
- 来源：**[IAA-TOPON-05-Waterfall 结构]**
- URL：https://help.toponad.net/docs/l6kH9E
- 摘录：head bidding 每次请求时返回价格，并与普通广告源按价格排序；TopOn 的 sorting price 主要影响请求优先级和展示顺序，不等同于真实回传价格；分层时应结合实际 eCPM、填充和展示结果。

### TopOn mediation data

- 状态：`readable`
- 标题：`Mediation data - TopOn Help center`
- 来源：**[IAA-TOPON-09-数据来源]**
- URL：https://help.toponad.net/docs/Mediation-data
- 摘录：TopOn 同时提供 SDK 统计和 network report API 数据；默认报表时区为 UTC+8，eCPM 由 API revenue 按展示比例拆分计算，部分数据每天更新，latency 等指标可能次日更新。

### TopOn A/B

- 状态：`readable`
- 标题：`A/B Test - TopOn Help center`
- 来源：**[IAA-TOPON-13-A/B 测试]**
- URL：https://help.toponad.net/docs/J8GsJv
- 摘录：支持最多 10 个测试组、placement 和 segment 两类实验，并展示 Est. Revenue、Request Fill Rate、Imp. Rate、Est. eCPM、Latency 等指标；文档提醒测试组配置不完整时实际分流比例可能偏离设定值。

### Meta App Bidding

- 状态：`readable`
- 标题：`Audience Network`
- 来源：**[IAA-META-01-Audience Network]**
- URL：https://developers.facebook.com/documentation/audience-network
- 摘录：Meta 将 App Bidding 描述为对每次广告机会开放实时竞价，以提高每次请求的优化空间、提供库存真实价值并减少运维工作。

### Meta policy and app-ads.txt

- 状态：`readable`
- 标题：`Policy` 与 `Identifying Authorized Sellers with app-ads.txt`
- 来源：**[IAA-META-02-Audience Network 政策]**、**[IAA-META-03-app-ads.txt]**
- URL：https://developers.facebook.com/docs/audience-network/policy?hc_location=ufi
- URL：https://developers.facebook.com/documentation/audience-network/optimization/best-practices/authorized-sellers-app-ads
- 摘录：Meta 要求广告 placement 信息准确、广告与内容明显区分、避免误触和遮挡，并要求隐私政策；app-ads.txt 用于声明授权销售方和降低供应链欺诈，更新后需要等待平台重新认证。

## 使用快照的规则

1. `readable` 的个人案例可以形成 B+/B/B- 经验性依据，用于优化方向、排查顺序和实验优先级，必须用目标应用的报表或客户端事件复测。
2. `text-fallback` 个人案例保留索引正文和附属链接，但只降低页面完整性信心；原文条件足够清楚时不自动降低 B+/B/B- 经验权重。
3. `indexed-excerpt`、`blocked`、`login-required` 和 `mismatch` 只用于提示搜索方向，不用于支持收入归因或已核验经验。
4. 官方摘录只说明机制和配置边界，不说明某个应用的实时 eCPM、fill 或收入。
5. 分析报告引用时同时写来源编号、快照状态、发布日期、地区/广告形式和局限。
