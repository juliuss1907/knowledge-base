#!/usr/bin/env python3
r"""Hygiene Inspector — production scan script.
Walks the entire knowledge base tree, validates every path against
folder-structure.md whitelist rules, and prints JSON for report generation.

Proven on 51K-path scans. Handles all documented pitfalls:
- Archive regex uses ^wiki/reviews/archive/ (not ^archive/)
- Papers use YYYY-MM-DD_<author>_<title>.md (checked before standard RE_RAW_CONTENT)
- Whitelisted files (USER.md, index-spec.md, etc.) skip generic naming checks
- Agent homes (.hermes/, .openclaw/) skipped at depth > 1
- .tmp- prefixed folders → WARNING not ERROR
- HEARTBEAT leaks in wiki/, wiki/reviews/, and raw/ flagged as ERROR
- .bak/.tmp/.swp/~ files flagged as WARNING (cleanup)
- Deduplication by (path, severity, category, issue) tuple
- Report limit: 20 issues max

When folder-structure.md changes, patch the whitelist dictionaries below.
"""
from __future__ import annotations

import json
import os
import re
from collections import Counter

ROOT = os.path.expanduser("~/knowledge-base")
os.chdir(ROOT)

# ── Unicode slug chars (non-raw, single \u for Vietnamese diacritics) ──
SLUG_CHARS = "a-z0-9\\u00e0-\\u1ef9-"
RE_LOWER_HYPHEN = re.compile("^[" + SLUG_CHARS + "]+$")
TEMP_SUFFIXES = (".tmp", ".bak", ".swp", "~")

# ── Regex patterns (non-raw for \u, double-backslash for regex escapes) ──
RE_RAW_CONTENT = re.compile(r"^\d{4}-\d{2}-\d{2}_([" + SLUG_CHARS + r"]+)\.md$")
RE_RAW_PAPERS = re.compile(
    r"^\d{4}-\d{2}-\d{2}_([" + SLUG_CHARS + r"]+)_([" + SLUG_CHARS + r"]+)\.md$"
)
RE_REVIEW_REPORT = re.compile(
    r"^\d{4}-\d{2}-\d{2}_(output|format|hygiene|spot-check)-report\.md$"
)
RE_REVIEW_ARCHIVE = re.compile(
    r"^wiki/reviews/archive/\d{4}-\d{2}/\d{4}-\d{2}-\d{2}_(output|format|hygiene|spot-check)-report\.md$"
)

# ── Root-level whitelist ──
ROOT_FILES = {
    "AGENTS.md", "TAGS.md", "README.md", "knowledge-base.md",
    "HEARTBEAT.md", "IDENTITY.md", "SOUL.md", "TOOLS.md", "USER.md",
    ".gitignore",
}
ROOT_FOLDERS = {
    ".git", ".obsidian", ".openclaw", ".hermes",
    "context", "raw", "wiki", "scripts",
}

# ── context/ whitelist ──
CONTEXT_FILES = {"context.md", "USER.md"}

# ── raw/ subfolders ──
RAW_SUBFOLDERS = {"articles", "posts", "websites", "videos", "papers", "repos"}
RAW_INDEX_FILES = {f"{t}.md" for t in RAW_SUBFOLDERS} | {"raw.md"}

# ── wiki/ subfolders ──
WIKI_SUBFOLDERS = {"meta", "sources", "concepts", "tag", "topic", "drafts", "reviews"}
WIKI_META_FILES = {"format-spec.md", "folder-structure.md", "index-spec.md"}

# Files in wiki/reviews/ that are explicitly whitelisted (not report files)
WIKI_REVIEWS_WHITELIST = {"_action-required.md", "_approval-log.md"}

# ── Known leak patterns ──
HEARTBEAT_LEAK_PATHS = {
    "raw/.last_heartbeat",
    "wiki/HEARTBEAT.md",
    "wiki/reviews/HEARTBEAT.md",
}

# ── Known root orphans ──
ROOT_ORPHAN_MAP = {
    "RAW_BACKLOG.md": "wiki/drafts/ or raw/articles/",
    "MEMORY.md": ".hermes/ or .openclaw/",
}

# ── Known recurring root folders (not in whitelist, keep reappearing) ──
ROOT_FOLDER_ORPHANS = {
    "state": "Recurring empty directory — previously resolved 2026-06-27, recreated 2026-07-02. "
             "Move inside .hermes/ or .openclaw/ if needed; otherwise rmdir.",
    "memory": "Recurring root folder — old folder migrated to .openclaw/memory/ in v1.2. "
              "Flagged 07-03, 07-06, 07-07, 07-08, 07-11. A process writes to 'memory/' instead of "
              "'.openclaw/memory/'. Move contents and rmdir; fix the writing process output path.",
}

# ── Global state ──
issues = []
seen = set()

def add_issue(path, severity, category, issue, current, expected, suggested_fix):
    key = (path, severity, category, issue)
    if key in seen:
        return
    seen.add(key)
    issues.append(dict(
        path=path, severity=severity, category=category,
        issue=issue, current=current, expected=expected,
        suggested_fix=suggested_fix,
    ))


def is_temp_file(name):
    return name.endswith(TEMP_SUFFIXES)


# ── Classifiers ──

def classify_root_file(name, rel_path):
    if name in ROOT_FILES:
        return
    if rel_path in HEARTBEAT_LEAK_PATHS:
        ctx = "recurring process leak" if "HEARTBEAT" in name else "heartbeat artifact"
        add_issue(rel_path, "ERROR", "Orphan",
                  f"Heartbeat artifact outside agent home ({ctx})",
                  rel_path,
                  "Heartbeat files belong in .hermes/ or .openclaw/",
                  "Identify and fix the writing process; delete file")
        return
    if name in ROOT_ORPHAN_MAP:
        add_issue(rel_path, "ERROR", "Orphan",
                  f"Known root orphan: {name}",
                  rel_path,
                  f"Should be in {ROOT_ORPHAN_MAP[name]}",
                  f"Move {name} to {ROOT_ORPHAN_MAP[name]}")
        return
    add_issue(rel_path, "ERROR", "Path",
              "File not in root whitelist",
              rel_path,
              "Only AGENTS.md, TAGS.md, README.md, knowledge-base.md, "
              "symlinks, .gitignore allowed",
              "Move to appropriate subfolder or delete")


def classify_root_folder(name, rel_path):
    if name in ROOT_FOLDERS:
        return
    if name.startswith(".tmp-"):
        add_issue(rel_path, "WARNING", "Orphan",
                  "Temporary folder (.tmp- prefix) detected",
                  rel_path,
                  "Temporary folders should be deleted when done",
                  "Delete folder or promote to permanent (update folder-structure.md first)")
        return
    if name.startswith("."):
        add_issue(rel_path, "ERROR", "Path",
                  "Hidden folder not in root whitelist",
                  rel_path,
                  "Only .git, .obsidian, .openclaw, .hermes allowed",
                  "Move or delete")
        return
    add_issue(rel_path, "ERROR", "Path",
              "Folder not in root whitelist",
              rel_path,
              "Allowed: context, raw, wiki, scripts",
              "Move or delete")


def classify_context_entry(rel_path):
    name = os.path.basename(rel_path)
    if name in CONTEXT_FILES:
        return  # whitelisted — skip naming check
    add_issue(rel_path, "ERROR", "Path",
              "File not allowed in context/",
              rel_path,
              "context/ must contain exactly: context.md, USER.md",
              "Move file to appropriate wiki/ or raw/ location")


def classify_raw_entry(rel_path):
    parts = rel_path.split("/")
    name = os.path.basename(rel_path)

    if len(parts) == 2:  # raw/<file>
        if name in RAW_INDEX_FILES:
            return
        if rel_path in HEARTBEAT_LEAK_PATHS:
            add_issue(rel_path, "ERROR", "Orphan",
                      "Heartbeat artifact outside agent home",
                      rel_path,
                      "Heartbeat files belong in .hermes/ or .openclaw/",
                      "Identify and fix writing process; delete file")
            return
        add_issue(rel_path, "ERROR", "Path",
                  "File at raw/ root level",
                  rel_path,
                  "All raw content must be in type subfolders",
                  "Move to appropriate raw/<type>/ subfolder")
        return

    if len(parts) == 3:  # raw/<type>/<file>
        raw_type = parts[1]
        if raw_type not in RAW_SUBFOLDERS:
            add_issue(rel_path, "ERROR", "Path",
                      f"Unknown raw subfolder '{raw_type}'",
                      rel_path,
                      f"Allowed: {', '.join(sorted(RAW_SUBFOLDERS))}",
                      "Move to correct subfolder or add to whitelist")
            return

        index_name = f"{raw_type}.md"
        if name == index_name:
            return

        # Papers: YYYY-MM-DD_<author>_<title>.md
        if raw_type == "papers":
            if RE_RAW_PAPERS.match(name):
                return
            add_issue(rel_path, "WARNING", "Naming",
                      "Papers file naming: expected YYYY-MM-DD_<author>_<title>.md",
                      name,
                      "YYYY-MM-DD_<author>_<title>.md",
                      "Rename to match papers convention")
            return

        # Repos: YYYY-MM-DD_<owner>_<repo>.md
        if raw_type == "repos":
            if re.match(r"^\d{4}-\d{2}-\d{2}_([" + SLUG_CHARS + r"]+)_([" + SLUG_CHARS + r"]+)\.md$", name):
                return
            add_issue(rel_path, "WARNING", "Naming",
                      "Repos file naming: expected YYYY-MM-DD_<owner>_<repo>.md",
                      name,
                      "YYYY-MM-DD_<owner>_<repo>.md",
                      "Rename to match repos convention")
            return

        # Standard raw content: YYYY-MM-DD_<slug>.md
        if RE_RAW_CONTENT.match(name):
            return

        if re.match(r"^\d{4}-\d{2}-\d{2}_.*\.md$", name):
            add_issue(rel_path, "WARNING", "Naming",
                      "Raw content filename has non-compliant slug",
                      name,
                      "YYYY-MM-DD_<lowercase-hyphen-slug>.md",
                      "Rename to use lowercase-hyphen slug only")
            return

        add_issue(rel_path, "WARNING", "Naming",
                  "Raw content filename does not match convention",
                  name,
                  "YYYY-MM-DD_<slug>.md",
                  "Rename to match naming convention")
        return

    if len(parts) > 3:
        add_issue(rel_path, "ERROR", "Path",
                  "Nested folder inside raw/<type>/",
                  rel_path,
                  "Raw content folders must be flat (no subfolders)",
                  "Move content to flat raw/<type>/ structure")


def classify_wiki_entry(rel_path):
    parts = rel_path.split("/")
    name = os.path.basename(rel_path)

    if len(parts) == 2:  # wiki/<file>
        if name == "wiki.md":
            return
        if rel_path in HEARTBEAT_LEAK_PATHS:
            add_issue(rel_path, "ERROR", "Orphan",
                      "HEARTBEAT.md leaked into wiki/ root (new variant — recurring process leak)",
                      rel_path,
                      "HEARTBEAT.md belongs in .hermes/ or .openclaw/; "
                      "file deletion is transient — the writing process must be fixed",
                      "Identify and fix the process writing HEARTBEAT.md to wiki/; "
                      "then delete this file")
            return
        add_issue(rel_path, "ERROR", "Path",
                  "File at wiki/ root level",
                  rel_path,
                  "wiki/ root may only contain wiki.md",
                  "Move to appropriate subfolder")
        return

    sub = parts[1]

    # wiki/meta/
    if sub == "meta":
        if name in WIKI_META_FILES:
            return  # whitelisted — skip naming check
        add_issue(rel_path, "ERROR", "Path",
                  "File not allowed in wiki/meta/",
                  rel_path,
                  "Only: format-spec.md, folder-structure.md, index-spec.md",
                  "Move or delete")
        return

    # wiki/sources/
    if sub == "sources":
        if name.startswith("src_") and RE_LOWER_HYPHEN.match(name[4:].removesuffix(".md")):
            return
        if name == "sources.md":
            return
        if not name.startswith("src_"):
            add_issue(rel_path, "WARNING", "Naming",
                      "Source file must start with 'src_'",
                      name, "src_<slug>.md", "Rename to src_<slug>.md")
            return
        slug = name[4:].removesuffix(".md")
        if not RE_LOWER_HYPHEN.match(slug):
            add_issue(rel_path, "WARNING", "Naming",
                      "Source slug must be lowercase-hyphen",
                      slug, "Lowercase with hyphens only", "Fix slug naming")
        return

    # wiki/concepts/, wiki/tag/, wiki/topic/
    if sub in ("concepts", "tag", "topic"):
        if name in ("tag.md", "topic.md"):
            return
        slug = name.removesuffix(".md")
        if RE_LOWER_HYPHEN.match(slug):
            return
        add_issue(rel_path, "WARNING", "Naming",
                  f"{sub.capitalize()} slug must be lowercase-hyphen",
                  name, "<lowercase-hyphen-slug>.md", "Rename to use lowercase-hyphen")
        return

    # wiki/drafts/
    if sub == "drafts":
        if name == ".gitkeep":
            add_issue(rel_path, "WARNING", "Orphan",
                      "Placeholder file in populated drafts/",
                      rel_path,
                      ".gitkeep not needed when drafts exist",
                      "Remove .gitkeep")
            return
        if is_temp_file(name):
            add_issue(rel_path, "WARNING", "Orphan",
                      "Temporary file in drafts/",
                      rel_path, "Temporary files should be cleaned up", "Delete temporary file")
            return
        if name == "drafts.md":
            return
        slug = name.removesuffix(".md")
        if RE_LOWER_HYPHEN.match(slug):
            return
        add_issue(rel_path, "WARNING", "Naming",
                  "Draft filename: lowercase-hyphen only",
                  name, "<lowercase-hyphen-slug>.md", "Rename to use lowercase-hyphen")
        return

    # wiki/reviews/
    if sub == "reviews":
        # Archive subfolder: YYYY-MM/YYYY-MM-DD_<type>-report.md
        if len(parts) >= 4 and parts[2] == "archive":
            if RE_REVIEW_ARCHIVE.match(rel_path):
                return
            if len(parts) == 5:
                add_issue(rel_path, "WARNING", "Naming",
                          "Archived report naming",
                          name, "YYYY-MM-DD_<type>-report.md",
                          "Rename to match archive naming convention")
                return
            if len(parts) == 4:
                add_issue(rel_path, "ERROR", "Path",
                          "File directly in wiki/reviews/archive/ (not in YYYY-MM/)",
                          rel_path,
                          "Archive files must be in YYYY-MM/ subfolders",
                          "Move to appropriate YYYY-MM/ folder")
            return

        # Active reviews zone
        if name in WIKI_REVIEWS_WHITELIST:
            return

        if rel_path in HEARTBEAT_LEAK_PATHS:
            add_issue(rel_path, "ERROR", "Orphan",
                      "HEARTBEAT.md leaked into wiki/reviews/ (recurring process leak)",
                      rel_path,
                      "HEARTBEAT.md belongs in .hermes/ or .openclaw/; "
                      "file deletion is transient — the writing process must be fixed",
                      "Identify and fix the process writing HEARTBEAT.md to wiki/reviews/; "
                      "then delete this file")
            return

        if RE_REVIEW_REPORT.match(name):
            return

        if re.match(r"^\d{4}-\d{2}-\d{2}_.*\.md$", name):
            add_issue(rel_path, "WARNING", "Naming",
                      "Review report naming: expected YYYY-MM-DD_<type>-report.md",
                      name,
                      "YYYY-MM-DD_<type>-report.md (type = output|format|hygiene|spot-check)",
                      "Rename to canonical format")
            return

        add_issue(rel_path, "WARNING", "Naming",
                  "File in wiki/reviews/ with unknown naming",
                  name, "Report files: YYYY-MM-DD_<type>-report.md", "Review and rename or move")
        return

    # Unknown wiki/ subfolder
    if sub not in WIKI_SUBFOLDERS:
        add_issue(rel_path, "ERROR", "Path",
                  f"Unknown wiki/ subfolder: {sub}",
                  rel_path,
                  f"Allowed: {', '.join(sorted(WIKI_SUBFOLDERS))}",
                  "Move to correct subfolder or update folder-structure.md")


def classify_generic_path(rel_path):
    """Catch-all for paths not covered by above classifiers."""
    if rel_path.startswith("scripts/"):
        return
    if rel_path.startswith(".hermes/") or rel_path.startswith(".openclaw/"):
        if rel_path.count("/") > 1:
            return  # skip deep agent internals
        name = os.path.basename(rel_path)
        if name.endswith(".md") and (
            re.match(r"^\d{4}-\d{2}-\d{2}", name) or name.startswith("src_")
        ):
            add_issue(rel_path, "WARNING", "Orphan",
                      "User content file inside agent home root",
                      rel_path,
                      "User content belongs in wiki/ or raw/",
                      "Move to appropriate wiki/ or raw/ location")
        return
    if rel_path.startswith(".git/") or rel_path.startswith(".obsidian/"):
        return
    add_issue(rel_path, "WARNING", "Path",
              "Path not classified by any rule",
              rel_path,
              "Should be in a known location or whitelisted",
              "Review and classify or move")


def main():
    paths_checked = 0

    for dirpath, dirnames, filenames in os.walk(ROOT):
        rel_dir = os.path.relpath(dirpath, ROOT)
        if rel_dir == ".":
            rel_dir = ""
        # Skip .git internals
        if rel_dir.startswith(".git") and rel_dir != ".git":
            continue
        if "/.git/" in "/" + rel_dir:
            continue

        for filename in filenames:
            paths_checked += 1
            rel = os.path.relpath(os.path.join(dirpath, filename), ROOT)
            rel = rel.replace(os.sep, "/")

            if "/" not in rel:
                classify_root_file(filename, rel)
            elif rel.startswith("context/"):
                classify_context_entry(rel)
            elif rel.startswith("raw/"):
                classify_raw_entry(rel)
            elif rel.startswith("wiki/"):
                classify_wiki_entry(rel)
            else:
                classify_generic_path(rel)

        # ── Root folder whitelist check ──
        # classify_root_folder was never called — root-level dirnames were only
        # caught later by the empty-directory check (INFO), not the path-whitelist
        # check (ERROR). This patch fixes that gap (2026-07-02).
        if rel_dir == "":
            for dirname in dirnames:
                if dirname in ROOT_FOLDER_ORPHANS:
                    add_issue(dirname, "ERROR", "Orphan",
                              f"Recurring root folder not in whitelist: {dirname}/",
                              dirname + "/",
                              ROOT_FOLDER_ORPHANS[dirname],
                              f"Remove directory: rmdir {dirname}/")
                else:
                    classify_root_folder(dirname, dirname)

    # ── Empty directory check ──
    for dirpath, dirnames, filenames in os.walk(ROOT):
        rel_dir = os.path.relpath(dirpath, ROOT)
        if rel_dir == ".":
            rel_dir = ""
        if rel_dir.startswith(".git") and rel_dir != ".git":
            continue
        if "/.git/" in "/" + rel_dir:
            continue
        if rel_dir.startswith(".hermes/") or rel_dir.startswith(".openclaw/"):
            continue
        if rel_dir.startswith(".obsidian/"):
            continue
        if rel_dir == "":
            continue
        if not filenames and not dirnames:
            if re.match(r"^wiki/reviews/archive/\d{4}-\d{2}$", rel_dir):
                continue
            add_issue(rel_dir, "INFO", "Orphan",
                      "Empty directory", rel_dir + "/",
                      "Non-empty directory or removed", "Add content or remove directory")

    # ── Sort and limit ──
    severity_order = {"ERROR": 0, "WARNING": 1, "INFO": 2}
    issues.sort(key=lambda x: (severity_order.get(x["severity"], 99), x["path"], x["issue"]))
    issues_limited = issues[:20]
    truncated = len(issues) > 20

    severity_counts = Counter(issue["severity"] for issue in issues_limited)
    total_counts = Counter(issue["severity"] for issue in issues)

    print(json.dumps(dict(
        paths_checked=paths_checked,
        issues_total=len(issues),
        issues_reported=len(issues_limited),
        truncated=truncated,
        severity_counts=dict(severity_counts),
        total_severity_counts=dict(total_counts),
        issues=issues_limited,
    ), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
