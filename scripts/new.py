#!/usr/bin/env python3
import argparse
import json
import os
from datetime import date
from pathlib import Path


DEFAULT_ROOT = "/Users/Admin/Documents/bulu"


def template_input(day: str) -> str:
    return f"""# {day} 夜报 input

把今天看到的新闻、讨论、想法、截图描述先放这里。不需要整理，也不需要判断对错。

## 原始素材

"""


def template_specify(day: str) -> str:
    return f"""# {day} 夜报 specify

本阶段用于把 input 里的素材澄清成候选选题、判断和今日主线。

"""


def template_outline(day: str) -> str:
    return f"""# {day} 夜报 outline

本阶段用于拆文章结构。先确定推荐标题和标题气质，再安排开头切口、主菜、编号短评和收尾。

## 推荐标题


## 备选标题


"""


def template_draft(day: str) -> str:
    return f"""# {day} 夜报 draft

本阶段只放推荐标题和正文初稿。

## 推荐标题


## 正文初稿


"""


def template_review(day: str) -> str:
    return f"""# {day} 夜报 review

本阶段用于审稿、修订和记录改动说明。

"""


def template_final(day: str) -> str:
    return f"""# {day} 夜报 final

本阶段只放最终标题和最终发布稿。

"""


def template_cover(day: str) -> str:
    return f"""# {day} 夜报 cover

本阶段记录封面主题、生成提示词和图片路径。

"""


def main() -> None:
    parser = argparse.ArgumentParser(description="Create a Bulu night-review workspace.")
    parser.add_argument("--date", default=date.today().isoformat(), help="Date in yyyy-mm-dd format.")
    parser.add_argument("--root", default=os.environ.get("BULU_DRAFT_ROOT", DEFAULT_ROOT), help="Draft root directory.")
    args = parser.parse_args()

    workspace = Path(args.root).expanduser() / args.date / "草稿"
    workspace.mkdir(parents=True, exist_ok=True)

    files = {
        "00-input.md": template_input(args.date),
        "01-specify.md": template_specify(args.date),
        "02-outline.md": template_outline(args.date),
        "03-draft.md": template_draft(args.date),
        "04-review.md": template_review(args.date),
        "05-final.md": template_final(args.date),
        "06-cover.md": template_cover(args.date),
    }

    for name, content in files.items():
        path = workspace / name
        if not path.exists():
            path.write_text(content, encoding="utf-8")

    meta_path = workspace / "meta.json"
    if not meta_path.exists():
        meta = {
            "date": args.date,
            "status": "new",
            "workflow": "bulu-writing-workflow",
            "workspace": str(workspace),
            "current_stage": "input",
            "title": "",
            "main_topic": "",
            "topics": [],
            "created_files": list(files.keys()) + ["meta.json"],
        }
        meta_path.write_text(json.dumps(meta, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    print(str(workspace))


if __name__ == "__main__":
    main()
