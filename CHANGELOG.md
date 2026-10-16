# Changelog

## Monety 1.2 - 2026-10-16

- 新增 Reddit、知乎和 V2EX 个人变现经验研究路由，允许社区实测影响优化方向、排查顺序和实验优先级。
- 增加 B+/B/B- 经验权重、页面可读性与 PDF 捕获状态规则，区分官方机制、社区经验和本地观测结论。
- 加入社区网页文本/PDF 快照索引、递归附属链接清单和访问受限状态说明。
- 扩展 TopOn 短窗口观察、聚合管理报表稀疏字段、排序价格和数据质量审计能力。
- 重建 Monety viewer，登记社区参考资料和 77 个公开来源。

### Validation

- Skill quick validation 通过。
- TopOn 单元测试 14 项通过。
- viewer 构建成功：21 个文档、77 个来源、77 个 URL。
- `git diff --check` 通过。

## Maintenance: patch-20260908-142326

- 将 Monety 部署脚本、CLI 推送/更新提示和安装文档从 Gitee 切换到 GitHub。
- 本次不纳入已有的 `viewer/index.html` 和 `viewer/template.html` 工作区修改。

### Validation

- Monety 部署与 CLI PowerShell AST 解析通过。
- `git diff --check` 通过；未执行生产部署或服务器重启。
