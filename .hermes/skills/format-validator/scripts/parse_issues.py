#!/usr/bin/env python3
"""Parse format-validator validate.py output and produce analysis statistics.

Usage:
  cd /home/julius/knowledge-base
  python3 .hermes/skills/format-validator/scripts/validate.py 2>&1 | tee /tmp/issues.txt
  python3 .hermes/skills/format-validator/scripts/parse_issues.py /tmp/issues.txt

Output:
  - Header stats (files checked, error/warning/info counts)
  - Broken wikilink analysis: unique targets, top-N list
  - Forward-reference summary groups count
  - Top files by warning count
  - ERROR file breakdown (topic vs tag vs other)
"""

import re, sys
from collections import Counter

def parse(filepath):
    with open(filepath) as f:
        raw = f.read()

    # Parse header
    header = {}
    for line in raw.split('\n'):
        if '=' in line and '---' not in line:
            k, v = line.split('=', 1)
            header[k.strip()] = v.strip()
        if line.startswith('---ISSUES_BEGIN---'):
            break

    print(f"=== HEADER ===")
    for k, v in header.items():
        print(f"  {k}: {v}")

    # Get issue lines
    issue_start = raw.index('---ISSUES_BEGIN---') + len('---ISSUES_BEGIN---\n')
    issue_end = raw.index('---ISSUES_END---')
    issue_lines = [l.strip() for l in raw[issue_start:issue_end].split('\n') if l.strip()]

    errors = [l for l in issue_lines if l.startswith('ERROR|')]
    warnings = [l for l in issue_lines if l.startswith('WARNING|')]
    infos = [l for l in issue_lines if l.startswith('INFO|')]

    # Categorize warnings
    broken_wikilinks = []
    forward_refs = []
    other_warnings = []
    for w in warnings:
        parts = w.split('|')
        if len(parts) >= 4:
            msg = parts[3]
            if 'broken wikilinks (forward-references' in msg:
                forward_refs.append((parts[2], msg))
            elif 'Broken wikilink:' in msg:
                broken_wikilinks.append((parts[2], msg))
            else:
                other_warnings.append(w)

    # Count broken targets
    target_counter = Counter()
    for _, msg in broken_wikilinks:
        m = re.search(r'\[\[(.+?)\]\]', msg)
        if m:
            target_counter[m.group(1)] += 1

    print(f"\n=== SUMMARY ===")
    print(f"  ERRORs:   {len(errors)}")
    print(f"  WARNINGs: {len(warnings)}")
    print(f"    - Individual broken wikilinks: {len(broken_wikilinks)}")
    print(f"    - Forward-reference groups:    {len(forward_refs)}")
    print(f"    - Other warnings:              {len(other_warnings)}")
    print(f"  INFOs:    {len(infos)}")
    print(f"  Unique broken targets: {len(target_counter)}")

    # Top broken targets
    print(f"\n=== TOP 20 BROKEN TARGETS ===")
    for t, c in target_counter.most_common(20):
        print(f"  [[{t}]]: {c}x")

    # ERROR file breakdown
    topic_errors = [l for l in errors if 'wiki/topic/' in l]
    tag_errors = [l for l in errors if 'wiki/tag/' in l]
    other_errors = [l for l in errors if 'wiki/topic/' not in l and 'wiki/tag/' not in l]
    print(f"\n=== ERROR BREAKDOWN ===")
    print(f"  Topic file ERRORs: {len(topic_errors)}")
    print(f"  Tag file ERRORs:   {len(tag_errors)}")
    print(f"  Other ERRORs:      {len(other_errors)}")
    if topic_errors:
        # Show first 3 examples
        print(f"  Topic examples:")
        for e in topic_errors[:3]:
            parts = e.split('|')
            print(f"    {parts[2] if len(parts) >= 3 else '?'} — {parts[3] if len(parts) >= 4 else '?'}")

    # Top files by warning count
    warn_file_counter = Counter()
    for w in warnings:
        parts = w.split('|')
        if len(parts) >= 3:
            warn_file_counter[parts[2]] += 1
    print(f"\n=== TOP 10 FILES BY WARNING COUNT ===")
    for f, c in warn_file_counter.most_common(10):
        print(f"  {f}: {c}")

    # Forward-reference details
    if forward_refs:
        print(f"\n=== FORWARD-REFERENCE SUMMARY GROUPS ({len(forward_refs)}) ===")
        for fpath, msg in forward_refs[:5]:
            print(f"  {fpath}: {msg}")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: parse_issues.py <issues_file>")
        sys.exit(1)
    parse(sys.argv[1])
