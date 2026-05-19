import os
import re
import yaml
from datetime import datetime
from collections import defaultdict

# --- Configuration ---
WIKI_SOURCES = 'wiki/sources/'
WIKI_CONCEPTS = 'wiki/concepts/'
TAG_DIR = 'wiki/tag/'
TOPIC_DIR = 'wiki/topic/'
TAGS_FILE = 'TAGS.md'
MEMORY_FILE = '.openclaw/MEMORY.md'
TAG_MASTER_INDEX = 'wiki/tag/tag.md'

POOL_A = ['ai', 'crypto', 'tech', 'productivity', 'system', 'economic', 'politic']
POOL_B = ['hack', 'tools', 'automation', 'vibecode', 'research', 'tutorial', 'opinion', 'news', 'defi', 'perpdex', 'layer1', 'layer2', 'law']

def derive_title(slug):
    # Remove src_ prefix for sources
    clean_slug = slug.replace('src_', '')
    return ' '.join(word.capitalize() for word in clean_slug.split('-'))

def parse_frontmatter(path):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
        match = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
        if not match:
            return None
        try:
            return yaml.safe_load(match.group(1))
        except Exception:
            return None

def get_slug(path):
    return os.path.basename(path).replace('.md', '')

def main():
    # 1. Scan Files
    all_files_data = []
    skipped_files = 0
    invalid_tags_found = []
    
    search_dirs = [WIKI_SOURCES, WIKI_CONCEPTS]
    for d in search_dirs:
        if not os.path.exists(d): continue
        for filename in sorted(os.listdir(d)):
            if filename.endswith('.md'):
                path = os.path.join(d, filename)
                fm = parse_frontmatter(path)
                if not fm:
                    print(f"[WARNING] {path}: No or invalid frontmatter. Skipping.")
                    skipped_files += 1
                    continue
                
                # Required fields
                try:
                    f_type = fm.get('type')
                    main_tag = fm.get('main_tag')
                    sub_tags = fm.get('sub_tags', [])
                    topic = fm.get('topic')
                    
                    if not all([f_type, main_tag, topic]):
                        print(f"[ERROR] {path}: Missing required frontmatter fields.")
                        skipped_files += 1
                        continue
                    
                    if not isinstance(sub_tags, list):
                        sub_tags = [sub_tags] if sub_tags else []
                    
                    # Tag validation
                    invalid_main = False
                    if main_tag not in POOL_A:
                        print(f"[INVALID TAG] {path}: main_tag={main_tag}")
                        invalid_tags_found.append((path, main_tag))
                        invalid_main = True
                    
                    invalid_subs = []
                    for st in sub_tags:
                        if st not in POOL_B:
                            print(f"[INVALID TAG] {path}: sub_tag={st}")
                            invalid_tags_found.append((path, st))
                            invalid_subs.append(st)
                    
                    all_files_data.append({
                        'path': path,
                        'slug': get_slug(path),
                        'type': f_type,
                        'main_tag': main_tag,
                        'sub_tags': sub_tags,
                        'topic': topic,
                        'invalid_main': invalid_main,
                        'invalid_subs': invalid_subs
                    })
                except Exception as e:
                    print(f"[ERROR] {path}: {e}")
                    skipped_files += 1

    # 2. Group by Tag
    tag_index = defaultdict(lambda: {'concepts': [], 'sources': []})
    for f in all_files_data:
        # Main tag
        if not f['invalid_main']:
            tag = f['main_tag']
            category = 'concepts' if f['type'] == 'concept' else 'sources'
            tag_index[tag][category].append(f)
        
        # Sub tags
        for st in f['sub_tags']:
            if st not in f['invalid_subs']:
                tag = st
                category = 'concepts' if f['type'] == 'concept' else 'sources'
                tag_index[tag][category].append(f)

    # 3. Co-occurrence
    co_occurrence = defaultdict(int)
    for f in all_files_data:
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
    for tag in tag_index.keys():
        pairs = []
        for (t1, t2), count in co_occurrence.items():
            if tag == t1: pairs.append((t2, count))
            elif tag == t2: pairs.append((t1, count))
        
        tag_co_occur[tag] = sorted(pairs, key=lambda x: -x[1])[:5]

    # 4. Group by Topic
    topic_index = defaultdict(lambda: {'concepts': [], 'sources': []})
    for f in all_files_data:
        topic = f['topic']
        category = 'concepts' if f['type'] == 'concept' else 'sources'
        topic_index[topic][category].append(f)

    # 5. Topic Overlap
    topic_overlap = defaultdict(int)
    topics = sorted(topic_index.keys())
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
    for topic in topic_index.keys():
        pairs = []
        for (t1, t2), count in topic_overlap.items():
            if topic == t1: pairs.append((t2, count))
            elif topic == t2: pairs.append((t1, count))
        topic_related[topic] = sorted(pairs, key=lambda x: -x[1])[:5]

    # 6. Write Tag Index Files
    os.makedirs(TAG_DIR, exist_ok=True)
    today = datetime.now().strftime('%Y-%m-%d')
    
    for tag, data in tag_index.items():
        # Sort entries alphabetically by slug
        items = []
        for f in data['concepts']:
            items.append((f['slug'], derive_title(f['slug']), 'concept'))
        for f in data['sources']:
            items.append((f['slug'], derive_title(f['slug']), 'source'))
        items.sort()

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

- Total files: {len(items)}
- Sources: {len(data['sources'])}
- Concepts: {len(data['concepts'])}
- Last updated: {today}

## Files with this tag

"""
        for slug, title, ftype in items:
            content += f"- [[{slug}]] — {title} ({ftype})\n"
        
        co_occur = tag_co_occur.get(tag, [])
        if co_occur:
            content += "\n## Co-occurring tags\n\n"
            for other_tag, count in co_occur:
                unit = "co-occurrence" if count == 1 else "co-occurrences"
                content += f"- [[{other_tag}]] — {count} {unit}\n"
        
        with open(os.path.join(TAG_DIR, f"{tag}.md"), 'w', encoding='utf-8') as f:
            f.write(content)

    # 7. Write Topic Index Files
    os.makedirs(TOPIC_DIR, exist_ok=True)
    for topic, data in topic_index.items():
        content = f"# Topic: {topic}\n\nAuto-generated index of all content with topic `{topic}`.\n\nLast updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n---\n\n## Concepts ({len(data['concepts'])})\n\n"
        
        sorted_concepts = sorted(data['concepts'], key=lambda x: x['slug'])
        for f in sorted_concepts:
            subs = ', '.join([f"#{s}" for s in f['sub_tags']])
            content += f"- [[{f['slug']}]] — main: #{f['main_tag']}, sub: [{subs}]\n"
        
        content += f"\n## Sources ({len(data['sources'])})\n\n"
        sorted_sources = sorted(data['sources'], key=lambda x: x['slug'])
        for f in sorted_sources:
            subs = ', '.join([f"#{s}" for s in f['sub_tags']])
            content += f"- [[{f['slug']}]] — main: #{f['main_tag']}, sub: [{subs}]\n"
        
        related = topic_related.get(topic, [])
        if related:
            content += "\n## Related topics\n\n"
            content += f"Topics that share concepts/sources with `{topic}`:\n"
            for other_topic, count in related:
                content += f"- `{other_topic}` ({count} shared files)\n"
        
        with open(os.path.join(TOPIC_DIR, f"{topic}.md"), 'w', encoding='utf-8') as f:
            f.write(content)

    # 8. Update tag.md master index
    if os.path.exists(TAG_MASTER_INDEX):
        with open(TAG_MASTER_INDEX, 'r', encoding='utf-8') as f:
            master_content = f.read()
        
        # Update items
        # We'll just regenerate the Items section if it's too complex, 
        # but the workflow says "Append new tags". Let's be safer and rebuild the list.
        
        # Extract description from TAGS.md
        tag_descriptions = {}
        with open(TAGS_FILE, 'r', encoding='utf-8') as tf:
            for line in tf:
                if '| `#`' in line:
                    parts = line.split('|')
                    if len(parts) >= 3:
                        tag_name = parts[1].strip().replace('#', '').replace('`', '')
                        desc = parts[2].strip()
                        tag_descriptions[tag_name] = desc

        # Rebuild Pool A and Pool B lists
        pool_a_list = ""
        for tag in POOL_A:
            if tag in tag_index:
                desc = tag_descriptions.get(tag, "[description]")
                pool_a_list += f"- [[{tag}]] — {desc}\n"
        
        pool_b_list = ""
        for tag in POOL_B:
            if tag in tag_index:
                desc = tag_descriptions.get(tag, "[description]")
                pool_b_list += f"- [[{tag}]] — {desc}\n"

        # Replace sections using regex
        master_content = re.sub(r'### Main Tags \(Pool A\)\n(.*?)(?=\n###|$)', 
                                f'### Main Tags (Pool A)\n{pool_a_list}', 
                                master_content, flags=re.DOTALL)
        master_content = re.sub(r'### Sub Tags \(Pool B\)\n(.*?)(?=\n###|$)', 
                                f'### Sub Tags (Pool B)\n{pool_b_list}', 
                                master_content, flags=re.DOTALL)
        
        # Update stats
        total_tags = len(tag_index)
        main_tags_count = len([t for t in POOL_A if t in tag_index])
        sub_tags_count = len([t for t in POOL_B if t in tag_index])
        
        # Top 3 tags
        counts = []
        for tag, data in tag_index.items():
            counts.append((len(data['concepts']) + len(data['sources']), tag))
        counts.sort(key=lambda x: -x[0])
        top_3 = ", ".join([f"#{t} ({c})" for c, t in counts[:3]])
        
        stats = f"""## Stats

- Total tags: {total_tags}
- Main tags: {main_tags_count}
- Sub tags: {sub_tags_count}
- Most used: {top_3}
- Last updated: {today}
"""
        master_content = re.sub(r'## Stats\n\n(.*?)(?=\n## Items|$)', 
                                f'{stats}', 
                                master_content, flags=re.DOTALL)
        
        with open(TAG_MASTER_INDEX, 'w', encoding='utf-8') as f:
            f.write(master_content)

    # 9. Cleanup Orphans
    orphaned_tags = []
    if os.path.exists(TAG_DIR):
        for filename in os.listdir(TAG_DIR):
            if filename.endswith('.md') and filename != 'tag.md':
                tag = filename.replace('.md', '')
                if tag not in tag_index:
                    orphaned_tags.append(tag)
                    os.remove(os.path.join(TAG_DIR, filename))
    
    orphaned_topics = []
    if os.path.exists(TOPIC_DIR):
        for filename in os.listdir(TOPIC_DIR):
            if filename.endswith('.md'):
                topic = filename.replace('.md', '')
                if topic not in topic_index:
                    orphaned_topics.append(topic)
                    os.remove(os.path.join(TOPIC_DIR, filename))

    # 10. Memory Log
    log_entry = f"""## {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} — Indexed

- **Scanned:** {len([f for f in all_files_data if f['type']=='concept'])} concepts + {len([f for f in all_files_data if f['type']=='source'])} sources = {len(all_files_data)} total files
- **Tags indexed:** {len(tag_index)} ({len([t for t in POOL_A if t in tag_index])} main-tags + {len([t for t in POOL_B if t in tag_index])} sub-tags)
- **Topics indexed:** {len(topic_index)}
- **Orphans deleted:** {len(orphaned_tags)} tag indexes + {len(orphaned_topics)} topic indexes
- **Invalid tags found:** {len(invalid_tags_found)}
- **Errors:** {skipped_files} files skipped due to invalid frontmatter
"""
    with open(MEMORY_FILE, 'a', encoding='utf-8') as f:
        f.write('\n' + log_entry)

    print("Indexing complete.")

if __name__ == '__main__':
    main()
