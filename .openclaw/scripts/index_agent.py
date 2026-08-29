#!/usr/bin/env python3
"""Index Agent: Scan wiki/sources and wiki/concepts, rebuild tag/topic indexes."""

import os
import re
import yaml
import glob
import sys
from datetime import datetime, timezone

KB = "/home/julius/knowledge-base"
TAGS_FILE = os.path.join(KB, "TAGS.md")
SOURCES_DIR = os.path.join(KB, "wiki/sources")
CONCEPTS_DIR = os.path.join(KB, "wiki/concepts")
TAG_DIR = os.path.join(KB, "wiki/tag")
TOPIC_DIR = os.path.join(KB, "wiki/topic")
MEMORY_FILE = os.path.join(KB, ".openclaw/MEMORY.md")
SUCCESS_FILE = os.path.join(KB, ".openclaw/last-index-success.txt")

NOW = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")
TODAY = datetime.now(timezone.utc).strftime("%Y-%m-%d")

# --- Load TAGS.md ---
def load_tags():
    main_tags = set()
    sub_tags = set()
    current_pool = None
    with open(TAGS_FILE, "r") as f:
        for line in f:
            m = re.match(r'^\| `#([^`]+)`', line)
            if m:
                tag = m.group(1)
                if current_pool == "A":
                    main_tags.add(tag)
                elif current_pool == "B":
                    sub_tags.add(tag)
            if "Pool A — Main-tags" in line:
                current_pool = "A"
            elif "Pool B — Sub-tags" in line:
                current_pool = "B"
    return main_tags, sub_tags

# --- Parse frontmatter ---
def parse_frontmatter(filepath):
    with open(filepath, "r") as f:
        content = f.read()
    # match YAML frontmatter between ---
    m = re.match(r'^---\s*\n(.*?)\n---', content, re.DOTALL)
    if not m:
        return None, None
    try:
        fm = yaml.safe_load(m.group(1))
    except yaml.YAMLError:
        return None, None
    if not isinstance(fm, dict):
        return None, None
    return fm, filepath

# --- Scan files ---
def scan_files(directory, file_type):
    results = []
    errors = []
    for fpath in sorted(glob.glob(os.path.join(directory, "*.md"))):
        slug = os.path.splitext(os.path.basename(fpath))[0]
        fm, _ = parse_frontmatter(fpath)
        if fm is None:
            errors.append(f"[FRONTMATTER ERROR] {file_type}/{slug} — Cannot parse YAML frontmatter")
            continue
        results.append((slug, fm, file_type))
    return results, errors

# --- Main ---
def main():
    main_tags, sub_tags = load_tags()
    valid_tags = main_tags | sub_tags
    valid_tags.discard("")  # remove empty if present

    # Scan sources
    sources, src_errors = scan_files(SOURCES_DIR, "source")
    # Scan concepts
    concepts, con_errors = scan_files(CONCEPTS_DIR, "concept")

    all_files = sources + concepts
    errors = src_errors + con_errors

    # Extract tags per file
    file_tags = {}  # slug -> {tags: set, main: str, subs: list, topic: str, title: str, ftype: str}
    invalid_tags_found = []
    co_occurrence = {}
    tag_to_files = {}  # tag -> list of (slug, title, ftype, main, subs, topic)
    topic_to_files = {}  # topic -> list of (slug, title, ftype, main, subs)

    for slug, fm, ftype in all_files:
        main_t = fm.get("main_tag", "")
        subs = fm.get("sub_tags", [])
        if isinstance(subs, str):
            subs = [subs]
        topic = fm.get("topic", "")
        title = fm.get("title", slug)

        all_tags = set()
        if main_t:
            all_tags.add(main_t)
        for s in subs:
            if s:
                all_tags.add(s)

        # Check validity
        tags_to_skip = set()
        for t in all_tags:
            if t not in valid_tags:
                invalid_tags_found.append(f"[INVALID TAG] Tag #{t} in {ftype}/{slug} — not in TAGS.md")
                tags_to_skip.add(t)

        # Only use valid tags
        valid_file_tags = all_tags - tags_to_skip
        if main_t and main_t not in tags_to_skip:
            fm_main = main_t
        else:
            fm_main = main_t

        file_tags[slug] = {
            "tags": valid_file_tags,
            "main": fm_main,
            "subs": [s for s in subs if s in valid_tags],
            "topic": topic,
            "title": title,
            "ftype": ftype,
        }

        # Update co-occurrence counts
        tag_list = sorted(valid_file_tags)
        for i, t1 in enumerate(tag_list):
            if t1 not in co_occurrence:
                co_occurrence[t1] = {}
            for t2 in tag_list:
                if t1 == t2:
                    continue
                co_occurrence[t1][t2] = co_occurrence[t1].get(t2, 0) + 1

        # Tag -> files
        for t in valid_file_tags:
            if t not in tag_to_files:
                tag_to_files[t] = []
            tag_to_files[t].append((slug, title, ftype, fm_main, [s for s in subs if s in valid_tags], topic))

        # Topic -> files
        if topic:
            if topic not in topic_to_files:
                topic_to_files[topic] = []
            topic_to_files[topic].append((slug, title, ftype, fm_main, [s for s in subs if s in valid_tags]))

    # --- Write tag index files ---
    os.makedirs(TAG_DIR, exist_ok=True)
    tags_written = 0
    for tag in sorted(tag_to_files.keys()):
        entries = tag_to_files[tag]
        tag_concepts_list = [e for e in entries if e[2] == "concept"]
        tag_sources_list = [e for e in entries if e[2] == "source"]
        # Sort alphabetically
        tag_concepts_list.sort(key=lambda x: x[0])
        tag_sources_list.sort(key=lambda x: x[0])
        all_entries = sorted(entries, key=lambda x: x[0])

        # Co-occurrence top 5
        co_tags = sorted(co_occurrence.get(tag, {}).items(), key=lambda x: -x[1])[:5]

        content = f"""---
type: index
level: 3
scope: tag
parent: [[tag]]
tag: {tag}
auto_generated: true
last_updated: {TODAY}
---

# Tag: #{tag}

Auto-generated index of all content tagged with `#{tag}`.

Last updated: {NOW}

---

## Parent

- [[tag]]

## Stats

- Total files: {len(all_entries)}
- Sources: {len(tag_sources_list)}
- Concepts: {len(tag_concepts_list)}
- Last updated: {TODAY}

## Files with this tag

"""
        for slug, title, ftype, main, subs, topic in all_entries:
            sub_str = ", ".join(f"#{s}" for s in subs) if subs else ""
            topic_str = f"topic: {topic}" if topic else ""
            parts = [f"({ftype}, main: #{main}"]
            if sub_str:
                parts.append(f"sub: [{sub_str}]")
            if topic_str:
                parts.append(topic_str)
            parts_str = ", ".join(parts) + ")"
            content += f"- [[{slug}]] — {title} {parts_str}\n"

        content += f"""
## Co-occurring tags

Tags that frequently appear with `#{tag}`:
"""
        if co_tags:
            for ct, count in co_tags:
                content += f"- `#{ct}` ({count} files)\n"
        else:
            content += "- None\n"

        fpath = os.path.join(TAG_DIR, f"{tag}.md")
        with open(fpath, "w") as f:
            f.write(content.lstrip())
        tags_written += 1

    # --- Write topic index files ---
    os.makedirs(TOPIC_DIR, exist_ok=True)
    topics_written = 0
    for topic in sorted(topic_to_files.keys()):
        entries = topic_to_files[topic]
        topic_concepts = [e for e in entries if e[2] == "concept"]
        topic_sources = [e for e in entries if e[2] == "source"]
        topic_concepts.sort(key=lambda x: x[0])
        topic_sources.sort(key=lambda x: x[0])

        # Find topics that share files
        # Count shared files between topics
        topic_shares = {}
        all_slugs_in_this_topic = {e[0] for e in entries}
        for other_topic, other_entries in topic_to_files.items():
            if other_topic == topic:
                continue
            other_slugs = {e[0] for e in other_entries}
            shared = all_slugs_in_this_topic & other_slugs
            if shared:
                topic_shares[other_topic] = len(shared)

        top_related = sorted(topic_shares.items(), key=lambda x: -x[1])[:5]

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

Last updated: {NOW}

---

## Concepts ({len(topic_concepts)})

"""
        for slug, title, ftype, main, subs in topic_concepts:
            sub_str = ", ".join(f"#{s}" for s in subs) if subs else ""
            subs_part = f"sub: [{sub_str}]" if sub_str else ""
            parts = [f"main: #{main}"]
            if subs_part:
                parts.append(subs_part)
            content += f"- [[{slug}]] — {', '.join(parts)}\n"

        content += f"""
## Sources ({len(topic_sources)})

"""
        for slug, title, ftype, main, subs in topic_sources:
            sub_str = ", ".join(f"#{s}" for s in subs) if subs else ""
            subs_part = f"sub: [{sub_str}]" if sub_str else ""
            parts = [f"main: #{main}"]
            if subs_part:
                parts.append(subs_part)
            content += f"- [[{slug}]] — {', '.join(parts)}\n"

        content += f"""
## Related topics

Topics that share concepts/sources with `{topic}`:
"""
        if top_related:
            for rt, count in top_related:
                content += f"- {rt} ({count} shared files)\n"
        else:
            content += "- None\n"

        fpath = os.path.join(TOPIC_DIR, f"{topic}.md")
        with open(fpath, "w") as f:
            f.write(content.lstrip())
        topics_written += 1

    # --- Orphan cleanup ---
    orphans_deleted = 0
    # Check tag files
    for fpath in glob.glob(os.path.join(TAG_DIR, "*.md")):
        slug = os.path.splitext(os.path.basename(fpath))[0]
        if slug == "tag":
            continue  # skip master tag.md
        if slug not in tag_to_files:
            os.remove(fpath)
            errors.append(f"[ORPHAN DELETED] wiki/tag/{slug}.md — no files use this tag")
            orphans_deleted += 1

    # Check topic files
    for fpath in glob.glob(os.path.join(TOPIC_DIR, "*.md")):
        slug = os.path.splitext(os.path.basename(fpath))[0]
        if slug not in topic_to_files:
            os.remove(fpath)
            errors.append(f"[ORPHAN DELETED] wiki/topic/{slug}.md — no files use this topic")
            orphans_deleted += 1

    # --- Count used tags ---
    used_main = main_tags & tag_to_files.keys()
    used_sub = sub_tags & tag_to_files.keys()

    # Prepare summary
    total_sources = len(sources)
    total_concepts = len(concepts)
    total_tags = len(tag_to_files)
    total_topics = len(topic_to_files)
    main_used = len(used_main)
    sub_used = len(used_sub)

    report = f"""
## {TODAY} 21:07 — Indexed

- Scanned: {total_concepts} concepts + {total_sources} sources
- Tags indexed: {total_tags} ({main_used} main-tags + {sub_used} sub-tags)
- Topics indexed: {total_topics}
- Orphans deleted: {orphans_deleted}
- Errors: {len(invalid_tags_found) + len([e for e in errors if e.startswith('[FRONTMATTER ERROR]')])}"""

    if errors:
        report += "\n\n### Details\n"
        for e in errors:
            report += f"- {e}\n"
    if invalid_tags_found:
        for e in invalid_tags_found:
            report += f"- {e}\n"

    # Write success timestamp
    now_iso = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S+0700")
    with open(SUCCESS_FILE, "w") as f:
        f.write(now_iso + "\n")

    # Print report for stdout
    print(f"SCANNED: {total_concepts} concepts + {total_sources} sources")
    print(f"TAGS: {total_tags} ({main_used} main + {sub_used} sub)")
    print(f"TOPICS: {total_topics}")
    print(f"ORPHANS: {orphans_deleted}")
    print(f"INVALID: {len(invalid_tags_found)}")
    print(f"FM_ERRORS: {len([e for e in errors if e.startswith('[FRONTMATTER ERROR]')])}")
    print(f"REPORT:\n{report}")

if __name__ == "__main__":
    main()