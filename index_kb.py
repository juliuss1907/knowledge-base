import os
import re
import yaml
from datetime import datetime
from pathlib import Path

# Configuration
WORKSPACE_ROOT = Path('/home/julius/knowledge-base')
TAGS_FILE = WORKSPACE_ROOT / 'TAGS.md'
SOURCES_DIR = WORKSPACE_ROOT / 'wiki/sources'
CONCEPTS_DIR = WORKSPACE_ROOT / 'wiki/concepts'
TAG_INDEX_DIR = WORKSPACE_ROOT / 'wiki/tag'
TOPIC_INDEX_DIR = WORKSPACE_ROOT / 'wiki/topic'
TAG_MASTER_FILE = TAG_INDEX_DIR / 'tag.md'

def load_tags():
    with open(TAGS_FILE, 'r', encoding='utf-8') as f:
        content = f.read()
    
    main_tags = {}
    sub_tags = {}
    
    # Extract Pool A
    pool_a_match = re.search(r'## 2\. Pool A — Main-tags.*?\| Tag \| Description\s*\|---|([^#]+?)(?=\n##)', content, re.S)
    if pool_a_match:
        lines = pool_a_match.group(1).strip().split('\n')
        for line in lines:
            parts = line.split('|')
            if len(parts) >= 3:
                tag = parts[1].strip().replace('#', '')
                desc = parts[2].strip()
                main_tags[tag] = desc
                
    # Extract Pool B
    pool_b_match = re.search(r'## 3\. Pool B — Sub-tags.*?\| Tag \| Description\s*\|---|([^#]+?)(?=\n##)', content, re.S)
    if pool_b_match:
        lines = pool_b_match.group(1).strip().split('\n')
        for line in lines:
            parts = line.split('|')
            if len(parts) >= 3:
                tag = parts[1].strip().replace('#', '')
                desc = parts[2].strip()
                sub_tags[tag] = desc
                
    return main_tags, sub_tags

def parse_frontmatter(path):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    match = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.S)
    if not match:
        return None
    
    try:
        return yaml.safe_load(match.group(1))
    except Exception:
        return None

def derive_title(slug):
    # Remove 'src_' prefix for sources
    slug = slug.replace('src_', '')
    return ' '.join(word.capitalize() for word in slug.split('-'))

def main():
    today = datetime.now().strftime('%Y-%m-%d')
    main_whitelist, sub_whitelist = load_tags()
    all_allowed = {**main_whitelist, **sub_whitelist}
    
    files_data = []
    errors = 0
    invalid_tags_found = []
    
    # 1. Scan Wiki Files
    for folder in [SOURCES_DIR, CONCEPTS_DIR]:
        if not folder.exists(): continue
        for file_path in sorted(folder.glob('*.md')):
            fm = parse_frontmatter(file_path)
            if not fm:
                errors += 1
                continue
            
            # Required fields
            try:
                ftype = fm.get('type')
                main_tag = fm.get('main_tag')
                sub_tags = fm.get('sub_tags', [])
                topic = fm.get('topic')
                
                if not all([ftype, main_tag, topic]):
                    errors += 1
                    continue
                
                if not isinstance(sub_tags, list):
                    sub_tags = []
                
                slug = file_path.stem
                
                # Validation
                invalid_main = False
                if main_tag not in main_whitelist:
                    invalid_tags_found.append(f"{file_path.relative_to(WORKSPACE_ROOT)}: main_tag={main_tag}")
                    invalid_main = True
                
                invalid_subs = []
                for st in sub_tags:
                    if st not in sub_whitelist:
                        invalid_tags_found.append(f"{file_path.relative_to(WORKSPACE_ROOT)}: sub_tag={st}")
                        invalid_subs.append(st)
                
                files_data.append({
                    'path': file_path,
                    'type': ftype,
                    'main_tag': main_tag,
                    'sub_tags': sub_tags,
                    'topic': topic,
                    'slug': slug,
                    'invalid_main': invalid_main,
                    'invalid_subs': invalid_subs
                })
            except Exception:
                errors += 1

    # 2. Build Tag Index
    tag_index = {}
    for f in files_data:
        # Process main tag
        if not f['invalid_main']:
            tag = f['main_tag']
            if tag not in tag_index:
                tag_index[tag] = {'concepts': [], 'sources': []}
            if f['type'] == 'concept':
                tag_index[tag]['concepts'].append(f)
            else:
                tag_index[tag]['sources'].append(f)
        
        # Process sub tags
        for st in f['sub_tags']:
            if st not in f['invalid_subs']:
                if st not in tag_index:
                    tag_index[st] = {'concepts': [], 'sources': []}
                if f['type'] == 'concept':
                    tag_index[st]['concepts'].append(f)
                else:
                    tag_index[st]['sources'].append(f)

    # Sort lists
    for tag in tag_index:
        tag_index[tag]['concepts'].sort(key=lambda x: x['slug'])
        tag_index[tag]['sources'].sort(key=lambda x: x['slug'])

    # 3. Calculate Co-occurrence
    co_occurrence = {}
    for f in files_data:
        all_f_tags = [f['main_tag']] + f['sub_tags']
        # Only use valid tags for co-occurrence
        valid_f_tags = [t for t in all_f_tags if t in all_allowed]
        
        for i in range(len(valid_f_tags)):
            for j in range(i + 1, len(valid_f_tags)):
                pair = tuple(sorted([valid_f_tags[i], valid_f_tags[j]]))
                co_occurrence[pair] = co_occurrence.get(pair, 0) + 1
    
    tag_co_occur = {}
    for tag in tag_index:
        pairs = [(other, count) for (t1, t2), count in co_occurrence.items() 
                 if tag in (t1, t2) and (other := t2 if t1 == tag else t1)]
        top_5 = sorted(pairs, key=lambda x: -x[1])[:5]
        tag_co_occur[tag] = top_5

    # 4. Build Topic Index
    topic_index = {}
    for f in files_data:
        topic = f['topic']
        if topic not in topic_index:
            topic_index[topic] = {'concepts': [], 'sources': []}
        if f['type'] == 'concept':
            topic_index[topic]['concepts'].append(f)
        else:
            topic_index[topic]['sources'].append(f)
            
    for topic in topic_index:
        topic_index[topic]['concepts'].sort(key=lambda x: x['slug'])
        topic_index[topic]['sources'].sort(key=lambda x: x['slug'])

    # 5. Topic Overlap
    topic_overlap = {}
    topic_list = list(topic_index.keys())
    for i in range(len(topic_list)):
        t1 = topic_list[i]
        files1 = {f['path'] for f in topic_index[t1]['concepts'] + topic_index[t1]['sources']}
        for j in range(i + 1, len(topic_list)):
            t2 = topic_list[j]
            files2 = {f['path'] for f in topic_index[t2]['concepts'] + topic_index[t2]['sources']}
            shared = len(files1 & files2)
            if shared > 0:
                topic_overlap[tuple(sorted([t1, t2]))] = shared
                
    topic_related = {}
    for topic in topic_index:
        pairs = [(other, count) for (t1, t2), count in topic_overlap.items()
                 if topic in (t1, t2) and (other := t2 if t1 == topic else t1)]
        top_5 = sorted(pairs, key=lambda x: -x[1])[:5]
        topic_related[topic] = top_5

    # 6. Write Tag Indexes
    TAG_INDEX_DIR.mkdir(parents=True, exist_ok=True)
    for tag, data in tag_index.items():
        co_occur = tag_co_occur.get(tag, [])
        
        all_items = []
        for f in data['concepts']:
            all_items.append((f['slug'], derive_title(f['slug']), 'concept'))
        for f in data['sources']:
            all_items.append((f['slug'], derive_title(f['slug']), 'source'))
        all_items.sort(key=lambda x: x[0])
        
        content = f"""---
type: index
level: 3
scope: tag
parent: [[tag]]
tag: {tag}
auto_generated: true
last_updated: {today}
---

# Tag: #{tag}

## Parent

- [[tag]]

## Stats

- Total files: {len(data['concepts']) + len(data['sources'])}
- Sources: {len(data['sources'])}
- Concepts: {len(data['concepts'])}
- Last updated: {today}

## Files with this tag

"""
        for slug, title, ftype in all_items:
            content += f"- [[{slug}]] — {title} ({ftype})\n"
            
        if co_occur:
            content += "\n## Co-occurring tags\n\n"
            for other_tag, count in co_occur:
                unit = "co-occurrence" if count == 1 else "co-occurrences"
                content += f"- [[{other_tag}]] — {count} {unit}\n"
                
        with open(TAG_INDEX_DIR / f"{tag}.md", 'w', encoding='utf-8') as f:
            f.write(content)

    # 7. Write Topic Indexes
    TOPIC_INDEX_DIR.mkdir(parents=True, exist_ok=True)
    for topic, data in topic_index.items():
        related = topic_related.get(topic, [])
        
        content = f"# Topic: {topic}\n\nAuto-generated index of all content with topic `{topic}`.\n\nLast updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n---\n\n## Concepts ({len(data['concepts'])})\n\n"
        for f in data['concepts']:
            subs = ', '.join([f"#{s}" for s in f['sub_tags']])
            content += f"- [[{f['slug']}]] — main: #{f['main_tag']}, sub: [{subs}]\n"
        
        content += f"\n## Sources ({len(data['sources'])})\n\n"
        for f in data['sources']:
            subs = ', '.join([f"#{s}" for s in f['sub_tags']])
            content += f"- [[{f['slug']}]] — main: #{f['main_tag']}, sub: [{subs}]\n"
            
        if related:
            content += "\n## Related topics\n\n"
            content += f"Topics that share concepts/sources with `{topic}`:\n"
            for other_topic, count in related:
                content += f"- `{other_topic}` ({count} shared files)\n"
        
        with open(TOPIC_INDEX_DIR / f"{topic}.md", 'w', encoding='utf-8') as f:
            f.write(content)

    # 8. Update tag.md Master Index
    main_tags_list = list(main_whitelist.keys())
    
    # Read current tag.md or use template
    if TAG_MASTER_FILE.exists():
        with open(TAG_MASTER_FILE, 'r', encoding='utf-8') as f:
            master_content = f.read()
    else:
        master_content = "# Tag Index\n\n## Stats\n\n## Items\n\n### Main Tags (Pool A)\n\n### Sub Tags (Pool B)\n"

    # Update Items section
    # This is a bit tricky with regex, but we will rebuild Items
    items_part = ""
    
    # Main tags
    items_part += "### Main Tags (Pool A)\n\n"
    for tag in sorted(main_whitelist.keys()):
        desc = main_whitelist[tag]
        items_part += f"- [[{tag}]] — {desc}\n"
    
    items_part += "\n### Sub Tags (Pool B)\n\n"
    for tag in sorted(sub_whitelist.keys()):
        desc = sub_whitelist[tag]
        items_part += f"- [[{tag}]] — {desc}\n"

    # Replace Items section
    if "## Items" in master_content:
        master_content = re.sub(r'## Items.*', f'## Items\n\n{items_part}', master_content, flags=re.S)
    else:
        master_content += f"\n\n## Items\n\n{items_part}"

    # Update Stats
    total_tags_files = len([f for f in TAG_INDEX_DIR.glob('*.md') if f.name != 'tag.md'])
    main_count = len(main_whitelist)
    sub_count = total_tags_files - main_count
    
    # Most used
    tag_counts = []
    for tag_file in TAG_INDEX_DIR.glob('*.md'):
        if tag_file.name == 'tag.md': continue
        with open(tag_file, 'r', encoding='utf-8') as f:
            count = len(re.findall(r'^\- \[\[', f.read(), re.M))
            tag_counts.append((count, tag_file.stem))
    
    top_3 = sorted(tag_counts, key=lambda x: -x[0])[:3]
    most_used_str = ", ".join([f"#{t} ({c})" for c, t in top_3])
    
    stats_content = f"""## Stats

- Total tags: {total_tags_files}
- Main tags: {main_count}
- Sub tags: {sub_count}
- Most used: {most_used_str}
- Last updated: {today}
"""
    if "## Stats" in master_content:
        master_content = re.sub(r'## Stats.*?(?=## Items|$)', stats_content, master_content, flags=re.S)
    else:
        master_content = stats_content + "\n\n" + master_content
        
    with open(TAG_MASTER_FILE, 'w', encoding='utf-8') as f:
        f.write(master_content)

    # 9. Cleanup Orphans
    orphaned_tags = []
    existing_tag_files = [f.stem for f in TAG_INDEX_DIR.glob('*.md') if f.name != 'tag.md']
    current_tags = set()
    for f in files_data:
        current_tags.add(f['main_tag'])
        for st in f['sub_tags']:
            current_tags.add(st)
    
    for tf in existing_tag_files:
        if tf not in current_tags:
            (TAG_INDEX_DIR / f"{tf}.md").unlink()
            orphaned_tags.append(tf)
            
    orphaned_topics = []
    existing_topic_files = [f.stem for f in TOPIC_INDEX_DIR.glob('*.md')]
    current_topics = {f['topic'] for f in files_data}
    for tf in existing_topic_files:
        if tf not in current_topics:
            (TOPIC_INDEX_DIR / f"{tf}.md").unlink()
            orphaned_topics.append(tf)

    # Final Summary
    summary = f"""## {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} — Indexed

- **Scanned:** {len([f for f in files_data if f['type'] == 'concept'])} concepts + {len([f for f in files_data if f['type'] == 'source'])} sources = {len(files_data)} total files
- **Tags indexed:** {len(tag_index)} ({len(main_whitelist)} main-tags + {len(tag_index)-len(main_whitelist)} sub-tags)
- **Topics indexed:** {len(topic_index)}
- **Orphans deleted:** {len(orphaned_tags)} tag indexes + {len(orphaned_topics)} topic indexes
- **Invalid tags found:** {len(invalid_tags_found)}
- **Errors:** {errors} files skipped
"""
    if invalid_tags_found:
        summary += "\n### Invalid Tags Detail\n"
        for item in invalid_tags_found:
            summary += f"- {item}\n"
            
    return summary

if __name__ == '__main__':
    print(main())
