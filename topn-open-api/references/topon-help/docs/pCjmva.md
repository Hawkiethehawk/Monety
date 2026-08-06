---
title: "流量分组规则数据格式"
source: "https://help.toponad.net/cn/docs/pCjmva"
captured_at: "2026-07-21T08:07:23Z"
site_modified: "2025-05-30"
category_path: ["Open API接入指南", "附录", "流量分组规则数据格式"]
content_sha256: "05fbd4e480a221aff9515e7bd7dbbf3541a3ac19cd90ef323efb706d53a06c46"
knowledge_role: "reference_only"
has_article_body: true
---

# 流量分组规则数据格式

| rule | 描述 | 示例 |
| --- | --- | --- |
| 0 | 包含（集合） | 一维数组JSON ["CN", "US"] |
| 1 | 不包含（集合） | 一维数组JSON ["1","2","3"] |
| 2 | 大于等于（值） | 整形或浮点 124 |
| 3 | 小于等于（值） | 整形或浮点 222.36 |
| 4 | 区间内（区间） | 二维数组JSON [["122","456"],["888","12322"]] |
| 5 | 区间外（区间） | 二维数组JSON [["122","456"],["888","12322"]] |
| 6 | 自定义规则（custom） | bb=1&c!=3&p=3&d=1,2,3 |
| 7 | 大于（值） | 整形、浮点或字符串 124 |
| 8 | 小于（值） | 整形、浮点或字符串 222.36 |

##
