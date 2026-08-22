# Skill 来源盘点

这份盘点回答一个问题：本地工作台里哪些能力已经沉淀成 Zane 自己的可公开方法，哪些仍属于外部能力、私有基础设施或需要继续泛化的实验。

## 扫描范围

- 扫描目录：`.agents/skills`
- 本地 Skill：100 个
- 发布包：13 个
- 发布前对 13 个目录逐一运行结构校验，并对发布目录做隐私、品牌、路径和凭据扫描。

## 公开核心库

### 职业资产方法

`career-assets`、`career-portfolio-builder`、`career-resume-builder`、`career-portfolio-website-design`、`career-portfolio-architecture`、`career-application-greeting`、`career-case-editor-zh`、`evidence-weighted-case-storytelling`、`former-employer-data-redactor`、`portfolio-multi-format-qa`。

来源是多轮真实简历、双语简历、作品集网站、案例深读、前雇主数据公开边界和 PDF／网页／二维码／线上部署验收。它们保留的是判断机制、工作流和失败后的闸门，不包含个人资料或固定页面。

### 视觉与主体性扩展

`design-reference-to-prompt`、`eastern-natural-light-cinema`、`self-insight`。

它们分别来自视觉参考转原创前端提示词、东方古代生活的自然光影像方法，以及在真实自我分析中形成的证据分层和主体性判断。公开版 `self-insight` 已移除私有工作台的路径和长期记忆接口。

## 暂不公开

### 需要继续泛化

`voc-koc-mix` 的方法有真实验证，但当前仍绑定具体品牌、产品型号、卖点池、平台话题和舆情红线；在改成通用的 KOC 混剪／品牌记忆点方法前，不放入公开库。

### 私有工作台系统

`life-context-router` 是个人长期人生上下文路由，涉及生命域、关系、身体、信仰、私密事实和本地目录。它属于 Zane 的个人基础设施，不是对外产品 Skill。

### 工具与本地适配

`markdown-to-word`、`pdf-document-reader`、`dbs-agent-migration`、`dbs-bridge` 等依赖本地脚本、工作台规则或外部工具。它们可以继续作为私有工作台能力维护，但不在这次方法库发布中冒充独立原创产品。

## 明确排除

- `dbs-*`：dontbesilent 的上游工具箱；本地有适配和使用经验，但不能署名为 Zane 原创；
- `baoyu-*`：外部 Skill 系列；
- `bb-browser`、`bb-browser-openclaw`、`ocr`、`impeccable`、`taste-skill`、`spacing-skill`、`motion-ref`：外部能力或工具适配；
- `culture-fragment-poster-engine`、`goutoujunshi`、`zhang-xiaoyu`：从外部项目安装或收编的能力；
- `dbs`、`dbs-bridge` 等治理入口：保留在本地工作台，不在公开库重新包装。

## 发布判断

“本地新增”不自动等于“个人原创”。只有同时满足真实来源、方法能脱离个案复用、没有私密资料、没有未经许可的第三方内容、陌生用户可以理解入口，才进入公开库。
