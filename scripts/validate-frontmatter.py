#!/usr/bin/env python3
"""Validate that key markdown files have valid YAML frontmatter."""

import glob
import re
import sys

REQUIRED_FRONTMATTER = {
    "SKILL.md": ["name", "description"],
    "agents/byescaleira.md": ["name", "description", "tools"],
}

FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)


def files_to_check():
    patterns = [
        "SKILL.md",
        "agents/*.md",
        ".claude/commands/*.md",
        ".claude/agents/*.md",
        ".claude/rules/*.md",
        ".claude/CLAUDE.md",
    ]
    found = set()
    for pattern in patterns:
        for path in glob.glob(pattern):
            found.add(path)
    return sorted(found)


def parse_frontmatter(content):
    match = FRONTMATTER_RE.match(content)
    if not match:
        return None
    raw = match.group(1)
    # Lightweight YAML-like parser for simple frontmatter keys
    data = {}
    for line in raw.splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if ":" in line:
            key, value = line.split(":", 1)
            data[key.strip()] = value.strip()
    return data


def main():
    errors = []
    for path in files_to_check():
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        fm = parse_frontmatter(content)
        required = REQUIRED_FRONTMATTER.get(path, [])
        if required and not fm:
            errors.append(f"{path}: missing frontmatter")
            continue
        for key in required:
            if fm is None or key not in fm:
                errors.append(f"{path}: missing required frontmatter key '{key}'")
    if errors:
        print("Frontmatter validation errors:")
        for e in errors:
            print(f"  - {e}")
        sys.exit(1)
    print("Frontmatter validation passed.")


if __name__ == "__main__":
    main()
