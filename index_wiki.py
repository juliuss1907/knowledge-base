import os
import re
import yaml
from datetime import datetime
from collections import Counter, defaultdict

# Configuration
SOURCES_DIR = 'wiki/sources/'
CONCEPTS_DIR = 'wiki/concepts/'
TAGS_DIR = 'wiki/tag/'
TOPICS_DIR = 'wiki/topic/'
TAGS_FILE = 'TAGS.md'
MASTER_TAG_FILE = 'wiki/tag/tag.md'
MEMORY_FILE = '.openclaw/MEMORY.md'

def load_tags():
    with open(TAGS_FILE, 'r', encoding='utf-8') as f:
        content = f.read()
    
    main_tags = {}
    sub_tags = {}
    
    # Simple table parser
    # Find section 2 and 3
    sections = re.split(r'## \d\.', content)
    # sections[0] is intro, sections[1] is rules, sections[2] is Pool A, sections[3] is Pool B
    
    if len(sections) > 2:
        # Pool A
        pool_a_text = sections[2]
        for line in pool_a_text.split('\n'):
            if '|' in line and not line.strip().startswith('|---'):
                parts = [p.strip() for p in line.split('|')]
                if len(parts) >= 3:
                    tag = parts[1].strip('#')
                    desc = parts[2]
                    main_tags[tag] = desc
                    
    if len(sections) > 3:
        # Pool B
        pool_b_text = sections[3]
        for line in pool_b_text.split('\n'):
            if '|' in line and not line.strip().startswith('|---'):
                parts = [p.strip() for p in line.split('|')]
                if len(parts) >= 3:
                    tag = parts[1].strip('#')
                    desc = parts[2]
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
    slug = slug.replace('src_', '')
    return ' '.join(word.capitalize() for word in slug.split('-'))

def main():
    main_tags_dict, sub_tags_dict = load_tags()
    allowed_main = set(main_tags_dict.keys())
    allowed_sub = set(sub_tags_dict.keys())
    
    files_data = []
    invalid_tags_log = []
    frontmatter_errors = 0
    
    for folder, ftype in [(SOURCES_DIR, 'source'), (CONCEPTS_DIR, 'concept')]:
        if not os.path.exists(folder): continue
        for filename in sorted(os.listdir(folder)):
            if not filename.endswith('.md'): continue
            path = os.path.join(folder, filename)
            fm = parse_frontmatter(path)
            if not fm:
                frontmatter_errors += 1
                continue
            
            slug = filename[:-3]
            main_tag = fm.get('main_tag')
            sub_tags = fm.get('sub_tags', [])
            topic = fm.get('topic')
            
            if not main_tag or not topic:
                frontmatter_errors += 1
                continue
            
            if not isinstance(sub_tags, list):
                sub_tags = []

            invalid_main = False
            if main_tag not in allowed_main:
                invalid_tags_log.append(f"[INVALID TAG] {path}: main_tag={main_tag}")
                invalid_main = True
                
            invalid_subs = []
            for st in sub_tags:
                if st not in allowed_sub:
                    invalid_tags_log.append(f"[INVALID TAG] {path}: sub_tag={st}")
                    invalid_subs.append(st)
            
            files_data.append({
                'path': path,
                'type': ftype,
                'main_tag': main_tag,
                'sub_tags': sub_tags,
                'topic': topic,
                'slug': slug,
                'invalid_main': invalid_main,
                'invalid_subs': invalid_subs
            })

    tag_index = defaultdict(lambda: {'concepts': [], 'sources': []})
    for f in files_data:
        if not f['invalid_main']:
            tag = f['main_tag']
            if f['type'] == 'concept': tag_index[tag]['concepts'].append(f)
            else: tag_index[tag]['sources'].append(f)
            
        for st in f['sub_tags']:
            if st not in f['invalid_subs']:
                if f['type'] == 'concept': tag_index[st]['concepts'].append(f)
                else: tag_index[st]['sources'].append(f)

    co_occurrence = Counter()
    for f in files_data:
        all_tags = []
        if not f['invalid_main']: all_tags.append(f['main_tag'])
        for st in f['sub_tags']:
            if st not in f['invalid_subs']: all_tags.append(st)
        
        all_tags = sorted(list(set(all_tags)))
        for i in range(len(all_tags)):
            for j in range(i + 1, len(all_tags)):
                co_occurrence[tuple(sorted([all_tags[i], all_tags[j]]))] += 1

    topic_index = defaultdict(lambda: {'concepts': [], 'sources': []})
    for f in files_data:
        topic = f['topic']
        if f['type'] == 'concept': topic_index[topic]['concepts'].append(f)
        else: topic_index[topic]['sources'].append(f)

    topic_overlap = Counter()
    topics = list(topic_index.keys())
    for i in range(len(topics)):
        t1 = topics[i]
        f1_paths = {f['path'] for f in topic_index[t1]['concepts'] + topic_index[t1]['sources']}
        for j in range(i + 1, len(topics)):
            t2 = topics[j]
            f2_paths = {f['path'] for f in topic_index[t2]['concepts'] + topic_index[t2]['sources']}
            shared = len(f1_paths & f2_paths)
            if shared > 0:
                topic_overlap[tuple(sorted([t1, t2]))] += shared

    os.makedirs(TAGS_DIR, exist_ok=True)
    today = datetime.now().strftime('%Y-%m-%d')
    
    for tag, data in tag_index.items():
        concepts = sorted(data['concepts'], key=lambda x: x['slug'])
        sources = sorted(data['sources'], key=lambda x: x['slug'])
        all_items = []
        for c in concepts: all_items.append((c['slug'], derive_title(c['slug']), 'concept'))
        for s in sources: all_items.append((s['slug'], derive_title(s['slug']), 'source'))
        all_items.sort()

        pairs = [(other, count) for (t1, t2), count in co_occurrence.items() 
                 if tag in (t1, t2) and (other := t2 if t1 == tag else t1)]
        top_5_co = sorted(pairs, key=lambda x: -x[1])[:5]

        content = f"---\ntype: index\nlevel: 3\nscope: tag\nparent: [[tag]]\ntag: {tag}\nauto_generated: true\nlast_updated: {today}\n---\n\n# Tag: #{tag}\n\n## Parent\n\n- [[tag]]\n\n## Stats\n\n- Total files: {len(all_items)}\n- Sources: {len(sources)}\n- Concepts: {len(concepts)}\n- Last updated: {today}\n\n## Files with this tag\n\n"
        for slug, title, ftype in all_items:
            content += f"- [[{slug}]] — {title} ({ftype})\n"
        if top_5_co:
            content += "\n## Co-occurring tags\n\n"
            for other, count in top_5_co:
                unit = "co-occurrence" if count == 1 else "co-occurrences"
                content += f"- [[{other}]] — {count} {unit}\n"
        
        with open(os.path.join(TAGS_DIR, f"{tag}.md"), 'w', encoding='utf-8') as f:
            f.write(content)

    os.makedirs(TOPICS_DIR, exist_ok=True)
    for topic, data in topic_index.items():
        concepts = sorted(data['concepts'], key=lambda x: x['slug'])
        sources = sorted(data['sources'], key=lambda x: x['slug'])
        related_pairs = [(other, count) for (t1, t2), count in topic_overlap.items() 
                         if topic in (t1, t2) and (other := t2 if t1 == topic else t1)]
        top_5_rel = sorted(related_pairs, key=lambda x: -x[1])[:5]

        content = f"# Topic: {topic}\n\nAuto-generated index of all content with topic `{topic}`.\n\nLast updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n---\n\n## Concepts ({len(concepts)})\n\n"
        for c in concepts:
            subs = ', '.join([f"#{s}" for s in c['sub_tags']])
            content += f"- [[{c['slug']}]] — main: #{c['main_tag']}, sub: [{subs}]\n"
        content += f"\n## Sources ({len(sources)})\n\n"
        for s in sources:
            subs = ', '.join([f"#{s}" for s in s['sub_tags']])
            content += f"- [[{s['slug']}]] — main: #{s['main_tag']}, sub: [{subs}]\n"
        if top_5_rel:
            content += "\n## Related topics\n\n"
            content += f"Topics that share concepts/sources with `{topic}`:\n"
            for other, count in top_5_rel:
                content += f"- `{other}` ({count} shared files)\n"
        with open(os.path.join(TOPICS_DIR, f"{topic}.md"), 'w', encoding='utf-8') as f:
            f.write(content)

    main_tags_list = sorted(list(allowed_main))
    sub_tags_list = sorted(list(allowed_sub))
    total_tags_count = len(tag_index)
    tag_counts = {tag: len(data['concepts']) + len(data['sources']) for tag, data in tag_index.items()}
    top_3 = sorted(tag_counts.items(), key=lambda x: -x[1])[:3]
    most_used = ', '.join([f"#{tag} ({count})" for tag, count in top_3])

    master_content = f"# Tags\n\nAuto-generated master index of all tags in Knowledge Base.\n\n## Stats\n\n- Total tags: {total_tags_count}\n- Main tags: {len(main_tags_list)}\n- Sub tags: {len(sub_tags_list)}\n- Most used: {most_used}\n- Last updated: {today}\n\n## Items\n\n### Main Tags (Pool A)\n\n"
    for tag in main_tags_list:
        desc = main_tags_dict.get(tag, '[description]')
        master_content += f"- [[{tag}]] — {desc}\n"
    master_content += "\n### Sub Tags (Pool B)\n\n"
    for tag in sub_tags_list:
        desc = sub_tags_dict.get(tag, '[description]')
        master_content += f"- [[{tag}]] — {desc}\n"
    with open(MASTER_TAG_FILE, 'w', encoding='utf-8') as f:
        f.write(master_content)

    orphans_tag = 0
    orphans_topic = 0
    for filename in os.listdir(TAGS_DIR):
        if filename == 'tag.md' or not filename.endswith('.md'): continue
        tag = filename[:-3]
        if tag not in tag_index:
            os.remove(os.path.join(TAGS_DIR, filename))
            orphans_tag += 1
    for filename in os.listdir(TOPICS_DIR):
        if not filename.endswith('.md'): continue
        topic = filename[:-3]
        if topic not in topic_index:
            os.remove(os.path.join(TOPICS_DIR, filename))
            orphans_topic += 1

    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log_entry = f"\n## {timestamp} — Indexed\n\n"
    log_entry += f"- **Scanned:** {len(files_data)} files ({len([f for f in files_data if f['type']=='concept'])} concepts + {len([f for f in files_data if f['type']=='source'])} sources)\n"
    log_entry += f"- **Tags indexed:** {len(tag_index)} ({len(allowed_main)} main-tags + {len(tag_index)-len(allowed_main)} sub-tags)\n"
    log_entry += f"- **Topics indexed:** {len(topic_index)}\n"
    log_entry += f"- **Orphans deleted:** {orphans_tag} tag indexes + {orphans_topic} topic indexes\n"
    log_entry += f"- **Invalid tags found:** {len(invalid_tags_log)}\n"
    log_entry += f"- **Errors:** {frontmatter_errors} files skipped\n"
    with open(MEMORY_FILE, 'a', encoding='utf-8') as f:
        f.write(log_entry)
    
    print(f"Indexed: {len(files_data)} files, {len(tag_index)} tags, {len(topic_index)} topics. Orphans: {orphans_tag+orphans_topic}. Errors: {frontmatter_errors}. Invalid: {len(invalid_tags_log)}")

if __name__ == '__main__':
    main()
