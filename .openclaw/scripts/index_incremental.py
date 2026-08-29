#!/usr/bin/env python3
"""Incremental index rebuild for Knowledge Base V2.

Usage: python3 index_incremental.py [--full]

Incremental mode: only processes changed files (sources + concepts) and
regenerates only affected tag/topic indexes.

Full mode: scan everything, rebuild all indexes.
"""

import os
import sys
import glob
import re
import yaml
from collections import defaultdict, Counter
from datetime import datetime, timezone

KB_ROOT = "/home/julius/knowledge-base"
SOURCES_DIR = os.path.join(KB_ROOT, "wiki/sources")
CONCEPTS_DIR = os.path.join(KB_ROOT, "wiki/concepts")
TAGS_DIR = os.path.join(KB_ROOT, "wiki/tag")
TOPIC_DIR = os.path.join(KB_ROOT, "wiki/topic")
SUCCESS_FILE = os.path.join(KB_ROOT, ".openclaw/last-index-success.txt")
TAGS_MD = os.path.join(KB_ROOT, "TAGS.md")
MEMORY_MD = os.path.join(KB_ROOT, ".openclaw/MEMORY.md")

# Valid tags from TAGS.md
VALID_TAGS = [
    "ai", "crypto", "tech", "productivity", "system", "economic", "politic",
    "health", "investment",  # Pool A main-tags
    "hack", "tools", "automation", "vibecode", "research", "tutorial",
    "opinion", "news", "defi", "perpdex", "layer1", "layer2", "law",
    "coding", "psychology", "geopolitics", "strategy",  # Pool B sub-tags
]
VALID_TAGS_SET = set(VALID_TAGS)

# Pool A (main tags)
MAIN_TAGS = {"ai", "crypto", "tech", "productivity", "system", "economic", "politic", "health", "investment"}


def parse_frontmatter(filepath):
    """Parse YAML frontmatter from a markdown file."""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Match frontmatter between --- markers
    match = re.match(r"^---\s*\n(.*?)\n---\s*\n", content, re.DOTALL)
    if not match:
        return None, content

    try:
        fm = yaml.safe_load(match.group(1))
        if not isinstance(fm, dict):
            return None, content
        return fm, content
    except yaml.YAMLError:
        return None, content


def get_file_type(filepath):
    """Determine if file is source or concept."""
    rel = os.path.relpath(filepath, KB_ROOT)
    if rel.startswith("wiki/sources/"):
        return "source"
    elif rel.startswith("wiki/concepts/"):
        return "concept"
    return None


def scan_files(filepaths):
    """Scan a list of files and return parsed data."""
    results = []
    errors = []
    invalid_tags = []

    for fp in filepaths:
        if not os.path.exists(fp):
            continue
        fm, _ = parse_frontmatter(fp)
        if fm is None:
            errors.append(f"wiki/sources/... or wiki/concepts/...: Cannot parse frontmatter")
            continue

        slug = os.path.splitext(os.path.basename(fp))[0]
        file_type = get_file_type(fp)

        # Extract tags
        main_tag = fm.get("main_tag", "")
        sub_tags = fm.get("sub_tags", [])
        if isinstance(sub_tags, str):
            sub_tags = [sub_tags]
        topic = fm.get("topic", "")

        # Validate tags
        all_tags = [main_tag] + sub_tags
        for t in all_tags:
            if t and t not in VALID_TAGS_SET:
                invalid_tags.append((slug, t))

        # Filter valid tags
        valid_main = main_tag if main_tag in VALID_TAGS_SET else ""
        valid_subs = [t for t in sub_tags if t in VALID_TAGS_SET]

        title = fm.get("title", slug)

        results.append({
            "slug": slug,
            "filepath": fp,
            "type": file_type,
            "title": title,
            "main_tag": valid_main,
            "sub_tags": valid_subs,
            "topic": topic,
            "all_tags": [valid_main] + valid_subs if valid_main else valid_subs,
        })

    return results, errors, invalid_tags


def scan_all_files():
    """Scan all source and concept files."""
    source_files = sorted(glob.glob(os.path.join(SOURCES_DIR, "*.md")))
    concept_files = sorted(glob.glob(os.path.join(CONCEPTS_DIR, "*.md")))

    all_files = source_files + concept_files
    results, errors, invalid_tags = scan_files(all_files)

    return results, errors, invalid_tags, len(source_files), len(concept_files)


def scan_changed_files():
    """Scan only files changed after last success timestamp."""
    last_success = None
    if os.path.exists(SUCCESS_FILE):
        with open(SUCCESS_FILE) as f:
            ts_str = f.read().strip()
            try:
                last_success = datetime.fromisoformat(ts_str)
            except:
                pass

    if last_success is None:
        return None  # Full rebuild

    # Find changed files
    changed = []
    for d in [SOURCES_DIR, CONCEPTS_DIR]:
        if not os.path.isdir(d):
            continue
        for f in os.listdir(d):
            if not f.endswith(".md"):
                continue
            fp = os.path.join(d, f)
            mtime = datetime.fromtimestamp(os.path.getmtime(fp), tz=last_success.tzinfo)
            if mtime > last_success:
                changed.append(fp)

    return changed if changed else []


def get_all_files_by_tag(results):
    """Build tag -> list of files mapping from all files."""
    tag_map = defaultdict(list)
    for r in results:
        for t in r["all_tags"]:
            if t:
                tag_map[t].append(r)
    return tag_map


def get_all_files_by_topic(results):
    """Build topic -> list of files mapping from all files."""
    topic_map = defaultdict(list)
    for r in results:
        if r["topic"]:
            topic_map[r["topic"]].append(r)
    return topic_map


def get_cooccurrence(tag_map, tag):
    """Calculate co-occurring tags for a given tag."""
    files_for_tag = tag_map.get(tag, [])
    counter = Counter()
    for r in files_for_tag:
        for t in r["all_tags"]:
            if t and t != tag:
                counter[t] += 1
    return counter.most_common(5)


def get_related_topics(topic_map, topic):
    """Find related topics (those sharing files with the given topic)."""
    files_for_topic = topic_map.get(topic, [])
    file_slugs = {r["slug"] for r in files_for_topic}
    topic_counter = Counter()
    for t, files in topic_map.items():
        if t == topic:
            continue
        shared = file_slugs & {r["slug"] for r in files}
        if shared:
            topic_counter[t] = len(shared)
    return topic_counter.most_common(5)


def format_tag_entry(r):
    """Format a single file entry for tag index."""
    md_line = f"- [[{r['slug']}]] — {r['title']} ({r['type']}, main: #{r['main_tag']}, sub: [{', '.join(f'#{s}' for s in r['sub_tags'])}], topic: {r['topic']})"
    # Clean up empty parts
    md_line = md_line.replace("main: #, ", "").replace(", sub: []", "").replace(", topic: ", "")
    return md_line


def format_topic_concept_entry(r):
    """Format concept entry for topic index."""
    return f"- [[{r['slug']}]] — main: #{r['main_tag']}, sub: [{', '.join(f'#{s}' for s in r['sub_tags'])}]"


def format_topic_source_entry(r):
    """Format source entry for topic index."""
    return f"- [[{r['slug']}]] — main: #{r['main_tag']}, sub: [{', '.join(f'#{s}' for s in r['sub_tags'])}]"


def generate_tag_index(tag, tag_map, all_results):
    """Generate content for a tag index file."""
    files = sorted(tag_map.get(tag, []), key=lambda x: x["slug"])
    sources = [f for f in files if f["type"] == "source"]
    concepts = [f for f in files if f["type"] == "concept"]
    total = len(files)
    source_count = len(sources)
    concept_count = len(concepts)
    cooccur = get_cooccurrence(tag_map, tag)

    today = datetime.now().strftime("%Y-%m-%d")
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    lines = [
        "---",
        "type: index",
        "level: 3",
        "scope: tag",
        f'parent: "[[tag]]"',
        f"tag: {tag}",
        "auto_generated: true",
        f"last_updated: {today}",
        "---",
        "",
        f"# Tag: #{tag}",
        "",
        "Auto-generated index of all content tagged with `#{tag}`.",
        "",
        f"Last updated: {now}",
        "",
        "---",
        "",
        "## Parent",
        "",
        "- [[tag]]",
        "",
        "## Stats",
        "",
        f"- Total files: {total}",
        f"- Sources: {source_count}",
        f"- Concepts: {concept_count}",
        f"- Last updated: {today}",
        "",
        "## Files with this tag",
        "",
    ]

    for r in files:
        lines.append(format_tag_entry(r))

    lines.extend(["", "## Co-occurring tags", ""])
    if cooccur:
        lines.append("Tags that frequently appear with `#{tag}`:")
        lines.append("")
        for ct, count in cooccur:
            lines.append(f"- `#{ct}` ({count} files)")
    else:
        lines.append("No co-occurring tags.")

    return "\n".join(lines) + "\n"


def generate_topic_index(topic, topic_map, all_results):
    """Generate content for a topic index file."""
    files = sorted(topic_map.get(topic, []), key=lambda x: x["slug"])
    sources = [f for f in files if f["type"] == "source"]
    concepts = [f for f in files if f["type"] == "concept"]

    today = datetime.now().strftime("%Y-%m-%d")
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    related = get_related_topics(topic_map, topic)

    lines = [
        "---",
        "type: index",
        "scope: topic",
        f'parent: "[[topic]]"',
        f"topic: {topic}",
        "auto_generated: true",
        f"last_updated: {today}",
        "---",
        "",
        f"# Topic: {topic}",
        "",
        "Auto-generated index of all content with topic `{topic}`.",
        "",
        f"Last updated: {now}",
        "",
        "---",
        "",
        f"## Concepts ({len(concepts)})",
        "",
    ]

    for r in concepts:
        lines.append(format_topic_concept_entry(r))

    lines.extend(["", f"## Sources ({len(sources)})", ""])
    for r in sources:
        lines.append(format_topic_source_entry(r))

    lines.extend(["", "## Related topics", ""])
    if related:
        lines.append("Topics that share concepts/sources with `{topic}`:")
        lines.append("")
        for rt, count in related:
            lines.append(f"- `{rt}` ({count} shared files)")
    else:
        lines.append("No related topics.")

    return "\n".join(lines) + "\n"


def generate_tag_master_index(tag_map):
    """Generate wiki/tag/tag.md master index."""
    all_tags = sorted(tag_map.keys(), key=lambda t: (t not in MAIN_TAGS, t))
    main_tags = sorted(t for t in all_tags if t in MAIN_TAGS)
    sub_tags = sorted(t for t in all_tags if t not in MAIN_TAGS)

    total = len(all_tags)
    main_count = len(main_tags)
    sub_count = len(sub_tags)

    # Most used tags
    usage = [(t, len(files)) for t, files in tag_map.items()]
    usage.sort(key=lambda x: -x[1])
    top3 = usage[:3]

    today = datetime.now().strftime("%Y-%m-%d")
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Tag descriptions from TAGS.md
    tag_descriptions = {
        "ai": "AI / ML / LLM",
        "crypto": "Blockchain, DeFi",
        "tech": "Software engineering",
        "productivity": "Workflows, KM",
        "system": "System design",
        "economic": "Macroeconomics",
        "politic": "Policy, regulation",
        "health": "Physical health, biohacking",
        "investment": "Investment principles, portfolio management",
        "hack": "Exploits, vulnerabilities",
        "tools": "Software, products",
        "automation": "Bots, scripts",
        "vibecode": "AI-assisted dev",
        "research": "Academic papers",
        "tutorial": "How-to guides",
        "opinion": "Personal takes",
        "news": "Recent events",
        "defi": "DeFi protocols",
        "perpdex": "Perpetual DEXs",
        "layer1": "Base blockchains",
        "layer2": "Scaling solutions",
        "law": "Legal frameworks, contracts",
        "coding": "Programming, software development",
        "psychology": "Cognitive science, behavioral psychology",
        "geopolitics": "Geopolitical analysis, international relations",
        "strategy": "Strategic thinking, decision frameworks",
    }

    lines = [
        "---",
        "type: index",
        "level: 2",
        "scope: tags",
        f'parent: "[[wiki]]"',
        "auto_generated: false",
        "items_managed_by: index-agent",
        f"last_updated: {today}",
        "---",
        "",
        "# Tags Index",
        "",
        "## Overview",
        "",
        "Master index of all tags used across the wiki. Each entry links to a tag file (`wiki/tag/<tag>.md`) listing all files with that tag.",
        "",
        "## Parent",
        "",
        "- [[wiki]]",
        "",
        "## Stats",
        "",
        f"- Total tags: {total}",
        f"- Main tags: {main_count}",
        f"- Sub tags: {sub_count}",
        f"- Most used: #{top3[0][0]} ({top3[0][1]}), #{top3[1][0]} ({top3[1][1]}), #{top3[2][0]} ({top3[2][1]})",
        f"- Last updated: {today}",
        "",
        "## Items",
        "",
        "### Main Tags (Pool A)",
        "",
    ]

    for t in main_tags:
        desc = tag_descriptions.get(t, "")
        lines.append(f"- [[{t}]] — {desc}")

    lines.extend(["", "### Sub Tags (Pool B)", ""])
    for t in sub_tags:
        desc = tag_descriptions.get(t, "")
        lines.append(f"- [[{t}]] — {desc}")

    lines.extend(["", "## Notes", "", "<!-- Free space for Julius -->", ""])
    return "\n".join(lines) + "\n"


def get_all_topics(topic_map):
    """Generate all topic index files."""
    return sorted(topic_map.keys())


def write_index(filepath, content):
    """Write index file, creating parent directories if needed."""
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)


def cleanup_orphans(tag_map, topic_map):
    """Delete orphaned index files (tags/topics no longer in use)."""
    orphans = []
    valid_tags = set(tag_map.keys())
    valid_topics = set(topic_map.keys())

    # Check tag files
    if os.path.isdir(TAGS_DIR):
        for f in os.listdir(TAGS_DIR):
            if not f.endswith(".md"):
                continue
            tag = f[:-3]  # Remove .md
            if tag == "tag":
                continue  # Skip master index
            if tag not in valid_tags:
                orphan_path = os.path.join(TAGS_DIR, f)
                orphans.append(orphan_path)

    # Check topic files
    if os.path.isdir(TOPIC_DIR):
        for f in os.listdir(TOPIC_DIR):
            if not f.endswith(".md"):
                continue
            topic = f[:-3]
            if topic not in valid_topics:
                orphan_path = os.path.join(TOPIC_DIR, f)
                orphans.append(orphan_path)

    # Delete orphans
    for path in orphans:
        os.remove(path)

    return orphans


def append_to_memory(log_entry):
    """Append log entry to MEMORY.md."""
    os.makedirs(os.path.dirname(MEMORY_MD), exist_ok=True)
    if os.path.exists(MEMORY_MD):
        with open(MEMORY_MD, "a", encoding="utf-8") as f:
            f.write("\n"