#!/usr/bin/env python3
"""Lightweight validator for this skill pack.

Checks:
- exactly one SKILL.md file,
- frontmatter exists,
- name matches parent folder,
- name uses lowercase letters, numbers, and hyphens,
- description is present and <= 1024 chars,
- key referenced files exist.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

NAME_RE = re.compile(r"^[a-z0-9](?:[a-z0-9-]{0,62}[a-z0-9])?$")


def parse_frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        raise ValueError("SKILL.md must start with YAML frontmatter")
    end = text.find("\n---\n", 4)
    if end == -1:
        raise ValueError("SKILL.md frontmatter must be closed with ---")
    raw = text[4:end]
    data: dict[str, str] = {}
    current_key: str | None = None
    for line in raw.splitlines():
        if not line.strip() or line.startswith("  "):
            continue
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        current_key = key.strip()
        value = value.strip().strip('"').strip("'")
        data[current_key] = value
    return data


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("skill_dir", nargs="?", default=".")
    args = parser.parse_args()
    root = Path(args.skill_dir).resolve()

    errors: list[str] = []
    skill_files = [p for p in root.rglob("SKILL.md") if p.is_file()]
    if len(skill_files) != 1:
        errors.append(f"Expected exactly one SKILL.md, found {len(skill_files)}: {skill_files}")
        skill_path = root / "SKILL.md"
    else:
        skill_path = skill_files[0]

    if not skill_path.exists():
        errors.append(f"Missing {skill_path}")
    else:
        try:
            fm = parse_frontmatter(skill_path.read_text(encoding="utf-8"))
            name = fm.get("name", "")
            desc = fm.get("description", "")
            if name != root.name:
                errors.append(f"name must match folder name: name={name!r}, folder={root.name!r}")
            if not NAME_RE.match(name) or "--" in name:
                errors.append(f"Invalid name: {name!r}")
            if not desc:
                errors.append("description is required")
            if len(desc) > 1024:
                errors.append(f"description too long: {len(desc)} chars")
        except Exception as exc:  # noqa: BLE001
            errors.append(str(exc))

    required_paths = [
        "references/cf-principles.md",
        "references/loop-protocol.md",
        "references/multi-task-orchestration.md",
        "references/subagent-prompts.md",
        "assets/pirfl-log-template.md",
        "assets/task-portfolio-template.md",
        "assets/reviewer-report-template.md",
    ]
    for rel in required_paths:
        if not (root / rel).exists():
            errors.append(f"Missing referenced file: {rel}")

    if errors:
        print("Skill validation failed:", file=sys.stderr)
        for err in errors:
            print(f"- {err}", file=sys.stderr)
        return 1

    print(f"Skill validation passed: {root}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
