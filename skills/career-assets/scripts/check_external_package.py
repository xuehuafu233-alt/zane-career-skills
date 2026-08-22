#!/usr/bin/env python3
"""Check that an external Skill package is visible, readable, and structurally complete."""

from __future__ import annotations

import argparse
import os
import stat
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("package", type=Path)
    parser.add_argument("--expected-skills", type=int)
    args = parser.parse_args()

    root = args.package.expanduser().resolve()
    skills = root / "skills"
    problems: list[str] = []

    if not skills.is_dir():
        problems.append("missing skills/ directory")
        skill_dirs: list[Path] = []
    else:
        skill_dirs = sorted(path for path in skills.iterdir() if path.is_dir())

    if args.expected_skills is not None and len(skill_dirs) != args.expected_skills:
        problems.append(f"expected {args.expected_skills} skill directories, found {len(skill_dirs)}")

    for skill_dir in skill_dirs:
        entry = skill_dir / "SKILL.md"
        if not entry.is_file() or not os.access(entry, os.R_OK):
            problems.append(f"missing or unreadable entrypoint: {entry.relative_to(root)}")

    hidden_flag = getattr(stat, "UF_HIDDEN", 0)
    for path in [root, *root.rglob("*")]:
        rel = path.relative_to(root)
        if path.name == ".DS_Store" or path.name.startswith("._"):
            problems.append(f"Finder metadata file: {rel}")
        try:
            if hidden_flag and path.stat().st_flags & hidden_flag:
                problems.append(f"macOS hidden flag: {rel}")
        except OSError as exc:
            problems.append(f"cannot stat {rel}: {exc}")

    if problems:
        print("FAIL external package")
        for problem in problems:
            print(f"- {problem}")
        return 2

    file_count = sum(1 for path in root.rglob("*") if path.is_file())
    print(f"PASS external package: skills={len(skill_dirs)} files={file_count}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
