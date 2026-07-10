import os
import re
from datetime import datetime
from collections import defaultdict

def derive_title(slug):
    # Remove 'src_' prefix for sources
    clean_slug = slug.replace('src_', '')
    return ' '.join(word.capitalize() for word in clean_slug.split('-'))

def parse_frontmatter(content):
    match = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
    if not match:
        return None
    
    yaml_block = match.group(1)
    data = {}
    for line in yaml_block.split('\n'):
        if ':' in line:
            key, value = line.split(':', 1)
            key = key.strip()
            value = value.strip()
            
            # Handle lists like [tag1, tag2]
            if value.startswith('[') and value.endswith(']'):
                value = [v.strip() for v in value[1:-1].split(',')]
            
            data[key] = value
    return data

def load_tags():
    with open('TAGS.md', 'r', encoding='utf-8') as f:
        content = f.read()
    
    pool_a = []
    pool_b = []
    
    lines = content.split('\n')
    current_pool = None
    
    for line in lines:
        if '## 2. Pool A' in line:
            current_pool = 'A'
            continue
        elif '## 3. Pool B' in line:
            current_pool = 'B'
            continue
        elif line.startswith('##'):
            current_pool = None
            continue
            
        if current_pool == 'A' and '|' in line and not line.startswith('| Tag') and not line.startswith('|---'):
            tag = line.split('|')[1].strip().strip('#')
            if tag: pool_a.append(tag)
        elif current_pool == 'B' and '|' in line and not line.startswith('| Tag') and not line.startswith('|---'):
            tag = line.split('|')[1].strip().strip('#')
            if tag: pool_b.append(tag)
            
    return pool_a, pool_b

def debug_tags():
    a, b = load_tags()
    print(f"DEBUG: Pool A: {a}")
    print(f"DEBUG: Pool B: {b}")


def main():
    debug_tags()
    today = datetime.now().strftime('%Y-%m-%d')
    now_full = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    pool_a, pool_b = load_tags()
    allowed_tags = {'main': set(pool_a), 'sub': set(pool_b)}
    
    all_files = []
    errors = 0
    invalid_tags_found = []
    
    # Step 1: Scan Wiki Files
    search_dirs = ['wiki/sources', 'wiki/concepts']
    for d in search_dirs:
        if not os.path.exists(d): continue
        for filename in sorted(os.listdir(d)):
            if filename.endswith('.md'):
                path = os.path.join(d, filename)
                with open(path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    fm = parse_frontmatter(content)
                    if not fm:
                        print(f"[WARNING] {path}: No frontmatter found")
                        errors += 1
                        continue
                    
                    # Validation
                    f_type = fm.get('type')
                    main_tag = fm.get('main_tag')
                    sub_tags = fm.get('sub_tags', [])
                    if isinstance(sub_tags, str): sub_tags = [sub_tags]
                    topic = fm.get('topic')
                    
                    if not all([f_type, main_tag, topic]):
                        print(f"[ERROR] {path}: Missing required fields")
                        errors += 1
                        continue
                        
                    # Tag validation
                    invalid_main = False
                    if main_tag not in allowed_tags['main']:
                        print(f"[INVALID TAG] {path}: main_tag={main_tag}")
                        invalid_tags_found.append((path, 'main', main_tag))
                        invalid_main = True
                    
                    invalid_subs = []
                    for st in sub_tags:
                        if st not in allowed_tags['sub']:
                            print(f"[INVALID TAG] {path}: sub_tag={st}")
                            invalid_tags_found.append((path, 'sub', st))
                            invalid_subs.append(st)
                            
                    all_files.append({
                        'path': path,
                        'type': f_type,
                        'main_tag': main_tag,
                        'sub_tags': sub_tags,
                        'topic': topic,
                        'slug': filename[:-3],
                        'invalid_main': invalid_main,
                        'invalid_subs': invalid_subs
                    })

    # Step 3: Group Files by Tag
    tag_index = defaultdict(lambda: {'concepts': [], 'sources': []})
    for f in all_files:
        # Main tag
        if not f['invalid_main']:
            tag = f['main_tag']
            if f['type'] == 'concept':
                tag_index[tag]['concepts'].append(f)
            else:
                tag_index[tag]['sources'].append(f)
        
        # Sub tags
        for st in f['sub_tags']:
            if st not in f['invalid_subs']:
                if f['type'] == 'concept':
                    tag_index[st]['concepts'].append(f)
                else:
                    tag_index[st]['sources'].append(f)

    # Sort files
    for tag in tag_index:
        tag_index[tag]['concepts'].sort(key=lambda x: x['slug'])
        tag_index[tag]['sources'].sort(key=lambda x: x['slug'])

    # Step 4: Co-occurrence
    co_occurrence = defaultdict(int)
    for f in all_files:
        tags = [f['main_tag']] + f['sub_tags']
        tags = sorted(list(set(tags))) # Unique and sorted
        for i in range(len(tags)):
            for j in range(i + 1, len(tags)):
                co_occurrence[(tags[i], tags[j])] += 1
                
    tag_co_occur = {}
    for tag in tag_index.keys():
        pairs = []
        for (t1, t2), count in co_occurrence.items():
            if t1 == tag: pairs.append((t2, count))
            elif t2 == tag: pairs.append((t1, count))
        tag_co_occur[tag] = sorted(pairs, key=lambda x: -x[1])[:5]

    # Step 5: Group Files by Topic
    topic_index = defaultdict(lambda: {'concepts': [], 'sources': []})
    for f in all_files:
        topic = f['topic']
        if f['type'] == 'concept':
            topic_index[topic]['concepts'].append(f)
        else:
            topic_index[topic]['sources'].append(f)
            
    for topic in topic_index:
        topic_index[topic]['concepts'].sort(key=lambda x: x['slug'])
        topic_index[topic]['sources'].sort(key=lambda x: x['slug'])

    # Step 6: Topic Overlap
    topic_overlap = defaultdict(int)
    topic_list = sorted(topic_index.keys())
    for i in range(len(topic_list)):
        for j in range(i + 1, len(topic_list)):
            t1, t2 = topic_list[i], topic_list[j]
            files1 = {f['path'] for f in topic_index[t1]['concepts'] + topic_index[t1]['sources']}
            files2 = {f['path'] for f in topic_index[t2]['concepts'] + topic_index[t2]['sources']}
            shared = len(files1 & files2)
            if shared > 0:
                topic_overlap[(t1, t2)] = shared
                
    topic_related = {}
    for topic in topic_index.keys():
        pairs = []
        for (t1, t2), count in topic_overlap.items():
            if t1 == topic: pairs.append((t2, count))
            elif t2 == topic: pairs.append((t1, count))
        topic_related[topic] = sorted(pairs, key=lambda x: -x[1])[:5]

    # Step 7: Write Tag Index Files
    os.makedirs('wiki/tag', exist_ok=True)
    for tag, data in tag_index.items():
        co_occur = tag_co_occur.get(tag, [])
        
        # Derive items list
        all_items = []
        for f in data['concepts']:
            all_items.append((f['slug'], derive_title(f['slug']), 'concept'))
        for f in data['sources']:
            all_items.append((f['slug'], derive_title(f['slug']), 'source'))
        all_items.sort(key=lambda x: x[0])
        
        content = f"---\ntype: index\nlevel: 3\nscope: tag\nparent: \"[[tag]]\"\ntag: {tag}\nauto_generated: true\nlast_updated: {today}\n---\n\n# Tag: #{tag}\n\n## Parent\n\n- [[tag]]\n\n## Stats\n\n- Total files: {len(all_items)}\n- Sources: {len(data['sources'])}\n- Concepts: {len(data['concepts'])}\n- Last updated: {today}\n\n## Files with this tag\n\n"
        for slug, title, ftype in all_items:
            content += f"- [[{slug}]] — {title} ({ftype})\n"
            
        if co_occur:
            content += "\n## Co-occurring tags\n\n"
            for other, count in co_occur:
                unit = "co-occurrence" if count == 1 else "co-occurrences"
                content += f"- [[{other}]] — {count} {unit}\n"
        
        with open(f'wiki/tag/{tag}.md', 'w', encoding='utf-8') as f:
            f.write(content)

    # Step 8: Write Topic Index Files
    os.makedirs('wiki/topic', exist_ok=True)
    for topic, data in topic_index.items():
        related = topic_related.get(topic, [])
        
        content = f"---\ntype: index\nscope: topic\nparent: \"[[topic]]\"\ntopic: {topic}\nauto_generated: true\nlast_updated: {today}\n---\n\n# Topic: {topic}\n\nAuto-generated index of all content with topic `{topic}`.\n\nLast updated: {now_full}\n\n---\n\n## Concepts ({len(data['concepts'])})\n\n"
        
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
            for other, count in related:
                content += f"- `{other}` ({count} shared files)\n"
                
        with open(f'wiki/topic/{topic}.md', 'w', encoding='utf-8') as f:
            f.write(content)

    # Step 9: Clean up Orphans
    orphaned_tags = []
    if os.path.exists('wiki/tag'):
        for filename in os.listdir('wiki/tag'):
            if filename == 'tag.md': continue
            tag = filename[:-3]
            if tag not in tag_index:
                orphaned_tags.append(tag)
                os.remove(os.path.join('wiki/tag', filename))
                
    orphaned_topics = []
    if os.path.exists('wiki/topic'):
        for filename in os.listdir('wiki/topic'):
            topic = filename[:-3]
            if topic not in topic_index:
                orphaned_topics.append(topic)
                os.remove(os.path.join('wiki/topic', filename))

    # Final summary for output
    print(f"SUMMARY|Scanned: {len(all_files)}|Tags: {len(tag_index)}|Topics: {len(topic_index)}|OrphansTag: {len(orphaned_tags)}|OrphansTopic: {len(orphaned_topics)}|Errors: {errors}|Invalid: {len(invalid_tags_found)}")
    for path, ptype, tag in invalid_tags_found:
        print(f"INVALID|{path}|{ptype}|{tag}")

if __name__ == '__main__':
    main()
