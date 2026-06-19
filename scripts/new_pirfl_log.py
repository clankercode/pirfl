#!/usr/bin/env python3
"""Create a PIRFL work log from the bundled template.

Usage:
  python scripts/new_pirfl_log.py "Task title" --out pirfl-log.md
"""
from __future__ import annotations

import argparse
import datetime as _dt
import re
from pathlib import Path


def slugify(text: str) -> str:
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", text.strip().lower()).strip("-")
    return slug or "pirfl-task"


def main() -> int:
    parser = argparse.ArgumentParser(description="Create a PIRFL log from assets/pirfl-log-template.md")
    parser.add_argument("title", help="Task title for the log")
    parser.add_argument("--out", "-o", help="Output markdown path. Defaults to pirfl-log-<slug>.md")
    parser.add_argument("--date", help="Override date string. Defaults to today's date")
    args = parser.parse_args()

    script_dir = Path(__file__).resolve().parent
    skill_root = script_dir.parent
    template_path = skill_root / "assets" / "pirfl-log-template.md"
    if not template_path.exists():
        raise FileNotFoundError(f"Template not found: {template_path}")

    out_path = Path(args.out) if args.out else Path(f"pirfl-log-{slugify(args.title)}.md")
    date = args.date or _dt.date.today().isoformat()

    text = template_path.read_text(encoding="utf-8")
    text = text.replace("{{TASK_TITLE}}", args.title).replace("{{DATE}}", date)

    if out_path.exists():
        raise FileExistsError(f"Refusing to overwrite existing file: {out_path}")

    out_path.write_text(text, encoding="utf-8")
    print(f"Created {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
