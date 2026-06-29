---
name: bulu-writing-workflow
description: Use when the user invokes `bulu-writing-workflow` to run a staged daily night-review writing workflow for 布鲁成长手记. Supports subcommands new, input, specify, outline, apply, review, final, and cover, creating and advancing a dated draft workspace without jumping straight to a finished article.
metadata:
  short-description: Staged daily night-review writing workflow
---

# Bulu Writing Workflow

用于“布鲁成长手记”的每日夜报/热点复盘工作流。核心目标不是一次成稿，而是把每天看到的新闻、讨论和想法，按固定栅栏推进成文章。

只接受一个触发名：

- `bulu-writing-workflow`

## 默认规则

- 全程用中文回复。
- 一次只执行一个子命令，不跨阶段。
- 不模仿任何在世作者的固定措辞、口头禅或身份设定；只吸收“夜报型写作”的机制：当天事件、白话解释、明确判断、自然转场、轻松节奏。
- 每个阶段都要读前置文件；缺前置文件时，先说明缺什么，并给最小补救方案。
- 默认草稿根目录为 `/Users/Admin/Documents/bulu`。如果用户另给目录，以用户指定为准。
- 默认工作目录为 `<草稿根目录>/yyyy-mm-dd/草稿/`。

## 可选风格参考

当用户说“参考猫笔刀”“参考当前目录文章”或类似表达时，可以把 `/Users/Admin/Documents/writing/material/wechatOfficial/猫笔刀` 下的文章作为可选参考库。

参考方式：

- 优先读 2-3 篇近期 `.md` 文章，提炼结构、节奏、信息密度、开头切口、转场方式和短评收尾方式。
- 只学习夜报机制，不复刻作者本人：不要复制固定口头禅、粗口、身份设定、独特比喻或连续句式。
- 写作时仍以“布鲁成长手记”的表达为准，参考库不是硬依赖；如果目录不存在、样本不相关或当前阶段不需要，就直接按本工作流推进。
- 在 `specify` 和 `outline` 阶段更适合参考结构；在 `apply` 和 `review` 阶段只用来检查文章是否有夜报节奏，不用来改成某个作者的腔调。

## 子命令

### `new`

创建当天写作空间。优先运行本 Skill 的脚本：

```bash
python3 scripts/new.py
```

可按需传参：

```bash
python3 scripts/new.py --date 2026-06-17 --root "/Users/Admin/Documents/bulu"
```

创建文件：

- `00-input.md`
- `01-specify.md`
- `02-outline.md`
- `03-draft.md`
- `04-review.md`
- `05-final.md`
- `06-cover.md`
- `meta.json`

完成后只引导用户进入 input：

```text
今天的写作空间已建好。现在进入 input 阶段，把今天看到的新闻、讨论、想法、截图描述丢给我，不需要整理。
```

### `input`

只收集素材，写入或追加到 `00-input.md`。不筛选、不定主线、不写正文。

素材可以包括：

- 今天看到的新闻、链接、截图描述。
- 和别人讨论的话题。
- 市场盘面、数据、异动。
- 用户自己的第一反应、困惑、吐槽。

输出时简短确认，并提示下一步是 `specify`。

### `specify`

读取 `00-input.md`，把混乱素材整理为 3-5 个候选选题，并完成澄清。写入 `01-specify.md`。

每个选题包含：

- 发生了什么。
- 为什么值得写。
- 读者关心点。
- 用户可能的判断。
- 事实、推测、情绪分别是什么。
- 一句话白话主线。
- 可用标题方向 2-3 个。

最后推荐 1 个今日主线，并说明为什么；同时给出 3-5 个标题方向，不定最终标题。

### `outline`

读取 `01-specify.md`，基于推荐主线拆文章结构，写入 `02-outline.md`。

大纲包含：

- 推荐标题 1 个。
- 备选标题 3-5 个。
- 标题气质说明：偏盘面、偏产业、偏情绪或偏短评。
- 开头切口。
- 主菜段落。
- 2-4 个编号短评候选。
- 是否需要轻话题收尾。
- 每段目标字数。
- 待核查事实。

### `apply`

读取 `02-outline.md`，只写正文初稿，写入 `03-draft.md`。

初稿顶部先保留推荐标题，例如：

```text
# 推荐标题

正文……
```

默认 1300-1700 字。不要同时给封面、排版或归档。

### `review`

读取 `03-draft.md`，做审稿和修订，写入 `04-review.md`。

重点检查：

- 标题是否准确、有张力、不标题党。
- 是否像新闻拼盘。
- 主线是否清楚。
- 判断是否过满。
- 事实是否需要核查。
- 是否不够像“布鲁成长手记”的表达。
- 节奏是否拖沓。

输出修订稿、最终推荐标题和改动说明。

### `final`

读取 `04-review.md`，生成最终发布稿，写入 `05-final.md`，并更新 `meta.json`。

最终稿只保留可发布内容；风险提示、待核查项和内部说明不要混入正文。

最终稿顶部保留最终标题；同时把最终标题写入 `meta.json.title`。

### `cover`

读取 `05-final.md` 和 `meta.json`，为最终稿生成公众号封面图，写入 `06-cover.md`，并更新 `meta.json`。

默认做法：

- 使用 `imagegen` 生成一张适合公众号封面的横图。
- 封面图优先表达文章主线和情绪，不直接把中文标题做进图里，避免图片中文字变形；如用户明确要带字，再单独处理。
- 图片应保存到当前草稿目录，文件名建议为 `cover.png`；如果另存到输出目录，也要在 `06-cover.md` 记录实际路径。
- `06-cover.md` 至少记录：封面主题、最终标题、生成提示词、图片路径、是否需要用户二次挑选或改字。
- 封面主题优先来自 `meta.json.title` 和 `05-final.md` 顶部标题；如果用户临时改标题，先更新 `meta.json.title` 再生成封面。
- 封面风格应服务“布鲁成长手记”：清爽、有信息感、不过度营销，不做夸张大字报。

## 阶段状态判断

如果用户只说“继续”，检查工作目录中最新非空文件：

- 没有目录：建议执行 `bulu-writing-workflow new`。
- 有 `00-input.md` 但无 `01-specify.md`：执行 `specify`。
- 有 `01-specify.md` 但无 `02-outline.md`：执行 `outline`。
- 有 `02-outline.md` 但无 `03-draft.md`：执行 `apply`。
- 有 `03-draft.md` 但无 `04-review.md`：执行 `review`。
- 有 `04-review.md` 但无 `05-final.md`：执行 `final`。
- 有 `05-final.md` 但无 `06-cover.md` 或 `06-cover.md` 未记录图片路径：执行 `cover`。

## 输出风格

- 像写作搭子，不像表格机器人。
- 每次阶段完成后，如果提到已创建、写入、更新或生成的本地文件/目录，必须输出为 Markdown 可点击链接，格式为 `[文件名](/绝对路径/文件名)` 或 `[草稿目录](/绝对路径/目录)`；不要只输出裸路径，也不要把路径包在反引号里。
- 阶段完成后优先给本阶段主文件链接，例如 `specify` 给 `[01-specify.md](...)`，`outline` 给 `[02-outline.md](...)`，`apply` 给 `[03-draft.md](...)`，`review` 给 `[04-review.md](...)`，`final` 给 `[05-final.md](...)`，`cover` 给 `[06-cover.md](...)` 和封面图片链接。
- 每次阶段完成后，只提示一个下一步命令。
- `final` 完成后的下一步是 `cover`；`cover` 完成后说明写作流程完成。
- 对素材保持开放，但对流程保持严格。
