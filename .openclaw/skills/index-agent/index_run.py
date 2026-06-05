import os
import re
from datetime import datetime
from collections import defaultdict

# Configuration
ROOT = "/home/julius/knowledge-base"
WIKI_SOURCES = os.path.join(ROOT, "wiki/sources")
WIKI_CONCEPTS = os.path.join(ROOT, "wiki/concepts")
TAG_DIR = os.path.join(ROOT, "wiki/tag")
TOPIC_DIR = os.path.join(ROOT, "wiki/topic")
TAGS_FILE = os.path.join(ROOT, "TAGS.md")
TAG_MASTER_FILE = os.path.join(TAG_DIR, "tag.md")
MEMORY_FILE = os.path.join(ROOT, ".openclaw/MEMORY.md")

# Tag Taxonomy from TAGS.md
POOL_A = ['ai', 'crypto', 'tech', 'productivity', 'system', 'economic', 'politic']
POOL_B = ['hack', 'tools', 'automation', 'vibecode', 'research', 'tutorial', 'opinion', 'news', 'defi', 'perpdex', 'layer1', 'layer2', 'law', 'coding', 'psychology', 'health']

def parse_frontmatter(content):
    if not content.startswith('---'):
        return None
    match = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
    if not match:
        return None
    
    yaml_text = match.group(1)
    data = {}
    for line in yaml_text.split('\n'):
        if ':' in line:
            k, v = line.split(':', 1)
            k = k.strip()
            v = v.strip()
            if v.startswith('[') and v.endswith(']'):
                v = [item.strip() for item in v[1:-1].split(',') if item.strip()]
            data[k] = v
    return data

def derive_title(slug):
    return ' '.join(word.capitalize() for word in slug.split('-'))

def run_indexing():
    today = datetime.now().strftime('%Y-%m-%d')
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    files_data = []
    errors = 0
    invalid_tags_found = []

    # 1. Scan files
    for folder in [WIKI_SOURCES, WIKI_CONCEPTS]:
        if not os.path.exists(folder): continue
        for filename in sorted(os.listdir(folder)):
            if not filename.endswith('.md'): continue
            path = os.path.join(folder, filename)
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
                fm = parse_frontmatter(content)
                if not fm:
                    errors += 1
                    continue
                
                # Basic validation
                ftype = fm.get('type')
                main_tag = fm.get('main_tag')
                sub_tags = fm.get('sub_tags', [])
                topic = fm.get('topic')
                
                if not all([ftype, main_tag, topic]):
                    errors += 1
                    continue
                
                if isinstance(sub_tags, str): sub_tags = [sub_tags]

                slug = filename[:-3]
                
                # Tag validation
                invalid_main = False
                if main_tag not in POOL_A:
                    invalid_tags_found.append(f"{path}: main_tag={main_tag}")
                    invalid_main = True
                
                invalid_subs = []
                for st in sub_tags:
                    if st not in POOL_B:
                        invalid_tags_found.append(f"{path}: sub_tag={st}")
                        invalid_subs.append(st)
                
                files_data.append({
                    'path': path,
                    'slug': slug,
                    'type': ftype,
                    'main_tag': main_tag,
                    'sub_tags': sub_tags,
                    'topic': topic,
                    'invalid_main': invalid_main,
                    'invalid_subs': invalid_subs
                })

    # 2. Group by tag
    tag_index = defaultdict(lambda: {'concepts': [], 'sources': []})
    for f in files_data:
        # Main tag
        if not f['invalid_main']:
            tag = f['main_tag']
            if f['type'] == 'concept': tag_index[tag]['concepts'].append(f)
            else: tag_index[tag]['sources'].append(f)
        
        # Sub tags
        for st in f['sub_tags']:
            if st not in f['invalid_subs']:
                if f['type'] == 'concept': tag_index[st]['concepts'].append(f)
                else: tag_index[st]['sources'].append(f)

    # 3. Co-occurrence
    co_occurrence = defaultdict(int)
    for f in files_data:
        tags = [f['main_tag']] + f['sub_tags']
        # Only use valid tags for co-occurrence
        valid_tags = []
        if not f['invalid_main']: valid_tags.append(f['main_tag'])
        for st in f['sub_tags']:
            if st not in f['invalid_subs']: valid_tags.append(st)
        
        valid_tags = sorted(list(set(valid_tags)))
        for i in range(len(valid_tags)):
            for j in range(i + 1, len(valid_tags)):
                pair = tuple(sorted([valid_tags[i], valid_tags[j]]))
                co_occurrence[pair] += 1

    # 4. Group by topic
    topic_index = defaultdict(lambda: {'concepts': [], 'sources': []})
    for f in files_data:
        topic = f['topic']
        if f['type'] == 'concept': topic_index[topic]['concepts'].append(f)
        else: topic_index[topic]['sources'].append(f)

    # 5. Topic overlap
    topic_overlap = defaultdict(int)
    topic_list = sorted(topic_index.keys())
    for i in range(len(topic_list)):
        for j in range(i + 1, len(topic_list)):
            t1, t2 = topic_list[i], topic_list[j]
            f1 = set([f['path'] for f in topic_index[t1]['concepts'] + topic_index[t1]['sources']])
            f2 = set([f['path'] for f in topic_index[t2]['concepts'] + topic_index[t2]['sources']])
            shared = len(f1 & f2)
            if shared > 0:
                topic_overlap[tuple(sorted([t1, t2]))] = shared

    # Write Tag Indexes
    os.makedirs(TAG_DIR, exist_ok=True)
    for tag, data in tag_index.items():
        # Top 5 co-occurring
        pairs = [(other, count) for (t1, t2), count in co_occurrence.items() if tag in (t1, t2)]
        others = [(t2 if t1 == tag else t1, count) for (t1, t2), count in pairs]
        top_5 = sorted(others, key=lambda x: -x[1])[:5]

        all_items = []
        for f in data['concepts']:
            all_items.append((f['slug'], derive_title(f['slug']), 'concept'))
        for f in data['sources']:
            # sources usually start with src_
            slug_clean = f['slug'].replace('src_', '')
            all_items.append((f['slug'], derive_title(slug_clean), 'source'))
        all_items.sort()

        content = f"---\ntype: index\nlevel: 3\nscope: tag\nparent: [[tag]]\ntag: {tag}\nauto_generated: true\nlast_updated: {today}\n---\n\n# Tag: #{tag}\n\n## Parent\n\n- [[tag]]\n\n## Stats\n\n- Total files: {len(all_items)}\n- Sources: {len(data['sources'])}\n- Concepts: {len(data['concepts'])}\n- Last updated: {today}\n\n## Files with this tag\n\n"
        for slug, title, ftype in all_items:
            content += f"- [[{slug}]] — {title} ({ftype})\n"
        
        if top_5:
            content += "\n## Co-occurring tags\n\n"
            for other, count in top_5:
                unit = "co-occurrence" if count == 1 else "co-occurrences"
                content += f"- [[{other}]] — {count} {unit}\n"
        
        with open(os.path.join(TAG_DIR, f"{tag}.md"), 'w', encoding='utf-8') as f:
            f.write(content)

    # Write Topic Indexes
    os.makedirs(TOPIC_DIR, exist_ok=True)
    for topic, data in topic_index.items():
        related = []
        pairs = [(other, count) for (t1, t2), count in topic_overlap.items() if topic in (t1, t2)]
        others = [(t2 if t1 == topic else t1, count) for (t1, t2), count in pairs]
        top_5_related = sorted(others, key=lambda x: -x[1])[:5]

        content = f"# Topic: {topic}\n\nAuto-generated index of all content with topic `{topic}`.\n\nLast updated: {timestamp}\n\n---\n\n## Concepts ({len(data['concepts'])})\n\n"
        for f in data['concepts']:
            subs = ', '.join([f"#{s}" for s in f['sub_tags']])
            content += f"- [[{f['slug']}]] — main: #{f['main_tag']}, sub: [{subs}]\n"
        
        content += f"\n## Sources ({len(data['sources'])})\n\n"
        for f in data['sources']:
            subs = ', '.join([f"#{s}" for s in f['sub_tags']])
            content += f"- [[{f['slug']}]] — main: #{f['main_tag']}, sub: [{subs}]\n"
        
        if top_5_related:
            content += "\n## Related topics\n\n"
            content += f"Topics that share concepts/sources with `{topic}`:\n"
            for other, count in top_5_related:
                content += f"- `{other}` ({count} shared files)\n"
        
        with open(os.path.join(TOPIC_DIR, f"{topic}.md"), 'w', encoding='utf-8') as f:
            f.write(content)

    # Update tag.md Master Index
    if os.path.exists(TAG_MASTER_FILE):
        with open(TAG_MASTER_FILE, 'r', encoding='utf-8') as f:
            master_content = f.read()
        
        # Update Items
        for tag in sorted(tag_index.keys()):
            if f"- [[{tag}]]" not in master_content:
                # Get description from TAGS.md
                desc = "[description]"
                with open(TAGS_FILE, 'r', encoding='utf-8') as tf:
                    for line in tf:
                        if f"| `#{tag}`" in line:
                            desc = line.split('|')[-1].strip()
                
                pool = "Main Tags (Pool A)" if tag in POOL_A else "Sub Tags (Pool B)"
                # Simple insertion after the pool header
                pattern = f"### {pool}"
                if pattern in master_content:
                    master_content = master_content.replace(pattern, f"{pattern}\n- [[{tag}]] — {desc}")

        # Update Stats
        all_tags = sorted(tag_index.keys())
        total_tags = len(all_tags)
        main_tags_count = len([t for t in all_tags if t in POOL_A])
        sub_tags_count = total_tags - main_tags_count
        
        tag_counts = {tag: len(data['concepts']) + len(data['sources']) for tag, data in tag_index.items()}
        top_3 = sorted(tag_counts.items(), key=lambda x: -x[1])[:3]
        most_used = ', '.join([f"#{t} ({c})" for t, c in top_3])
        
        stats_block = f"## Stats\n\n- Total tags: {total_tags}\n- Main tags: {main_tags_count}\n- Sub tags: {sub_tags_count}\n- Most used: {most_used}\n- Last updated: {today}"
        
        if "## Stats" in master_content:
            # Replace content between ## Stats and ## Items (or end of file)
            start = master_content.find("## Stats")
            end = master_content.find("## Items")
            if end == -1: end = len(master_content)
            master_content = master_content[:start] + stats_block + master_content[end:]
        
        with open(TAG_MASTER_FILE, 'w', encoding='utf-8') as f:
            f.write(master_content)

    # Cleanup Orphans
    orphaned_tags = []
    if os.path.exists(TAG_DIR):
        for filename in os.listdir(TAG_DIR):
            if filename == "tag.md" or not filename.endswith('.md'): continue
            tag = filename[:-3]
            if tag not in tag_index:
                orphaned_tags.append(tag)
                os.remove(os.path.join(TAG_DIR, filename))
    
    orphaned_topics = []
    if os.path.exists(TOPIC_DIR):
        for filename in os.listdir(TOPIC_DIR):
            if not filename.endswith('.md'): continue
            topic = filename[:-3]
            if topic not in topic_index:
                orphaned_topics.append(topic)
                os.remove(os.path.join(TOPIC_DIR, filename))

    # Log to Memory
    log_entry = f"\n## {timestamp} — Indexed\n\n"
    log_entry += f"- **Scanned:** {len([f for f in files_data if f['type']=='concept'])} concepts + {len([f for f in files_data if f['type']=='source'])} sources = {len(files_data)} total files\n"
    log_entry += f"- **Tags indexed:** {len(tag_index)} ({len([t for t in tag_index if t in POOL_A])} main-tags + {len([t for t in tag_index if t not in POOL_A])} sub-tags)\n"
    log_entry += f"- **Topics indexed:** {len(topic_index)}\n"
    log_entry += f"- **Orphans deleted:** {len(orphaned_tags)} tag indexes + {len(orphaned_topics)} topic indexes\n"
    log_entry += f"- **Invalid tags found:** {len(invalid_tags_found)}\n"
    log_entry += f"- **Errors:** {errors} files skipped due to invalid frontmatter\n"
    
    with open(MEMORY_FILE, 'a', encoding='utf-8') as f:
        f.write(log_entry)

    return {
        'scanned': len(files_data),
        'concepts': len([f for f in files_data if f['type']=='concept']),
        'sources': len([f for f in files_data if f['type']=='source']),
        'tags': len(tag_index),
        'topics': len(topic_index),
        'orphans_tags': len(orphaned_tags),
        'orphans_topics': len(orphaned_topics),
        'invalid_tags': len(invalid_tags_found),
        'errors': errors
    }

if __name__ == "__main__":
    result = run_indexing()
    print(result)
