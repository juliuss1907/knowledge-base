import os
import yaml
import re
from datetime import datetime
from collections import defaultdict

# Configuration
SOURCES_DIR = 'wiki/sources/'
CONCEPTS_DIR = 'wiki/concepts/'
TAGS_DIR = 'wiki/tag/'
TOPICS_DIR = 'wiki/topic/'
TAGS_FILE = 'TAGS.md'

ALLOWED_TAGS = {
    'main': ['ai', 'crypto', 'tech', 'productivity', 'system', 'economic', 'politic'],
    'sub': ['hack', 'tools', 'automation', 'vibecode', 'research', 'tutorial', 'opinion', 'news', 'defi', 'perpdex', 'layer1', 'layer2', 'law', 'coding', 'psychology', 'health']
}

def derive_title(slug):
    # Remove 'src_' prefix for sources
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
        except yaml.YAMLError:
            return None

def main():
    # 1. Scan Files
    wiki_files = []
    for folder in [SOURCES_DIR, CONCEPTS_DIR]:
        if not os.path.exists(folder): continue
        for f in os.listdir(folder):
            if f.endswith('.md'):
                path = os.path.join(folder, f)
                fm = parse_frontmatter(path)
                if fm:
                    slug = f[:-3]
                    wiki_files.append({
                        'path': path,
                        'slug': slug,
                        'type': fm.get('type'),
                        'main_tag': fm.get('main_tag'),
                        'sub_tags': fm.get('sub_tags', []),
                        'topic': fm.get('topic'),
                        'fm': fm
                    })
                else:
                    print(f"[WARNING] {path}: No valid frontmatter found")

    # 2. Validate and Group
    tag_index = defaultdict(lambda: {'concepts': [], 'sources': []})
    topic_index = defaultdict(lambda: {'concepts': [], 'sources': []})
    invalid_tags_log = []

    for file in wiki_files:
        # Validate main_tag
        main = file['main_tag']
        if main not in ALLOWED_TAGS['main']:
            invalid_tags_log.append(f"[INVALID TAG] {file['path']}: main_tag={main}")
            main_valid = False
        else:
            main_valid = True

        # Validate sub_tags
        subs = file['sub_tags']
        valid_subs = []
        for s in subs:
            if s in ALLOWED_TAGS['sub']:
                valid_subs.append(s)
            else:
                invalid_tags_log.append(f"[INVALID TAG] {file['path']}: sub_tag={s}")

        # Add to tag_index
        if main_valid:
            if file['type'] == 'concept':
                tag_index[main]['concepts'].append(file)
            else:
                tag_index[main]['sources'].append(file)
        
        for s in valid_subs:
            if file['type'] == 'concept':
                tag_index[s]['concepts'].append(file)
            else:
                tag_index[s]['sources'].append(file)

        # Add to topic_index
        topic = file['topic']
        if topic:
            if file['type'] == 'concept':
                topic_index[topic]['concepts'].append(file)
            else:
                topic_index[topic]['sources'].append(file)

    # Sort lists
    for tag in tag_index:
        tag_index[tag]['concepts'].sort(key=lambda x: x['slug'])
        tag_index[tag]['sources'].sort(key=lambda x: x['slug'])
    for topic in topic_index:
        topic_index[topic]['concepts'].sort(key=lambda x: x['slug'])
        topic_index[topic]['sources'].sort(key=lambda x: x['slug'])

    # 3. Co-occurrence
    co_occurrence = defaultdict(int)
    for file in wiki_files:
        # Use validated tags for co-occurrence
        main = file['main_tag'] if file['main_tag'] in ALLOWED_TAGS['main'] else None
        subs = [s for s in file['sub_tags'] if s in ALLOWED_TAGS['sub']]
        tags = [t for t in [main] + subs if t]
        
        for i in range(len(tags)):
            for j in range(i + 1, len(tags)):
                pair = tuple(sorted([tags[i], tags[j]]))
                co_occurrence[pair] += 1

    tag_co_occur = {}
    for tag in tag_index:
        pairs = []
        for (t1, t2), count in co_occurrence.items():
            if tag == t1: pairs.append((t2, count))
            elif tag == t2: pairs.append((t1, count))
        tag_co_occur[tag] = sorted(pairs, key=lambda x: -x[1])[:5]

    # 4. Topic Overlap
    topic_overlap = defaultdict(int)
    topic_list = list(topic_index.keys())
    for i in range(len(topic_list)):
        for j in range(i + 1, len(topic_list)):
            t1, t2 = topic_list[i], topic_list[j]
            files1 = set([f['path'] for f in topic_index[t1]['concepts'] + topic_index[t1]['sources']])
            files2 = set([f['path'] for f in topic_index[t2]['concepts'] + topic_index[t2]['sources']])
            overlap = len(files1 & files2)
            if overlap > 0:
                topic_overlap[tuple(sorted([t1, t2]))] = overlap

    topic_related = {}
    for topic in topic_index:
        pairs = []
        for (t1, t2), count in topic_overlap.items():
            if topic == t1: pairs.append((t2, count))
            elif topic == t2: pairs.append((t1, count))
        topic_related[topic] = sorted(pairs, key=lambda x: -x[1])[:5]

    # 5. Write Tag Indexes
    os.makedirs(TAGS_DIR, exist_ok=True)
    today = datetime.now().strftime('%Y-%m-%d')
    for tag, data in tag_index.items():
        all_items = []
        for f in data['concepts']:
            all_items.append((f['slug'], derive_title(f['slug']), 'concept'))
        for f in data['sources']:
            all_items.append((f['slug'], derive_title(f['slug']), 'source'))
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
        
        with open(os.path.join(TAGS_DIR, f"{tag}.md"), 'w', encoding='utf-8') as f:
            f.write(content)

    # 6. Write Topic Indexes
    os.makedirs(TOPICS_DIR, exist_ok=True)
    for topic, data in topic_index.items():
        content = f"# Topic: {topic}\n\nAuto-generated index of all content with topic `{topic}`.\n\nLast updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n---\n\n## Concepts ({len(data['concepts'])})\n\n"
        for f in data['concepts']:
            main = f['main_tag']
            subs = ', '.join([f"#{s}" for s in f['sub_tags']])
            content += f"- [[{f['slug']}]] — main: #{main}, sub: [{subs}]\n"
        
        content += f"\n## Sources ({len(data['sources'])})\n\n"
        for f in data['sources']:
            main = f['main_tag']
            subs = ', '.join([f"#{s}" for s in f['sub_tags']])
            content += f"- [[{f['slug']}]] — main: #{main}, sub: [{subs}]\n"
        
        related = topic_related.get(topic, [])
        if related:
            content += "\n## Related topics\n\n"
            content += f"Topics that share concepts/sources with `{topic}`:\n"
            for other, count in related:
                content += f"- `{other}` ({count} shared files)\n"
        
        with open(os.path.join(TOPICS_DIR, f"{topic}.md"), 'w', encoding='utf-8') as f:
            f.write(content)

    # 7. Summary for logs
    print(f"SCAN_SUMMARY: {len(wiki_files)} files scanned")
    print(f"TAGS_INDEXED: {len(tag_index)}")
    print(f"TOPICS_INDEXED: {len(topic_index)}")
    for log in invalid_tags_log:
        print(log)

if __name__ == '__main__':
    main()
