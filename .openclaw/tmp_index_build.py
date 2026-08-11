#!/usr/bin/env python3
"""Index Agent — Full rebuild of tag and topic indexes."""
import os, sys, yaml, glob, re, json
from datetime import datetime, timezone
from collections import defaultdict

KB = "/home/julius/knowledge-base"
NOW = datetime.now(timezone.utc)
TODAY = NOW.strftime("%Y-%m-%d")
NOW_ISO = NOW.isoformat()

# ─── Load TAGS.md taxonomy ───
def parse_tags_md():
    main_tags = []
    sub_tags = []
    in_main = False
    in_sub = False
    with open(f"{KB}/TAGS.md") as f:
        for line in f:
            if line.startswith("## 2. Pool A"):
                in_main = True
                in_sub = False
                continue
            if line.startswith("## 3. Pool B"):
                in_main = False
                in_sub = True
                continue
            if line.startswith("## ") and (in_main or in_sub):
                break
            if in_main and line.startswith("| `#"):
                tag = line.split("`#")[1].split("`")[0].strip()
                main_tags.append(tag)
            if in_sub and line.startswith("| `#"):
                tag = line.split("`#")[1].split("`")[0].strip()
                sub_tags.append(tag)
    return main_tags, sub_tags

MAIN_TAGS, SUB_TAGS = parse_tags_md()
ALLOWED_TAGS = set(MAIN_TAGS + SUB_TAGS)
print(f"TAGS.md loaded: {len(MAIN_TAGS)} main-tags, {len(SUB_TAGS)} sub-tags")

# ─── Scan all wiki files and extract frontmatter ───
def extract_frontmatter(filepath):
    """Extract YAML frontmatter from a markdown file. Returns dict or None."""
    try:
        with open(filepath) as f:
            content = f.read()
        if not content.startswith("---"):
            return None
        parts = content.split("---", 2)
        if len(parts) < 3:
            return None
        fm = yaml.safe_load(parts[1])
        return fm if isinstance(fm, dict) else None
    except Exception as e:
        return None

files_data = []
warnings = []
errors = []
invalid_tags_found = []

concept_files = glob.glob(f"{KB}/wiki/concepts/*.md")
source_files = glob.glob(f"{KB}/wiki/sources/*.md")
all_files = sorted(concept_files + source_files)

print(f"Scanning {len(all_files)} files...")

for fpath in all_files:
    fm = extract_frontmatter(fpath)
    if fm is None:
        warnings.append(f"[WARNING] {fpath}: No frontmatter found, skipped")
        continue
    
    ftype = fm.get("type", "")
    if ftype not in ("source", "concept"):
        errors.append(f"[ERROR] {fpath}: type={ftype}, expected source or concept")
        continue
    
    main_tag = fm.get("main_tag", "")
    sub_tags = fm.get("sub_tags", [])
    topic = fm.get("topic", "")
    
    if not main_tag:
        errors.append(f"[ERROR] {fpath}: missing main_tag")
        continue
    if not topic:
        errors.append(f"[ERROR] {fpath}: missing topic")
        continue
    
    # Validate main_tag
    invalid_main = False
    if main_tag not in MAIN_TAGS:
        invalid_tags_found.append(f"[INVALID TAG] {fpath}: main_tag={main_tag}")
        invalid_main = True
    
    # Validate sub_tags
    invalid_subs = []
    valid_subs = []
    for t in sub_tags:
        if t not in SUB_TAGS:
            invalid_tags_found.append(f"[INVALID TAG] {fpath}: sub_tag={t}")
            invalid_subs.append(t)
        else:
            valid_subs.append(t)
    
    # Derive slug from filename
    slug = os.path.basename(fpath).replace(".md", "")
    
    files_data.append({
        "path": fpath,
        "type": ftype,
        "slug": slug,
        "main_tag": main_tag,
        "sub_tags": valid_subs,
        "topic": topic,
        "invalid_main": invalid_main,
        "invalid_subs": invalid_subs,
    })

print(f"Parsed: {len(files_data)} files")
print(f"Warnings: {len(warnings)}")
print(f"Errors: {len(errors)}")
print(f"Invalid tags: {len(invalid_tags_found)}")

# ─── Build tag → files mapping ───
tag_index = defaultdict(lambda: {"concepts": [], "sources": []})

for f in files_data:
    # Add to main_tag index
    if not f["invalid_main"]:
        tag_index[f["main_tag"]][f["type"] + "s"].append(f)
    
    # Add to sub_tags indexes
    for tag in f["sub_tags"]:
        tag_index[tag][f["type"] + "s"].append(f)

# Sort within each tag
for tag in tag_index:
    tag_index[tag]["concepts"].sort(key=lambda x: x["slug"])
    tag_index[tag]["sources"].sort(key=lambda x: x["slug"])

print(f"Tags indexed: {len(tag_index)}")

# ─── Calculate co-occurrence ───
co_occurrence = defaultdict(int)

for f in files_data:
    file_tags = [f["main_tag"]] + f["sub_tags"]
    # Filter invalid
    file_tags = [t for t in file_tags if t in ALLOWED_TAGS or t == f["main_tag"]]
    for i, t1 in enumerate(file_tags):
        for t2 in file_tags[i+1:]:
            pair = tuple(sorted([t1, t2]))
            co_occurrence[pair] += 1

# Build per-tag co-occurrence lists
tag_co_occur = {}
for tag in tag_index:
    pairs = []
    for other_tag in tag_index:
        if other_tag == tag:
            continue
        pair = tuple(sorted([tag, other_tag]))
        count = co_occurrence.get(pair, 0)
        if count > 0:
            pairs.append((other_tag, count))
    pairs.sort(key=lambda x: -x[1])
    tag_co_occur[tag] = pairs[:5]

# ─── Build topic → files mapping ───
topic_index = defaultdict(lambda: {"concepts": [], "sources": []})

for f in files_data:
    topic_index[f["topic"]][f["type"] + "s"].append(f)

for topic in topic_index:
    topic_index[topic]["concepts"].sort(key=lambda x: x["slug"])
    topic_index[topic]["sources"].sort(key=lambda x: x["slug"])

print(f"Topics indexed: {len(topic_index)}")

# ─── Calculate topic overlap ───
topic_overlap = defaultdict(int)
for t1 in topic_index:
    files1 = set(f["path"] for f in topic_index[t1]["concepts"] + topic_index[t1]["sources"])
    for t2 in topic_index:
        if t1 >= t2:
            continue
        files2 = set(f["path"] for f in topic_index[t2]["concepts"] + topic_index[t2]["sources"])
        shared = len(files1 & files2)
        if shared > 0:
            topic_overlap[tuple(sorted([t1, t2]))] = shared

topic_related = {}
for topic in topic_index:
    pairs = []
    for other_topic in topic_index:
        if other_topic == topic:
            continue
        pair = tuple(sorted([topic, other_topic]))
        count = topic_overlap.get(pair, 0)
        if count > 0:
            pairs.append((other_topic, count))
    pairs.sort(key=lambda x: -x[1])
    topic_related[topic] = pairs[:5]

def derive_title(slug):
    return " ".join(w.capitalize() for w in slug.replace("_", "-").split("-"))

# ─── Write tag index files ───
os.makedirs(f"{KB}/wiki/tag", exist_ok=True)

for tag in tag_index:
    data = tag_index[tag]
    co_occur = tag_co_occur.get(tag, [])
    total = len(data["concepts"]) + len(data["sources"])
    
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

Auto-generated index of all content tagged with `#{tag}`.

Last updated: {TODAY} {NOW.strftime("%H:%M:%S")}

---

## Stats

- Total files: {total}
- Sources: {len(data["sources"])}
- Concepts: {len(data["concepts"])}
- Last updated: {TODAY}

## Concepts ({len(data["concepts"])})

"""
    for f in data["concepts"]:
        title = derive_title(f["slug"])
        main = f["main_tag"]
        subs = ", ".join([f"#{s}" for s in f["sub_tags"]])
        content += f"- [[{f['slug']}]] — {title} (concept, main: #{main}, sub: [{subs}], topic: {f['topic']})\n"
    
    content += f"\n## Sources ({len(data['sources'])})\n\n"
    for f in data["sources"]:
        title = derive_title(f["slug"].replace("src_", ""))
        main = f["main_tag"]
        subs = ", ".join([f"#{s}" for s in f["sub_tags"]])
        content += f"- [[{f['slug']}]] — {title} (source, main: #{main}, sub: [{subs}], topic: {f['topic']})\n"
    
    if co_occur:
        content += "\n## Co-occurring tags\n\n"
        content += "Tags that frequently appear with `#{}`:\n\n".format(tag)
        for other_tag, count in co_occur:
            unit = "co-occurrence" if count == 1 else "co-occurrences"
            content += f"- [[{other_tag}]] — {count} {unit}\n"
    
    with open(f"{KB}/wiki/tag/{tag}.md", "w") as f:
        f.write(content)

print(f"Written {len(tag_index)} tag index files")

# ─── Write topic index files ───
os.makedirs(f"{KB}/wiki/topic", exist_ok=True)

for topic in topic_index:
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

Last updated: {TODAY} {NOW.strftime("%H:%M:%S")}

---

## Concepts ({len(data['concepts'])})

"""
    for f in data["concepts"]:
        main = f["main_tag"]
        subs = ", ".join([f"#{s}" for s in f["sub_tags"]])
        content += f"- [[{f['slug']}]] — main: #{main}, sub: [{subs}]\n"
    
    content += f"\n## Sources ({len(data['sources'])})\n\n"
    for f in data["sources"]:
        main = f["main_tag"]
        subs = ", ".join([f"#{s}" for s in f["sub_tags"]])
        content += f"- [[{f['slug']}]] — main: #{main}, sub: [{subs}]\n"
    
    if related:
        content += "\n## Related topics\n\n"
        content += f"Topics that share concepts/sources with `{topic}`:\n\n"
        for other_topic, count in related:
            content += f"- `{other_topic}` ({count} shared files)\n"
    
    with open(f"{KB}/wiki/topic/{topic}.md", "w") as f:
        f.write(content)

print(f"Written {len(topic_index)} topic index files")

# ─── Clean up orphaned index files ───
orphaned_tags = []
existing_tag_files = glob.glob(f"{KB}/wiki/tag/*.md")
for tf in existing_tag_files:
    tname = os.path.basename(tf).replace(".md", "")
    if tname != "tag" and tname not in tag_index:
        orphaned_tags.append(tname)
        os.remove(tf)
        print(f"Deleted orphaned tag index: wiki/tag/{tname}.md")

orphaned_topics = []
existing_topic_files = glob.glob(f"{KB}/wiki/topic/*.md")
for tf in existing_topic_files:
    tname = os.path.basename(tf).replace(".md", "")
    if tname not in topic_index:
        orphaned_topics.append(tname)
        os.remove(tf)
        print(f"Deleted orphaned topic index: wiki/topic/{tname}.md")

print(f"Orphans: {len(orphaned_tags)} tags + {len(orphaned_topics)} topics deleted")

# ─── Update tag.md master index ───
tag_md_path = f"{KB}/wiki/tag/tag.md"

# Count tag usage
tag_counts = {}
for tag in tag_index:
    data = tag_index[tag]
    tag_counts[tag] = len(data["concepts"]) + len(data["sources"])

# Sort by usage
sorted_by_usage = sorted(tag_counts.items(), key=lambda x: -x[1])
top_3 = sorted_by_usage[:3]
most_used = ", ".join([f"#{t} ({c})" for t, c in top_3])

total_tags = len(tag_index)
main_tags_count = len([t for t in tag_index if t in MAIN_TAGS])
sub_tags_count = total_tags - main_tags_count

# Build Items section
items_lines = []
items_lines.append("## Items\n")
items_lines.append("### Main Tags (Pool A)\n")
for t in MAIN_TAGS:
    if t in tag_index:
        items_lines.append(f"- [[{t}]]\n")
    else:
        items_lines.append(f"- [[{t}]]\n")  # still list even if empty

items_lines.append("\n### Sub Tags (Pool B)\n")
for t in SUB_TAGS:
    if t in tag_index:
        items_lines.append(f"- [[{t}]]\n")
    else:
        items_lines.append(f"- [[{t}]]\n")  # still list even if empty

# Read existing tag.md
with open(tag_md_path) as f:
    tag_md_content = f.read()

# Update Stats section
new_stats = f"""## Stats

- Total tags: {total_tags}
- Main tags: {main_tags_count}
- Sub tags: {sub_tags_count}
- Most used: {most_used}
- Last updated: {TODAY}
"""

# Replace Stats section
import re
tag_md_content = re.sub(
    r"## Stats\n.*?(?=\n## Items|\Z)",
    new_stats.strip(),
    tag_md_content,
    flags=re.DOTALL
)

# Replace Items section
tag_md_content = re.sub(
    r"## Items\n.*",
    "".join(items_lines),
    tag_md_content,
    flags=re.DOTALL
)

with open(tag_md_path, "w") as f:
    f.write(tag_md_content)

print("Updated tag.md master index")

# ─── Log to MEMORY.md ───
memory_path = f"{KB}/.openclaw/MEMORY.md"
log_entry = f"""
## {NOW_ISO} — Indexed (full rebuild)

- **Scanned:** {len([f for f in files_data if f['type']=='concept'])} concepts + {len([f for f in files_data if f['type']=='source'])} sources = {len(files_data)} total files
- **Tags indexed:** {total_tags} ({main_tags_count} main-tags + {sub_tags_count} sub-tags)
- **Topics indexed:** {len(topic_index)}
- **Orphans deleted:** {len(orphaned_tags)} tag indexes + {len(orphaned_topics)} topic indexes
- **Invalid tags found:** {len(invalid_tags_found)}
- **Errors:** {len(errors)} files skipped due to invalid frontmatter
- **Mode:** full (28 files changed since last run, ≥20 threshold)
"""

if invalid_tags_found:
    log_entry += "\n### Invalid tag details\n"
    for detail in invalid_tags_found:
        log_entry += f"- {detail}\n"

if errors:
    log_entry += "\n### Error details\n"
    for detail in errors:
        log_entry += f"- {detail}\n"

if warnings:
    log_entry += "\n### Warning details\n"
    for detail in warnings:
        log_entry += f"- {detail}\n"

with open(memory_path, "a") as f:
    f.write(log_entry)

print("Logged to MEMORY.md")

# ─── Write success timestamp ───
with open(f"{KB}/.openclaw/last-index-success.txt", "w") as f:
    f.write(NOW_ISO)

print(f"Success timestamp written: {NOW_ISO}")
print("\n=== INDEX REBUILD COMPLETE ===")