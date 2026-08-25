# 职业资产路由与交接

| 当前任务 | 主 Skill | 交付 | 停止线 |
|---|---|---|---|
| 从零建设整套职业资产 | `zane-career-portfolio-builder` | 跨载体项目与状态 | 未确认必要载体时不批量生产 |
| 简历新建、重构或多语言 | `zane-career-resume-builder` | 文本、结构、可编辑源、PDF 与 QA | `content/structure/visual` 未审核时禁止 Build |
| 网站与深读的载体分工 | `zane-career-portfolio-architecture` | 首页、深页和下载文档地图 | 不以网站摘要重复扩写代替深读 |
| 作品集网站设计与开发 | `zane-career-portfolio-website-design` | 响应式网站与可部署源 | 结构与视觉未选择时禁止实现 |
| 案例主张、数据与责任边界 | `zane-evidence-weighted-case-storytelling` | 证据加权的案例主张 | 证据不足时降级措辞或留空 |
| 中文职业案例编辑 | `zane-career-case-editor-zh` | 有现场、取舍与边界的文本 | 不脱离证据自由发挥 |
| 前雇主数据与截图审查 | `zane-former-employer-data-redactor` | 保留、模糊、口述或删除清单 | 高风险项未处理时禁止公开 |
| 网页、Word、PDF、二维码和线上副本验收 | `zane-portfolio-multi-format-qa` | 逐格式 QA 报告 | 实际渲染或链接未测时不得通过 |
| 招聘平台、猎头或主动投递首句 | `zane-career-application-greeting` | 短招呼语 | 不重复简历或伪造已读 JD |

## 默认串联

`zane-career-assets 定义任务 → 事实与定位 → 当前交付物的专项 Skill → 脱敏 → 多格式 QA → 用户最终确认 → 必要时生成招呼语`

这是项目级候选链，不是每个任务必经清单。每次只调用当前阶段必要的一个主 Skill 和最多两个前置／验收 Skill。

所有专项 Skill 共享`operating-model.md`中的五层真源。事实、术语、定位或公开边界变化时先改共享层，再路由到所有受影响载体；不要让简历、网站和英文版分别维护互相漂移的答案。

多轮修改先按`change-control.md`分类反馈与计算影响范围。同类缺陷第二次出现时，从单项修复升级为类别审计；发布验收按`evaluation-model.md`选择字节、语义、视觉或交互证据。

## 最小交接包

```yaml
task:
  object: ""
  audience: ""
  deliverable: ""
evidence:
  facts: []
  user_judgments: []
  hypotheses: []
decision:
  chosen: []
  rejected: []
  open_gaps: []
  constraints: []
state:
  current_gate: ""
  gate_status: ""
  artifacts: {}
handoff:
  next_skill: ""
  acceptance: ""
  stop: ""
```
