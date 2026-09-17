#!/usr/bin/env python3
"""
Spot-check validator for Knowledge Base pre-promotion checks.
Scans a specific batch (by mtime) and reports issues.
Run from knowledge-base root: python3 references/spot-check-validator.py
"""

import os
import re
import yaml
from datetime import datetime
from pathlib import Path

os.chdir('/home/julius/knowledge-base')

# Ground truth — ALWAYS read TAGS.md, do NOT hardcode
POOL_A = {'ai', 'crypto', 'tech', 'productivity', 'system', 'economic', 'politic'}
POOL_B = {'hack', 'tools', 'automation', 'vibecode', 'research', 'tutorial', 'opinion', 'news', 'defi', 'perpdex', 'layer1', 'layer2', 'law', 'coding', 'psychology', 'health'}
VALID_STATUS = {'draft', 'reviewed', 'needs-revision'}

def check_frontmatter(content, fname, ftype):
    """Validate frontmatter. Returns (fm_dict, issues_list)."""
    issues = []
    if not content.startswith('---'):
        return None, [(fname, 'ERROR', 'Frontmatter', 'Missing frontmatter opener')]
    try:
        parts = content.split('---', 2)
        if len(parts) < 3:
            return None, [(fname, 'ERROR', 'Frontmatter', 'Incomplete frontmatter')]
        fm = yaml.safe_load(parts[1])
    except Exception as e:
        return None, [(fname, 'ERROR', 'Frontmatter', f'Invalid YAML: {e}')]
    if fm is None:
        return None, [(fname, 'ERROR', 'Frontmatter', 'Empty frontmatter')]

    # Type
    if fm.get('type') != ftype:
        issues.append((fname, 'ERROR', 'Frontmatter', f"type mismatch: expected {ftype}, got {fm.get('type')}"))

    # Status (concept ONLY — sources do NOT have status)
    if ftype == 'concept':
        status = fm.get('status')
        if status not in VALID_STATUS:
            issues.append((fname, 'ERROR', 'Frontmatter', f'Invalid status: {status}'))

    # main_tag
    main_tag = fm.get('main_tag')
    if main_tag not in POOL_A:
        issues.append((fname, 'ERROR', 'Frontmatter', f'Invalid main_tag: {main_tag}'))

    # sub_tags
    sub_tags = fm.get('sub_tags')
    if isinstance(sub_tags, list):
        if len(sub_tags) < 1 or len(sub_tags) > 3:
            issues.append((fname, 'ERROR', 'Frontmatter', f'sub_tags count: {len(sub_tags)}'))
        for tag in sub_tags:
            if tag not in POOL_B:
                issues.append((fname, 'ERROR', 'Frontmatter', f'Invalid sub_tag: {tag}'))
            if tag in POOL_A:
                issues.append((fname, 'WARNING', 'Frontmatter', f'main_tag in sub_tags: {tag}'))
    elif isinstance(sub_tags, str):
        issues.append((fname, 'ERROR', 'Frontmatter', f'sub_tags is string: {sub_tags}'))
    else:
        issues.append((fname, 'ERROR', 'Frontmatter', 'sub_tags missing or wrong type'))

    # Duplicate sub_tags
    raw_fm = parts[1]
    if raw_fm.count('sub_tags:') > 1:
        issues.append((fname, 'ERROR', 'Frontmatter', 'Duplicate sub_tags field'))

    # Field order
    if ftype == 'concept':
        expected = ['type', 'status', 'main_tag', 'sub_tags', 'topic', 'sources', 'last_updated']
    else:
        expected = ['type', 'original', 'main_tag', 'sub_tags', 'topic', 'date_compiled']
    fm_lines = [l.strip() for l in raw_fm.split('\n') if l.strip() and not l.strip().startswith('#')]
    actual_keys = []
    for line in fm_lines:
        if ':' in line and not line.startswith('-'):
            key = line.split(':')[0].strip()
            if key in expected:
                actual_keys.append(key)
    filtered = [k for k in expected if k in actual_keys]
    if actual_keys != filtered:
        issues.append((fname, 'WARNING', 'Frontmatter', f'Field order off: {actual_keys}'))

    # original field (source only)
    if ftype == 'source':
        original = fm.get('original', '')
        if isinstance(original, str) and '.md' in original:
            issues.append((fname, 'ERROR', 'Frontmatter', f'original has .md: {original}'))

    return fm, issues

def check_sections(content, fname, required_sections):
    """Check required sections exist."""
    issues = []
    headers = re.findall(r'^## (.+)$', content, re.MULTILINE)
    for sec in required_sections:
        if not any(sec.lower() in h.lower() for h in headers):
            issues.append((fname, 'ERROR', 'Sections', f'Missing section: {sec}'))
    return issues

def check_content(content, fname, ftype):
    """Content quality checks."""
    issues = []
    # Key ideas / Key points — count BOTH bullets AND numbered items
    if ftype == 'concept':
        key_match = re.search(r'## Key ideas\n\n(.+?)(?=\n## |\Z)', content, re.DOTALL)
    else:
        key_match = re.search(r'## Key points\n\n(.+?)(?=\n## |\Z)', content, re.DOTALL)
    if key_match:
        key_sec = key_match.group(1).strip()
        bullets = re.findall(r'^[\s]*[-*][\s]+', key_sec, re.MULTILINE)
        numbered = re.findall(r'^[\s]*\d+\.[\s]+', key_sec, re.MULTILINE)
        total = len(bullets) + len(numbered)
        if total == 0 and len(key_sec) > 0:
            issues.append((fname, 'WARNING', 'Content', 'Key section has 0 items'))
        elif total > 0 and total < 3:
            issues.append((fname, 'INFO', 'Content', f'Key section has only {total} items'))

    # Sources section (concept)
    if ftype == 'concept':
        sources_match = re.search(r'## Sources\n\n(.+?)(?=\n## |\Z)', content, re.DOTALL)
        if sources_match:
            sources_sec = sources_match.group(1).strip()
            if not sources_sec:
                issues.append((fname, 'ERROR', 'Content', 'Empty Sources section'))

    # Vietnamese check
    vn_chars = set('àáạảãâầấậẩẫăằắặẳẵèéẹẻẽêềếệểễìíịỉĩòóọỏõôồốộổỗơờớợởỡùúụủũưừứựửữỳýỵỷỹđ')
    text = re.sub(r'[#*\-\[\]\(\)\|`]', '', content)
    has_vn = any(c in vn_chars for c in text.lower())
    if not has_vn and len(text) > 200:
        issues.append((fname, 'INFO', 'Content', 'English-only content'))

    return issues

def main():
    start_ts = datetime(2026, 6, 14, 0, 0).timestamp()
    end_ts = datetime(2026, 6, 16, 0, 0).timestamp()

    concepts_dir = Path('wiki/concepts')
    sources_dir = Path('wiki/sources')

    batch_concepts = [f for f in concepts_dir.glob('*.md') if start_ts <= os.path.getmtime(f) < end_ts]
    batch_sources = [f for f in sources_dir.glob('*.md') if start_ts <= os.path.getmtime(f) < end_ts]

    print(f"Spot-check batch: {len(batch_concepts)} concepts + {len(batch_sources)} sources")

    all_issues = []
    status_counts = {'draft': 0, 'reviewed': 0, 'needs-revision': 0}

    for f in batch_concepts:
        content = f.read_text()
        fm, issues = check_frontmatter(content, f.name, 'concept')
        all_issues.extend(issues)
        if fm and fm.get('status') in status_counts:
            status_counts[fm['status']] += 1
        if fm:
            all_issues.extend(check_sections(content, f.name, ['Definition', 'Key ideas', 'Related concepts', 'Sources']))
            all_issues.extend(check_content(content, f.name, 'concept'))

    for f in batch_sources:
        content = f.read_text()
        fm, issues = check_frontmatter(content, f.name, 'source')
        all_issues.extend(issues)
        if fm:
            all_issues.extend(check_sections(content, f.name, ['Metadata', 'Summary', 'Key points', 'Concepts referenced']))
            all_issues.extend(check_content(content, f.name, 'source'))

    errors = [i for i in all_issues if i[1] == 'ERROR']
    warnings = [i for i in all_issues if i[1] == 'WARNING']
    infos = [i for i in all_issues if i[1] == 'INFO']

    print(f"\nERROR: {len(errors)}")
    for f, sev, cat, msg in errors:
        print(f"  [{f}] {cat}: {msg}")
    print(f"\nWARNING: {len(warnings)}")
    for f, sev, cat, msg in warnings:
        print(f"  [{f}] {cat}: {msg}")
    print(f"\nINFO: {len(infos)}")
    for f, sev, cat, msg in infos:
        print(f"  [{f}] {cat}: {msg}")

    print(f"\nStatus audit: {status_counts}")
    print(f"\nVerdict:", end=' ')
    if errors:
        print("REJECT")
    elif warnings:
        print("REVISE")
    else:
        print("PROMOTE")

if __name__ == '__main__':
    main()
