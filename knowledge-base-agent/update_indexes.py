import os
import re
from datetime import datetime

def parse_frontmatter(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            match = re.search(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
            if match:
                fm_text = match.group(1)
                fm = {}
                for line in fm_text.split('\n'):
                    if ':' in line:
                        k, v = line.split(':', 1)
                        fm[k.strip()] = v.strip()
                return fm
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
    return None

def update_concepts_index():
    concepts_dir = 'wiki/concepts/'
    if not os.path.exists(concepts_dir):
        return
    files = sorted([f for f in os.listdir(concepts_dir) if f.endswith('.md')])
    lines = ['# Concepts Index\n']
    
    for f in files:
        path = os.path.join(concepts_dir, f)
        fm = parse_frontmatter(path)
        if fm:
            status = fm.get('status', 'unknown')
            tags = fm.get('tags', '[]')
            updated = fm.get('updated', 'unknown')
            lines.append(f"- [[wiki/concepts/{f}]] | status: {status} | tags: {tags} | updated: {updated}")
    
    with open('wiki/indexes/concepts_index.md', 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))

def update_sources_index():
    sources_dir = 'wiki/sources/'
    if not os.path.exists(sources_dir):
        return
    files = sorted([f for f in os.listdir(sources_dir) if f.endswith('.md')])
    lines = ['# Sources Index\n']
    
    for f in files:
        path = os.path.join(sources_dir, f)
        fm = parse_frontmatter(path)
        if fm:
            updated = fm.get('updated', 'unknown')
            lines.append(f"- [[wiki/sources/{f}]] | updated: {updated}")
    
    with open('wiki/indexes/sources_index.md', 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))

def update_reviews_index():
    reviews_dir = 'wiki/reviews/'
    if not os.path.exists(reviews_dir):
        return
    files = sorted([f for f in os.listdir(reviews_dir) if f.endswith('.md') and not f.startswith('_')])
    lines = ['# Reviews Index\n']
    
    for f in files:
        path = os.path.join(reviews_dir, f)
        fm = parse_frontmatter(path)
        if fm:
            verdict = fm.get('verdict', 'unknown')
            updated = fm.get('updated', 'unknown')
            lines.append(f"- [[wiki/reviews/{f}]] | verdict: {verdict} | updated: {updated}")
    
    with open('wiki/indexes/reviews_index.md', 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))

def update_questions_index():
    questions_dir = 'wiki/questions/'
    if not os.path.exists(questions_dir):
        return
    files = sorted([f for f in os.listdir(questions_dir) if f.endswith('.md')])
    lines = ['# Questions Index\n']
    
    for f in files:
        path = os.path.join(questions_dir, f)
        fm = parse_frontmatter(path)
        if fm:
            updated = fm.get('updated', 'unknown')
            lines.append(f"- [[wiki/questions/{f}]] | updated: {updated}")
    
    with open('wiki/indexes/questions_index.md', 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))

if __name__ == "__main__":
    update_concepts_index()
    update_sources_index()
    update_reviews_index()
    update_questions_index()
    print("Indexes updated successfully.")
