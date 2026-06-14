#!/usr/bin/env python3
"""
Hygiene scan template for Knowledge Base V2.
Usage: python3 /tmp/hygiene_scan.py
Output: pipe-delimited lines for terminal parsing.
"""

import os
import re

root = '/home/julius/knowledge-base'

# Whitelist definitions
root_allowed_files = {
    'AGENTS.md', 'TAGS.md', 'README.md', 'knowledge-base.md',
    'HEARTBEAT.md', 'IDENTITY.md', 'SOUL.md', 'TOOLS.md', 'USER.md',
    '.gitignore'
}
root_allowed_dirs = {'.git', '.obsidian', '.openclaw', '.hermes', 'context', 'raw', 'wiki', 'scripts'}

raw_allowed_dirs = {'articles', 'posts', 'websites', 'videos', 'papers', 'repos'}
wiki_allowed_dirs = {'meta', 'sources', 'concepts', 'tag', 'topic', 'drafts', 'reviews'}

issues = []
paths_checked = 0
seen = set()

def add_issue(path, severity, category, issue, current, expected, fix):
    key = (path, issue)
    if key in seen:
        return
    seen.add(key)
    issues.append({
        'path': path,
        'severity': severity,
        'category': category,
        'issue': issue,
        'current': current,
        'expected': expected,
        'suggested_fix': fix
    })

for dirpath, dirnames, filenames in os.walk(root):
    rel = os.path.relpath(dirpath, root)
    if rel == '.':
        rel = ''
    parts = rel.split(os.sep) if rel else []
    
    # Skip git internals and agent deep internals
    if any(p in {'.git', 'node_modules', '.obsidian', '.hermes', '.openclaw'} for p in parts):
        continue
    
    paths_checked += 1
    
    # Root level
    if rel == '':
        for fn in filenames:
            if fn.startswith('.'):
                if fn == '.gitignore':
                    continue
                add_issue(fn, 'WARNING', 'Naming', 'Hidden file at root', fn, 'Only .gitignore allowed', 'Remove or gitignore')
                continue
            if fn not in root_allowed_files:
                add_issue(fn, 'ERROR', 'Path', 'File not in root whitelist', fn, 'One of allowed root files', 'Remove or move to allowed folder')
        for dn in dirnames:
            if dn.startswith('.') and dn in {'.git', '.obsidian', '.openclaw', '.hermes'}:
                continue
            if dn not in root_allowed_dirs:
                if dn.startswith('.tmp-'):
                    add_issue(dn, 'WARNING', 'Path', 'Temporary folder not in whitelist', dn, 'Update folder-structure.md or remove', 'Remove after testing or update whitelist')
                else:
                    add_issue(dn + '/', 'ERROR', 'Path', 'Folder not in root whitelist', dn, 'One of allowed root folders', 'Remove or update folder-structure.md')
        continue
    
    # Depth 1
    if len(parts) == 1:
        top = parts[0]
        if top == 'context':
            for fn in filenames:
                if fn not in {'context.md', 'USER.md'}:
                    add_issue(os.path.join(rel, fn), 'ERROR', 'Path', 'File not allowed in context/', fn, 'Only context.md and USER.md', 'Remove or move')
            for dn in dirnames:
                add_issue(os.path.join(rel, dn), 'ERROR', 'Path', 'No subfolders allowed in context/', dn, 'None', 'Remove subfolder')
        elif top == 'raw':
            for fn in filenames:
                if fn != 'raw.md' and not fn.startswith('.'):
                    add_issue(os.path.join(rel, fn), 'ERROR', 'Path', 'File not allowed at raw/ root', fn, 'Only raw.md', 'Move to subfolder or remove')
            for dn in dirnames:
                if dn not in raw_allowed_dirs:
                    add_issue(os.path.join(rel, dn), 'ERROR', 'Path', 'Subfolder not allowed in raw/', dn, 'One of allowed raw subfolders', 'Remove or rename')
        elif top == 'wiki':
            for fn in filenames:
                if fn != 'wiki.md' and not fn.startswith('.'):
                    add_issue(os.path.join(rel, fn), 'ERROR', 'Path', 'File not allowed at wiki/ root', fn, 'Only wiki.md', 'Move to subfolder or remove')
            for dn in dirnames:
                if dn not in wiki_allowed_dirs:
                    add_issue(os.path.join(rel, dn), 'ERROR', 'Path', 'Subfolder not allowed in wiki/', dn, 'One of allowed wiki subfolders', 'Remove or rename')
        continue
    
    # Depth 2
    if len(parts) == 2:
        top, sub = parts[0], parts[1]
        if top == 'raw' and sub in raw_allowed_dirs:
            index_name = f'{sub}.md'
            if index_name not in filenames:
                add_issue(os.path.join(rel, f'MISSING {index_name}'), 'ERROR', 'Path', f'Missing index file in raw/{sub}/', 'none', index_name, f'Create {index_name}')
            for fn in filenames:
                if fn == index_name or fn.startswith('.'):
                    continue
                if not re.match(r'^\d{4}-\d{2}-\d{2}_[a-z0-9\-]+\.md$', fn):
                    add_issue(os.path.join(rel, fn), 'WARNING', 'Naming', f'File naming convention violated in raw/{sub}/', fn, 'YYYY-MM-DD_<slug>.md (lowercase, hyphens)', 'Rename to match convention')
            for dn in dirnames:
                add_issue(os.path.join(rel, dn), 'ERROR', 'Path', f'No nested folders in raw/{sub}/', dn, 'Flat structure only', 'Move files up or remove folder')
        elif top == 'wiki':
            if sub == 'meta':
                allowed_meta = {'format-spec.md', 'folder-structure.md', 'index-spec.md'}
                for fn in filenames:
                    if fn not in allowed_meta and not fn.startswith('.'):
                        add_issue(os.path.join(rel, fn), 'ERROR', 'Path', 'Extra file in wiki/meta/', fn, 'Only format-spec.md, folder-structure.md, index-spec.md', 'Remove')
                for dn in dirnames:
                    add_issue(os.path.join(rel, dn), 'ERROR', 'Path', 'No subfolders in wiki/meta/', dn, 'None', 'Remove')
            elif sub == 'sources':
                for fn in filenames:
                    if fn.startswith('.'):
                        continue
                    if not re.match(r'^src_[a-z0-9\-]+\.md$', fn):
                        add_issue(os.path.join(rel, fn), 'WARNING', 'Naming', 'Source file naming convention violated', fn, 'src_<slug>.md (lowercase, hyphens)', 'Rename')
            elif sub == 'concepts':
                for fn in filenames:
                    if fn.startswith('.'):
                        continue
                    if not re.match(r'^[a-z0-9\-]+\.md$', fn):
                        add_issue(os.path.join(rel, fn), 'WARNING', 'Naming', 'Concept file naming convention violated', fn, '<concept-slug>.md (lowercase, hyphens)', 'Rename')
            elif sub == 'tag':
                for fn in filenames:
                    if fn.startswith('.'):
                        continue
                    if fn == 'tag.md':
                        continue
                    if not re.match(r'^[a-z0-9\-]+\.md$', fn):
                        add_issue(os.path.join(rel, fn), 'WARNING', 'Naming', 'Tag file naming convention violated', fn, '<tag>.md (lowercase, hyphens)', 'Rename')
            elif sub == 'topic':
                for fn in filenames:
                    if fn.startswith('.'):
                        continue
                    if not re.match(r'^[a-z0-9\-]+\.md$', fn):
                        add_issue(os.path.join(rel, fn), 'WARNING', 'Naming', 'Topic file naming convention violated', fn, '<topic>.md (lowercase, hyphens)', 'Rename')
            elif sub == 'drafts':
                for fn in filenames:
                    if fn.startswith('.'):
                        continue
                    if not re.match(r'^[a-z0-9\-]+\.md$', fn):
                        add_issue(os.path.join(rel, fn), 'WARNING', 'Naming', 'Draft file naming convention violated', fn, '<slug>.md (lowercase, hyphens)', 'Rename')
            elif sub == 'reviews':
                for fn in filenames:
                    if fn.startswith('.'):
                        continue
                    if fn in {'_action-required.md', 'HEARTBEAT.md'}:
                        continue
                    if not re.match(r'^\d{4}-\d{2}-\d{2}_(format|output|hygiene)-report(|-v2)?\.md$', fn):
                        add_issue(os.path.join(rel, fn), 'WARNING', 'Naming', 'Review file naming convention violated', fn, 'YYYY-MM-DD_<type>-report.md', 'Rename or archive')
                for dn in dirnames:
                    if dn == 'archive':
                        continue
                    else:
                        add_issue(os.path.join(rel, dn), 'ERROR', 'Path', 'Unexpected folder in wiki/reviews/', dn, 'Only archive/ allowed', 'Remove')
        continue
    
    # Depth 3: archive/
    if len(parts) == 3 and parts[0] == 'wiki' and parts[1] == 'reviews' and parts[2] == 'archive':
        for fn in filenames:
            if fn.startswith('.'):
                continue
            add_issue(os.path.join(rel, fn), 'INFO', 'Orphan', 'File directly in archive/', fn, 'Should be in archive/YYYY-MM/', 'Move to month subfolder')
        for dn in dirnames:
            if not re.match(r'^\d{4}-\d{2}$', dn):
                add_issue(os.path.join(rel, dn), 'WARNING', 'Naming', 'Archive subfolder naming convention violated', dn, 'YYYY-MM', 'Rename')
        continue
    
    # Depth 4: archive/YYYY-MM/
    if len(parts) == 4 and parts[0] == 'wiki' and parts[1] == 'reviews' and parts[2] == 'archive':
        for fn in filenames:
            if fn.startswith('.'):
                continue
            if not re.match(r'^\d{4}-\d{2}-\d{2}_(format|output|hygiene)-report(|-v2)?\.md$', fn):
                add_issue(os.path.join(rel, fn), 'WARNING', 'Naming', 'Archived report naming convention violated', fn, 'YYYY-MM-DD_<type>-report.md', 'Rename')
        continue

# Explicit checks for root-level orphans (deduplicated via seen set)
for fn in ['RAW_BACKLOG.md', 'MEMORY.md']:
    if os.path.exists(os.path.join(root, fn)):
        add_issue(fn, 'ERROR', 'Path', 'File not in root whitelist', fn, 'One of allowed root files', 'Move to wiki/drafts/ or raw/ and remove')

for dn in ['search', 'state', 'temp_content', 'memory']:
    if os.path.isdir(os.path.join(root, dn)):
        add_issue(dn + '/', 'ERROR', 'Path', 'Folder not in root whitelist', dn, 'Allowed root folders', 'Remove or update folder-structure.md')

if os.path.exists(os.path.join(root, 'raw', '.last_heartbeat')):
    add_issue('raw/.last_heartbeat', 'ERROR', 'Path', 'Hidden file not allowed at raw/ root', 'raw/.last_heartbeat', 'Only raw.md allowed', 'Remove')

if os.path.exists(os.path.join(root, 'wiki', 'reviews', 'HEARTBEAT.md')):
    add_issue('wiki/reviews/HEARTBEAT.md', 'ERROR', 'Path', 'File not allowed in wiki/reviews/', 'HEARTBEAT.md', '_action-required.md, reports, archive/', 'Remove (should be in .hermes/ or root)')

# Summary
error_count = sum(1 for i in issues if i['severity'] == 'ERROR')
warning_count = sum(1 for i in issues if i['severity'] == 'WARNING')
info_count = sum(1 for i in issues if i['severity'] == 'INFO')

print(f"PATHS_CHECKED={paths_checked}")
print(f"TOTAL={len(issues)}")
print(f"ERROR={error_count}")
print(f"WARNING={warning_count}")
print(f"INFO={info_count}")
for i in issues:
    print(f"SEV={i['severity']}|CAT={i['category']}|PATH={i['path']}|ISSUE={i['issue']}|CURRENT={i['current']}|EXPECTED={i['expected']}|FIX={i['suggested_fix']}")
