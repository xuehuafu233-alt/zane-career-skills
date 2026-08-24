---
name: zane-career-portfolio-architecture
description: 设计面向招聘的分层职业作品集与双语投递入口：用网站完成30秒定位与深读引导，用知识库或长文证明判断、取舍、代价和工作现场，用可下载文档支持投递。Use when creating, restructuring or reviewing a career portfolio, personal site, bilingual portfolio, Feishu/Notion case library, case-study navigation, or deciding what belongs on the homepage versus deep-reading pages.
---

# Career Portfolio Architecture

把作品集当成招聘决策路径，而不是经历资料库。架构连接共享事实与各载体，不为网站、简历和长文分别发明定位。

若用户要求从资料开始建设网站、知识库、Word和发布包，立即转由 `zane-career-portfolio-builder` 主持全流程；本Skill只负责定位、信息架构与载体分工，并把结论交回主Skill的事实台账和manifest。

## 1. 先定义招聘者的决策链

至少定义：入口如何获得注意与相关性；简历／首页如何形成级别与价值判断；深页如何建立可信度；作品与关于页如何补足产物和人物；联系入口如何促成下一步。渠道存在真实截断或时间约束时记录具体预算，没有证据时不把“30秒”变成固定字数。

若目标岗位、核心定位或代表经历未明确，先补齐这三项；不要直接设计页面。

涉及特定国家或招聘市场时读取[目标市场适配协议](../zane-career-assets/references/market-localization.md)，不要把某一地区的页面、隐私或语言习惯写成全球默认。

## 2. 分配各载体的任务

| 层级 | 任务 | 应放内容 | 不应放内容 |
|---|---|---|---|
| 网站 | 钩子与导航 | 定位、责任跨度、关键决定、深读理由 | SOP、完整复盘、口径辩护 |
| 知识库 | 证据与现场 | Why→What→How、冲突、取舍、协作边界、结果 | 网站摘要的重复扩写 |
| 下载文档 | 投递与离线阅读 | 经过排版压缩的权威内容 | 与线上版本冲突的旧口径 |
| 面试 | 追问与口述 | 敏感细节的合规表达、失败与复盘 | 不适合公开的经营数据 |

## 3. 建立母题与业务问题

- 用一句母题连接经历，但不要把不同案例写成同一个模板。
- 从业务断点命名能力，不从渠道名堆砌标签。
- 让职业路径体现责任升级：交付动作 → 团队与实验 → 业务与品牌责任。

## 4. 设计首页

首页至少回答：目标岗位、当前级别、独特价值、3个以内代表经历、继续阅读入口。

每张经历卡只保留：背景/角色跨度、一个关键决定、一个证据锚点、深读理由。若卡片能独立替代知识库，说明过长。

## 5. 设计深读页

每篇案例优先使用：业务为何要做 → 本人定义什么任务 → 如何落地 → 做了什么取舍 → 代价/边界 → 结果与未解决问题。

允许案例长度和结构不均匀。不要强行让每篇都成功、闭环或升华。

## 6. 验收

- 让陌生招聘者30秒复述定位、级别、独特价值和最想深读的经历。
- 检查网站是否仍是钩子。
- 检查知识库是否提供网站没有的判断与现场。
- 检查各载体是否共用同一权威事实源。
- 建立`核心主张 → 简历位置 → 网站入口 → 深页证据 → 面试边界`映射；缺失承接时补入口或降级主张，不复制全文。

## 7. Multilingual and application entry points

- Determine the hiring reader for each language; do not substitute “translate the same content twice” for localization. Share facts, not necessarily sentence structure, length, or evidence order.
- Keep a terminology contract for public brand names, legal entities, platforms, acronyms, and metric definitions. If no verified English legal name exists, do not invent one.
- Use one domain with language paths: Chinese `/`, English `/en/`; language buttons switch between them, while resume links go directly to the reader's language.
- Localize explanatory diagrams when needed, but preserve portraits, work covers, original dashboards, and logos as evidence. Record whether each Chinese-heavy image is retained, captioned, or given a derived language version.
- Before handoff, check bidirectional language links, desktop/mobile layout, language residue, URL paths, cross-carrier metrics, and temporary pre-deployment URLs.
- Treat the localized site as a market edition: run a native-editing pass on every public page, not only About or the page named by a reviewer. Preserve personal judgment, but remove over-complete arguments, publicity tone, and translation-shaped headings where they reduce trust.

## 8. Application message handoff

A greeting message is a connector, not a third resume or a portfolio manifesto. It only connects the current role to the single most relevant value-and-evidence pair, without copying the resume's full summary or the portfolio's long result narrative.

涉及职责、数据视觉权重或前雇主敏感信息时，分别调用 `zane-evidence-weighted-case-storytelling`、`zane-portfolio-multi-format-qa`、`zane-former-employer-data-redactor`。

来源与方法边界见 [references/method-origin.md](references/method-origin.md)。
