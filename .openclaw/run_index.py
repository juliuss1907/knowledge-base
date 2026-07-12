#!/usr/bin/env python3
"""Index Agent — Incremental mode. Reads all wiki frontmatter, rewrites only affected indexes."""

import os
import re
import sys
import yaml
from datetime import datetime, timezone, timedelta
from collections import defaultdict

KB = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(KB)

LAST_SUCCESS_FILE = ".openclaw/last-index-success.txt"
TAGS_FILE = "TAGS.md"
TAG_MD = "wiki/tag/tag.md"

TZ = timezone(timedelta(hours=7))
TODAY = datetime.now(TZ).strftime("%Y-%m-%d")
NOW_ISO = datetime.now(TZ).strftime("%Y-%m-%d %H:%M:%S")
NOW_DATE_ISO = datetime.now(TZ).strftime("%Y-%m-%d")

LOG_LINES = []
WARNINGS = []
ERRORS = []

def log(msg):
    LOG_LINES.append(msg)
    print(msg)

def warn(msg):
    WARNINGS.append(msg)
    print(f"  ⚠ {msg}")

def err(msg):
    ERRORS.append(msg)
    print(f"  ❌ {msg}")

# ── Step 0: Parse TAGS.md ──────────────────────────────────────────────
log("── Step 0: Parsing TAGS.md ──")

with open(TAGS_FILE) as f:
    tags_content = f.read()

# Parse main tags (Pool A)
main_tags = {}
m = re.search(r'## 2\. Pool A.*?\n\n(.*?)(?=\n## 3\.|\Z)', tags_content, re.DOTALL)
if m:
    for line in m.group(1).strip().split('\n'):
        line = line.strip()
        if line.startswith('| `#'):
            parts = [p.strip() for p in line.split('|')]
            tag_name = parts[1].replace('`', '').replace('#', '')
            desc = parts[2] if len(parts) > 2 else ""
            main_tags[tag_name] = desc

# Parse sub tags (Pool B)
sub_tags = {}
m = re.search(r'## 3\. Pool B.*?\n\n(.*?)(?=\n## 4\.|\Z)', tags_content, re.DOTALL)
if m:
    for line in m.group(1).strip().split('\n'):
        line = line.strip()
        if line.startswith('| `#'):
            parts = [p.strip() for p in line.split('|')]
            tag_name = parts[1].replace('`', '').replace('#', '')
            desc = parts[2] if len(parts) > 2 else ""
            sub_tags[tag_name] = desc

allowed_main = set(main_tags.keys())
allowed_sub = set(sub_tags.keys())
all_allowed = allowed_main | allowed_sub

log(f"  Main tags: {len(main_tags)} — {', '.join(sorted(allowed_main))}")
log(f"  Sub tags: {len(sub_tags)} — {', '.join(sorted(allowed_sub))}")

# ── Step 1: Scan all wiki files ────────────────────────────────────────
log(f"\n── Step 1: Scanning wiki/ files ──")

wiki_files = []
for root, dirs, files in os.walk("wiki"):
    # Only sources and concepts
    rel_root = os.path.relpath(root, "wiki")
    if rel_root not in ("sources", "concepts"):
        continue
    for f in files:
        if f.endswith(".md"):
            wiki_files.append(os.path.join(root, f))

log(f"  Found {len(wiki_files)} wiki files")

files_data = []
invalid_tags_found = []

for fpath in sorted(wiki_files):
    try:
        with open(fpath) as f:
            content = f.read()
    except Exception as ex:
        warn(f"Cannot read {fpath}: {ex}")
        continue

    # Extract frontmatter
    fm_match = re.match(r'^---\s*\n(.*?)\n---', content, re.DOTALL)
    if not fm_match:
        warn(f"No frontmatter: {fpath}")
        continue

    try:
        fm = yaml.safe_load(fm_match.group(1))
    except yaml.YAMLError as ex:
        err(f"Invalid YAML: {fpath} — {ex}")
        continue

    if not isinstance(fm, dict):
        warn(f"Frontmatter not a dict: {fpath}")
        continue

    ftype = fm.get("type", "")
    if ftype not in ("source", "concept"):
        warn(f"Unknown type '{ftype}': {fpath}")
        continue

    main_tag = fm.get("main_tag", "")
    sub_tags_raw = fm.get("sub_tags", [])
    topic = fm.get("topic", "")

    # Validate main_tag
    if not main_tag:
        warn(f"Missing main_tag: {fpath}")
        continue
    if main_tag not in allowed_main:
        invalid_tags_found.append((fpath, "main_tag", main_tag))
        warn(f"Invalid main_tag '{main_tag}': {fpath}")

    # Validate sub_tags
    valid_subs = []
    if isinstance(sub_tags_raw, list):
        for st in sub_tags_raw:
            st = str(st).strip()
            if st in allowed_sub:
                valid_subs.append(st)
            else:
                invalid_tags_found.append((fpath, "sub_tag", st))

    slug = os.path.splitext(os.path.basename(fpath))[0]

    # Derive title from slug
    if ftype == "source" and slug.startswith("src_"):
        display_slug = slug[4:]
    else:
        display_slug = slug
    title = " ".join(w.capitalize() for w in display_slug.replace("-", " ").split())

    files_data.append({
        "path": fpath,
        "slug": slug,
        "title": title,
        "type": ftype,
        "main_tag": main_tag,
        "sub_tags": valid_subs,
        "topic": topic,
        "all_tags": [main_tag] + valid_subs,
    })

log(f"  Parsed {len(files_data)} valid files")
if invalid_tags_found:
    log(f"  ⚠ {len(invalid_tags_found)} invalid tag(s) found:")
    for fp, tag_type, tag_val in invalid_tags_found:
        log(f"    {fp}: {tag_type}={tag_val}")

# ── Step 2: Determine changed files ────────────────────────────────────
log(f"\n── Step 2: Determining affected indexes ──")

changed_slugs = set()
try:
    if os.path.exists(LAST_SUCCESS_FILE):
        last_ts = open(LAST_SUCCESS_FILE).read().strip()
        for fp in os.popen(f'find wiki/sources/ wiki/concepts/ -name "*.md" -newer {LAST_SUCCESS_FILE} -type f 2>/dev/null').read().strip().split('\n'):
            if fp:
                changed_slugs.add(os.path.splitext(os.path.basename(fp))[0])
except Exception as ex:
    log(f"  Cannot determine changed files: {ex}")
    changed_slugs = set(fd["slug"] for fd in files_data)

log(f"  Changed files: {len(changed_slugs)}")

# Determine all used tags and topics (from all files, not just changed)
all_tags = set()
all_topics = set()
for fd in files_data:
    all_tags.add(fd["main_tag"])
    for st in fd["sub_tags"]:
        all_tags.add(st)
    if fd["topic"]:
        all_topics.add(fd["topic"])

log(f"  All tags in use: {len(all_tags)}")
log(f"  All topics in use: {len(all_topics)}")

# ── Step 3: Build tag → files index ───────────────────────────────────
log(f"\n── Step 3: Building tag index ──")

tag_index = defaultdict(lambda: {"concepts": [], "sources": []})
for fd in files_data:
    for tag in fd["all_tags"]:
        if fd["type"] == "concept":
            tag_index[tag]["concepts"].append(fd)
        else:
            tag_index[tag]["sources"].append(fd)

# Sort within each tag
for tag in tag_index:
    tag_index[tag]["concepts"].sort(key=lambda x: x["slug"])
    tag_index[tag]["sources"].sort(key=lambda x: x["slug"])

# ── Step 4: Co-occurrence ─────────────────────────────────────────────
log(f"\n── Step 4: Computing co-occurrence ──")

co_occurrence = defaultdict(int)
for fd in files_data:
    tags = list(set(fd["all_tags"]))  # unique tags per file
    for i in range(len(tags)):
        for j in range(i+1, len(tags)):
            pair = tuple(sorted([tags[i], tags[j]]))
            co_occurrence[pair] += 1

# Per-tag co-occurrence (top 5)
tag_co_occur = {}
for tag in all_tags:
    pairs = []
    for (t1, t2), count in co_occurrence.items():
        other = t2 if t1 == tag else (t1 if t2 == tag else None)
        if other and other in all_tags:
            pairs.append((other, count))
    pairs.sort(key=lambda x: -x[1])
    tag_co_occur[tag] = pairs[:5]

# ── Step 5: Build topic index ─────────────────────────────────────────
log(f"\n── Step 5: Building topic index ──")

topic_index = defaultdict(lambda: {"concepts": [], "sources": []})
for fd in files_data:
    topic = fd["topic"]
    if not topic:
        continue
    if fd["type"] == "concept":
        topic_index[topic]["concepts"].append(fd)
    else:
        topic_index[topic]["sources"].append(fd)

for topic in topic_index:
    topic_index[topic]["concepts"].sort(key=lambda x: x["slug"])
    topic_index[topic]["sources"].sort(key=lambda x: x["slug"])

# Topic overlap
log(f"  Computing topic overlap...")
topic_overlap = defaultdict(int)
topic_list = list(topic_index.keys())
for idx, t1 in enumerate(topic_list):
    files1 = set(fd["path"] for fd in topic_index[t1]["concepts"] + topic_index[t1]["sources"])
    for t2 in topic_list[idx+1:]:
        files2 = set(fd["path"] for fd in topic_index[t2]["concepts"] + topic_index[t2]["sources"])
        shared = len(files1 & files2)
        if shared > 0:
            topic_overlap[tuple(sorted([t1, t2]))] = shared

# Per-topic related (top 5)
topic_related = {}
for topic in topic_list:
    pairs = []
    for (tp1, tp2), count in topic_overlap.items():
        other = tp2 if tp1 == topic else (tp1 if tp2 == topic else None)
        if other:
            pairs.append((other, count))
    pairs.sort(key=lambda x: -x[1])
    topic_related[topic] = pairs[:5]

# ── Step 6: Write tag index files ─────────────────────────────────────
log(f"\n── Step 6: Writing tag index files ──")

os.makedirs("wiki/tag", exist_ok=True)

def derive_title(slug):
    return " ".join(w.capitalize() for w in slug.replace("-", " ").split())

written_tags = 0
for tag in all_tags:
    data = tag_index[tag]
    co_occs = tag_co_occur.get(tag, [])

    content = f"""---
type: index
level: 3
scope: tag
parent: "[[tag]]"
tag: {tag}
auto_generated: true
last_updated: {TODAY}
---

# Tag: #{tag}

## Parent

- [[tag]]

## Stats

- Total files: {len(data['concepts']) + len(data['sources'])}
- Sources: {len(data['sources'])}
- Concepts: {len(data['concepts'])}
- Last updated: {TODAY}

## Files with this tag

"""

    all_items = []
    for fd in data["concepts"]:
        all_items.append((fd["slug"], fd["title"], "concept"))
    for fd in data["sources"]:
        all_items.append((fd["slug"], fd["title"], "source"))
    all_items.sort(key=lambda x: x[0])

    for slug, title, ftype in all_items:
        content += f"- [[{slug}]] — {title} ({ftype})\n"

    if co_occs:
        content += "\n## Co-occurring tags\n\n"
        for other_tag, count in co_occs:
            unit = "co-occurrence" if count == 1 else "co-occurrences"
            content += f"- [[{other_tag}]] — {count} {unit}\n"

    fpath = f"wiki/tag/{tag}.md"
    with open(fpath, "w") as f:
        f.write(content)
    written_tags += 1

log(f"  Written: {written_tags} tag index files")

# ── Step 7: Write topic index files ────────────────────────────────────
log(f"\n── Step 7: Writing topic index files ──")

os.makedirs("wiki/topic", exist_ok=True)

written_topics = 0
for topic in all_topics:
    data = topic_index[topic]
    related = topic_related.get(topic, [])

    content = f"""---
type: index
scope: topic
parent: "[[topic]]"
topic: {topic}
auto_generated: true
last_updated: {TODAY}
---

# Topic: {topic}

Auto-generated index of all content with topic `{topic}`.

Last updated: {NOW_ISO}

---

## Concepts ({len(data['concepts'])})

"""
    for fd in data["concepts"]:
        subs = ", ".join(f"#{s}" for s in fd["sub_tags"])
        content += f"- [[{fd['slug']}]] — main: #{fd['main_tag']}, sub: [{subs}]\n"

    content += f"\n## Sources ({len(data['sources'])})\n\n"
    for fd in data["sources"]:
        subs = ", ".join(f"#{s}" for s in fd["sub_tags"])
        content += f"- [[{fd['slug']}]] — main: #{fd['main_tag']}, sub: [{subs}]\n"

    if related:
        content += "\n## Related topics\n\n"
        content += f"Topics that share concepts/sources with `{topic}`:\n"
        for other_topic, count in related:
            content += f"- `{other_topic}` ({count} shared files)\n"

    fpath = f"wiki/topic/{topic}.md"
    with open(fpath, "w") as f:
        f.write(content)
    written_topics += 1

log(f"  Written: {written_topics} topic index files")

# ── Step 8: Clean up orphaned indexes ──────────────────────────────────
log(f"\n── Step 8: Cleaning orphans ──")

# Orphan tag indexes
tag_orphans = 0
for fname in os.listdir("wiki/tag"):
    if fname.endswith(".md") and fname != "tag.md":
        tag_name = fname[:-3]
        if tag_name not in all_tags:
            os.remove(f"wiki/tag/{fname}")
            log(f"  Deleted orphan tag: {fname}")
            tag_orphans += 1

# Orphan topic indexes
topic_orphans = 0
for fname in os.listdir("wiki/topic"):
    if fname.endswith(".md"):
        topic_name = fname[:-3]
        if topic_name not in all_topics:
            os.remove(f"wiki/topic/{fname}")
            log(f"  Deleted orphan topic: {fname}")
            topic_orphans += 1

log(f"  Orphans deleted: {tag_orphans} tags + {topic_orphans} topics")

# ── Step 9: Update tag.md master index ─────────────────────────────────
log(f"\n── Step 9: Updating tag.md ──")

# Compute tag counts
tag_counts = {}
for tag in all_tags:
    data = tag_index[tag]
    tag_counts[tag] = len(data["concepts"]) + len(data["sources"])

# Find top 3 most used
top_3 = sorted(tag_counts.items(), key=lambda x: -x[1])[:3]
most_used = ", ".join(f"#{t} ({c})" for t, c in top_3)

total_tags = len(all_tags)
# Only count tags in allowed_main that are actually used
active_main = [t for t in allowed_main if t in all_tags]
active_sub = [t for t in allowed_sub if t in all_tags]

main_section = "### Main Tags (Pool A)\n\n"
for tag in sorted(active_main):
    desc = main_tags.get(tag, "")
    main_section += f"- [[{tag}]] — {desc}\n"

sub_section = "### Sub Tags (Pool B)\n\n"
for tag in sorted(active_sub):
    desc = sub_tags.get(tag, "")
    sub_section += f"- [[{tag}]] — {desc}\n"

tag_md_content = f"""---
type: index
level: 2
scope: tags
parent: "[[wiki]]"
auto_generated: false
items_managed_by: index-agent
last_updated: {TODAY}
---

# Tag Index

Master index of all tags in the Knowledge Base.

Last updated: {NOW_ISO}

---

## Overview

Auto-generated master index of all tags used in the Knowledge Base. Tracks statistics, files per tag, and co-occurrence relationships across both main-tags (Pool A) and sub-tags (Pool B).

## Parent

- [[wiki]]

## Stats

- Total tags: {total_tags}
- Main tags: {len(active_main)}
- Sub tags: {len(active_sub)}
- Most used: {most_used}
- Last updated: {TODAY}

## Items

{main_section}
{sub_section}
## Notes

<!-- Auto-managed by index-agent. Manual notes below this line. -->
"""

with open(TAG_MD, "w") as f:
    f.write(tag_md_content)
log(f"  Updated tag.md: {total_tags} tags ({len(active_main)} main + {len(active_sub)} sub)")

# ── Step 10: Write success timestamp ───────────────────────────────────
log(f"\n── Step 10: Writing success timestamp ──")

with open(LAST_SUCCESS_FILE, "w") as f:
    f.write(NOW_ISO.replace(" ", "T") + "+07:00")
log(f"  Written: {LAST_SUCCESS_FILE}")

# ── Summary ────────────────────────────────────────────────────────────
log(f"\n══ Index run complete ══")
log(f"  Mode: incremental ({len(changed_slugs)} changed files)")
log(f"  Scanned: {len(files_data)} wiki files")
log(f"  Tags indexed: {written_tags}")
log(f"  Topics indexed: {written_topics}")
log(f"  Orphans: {tag_orphans} tags + {topic_orphans} topics")
log(f"  Invalid tags: {len(invalid_tags_found)}")
log(f"  Warnings: {len(WARNINGS)}")
log(f"  Errors: {len(ERRORS)}")

if ERRORS:
    log("\n!! ERRORS DETECTED !!")
    sys.exit(1)
