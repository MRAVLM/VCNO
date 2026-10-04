#!/usr/bin/env python3
"""VCNO repository validator — run by CI on every push, and locally:

    python3 scripts/validate.py

Checks (stdlib only, no dependencies):
  1. Every SKILL.md (skills/ and .claude/skills/) has valid frontmatter:
     - block delimiters --- ... ---
     - `name`: kebab-case, identical to its parent directory name
     - `description`: non-empty, at least 20 characters
  2. Every relative Markdown link in *.md (and .windsurfrules) resolves
     to an existing file/path. External links (http/https/mailto) and
     pure anchors (#...) are skipped; anchors on local links are stripped
     before resolving.

Exit code: 0 = all checks passed, 1 = at least one failure (all failures
are listed; the script does not stop at the first one).
"""
from __future__ import annotations

import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKIP_DIRS = {".git", "node_modules", ".freebuff"}
FRONTMATTER_RE = re.compile(
    r"^---\nname: (?P<name>[^\n]+)\n"
    r"description: (?P<desc>.+)\n---\n",
    re.DOTALL,
)
KEBAB_RE = re.compile(r"^[a-z0-9][a-z0-9-]*$")
LINK_RE = re.compile(r"\[[^\]]*\]\(([^)\s#]+)?(#[^)]*)?\)")
# LINK_RE group(1) is None for bare anchors like [text](#section)


def iter_files(suffix_check):
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for filename in filenames:
            if suffix_check(filename):
                yield os.path.join(dirpath, filename)


def check_frontmatter(errors):
    checked = 0
    for base in ("skills", os.path.join(".claude", "skills")):
        base_path = os.path.join(ROOT, base)
        if not os.path.isdir(base_path):
            continue
        for entry in sorted(os.listdir(base_path)):
            path = os.path.join(base_path, entry, "SKILL.md")
            if not os.path.isfile(path):
                continue
            checked += 1
            rel = os.path.relpath(path, ROOT)
            with open(path, encoding="utf-8") as fh:
                text = fh.read()
            match = FRONTMATTER_RE.match(text)
            if not match:
                errors.append(
                    f"{rel}: frontmatter must start the file as "
                    f"'---\\nname: <kebab-case>\\ndescription: <text>\\n---'"
                )
                continue
            name = match.group("name")
            if not KEBAB_RE.match(name):
                errors.append(
                    f"{rel}: name '{name}' is not kebab-case "
                    f"(lowercase letters, digits, hyphens)"
                )
            # '_' directories are templates with placeholders: still require
            # a kebab-case name above, but not an exact directory match.
            if not entry.startswith("_") and name != entry:
                errors.append(
                    f"{rel}: name '{name}' != directory '{entry}'"
                )
            desc = match.group("desc").strip()
            if len(desc) < 20:
                errors.append(f"{rel}: description too short ({len(desc)} chars)")
    return checked


def check_links(errors):
    checked = 0
    for path in iter_files(
        lambda f: f.endswith(".md") or f == ".windsurfrules"
    ):
        rel = os.path.relpath(path, ROOT)
        base = os.path.dirname(path)
        with open(path, encoding="utf-8") as fh:
            lines = fh.readlines()
        in_fence = False
        for lineno, line in enumerate(lines, start=1):
            if line.strip().startswith("```"):
                in_fence = not in_fence
                continue
            if in_fence:
                continue  # links inside code samples are not real links
            for match in LINK_RE.finditer(line):
                target = match.group(1)
                if target is None or target == "":
                    continue  # pure anchor link
                if target.startswith(("http://", "https://", "mailto:")):
                    continue
                checked += 1
                resolved = os.path.normpath(os.path.join(base, target))
                if not os.path.exists(resolved):
                    errors.append(
                        f"{rel}:{lineno}: broken relative link -> {target}"
                    )
    return checked


def main() -> int:
    errors: list[str] = []
    skills = check_frontmatter(errors)
    links = check_links(errors)

    print(f"frontmatter: {skills} SKILL.md files checked")
    print(f"links:       {links} relative links checked")

    if errors:
        print(f"\n{len(errors)} problem(s) found:")
        for err in errors:
            print(f"  - {err}")
        return 1
    print("\nall checks passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
