#!/usr/bin/env python3
r"""Template scan script for Hygiene Inspector cron runs.

Purpose:
- Be written to /tmp via write_file
- Be executed with `python3 /tmp/hygiene_scan.py`
- Print JSON for the parent agent to turn into a markdown report

Pitfalls encoded here:
- Use a raw docstring so `\u` literals survive JSON write_file transport
- Do NOT use raw regex strings for patterns containing `\u`
- Deduplicate issues by `(path, severity, category, issue)`
"""

from __future__ import annotations

import json
import os
import re
from collections import Counter

ROOT = os.getcwd()
SLUG_CHARS = "a-z0-9\u00e0-\u1ef9-"
RE_LOWER_HYPHEN = re.compile("^[" + SLUG_CHARS + "]+$")
TEMP_SUFFIXES = (".tmp", ".bak", ".swp", "~")

issues = []
seen = set()


def add_issue(path, severity, category, issue, current, expected, suggested_fix):
    key = (path, severity, category, issue)
    if key in seen:
        return
    seen.add(key)
    issues.append(
        {
            "path": path,
            "severity": severity,
            "category": category,
            "issue": issue,
            "current": current,
            "expected": expected,
            "suggested_fix": suggested_fix,
        }
    )


def is_temp_file(name: str) -> bool:
    return name.endswith(TEMP_SUFFIXES)


# Example classification helpers. Extend these for the current repo.
def classify_draft_entry(rel_path: str):
    name = os.path.basename(rel_path)
    if name == ".gitkeep":
        add_issue(
            rel_path,
            "WARNING",
            "Orphan",
            "Placeholder file present in wiki/drafts/",
            name,
            "Drafts should contain actual markdown drafts only",
            "Remove .gitkeep once drafts exist",
        )
    elif is_temp_file(name):
        add_issue(
            rel_path,
            "WARNING",
            "Orphan",
            "Temporary file detected",
            rel_path,
            "Temporary files should be cleaned up",
            "Delete temporary file",
        )


def main():
    # Replace this walk with repo-specific whitelist logic.
    paths_checked = 0
    for dirpath, _, filenames in os.walk(ROOT):
        for filename in filenames:
            paths_checked += 1
            rel = os.path.relpath(os.path.join(dirpath, filename), ROOT)
            rel = rel.replace(os.sep, "/")
            if rel.startswith("wiki/drafts/"):
                classify_draft_entry(rel)

    severity_counts = Counter(issue["severity"] for issue in issues)
    issues.sort(key=lambda x: (x["severity"], x["path"], x["issue"]))
    print(
        json.dumps(
            {
                "paths_checked": paths_checked,
                "issues_total": len(issues),
                "severity_counts": dict(severity_counts),
                "issues": issues,
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
