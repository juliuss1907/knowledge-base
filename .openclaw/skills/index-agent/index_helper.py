import os
import re
import yaml
from datetime import datetime
from collections import defaultdict

def derive_title(slug):
    # Remove 'src_' prefix if present
    slug = slug.replace('src_', '')
    # Replace hyphens with spaces, title case
    return ' '.join(word.capitalize() for word in slug.split('-'))

def parse_frontmatter(content):
    match = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
    if not match:
        return None
    try:
        return yaml.safe_load(match.group(1))
    except Exception:
        return None

def load_taxonomy(tags_file):
    with open(tags_file, 'r', encoding='utf-8') as f:
        text = f.read()
    
    main_tags = {}
    sub_tags = {}
    
    # Split by sections
    sections = re.split(r'## \d+\.', text)
    
    for section in sections:
        if 'Pool A' in section:
            for line in section.split('\n'):
                if line.startswith('|') and '---' not in line and 'Tag' not in line:
                    parts = line.split('|')
                    if len(parts) >= 3:
                        tag = parts[1].strip().strip('`').lstrip('#')
                        desc = parts[2].strip()
                        main_tags[tag] = desc
        elif 'Pool B' in section:
            for line in section.split('\n'):
                if line.startswith('|') and '---' not in line and 'Tag' not in line:
                    parts = line.split('|')
                    if len(parts) >= 3:
                        tag = parts[1].strip().strip('`').lstrip('#')
                        desc = parts[2].strip()
                        sub_tags[tag] = desc
                
    return main_tags, sub_tags

def main():
    today = datetime.now().strftime('%Y-%m-%d')
    today_full = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    # 1. Load Taxonomy
    main_allowed, sub_allowed = load_taxonomy('TAGS.md')
    all_allowed = {**main_allowed, **sub_allowed}
    
    # 2. Scan Files
    wiki_files = []
    errors = 0
    invalid_tags_found = []
    
    search_dirs = ['wiki/sources/', 'wiki/concepts/']
    for d in search_dirs:
        if not os.path.exists(d): continue
        for root, _, files in os.walk(d):
            for file in files:
                if file.endswith('.md'):
                    path = os.path.join(root, file)
                    with open(path, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    fm = parse_frontmatter(content)
                    if not fm:
                        errors += 1
                        continue
                    
                    # Required fields
                    try:
                        f_type = fm.get('type')
                        m_tag = fm.get('main_tag')
                        s_tags = fm.get('sub_tags', [])
                        topic = fm.get('topic')
                        
                        if not all([f_type, m_tag, topic]):
                            errors += 1
                            continue
                        
                        # Validate tags
                        invalid_main = False
                        if m_tag not in main_allowed:
                            invalid_tags_found.append(f"{path}: main_tag={m_tag}")
                            invalid_main = True
                            
                        invalid_subs = []
                        for st in s_tags:
                            if st not in sub_allowed:
                                invalid_tags_found.append(f"{path}: sub_tag={st}")
                                invalid_subs.append(st)
                        
                        slug = file[:-3]
                        wiki_files.append({
                            'path': path,
                            'type': f_type,
                            'main_tag': m_tag,
                            'sub_tags': s_tags,
                            'topic': topic,
                            'slug': slug,
                            'invalid_main': invalid_main,
                            'invalid_subs': invalid_subs
                        })
                    except Exception:
                        errors += 1
    
    # 3. Group by Tag
    tag_index = defaultdict(lambda: {'concepts': [], 'sources': []})
    for f in wiki_files:
        # Main tag
        if not f['invalid_main']:
            tag = f['main_tag']
            if f['type'] == 'concept': tag_index[tag]['concepts'].append(f)
            else: tag_index[tag]['sources'].append(f)
        
        # Sub tags
        for st in f['sub_tags']:
            if st not in f['invalid_subs']:
                tag = st
                if f['type'] == 'concept': tag_index[tag]['concepts'].append(f)
                else: tag_index[tag]['sources'].append(f)

    # Sort lists
    for tag in tag_index:
        tag_index[tag]['concepts'].sort(key=lambda x: x['slug'])
        tag_index[tag]['sources'].sort(key=lambda x: x['slug'])

    # 4. Co-occurrence
    co_occurrence = defaultdict(int)
    for f in wiki_files:
        # Only use valid tags for co-occurrence
        tags = []
        if not f['invalid_main']: tags.append(f['main_tag'])
        for st in f['sub_tags']:
            if st not in f['invalid_subs']: tags.append(st)
        
        tags = sorted(list(set(tags)))
        for i in range(len(tags)):
            for j in range(i + 1, len(tags)):
                co_occurrence[tuple(sorted([tags[i], tags[j]]))] += 1
    
    tag_co_occur = {}
    for tag in tag_index:
        pairs = []
        for (t1, t2), count in co_occurrence.items():
            if tag == t1: pairs.append((t2, count))
            elif tag == t2: pairs.append((t1, count))
        tag_co_occur[tag] = sorted(pairs, key=lambda x: -x[1])[:5]

    # 5. Group by Topic
    topic_index = defaultdict(lambda: {'concepts': [], 'sources': []})
    for f in wiki_files:
        topic = f['topic']
        if f['type'] == 'concept': topic_index[topic]['concepts'].append(f)
        else: topic_index[topic]['sources'].append(f)
        
    for topic in topic_index:
        topic_index[topic]['concepts'].sort(key=lambda x: x['slug'])
        topic_index[topic]['sources'].sort(key=lambda x: x['slug'])

    # 6. Topic Overlap
    topic_overlap = defaultdict(int)
    topics = list(topic_index.keys())
    for i in range(len(topics)):
        t1 = topics[i]
        f1 = {f['path'] for f in topic_index[t1]['concepts'] + topic_index[t1]['sources']}
        for j in range(i + 1, len(topics)):
            t2 = topics[j]
            f2 = {f['path'] for f in topic_index[t2]['concepts'] + topic_index[t2]['sources']}
            shared = len(f1 & f2)
            if shared > 0:
                topic_overlap[tuple(sorted([t1, t2]))] = shared
    
    topic_related = {}
    for topic in topic_index:
        pairs = []
        for (t1, t2), count in topic_overlap.items():
            if topic == t1: pairs.append((t2, count))
            elif topic == t2: pairs.append((t1, count))
        topic_related[topic] = sorted(pairs, key=lambda x: -x[1])[:5]

    # 7. Write Tag Indexes
    os.makedirs('wiki/tag', exist_ok=True)
    for tag, data in tag_index.items():
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

- Total files: {len(all_items)}
- Sources: {len(data['sources'])}
- Concepts: {len(data['concepts'])}
- Last updated: {today}

## Files with this tag

"""
        for slug, title, ftype in all_items:
            content += f"- [[{slug}]] — {title} ({ftype})\n"
        
        co_occur = tag_co_occur.get(tag, [])
        if co_occur:
            content += "\n## Co-occurring tags\n\n"
            for other, count in co_occur:
                unit = "co-occurrence" if count == 1 else "co-occurrences"
                content += f"- [[{other}]] — {count} {unit}\n"
        
        with open(f'wiki/tag/{tag}.md', 'w', encoding='utf-8') as f:
            f.write(content)

    # 8. Write Topic Indexes
    os.makedirs('wiki/topic', exist_ok=True)
    for topic, data in topic_index.items():
        content = f"""# Topic: {topic}

Auto-generated index of all content with topic `{topic}`.

Last updated: {today_full}

---

## Concepts ({len(data['concepts'])})

"""
        for f in data['concepts']:
            subs = ', '.join([f"#{s}" for s in f['sub_tags']])
            content += f"- [[{f['slug']}]] — main: #{f['main_tag']}, sub: [{subs}]\n"
        
        content += f"\n## Sources ({len(data['sources'])})\n\n"
        for f in data['sources']:
            subs = ', '.join([f"#{s}" for s in f['sub_tags']])
            content += f"- [[{f['slug']}]] — main: #{f['main_tag']}, sub: [{subs}]\n"
            
        related = topic_related.get(topic, [])
        if related:
            content += "\n## Related topics\n\n"
            content += f"Topics that share concepts/sources with `{topic}`:\n"
            for other, count in related:
                content += f"- `{other}` ({count} shared files)\n"
        
        with open(f'wiki/topic/{topic}.md', 'w', encoding='utf-8') as f:
            f.write(content)

    # 9. Update tag.md
    tag_master_path = 'wiki/tag/tag.md'
    if os.path.exists(tag_master_path):
        with open(tag_master_path, 'r', encoding='utf-8') as f:
            master_text = f.read()
    else:
        master_text = "# Tag Index\n\n## Stats\n\n## Items\n\n### Main Tags (Pool A)\n\n### Sub Tags (Pool B)\n"

    # Update Items
    for tag in all_allowed:
        desc = main_allowed.get(tag) or sub_allowed.get(tag)
        pool = "Main Tags (Pool A)" if tag in main_allowed else "Sub Tags (Pool B)"
        entry = f"- [[{tag}]] — {desc}"
        if entry not in master_text:
            # Find section and insert
            section_marker = f"### {pool}"
            if section_marker in master_text:
                master_text = master_text.replace(section_marker, f"{section_marker}\n{entry}")
            else:
                master_text += f"\n\n### {pool}\n{entry}"

    # Update Stats
    all_tag_files = [f for f in os.listdir('wiki/tag') if f.endswith('.md') and f != 'tag.md']
    total_tags = len(all_tag_files)
    main_tags_count = len(main_allowed)
    sub_tags_count = total_tags - main_tags_count
    
    tag_counts = []
    for tf in all_tag_files:
        tag = tf[:-3]
        with open(f'wiki/tag/{tf}', 'r', encoding='utf-8') as f:
            c = f.read().count('- [[')
            tag_counts.append((c, tag))
    
    tag_counts.sort(key=lambda x: -x[0])
    top_3 = ", ".join([f"#{t} ({c})" for c, t in tag_counts[:3]])
    
    stats_content = f"""## Stats

- Total tags: {total_tags}
- Main tags: {main_tags_count}
- Sub tags: {sub_tags_count}
- Most used: {top_3}
- Last updated: {today}
"""
    
    if "## Stats" in master_text:
        master_text = re.sub(r'## Stats.*?(\n\n## Items|\Z)', stats_content + "\n\n## Items", master_text, flags=re.DOTALL)
    else:
        master_text = stats_content + "\n\n" + master_text
        
    with open(tag_master_path, 'w', encoding='utf-8') as f:
        f.write(master_text)

    # 10. Cleanup Orphans
    orphaned_tags = []
    existing_tag_files = [f[:-3] for f in os.listdir('wiki/tag') if f.endswith('.md') and f != 'tag.md']
    current_tags = set()
    for f in wiki_files:
        if not f['invalid_main']: current_tags.add(f['main_tag'])
        for st in f['sub_tags']:
            if st not in f['invalid_subs']: current_tags.add(st)
            
    for etf in existing_tag_files:
        if etf not in current_tags:
            orphaned_tags.append(etf)
            os.remove(f'wiki/tag/{etf}.md')
            
    orphaned_topics = []
    existing_topic_files = [f[:-3] for f in os.listdir('wiki/topic') if f.endswith('.md')]
    current_topics = {f['topic'] for f in wiki_files}
    for etf in existing_topic_files:
        if etf not in current_topics:
            orphaned_topics.append(etf)
            os.remove(f'wiki/topic/{etf}.md')

    # Final Summary
    print(f"SCANNED: {len(wiki_files)} files ({len([f for f in wiki_files if f['type'] == 'concept'])} concepts, {len([f for f in wiki_files if f['type'] != 'concept'])} sources)")
    print(f"TAGS_INDEXED: {len(tag_index)}")
    print(f"TOPICS_INDEXED: {len(topic_index)}")
    print(f"ORPHANS_DELETED: {len(orphaned_tags)} tags, {len(orphaned_topics)} topics")
    print(f"ERRORS: {errors}")
    print(f"INVALID_TAGS: {len(invalid_tags_found)}")
    for it in invalid_tags_found:
        print(f"INVALID: {it}")

if __name__ == '__main__':
    main()
