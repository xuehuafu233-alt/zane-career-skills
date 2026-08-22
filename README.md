# Zane Career Skills v0.7 beta

简体中文 | [English](README.en.md)

> 面向求职者、职业转型者与独立创作者的职业资产 Skill 库。把真实经历、证据、审美与招聘目标交给 Agent，得到一套能继续行动的简历、作品集与发布交付物。

## 这是什么

这不是某个人的简历模板，也不是固定网站主题。它只保留解决问题的方法：如何从经历和证据建立招聘定位，如何把内容分配到简历、网站和案例，如何保留个人文风与审美，如何完成双语本地化，以及如何在发布前验收链接、二维码、PDF、网页和隐私边界。

这套库来自 Zane 在真实职业资产项目中反复遇到的问题、失败复盘和可验证改进。每个人仍然要从自己的目标岗位、经历、证据、招聘读者、语言和视觉偏好出发。

## 你会得到什么

| 真实处境 | 主要产出 |
| --- | --- |
| 只有旧简历、零散经历和项目文件 | 从 0 到 1 的事实台账、定位、简历和作品集结构 |
| 简历能写出来，但招聘者看不懂 | 扫读层级、证据主张和载体分工 |
| 想保留自己的文风和信息密度 | 不套模板的取舍、案例编辑和个人化表达 |
| 需要英文或其他语言版本 | 与招聘判断对齐的本地化，而不是逐句翻译 |
| 网站、PDF、二维码和链接经常互相漂移 | 跨格式、跨语言和线上发布 QA |
| 想从视觉参考做出自己的页面 | 设计解码、原创 Master Prompt 与响应式验收 |

## 快速开始

安装完成后，直接在 Agent 中输入：

```text
我想申请产品营销负责人。请根据我的经历和现有材料，先帮我建立事实台账和招聘定位，再决定我需要简历、作品集网站还是深读案例。我的文风希望保留信息密度，不要写成 AI 腔。
```

不知道入口时，先调用 `career-assets`。要从零完成整套职业资产时，调用 `career-portfolio-builder`。

已经知道任务时，可以直接调用：

```text
career-resume-builder：重构一份中文或英文简历
career-portfolio-website-design：设计并构建个性化作品集网站
career-case-editor-zh：编辑中文职业案例，保留工作现场和个人语气
portfolio-multi-format-qa：验收网页、PDF、Word、链接和二维码
```

## 能力一览

| 工作目标 | 主要入口 | 常见产出 |
| --- | --- | --- |
| 统筹完整职业资产 | `career-assets`、`career-portfolio-builder` | 事实台账、定位、载体分工、生产计划和交付状态 |
| 创建多语言简历 | `career-resume-builder` | 简历文案、结构、视觉、PDF 和语言对齐 |
| 设计作品集信息架构 | `career-portfolio-architecture` | 首页钩子、案例深读、索引和投递入口 |
| 构建个性化网站 | `career-portfolio-website-design` | 页面结构、视觉人格、响应式实现与全站 QA |
| 讲清职业案例 | `evidence-weighted-case-storytelling`、`career-case-editor-zh` | 判断、动作、代价、边界与证据权重 |
| 处理前雇主数据 | `former-employer-data-redactor` | 保留、模糊、转口述或移除的公开决策 |
| 写投递第一句话 | `career-application-greeting` | 招聘平台、猎头和主动投递的首条消息 |
| 验收发布版本 | `portfolio-multi-format-qa` | 桌面／手机、PDF／网页、链接、二维码和线上副本检查 |
| 解码视觉参考 | `design-reference-to-prompt` | 观察事实、设计判断、待确认项与原创 Master Prompt |
| 生成东方自然光生活视觉 | `eastern-natural-light-cinema` | 场景、动作、光线、材质和模型适配提示词 |
| 做主体性自我分析 | `self-insight` | 事实、体验、自我叙述、外部脚本与待验证模式 |

仓库直接保留 `skills/<skill-name>/SKILL.md` 目录结构，安装器可以按 Skill 读取；根目录的 ZIP 是离线下载备用。完整目录见 [VERSION.md](VERSION.md)，安装方法见 [docs/install.md](docs/install.md)。

## 安装

### 支持 Skills 的 Agent

如果你的 Agent 支持 `skills.sh` 安装器，直接安装：

```bash
npx -y skills add xuehuafu233-alt/zane-career-skills -g --all
```

也可以克隆仓库后整体复制 `skills/`，或下载 ZIP 离线安装。具体安装位置以你的 Agent 文档为准。

### 第一次使用

告诉 Agent：目标岗位与级别、招聘市场与渠道、经历与可核验事实、想做的载体、语言、视觉偏好、文风、公开边界和完成证据。资料可以分批提供，先建立事实和决策结构，再进入写作与设计。

## 工作方式

```text
真实任务
   ↓
目标、读者、证据与公开边界
   ↓
招聘定位与载体分工
   ↓
文案、结构、视觉与本地化
   ↓
PDF／网页／链接／二维码／线上副本 QA
   ↓
用户确认、投递或部署
```

简历、网站、案例和部署分别记录状态；用户确认、正式投递、线上部署和现实招聘反馈不会混为一个“完成”。

## 原创与第三方边界

本仓库只发布 Zane 自己沉淀的职业资产、视觉与自我分析方法，以及明确标注来源的公共转译方法。不会把 dbs、宝玉、Jiro Build、外部设计库或其他作者的原始 Skill 当作原创发布；也不包含个人简历、公司名、联系方式、项目数字、域名、照片、工作台路径、私密人生资料、凭据或客户材料。

方法署名口径：`Zane method; structured with AI assistance.`

详细来源、边界和待泛化项目见 [docs/provenance.md](docs/provenance.md) 与 [docs/skill-inventory.md](docs/skill-inventory.md)。

## 使用边界

- Skill 不会替你虚构经历、数字、结果或客户事实；
- 复杂信息不必全部挤进首触点，但重大误导、法律／合规、隐私和直接改变招聘判断的事实必须前置；
- 视觉和结构是项目结果，不是套装预设；替换姓名和颜色后仍完全相同，说明推导不足；
- `voc-koc-mix`、`life-context-router` 以及 dbs／宝玉／外部安装的 Skill 不在本公开库中。

## 许可证

除 [docs/provenance.md](docs/provenance.md) 另有说明外，本仓库内容以 MIT License 发布。发布不授予使用他人品牌、案例资料或私有数据的权利，详见 [LICENSE](LICENSE)。

## 作者与服务

作者：Zane。Skill 用来让更多人先独立完成一轮；需要针对个人材料进行深度定位、重构、发布或工作台搭建时，可通过 GitHub 主页联系作者。服务不是使用 Skill 的前置条件。
