---
name: zane-career-assets
description: 职业资产 Skill 组的统一入口和状态总控。用于找工作、求职准备、改简历、做中英文简历、做职业作品集或网站、整理项目案例、审查前雇主数据、验收 PDF／Word／网页、生成投递招呼语，或用户不知道该调用哪个职业 Skill 时使用。它根据目标和当前阶段调用必要的专项 Skill，维护跨阶段状态，并在事实、文案、结构、视觉和最终交付前强制人审闸门。
---

# 职业资产总控

用一个入口接住自然语言求职任务，再按需调用专项 Skill。不要一次读取全部专项 Skill，也不让用户先学会 Skill 名称。

先读取 [references/operating-model.md](references/operating-model.md)，把所有载体视为同一职业证据系统的投影；涉及多轮修改时再读取 [references/change-control.md](references/change-control.md)，发布或验收时读取 [references/evaluation-model.md](references/evaluation-model.md)。

## 首先定义任务

确认 `目标岗位与级别 / 招聘市场与读者 / 投递渠道 / 现有材料 / 需要的载体 / 公开边界 / 截止时间 / 完成证据`。只追问会改变执行或验收的缺口。

先做隐私准入。受试者、患者、客户个人资料、证件、未脱敏合同、私聊和访问凭据等高度敏感原件若不是完成任务所必需，不读取、不复制到工作区，只记录描述与排除原因，并请求脱敏摘要或公开替代证据。

将需要跨阶段生产或生成可投递成品的任务建立状态文件：

```bash
python3 scripts/career_assets_state.py init --state <project>/zane-career-assets-state.json --project "<name>" --scope resume
```

只诊断某句文案、审查一项数据或回答一个问题时，不强制建立状态文件。

## 按当前任务路由

只读当前需要的专项 Skill。完整路由、输入输出和停止线见 [references/routing.md](references/routing.md)。

- 完整职业资产项目：`zane-career-portfolio-builder`；
- 简历：`zane-career-resume-builder`；
- 网站信息架构：`zane-career-portfolio-architecture`；
- 网站设计与实现：`zane-career-portfolio-website-design`；
- 案例证据与归因：`zane-evidence-weighted-case-storytelling`；
- 中文案例编辑：`zane-career-case-editor-zh`；
- 前雇主数据安全：`zane-former-employer-data-redactor`；
- 多格式交付验收：`zane-portfolio-multi-format-qa`；
- 投递第一句：`zane-career-application-greeting`。

用户只要单项交付时，调用对应专项 Skill 并返回本入口记录状态；不自动扩展成整套作品集。

## 共享真源与阶段闸门

持续维护五层真源：事实、招聘判断、载体分工、表达设计、发布状态。用户确认、否决、事实纠正或稳定偏好出现时，自动写入决策账本；不等待用户再次要求“写进合同”。

每个资产分别记录状态，禁止用一个总状态混写简历、网站和部署。

每个现实触点还要记录自己的局部目的、前序输入、下一环依赖和现实证据。局部资产完成不等于投递、面试或招聘结果完成；只有真实投递、面试或招聘反馈才进入现实验证。

项目只记录当前工作阶段`intake / modeling / production / qa / release / feedback / complete`，它不代表任何资产已经确认或部署。单项资产还可记为`on_hold / not_required / rejected`。

### 七道阶段闸门

详细合同见 [references/stage-contract.md](references/stage-contract.md)。

1. `task_contract`：目标、输入、交付物、风险和完成证据；
2. `evidence_position`：事实台账、归因边界和招聘定位；
3. `content`：黑白文本的内容与取舍；
4. `structure`：结构假设与对照；高不确定性时比较至少两种真正不同的黑白结构；
5. `visual`：视觉人格及其反事实检查；高不确定性时比较至少两种关系机制不同的方向；
6. `qa`：机器检查与全页实图验收；
7. `final_confirmation`：用户确认候选版可转为正式投递版。

每道闸门只能是 `pending / approved / waived / not_required`。`approved` 和 `waived` 必须来自用户的明确表达；不得将“帮我做完”、沉默、上传材料或 Agent 自评解释为审核通过。

记录用户确认或明确放弃审核：

```bash
python3 scripts/career_assets_state.py decide --state <project>/zane-career-assets-state.json --gate content --status approved --note "<user's decision>" --evidence <reviewed-file>
```

不适用的闸门可记为 `not_required`，但必须说明原因。

## 构建前强制检查

生成可投递简历前运行：

```bash
python3 scripts/career_assets_state.py check --state <project>/zane-career-assets-state.json --action build-resume
```

生成可部署网站前运行 `--action build-website`；将候选版标记为正式投递或已交付前运行 `--action release`。检查失败必须停止，向用户展示当前待审核对象，不得先出成品再补审。

用户明确要求一次性出稿时，可以将未审核阶段记为 `waived`，Agent 需完成内部迭代与 QA，交付仍只能称为候选版；不能默认代用户放弃。

记录影响后续的确认、否决、事实纠正或稳定偏好：

```bash
python3 scripts/career_assets_state.py record --state <project>/zane-career-assets-state.json \
  --area content --status confirmed --statement "<decision>" --reason "<why>" --affects resume,website
```

把任务、证据、主张、术语、结构、视觉与发布合同登记为一等状态，不依赖聊天记忆：

```bash
python3 scripts/career_assets_state.py contract --state <project>/zane-career-assets-state.json \
  --name terminology --status current --path <project>/terminology.md
```

不应读取的敏感输入只登记描述，不写入原文：

```bash
python3 scripts/career_assets_state.py exclude --state <project>/zane-career-assets-state.json \
  --description "participant records" --reason "third-party sensitive data" --replacement "redacted project summary"
```

## 跨 Skill 交接

每次交接都传递：对象与读者、已核验事实、用户判断、待验证假设、已选与已排除、当前闸门、每个资产状态、下一交付物、验收与停止线。专项 Skill 不得重新推翻已确认内容，除非出现新事实、冲突、目标变化或客观 QA 缺陷。

同类问题第二次出现、连续两轮修一处坏一处或用户重复提醒既有决定时，停止局部修改，按`change-control.md`做类别级影响分析与全量回归。

## 完成边界

- 文件已生成：候选版；
- 机器检查通过：仍不等于视觉通过；
- 全页实图 QA 通过：可请用户最终确认；
- 用户明确确认：可称正式投递版；
- 网站存在本地文件：不等于已部署；
- 候选、待部署、已部署三种网站状态互斥；上传成功不等于线上验收完成；
- 已部署状态至少记录正式 URL、部署标识和线上资源验证，部署标识不进入简历公开链接；
- 只有真实投递、面试或招聘反馈才进入现实验证。

制作供他人安装的外部包时，不能从隐藏真源复制后只检查文件数量。macOS 需要清除副本的`hidden`标志与Finder元数据，再运行：

```bash
python3 scripts/check_external_package.py <package> --expected-skills <count>
```

目录在终端可读不等于 Finder 可见；ZIP 也必须从已清除隐藏标志的副本重新生成并解压复验。

## 发布状态

本 Skill 组为 `v0.7 beta`：能力边界已经固定，仍允许根据真实使用中的新问题进行小步迭代。它提供从资料盘点到可投递／可部署交付的完整工作流，不承诺替用户补齐不存在的事实、代替用户确认，也不把部署或现实招聘结果伪装成 Skill 自身的完成证明。

方法形成记录见 [references/method-origin.md](references/method-origin.md)。
