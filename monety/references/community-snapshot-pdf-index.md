# 社区网页 PDF 快照索引

核验日期：2026-10-15（Asia/Shanghai）。这是 Monety 的 PDF 快照入口；完整递归链接清单和每个文件的状态见 [output manifest](../../output/pdf/community-web-snapshots/manifest.md)。

## 优先阅读

| 类型 | PDF | 用途 | 状态 |
|:---|:---|:---|:---|
| Reddit 个人经验 | [admob-network-experience.pdf](../../output/pdf/community-web-snapshots/reddit/admob-network-experience.pdf) | 多广告网络、eCPM/fill、支付、支持和账号风险 | `text-fallback` |
| Reddit 优化帖 | [admob-revenue-tips.pdf](../../output/pdf/community-web-snapshots/reddit/admob-revenue-tips.pdf) | mediation、bidding、预加载、fallback、频控和隐私 | `text-fallback` |
| Meta 测试页 | [meta-testing-status.pdf](../../output/pdf/community-web-snapshots/official/meta-testing-status.pdf) | 记录登录/阻断状态，不把登录页当正文 | `blocked` |
| Meta app-ads.txt | [meta-app-ads-txt.pdf](../../output/pdf/community-web-snapshots/official/meta-app-ads-txt.pdf) | 官方授权销售方机制 | `rendered` |
| AdMob bidding | [admob-bidding.pdf](../../output/pdf/community-web-snapshots/official/admob-bidding.pdf) | 官方实时竞价机制 | `rendered` |
| AdMob A/B | [admob-ab-test.pdf](../../output/pdf/community-web-snapshots/official/admob-ab-test.pdf) | 官方实验边界 | `rendered` |
| AdMob floor | [admob-floor.pdf](../../output/pdf/community-web-snapshots/official/admob-floor.pdf) | 官方底价行为 | `rendered` |
| TopOn waterfall | [topon-waterfall.pdf](../../output/pdf/community-web-snapshots/official/topon-waterfall.pdf) | 官方瀑布与排序说明 | `rendered` |
| TopOn A/B | [topon-ab-test.pdf](../../output/pdf/community-web-snapshots/official/topon-ab-test.pdf) | placement/segment 实验指标 | `rendered` |

## 使用边界

- `rendered` 是浏览器打印的页面快照，可作为官方机制或页面事实的离线参考。
- `text-fallback` 是搜索索引正文的 PDF；保留正文和附属链接，但不声称保存了完整 HTML、图片或评论加载状态。
- `blocked` 是登录、Cloudflare 或网络安全阻断状态。它只证明抓取限制，不支持页面正文结论。
- 个人经验按 B+/B/B- 权重使用；`text-fallback` 只降低页面完整性信心，不自动降低经验等级：可用于经验性策略、问题排查顺序和实验优先级；仍必须用 Monety 用户自己的 TopOn/AdMob 报表和客户端事件复测，不能直接作为当前应用的因果结论。
