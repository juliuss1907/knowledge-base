import os
import re
from datetime import datetime
from collections import defaultdict

def parse_frontmatter(content):
    match = re.search(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
    if not match:
        return None
    
    yaml_block = match.group(1)
    data = {}
    for line in yaml_block.split('\n'):
        if ':' in line:
            key, value = line.split(':', 1)
            key = key.strip()
            value = value.strip()
            if value.startswith('[') and value.endswith(']'):
                # Simple list parsing
                value = [v.strip() for v in value[1:-1].split(',') if v.strip()]
            data[key] = value
    return data

def derive_title(slug):
    return ' '.join(word.capitalize() for word in slug.split('-'))

def main():
    # Configuration
    sources_dir = 'wiki/sources'
    concepts_dir = 'wiki/concepts'
    tags_dir = 'wiki/tag'
    topics_dir = 'wiki/topic'
    
    os.makedirs(tags_dir, exist_ok=True)
    os.makedirs(topics_dir, exist_ok=True)
    
    allowed_main = {'ai', 'crypto', 'tech', 'productivity', 'system', 'economic', 'politic'}
    allowed_sub = {'hack', 'tools', 'automation', 'vibecode', 'research', 'tutorial', 
                   'opinion', 'news', 'defi', 'perpdex', 'layer1', 'layer2', 'law', 
                   'coding', 'psychology', 'health'}

    all_files = []
    errors = 0
    invalid_tags_found = []

    # Step 1: Scan files
    for folder, ftype in [(sources_dir, 'source'), (concepts_dir, 'concept')]:
        if not os.path.exists(folder):
            continue
        for filename in sorted(os.listdir(folder)):
            if not filename.endswith('.md'):
                continue
            path = os.path.join(folder, filename)
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            fm = parse_frontmatter(content)
            if not fm:
                print(f"[WARNING] {path}: No frontmatter found")
                errors += 1
                continue
            
            # Validation
            main_tag = fm.get('main_tag')
            sub_tags = fm.get('sub_tags', [])
            if isinstance(sub_tags, str): sub_tags = [sub_tags]
            topic = fm.get('topic')
            
            if not main_tag or not topic:
                print(f"[ERROR] {path}: Missing required fields")
                errors += 1
                continue
            
            # Tag validation
            is_main_valid = main_tag in allowed_main
            if not is_main_valid:
                invalid_tags_found.append(f"{path}: main_tag={main_tag}")
            
            valid_subs = []
            for s in sub_tags:
                if s in allowed_sub:
                    valid_subs.append(s)
                else:
                    invalid_tags_found.append(f"{path}: sub_tag={s}")
            
            slug = filename[:-3]
            all_files.append({
                'path': path,
                'type': ftype,
                'main_tag': main_tag,
                'sub_tags': sub_tags, # Keep original for co-occurrence, but we use valid_subs for index? 
                                      # Workflow says: "Do NOT create index file for invalid tag, still include file in valid tag indexes"
                'valid_subs': valid_subs,
                'topic': topic,
                'slug': slug
            })

    # Step 3: Group by Tag
    tag_index = defaultdict(lambda: {'concepts': [], 'sources': []})
    for f in all_files:
        # Main tag
        if f['main_tag'] in allowed_main:
            tag = f['main_tag']
            if f['type'] == 'concept': tag_index[tag]['concepts'].append(f)
            else: tag_index[tag]['sources'].append(f)
        
        # Sub tags
        for s in f['valid_subs']:
            if f['type'] == 'concept': tag_index[s]['concepts'].append(f)
            else: tag_index[s]['sources'].append(f)

    # Sort items
    for tag in tag_index:
        tag_index[tag]['concepts'].sort(key=lambda x: x['slug'])
        tag_index[tag]['sources'].sort(key=lambda x: x['slug'])

    # Step 4: Co-occurrence
    co_occurrence = defaultdict(int)
    for f in all_files:
        all_tags = [f['main_tag']] + f['sub_tags']
        # Only use allowed tags for co-occurrence matrix to avoid cluttering with invalid ones?
        # Actually, let's use allowed tags.
        filtered_tags = [t for t in all_tags if t in allowed_main or t in allowed_sub]
        filtered_tags = sorted(list(set(filtered_tags)))
        for i in range(len(filtered_tags)):
            for j in range(i + 1, len(filtered_tags)):
                co_occurrence[tuple(sorted([filtered_tags[i], filtered_tags[j]]))] += 1

    tag_co_occur = {}
    for tag in tag_index.keys():
        pairs = []
        for (t1, t2), count in co_occurrence.items():
            if tag == t1: pairs.append((t2, count))
            elif tag == t2: pairs.append((t1, count))
        tag_co_occur[tag] = sorted(pairs, key=lambda x: -x[1])[:5]

    # Step 5: Topic Index
    topic_index = defaultdict(lambda: {'concepts': [], 'sources': []})
    for f in all_files:
        topic = f['topic']
        if f['type'] == 'concept': topic_index[topic]['concepts'].append(f)
        else: topic_index[topic]['sources'].append(f)

    for topic in topic_index:
        topic_index[topic]['concepts'].sort(key=lambda x: x['slug'])
        topic_index[topic]['sources'].sort(key=lambda x: x['slug'])

    # Step 6: Topic Overlap
    topic_overlap = defaultdict(int)
    topics_list = list(topic_index.keys())
    for i in range(len(topics_list)):
        t1 = topics_list[i]
        files1 = {f['path'] for f in topic_index[t1]['concepts'] + topic_index[t1]['sources']}
        for j in range(i + 1, len(topics_list)):
            t2 = topics_list[j]
            files2 = {f['path'] for f in topic_index[t2]['concepts'] + topic_index[t2]['sources']}
            shared = len(files1 & files2)
            if shared > 0:
                topic_overlap[tuple(sorted([t1, t2]))] = shared

    topic_related = {}
    for topic in topic_index.keys():
        pairs = []
        for (t1, t2), count in topic_overlap.items():
            if topic == t1: pairs.append((t2, count))
            elif topic == t2: pairs.append((t1, count))
        topic_related[topic] = sorted(pairs, key=lambda x: -x[1])[:5]

    # Step 7: Write Tag Index Files
    today = datetime.now().strftime('%Y-%m-%d')
    for tag, data in tag_index.items():
        content = f"---\ntype: index\nlevel: 3\nscope: tag\nparent: [[tag]]\ntag: {tag}\nauto_generated: true\nlast_updated: {today}\n---\n\n# Tag: #{tag}\n\n## Parent\n\n- [[tag]]\n\n## Stats\n\n- Total files: {len(data['concepts']) + len(data['sources'])}\n- Sources: {len(data['sources'])}\n- Concepts: {len(data['concepts'])}\n- Last updated: {today}\n\n## Files with this tag\n\n"
        
        all_items = []
        for f in data['concepts']:
            all_items.append((f['slug'], derive_title(f['slug']), 'concept'))
        for f in data['sources']:
            all_items.append((f['slug'], derive_title(f['slug'].replace('src_', '')), 'source'))
        
        all_items.sort(key=lambda x: x[0])
        for slug, title, ftype in all_items:
            content += f"- [[{slug}]] — {title} ({ftype})\n"
        
        if tag in tag_co_occur:
            content += "\n## Co-occurring tags\n\n"
            for other_tag, count in tag_co_occur[tag]:
                unit = "co-occurrence" if count == 1 else "co-occurrences"
                content += f"- [[{other_tag}]] — {count} {unit}\n"
        
        with open(os.path.join(tags_dir, f"{tag}.md"), 'w', encoding='utf-8') as f:
            f.write(content)

    # Step 8: Write Topic Index Files
    for topic, data in topic_index.items():
        content = f"# Topic: {topic}\n\nAuto-generated index of all content with topic `{topic}`.\n\nLast updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n---\n\n## Concepts ({len(data['concepts'])})\n\n"
        for f in data['concepts']:
            subs = ', '.join([f"#{s}" for s in f['sub_tags']])
            content += f"- [[{f['slug']}]] — main: #{f['main_tag']}, sub: [{subs}]\n"
        
        content += f"\n## Sources ({len(data['sources'])})\n\n"
        for f in data['sources']:
            subs = ', '.join([f"#{s}" for s in f['sub_tags']])
            content += f"- [[{f['slug']}]] — main: #{f['main_tag']}, sub: [{subs}]\n"
        
        if topic in topic_related:
            content += "\n## Related topics\n\n"
            content += f"Topics that share concepts/sources with `{topic}`:\n"
            for other_topic, count in topic_related[topic]:
                content += f"- `{other_topic}` ({count} shared files)\n"
        
        with open(os.path.join(topics_dir, f"{topic}.md"), 'w', encoding='utf-8') as f:
            f.write(content)

    # Step 8.5: Update tag.md
    tag_master_path = os.path.join(tags_dir, 'tag.md')
    if not os.path.exists(tag_master_path):
        # Minimal template if doesn't exist
        with open(tag_master_path, 'w', encoding='utf-8') as f:
            f.write("# Tag Index\n\n## Stats\n\n## Items\n\n### Main Tags (Pool A)\n\n### Sub Tags (Pool B)\n")

    with open(tag_master_path, 'r', encoding='utf-8') as f:
        master_content = f.read()

    # Update Items section
    # We'll read TAGS.md for descriptions
    tag_descriptions = {}
    with open('TAGS.md', 'r', encoding='utf-8') as f:
        for line in f:
            if '| `#`' in line:
                parts = line.split('|')
                if len(parts) >= 3:
                    tag_name = parts[1].strip().replace('#', '').replace('`', '')
                    desc = parts[2].strip()
                    tag_descriptions[tag_name] = desc

    for tag in tag_index.keys():
        if f"- [[{tag}]]" not in master_content:
            pool = "Main Tags (Pool A)" if tag in allowed_main else "Sub Tags (Pool B)"
            desc = tag_descriptions.get(tag, "[description]")
            pattern = f"### {pool}"
            if pattern in master_content:
                master_content = master_content.replace(pattern, f"{pattern}\n- [[{tag}]] — {desc}")

    # Update Stats
    total_tags = len(tag_index)
    main_tags_count = len([t for t in tag_index if t in allowed_main])
    sub_tags_count = total_tags - main_tags_count
    
    tag_counts = {tag: len(data['concepts']) + len(data['sources']) for tag, data in tag_index.items()}
    top_3 = sorted(tag_counts.items(), key=lambda x: -x[1])[:3]
    most_used = ', '.join([f"#{t} ({c})" for t, c in top_3])
    
    stats_block = f"## Stats\n\n- Total tags: {total_tags}\n- Main tags: {main_tags_count}\n- Sub tags: {sub_tags_count}\n- Most used: {most_used}\n- Last updated: {today}"
    
    if "## Stats" in master_content:
        master_content = re.sub(r'## Stats.*?(?=## Items|$)', stats_block, master_content, flags=re.DOTALL)
    else:
        master_content = stats_block + "\n\n" + master_content

    with open(tag_master_path, 'w', encoding='utf-8') as f:
        f.write(master_content)

    # Step 9: Cleanup Orphans
    deleted_tags = []
    for filename in os.listdir(tags_dir):
        if filename == 'tag.md' or not filename.endswith('.md'): continue
        tag = filename[:-3]
        if tag not in tag_index:
            os.remove(os.path.join(tags_dir, filename))
            deleted_tags.append(tag)

    deleted_topics = []
    for filename in os.listdir(topics_dir):
        if not filename.endswith('.md'): continue
        topic = filename[:-3]
        if topic not in topic_index:
            os.remove(os.path.join(topics_dir, filename))
            deleted_topics.append(topic)

    # Final Summary
    print("--- SUMMARY ---")
    print(f"Scanned: {len(all_files)} files")
    print(f"Tags indexed: {len(tag_index)} ({main_tags_count} main + {sub_tags_count} sub)")
    print(f"Topics indexed: {len(topic_index)}")
    print(f"Orphans deleted: {len(deleted_tags)} tags + {len(deleted_topics)} topics")
    print(f"Invalid tags found: {len(invalid_tags_found)}")
    print(f"Errors: {errors} files skipped")
    for it in invalid_tags_found:
        print(f"  - {it}")

if __name__ == '__main__':
    main()
