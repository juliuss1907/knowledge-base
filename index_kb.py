import os
import re
from datetime import datetime
from collections import defaultdict

# --- Configuration ---
BASE_DIR = "/home/julius/knowledge-base"
TAGS_FILE = os.path.join(BASE_DIR, "TAGS.md")
SOURCES_DIR = os.path.join(BASE_DIR, "wiki/sources")
CONCEPTS_DIR = os.path.join(BASE_DIR, "wiki/concepts")
TAG_INDEX_DIR = os.path.join(BASE_DIR, "wiki/tag")
TOPIC_INDEX_DIR = os.path.join(BASE_DIR, "wiki/topic")
MASTER_TAG_FILE = os.path.join(BASE_DIR, "wiki/tag/tag.md")
MEMORY_FILE = os.path.join(BASE_DIR, ".openclaw/MEMORY.md")

def parse_tags_taxonomy():
    with open(TAGS_FILE, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    print("DEBUG: First 20 lines of TAGS.md:")
    for i in range(min(20, len(lines))):
        print(f"{i}: {repr(lines[i])}")

    main_tags = {}
    sub_tags = {}
    
    current_pool = None
    for line in lines:
        line_stripped = line.strip()
        if '## 2. Pool A' in line:
            current_pool = 'A'
            continue
        elif '## 3. Pool B' in line:
            current_pool = 'B'
            continue
        elif line_stripped.startswith('##'):
            current_pool = None
            continue
            
        if current_pool and line_stripped.startswith('| #'):
            parts = [p.strip() for p in line_stripped.split('|')]
            if len(parts) >= 3:
                tag = parts[1].replace('#', '').replace('`', '').strip()
                desc = parts[2]
                if current_pool == 'A':
                    main_tags[tag] = desc
                else:
                    sub_tags[tag] = desc
                    
    print(f"DEBUG: main_tags_tax={list(main_tags.keys())}")
    print(f"DEBUG: sub_tags_tax={list(sub_tags.keys())}")
    return main_tags, sub_tags

def parse_frontmatter(path):
    try:
        with open(path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        if not lines or not lines[0].startswith('---'):
            return None
            
        fm_lines = []
        for i in range(1, len(lines)):
            if lines[i].startswith('---'):
                break
            fm_lines.append(lines[i])
        
        fm = {}
        for line in fm_lines:
            if ':' in line:
                k, v = line.split(':', 1)
                k = k.strip()
                v = v.strip()
                # Basic list parsing for sub_tags: [tag1, tag2]
                if v.startswith('[') and v.endswith(']'):
                    v = [t.strip().strip("'\"") for t in v[1:-1].split(',')]
                fm[k] = v
        return fm
    except Exception:
        return None

def derive_title(slug):
    # Remove 'src_' prefix for sources
    clean_slug = slug.replace('src_', '')
    return ' '.join(word.capitalize() for word in clean_slug.split('-'))

def main():
    main_tags_tax, sub_tags_tax = parse_tags_taxonomy()
    allowed_main = set(main_tags_tax.keys())
    allowed_sub = set(sub_tags_tax.keys())
    
    files_data = []
    
    # Scan sources and concepts
    for folder, ftype in [(SOURCES_DIR, 'source'), (CONCEPTS_DIR, 'concept')]:
        if not os.path.exists(folder): continue
        for filename in sorted(os.listdir(folder)):
            if filename.endswith('.md'):
                path = os.path.join(folder, filename)
                fm = parse_frontmatter(path)
                if not fm:
                    print(f"[WARNING] {path}: No frontmatter")
                    continue
                
                # Basic validation of required fields
                main_tag = fm.get('main_tag')
                sub_tags = fm.get('sub_tags')
                topic = fm.get('topic')
                
                if not all([main_tag, sub_tags, topic]):
                    print(f"[ERROR] {path}: Missing required frontmatter fields")
                    continue
                
                if isinstance(sub_tags, str): sub_tags = [sub_tags]
                
                # Tag validation
                invalid_main = main_tag not in allowed_main
                invalid_subs = [t for t in sub_tags if t not in allowed_sub]
                
                files_data.append({
                    'path': path,
                    'slug': filename[:-3],
                    'type': ftype,
                    'main_tag': main_tag,
                    'sub_tags': sub_tags,
                    'topic': topic,
                    'invalid_main': invalid_main,
                    'invalid_subs': invalid_subs
                })

    # Build Tag Index
    tag_index = defaultdict(lambda: {'concepts': [], 'sources': []})
    for f in files_data:
        # Main tag
        if not f['invalid_main']:
            tag = f['main_tag']
            target = 'concepts' if f['type'] == 'concept' else 'sources'
            tag_index[tag][target].append(f)
        
        # Sub tags
        for st in f['sub_tags']:
            if st not in f['invalid_subs']:
                tag = st
                target = 'concepts' if f['type'] == 'concept' else 'sources'
                tag_index[tag][target].append(f)

    # Sort files in each tag index
    for tag in tag_index:
        tag_index[tag]['concepts'].sort(key=lambda x: x['slug'])
        tag_index[tag]['sources'].sort(key=lambda x: x['slug'])

    # Co-occurrence
    co_occurrence = defaultdict(int)
    for f in files_data:
        all_tags = [f['main_tag']] + f['sub_tags']
        all_tags = sorted(list(set(all_tags))) # Unique
        for i in range(len(all_tags)):
            for j in range(i + 1, len(all_tags)):
                co_occurrence[tuple(sorted([all_tags[i], all_tags[j]]))] += 1

    # Build Topic Index
    topic_index = defaultdict(lambda: {'concepts': [], 'sources': []})
    for f in files_data:
        topic = f['topic']
        target = 'concepts' if f['type'] == 'concept' else 'sources'
        topic_index[topic][target].append(f)
        
    for topic in topic_index:
        topic_index[topic]['concepts'].sort(key=lambda x: x['slug'])
        topic_index[topic]['sources'].sort(key=lambda x: x['slug'])

    # Topic Overlap
    topic_overlap = defaultdict(int)
    topic_list = list(topic_index.keys())
    for i in range(len(topic_list)):
        t1 = topic_list[i]
        f1 = set([f['path'] for f in topic_index[t1]['concepts'] + topic_index[t1]['sources']])
        for j in range(i + 1, len(topic_list)):
            t2 = topic_list[j]
            f2 = set([f['path'] for f in topic_index[t2]['concepts'] + topic_index[t2]['sources']])
            shared = len(f1 & f2)
            if shared > 0:
                topic_overlap[tuple(sorted([t1, t2]))] = shared

    # Write Tag Indexes
    today = datetime.now().strftime('%Y-%m-%d')
    os.makedirs(TAG_INDEX_DIR, exist_ok=True)
    for tag, data in tag_index.items():
        # Top 5 co-occurring
        pairs = []
        for (t1, t2), count in co_occurrence.items():
            if tag == t1: pairs.append((t2, count))
            elif tag == t2: pairs.append((t1, count))
        top_5 = sorted(pairs, key=lambda x: -x[1])[:5]
        
        all_items = []
        for f in data['concepts']: all_items.append((f['slug'], derive_title(f['slug']), 'concept'))
        for f in data['sources']: all_items.append((f['slug'], derive_title(f['slug']), 'source'))
        all_items.sort()

        content = f"---\ntype: index\nlevel: 3\nscope: tag\nparent: [[tag]]\ntag: {tag}\nauto_generated: true\nlast_updated: {today}\n---\n\n# Tag: #{tag}\n\n## Parent\n\n- [[tag]]\n\n## Stats\n\n- Total files: {len(all_items)}\n- Sources: {len(data['sources'])}\n- Concepts: {len(data['concepts'])}\n- Last updated: {today}\n\n## Files with this tag\n\n"
        for slug, title, ftype in all_items:
            content += f"- [[{slug}]] — {title} ({ftype})\n"
        
        if top_5:
            content += "\n## Co-occurring tags\n\n"
            for other, count in top_5:
                unit = "co-occurrence" if count == 1 else "co-occurrences"
                content += f"- [[{other}]] — {count} {unit}\n"
        
        with open(os.path.join(TAG_INDEX_DIR, f"{tag}.md"), 'w', encoding='utf-8') as f:
            f.write(content)

    # Write Topic Indexes
    os.makedirs(TOPIC_INDEX_DIR, exist_ok=True)
    for topic, data in topic_index.items():
        # Top 5 related
        related = []
        for (t1, t2), count in topic_overlap.items():
            if topic == t1: related.append((t2, count))
            elif topic == t2: related.append((t1, count))
        top_5 = sorted(related, key=lambda x: -x[1])[:5]
        
        content = f"# Topic: {topic}\n\nAuto-generated index of all content with topic `{topic}`.\n\nLast updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n---\n\n## Concepts ({len(data['concepts'])})\n\n"
        for f in data['concepts']:
            subs = ', '.join([f"#{s}" for s in f['sub_tags']])
            content += f"- [[{f['slug']}]] — main: #{f['main_tag']}, sub: [{subs}]\n"
        
        content += f"\n## Sources ({len(data['sources'])})\n\n"
        for f in data['sources']:
            subs = ', '.join([f"#{s}" for s in f['sub_tags']])
            content += f"- [[{f['slug']}]] — main: #{f['main_tag']}, sub: [{subs}]\n"
            
        if top_5:
            content += "\n## Related topics\n\nTopics that share concepts/sources with `{topic}`:\n"
            for other, count in top_5:
                content += f"- `{other}` ({count} shared files)\n"
                
        with open(os.path.join(TOPIC_INDEX_DIR, f"{topic}.md"), 'w', encoding='utf-8') as f:
            f.write(content)

    # Update Master Tag Index (tag.md)
    if os.path.exists(MASTER_TAG_FILE):
        with open(MASTER_TAG_FILE, 'r', encoding='utf-8') as f:
            master_content = f.read()
        
        # Update Items
        for tag in tag_index:
            if f"- [[{tag}]]" not in master_content:
                pool = "Main Tags (Pool A)" if tag in main_tags_tax else "Sub Tags (Pool B)"
                desc = main_tags_tax.get(tag) or sub_tags_tax.get(tag, "[description]")
                pattern = f"### {pool}"
                if pattern in master_content:
                    master_content = master_content.replace(pattern, f"{pattern}\n- [[{tag}]] — {desc}")

        # Update Stats
        total_tags = len(tag_index)
        main_count = len(main_tags_tax)
        sub_count = total_tags - main_count
        
        # Top 3 tags
        tag_counts = []
        for tag, data in tag_index.items():
            tag_counts.append((len(data['concepts']) + len(data['sources']), tag))
        tag_counts.sort(key=lambda x: -x[0])
        top_3_str = ', '.join([f"#{t} ({c})" for c, t in tag_counts[:3]])
        
        stats_block = f"## Stats\n\n- Total tags: {total_tags}\n- Main tags: {main_count}\n- Sub tags: {sub_count}\n- Most used: {top_3_str}\n- Last updated: {today}"
        
        # Replace stats section
        if "## Stats" in master_content and "## Items" in master_content:
            start = master_content.find("## Stats")
            end = master_content.find("## Items")
            master_content = master_content[:start] + stats_block + "\n\n" + master_content[end:]
        
        with open(MASTER_TAG_FILE, 'w', encoding='utf-8') as f:
            f.write(master_content)

    # Cleanup Orphans
    current_tags = set(tag_index.keys())
    current_topics = set(topic_index.keys())
    
    orphaned_tags = 0
    if os.path.exists(TAG_INDEX_DIR):
        for filename in os.listdir(TAG_INDEX_DIR):
            if filename == 'tag.md': continue
            tag = filename[:-3]
            if tag not in current_tags:
                os.remove(os.path.join(TAG_INDEX_DIR, filename))
                orphaned_tags += 1
            
    orphaned_topics = 0
    if os.path.exists(TOPIC_INDEX_DIR):
        for filename in os.listdir(TOPIC_INDEX_DIR):
            topic = filename[:-3]
            if topic not in current_topics:
                os.remove(os.path.join(TOPIC_INDEX_DIR, filename))
                orphaned_topics += 1

    # Summary
    invalid_tags_count = sum(1 for f in files_data if f['invalid_main'] or f['invalid_subs'])
    errors_count = 0 # simplified for this script
    
    print(f"DONE|{len(files_data)}|{len(tag_index)}|{len(main_tags_tax)}|{len(tag_index)-len(main_tags_tax)}|{len(topic_index)}|{orphaned_tags}|{orphaned_topics}|{invalid_tags_count}|{errors_count}")

if __name__ == "__main__":
    main()
