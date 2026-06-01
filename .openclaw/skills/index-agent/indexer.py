import os
import yaml
import re
from datetime import datetime
from collections import defaultdict

# Configuration
ROOT = "/home/julius/knowledge-base"
SOURCES_DIR = os.path.join(ROOT, "wiki/sources")
CONCEPTS_DIR = os.path.join(ROOT, "wiki/concepts")
TAG_INDEX_DIR = os.path.join(ROOT, "wiki/tag")
TOPIC_INDEX_DIR = os.path.join(ROOT, "wiki/topic")
TAGS_FILE = os.path.join(ROOT, "TAGS.md")
TAG_MASTER_FILE = os.path.join(TAG_INDEX_DIR, "tag.md")
MEMORY_FILE = os.path.join(ROOT, ".openclaw/MEMORY.md")

def derive_title(slug):
    # Remove src_ prefix if present
    clean_slug = slug.replace('src_', '')
    return ' '.join(word.capitalize() for word in clean_slug.split('-'))

def load_taxonomy():
    with open(TAGS_FILE, 'r', encoding='utf-8') as f:
        content = f.read()
    
    main_tags = {}
    sub_tags = {}
    
    # Regex to find table rows in TAGS.md
    # | #tag | Description |
    rows = re.findall(r'\| #(\w+) \| ([^|]+) \|', content)
    
    # We need to distinguish Pool A and Pool B. 
    # The file has sections "2. Pool A" and "3. Pool B".
    parts = content.split("## 3. Pool B")
    
    pool_a_content = parts[0]
    pool_b_content = parts[1] if len(parts) > 1 else ""
    
    for tag, desc in re.findall(r'\| #(\w+) \| ([^|]+) \|', pool_a_content):
        main_tags[tag] = desc.strip()
        
    for tag, desc in re.findall(r'\| #(\w+) \| ([^|]+) \|', pool_b_content):
        sub_tags[tag] = desc.strip()
        
    return main_tags, sub_tags

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

def run_indexer():
    main_tags_tax, sub_tags_tax = load_taxonomy()
    allowed_main = set(main_tags_tax.keys())
    allowed_sub = set(sub_tags_tax.keys())
    
    files_data = []
    invalid_tags_found = []
    errors_count = 0
    
    # Scan wiki
    for folder in [SOURCES_DIR, CONCEPTS_DIR]:
        if not os.path.exists(folder): continue
        for filename in sorted(os.listdir(folder)):
            if not filename.endswith(".md"): continue
            path = os.path.join(folder, filename)
            fm = parse_frontmatter(path)
            
            if not fm:
                errors_count += 1
                continue
            
            # Validation
            main_tag = fm.get('main_tag')
            sub_tags = fm.get('sub_tags', [])
            topic = fm.get('topic')
            
            if not main_tag or not topic:
                errors_count += 1
                continue
                
            # Tag validation
            if main_tag not in allowed_main:
                invalid_tags_found.append(f"{filename}: main_tag {main_tag}")
                
            for st in sub_tags:
                if st not in allowed_sub:
                    invalid_tags_found.append(f"{filename}: sub_tag {st}")
            
            slug = filename[:-3]
            files_data.append({
                'path': path,
                'filename': filename,
                'slug': slug,
                'type': 'concept' if 'concepts' in path else 'source',
                'main_tag': main_tag,
                'sub_tags': sub_tags,
                'topic': topic
            })

    # Tag grouping
    tag_index = defaultdict(lambda: {'concepts': [], 'sources': []})
    for f in files_data:
        # Main tag
        if f['main_tag'] in allowed_main:
            target = tag_index[f['main_tag']]
            if f['type'] == 'concept': target['concepts'].append(f)
            else: target['sources'].append(f)
            
        # Sub tags
        for st in f['sub_tags']:
            if st in allowed_sub:
                target = tag_index[st]
                if f['type'] == 'concept': target['concepts'].append(f)
                else: target['sources'].append(f)

    # Topic grouping
    topic_index = defaultdict(lambda: {'concepts': [], 'sources': []})
    for f in files_data:
        target = topic_index[f['topic']]
        if f['type'] == 'concept': target['concepts'].append(f)
        else: target['sources'].append(f)

    # Co-occurrence
    co_occurrence = defaultdict(int)
    for f in files_data:
        all_tags = [f['main_tag']] + f['sub_tags']
        all_tags = [t for t in all_tags if t in allowed_main or t in allowed_sub]
        for i in range(len(all_tags)):
            for j in range(i + 1, len(all_tags)):
                pair = tuple(sorted([all_tags[i], all_tags[j]]))
                co_occurrence[pair] += 1

    # Write Tag Indexes
    today = datetime.now().strftime('%Y-%m-%d')
    for tag, data in tag_index.items():
        # Sort
        data['concepts'].sort(key=lambda x: x['slug'])
        data['sources'].sort(key=lambda x: x['slug'])
        
        # Co-occurring
        related = []
        for (t1, t2), count in co_occurrence.items():
            if tag == t1: related.append((t2, count))
            elif tag == t2: related.append((t1, count))
        related.sort(key=lambda x: -x[1])[:5]
        
        content = f"---\ntype: index\nlevel: 3\nscope: tag\nparent: [[tag]]\ntag: {tag}\nauto_generated: true\nlast_updated: {today}\n---\n\n# Tag: #{tag}\n\n## Parent\n\n- [[tag]]\n\n## Stats\n\n- Total files: {len(data['concepts']) + len(data['sources'])}\n- Sources: {len(data['sources'])}\n- Concepts: {len(data['concepts'])}\n- Last updated: {today}\n\n## Files with this tag\n\n"
        
        all_items = []
        for f in data['concepts']: all_items.append((f['slug'], derive_title(f['slug']), 'concept'))
        for f in data['sources']: all_items.append((f['slug'], derive_title(f['slug']), 'source'))
        all_items.sort(key=lambda x: x[0])
        
        for slug, title, ftype in all_items:
            content += f"- [[{slug}]] — {title} ({ftype})\n"
            
        if related:
            content += "\n## Co-occurring tags\n\n"
            for rt, rc in related[:5]:
                unit = "co-occurrence" if rc == 1 else "co-occurrences"
                content += f"- [[{rt}]] — {rc} {unit}\n"
        
        with open(os.path.join(TAG_INDEX_DIR, f"{tag}.md"), 'w', encoding='utf-8') as f:
            f.write(content)

    # Write Topic Indexes
    for topic, data in topic_index.items():
        data['concepts'].sort(key=lambda x: x['slug'])
        data['sources'].sort(key=lambda x: x['slug'])
        
        content = f"# Topic: {topic}\n\nAuto-generated index of all content with topic `{topic}`.\n\nLast updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n---\n\n## Concepts ({len(data['concepts'])})\n\n"
        for f in data['concepts']:
            subs = ', '.join([f"#{s}" for s in f['sub_tags']])
            content += f"- [[{f['slug']}]] — main: #{f['main_tag']}, sub: [{subs}]\n"
        
        content += f"\n## Sources ({len(data['sources'])})\n\n"
        for f in data['sources']:
            subs = ', '.join([f"#{s}" for s in f['sub_tags']])
            content += f"- [[{f['slug']}]] — main: #{f['main_tag']}, sub: [{subs}]\n"
            
        with open(os.path.join(TOPIC_INDEX_DIR, f"{topic}.md"), 'w', encoding='utf-8') as f:
            f.write(content)

    # Update tag.md
    if os.path.exists(TAG_MASTER_FILE):
        with open(TAG_MASTER_FILE, 'r', encoding='utf-8') as f:
            master_content = f.read()
        
        # Update stats
        all_tag_files = [f for f in os.listdir(TAG_INDEX_DIR) if f.endswith(".md") and f != "tag.md"]
        total_tags = len(all_tag_files)
        
        tag_counts = {}
        for tf in all_tag_files:
            tag = tf[:-3]
            with open(os.path.join(TAG_INDEX_DIR, tf), 'r', encoding='utf-8') as f:
                tag_counts[tag] = len(re.findall(r'^\- \[\[', f.read(), re.MULTILINE))
        
        top_3 = sorted(tag_counts.items(), key=lambda x: -x[1])[:3]
        most_used = ', '.join([f"#{t} ({c})" for t, c in top_3])
        
        stats_section = f"## Stats\n\n- Total tags: {total_tags}\n- Main tags: {len(main_tags_tax)}\n- Sub tags: {len(sub_tags_tax)}\n- Most used: {most_used}\n- Last updated: {today}"
        
        # Replace stats section
        if "## Stats" in master_content:
            master_content = re.sub(r'## Stats.*?## Items', f'{stats_section}\n\n## Items', master_content, flags=re.DOTALL)
        else:
            master_content = master_content.replace("## Items", f"{stats_section}\n\n## Items")

        # Update items
        for tag, desc in {**main_tags_tax, **sub_tags_tax}.items():
            entry = f"- [[{tag}]] — {desc}"
            if entry not in master_content:
                pool = "Main Tags (Pool A)" if tag in main_tags_tax else "Sub Tags (Pool B)"
                master_content = master_content.replace(f"### {pool}", f"### {pool}\n{entry}")

        with open(TAG_MASTER_FILE, 'w', encoding='utf-8') as f:
            f.write(master_content)

    # Cleanup orphans
    deleted_tags = []
    current_tags = set(tag_index.keys())
    for tf in os.listdir(TAG_INDEX_DIR):
        if tf == "tag.md" or not tf.endswith(".md"): continue
        tag = tf[:-3]
        if tag not in current_tags:
            os.remove(os.path.join(TAG_INDEX_DIR, tf))
            deleted_tags.append(tag)
            
    deleted_topics = []
    current_topics = set(topic_index.keys())
    for tf in os.listdir(TOPIC_INDEX_DIR):
        if not tf.endswith(".md"): continue
        topic = tf[:-3]
        if topic not in current_topics:
            os.remove(os.path.join(TOPIC_INDEX_DIR, tf))
            deleted_topics.append(topic)

    # Result
    return {
        'scanned': len(files_data),
        'concepts': len([f for f in files_data if f['type'] == 'concept']),
        'sources': len([f for f in files_data if f['type'] == 'source']),
        'tags': len(tag_index),
        'main_tags': len(main_tags_tax),
        'sub_tags': len(sub_tags_tax),
        'topics': len(topic_index),
        'deleted_tags': len(deleted_tags),
        'deleted_topics': len(deleted_topics),
        'invalid_tags': len(invalid_tags_found),
        'errors': errors_count,
        'invalid_details': invalid_tags_found
    }

if __name__ == "__main__":
    res = run_indexer()
    print(res)
