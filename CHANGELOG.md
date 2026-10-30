# Changelog

## Monety 1.2.0 - 2026-10-30

版本格式迁移：`monety/SKILL.md` 版本字段由两级 `1.2` 补零为三级 `1.2.0`，对齐 version-manager 2026-10-30 起的规则。Skill 指令内容无变化，标签使用 `monety-v1.2.0`。

### Validation

- `version_inspect.py --repo F:\Monety --project monety` 读出 `1.2.0`，版本检测通过。
- 本次只改版本字段，未改动 Skill 行为，未执行额外测试。

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
