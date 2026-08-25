# 安装与使用

## 推荐：直接安装

如果你的 Agent 支持 `skills.sh` 安装器：

```bash
npx -y skills add xuehuafu233-alt/zane-career-skills -g --all
```

安装后重新打开 Agent 会话，让它重新读取 Skill 目录。

## 手动复制到 Codex

把仓库 `skills/` 下需要的 Skill 目录复制到你的 Codex skills 目录：

```bash
cp -R skills/zane-career-portfolio-builder ~/.codex/skills/
cp -R skills/zane-career-assets ~/.codex/skills/
```

也可以整体复制 `skills/` 目录。复制后重新打开 Agent 会话，让它重新读取 Skill 目录。

## 其他 Agent

这些目录遵循常见的 `SKILL.md` 结构。支持该结构的 Agent 可直接将相应目录加入自己的 Skill 路径；具体安装位置以工具本身的文档为准。

## 第一次使用

不要先填模板。先告诉 Agent：

- 想进入的岗位与级别；
- 招聘市场、读者和投递渠道；
- 现有经历、作品和能核验的证据；
- 想做的载体；
- 语言、视觉偏好、文风和公开边界；
- 这次交付完成的证据。

先从 `zane-career-portfolio-builder` 开始，或从 `zane-career-assets` 让它按任务自动路由。

## 发布前

使用 `zane-portfolio-multi-format-qa` 复查全部载体。网页能打开、PDF 能生成或二维码能扫描，都不单独等于整套职业资产已经通过。
