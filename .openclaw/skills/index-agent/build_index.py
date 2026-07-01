#!/usr/bin/env python3
"""Index Agent: Build tag and topic indexes from wiki content files."""
import os
import re
import yaml
import sys
from datetime import datetime, timezone, timedelta
from collections import defaultdict

KB = "/home/julius/knowledge-base"
NOW = datetime.now(timezone(timedelta(hours=7))).strftime("%Y-%m-%d %H:%M:%S")
TZ = "+07:00"

# ── Load TAGS.md ──────────────────────────────────────────────────
with open(os.path.join(KB, "TAGS.md")) as f:
    tags_content = f.read()

# Extract Pool A (main-tags)
pool_a_match = re.search(r'## 2\. Pool A.*?\n\n((?:.|\n)*?)## 3\.', tags_content)
pool_a_text = pool_a_match.group(1)
main_tags = set(re.findall(r'\| `#(\w[\w-]*)`', pool_a_text))
print(f"[TAGS] Pool A main-tags: {sorted(main_tags)}")

# Extract Pool B (sub-tags)
pool_b_match = re.search(r'## 3\. Pool B.*?\n\n((?:.|\n)*?)## 4\.', tags_content)
pool_b_text = pool_b_match.group(1)
sub_tags = set(re.findall(r'\| `#(\w[\w-]*)`', pool_b_text))
print(f"[TAGS] Pool B sub-tags: {sorted(sub_tags)}")

# ── Scan wiki files ───────────────────────────────────────────────
files = []
errors = []
invalid_tags_found = []

for dirpath in ["wiki/sources", "wiki/concepts"]:
    full_path = os.path.join(KB, dirpath)
    if not os.path.isdir(full_path):
        continue
    for fname in sorted(os.listdir(full_path)):
        if not fname.endswith(".md"):
            continue
        fpath = os.path.join(dirpath, fname)
        full_fpath = os.path.join(KB, fpath)

        with open(full_fpath) as f:
            content = f.read()

        # Extract YAML frontmatter between first two ---
        fm_match = re.match(r'^---\s*\n(.*?)\n---', content, re.DOTALL)
        if not fm_match:
            errors.append(f"[WARNING] {fpath}: No frontmatter found — skipped")
            continue

        try:
            fm = yaml.safe_load(fm_match.group(1))
            if fm is None:
                fm = {}
        except yaml.YAMLError as e:
            errors.append(f"[ERROR] {fpath}: Invalid YAML — {str(e)[:80]}")
            continue

        if not isinstance(fm, dict):
            errors.append(f"[ERROR] {fpath}: Frontmatter is not a dict")
            continue

        # Validate required fields
        ftype = fm.get("type", "")
        if ftype not in ("source", "concept"):
            errors.append(f"[WARNING] {fpath}: Missing/invalid type '{ftype}' — skipped")
            continue

        main_tag = fm.get("main_tag", "")
        sub_tags_raw = fm.get("sub_tags", [])
        topic = fm.get("topic", "")

        if not main_tag:
            errors.append(f"[ERROR] {fpath}: Missing main_tag — skipped")
            continue
        if not topic:
            errors.append(f"[ERROR] {fpath}: Missing topic — skipped")
            continue

        if isinstance(sub_tags_raw, str):
            sub_tags_raw = [sub_tags_raw]
        elif not isinstance(sub_tags_raw, list):
            sub_tags_raw = []

        # Validate tags
        has_invalid = False
        if main_tag not in main_tags and main_tag not in sub_tags:
            # Note: some tags appear in both pools (ai, system, health)
            allowed_all = main_tags | sub_tags
            if main_tag not in allowed_all:
                invalid_tags_found.append(f"[INVALID TAG] {fpath}: main_tag=#{main_tag} (not in TAGS.md)")
                has_invalid = True

        valid_subs = []
        for stag in sub_tags_raw:
            if stag in sub_tags:
                valid_subs.append(stag)
            elif stag in main_tags:
                # sub-tag that happens to also be a main-tag name is allowed if it's in Pool B
                # Actually check if it's explicitly in sub_tags set
                if stag in sub_tags:
                    valid_subs.append(stag)
                else:
                    invalid_tags_found.append(f"[INVALID TAG] {fpath}: sub_tag=#{stag} (not in Pool B of TAGS.md)")
            else:
                invalid_tags_found.append(f"[INVALID TAG] {fpath}: sub_tag=#{stag} (not in TAGS.md)")

        slug = fname.replace(".md", "")

        files.append({
            "path": fpath,
            "type": ftype,
            "main_tag": main_tag,
            "sub_tags": valid_subs,
            "topic": topic,
            "slug": slug,
        })

print(f"\n[SCAN] Found {len(files)} valid files ({sum(1 for f in files if f['type']=='concept')} concepts + {sum(1 for f in files if f['type']=='source')} sources)")
if errors:
    print(f"[SCAN] {len(errors)} files skipped with errors:")
    for e in errors:
        print(f"  {e}")
if invalid_tags_found:
    print(f"[SCAN] {len(invalid_tags_found)} invalid tags found:")
    for it in invalid_tags_found:
        print(f"  {it}")

# ── Build tag index ───────────────────────────────────────────────
tag_index = defaultdict(lambda: {"concepts": [], "sources": []})

for fobj in files:
    all_tags = [fobj["main_tag"]] + fobj["sub_tags"]
    for tag in all_tags:
        bucket = "concepts" if fobj["type"] == "concept" else "sources"
        tag_index[tag][bucket].append(fobj)

# Sort within each tag
for tag in tag_index:
    for bucket in ("concepts", "sources"):
        tag_index[tag][bucket].sort(key=lambda x: x["slug"])

# ── Co-occurrence ─────────────────────────────────────────────────
co_occur = defaultdict(set)
for fobj in files:
    all_tags = [fobj["main_tag"]] + fobj["sub_tags"]
    for i, t1 in enumerate(all_tags):
        for t2 in all_tags[i+1:]:
            pair = tuple(sorted([t1, t2]))
            co_occur[pair].add(fobj["slug"])

# Build per-tag co-occurrence lists
tag_co_occur = {}
for tag in tag_index:
    pairs = []
    for (t1, t2), slugs in co_occur.items():
        if tag == t1:
            pairs.append((t2, len(slugs)))
        elif tag == t2:
            pairs.append((t1, len(slugs)))
    pairs.sort(key=lambda x: -x[1])
    tag_co_occur[tag] = pairs[:5]

# ── Topic index ───────────────────────────────────────────────────
topic_index = defaultdict(lambda: {"concepts": [], "sources": []})
for fobj in files:
    bucket = "concepts" if fobj["type"] == "concept" else "sources"
    topic_index[fobj["topic"]][bucket].append(fobj)

# Sort within each topic
for topic in topic_index:
    for bucket in ("concepts", "sources"):
        topic_index[topic][bucket].sort(key=lambda x: x["slug"])

# Topic overlap (topics sharing files)
topic_overlap = {}
for topic, data in topic_index.items():
    all_slugs = set(f["slug"] for f in data["concepts"] + data["sources"])
    overlap_pairs = []
    for other_topic, other_data in topic_index.items():
        if other_topic == topic:
            continue
        other_slugs = set(f["slug"] for f in other_data["concepts"] + other_data["sources"])
        shared = all_slugs & other_slugs
        if shared:
            overlap_pairs.append((other_topic, len(shared)))
    overlap_pairs.sort(key=lambda x: -x[1])
    topic_overlap[topic] = overlap_pairs[:5]

# ── Write tag indexes ─────────────────────────────────────────────
tag_dir = os.path.join(KB, "wiki/tag")
os.makedirs(tag_dir, exist_ok=True)

all_valid_tags = main_tags | sub_tags
tags_written = 0
for tag in sorted(tag_index):
    if tag not in all_valid_tags:
        print(f"[SKIP] Tag #{tag} not in TAGS.md — skipping index creation")
        continue
    data = tag_index[tag]
    concepts = data["concepts"]
    sources = data["sources"]
    co_tags = tag_co_occur.get(tag, [])

    today = NOW.split(" ")[0]
    lines = []
    lines.append("---")
    lines.append("type: index")
    lines.append("level: 3")
    lines.append("scope: tag")
    lines.append('parent: "[[tag]]"')
    lines.append(f"tag: {tag}")
    lines.append("auto_generated: true")
    lines.append(f"last_updated: {today}")
    lines.append("---")
    lines.append("")
    lines.append(f"# Tag: #{tag}")
    lines.append("")
    lines.append(f"Auto-generated index of all content tagged with `#{tag}`.")
    lines.append("")
    lines.append(f"Last updated: {NOW}")
    lines.append("")
    lines.append("---")
    lines.append("")

    if concepts:
        lines.append(f"## Concepts ({len(concepts)})")
        lines.append("")
        for fobj in concepts:
            main = f"#{fobj['main_tag']}"
            sub = ", ".join(f"#{s}" for s in fobj['sub_tags']) if fobj['sub_tags'] else "none"
            lines.append(f"- [[{fobj['slug']}]] — main: {main}, sub: [{sub}], topic: {fobj['topic']}")
        lines.append("")

    if sources:
        lines.append(f"## Sources ({len(sources)})")
        lines.append("")
        for fobj in sources:
            main = f"#{fobj['main_tag']}"
            sub = ", ".join(f"#{s}" for s in fobj['sub_tags']) if fobj['sub_tags'] else "none"
            lines.append(f"- [[{fobj['slug']}]] — main: {main}, sub: [{sub}], topic: {fobj['topic']}")
        lines.append("")

    if co_tags:
        lines.append("## Co-occurring tags")
        lines.append("")
        lines.append(f"Tags that frequently appear with `#{tag}`:")
        for other_tag, count in co_tags:
            lines.append(f"- `#{other_tag}` ({count} files)")
        lines.append("")

    content = "\n".join(lines)
    fpath = os.path.join(tag_dir, f"{tag}.md")
    with open(fpath, "w") as f:
        f.write(content)
    tags_written += 1

print(f"\n[TAG INDEX] Written {tags_written} tag index files")

# ── Write topic indexes ───────────────────────────────────────────
topic_dir = os.path.join(KB, "wiki/topic")
os.makedirs(topic_dir, exist_ok=True)

topics_written = 0
for topic in sorted(topic_index):
    data = topic_index[topic]
    concepts = data["concepts"]
    sources = data["sources"]
    related = topic_overlap.get(topic, [])

    today = NOW.split(" ")[0]
    lines = []
    lines.append("---")
    lines.append("type: index")
    lines.append("scope: topic")
    lines.append('parent: "[[topic]]"')
    lines.append(f"topic: {topic}")
    lines.append("auto_generated: true")
    lines.append(f"last_updated: {today}")
    lines.append("---")
    lines.append("")
    lines.append(f"# Topic: {topic}")
    lines.append("")
    lines.append(f"Auto-generated index of all content with topic `{topic}`.")
    lines.append("")
    lines.append(f"Last updated: {NOW}")
    lines.append("")
    lines.append("---")
    lines.append("")

    if concepts:
        lines.append(f"## Concepts ({len(concepts)})")
        lines.append("")
        for fobj in concepts:
            main = f"#{fobj['main_tag']}"
            sub = ", ".join(f"#{s}" for s in fobj['sub_tags']) if fobj['sub_tags'] else "none"
            lines.append(f"- [[{fobj['slug']}]] — main: {main}, sub: [{sub}]")
        lines.append("")

    if sources:
        lines.append(f"## Sources ({len(sources)})")
        lines.append("")
        for fobj in sources:
            main = f"#{fobj['main_tag']}"
            sub = ", ".join(f"#{s}" for s in fobj['sub_tags']) if fobj['sub_tags'] else "none"
            lines.append(f"- [[{fobj['slug']}]] — main: {main}, sub: [{sub}]")
        lines.append("")

    if related:
        lines.append("## Related topics")
        lines.append("")
        lines.append(f"Topics that share concepts/sources with `{topic}`:")
        for other_topic, count in related:
            lines.append(f"- `{other_topic}` ({count} shared files)")
        lines.append("")

    content = "\n".join(lines)
    fpath = os.path.join(topic_dir, f"{topic}.md")
    with open(fpath, "w") as f:
        f.write(content)
    topics_written += 1

print(f"[TOPIC INDEX] Written {topics_written} topic index files")

# ── Cleanup orphaned index files ─────────────────────────────────
# Tag orphans
orphans_deleted = 0
for fname in os.listdir(tag_dir):
    if not fname.endswith(".md"):
        continue
    tag = fname.replace(".md", "")
    if tag not in tag_index or tag not in all_valid_tags:
        os.remove(os.path.join(tag_dir, fname))
        print(f"[ORPHAN] Deleted orphaned tag index: wiki/tag/{fname}")
        orphans_deleted += 1

# Topic orphans
for fname in os.listdir(topic_dir):
    if not fname.endswith(".md"):
        continue
    topic = fname.replace(".md", "")
    if topic not in topic_index:
        os.remove(os.path.join(topic_dir, fname))
        print(f"[ORPHAN] Deleted orphaned topic index: wiki/topic/{fname}")
        orphans_deleted += 1

print(f"\n[ORPHAN] Cleaned up {orphans_deleted} orphaned index files")

# ── Summary ───────────────────────────────────────────────────────
print(f"\n{'='*60}")
print(f"INDEX COMPLETE — {NOW}")
print(f"{'='*60}")
print(f"  Scanned: {len(files)} files ({sum(1 for f in files if f['type']=='concept')} concepts + {sum(1 for f in files if f['type']=='source')} sources)")
print(f"  Tags indexed: {tags_written}")
print(f"  Topics indexed: {topics_written}")
print(f"  Orphans deleted: {orphans_deleted}")
if errors:
    print(f"  Errors: {len(errors)}")
for e in errors:
    print(f"    {e}")
if invalid_tags_found:
    print(f"  Invalid tags flagged: {len(invalid_tags_found)}")
print(f"{'='*60}")

# Build MEMORY.md log entry
memory_log = f"""
## {NOW} +07:00 — Indexed
- Scanned: {sum(1 for f in files if f['type']=='concept')} concepts + {sum(1 for f in files if f['type']=='source')} sources = {len(files)} total
- Tags indexed: {tags_written} ({len(main_tags)} main-tags + {len(sub_tags)} sub-tags in taxonomy)
- Topics indexed: {topics_written}
- Orphans deleted: {orphans_deleted}
- Errors: {len(errors)}
- Invalid tags flagged: {len(invalid_tags_found)}
"""
if invalid_tags_found:
    memory_log += "\n### Invalid tags\n"
    for it in invalid_tags_found:
        memory_log += f"- {it}\n"
if errors:
    memory_log += "\n### Errors\n"
    for e in errors:
        memory_log += f"- {e}\n"

# Write to MEMORY.md
memory_path = os.path.join(KB, ".openclaw", "MEMORY.md")
with open(memory_path, "a") as f:
    f.write(memory_log)

print(f"\n[MEMORY] Logged to .openclaw/MEMORY.md")
print(log_memory := memory_log.strip())
