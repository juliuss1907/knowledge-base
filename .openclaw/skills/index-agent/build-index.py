#!/usr/bin/env python3
"""
Index Agent - Full Rebuild Mode
Builds tag and topic indexes from wiki files.
"""

import os
import re
import yaml
from datetime import datetime
from collections import defaultdict
from pathlib import Path

# Paths
WIKI_ROOT = Path("/home/julius/knowledge-base")
TAGS_MD = WIKI_ROOT / "TAGS.md"
WIKI_SOURCES = WIKI_ROOT / "wiki" / "sources"
WIKI_CONCEPTS = WIKI_ROOT / "wiki" / "concepts"
WIKI_TAG = WIKI_ROOT / "wiki" / "tag"
WIKI_TOPIC = WIKI_ROOT / "wiki" / "topic"
MEMORY_MD = WIKI_ROOT / ".openclaw" / "MEMORY.md"

def extract_frontmatter(filepath):
    """Extract YAML frontmatter from markdown file."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find frontmatter between --- markers
        match = re.search(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
        if not match:
            return None, f"No frontmatter found"
        
        try:
            frontmatter = yaml.safe_load(match.group(1))
            return frontmatter, None
        except yaml.YAMLError as e:
            return None, f"YAML parse error: {e}"
    except Exception as e:
        return None, f"Read error: {e}"

def load_allowed_tags():
    """Parse TAGS.md to get allowed tags."""
    with open(TAGS_MD, 'r', encoding='utf-8') as f:
        content = f.read()
    
    main_tags = []
    sub_tags = []
    
    # Extract main tags (Pool A)
    in_pool_a = False
    for line in content.split('\n'):
        if 'Pool A' in line or 'Main Tags' in line:
            in_pool_a = True
        elif 'Pool B' in line or 'Sub Tags' in line:
            in_pool_a = False
        elif in_pool_a and '|' in line and '`#' in line:
            tag = re.search(r'`#([^`]+)`', line)
            if tag:
                main_tags.append(tag.group(1))
    
    # Extract sub tags (Pool B)
    in_pool_b = False
    for line in content.split('\n'):
        if 'Pool B' in line or 'Sub Tags' in line:
            in_pool_b = True
        if in_pool_b and '|' in line and '`#' in line:
            tag = re.search(r'`#([^`]+)`', line)
            if tag:
                sub_tags.append(tag.group(1))
    
    return set(main_tags), set(sub_tags)

def derive_title(slug):
    """Convert slug to human-readable title."""
    # Remove src_ prefix for sources
    clean_slug = slug.replace('src_', '')
    # Replace hyphens with spaces, title case
    return ' '.join(word.capitalize() for word in clean_slug.split('-'))

def scan_files():
    """Scan all wiki files and extract metadata."""
    files = []
    errors = []
    invalid_tags = []
    
    main_tags, sub_tags = load_allowed_tags()
    print(f"Loaded {len(main_tags)} main tags, {len(sub_tags)} sub tags")
    
    # Scan sources
    if WIKI_SOURCES.exists():
        for filepath in sorted(WIKI_SOURCES.glob('*.md')):
            fm, err = extract_frontmatter(filepath)
            if err:
                errors.append((str(filepath), err))
                continue
            
            slug = filepath.stem
            file_data = {
                'path': str(filepath.relative_to(WIKI_ROOT)),
                'slug': slug,
                'type': 'source',
                'title': derive_title(slug),
                'main_tag': fm.get('main_tag'),
                'sub_tags': fm.get('sub_tags', []),
                'topic': fm.get('topic'),
            }
            
            # Validate tags
            if file_data['main_tag'] and file_data['main_tag'] not in main_tags:
                invalid_tags.append((file_data['path'], 'main_tag', file_data['main_tag']))
            
            for tag in file_data['sub_tags']:
                if tag not in sub_tags:
                    invalid_tags.append((file_data['path'], 'sub_tag', tag))
            
            files.append(file_data)
    
    # Scan concepts
    if WIKI_CONCEPTS.exists():
        for filepath in sorted(WIKI_CONCEPTS.glob('*.md')):
            fm, err = extract_frontmatter(filepath)
            if err:
                errors.append((str(filepath), err))
                continue
            
            slug = filepath.stem
            file_data = {
                'path': str(filepath.relative_to(WIKI_ROOT)),
                'slug': slug,
                'type': 'concept',
                'title': derive_title(slug),
                'main_tag': fm.get('main_tag'),
                'sub_tags': fm.get('sub_tags', []),
                'topic': fm.get('topic'),
            }
            
            # Validate tags
            if file_data['main_tag'] and file_data['main_tag'] not in main_tags:
                invalid_tags.append((file_data['path'], 'main_tag', file_data['main_tag']))
            
            for tag in file_data['sub_tags']:
                if tag not in sub_tags:
                    invalid_tags.append((file_data['path'], 'sub_tag', tag))
            
            files.append(file_data)
    
    return files, errors, invalid_tags

def build_tag_index(files):
    """Build tag -> files mapping."""
    tag_index = defaultdict(lambda: {'concepts': [], 'sources': []})
    
    for file in files:
        main_tag = file.get('main_tag')
        sub_tags = file.get('sub_tags', [])
        
        # Add to main_tag index
        if main_tag:
            if file['type'] == 'concept':
                tag_index[main_tag]['concepts'].append(file)
            else:
                tag_index[main_tag]['sources'].append(file)
        
        # Add to sub_tags indexes
        for tag in sub_tags:
            if file['type'] == 'concept':
                tag_index[tag]['concepts'].append(file)
            else:
                tag_index[tag]['sources'].append(file)
    
    return tag_index

def build_topic_index(files):
    """Build topic -> files mapping."""
    topic_index = defaultdict(lambda: {'concepts': [], 'sources': []})
    
    for file in files:
        topic = file.get('topic')
        if topic:
            if file['type'] == 'concept':
                topic_index[topic]['concepts'].append(file)
            else:
                topic_index[topic]['sources'].append(file)
    
    return topic_index

def calculate_cooccurrence(files):
    """Calculate tag co-occurrence matrix."""
    co_occurrence = defaultdict(int)
    
    for file in files:
        all_tags = []
        if file.get('main_tag'):
            all_tags.append(file['main_tag'])
        all_tags.extend(file.get('sub_tags', []))
        
        # Count pairs
        for i, tag1 in enumerate(all_tags):
            for tag2 in all_tags[i+1:]:
                pair = tuple(sorted([tag1, tag2]))
                co_occurrence[pair] += 1
    
    return co_occurrence

def get_top_cooccurring(co_occurrence, tag, n=5):
    """Get top N co-occurring tags for a given tag."""
    pairs = []
    for (t1, t2), count in co_occurrence.items():
        if t1 == tag:
            pairs.append((t2, count))
        elif t2 == tag:
            pairs.append((t1, count))
    
    pairs.sort(key=lambda x: -x[1])
    return pairs[:n]

def write_tag_index(tag, data, co_occurrence, today):
    """Generate and write tag index file."""
    total = len(data['concepts']) + len(data['sources'])
    
    content = f"""---
type: index
level: 3
scope: tag
parent: "[[tag]]"
tag: {tag}
auto_generated: true
last_updated: {today}
---

# Tag: #{tag}

## Parent

- [[tag]]

## Stats

- Total files: {total}
- Sources: {len(data['sources'])}
- Concepts: {len(data['concepts'])}
- Last updated: {today}

## Files with this tag

"""
    
    # Merge and sort all items
    all_items = []
    for f in data['concepts']:
        all_items.append((f['slug'], f['title'], 'concept'))
    for f in data['sources']:
        all_items.append((f['slug'], f['title'], 'source'))
    
    all_items.sort(key=lambda x: x[0])
    
    for slug, title, ftype in all_items:
        content += f"- [[{slug}]] — {title} ({ftype})\n"
    
    # Add co-occurring tags
    top_cooccur = get_top_cooccurring(co_occurrence, tag)
    if top_cooccur:
        content += "\n## Co-occurring tags\n\n"
        for other_tag, count in top_cooccur:
            unit = "co-occurrence" if count == 1 else "co-occurrences"
            content += f"- [[{other_tag}]] — {count} {unit}\n"
    
    # Write file
    tag_file = WIKI_TAG / f"{tag}.md"
    tag_file.write_text(content, encoding='utf-8')
    return str(tag_file.relative_to(WIKI_ROOT))

def write_topic_index(topic, data, today):
    """Generate and write topic index file."""
    content = f"""---
type: index
scope: topic
parent: "[[topic]]"
topic: {topic}
auto_generated: true
last_updated: {today}
---

# Topic: {topic}

Auto-generated index of all content with topic `{topic}`.

Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

---

## Concepts ({len(data['concepts'])})

"""
    
    # Sort concepts
    concepts = sorted(data['concepts'], key=lambda x: x['slug'])
    for f in concepts:
        main = f.get('main_tag', 'none')
        subs = ', '.join([f"#{s}" for s in f.get('sub_tags', [])]) or 'none'
        content += f"- [[{f['slug']}]] — main: #{main}, sub: [{subs}]\n"
    
    content += f"\n## Sources ({len(data['sources'])})\n\n"
    
    # Sort sources
    sources = sorted(data['sources'], key=lambda x: x['slug'])
    for f in sources:
        main = f.get('main_tag', 'none')
        subs = ', '.join([f"#{s}" for s in f.get('sub_tags', [])]) or 'none'
        content += f"- [[{f['slug']}]] — main: #{main}, sub: [{subs}]\n"
    
    # Write file
    topic_file = WIKI_TOPIC / f"{topic}.md"
    topic_file.write_text(content, encoding='utf-8')
    return str(topic_file.relative_to(WIKI_ROOT))

def update_tag_master(tag_index, today):
    """Update wiki/tag/tag.md master index."""
    main_tags = set()
    sub_tags = set()
    
    # Load TAGS.md to categorize
    with open(TAGS_MD, 'r', encoding='utf-8') as f:
        tags_content = f.read()
    
    in_pool_a = False
    for line in tags_content.split('\n'):
        if 'Pool A' in line or 'Main Tags' in line:
            in_pool_a = True
        elif 'Pool B' in line or 'Sub Tags' in line:
            in_pool_a = False
        elif in_pool_a and '|' in line and '`#' in line:
            tag = re.search(r'`#([^`]+)`', line)
            if tag:
                main_tags.add(tag.group(1))
    
    in_pool_b = False
    for line in tags_content.split('\n'):
        if 'Pool B' in line or 'Sub Tags' in line:
            in_pool_b = True
        if in_pool_b and '|' in line and '`#' in line:
            tag = re.search(r'`#([^`]+)`', line)
            if tag:
                sub_tags.add(tag.group(1))
    
    # Calculate counts
    total_tags = len(tag_index)
    main_count = len([t for t in tag_index if t in main_tags])
    sub_count = total_tags - main_count
    
    # Find most used tags
    tag_counts = {}
    for tag, data in tag_index.items():
        tag_counts[tag] = len(data['concepts']) + len(data['sources'])
    
    top_3 = sorted(tag_counts.items(), key=lambda x: -x[1])[:3]
    most_used = ', '.join([f"#{t} ({c})" for t, c in top_3])
    
    # Read current tag.md
    tag_md_path = WIKI_TAG / "tag.md"
    if tag_md_path.exists():
        with open(tag_md_path, 'r', encoding='utf-8') as f:
            content = f.read()
    else:
        content = "# Tag Index\n\n"
    
    # Update Stats section
    stats_section = f"""## Stats

- Total tags: {total_tags}
- Main tags: {main_count}
- Sub tags: {sub_count}
- Most used: {most_used}
- Last updated: {today}"""
    
    if '## Stats' in content:
        content = re.sub(r'## Stats.*?\n## ', stats_section + '\n\n## ', content, flags=re.DOTALL)
    else:
        content = content.replace('# Tag Index\n\n', f'# Tag Index\n\n{stats_section}\n\n')
    
    # Update Items section - add missing tags
    for tag in sorted(tag_index.keys()):
        if f"[[{tag}]]" not in content:
            # Find description from TAGS.md
            desc_match = re.search(rf'\| `#?{tag}`? \| ([^|]+) \|', tags_content)
            description = desc_match.group(1).strip() if desc_match else "[description]"
            
            if tag in main_tags:
                section = "### Main Tags (Pool A)"
            else:
                section = "### Sub Tags (Pool B)"
            
            if section in content:
                content = content.replace(section + '\n', section + f'\n- [[{tag}]] — {description}\n')
    
    tag_md_path.write_text(content, encoding='utf-8')

def cleanup_orphans(tag_index, topic_index):
    """Remove orphaned index files."""
    deleted = {'tags': [], 'topics': []}
    
    # Check tag orphans
    if WIKI_TAG.exists():
        for tag_file in WIKI_TAG.glob('*.md'):
            tag_name = tag_file.stem
            if tag_name != 'tag' and tag_name not in tag_index:
                tag_file.unlink()
                deleted['tags'].append(tag_name)
    
    # Check topic orphans
    if WIKI_TOPIC.exists():
        for topic_file in WIKI_TOPIC.glob('*.md'):
            topic_name = topic_file.stem
            if topic_name not in topic_index:
                topic_file.unlink()
                deleted['topics'].append(topic_name)
    
    return deleted

def log_to_memory(files, tag_index, topic_index, deleted, errors, invalid_tags):
    """Append summary to MEMORY.md."""
    concepts = [f for f in files if f['type'] == 'concept']
    sources = [f for f in files if f['type'] == 'source']
    
    log_entry = f"""
## {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} — Indexed

- **Scanned:** {len(concepts)} concepts + {len(sources)} sources = {len(files)} total files
- **Tags indexed:** {len(tag_index)} ({len([t for t in tag_index if t in ['ai', 'crypto', 'tech', 'productivity', 'system', 'economic', 'politic']])} main-tags + {len(tag_index) - len([t for t in tag_index if t in ['ai', 'crypto', 'tech', 'productivity', 'system', 'economic', 'politic']])} sub-tags)
- **Topics indexed:** {len(topic_index)}
- **Orphans deleted:** {len(deleted['tags'])} tag indexes + {len(deleted['topics'])} topic indexes
- **Invalid tags found:** {len(invalid_tags)}
- **Errors:** {len(errors)} files skipped
"""
    
    if invalid_tags:
        log_entry += "\n**Invalid tag details:**\n"
        for path, tag_type, tag in invalid_tags[:10]:
            log_entry += f"- {path}: {tag_type}=#{tag}\n"
    
    if errors:
        log_entry += "\n**Error details:**\n"
        for path, err in errors[:5]:
            log_entry += f"- {path}: {err}\n"
    
    with open(MEMORY_MD, 'a', encoding='utf-8') as f:
        f.write(log_entry)

def main():
    print("=" * 60)
    print("Index Agent - Full Rebuild Mode")
    print("=" * 60)
    
    today = datetime.now().strftime('%Y-%m-%d')
    
    # Step 1: Scan all files
    print("\n[Step 1] Scanning wiki files...")
    files, errors, invalid_tags = scan_files()
    print(f"  ✓ Scanned {len(files)} files")
    if errors:
        print(f"  ⚠ {len(errors)} files with errors (skipped)")
    if invalid_tags:
        print(f"  ⚠ {len(invalid_tags)} invalid tags found")
    
    # Step 2: Build tag index
    print("\n[Step 2] Building tag index...")
    tag_index = build_tag_index(files)
    print(f"  ✓ {len(tag_index)} unique tags")
    
    # Step 3: Calculate co-occurrence
    print("\n[Step 3] Calculating co-occurrence...")
    co_occurrence = calculate_cooccurrence(files)
    print(f"  ✓ {len(co_occurrence)} tag pairs")
    
    # Step 4: Build topic index
    print("\n[Step 4] Building topic index...")
    topic_index = build_topic_index(files)
    print(f"  ✓ {len(topic_index)} unique topics")
    
    # Step 5: Write tag index files
    print("\n[Step 5] Writing tag index files...")
    WIKI_TAG.mkdir(parents=True, exist_ok=True)
    for tag, data in tag_index.items():
        write_tag_index(tag, data, co_occurrence, today)
    print(f"  ✓ {len(tag_index)} tag index files written")
    
    # Step 6: Write topic index files
    print("\n[Step 6] Writing topic index files...")
    WIKI_TOPIC.mkdir(parents=True, exist_ok=True)
    for topic, data in topic_index.items():
        write_topic_index(topic, data, today)
    print(f"  ✓ {len(topic_index)} topic index files written")
    
    # Step 7: Update master tag index
    print("\n[Step 7] Updating tag.md master index...")
    update_tag_master(tag_index, today)
    print("  ✓ tag.md updated")
    
    # Step 8: Cleanup orphans
    print("\n[Step 8] Cleaning up orphaned indexes...")
    deleted = cleanup_orphans(tag_index, topic_index)
    print(f"  ✓ Deleted {len(deleted['tags'])} orphaned tag indexes")
    print(f"  ✓ Deleted {len(deleted['topics'])} orphaned topic indexes")
    
    # Step 9: Log to memory
    print("\n[Step 9] Logging to MEMORY.md...")
    log_to_memory(files, tag_index, topic_index, deleted, errors, invalid_tags)
    print("  ✓ Logged")
    
    # Step 10: Write success timestamp
    print("\n[Step 10] Writing success timestamp...")
    success_file = WIKI_ROOT / ".openclaw" / "last-index-success.txt"
    with open(success_file, 'w') as f:
        f.write(datetime.now().isoformat())
    print(f"  ✓ Timestamp written: {success_file}")
    
    print("\n" + "=" * 60)
    print("Index rebuild complete!")
    print("=" * 60)
    
    return 0

if __name__ == "__main__":
    exit(main())
