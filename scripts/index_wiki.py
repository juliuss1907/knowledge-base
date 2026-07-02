import os
import re
from datetime import datetime
from collections import defaultdict

# Paths
BASE_DIR = "/home/julius/knowledge-base"
SOURCES_DIR = os.path.join(BASE_DIR, "wiki/sources")
CONCEPTS_DIR = os.path.join(BASE_DIR, "wiki/concepts")
TAG_INDEX_DIR = os.path.join(BASE_DIR, "wiki/tag")
TOPIC_INDEX_DIR = os.path.join(BASE_DIR, "wiki/topic")
TAGS_FILE = os.path.join(BASE_DIR, "TAGS.md")
TAG_MASTER_FILE = os.path.join(BASE_DIR, "wiki/tag/tag.md")
MEMORY_FILE = os.path.join(BASE_DIR, ".openclaw/MEMORY.md")

def parse_frontmatter(content):
    match = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
    if not match:
        return None
    
    yaml_text = match.group(1)
    data = {}
    for line in yaml_text.split('\n'):
        if ':' in line:
            key, val = line.split(':', 1)
            key = key.strip()
            val = val.strip()
            if val.startswith('[') and val.endswith(']'):
                # Simple list parsing
                items = val[1:-1].split(',')
                val = [i.strip().strip("'").strip('"') for i in items if i.strip()]
            data[key] = val
    return data

def load_taxonomy():
    with open(TAGS_FILE, 'r', encoding='utf-8') as f:
        content = f.read()
    
    main_tags = {}
    sub_tags = {}
    
    current_pool = None
    for line in content.split('\n'):
        if '## 2. Pool A' in line:
            current_pool = 'A'
            print("Entering Pool A")
            continue
        elif '## 3. Pool B' in line:
            current_pool = 'B'
            print("Entering Pool B")
            continue
        elif line.startswith('##'):
            current_pool = None
            continue
            
        if current_pool and '|' in line and not line.startswith('|---'):
            parts = [p.strip() for p in line.split('|')]
            found_tag = None
            for part in parts:
                if part.startswith('#'):
                    found_tag = part.strip('#')
                    idx = parts.index(part)
                    if idx + 1 < len(parts):
                        desc = parts[idx+1]
                        if current_pool == 'A':
                            main_tags[found_tag] = desc
                        else:
                            sub_tags[found_tag] = desc
                    break
                    
    print(f"Loaded Main Tags: {list(main_tags.keys())}")
    print(f"Loaded Sub Tags: {list(sub_tags.keys())}")
    return main_tags, sub_tags

def derive_title(slug):
    return ' '.join(word.capitalize() for word in slug.split('-'))

def main():
    print("Starting Index Agent...")
    main_tags_tax, sub_tags_tax = load_taxonomy()
    all_allowed_tags = set(main_tags_tax.keys()) | set(sub_tags_tax.keys())
    
    files_data = []
    errors = 0
    warnings = 0
    invalid_tags_found = []

    # Scan sources and concepts
    for directory, dtype in [(SOURCES_DIR, 'source'), (CONCEPTS_DIR, 'concept')]:
        if not os.path.exists(directory):
            continue
        for filename in sorted(os.listdir(directory)):
            if filename.endswith('.md'):
                path = os.path.join(directory, filename)
                with open(path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    fm = parse_frontmatter(content)
                    if not fm:
                        print(f"[WARNING] {path}: No frontmatter found")
                        warnings += 1
                        continue
                    
                    main_tag = fm.get('main_tag')
                    sub_tags = fm.get('sub_tags', [])
                    topic = fm.get('topic')
                    
                    if not main_tag or not topic:
                        print(f"[ERROR] {path}: Missing required fields (main_tag or topic)")
                        errors += 1
                        continue
                    
                    if not isinstance(sub_tags, list):
                        sub_tags = []

                    is_invalid_main = False
                    if main_tag not in main_tags_tax:
                        print(f"[INVALID TAG] {path}: main_tag={main_tag}")
                        invalid_tags_found.append((path, main_tag))
                        is_invalid_main = True
                    
                    invalid_subs = []
                    for st in sub_tags:
                        if st not in sub_tags_tax:
                            print(f"[INVALID TAG] {path}: sub_tag={st}")
                            invalid_tags_found.append((path, st))
                            invalid_subs.append(st)
                    
                    slug = filename[:-3]
                    files_data.append({
                        'path': path,
                        'slug': slug,
                        'type': dtype,
                        'main_tag': main_tag,
                        'sub_tags': sub_tags,
                        'topic': topic,
                        'invalid_main': is_invalid_main,
                        'invalid_subs': invalid_subs
                    })

    tag_index = defaultdict(lambda: {'concepts': [], 'sources': []})
    topic_index = defaultdict(lambda: {'concepts': [], 'sources': []})
    
    for f in files_data:
        if not f['invalid_main']:
            tag = f['main_tag']
            tag_index[tag][f'{"concepts" if f["type"] == "concept" else "sources"}'].append(f)
        for st in f['sub_tags']:
            if st not in f['invalid_subs']:
                tag = st
                tag_index[tag][f'{"concepts" if f["type"] == "concept" else "sources"}'].append(f)
        topic = f['topic']
        topic_index[topic][f'{"concepts" if f["type"] == "concept" else "sources"}'].append(f)

    co_occurrence = defaultdict(int)
    for f in files_data:
        all_tags = []
        if not f['invalid_main']: all_tags.append(f['main_tag'])
        for st in f['sub_tags']:
            if st not in f['invalid_subs']: all_tags.append(st)
        all_tags = sorted(list(set(all_tags)))
        for i in range(len(all_tags)):
            for j in range(i + 1, len(all_tags)):
                co_occurrence[tuple(sorted([all_tags[i], all_tags[j]]))] += 1

    topic_overlap = defaultdict(int)
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

    today = datetime.now().strftime('%Y-%m-%d')
    os.makedirs(TAG_INDEX_DIR, exist_ok=True)
    for tag, data in tag_index.items():
        pairs = []
        for (t1, t2), count in co_occurrence.items():
            if tag == t1: pairs.append((t2, count))
            elif tag == t2: pairs.append((t1, count))
        top_5 = sorted(pairs, key=lambda x: -x[1])[:5]
        all_items = []
        for f in data['concepts']:
            all_items.append((f['slug'], derive_title(f['slug']), 'concept'))
        for f in data['sources']:
            all_items.append((f['slug'], derive_title(f['slug'].replace('src_', '')), 'source'))
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

    os.makedirs(TOPIC_INDEX_DIR, exist_ok=True)
    for topic, data in topic_index.items():
        related = []
        for (t1, t2), count in topic_overlap.items():
            if topic == t1: related.append((t2, count))
            elif topic == t2: related.append((t1, count))
        top_5_rel = sorted(related, key=lambda x: -x[1])[:5]
        content = f"---\ntype: index\nscope: topic\nparent: \"[[topic]]\"\ntopic: {topic}\nauto_generated: true\nlast_updated: {today}\n---\n\n# Topic: {topic}\n\nAuto-generated index of all content with topic `{topic}`.\n\nLast updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n---\n\n## Concepts ({len(data['concepts'])})\n\n"
        for f in data['concepts']:
            subs = ', '.join([f"#{s}" for s in f['sub_tags']])
            content += f"- [[{f['slug']}]] — main: #{f['main_tag']}, sub: [{subs}]\n"
        content += f"\n## Sources ({len(data['sources'])})\n\n"
        for f in data['sources']:
            subs = ', '.join([f"#{s}" for s in f['sub_tags']])
            content += f"- [[{f['slug']}]] — main: #{f['main_tag']}, sub: [{subs}]\n"
        if top_5_rel:
            content += "\n## Related topics\n\n"
            content += f"Topics that share concepts/sources with `{topic}`:\n"
            for other, count in top_5_rel:
                content += f"- `{other}` ({count} shared files)\n"
        with open(os.path.join(TOPIC_INDEX_DIR, f"{topic}.md"), 'w', encoding='utf-8') as f:
            f.write(content)

    if os.path.exists(TAG_MASTER_FILE):
        with open(TAG_MASTER_FILE, 'r', encoding='utf-8') as f:
            master_content = f.read()
        for tag in all_allowed_tags:
            if f"- [[{tag}]]" not in master_content:
                desc = main_tags_tax.get(tag) or sub_tags_tax.get(tag) or "[description]"
                pool = "Main Tags (Pool A)" if tag in main_tags_tax else "Sub Tags (Pool B)"
                pattern = f"### {pool}"
                if pattern in master_content:
                    master_content = re.sub(rf"({pattern})", rf"\1\n- [[{tag}]] — {desc}", master_content)
        total_tags_files = len([f for f in os.listdir(TAG_INDEX_DIR) if f.endswith('.md') and f != 'tag.md'])
        main_count = len(main_tags_tax)
        sub_count = total_tags_files - main_count
        usage = []
        for tag_file in os.listdir(TAG_INDEX_DIR):
            if tag_file.endswith('.md') and tag_file != 'tag.md':
                tag = tag_file[:-3]
                with open(os.path.join(TAG_INDEX_DIR, tag_file), 'r', encoding='utf-8') as tf:
                    count = len(re.findall(r'^\- \[\[', tf.read(), re.MULTILINE))
                    usage.append((tag, count))
        top_3 = sorted(usage, key=lambda x: -x[1])[:3]
        most_used_str = ", ".join([f"#{t} ({c})" for t, c in top_3])
        stats_block = f"## Stats\n\n- Total tags: {total_tags_files}\n- Main tags: {main_count}\n- Sub tags: {sub_count}\n- Most used: {most_used_str}\n- Last updated: {today}"
        if "## Stats" in master_content:
            master_content = re.sub(r"## Stats.*?## Items", f"{stats_block}\n\n## Items", master_content, flags=re.DOTALL)
        with open(TAG_MASTER_FILE, 'w', encoding='utf-8') as f:
            f.write(master_content)

    orphaned_tags = []
    existing_tag_files = [f[:-3] for f in os.listdir(TAG_INDEX_DIR) if f.endswith('.md') and f != 'tag']
    current_tags = set(tag_index.keys())
    for et in existing_tag_files:
        if et not in current_tags:
            orphaned_tags.append(et)
            os.remove(os.path.join(TAG_INDEX_DIR, f"{et}.md"))
    orphaned_topics = []
    existing_topic_files = [f[:-3] for f in os.listdir(TOPIC_INDEX_DIR) if f.endswith('.md')]
    current_topics = set(topic_index.keys())
    for et in existing_topic_files:
        if et not in current_topics:
            orphaned_topics.append(et)
            os.remove(os.path.join(TOPIC_INDEX_DIR, f"{et}.md"))

    with open(MEMORY_FILE, 'a', encoding='utf-8') as f:
        f.write(f"\n## {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} — Indexed\n\n")
        f.write(f"- **Scanned:** {len([f for f in files_data if f['type'] == 'concept'])} concepts + {len([f for f in files_data if f['type'] == 'source'])} sources = {len(files_data)} total files\n")
        f.write(f"- **Tags indexed:** {len(tag_index)} ({len(main_tags_tax)} main-tags + {len(tag_index)-len(main_tags_tax)} sub-tags)\n")
        f.write(f"- **Topics indexed:** {len(topic_index)}\n")
        f.write(f"- **Orphans deleted:** {len(orphaned_tags)} tag indexes + {len(orphaned_topics)} topic indexes\n")
        f.write(f"- **Invalid tags found:** {len(invalid_tags_found)}\n")
        f.write(f"- **Errors:** {errors} files skipped due to invalid frontmatter\n")
    print("Indexing complete.")

if __name__ == "__main__":
    main()
