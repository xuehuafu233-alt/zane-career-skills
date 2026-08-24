---
name: zane-career-resume-builder
description: 从零创建、重构并交付面向不同招聘市场的职业简历，支持中文、英文及其他目标语言的本地化重写。根据目标岗位、招聘渠道、读者语言、证据强度、职业阶段和审美偏好，自主决定信息结构、页数、视觉人格与交付格式；覆盖资料盘点、事实归因、招聘定位、扫读层级、文案收敛、黑白结构、个性化视觉、PDF验收、多语言链接路径与作品集承接。用于用户只有零散经历、旧简历效果差、招聘者看不懂、需要跨语言重写或内容反复修改、版面失衡，或希望得到不套固定模板的完整简历时。
---

# 多语言职业简历构建

把简历当作有限空间内的招聘决策界面。固定的是判断顺序与验收标准，不固定页数、模块名称、颜色、版式或文案句型。简历继承职业资产系统的事实与判断层，不在 PDF 中另建一套事实。

若任务由 `zane-career-assets` 总控发起，先读取其状态文件和交接包，只处理当前获准阶段。若用户直接调用本 Skill 从零生成可投递简历，也要建立 `zane-career-assets-state.json`；“帮我做完”不等于用户放弃文案、结构和视觉审核。

## 生产流程

按 `Define → Evidence → Position → Allocate → Write → Freeze → Wireframe → Style → Build → Verify → Handoff` 执行。不得从配色或模板开始。

### 1. Define

建立任务合同，确认目标岗位与级别、主要阅读者、招聘渠道、展示截断规则、打印或屏幕场景、语言、公开边界、截止时间与交付格式；同时写清首触点要促成的决定、下一环和最终招聘结果。简历优先完成能力证明与面试入口，不主动承担后续面试／尽调的全部解释任务；只有会造成重大误导、法律／合规／隐私风险或直接改变当前岗位判断的事实才阻断成稿。

目标涉及特定国家或招聘市场时，读取[目标市场适配协议](../zane-career-assets/references/market-localization.md)，区分已验证规则、样本趋势与假设。

平台只展示前若干字符时，把该数字作为本项目的 `preview_budget`；没有平台截断证据时，不默认 22 字。页数由资历、证据密度与渠道决定，不默认所有人两页。

### 2. Evidence

读取用户资料并建立事实台账。区分本人动作、本人负责的团队结果、跨部门结果、直接数据、模型测算、同期趋势、转述和待验证假设。禁止根据职位常识补写不存在的预算权、管理、投放、制作、发布或转化职责。

详细规则见 [references/content-and-evidence.md](references/content-and-evidence.md)。

### 3. Position

回答三个问题：招聘者为什么需要这个岗位；用户已经证明了什么；与同级候选人相比，哪组证据最值得先看。定位必须由事实交集得出，不用抽象人格或未来愿望冒充当前能力。

### 4. Allocate

为每条信息指定唯一任务：入口负责获得继续阅读，摘要负责形成价值判断，经历负责证明职责与结果，补充模块负责处理教育、作品、技能或公开链接。模块名称和数量按岗位与证据选择，不固定使用“个人优势／核心产出／主要工作”。

执行删除测试：删掉一项后若不损失新的招聘判断，合并或删除。相同主题可以概括—证明，不得原样重复。

同时做页数竞争，不先写“计划两页”：分别估算 1 页、2 页，以及资历确有必要时的 3 页方案。每新增一页必须承担前页无法承担的一项独立招聘判断；若某页明显稀疏，只因模块被人为拆开，必须比较“合并为更少页”而不能用留白合理化。若为了减页需要缩小到难读、破坏语义边界或删除关键证据，则保留更多页。把通过与淘汰的页数及代价写入合同。

### 5. Write

先写完整黑白文本，再局部收敛。语言优先让第一阅读者理解；专业词只在能提高可信度时出现，并由上下文说明它解决什么问题。记忆点来自准确判断、具体动作和自然节奏，不写口号墙、岗位说明书或模板化对仗。

每个条目只承担一个主要招聘判断，但允许一个句子用分号连接动作与结果形成闭环。不要为了“金句感”先写宣言再列事实证明；主体性通过自然的`负责、主导、擅长、习惯、熟悉`等动词体现，不机械重复。

### 6. Freeze

用 [assets/resume-decision-contract-template.md](assets/resume-decision-contract-template.md) 记录已确认、已淘汰、事实边界、模块分工、视觉偏好与当前停点。新事实、证据冲突或跨模块重复才允许重开冻结内容。

每次用户确认、否决、纠正或提出稳定偏好后立即更新合同。改一处前检查当前条目、相邻模块、同类经历与网站／多语言版本；同类问题第二次出现时升级为类别审计，不继续逐行打补丁。

### 7. Wireframe

禁用品牌色、装饰、照片滤镜和动效。高不确定性时比较至少两种真正不同的信息结构；事实、参考和偏好已经足够明确时，可以提交一个有依据的结构，但必须做删除测试、替代结构反事实与页数竞争。只判断阅读顺序、信息重量、分页、行长、留白和入口是否成立。黑白结构未通过，不进入视觉。

比较方向时记录结构签名：入口形态、首个证据形态、主阅读轴、经历组织、数字角色、页面收束。两个方向至少有三项不同；“同一骨架换左右、换色或换标题”不算第二种方向。

### 8. Style

读取 [references/style-personalization.md](references/style-personalization.md)，从用户本人、目标岗位、真实资产、偏好与反偏好中生成视觉人格。高不确定性时提出至少两种具有不同关系机制的方向；偏好和视觉参照明确时可以提出一个方向，但要说明依据、风险和被淘汰的替代机制。用户未选择前不把某种颜色、卡片、照片或字体写成默认模板。

### 9. Build

只将通过的黑白结构和视觉方向实现为可编辑源与 PDF。建立全局排版变量，避免为每段经历叠加局部补丁。压行优先改重复与冗余，不得为排版偷偷改变事实、时间或归因。

Build 前必须运行 `zane-career-assets/scripts/career_assets_state.py check --action build-resume`。`task_contract / evidence_position / content / structure / visual` 任一项仍为 `pending` 时立即停止。只有用户明确确认才记为 `approved`；用户明确要求一次性出稿时才可记为 `waived`，且生成物仍只能称候选版。

### 10. Verify

运行 `scripts/check_resume_pdf.py` 做结构初检，再以高分辨率渲染全部页面，按从上到下的连续阅读带逐段实看。检查视觉居中、上方分离与下方归属、同类间距、断行、孤字、裁切、重叠、页尾平衡、链接和打印可读性。

如果这是同一证据系统的另一语言版本，必须把已确认版本作为视觉参照重新对照，而不是只检查英文版自己是否“没有溢出”：比较标题层级、正文可读字号、行距、模块间距、色块比例、每页内容重心和页尾收束。语言变化会改变换行和信息高度，不能沿用原语言的字号／行距参数后直接放行。若新语言版明显更紧、更小、内容集中在页面上半部，或两页都出现无功能大空白，视觉验收失败，必须回到全局排版变量或分页重排。

页数通过不代表分页通过。除非合同明确选择封面页或作品跨页，任一正文页的最后一块有效内容若停在页面上方约三分之二以内，留下的大块空白又不承担分组、批注、图像或行动任务，必须重开分页：试排更少页、跨页重分配或调整全局密度后再比较。不得仅写“留白是设计选择”后放行。

固定“六帧”只适用于恰好两页且结构相符的项目；其他页数按内容边界划分连续检查带。脚本通过不等于视觉通过。

### 11. Multilingual Delivery

When an English resume is requested, do not translate the Chinese PDF line by line. Rebuild the same evidence set for an English hiring reader:

- remove demographic fields that do not help the target market unless required;
- rewrite labels, sentence rhythm, and business verbs in native professional English;
- preserve dates, numbers, units, evidence type, ownership, and uncertainty exactly;
- keep a terminology contract for brands and platforms; do not invent legal English company names;
- keep model-estimated results, peaks, cumulative values, GTV, team outcomes, and direct outcomes visibly distinct;
- review for translationese, corporate publicity language, unexplained China-market jargon, and repeated summary/experience claims;
- decide labels, numbering, chronology and section breaks by the target market and evidence density; removing Chinese-style labels or numbering is not automatically more native, and keeping them is not automatically wrong;
- run an independent native-editing pass after factual translation: shorten over-complete arguments, remove management manifestos and Chinese rhetorical parallelism, while preserving distinctive personal judgment;
- render every page, inspect spacing and page balance, then check extractable text, visible-language residue, PDF annotations, and the QR code decoded from the final rendered page.
- compare the localized PDF against the confirmed source-language PDF at the same render scale; match reading rhythm and information weight, not literal line counts. A structurally valid two-page PDF is not approved if its localized typography is materially tighter or smaller than the confirmed version.

For a bilingual portfolio, use one domain with language-specific paths: Chinese `/`, English `/en/`. Do not make both resumes point to the same default-language root when the hiring reader's language is known.

Do not rebuild an approved PDF merely because website content or a deployment identifier changed. Rebuild only when the public domain or language path, visible URL, PDF link annotation, or final-page QR target changes. Deployment identifiers are release evidence, not resume URLs.

### 12. Handoff

交付事实台账、决策合同、可编辑源、生成器、最终文件和 QA 结果。若有作品集，读取 [references/cross-medium-handoff.md](references/cross-medium-handoff.md)，建立 `简历主张 → 网站入口 → 深读证据` 映射；硬事实一致，不要求逐字统一。英文交付同时保存翻译分析、术语合同、批评与修订记录；把当前可访问地址和部署后语言路径分开记录，不能把临时根路径写成英文站已上线。

版本状态必须互斥：未经用户确认只能称候选版；用户确认且交付源完成后才称确认版或正式投递版。简历没有“待部署”状态。不得把“文件已生成”写成“已确认”。

## 完成标准

- 陌生招聘者能在渠道允许的第一屏内说清候选人是谁、处于什么级别、能创造什么价值；
- 关键主张均有证据，职责与测算边界可解释；
- 信息结构适合当前岗位与渠道，而非复刻某个案例；
- 视觉方向能说明“为什么属于这个人”，替换姓名后不能无损套给另一位候选人；
- 全部页面完成机器与实图验收；
- 无功能大空白已通过重新试排证明必要，或已经消除；
- 候选版、确认版、投递版和线上链接状态没有混淆。

## 发布状态

本 Skill 为 `v0.7 beta`，可从零生成与迭代个性化简历，并覆盖中文、英文、本地化表达、PDF 交付和投递前验收。它不把任何人的经历、结构或视觉样式当作默认模板；岗位、证据和招聘读者变化时，结论与版式也应随之变化。
