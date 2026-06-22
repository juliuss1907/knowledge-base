import os
import yaml
import re
from datetime import datetime
from pathlib import Path
from collections import defaultdict

# Configuration
WORKSPACE = Path("/home/julius/knowledge-base")
RAW_SOURCES = WORKSPACE / "wiki/sources"
RAW_CONCEPTS = WORKSPACE / "wiki/concepts"
TAG_INDEX_DIR = WORKSPACE / "wiki/tag"
TOPIC_INDEX_DIR = WORKSPACE / "wiki/topic"
TAGS_FILE = WORKSPACE / "TAGS.md"
MASTER_TAG_FILE = TAG_INDEX_DIR / "tag.md"
MEMORY_FILE = WORKSPACE / ".openclaw/MEMORY.md"

def derive_title(slug):
    clean_slug = slug.replace('src_', '')
    return ' '.join(word.capitalize() for word in clean_slug.split('-'))

def load_tags_taxonomy():
    with open(TAGS_FILE, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Robust regex for table rows: | #tag | description |
    # Matches | followed by optional space, #, then word chars, then space/pipe
    row_pattern = r'\|\s*#(\w+)\s*\|\s*([^|]+)\s*\|'
    
    # Split by Pool headers
    parts = re.split(r'## (?:2\.|3\.) Pool [AB]', content)
    if len(parts) < 3:
        return {}, {}
        
    pool_a_content = parts[1]
    pool_b_content = parts[2]
    
    main_tags = {}
    for tag, desc in re.findall(row_pattern, pool_a_content):
        main_tags[tag] = desc.strip()
        
    sub_tags = {}
    for tag, desc in re.findall(row_pattern, pool_b_content):
        sub_tags[tag] = desc.strip()
        
    return main_tags, sub_tags

def parse_frontmatter(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    match = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
    if not match: return None
    try:
        return yaml.safe_load(match.group(1))
    except yaml.YAMLError:
        return None

def run_indexing():
    main_pool, sub_pool = load_tags_taxonomy()
    all_allowed = {**main_pool, **sub_pool}
    
    # Debugging taxonomy
    print(f"Loaded taxonomy: {len(main_pool)} main, {len(sub_pool)} sub tags.")

    wiki_files = []
    errors = 0
    warnings = 0
    invalid_tags_found = []

    for folder in [RAW_SOURCES, RAW_CONCEPTS]:
        if not folder.exists(): continue
        for f in sorted(folder.glob("*.md")):
            fm = parse_frontmatter(f)
            if not fm:
                warnings += 1
                continue
            
            if 'main_tag' not in fm or 'topic' not in fm:
                errors += 1
                continue
            
            main = fm['main_tag']
            subs = fm.get('sub_tags', [])
            if not isinstance(subs, list): subs = [subs] if subs else []
            
            file_info = {
                'path': str(f.relative_to(WORKSPACE)),
                'slug': f.stem,
                'type': 'concept' if 'wiki/concepts' in str(f.relative_to(WORKSPACE)) else 'source',
                'main_tag': main,
                'sub_tags': subs,
                'topic': fm['topic'],
                'invalid_main': False,
                'invalid_subs': []
            }
            
            if main not in main_pool:
                file_info['invalid_main'] = True
                invalid_tags_found.append(f"{f.name} (#{main})")
            
            for s in subs:
                if s not in sub_pool:
                    file_info['invalid_subs'].append(s)
                    invalid_tags_found.append(f"{f.name} (#{s})")
            
            wiki_files.append(file_info)

    tag_index = defaultdict(lambda: {'concepts': [], 'sources': []})
    for f in wiki_files:
        if not f['invalid_main']:
            tag_index[f['main_tag']][f['type'] + 's'].append(f)
        for s in f['sub_tags']:
            if s not in f['invalid_subs']:
                tag_index[s][f['type'] + 's'].append(f)

    for tag in tag_index:
        tag_index[tag]['concepts'].sort(key=lambda x: x['slug'])
        tag_index[tag]['sources'].sort(key=lambda x: x['slug'])

    co_occurrence = defaultdict(int)
    for f in wiki_files:
        valid_tags = [t for t in ([f['main_tag']] + f['sub_tags']) if t in all_allowed]
        for i in range(len(valid_tags)):
            for j in range(i + 1, len(valid_tags)):
                pair = tuple(sorted([valid_tags[i], valid_tags[j]]))
                co_occurrence[pair] += 1
                
    tag_co_occur = {}
    for tag in tag_index:
        pairs = [(other, count) for (t1, t2), count in co_occurrence.items() 
                 if tag in (t1, t2) and (other := t2 if t1 == tag else t1)]
        tag_co_occur[tag] = sorted(pairs, key=lambda x: -x[1])[:5]

    topic_index = defaultdict(lambda: {'concepts': [], 'sources': []})
    for f in wiki_files:
        topic_index[f['topic']][f['type'] + 's'].append(f)
    
    for topic in topic_index:
        topic_index[topic]['concepts'].sort(key=lambda x: x['slug'])
        topic_index[topic]['sources'].sort(key=lambda x: x['slug'])

    topic_overlap = defaultdict(int)
    topic_list = list(topic_index.keys())
    for i in range(len(topic_list)):
        t1 = topic_list[i]
        f1 = {f['path'] for f in topic_index[t1]['concepts'] + topic_index[t1]['sources']}
        for j in range(i + 1, len(topic_list)):
            t2 = topic_list[j]
            f2 = {f['path'] for f in topic_index[t2]['concepts'] + topic_index[t2]['sources']}
            shared = len(f1 & f2)
            if shared > 0:
                topic_overlap[tuple(sorted([t1, t2]))] = shared
                
    topic_related = {}
    for topic in topic_index:
        pairs = [(other, count) for (t1, t2), count in topic_overlap.items() 
                 if topic in (t1, t2) and (other := t2 if t1 == topic else t1)]
        topic_related[topic] = sorted(pairs, key=lambda x: -x[1])[:5]

    TAG_INDEX_DIR.mkdir(parents=True, exist_ok=True)
    today = datetime.now().strftime('%Y-%m-%d')
    
    for tag, data in tag_index.items():
        all_items = []
        for f in data['concepts']: all_items.append((f['slug'], derive_title(f['slug']), 'concept'))
        for f in data['sources']: all_items.append((f['slug'], derive_title(f['slug']), 'source'))
        all_items.sort(key=lambda x: x[0])
        
        content = f"---\ntype: index\nlevel: 3\nscope: tag\nparent: [[tag]]\ntag: {tag}\nauto_generated: true\nlast_updated: {today}\n---\n\n# Tag: #{tag}\n\n## Parent\n\n- [[tag]]\n\n## Stats\n\n- Total files: {len(all_items)}\n- Sources: {len(data['sources'])}\n- Concepts: {len(data['concepts'])}\n- Last updated: {today}\n\n## Files with this tag\n\n"
        for slug, title, ftype in all_items:
            content += f"- [[{slug}]] — {title} ({ftype})\n"
        co_occur = tag_co_occur.get(tag, [])
        if co_occur:
            content += "\n## Co-occurring tags\n\n"
            for other, count in co_occur:
                unit = "co-occurrence" if count == 1 else "co-occurrences"
                content += f"- [[{other}]] — {count} {unit}\n"
        with open(TAG_INDEX_DIR / f"{tag}.md", 'w', encoding='utf-8') as f:
            f.write(content)

    TOPIC_INDEX_DIR.mkdir(parents=True, exist_ok=True)
    now_str = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    for topic, data in topic_index.items():
        content = f"# Topic: {topic}\n\nAuto-generated index of all content with topic `{topic}`.\n\nLast updated: {now_str}\n\n---\n\n## Concepts ({len(data['concepts'])})\n\n"
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
        with open(TOPIC_INDEX_DIR / f"{topic}.md", 'w', encoding='utf-8') as f:
            f.write(content)

    if MASTER_TAG_FILE.exists():
        with open(MASTER_TAG_FILE, 'r', encoding='utf-8') as f:
            master_content = f.read()
        for tag in tag_index:
            if f"- [[{tag}]]" not in master_content:
                pool = "Main Tags (Pool A)" if tag in main_pool else "Sub Tags (Pool B)"
                desc = main_pool.get(tag) or sub_pool.get(tag) or "[description]"
                master_content = re.sub(rf"(### {re.escape(pool)})\n", rf"\\1\n- [[{tag}]] — {desc}\n", master_content)

        total_tags = len([f for f in os.listdir(TAG_INDEX_DIR) if f.endswith('.md') and f != 'tag.md'])
        main_count = len(main_pool)
        sub_count = total_tags - main_count
        counts = sorted([(t, len(d['concepts']) + len(d['sources'])) for t, d in tag_index.items()], key=lambda x: -x[1])
        most_used = ", ".join([f"#{t} ({c})" for t, c in counts[:3]])
        stats_block = f"## Stats\n\n- Total tags: {total_tags}\n- Main tags: {main_count}\n- Sub tags: {sub_count}\n- Most used: {most_used}\n- Last updated: {today}\n"
        master_content = re.sub(r'## Stats\n\n.*?(?=## Items|$)', stats_block, master_content, flags=re.DOTALL)
        with open(MASTER_TAG_FILE, 'w', encoding='utf-8') as f:
            f.write(master_content)

    deleted_tags = []
    for f in os.listdir(TAG_INDEX_DIR):
        if f.endswith('.md') and f != 'tag.md':
            tag = f[:-3]
            if tag not in tag_index:
                (TAG_INDEX_DIR / f).unlink()
                deleted_tags.append(tag)
    deleted_topics = []
    for f in os.listdir(TOPIC_INDEX_DIR):
        if f.endswith('.md'):
            topic = f[:-3]
            if topic not in topic_index:
                (TOPIC_INDEX_DIR / f).unlink()
                deleted_topics.append(topic)

    c_count = sum(1 for f in wiki_files if f['type'] == 'concept')
    s_count = sum(1 for f in wiki_files if f['type'] == 'source')
    mem_entry = f"## {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} — Indexed\n\n"
    mem_entry += f"- **Scanned:** {c_count} concepts + {s_count} sources = {len(wiki_files)} total files\n"
    mem_entry += f"- **Tags indexed:** {len(tag_index)} ({len(main_pool)} main-tags + {len(tag_index)-len(main_pool)} sub-tags)\n"
    mem_entry += f"- **Topics indexed:** {len(topic_index)}\n"
    mem_entry += f"- **Orphans deleted:** {len(deleted_tags)} tag indexes + {len(deleted_topics)} topic indexes\n"
    mem_entry += f"- **Invalid tags found:** {len(invalid_tags_found)}\n"
    mem_entry += f"- **Errors:** {errors} files skipped due to invalid frontmatter\n"
    with open(MEMORY_FILE, 'a', encoding='utf-8') as f:
        f.write("\n\n" + mem_entry)

    return {"scanned": len(wiki_files), "concepts": c_count, "sources": s_count, "tags": len(tag_index), "topics": len(topic_index), "orphans_tag": len(deleted_tags), "orphans_topic": len(deleted_topics), "invalid": len(invalid_tags_found), "errors": errors}

if __name__ == "__main__":
    print(run_indexing())
